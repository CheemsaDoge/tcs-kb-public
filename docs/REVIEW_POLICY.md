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
