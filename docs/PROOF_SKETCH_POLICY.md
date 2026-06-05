# Proof Sketch Policy

This repository may store public proof-sketch artifacts when they help explain accepted theorem artifacts. Proof sketches are explanatory, source-reviewed artifacts. They are not machine-checked proofs.

## Scope

Proof sketches may be used for:

- definitional expansion;
- elementary argument;
- literature-backed proof sketch;
- informal intuition only.

The reasoning classification must be recorded in the artifact statement, review notes, or risk notes. A proof sketch that is only informal intuition must not be presented as a proof.

## Requirements

Every public proof-sketch artifact must:

- start as `status: draft`;
- depend only on accepted theorem or definition artifacts;
- include source metadata sufficient to relocate the public source;
- include external or repository-local evidence references;
- include a human review record under `reviews/human/`;
- remain explicit about the theorem or definition convention it relies on;
- use the accepted artifact promotion workflow before becoming accepted.

Accepted proof sketches require source metadata, validation, gate results, and human review. Passing validation is not enough to mark a proof sketch accepted.

## Formalization Boundary

Proof sketches must not:

- claim to be machine-checked proofs;
- be used as Lean verification evidence;
- upgrade any `formalization.status` to `checked`;
- require Lean execution in this repository;
- introduce Lean, lake, mathlib, or CSLib dependencies.

If formalization metadata is present, it must be planned-only unless a later, separate workflow records an actual external formal check and review. Planned formalization metadata is a locator for future alignment work, not proof evidence.

## Review Notes

Human review notes for proof sketches should state:

- the reasoning classification;
- the source metadata reviewed;
- the accepted artifacts the sketch depends on;
- that the sketch is not Lean-checked;
- that the sketch is not machine-checked;
- that no formalization status is upgraded.

Reviewers should request revision when a proof sketch is too broad, relies on an unstated convention, cites an uncertain source locator too specifically, or reads like a private proof attempt rather than public explanatory knowledge.
