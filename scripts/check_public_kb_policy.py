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


def check_record(path: Path, record: dict[str, Any]) -> list[PolicyError]:
    errors: list[PolicyError] = []
    status = str(record.get("status", "")).lower()
    if status == "accepted":
        if not has_source_metadata(record):
            errors.append(PolicyError(path, "accepted artifact is missing source metadata"))
        if not has_human_review(record):
            errors.append(PolicyError(path, "accepted artifact is missing human review metadata"))
        if nonhuman_output_claimed_as_human_review(record):
            errors.append(
                PolicyError(path, "operator or model output is claimed as human review")
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
    else:
        raise ValueError(case)
    base["id"] = f"definition.{case}"
    return yaml.safe_dump(base, sort_keys=False)


def run_self_test() -> int:
    cases = {
        "missing_sources": "missing source metadata",
        "missing_human_review": "missing human review metadata",
        "private_dependency": "depends on a private artifact",
        "skipped_as_pass": "skipped verifier result is treated as pass",
        "operator_as_human_review": "operator or model output is claimed as human review",
        "operator_as_verifier_pass": "operator or model output is claimed as verifier pass",
        "checked_without_evidence": "checked formalization lacks checker evidence",
        "private_marker": "private-looking marker",
    }
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        write_fixture(root, "definition.good", good_artifact())
        positive_errors = check_repository(root)
        if positive_errors:
            print("positive fixture failed:", file=sys.stderr)
            for error in positive_errors:
                print(error, file=sys.stderr)
            return 1
        for case, expected_message in cases.items():
            case_root = root / case
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
