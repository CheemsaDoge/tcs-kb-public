# Release Checklist

This repository follows the TCS-Cosheaf framework release line and keeps the
public KB release gates small, policy-focused, and artifact-preserving.

## Current Framework Baseline

- [x] Public KB CI installs the framework from the immutable `v0.2.2` tag:
  `python -m pip install "git+https://github.com/CheemsaDoge/tcs-cosheaf.git@v0.2.2"`.
- [x] Public KB CI does not install the framework from `main`.
- [x] Downstream users are directed to `tcs-cosheaf-workspace-template`
  instead of manually merging framework, public KB, and private workspace
  repositories.

## Required Checks

Run these before merging public KB release-followup or policy PRs:

```bash
cosheaf version --json
cosheaf workspace info
cosheaf validate
python scripts/check_public_kb_policy.py --self-test
python scripts/check_public_kb_policy.py
cosheaf gate run
cosheaf gate run --pr-checklist .github/pull_request_template.md
git diff --check
```

## Public KB Policy Boundary

- [x] License policy is Apache-2.0 and the repository includes a root `LICENSE`.
- [x] Public KB policy forbids private conjectures, unpublished research ideas,
  and unreviewed accepted LLM-generated artifacts.
- [x] Accepted public artifacts require source metadata and human review.
- [x] Validation and gate success are not human review.
- [x] Public KB proof sketches are policy-bound explanatory artifacts and are
  not treated as machine-checked proofs or Lean verification evidence.
- [x] Planned or linked formalizations remain metadata unless a real checker
  runs and records evidence.

## Compatibility Validation

- [x] Public KB CI runs workspace info, validation, policy guard self-test,
  policy guard, gatekeeper, PR checklist gate, and whitespace checks.
- [x] Compatibility PRs do not add new public KB artifacts or promote drafts.
- [x] Compatibility PRs do not change review records, formalization metadata,
  schemas, or accepted-promotion semantics unless explicitly scoped.

## Backlog And Source-Note PRs

- [ ] Backlog/source-note refresh PRs do not add accepted artifacts, promote
  drafts, alter review records, or change formalization metadata.
- [ ] Source-note PRs preserve artifact-local source metadata requirements.
- [ ] Provider, agent, or model outputs are not treated as source evidence,
  human review, checker evidence, or accepted public knowledge.

## Proof Sketch Follow-Up

- [ ] Proof-sketch PRs add at most one pilot proof sketch unless the issue
  explicitly scopes a larger reviewed batch.
- [ ] Proof-sketch artifacts do not upgrade `formalization.status` to
  `checked`.
- [ ] Proof-sketch artifacts do not add Lean, lake, mathlib, or CSLib
  dependencies.
