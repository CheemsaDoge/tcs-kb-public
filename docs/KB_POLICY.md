# Public KB Policy

This repository stores public, citable TCS knowledge only.

## Repository Boundary

This repository is the public reusable KB. It is writable only for public KB
maintainers through focused PRs. Downstream users should normally consume it
through
[`tcs-cosheaf-workspace-template`](https://github.com/CheemsaDoge/tcs-cosheaf-workspace-template),
where it is mounted readonly beside a writable private KB overlay.

Do not manually merge this public KB with the `tcs-cosheaf` framework repository
or with a private workspace. Private downstream artifacts may depend on public
artifacts here, but public artifacts here must not depend on downstream private
artifacts.

## Allowed Content

- Public definitions with clear terminology.
- Public constructions with cited sources or standard references.
- Public reductions, counterexamples, theorem statements, and proof sketches after review.
- Draft artifacts clearly marked with `status: draft`.
- Review records and gate outputs.

## Disallowed Content

- Private conjectures.
- Unpublished research ideas.
- Private proof attempts.
- Accepted theorem artifacts without source metadata.
- Accepted proof-sketch artifacts without source metadata and human review.
- LLM-generated accepted artifacts without human review.
- Mass imports of papers or large batches that cannot be reviewed.

## Proof Sketches

Proof sketches are explanatory, source-reviewed artifacts. They are not
machine-checked proofs and must not be used as Lean verification evidence.
They must depend on accepted theorem or definition artifacts, include source
metadata, include human review, and keep any formalization metadata planned-only
unless a later formal-check workflow actually verifies it.

See `docs/PROOF_SKETCH_POLICY.md`.

## Failure Logs

Artifact-level `failure_log` entries are public research memory only. They can
record reviewed failed directions, source-locator dead ends, or formalization
alignment attempts, but they are not proof, refutation, verifier evidence,
human review, gate success, accepted status, or promotion evidence by
themselves.

Unreviewed LLM, hosted-provider, or agent failure dumps must not enter accepted
public paths. Downstream private failure memory belongs in downstream private
KB overlays unless maintainers explicitly review it through a public-KB PR.

See `docs/FAILURE_LOG_POLICY.md`.

## Checked Evidence And Research Runs

Checked counterexample evidence may be stored or referenced as public review
context when it has been reviewed for public safety and limitations. It is not
human review, proof, accepted refutation, accepted status, verifier pass, gate
pass, promotion authority, or a replacement for source metadata.

Research-run records may document operator provenance for public-KB PRs. They
must not include private workspace material, unreviewed provider dumps, API
keys, hidden reasoning, `.env` content, or full private KB text in accepted
public paths. Run records are provenance only and do not make a public artifact
accepted.

Candidates and checked evidence must be labeled separately. A
`candidate_counterexample` is proposed evidence only; checked counterexample
evidence requires an explicit checked-evidence record with method, result,
support references, checker label, and limitations.

See `docs/CHECKED_EVIDENCE_POLICY.md`.

## Workflow, Operator, MCP, And Provider Outputs

Workflow, operator, Codex, MCP, provider, LLM, and agent outputs may be used
only as bounded public review context. They are not source metadata, human
review, proof, verifier pass, gate pass, accepted status, accepted refutation,
or promotion authority.

Accepted artifacts must not use structured review metadata to claim an
operator or model as the human reviewer. Verifier results must not claim a pass
when the only authority is a workflow, operator, MCP adapter, hosted provider,
LLM, or agent output.

See `docs/OPERATOR_POLICY.md`.

## Research Loop Outputs

Research loop outputs may be included only as public review context. They are
not source metadata, accepted proof, human review, verifier pass, gate pass,
accepted status, accepted refutation, or promotion authority.

Accepted public artifacts still require complete artifact-local source
metadata, validation, gate results, and maintainer human review. Validation and
gate success are not human review, and loop success never means accepted
knowledge.

See `docs/RESEARCH_LOOP_POLICY.md`.

## Promotion

Draft artifacts may be promoted only after complete source metadata,
validation, gate results, and human review have been recorded. Passing
validation is not enough to mark an artifact accepted.
