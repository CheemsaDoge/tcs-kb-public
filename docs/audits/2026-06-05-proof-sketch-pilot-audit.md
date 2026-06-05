# Proof Sketch Pilot Audit, 2026-06-05

Issue: #27

This audit covers the first two accepted proof-sketch pilots after the proof-sketch policy pilot. It checks whether the workflow is stable enough to use as a baseline before adding harder proof sketches. It is a repository metadata and policy audit only. It does not run Lean, check external formal libraries, add theorem artifacts, add proof-sketch artifacts, or change accepted-promotion semantics.

## Audited Scope

- `proof-sketch.tree-connected`
- `proof-sketch.tree-acyclic`
- `docs/PROOF_SKETCH_POLICY.md`
- `theorem.tree-connected`
- `theorem.tree-acyclic`
- `definition.tree`
- `definition.connected`
- `definition.acyclic`

## Proof Sketch Findings

Both audited proof sketches are accepted `type: proof` artifacts under `kb/public/accepted/proofs/`.

- `proof-sketch.tree-connected` explains `theorem.tree-connected` by definitional expansion from `definition.tree` and `definition.connected`.
- `proof-sketch.tree-acyclic` explains `theorem.tree-acyclic` by definitional expansion from `definition.tree` and `definition.acyclic`.
- Both proof sketches state that the reasoning is a definitional expansion under the current tree convention.
- Both proof sketches state that they are not Lean-checked, not machine-checked, and not Lean verification evidence.

## Dependency Correctness

The audited proof-sketch dependencies are correct and intentionally narrow.

- `proof-sketch.tree-connected` depends only on:
  - `theorem.tree-connected`
  - `definition.tree`
  - `definition.connected`
- `proof-sketch.tree-acyclic` depends only on:
  - `theorem.tree-acyclic`
  - `definition.tree`
  - `definition.acyclic`

All listed dependencies resolve to accepted public theorem or definition artifacts. No audited proof sketch depends on a private artifact, draft artifact, unrelated construction, or another proof sketch.

## Reasoning Classification

Both pilots are classified as definitional expansion proof sketches. This is the lowest-risk proof-sketch class currently allowed by `docs/PROOF_SKETCH_POLICY.md`, because each sketch only expands the accepted source-reviewed convention that a tree is a connected acyclic graph.

The classification is recorded in the proof-sketch statements, review records, source notes, and risk notes. The artifacts do not store independent proof bodies and do not present the sketches as machine-checked theorems.

## Source Locator Status

Both proof sketches use the same conservative public source locator as the related tree theorem and definition artifacts:

- Reinhard Diestel, `Graph Theory`, sixth edition preview.
- URL: `https://www.math.uni-hamburg.de/home/diestel/books/graph.theory/preview/Ch1.pdf`
- Locator: Chapter 1, Section 1.5; exact page to be confirmed.

The locator is adequate for the pilot workflow because it identifies the public chapter and section convention being expanded. It remains intentionally conservative: exact page tightening is future bibliographic work and should not be invented during proof-sketch authoring.

## Review Record Status

Both proof sketches have human review records under `reviews/human/`.

- `reviews/human/review.proof-sketch.tree-connected.md`
- `reviews/human/review.proof-sketch.tree-acyclic.md`

The review records state that the sketches are source-reviewed, definitional expansions, not Lean-checked, not machine-checked, and planned-only with respect to formalization metadata. The `tree-acyclic` review explicitly says the sketch is not Lean verification evidence. The `tree-connected` artifact metadata now mirrors that same wording in `review.notes` and `risk.notes`.

## Risk Notes

The current risk level is low for both pilots, because the sketches are direct expansions of the accepted `definition.tree` convention rather than new graph-theoretic arguments.

The main remaining risk is convention drift: if a future external formal library uses a different tree convention, these proof sketches may require an alignment note or separate formalization review. This is already captured by `alignment.status: requested` and by the planned-only formalization metadata.

## Formalization Metadata

Both proof sketches include formalization locator metadata only.

- `formalizations.status` is `planned`.
- `verification_policy.require_lean_check` is `false`.
- `alignment.status` is `requested`.
- Formalization entries use `check_mode: external_library_ref`.
- The repository does not check CSLib symbol existence for these pilots.

No audited artifact has `formalization.status: checked`, and no proof sketch is used as Lean verification evidence.

## G10 Status

G10 has no blocking issue for these two pilots under the current proof-sketch policy:

- the proof-sketch artifacts are accepted through the repository promotion workflow;
- dependencies resolve to accepted public theorem and definition artifacts;
- source metadata and human review records are present;
- formalization metadata remains planned-only;
- Lean checks are not required by the proof-sketch verification policy.

## Limitations

- No Lean execution.
- No machine-checked proof.
- No external formal library check.
- Formalization links remain planned only.
- Exact source page locators remain to be tightened in a later bibliographic pass.
- This audit checks repository metadata, dependency shape, and policy conformance; it does not independently verify the cited textbook PDF contents.

## Recommendations Before Harder Proof Sketches

- Keep definitional expansion as the pilot baseline; do not use harder sketches until this pattern remains stable across review and gate checks.
- Before adding elementary-argument proof sketches, require the statement to spell out quantifiers and conventions more explicitly than these definitional pilots need.
- Require every harder proof sketch to name its reasoning class in the statement and review record.
- Keep source locators conservative unless a reviewer confirms exact pages.
- Keep `formalizations.status: planned` and `verification_policy.require_lean_check: false` unless a separate workflow performs and reviews actual external formal checks.
- Do not treat planned CSLib or mathlib locator metadata as proof evidence.
- Add alignment review before relying on any external formal-library symbol for semantic confidence.
