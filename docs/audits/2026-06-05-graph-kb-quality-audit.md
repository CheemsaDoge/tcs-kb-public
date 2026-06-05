# Graph KB Quality Audit, 2026-06-05

Issue: #21

This audit covers the accepted graph-theory public KB artifacts after the elementary theorem statement pack. It is a repository metadata and statement-quality audit only. It does not run Lean, check external formal libraries, or add new artifacts.

## Audited Artifacts

- `definition.graph`
- `definition.vertex`
- `definition.edge`
- `definition.simple-graph`
- `definition.path`
- `definition.cycle`
- `definition.subgraph`
- `definition.degree`
- `definition.neighborhood`
- `definition.connected`
- `definition.acyclic`
- `definition.tree`
- `theorem.tree-connected`
- `theorem.tree-acyclic`
- `theorem.connected-path-exists`
- `theorem.cycle-contains-path`

## Source Locator Findings

- All audited accepted artifacts have source metadata.
- All source entries use the public Diestel graph-theory chapter preview as the current external source locator.
- `definition.graph`, `definition.vertex`, `definition.edge`, and `definition.simple-graph` retain the prior source-reviewed locator `Chapter 1, Section 1.1, p. 2`.
- Artifacts whose exact PDF preview page has not been tightened use conservative section-level locators such as `Chapter 1, Section 1.3; exact page to be confirmed.`
- This PR normalizes all audited uncertain page locators to the conservative `exact page to be confirmed.` form.
- The theorem source notes now state when a theorem statement is a definitional consequence or an elementary consequence of the accepted definitions. No new theorem numbers or page numbers are introduced.

## Theorem Classification Findings

- `theorem.tree-connected` is a definitional consequence under the current tree convention.
- `theorem.tree-acyclic` is a definitional consequence under the current tree convention.
- `theorem.connected-path-exists` is a definitional consequence under the current connectedness convention.
- `theorem.cycle-contains-path` is an elementary source-reviewed statement under the current path and cycle conventions.
- None of the four theorem artifacts stores a proof body.
- None of the four theorem artifacts is presented as an independent machine-checked theorem.
- `theorem.cycle-contains-path` remains intentionally broad at statement-artifact granularity; a later proof sketch should clarify pairwise quantification and the subpath convention used.

## Dependency Findings

- The audited graph contains 16 accepted artifacts and 33 dependency edges.
- All audited dependencies resolve to accepted public artifacts in the audited set.
- No audited artifact depends on a private artifact.
- No dependency cycles were found.
- The theorem dependencies match the intended definition anchors:
  - `theorem.tree-connected` depends on `definition.tree` and `definition.connected`.
  - `theorem.tree-acyclic` depends on `definition.tree` and `definition.acyclic`.
  - `theorem.connected-path-exists` depends on `definition.connected`, `definition.path`, and `definition.vertex`.
  - `theorem.cycle-contains-path` depends on `definition.cycle`, `definition.path`, and `definition.vertex`.
- The connected/path/tree/cycle dependency structure is semantically reasonable for statement-only accumulation.

## Formalization Metadata Findings

- All audited artifacts have `formalizations` metadata.
- All audited formalization entries have `status: planned`.
- No audited formalization entry has `status: checked`.
- `declaration_kind` matches artifact type: definitions use `definition`, and theorem statements use `theorem`.
- All audited formalization entries use `check_mode: external_library_ref`.
- All audited artifacts have `verification_policy.require_lean_check: false`.
- All audited artifacts have `alignment.status: requested`.
- Formalization notes state that the referenced symbol is not checked by this repository.

## Known Limitations

- No Lean execution.
- No machine-checked proof.
- No external formal library check.
- Formalization links remain planned only.
- Source locators may still need later bibliographic tightening.
- The audit checks repository metadata and statement classification; it does not independently verify the cited textbook PDF contents.

## Follow-Up Recommendations

- Tighten exact source page locators in a later bibliographic pass, without inventing page numbers.
- Add proof-sketch artifacts only through the accepted artifact workflow after source and review policy are clear.
- Before any formalization-status upgrade, run the relevant external Lean checks outside this repository and record a separate alignment review.
- For `theorem.cycle-contains-path`, make the intended pairwise quantification and subpath convention explicit before adding proof sketches.
