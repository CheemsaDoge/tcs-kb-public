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

Downstream workspaces should include this repository as a readonly public KB
root and keep private work in a separate writable root. The workspace template
is the recommended starting point for that setup.
