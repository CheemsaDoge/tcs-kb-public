# TCS Public Knowledge Base

This repository is the public reusable theoretical computer science knowledge base for TCS-Cosheaf.

It contains public, citable definitions, constructions, reductions, counterexamples, and reviewed knowledge artifacts. It is intended to be mounted by user workspaces as a readonly KB root, with private research stored in a separate writable overlay.

For ordinary downstream use, start from
[`tcs-cosheaf-workspace-template`](https://github.com/CheemsaDoge/tcs-cosheaf-workspace-template).
That template combines the
[`tcs-cosheaf`](https://github.com/CheemsaDoge/tcs-cosheaf) framework, this
public KB as readonly common knowledge, and a writable `kb/private` overlay.
Do not manually merge the framework, public KB, and private workspace
repositories into one mixed tree.

This repository should be written only by public KB maintainers through
reviewed PRs. Downstream private artifacts may depend on public artifacts here;
public artifacts here must not depend on downstream private artifacts.

## Layout

- `kb/public/accepted/definitions/`: accepted public definition artifacts.
- `kb/public/accepted/theorems/`: accepted public theorem artifacts.
- `kb/public/accepted/proofs/`: accepted public proof or proof-sketch artifacts.
- `kb/public/draft/proofs/`: draft public proof or proof-sketch artifacts before accepted promotion.
- `kb/public/constructions/`: public construction artifacts; current artifacts here may still be drafts.
- `kb/public/reductions/`: public reduction notes or artifacts.
- `kb/public/counterexamples/`: public counterexample notes or artifacts.
- `sources/`: source notes and bibliographic metadata.
- `reviews/human/`: human review records.
- `reviews/ai/`: AI-assisted review notes.
- `reviews/gatekeeper/`: validation and gatekeeper review outputs.
- `docs/`: repository policies.

See `docs/GRAPH_FOUNDATION_BACKLOG.md` for the controlled graph/SAT foundation
backlog and `docs/SOURCE_NOTES.md` for the durable source-note convention.

## Policy

This repository does not contain private conjectures, unpublished research ideas, or accepted LLM-generated artifacts without human review. New knowledge should normally begin as a GitHub issue and land as a small PR.

The current public KB includes accepted definitions, theorem statements, and proof sketches under `kb/public/accepted/`. Draft artifacts remain outside `accepted/` until they pass the repository promotion workflow.

Accepted public artifacts require complete source metadata and human review.
Validation or gate success alone is not enough to mark an artifact accepted.

Proof sketches are explanatory source-reviewed artifacts, not machine-checked
proofs. See `docs/PROOF_SKETCH_POLICY.md`.

Artifact-level failure logs, when present, are public research memory only.
They do not prove, refute, verify, review, accept, or promote artifacts by
themselves. See `docs/FAILURE_LOG_POLICY.md`.

Checked counterexample evidence and research-run records are public review
context only. They do not replace human review, source metadata, validation,
gates, verifier policy, or accepted promotion. See
`docs/CHECKED_EVIDENCE_POLICY.md`.

Strategy plans and strategy review exports are public review context only. They
cannot replace source metadata, validation, gates, verifier evidence, human
review, or accepted promotion, and private workspace strategy plans must not be
copied into this public KB. See `docs/STRATEGY_PLAN_POLICY.md`.

Operator, Codex, MCP, provider, workflow, research-run, checked-evidence, and
strategy outputs are review context only. They cannot create source metadata,
human review, verifier pass, gate pass, accepted status, accepted refutation,
or promotion authority. See `docs/OPERATOR_POLICY.md` and
`docs/OPERATOR_HANDOFF_POLICY.md`.

Workflow cross-check reports, evidence reports, gap reports, checker sidecars,
and checker/cross-check eval outputs are also review context only. They cannot
be accepted proof, accepted theorem/refutation, source metadata, human review,
verifier pass, gate pass, accepted status, or promotion authority. See
`docs/CROSSCHECK_REPORT_POLICY.md`.

Research loop outputs are public review context only. They are not source
metadata, not accepted proof, not human review, not verifier or gate passes,
and not promotion authority. Accepted public artifacts still require complete
source metadata and maintainer human review. Validation and gate success are
not human review. See `docs/RESEARCH_LOOP_POLICY.md`.

The repository includes `formal-libs/lean-libraries.example.yaml` so existing
planned CSLib formal-link metadata resolves under the G10 formal-link gate.
That manifest is placeholder metadata only. It does not fetch CSLib, run Lean,
check symbols, or prove informal/formal semantic alignment.

## License

This public KB is released under the Apache-2.0 license. See `LICENSE`.

## Local Commands

Install or otherwise make `cosheaf` available, then run:

```bash
cosheaf workspace info
cosheaf validate
cosheaf gate run
cosheaf gate run --pr-checklist .github/pull_request_template.md
```

Repository CI installs `tcs-cosheaf` from the published `v0.10.0` framework tag.

Downstream workspaces should include this repository as a readonly public KB
root and keep private work in a separate writable root. The workspace template
is the recommended starting point for that setup.
