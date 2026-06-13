# Graph Foundation Backlog

This backlog controls the next graph-theory foundation additions for the public
KB. It is planning metadata only: it does not add, promote, or revise accepted
artifacts.

The public KB should grow through small source-reviewed PRs. Before any
candidate becomes accepted, maintainers must verify complete artifact source
metadata, a real source locator, public-only dependencies, validation and gate
results, and human review evidence. Validation or gate success alone is not a
substitute for human review.

Formalization status for these candidates should start as `planned` unless an
actual checker is run and its result is recorded. Planned formal links are
metadata only and do not mean Lean, CSLib, mathlib, SAT, SMT, or any other
external checker has verified the artifact.

## Current Scope

The first controlled pack is intentionally small:

Post-v0.2.1 refresh status:

- Accepted graph definition support currently includes `definition.graph`,
  `definition.vertex`, `definition.edge`, `definition.simple-graph`,
  `definition.path`, `definition.cycle`, `definition.connected`,
  `definition.acyclic`, `definition.neighborhood`, `definition.tree`,
  `definition.degree`, and `definition.subgraph`.
- Draft foundation candidates currently include `definition.walk` and
  `definition.connected-graph`.
- The durable Diestel source note exists at
  `sources/books/diestel-graph-theory.md`.
- This refresh does not add, promote, or modify artifacts. It only keeps the
  backlog aligned with current repository state.

| Artifact ID | Type | Domain | Current State | Expected Dependencies | Candidate Source | Exact Source Locator Known? | Risk | Formalization Starting Status | Alignment Review Needed? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `definition.tree` | definition | Graph theory | Already accepted; do not re-add. Future work is source-note migration or locator tightening only. | `definition.graph`, `definition.connected`, `definition.acyclic` | Diestel, *Graph Theory*, Chapter 1 tree terminology. | Section-level locator recorded; exact preview page remains to be confirmed in current artifact notes. | Low, but convention-sensitive. | `planned` unless actually checked. | Yes, before relying on any external formal-library tree convention. |
| `definition.degree` | definition | Graph theory | Already accepted; do not re-add. Future work is source-note migration or locator tightening only. | `definition.graph`, `definition.vertex`, `definition.edge` | Diestel, *Graph Theory*, Chapter 1 degree terminology. | Section-level locator recorded; exact preview page remains to be confirmed in current artifact notes. | Low, with simple-graph convention notes required. | `planned` unless actually checked. | Yes, before relying on external formal-library degree symbols. |
| `definition.walk` | definition | Graph theory | Draft candidate exists under `kb/public/draft/definitions/` and now points to the durable Diestel source note; keep draft until source locator and convention review are complete. | `definition.graph`, `definition.vertex`, `definition.edge` | Diestel, *Graph Theory*, Chapter 1 walk/path terminology, or another stable graph-theory text if Diestel locator is insufficient. | Unknown; must be confirmed before acceptance. | Low to medium, because walk conventions vary by repeated vertices/edges and length-zero cases. | `planned` unless actually checked. | Yes, because formal libraries often encode walks differently. |
| `definition.connected-graph` | definition | Graph theory | Draft candidate added for maintainer review; do not promote unless the alias adds value beyond `definition.connected`. | `definition.graph`, `definition.connected` | Diestel, *Graph Theory*, Chapter 1 connectedness terminology. | Section-level locator exists for connectedness; exact page should be confirmed before any accepted alias. | Low, but duplication risk is real. | `planned` unless actually checked. | Yes, especially if mapped to an external predicate name. |
| `definition.subgraph` | definition | Graph theory | Already accepted; do not re-add. Future work is source-note migration or locator tightening only. | `definition.graph`, `definition.vertex`, `definition.edge` | Diestel, *Graph Theory*, Chapter 1 subgraph terminology. | Section-level locator recorded; exact preview page remains to be confirmed in current artifact notes. | Low. | `planned` unless actually checked. | Yes, because subgraph encodings vary by induced/non-induced convention. |
| `definition.clique` | definition | Graph theory | Candidate for a future small PR. | `definition.graph`, `definition.vertex`, `definition.edge`, possibly `definition.subgraph` | Diestel, *Graph Theory*, Chapter 1 complete graph/subgraph terminology, or another stable graph-theory text with an explicit clique definition. | Unknown; must be confirmed before acceptance. | Medium, because clique may be defined as a vertex set, complete subgraph, or maximal complete subgraph in some contexts. | `planned` unless actually checked. | Yes, to align set/subgraph conventions. |
| `definition.independent-set` | definition | Graph theory | Candidate for a future small PR. | `definition.graph`, `definition.vertex`, `definition.edge`, possibly `definition.subgraph` | Diestel, *Graph Theory*, Chapter 1 independence terminology, or another stable graph-theory text with an explicit independent-set definition. | Unknown; must be confirmed before acceptance. | Medium, because terminology can differ between vertex independence and edge independence. | `planned` unless actually checked. | Yes, to align vertex-set and no-edge conventions. |
| `definition.matching` | definition | Graph theory | Candidate for a future small PR. | `definition.graph`, `definition.vertex`, `definition.edge` | Diestel, *Graph Theory*, Chapter 1 matching terminology, or another stable graph-theory text with an explicit matching definition. | Unknown; must be confirmed before acceptance. | Medium, because matching conventions interact with simple graphs, endpoints, and maximal/maximum terminology. | `planned` unless actually checked. | Yes, before mapping to external library matching structures. |
| `definition.cnf-formula` | definition | Boolean satisfiability | Candidate for a future small PR after graph basics are stable. | Candidate prerequisite definitions for Boolean variable, literal, clause, and formula, or explicit external references if those are not yet local artifacts. | Sipser, CLRS, or a stable SAT/complexity text with explicit CNF terminology. | Unknown; must be confirmed before acceptance. | Medium, because formula syntax and encoding conventions must be stated carefully. | `planned` unless actually checked. | Yes, before relating to SAT solver or formal-library encodings. |
| `definition.sat-instance` | definition | Boolean satisfiability | Candidate for a future small PR after `definition.cnf-formula` or equivalent prerequisites exist. | `definition.cnf-formula`, plus prerequisite Boolean syntax artifacts or explicit external references. | Sipser, CLRS, or a stable SAT/complexity text with explicit SAT-instance terminology. | Unknown; must be confirmed before acceptance. | Medium, because decision-problem, assignment, and encoding boundaries must be explicit. | `planned` unless actually checked. | Yes, before relating to solver results or formal-library encodings. |

## Follow-Up Order

1. Keep the source-note convention current and reuse the existing Diestel source
   note where artifact-local source metadata already cites Diestel.
2. Add SAT/complexity source notes before adding SAT foundation artifacts.
3. Tighten source locators for existing accepted definitions where a reviewer
   can confirm exact pages or sections. Do not guess page numbers.
4. Add at most one new foundation definition per PR unless the dependencies are
   inseparable and the review scope remains small.
5. Do not add additional theorem or proof-sketch packs from this backlog unless
   a separate issue scopes the source-review plan and keeps proof sketches
   explanatory, source-reviewed, and not machine-checked.

## Candidate Review Checklist

For each future artifact PR:

- Confirm the candidate is public, citable knowledge.
- Confirm the statement matches the cited source.
- Record source metadata in the artifact itself.
- Add or reuse a durable source note when useful.
- Record whether the exact source locator is confirmed or still uncertain.
- Record human review under `reviews/human/`.
- Keep formalization metadata planned-only unless an actual checker ran.
- Keep alignment review requested when external formal-library semantics matter.
- Run validation and gates, but do not treat them as a replacement for review.
- Do not use provider or agent output as accepted public knowledge, source
  evidence, human review, or checker evidence.
