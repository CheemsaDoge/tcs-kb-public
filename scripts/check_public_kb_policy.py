#!/usr/bin/env python3
"""Policy guard for tcs-kb-public.

This script is intentionally local and dependency-light. It scans public KB YAML
records for policy mistakes that validation and gate checks should not be asked
to catch by themselves.
"""

from __future__ import annotations

import argparse
import shutil
import sys
import tempfile
from pathlib import Path
from typing import Any

import yaml


PRIVATE_MARKERS = (
    "private conjecture",
    "private note",
    "private notes",
    "private proof",
    "private workspace",
    "unpublished research",
    "unpublished idea",
    "work-in-progress private",
)

CHECKED_STATUSES = {"checked"}
SKIPPED_STATUSES = {"skipped"}
PASS_STATUSES = {"pass", "passed", "ok", "success"}
NON_HUMAN_AUTHORITY_MARKERS = (
    "agent",
    "ai",
    "chatgpt",
    "codex",
    "llm",
    "mcp",
    "model",
    "operator",
    "provider",
    "workflow",
)
OPERATOR_HANDOFF_SOURCE_MARKERS = (
    "operator handoff",
    "operator_handoff",
    "operator-session",
    "operator session",
    "reviews/operator",
)
RESEARCH_LOOP_SOURCE_MARKERS = (
    ".cosheaf/research-loops",
    "attempt memory",
    "attempt-memory",
    "research loop",
    "research-loop",
    "research_loop",
    "retry_justification",
)
WORKFLOW_SOURCE_MARKERS = (
    ".cosheaf/workflows",
    "research workflow",
    "reviewable workflow",
    "workflow output",
    "workflow record",
    "workflow_output",
)
OPERATOR_HANDOFF_FORBIDDEN_MARKERS = (
    ".env",
    "api key",
    "api_key",
    "authorization:",
    "bearer ",
    "chain of thought",
    "chain-of-thought",
    "context/tasks/",
    "environment dump",
    "hidden reasoning",
    "kb/private",
    "private workspace",
    "private_research",
    "provider request",
    "provider response",
    "provider_request",
    "provider_response",
    "raw provider",
    "\\private\\",
    "/private/",
)
RESEARCH_LOOP_FORBIDDEN_MARKERS = OPERATOR_HANDOFF_FORBIDDEN_MARKERS + (
    "accepted proof",
    "accepted_proof",
    "source metadata created",
    "source_metadata_created",
)
OPERATOR_HANDOFF_FALSE_AUTHORITY_KEYS = (
    "accepted_proof_created",
    "accepted_status_claimed",
    "accepted_write_performed",
    "gate_result_mutated",
    "gate_pass_created",
    "human_review_created",
    "promotion_performed",
    "source_metadata_created",
    "verifier_result_mutated",
    "verifier_pass_created",
)
REVIEW_AUTHORITY_KEYS = (
    "actor_kind",
    "created_by",
    "created_with",
    "origin",
    "review_kind",
    "review_source",
    "reviewer",
    "reviewer_kind",
    "reviewed_by",
    "source",
    "source_kind",
)
VERIFIER_AUTHORITY_KEYS = (
    "actor_kind",
    "checker_kind",
    "created_by",
    "created_with",
    "origin",
    "provider",
    "source",
    "source_kind",
    "tool",
    "tool_name",
)


class PolicyError:
    def __init__(self, path: Path, message: str) -> None:
        self.path = path
        self.message = message

    def __str__(self) -> str:
        return f"{self.path}: {self.message}"


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path} did not contain a YAML mapping")
    return data


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def string_values(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, dict):
        values: list[str] = []
        for item in value.values():
            values.extend(string_values(item))
        return values
    if isinstance(value, list):
        values = []
        for item in value:
            values.extend(string_values(item))
        return values
    return []


def string_values_and_keys(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, dict):
        values: list[str] = []
        for key, item in value.items():
            values.append(str(key))
            values.extend(string_values_and_keys(item))
        return values
    if isinstance(value, list):
        values = []
        for item in value:
            values.extend(string_values_and_keys(item))
        return values
    if value is None:
        return []
    return [str(value)]


def value_has_nonhuman_authority_marker(value: Any) -> bool:
    text = "\n".join(string_values(value)).lower()
    return any(marker in text for marker in NON_HUMAN_AUTHORITY_MARKERS)


def has_source_metadata(record: dict[str, Any]) -> bool:
    sources = record.get("sources")
    if not isinstance(sources, list) or not sources:
        return False
    for source in sources:
        if not isinstance(source, dict):
            continue
        if source.get("kind") and source.get("title") and source.get("authors"):
            locator = source.get("page") or source.get("theorem_number") or source.get("url") or source.get("doi")
            if locator:
                return True
    return False


def operator_handoff_claimed_as_source_metadata(record: dict[str, Any]) -> bool:
    sources = record.get("sources")
    if not isinstance(sources, list):
        return False
    for source in sources:
        if not isinstance(source, dict):
            continue
        text = "\n".join(string_values_and_keys(source)).lower()
        if any(marker in text for marker in OPERATOR_HANDOFF_SOURCE_MARKERS):
            return True
    return False


def research_loop_claimed_as_source_metadata(record: dict[str, Any]) -> bool:
    sources = record.get("sources")
    if not isinstance(sources, list):
        return False
    for source in sources:
        if not isinstance(source, dict):
            continue
        text = "\n".join(string_values_and_keys(source)).lower()
        if any(marker in text for marker in RESEARCH_LOOP_SOURCE_MARKERS):
            return True
    return False


def workflow_claimed_as_source_metadata(record: dict[str, Any]) -> bool:
    sources = record.get("sources")
    if not isinstance(sources, list):
        return False
    for source in sources:
        if not isinstance(source, dict):
            continue
        text = "\n".join(string_values_and_keys(source)).lower()
        if any(marker in text for marker in WORKFLOW_SOURCE_MARKERS):
            return True
    return False


def research_loop_claimed_as_accepted_proof(record: dict[str, Any]) -> bool:
    status = str(record.get("status", "")).lower()
    artifact_type = str(record.get("type", "")).lower()
    if status != "accepted" or artifact_type not in {"proof", "proof-sketch", "theorem"}:
        return False
    text = "\n".join(string_values_and_keys(record)).lower()
    return any(marker in text for marker in RESEARCH_LOOP_SOURCE_MARKERS) and (
        "accepted proof" in text
        or "accepted_proof" in text
        or "proof authority" in text
        or "proves the theorem" in text
    )


def workflow_claimed_as_accepted_proof(record: dict[str, Any]) -> bool:
    status = str(record.get("status", "")).lower()
    artifact_type = str(record.get("type", "")).lower()
    if status != "accepted" or artifact_type not in {"proof", "proof-sketch", "theorem"}:
        return False
    text = "\n".join(string_values_and_keys(record)).lower()
    return any(marker in text for marker in WORKFLOW_SOURCE_MARKERS) and (
        "accepted proof" in text
        or "accepted_proof" in text
        or "proof authority" in text
        or "proves the theorem" in text
    )


def has_human_review(record: dict[str, Any]) -> bool:
    review = record.get("review")
    return isinstance(review, dict) and review.get("state") == "human_reviewed"


def nonhuman_output_claimed_as_human_review(record: dict[str, Any]) -> bool:
    review = record.get("review")
    if not isinstance(review, dict) or review.get("state") != "human_reviewed":
        return False
    for key in REVIEW_AUTHORITY_KEYS:
        if key in review and value_has_nonhuman_authority_marker(review[key]):
            return True
    return False


def has_private_dependency(record: dict[str, Any]) -> bool:
    for dep in as_list(record.get("depends_on")):
        dep_text = str(dep).lower()
        if dep_text.startswith("private:") or "/private/" in dep_text or "\\private\\" in dep_text:
            return True
    return False


def has_private_marker(path: Path, record: dict[str, Any]) -> bool:
    path_text = path.as_posix().lower()
    if "/private/" in path_text or path_text.startswith("private/"):
        return True
    tags = [str(tag).lower() for tag in as_list(record.get("tags"))]
    if any(tag in {"private", "private-workspace", "unpublished"} for tag in tags):
        return True
    checked_fields = {
        "title": record.get("title"),
        "statement": record.get("statement"),
        "evidence": record.get("evidence"),
        "review": record.get("review"),
        "risk": record.get("risk"),
    }
    text = "\n".join(string_values(checked_fields)).lower()
    return any(marker in text for marker in PRIVATE_MARKERS)


def verifier_results(record: dict[str, Any]) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for key in ("verifier_results", "verification_results", "verifications"):
        value = record.get(key)
        if isinstance(value, list):
            results.extend(item for item in value if isinstance(item, dict))
        elif isinstance(value, dict):
            results.append(value)
    policy = record.get("verification_policy")
    if isinstance(policy, dict):
        for key in ("result", "results", "verifier_result", "verifier_results"):
            value = policy.get(key)
            if isinstance(value, list):
                results.extend(item for item in value if isinstance(item, dict))
            elif isinstance(value, dict):
                results.append(value)
    return results


def skipped_treated_as_pass(record: dict[str, Any]) -> bool:
    for result in verifier_results(record):
        status = str(result.get("status", "")).lower()
        verdict = str(result.get("verdict", "")).lower()
        conclusion = str(result.get("conclusion", "")).lower()
        if status in SKIPPED_STATUSES and (verdict in PASS_STATUSES or conclusion in PASS_STATUSES):
            return True
        if status in PASS_STATUSES and str(result.get("tool_status", "")).lower() in SKIPPED_STATUSES:
            return True
    return False


def nonhuman_output_claimed_as_verifier_pass(record: dict[str, Any]) -> bool:
    for result in verifier_results(record):
        status = str(result.get("status", "")).lower()
        verdict = str(result.get("verdict", "")).lower()
        conclusion = str(result.get("conclusion", "")).lower()
        if not (
            status in PASS_STATUSES
            or verdict in PASS_STATUSES
            or conclusion in PASS_STATUSES
        ):
            continue
        for key in VERIFIER_AUTHORITY_KEYS:
            if key in result and value_has_nonhuman_authority_marker(result[key]):
                return True
    return False


def checked_formalization_without_evidence(record: dict[str, Any]) -> bool:
    for formalization in as_list(record.get("formalizations")):
        if not isinstance(formalization, dict):
            continue
        if str(formalization.get("status", "")).lower() not in CHECKED_STATUSES:
            continue
        evidence_keys = (
            "checker_evidence",
            "check_result",
            "checked_at",
            "stdout",
            "stderr",
            "log_path",
            "command",
            "exit_code",
        )
        if not any(formalization.get(key) not in (None, "", []) for key in evidence_keys):
            return True
    return False


def truthy_authority_value(value: Any) -> bool:
    if value is True:
        return True
    if isinstance(value, str):
        return value.strip().lower() in {"true", "yes", "1"}
    return False


def has_true_operator_handoff_authority_field(value: Any) -> bool:
    if isinstance(value, dict):
        for key, item in value.items():
            if key in OPERATOR_HANDOFF_FALSE_AUTHORITY_KEYS and truthy_authority_value(item):
                return True
            if has_true_operator_handoff_authority_field(item):
                return True
    elif isinstance(value, list):
        return any(has_true_operator_handoff_authority_field(item) for item in value)
    return False


def operator_handoff_has_forbidden_marker(record: dict[str, Any]) -> bool:
    text = "\n".join(string_values_and_keys(record)).lower()
    return any(marker in text for marker in OPERATOR_HANDOFF_FORBIDDEN_MARKERS)


def check_operator_handoff_record(path: Path, record: dict[str, Any]) -> list[PolicyError]:
    errors: list[PolicyError] = []
    if record.get("review_context_only") is not True:
        errors.append(PolicyError(path, "operator handoff is not marked review_context_only"))
    if has_true_operator_handoff_authority_field(record):
        errors.append(PolicyError(path, "operator handoff claims accepted/review/promotion authority"))
    if operator_handoff_has_forbidden_marker(record):
        errors.append(
            PolicyError(path, "operator handoff contains private, secret, reasoning, or provider-payload marker")
        )
    return errors


def research_loop_has_forbidden_marker(record: dict[str, Any]) -> bool:
    text = "\n".join(string_values_and_keys(record)).lower()
    return any(marker in text for marker in RESEARCH_LOOP_FORBIDDEN_MARKERS)


def check_research_loop_record(path: Path, record: dict[str, Any]) -> list[PolicyError]:
    errors: list[PolicyError] = []
    if record.get("review_context_only") is not True:
        errors.append(PolicyError(path, "research loop output is not marked review_context_only"))
    if has_true_operator_handoff_authority_field(record):
        errors.append(PolicyError(path, "research loop output claims accepted/review/promotion authority"))
    if research_loop_has_forbidden_marker(record):
        errors.append(
            PolicyError(path, "research loop output contains private, secret, proof, source, reasoning, or provider-payload marker")
        )
    return errors


def check_record(path: Path, record: dict[str, Any]) -> list[PolicyError]:
    errors: list[PolicyError] = []
    status = str(record.get("status", "")).lower()
    if status == "accepted":
        if not has_source_metadata(record):
            errors.append(PolicyError(path, "accepted artifact is missing source metadata"))
        if not has_human_review(record):
            errors.append(PolicyError(path, "accepted artifact is missing human review metadata"))
        if operator_handoff_claimed_as_source_metadata(record):
            errors.append(
                PolicyError(path, "operator handoff is claimed as source metadata")
            )
        if research_loop_claimed_as_source_metadata(record):
            errors.append(
                PolicyError(path, "research loop output is claimed as source metadata")
            )
        if workflow_claimed_as_source_metadata(record):
            errors.append(
                PolicyError(path, "workflow output is claimed as source metadata")
            )
        if research_loop_claimed_as_accepted_proof(record):
            errors.append(
                PolicyError(path, "research loop output is claimed as accepted proof")
            )
        if workflow_claimed_as_accepted_proof(record):
            errors.append(
                PolicyError(path, "workflow output is claimed as accepted proof")
            )
        if nonhuman_output_claimed_as_human_review(record):
            errors.append(
                PolicyError(path, "operator, workflow, or model output is claimed as human review")
            )
    if has_private_dependency(record):
        errors.append(PolicyError(path, "public artifact depends on a private artifact"))
    if skipped_treated_as_pass(record):
        errors.append(PolicyError(path, "skipped verifier result is treated as pass"))
    if nonhuman_output_claimed_as_verifier_pass(record):
        errors.append(
            PolicyError(path, "operator or model output is claimed as verifier pass")
        )
    if checked_formalization_without_evidence(record):
        errors.append(PolicyError(path, "checked formalization lacks checker evidence"))
    if has_private_marker(path, record):
        errors.append(PolicyError(path, "public KB artifact contains private-looking marker"))
    return errors


def iter_yaml_files(kb_root: Path) -> list[Path]:
    if not kb_root.exists():
        return []
    return sorted(path for path in kb_root.rglob("*.yaml") if path.is_file())


def check_repository(repo_root: Path) -> list[PolicyError]:
    kb_root = repo_root / "kb" / "public"
    errors: list[PolicyError] = []
    for path in iter_yaml_files(kb_root):
        try:
            record = load_yaml(path)
        except Exception as exc:  # pragma: no cover - surfaced through CLI
            errors.append(PolicyError(path, f"could not load YAML: {exc}"))
            continue
        errors.extend(check_record(path, record))
    operator_review_root = repo_root / "reviews" / "operator"
    for path in iter_yaml_files(operator_review_root):
        try:
            record = load_yaml(path)
        except Exception as exc:  # pragma: no cover - surfaced through CLI
            errors.append(PolicyError(path, f"could not load YAML: {exc}"))
            continue
        errors.extend(check_operator_handoff_record(path, record))
    research_loop_review_root = repo_root / "reviews" / "research-loop"
    for path in iter_yaml_files(research_loop_review_root):
        try:
            record = load_yaml(path)
        except Exception as exc:  # pragma: no cover - surfaced through CLI
            errors.append(PolicyError(path, f"could not load YAML: {exc}"))
            continue
        errors.extend(check_research_loop_record(path, record))
    return errors


def write_fixture(root: Path, name: str, body: str) -> Path:
    path = root / "kb" / "public" / "accepted" / "definitions" / f"{name}.yaml"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")
    return path


def good_artifact() -> str:
    return """\
id: definition.good
type: definition
title: Good
domain:
- graph-theory
status: accepted
created_at: '2026-06-06T00:00:00Z'
updated_at: '2026-06-06T00:00:00Z'
authors:
- TCS-Cosheaf contributors
depends_on: []
statement: A good fixture is a public test artifact.
sources:
- kind: book
  title: Public Source
  authors:
  - Example Author
  year: 2026
  url: https://example.invalid/source
  page: Section 1
review:
  state: human_reviewed
  notes: Test fixture review.
formalizations:
- id: good.planned
  status: planned
  system: lean4
verification_policy:
  require_lean_check: false
"""


def bad_artifact(case: str) -> str:
    base = yaml.safe_load(good_artifact())
    assert isinstance(base, dict)
    if case == "missing_sources":
        base.pop("sources", None)
    elif case == "missing_human_review":
        base["review"] = {"state": "requested"}
    elif case == "private_dependency":
        base["depends_on"] = ["private:claim.secret"]
    elif case == "skipped_as_pass":
        base["verifier_results"] = [{"status": "skipped", "verdict": "pass"}]
    elif case == "operator_as_human_review":
        base["review"] = {
            "state": "human_reviewed",
            "reviewer_kind": "mcp_operator",
            "notes": "This fixture tries to spoof human review.",
        }
    elif case == "operator_as_verifier_pass":
        base["verifier_results"] = [
            {
                "status": "pass",
                "tool": "codex-mcp-operator",
                "notes": "This fixture tries to spoof checker authority.",
            }
        ]
    elif case == "checked_without_evidence":
        base["formalizations"] = [{"id": "bad.checked", "status": "checked", "system": "lean4"}]
    elif case == "private_marker":
        base["tags"] = ["private"]
    elif case == "operator_handoff_as_source":
        base["sources"] = [
            {
                "kind": "operator_handoff",
                "title": "Operator handoff review context",
                "authors": ["workspace operator"],
                "year": 2026,
                "url": "reviews/operator/handoff.example.yaml",
            }
        ]
    elif case == "research_loop_as_source":
        base["sources"] = [
            {
                "kind": "research_loop",
                "title": "Research loop review context",
                "authors": ["workspace operator"],
                "year": 2026,
                "url": "reviews/research-loop/loop.example.yaml",
            }
        ]
    elif case == "research_loop_as_accepted_proof":
        base["type"] = "proof"
        base["title"] = "Bad research-loop proof"
        base["statement"] = "The research loop output is accepted proof and proves the theorem."
        base["evidence"] = [
            {
                "kind": "research_loop",
                "path": "reviews/research-loop/loop.example.yaml",
                "summary": "This tries to make research-loop output proof authority.",
            }
        ]
    elif case == "workflow_as_source":
        base["sources"] = [
            {
                "kind": "workflow_output",
                "title": "Reviewable workflow record",
                "authors": ["workspace operator"],
                "year": 2026,
                "url": ".cosheaf/workflows/wf.example/workflow.json",
            }
        ]
    elif case == "workflow_as_accepted_proof":
        base["type"] = "proof"
        base["title"] = "Bad workflow proof"
        base["statement"] = "The workflow output is accepted proof and proves the theorem."
        base["evidence"] = [
            {
                "kind": "workflow_output",
                "path": ".cosheaf/workflows/wf.example/workflow.json",
                "summary": "This tries to make workflow output proof authority.",
            }
        ]
    elif case == "workflow_as_human_review":
        base["review"] = {
            "state": "human_reviewed",
            "review_source": ".cosheaf/workflows/wf.example/handoff.json",
            "reviewer_kind": "reviewable_workflow_packet",
            "notes": "This fixture tries to spoof human review with a workflow packet.",
        }
    else:
        raise ValueError(case)
    base["id"] = f"definition.{case}"
    return yaml.safe_dump(base, sort_keys=False)


def good_operator_handoff() -> str:
    return """\
kind: operator_handoff_export
handoff_id: handoff.public.example
review_context_only: true
accepted_write_performed: false
human_review_created: false
promotion_performed: false
verifier_result_mutated: false
summary: Public-safe handoff fixture for policy guard self-test.
checks:
- kind: validate
  status: pass
- kind: test
  status: skipped
  summary: Skipped operator-session checks are not pass evidence.
"""


def bad_operator_handoff(case: str) -> str:
    base = yaml.safe_load(good_operator_handoff())
    assert isinstance(base, dict)
    if case == "operator_handoff_private_marker":
        base["policy_mode"] = "private_research"
        base["referenced_files"] = ["kb/private/claims/claim.secret.yaml"]
    elif case == "operator_handoff_authority_true":
        base["human_review_created"] = True
    elif case == "operator_handoff_provider_dump":
        base["provider_response"] = {"raw": "provider response payload should not be imported"}
    else:
        raise ValueError(case)
    base["handoff_id"] = f"handoff.{case}"
    return yaml.safe_dump(base, sort_keys=False)


def good_research_loop_export() -> str:
    return """\
kind: research_loop_export
loop_id: loop.public.example
review_context_only: true
accepted_write_performed: false
human_review_created: false
promotion_performed: false
verifier_result_mutated: false
summary: Public-safe research-loop fixture for policy guard self-test.
attempts:
- status: failed
  summary: Failed attempt is retained as review context only.
- status: succeeded
  summary: Succeeded loop attempt is not accepted knowledge.
"""


def bad_research_loop_export(case: str) -> str:
    base = yaml.safe_load(good_research_loop_export())
    assert isinstance(base, dict)
    if case == "research_loop_private_marker":
        base["referenced_files"] = ["kb/private/claims/claim.secret.yaml"]
    elif case == "research_loop_authority_true":
        base["accepted_write_performed"] = True
    elif case == "research_loop_provider_dump":
        base["provider_response"] = {"raw": "provider response payload should not be imported"}
    else:
        raise ValueError(case)
    base["loop_id"] = f"loop.{case}"
    return yaml.safe_dump(base, sort_keys=False)


def write_operator_handoff_fixture(root: Path, name: str, body: str) -> Path:
    path = root / "reviews" / "operator" / f"{name}.yaml"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")
    return path


def write_research_loop_fixture(root: Path, name: str, body: str) -> Path:
    path = root / "reviews" / "research-loop" / f"{name}.yaml"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")
    return path


def run_self_test() -> int:
    cases = {
        "missing_sources": "missing source metadata",
        "missing_human_review": "missing human review metadata",
        "private_dependency": "depends on a private artifact",
        "skipped_as_pass": "skipped verifier result is treated as pass",
        "operator_as_human_review": "operator, workflow, or model output is claimed as human review",
        "operator_as_verifier_pass": "operator or model output is claimed as verifier pass",
        "checked_without_evidence": "checked formalization lacks checker evidence",
        "private_marker": "private-looking marker",
        "operator_handoff_as_source": "operator handoff is claimed as source metadata",
        "operator_handoff_private_marker": "operator handoff contains private, secret, reasoning, or provider-payload marker",
        "operator_handoff_authority_true": "operator handoff claims accepted/review/promotion authority",
        "operator_handoff_provider_dump": "operator handoff contains private, secret, reasoning, or provider-payload marker",
        "research_loop_as_source": "research loop output is claimed as source metadata",
        "research_loop_as_accepted_proof": "research loop output is claimed as accepted proof",
        "workflow_as_source": "workflow output is claimed as source metadata",
        "workflow_as_accepted_proof": "workflow output is claimed as accepted proof",
        "workflow_as_human_review": "operator, workflow, or model output is claimed as human review",
        "research_loop_private_marker": "research loop output contains private, secret, proof, source, reasoning, or provider-payload marker",
        "research_loop_authority_true": "research loop output claims accepted/review/promotion authority",
        "research_loop_provider_dump": "research loop output contains private, secret, proof, source, reasoning, or provider-payload marker",
    }
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        write_fixture(root, "definition.good", good_artifact())
        write_operator_handoff_fixture(root, "handoff.good", good_operator_handoff())
        write_research_loop_fixture(root, "loop.good", good_research_loop_export())
        positive_errors = check_repository(root)
        if positive_errors:
            print("positive fixture failed:", file=sys.stderr)
            for error in positive_errors:
                print(error, file=sys.stderr)
            return 1
        for case, expected_message in cases.items():
            case_root = root / case
            if case.startswith("operator_handoff_") and case != "operator_handoff_as_source":
                write_operator_handoff_fixture(case_root, case, bad_operator_handoff(case))
            elif case.startswith("research_loop_") and case not in {
                "research_loop_as_source",
                "research_loop_as_accepted_proof",
            }:
                write_research_loop_fixture(case_root, case, bad_research_loop_export(case))
            else:
                write_fixture(case_root, case, bad_artifact(case))
            errors = check_repository(case_root)
            if not errors:
                print(f"negative fixture did not fail: {case}", file=sys.stderr)
                return 1
            if not any(expected_message in error.message for error in errors):
                print(f"negative fixture failed for the wrong reason: {case}", file=sys.stderr)
                for error in errors:
                    print(error, file=sys.stderr)
                return 1
        shutil.rmtree(root)
    print("policy guard self-test passed")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".", help="Repository root to scan.")
    parser.add_argument("--self-test", action="store_true", help="Run built-in positive and negative fixtures.")
    args = parser.parse_args(argv)

    if args.self_test:
        return run_self_test()

    repo_root = Path(args.repo_root).resolve()
    errors = check_repository(repo_root)
    if errors:
        print("Public KB policy guard failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Public KB policy guard passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
