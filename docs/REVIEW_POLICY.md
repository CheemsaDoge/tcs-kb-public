# Review Policy

Human review is the boundary for accepted public knowledge in this repository.
Validation, gates, source notes, formal-link metadata, and AI-assisted review
can support review, but none of them replaces human review.

## Required Human Review

Human review is required before accepting:

- public definition artifacts;
- public theorem or claim artifacts;
- public proof-sketch artifacts;
- source-note policy changes;
- artifact schema-facing changes;
- formal-link or alignment semantics that affect accepted artifacts.

Review records should live under `reviews/human/` and identify the reviewed
artifact, source metadata, dependency set, formalization status, limitations,
and decision.

## Source Review

Reviewers should confirm:

- the cited source is public and citable;
- the artifact statement matches the source;
- source locators are real and not guessed;
- any uncertainty is explicitly recorded;
- artifact-local source metadata remains complete.

Source notes are durable bibliographic records. Under current policy, they do
not replace source metadata required inside accepted artifact YAML.

## Dependency Review

Accepted public artifacts must not depend on private or draft artifacts.
Dependencies must be accepted public artifacts or explicit external references
that are documented in the artifact.

Private workspace material must not be copied into this repository.

## Formalization And Alignment Review

Formal links are metadata unless a real checker verifies them and records
evidence. Planned or linked formalizations are not Lean, mathlib, CSLib, SAT,
SMT, or semantic-alignment proof.

A future successful Lean `#check`, by itself, would show symbol/import
availability. It would not prove that the informal statement and formal
declaration are semantically aligned. Alignment review remains human-reviewed
metadata.

## Gate Results

Validation and gate success are required workflow evidence for accepted
artifacts, but they are not substitutes for human review. Skipped verifier
results are not passes.

## Failure Log Review

Failure-log entries are research memory, not authority. Reviewers should verify
that any `failure_log` entry is public, preserves its origin and limitations,
does not leak private workspace material, and does not claim proof, refutation,
verifier success, checked counterexample evidence, human review, gate success,
accepted status, or promotion evidence.

Accepted-path failure logs require the same source and review discipline as
other accepted artifact metadata. Unreviewed provider, agent, or LLM failure
logs must not be copied into accepted public artifacts.

## Checked Evidence And Research-Run Review

Checked counterexample evidence is public review context only. Reviewers should
verify that a checked-evidence record is public-safe, distinguishes candidate
evidence from checked evidence, records the check method and support, preserves
limitations, and does not claim human review, proof, accepted refutation,
accepted status, verifier pass, gate pass, or promotion authority.

Research-run records are provenance only. They may help reviewers see which
commands were run and which outputs were referenced, but they do not prove
correctness and do not replace validation, gates, source review, or human
review.

Run records or review exports included in public KB PRs must not contain
private workspace material, unreviewed provider dumps, secrets, hidden
reasoning, `.env` content, or full private KB text. Accepted public artifacts
must not depend on research-run records as a substitute for source metadata.

## Workflow, Operator, And MCP Review Boundary

Workflow, operator, Codex, MCP, provider, LLM, and agent outputs can support a
public KB review by recording commands, proposed drafts, bounded context,
checked evidence, or strategy notes. They are not source metadata, human
review, verifier pass, gate pass, accepted status, accepted refutation, or
promotion authority, and must not be recorded as human reviewers in structured
review fields.

Maintainer notes may mention where review context came from, but accepted
public artifacts still need maintainer human review, source metadata,
validation, gates, and normal promotion. See `docs/OPERATOR_POLICY.md`.

## Cross-Check Report Review Boundary

Workflow cross-check reports, workflow evidence reports, workflow gap reports,
checker-run sidecars, and checker/cross-check eval outputs can help reviewers
see checked, failed, skipped, inconclusive, unsourced, or unreviewed items.
They are still review context only. They are not source metadata, accepted
proof, accepted theorem/refutation, human review, verifier pass, gate pass,
accepted status, or promotion authority.

Reviewers should confirm that any included cross-check material is public-safe,
clearly labeled review context only, independent from artifact-local source
metadata and maintainer review records, and free of private workspace material,
secrets, hidden reasoning, raw provider payloads, or authority claims. See
`docs/CROSSCHECK_REPORT_POLICY.md`.

## Research Loop Review Boundary

Research loop outputs can support public KB review by preserving attempted
directions, failed directions, retry justifications, scanner findings, and
bounded task/result packets. They are not source metadata, accepted proof,
human review, verifier pass, gate pass, accepted status, accepted refutation,
or promotion authority.

Reviewers should confirm that any included loop material is public-safe,
clearly labeled review context only, independent from artifact-local source
metadata, and free of private workspace material, secrets, hidden reasoning,
raw provider payloads, and authority claims. See
`docs/RESEARCH_LOOP_POLICY.md`.
