# Foundation Backlog

This document is the general entrypoint for public KB foundation backlog work.
The current controlled foundation backlog is:

- `docs/GRAPH_FOUNDATION_BACKLOG.md`: graph-theory and SAT-adjacent
  foundation candidates.

Backlog entries are planning metadata only. They do not add accepted artifacts,
do not promote drafts, and do not make source or formalization claims true by
themselves.

## Policy

Foundation work must stay small and reviewable:

- Add at most one future foundation artifact per PR unless dependencies are
  inseparable and the review scope remains small.
- Do not fabricate page, section, theorem, lemma, or equation locators.
- If source metadata is missing or uncertain, mark the item as needing source
  review instead of guessing.
- Formalization status starts as `planned` unless an actual checker runs and
  records evidence.
- Planned or linked formalizations are metadata only. They do not mean Lean,
  CSLib, mathlib, SAT, SMT, or semantic alignment has been checked.
- Accepted public artifacts require complete artifact-local source metadata,
  validation/gate evidence, and human review.
- Validation or gate success is not a substitute for human review.

## Current Candidates

See `docs/GRAPH_FOUNDATION_BACKLOG.md` for the active candidate table covering:

- `definition.tree`
- `definition.degree`
- `definition.walk`
- `definition.connected-graph`
- `definition.subgraph`
- `definition.clique`
- `definition.independent-set`
- `definition.matching`
- `definition.cnf-formula`
- `definition.sat-instance`

Future domain-specific backlogs should be linked from this file rather than
mixed into one large import plan.
