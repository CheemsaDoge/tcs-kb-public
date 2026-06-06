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

| Artifact ID | Type | Domain | Current State | Expected Dependencies | Candidate Source | Exact Source Locator Known? | Risk | Formalization Starting Status | Alignment Review Needed? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `definition.tree` | definition | Graph theory | Already accepted; do not re-add. Future work is source-note migration or locator tightening only. | `definition.graph`, `definition.connected`, `definition.acyclic` | Diestel, *Graph Theory*, Chapter 1 tree terminology. | Section-level locator recorded; exact preview page remains to be confirmed in current artifact notes. | Low, but convention-sensitive. | `planned` unless actually checked. | Yes, before relying on any external formal-library tree convention. |
| `definition.degree` | definition | Graph theory | Already accepted; do not re-add. Future work is source-note migration or locator tightening only. | `definition.graph`, `definition.vertex`, `definition.edge` | Diestel, *Graph Theory*, Chapter 1 degree terminology. | Section-level locator recorded; exact preview page remains to be confirmed in current artifact notes. | Low, with simple-graph convention notes required. | `planned` unless actually checked. | Yes, before relying on external formal-library degree symbols. |
| `definition.walk` | definition | Graph theory | Candidate for a future small PR. | `definition.graph`, `definition.vertex`, `definition.edge` | Diestel, *Graph Theory*, Chapter 1 walk/path terminology, or another stable graph-theory text if Diestel locator is insufficient. | Unknown; must be confirmed before acceptance. | Low to medium, because walk conventions vary by repeated vertices/edges and length-zero cases. | `planned` unless actually checked. | Yes, because formal libraries often encode walks differently. |
| `definition.connected-graph` | definition | Graph theory | Candidate for a future small PR only if it adds value beyond `definition.connected`; otherwise record as an alias or defer. | `definition.graph`, `definition.connected`, `definition.path` | Diestel, *Graph Theory*, Chapter 1 connectedness terminology. | Section-level locator exists for connectedness; exact page should be confirmed before a new accepted alias. | Low, but duplication risk is real. | `planned` unless actually checked. | Yes, especially if mapped to an external predicate name. |
| `definition.subgraph` | definition | Graph theory | Already accepted; do not re-add. Future work is source-note migration or locator tightening only. | `definition.graph`, `definition.vertex`, `definition.edge` | Diestel, *Graph Theory*, Chapter 1 subgraph terminology. | Section-level locator recorded; exact preview page remains to be confirmed in current artifact notes. | Low. | `planned` unless actually checked. | Yes, because subgraph encodings vary by induced/non-induced convention. |
| `definition.clique` | definition | Graph theory | Candidate for a future small PR. | `definition.graph`, `definition.vertex`, `definition.edge`, possibly `definition.subgraph` | Diestel, *Graph Theory*, Chapter 1 complete graph/subgraph terminology, or another stable graph-theory text with an explicit clique definition. | Unknown; must be confirmed before acceptance. | Medium, because clique may be defined as a vertex set, complete subgraph, or maximal complete subgraph in some contexts. | `planned` unless actually checked. | Yes, to align set/subgraph conventions. |
| `definition.independent-set` | definition | Graph theory | Candidate for a future small PR. | `definition.graph`, `definition.vertex`, `definition.edge`, possibly `definition.subgraph` | Diestel, *Graph Theory*, Chapter 1 independence terminology, or another stable graph-theory text with an explicit independent-set definition. | Unknown; must be confirmed before acceptance. | Medium, because terminology can differ between vertex independence and edge independence. | `planned` unless actually checked. | Yes, to align vertex-set and no-edge conventions. |
| `definition.matching` | definition | Graph theory | Candidate for a future small PR. | `definition.graph`, `definition.vertex`, `definition.edge` | Diestel, *Graph Theory*, Chapter 1 matching terminology, or another stable graph-theory text with an explicit matching definition. | Unknown; must be confirmed before acceptance. | Medium, because matching conventions interact with simple graphs, endpoints, and maximal/maximum terminology. | `planned` unless actually checked. | Yes, before mapping to external library matching structures. |
| `definition.cnf-formula` | definition | Boolean satisfiability | Candidate for a future small PR after graph basics are stable. | Candidate prerequisite definitions for Boolean variable, literal, clause, and formula, or explicit external references if those are not yet local artifacts. | Sipser, CLRS, or a stable SAT/complexity text with explicit CNF terminology. | Unknown; must be confirmed before acceptance. | Medium, because formula syntax and encoding conventions must be stated carefully. | `planned` unless actually checked. | Yes, before relating to SAT solver or formal-library encodings. |
| `definition.sat-instance` | definition | Boolean satisfiability | Candidate for a future small PR after `definition.cnf-formula` or equivalent prerequisites exist. | `definition.cnf-formula`, plus prerequisite Boolean syntax artifacts or explicit external references. | Sipser, CLRS, or a stable SAT/complexity text with explicit SAT-instance terminology. | Unknown; must be confirmed before acceptance. | Medium, because decision-problem, assignment, and encoding boundaries must be explicit. | `planned` unless actually checked. | Yes, before relating to solver results or formal-library encodings. |

## Follow-Up Order

1. Add durable source-note conventions before adding more artifacts.
2. Add or migrate source notes for the stable graph-theory book source already
   used by accepted graph definitions.
3. Tighten source locators for existing accepted definitions where a reviewer
   can confirm exact pages or sections. Do not guess page numbers.
4. Add at most one new foundation definition per PR unless the dependencies are
   inseparable and the review scope remains small.
5. Do not add new theorem or proof-sketch packs until this backlog and the
   source-note convention are in place.

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
