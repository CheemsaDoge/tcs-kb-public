# Repository Instructions

This repository contains public, citable theoretical computer science knowledge for TCS-Cosheaf. It is a public knowledge base, not a private research notebook and not the framework repository.

## Operating Model

- This repository is writable only for public KB maintainers through focused
  public-KB PRs. Downstream user workspaces should mount it readonly.
- Ordinary users should start from
  `tcs-cosheaf-workspace-template`, not by manually merging this repository with
  the framework or a private workspace.
- Use GitHub issues for nontrivial knowledge additions, policy changes, source ingestion, or schema-facing work.
- One source-ingestion task should normally be one issue, one branch, one PR, and one small reviewable batch.
- Use branches named `codex/<task-id-or-short-name>`.
- Do not push directly to `main`.
- Every implementation or knowledge addition should go through PR review.
- Keep durable decisions in repository files; chat transcripts are not project memory.

## Knowledge Policy

- Only public, citable TCS knowledge belongs here.
- No private conjectures.
- No unpublished research ideas.
- No private research notes or proof attempts.
- No LLM-generated accepted artifacts without human review.
- Accepted artifacts require source metadata and review evidence.
- Draft artifacts must be clearly marked `draft`.
- Public KB artifacts must not depend on private KB artifacts.
- Do not mass-import papers; prefer small, reviewable artifact batches.

## Artifact Workflow

- New artifacts should start as `draft`.
- Accepted status requires source metadata, gate results, and human review.
- Keep source references under `sources/` or use clearly external evidence references.
- Keep human, AI, and gatekeeper review records under `reviews/`.
- Do not promote a draft to accepted just because validation passes.

## Validation

Run available checks before opening or updating a PR:

- `cosheaf workspace info`
- `cosheaf validate`
- `cosheaf gate run`
- `cosheaf gate run --pr-checklist .github/pull_request_template.md`

If the framework is checked out locally, also run any applicable framework gate commands against this repository. If a command is unavailable or fails because of the environment, report it exactly. Skipped is not pass.

## Repository Relationship

- `tcs-cosheaf` is the framework repository.
- This repository is the public reusable KB.
- `tcs-cosheaf-workspace-template` is the recommended user entry point for
  combining the framework, this public KB, and a private writable overlay.
- User workspaces should mount this KB as readonly common knowledge.
- User private KB overlays may depend on this public KB.
- This public KB must not depend on private overlays.
