# Release Checklist

This repository follows the TCS-Cosheaf framework release line and keeps the
public KB release gates small, policy-focused, and artifact-preserving.

## P0 Exit

- [x] Public KB CI installs the framework from the immutable `v0.1.1` tag:
  `python -m pip install "git+https://github.com/CheemsaDoge/tcs-cosheaf.git@v0.1.1"`.
- [x] License policy is Apache-2.0 and the repository includes a root `LICENSE`.
- [x] Public KB policy forbids private conjectures, unpublished research ideas,
  and unreviewed accepted LLM-generated artifacts.
- [x] Downstream users are directed to `tcs-cosheaf-workspace-template` instead
  of manually merging framework, public KB, and private workspace repositories.
- [x] v0.1.1 formal-link follow-up changes do not add new KB artifacts; any
  existing artifact changes are metadata-only.

## Required Checks

Run these before merging release-followup PRs:

```bash
cosheaf workspace info
cosheaf validate
cosheaf gate run
cosheaf gate run --pr-checklist .github/pull_request_template.md
git diff --check
```

## P1 Entry

P1 testing hardening may start only after:

- `CheemsaDoge/tcs-cosheaf` has tag `v0.1.1`.
- Public KB CI installs `tcs-cosheaf` from `@v0.1.1`, not `@main`.
- Workspace template CI upgrade to `@v0.1.1` is tracked in the separate
  workspace-template follow-up PR.
- Related P0 release-followup PRs are merged and CI passes.

## P1 Public KB Validation

- [x] Public KB CI still installs `tcs-cosheaf` from immutable `@v0.1.1`.
- [x] Public KB CI runs workspace info, validation, gatekeeper, PR checklist
  gate, and whitespace checks.
- [x] P1 validation PRs do not add new public KB artifacts or promote drafts.
