# Contributing To The Public KB

This repository stores public, citable TCS knowledge for TCS-Cosheaf. Keep each
contribution small enough for source review.

## Start With An Issue

Use the most specific issue template:

- definition artifact proposal;
- theorem or claim artifact proposal;
- source note proposal;
- formal link proposal;
- alignment review request.

Use the generic KB artifact routing template only when none of the specific
templates fits. Every proposal must state its scope, source metadata, statement,
dependency list, review status, formalization status, known limitations, and
confirmation that no private material is included.

## Accepted Knowledge Boundary

Accepted public artifacts require:

- complete artifact-local source metadata;
- public-only dependencies;
- validation and gate results;
- human review evidence under `reviews/human/`;
- promotion through the repository workflow.

Validation or gate success is not human review. LLM output is not human review.
Do not mark LLM-generated content accepted without maintainer human review.

## Source And Review Rules

Do not fabricate page, theorem, lemma, chapter, section, or equation locators.
If a locator is uncertain, record the uncertainty explicitly.

Do not include private conjectures, unpublished research ideas, private proof
attempts, or private workspace material. Public artifacts here must not depend
on private artifacts.

Proof sketches are explanatory and source-reviewed, not machine-checked proofs.
Formal links are metadata unless a real checker verifies them and records
evidence. Planned formal links do not mean Lean, CSLib, mathlib, SAT, SMT, or
semantic alignment has been checked.

Failure logs are public research memory only. Do not include private workspace
failure notes, unreviewed provider or agent failure dumps, secrets, or claims
that a failure log proves, refutes, verifies, reviews, accepts, or promotes an
artifact. See `docs/FAILURE_LOG_POLICY.md`.

Research loop outputs are public review context only. Do not use them as
source metadata, accepted proof, human review, verifier pass, gate pass,
accepted status, accepted refutation, or promotion authority. Do not copy
private loop material, provider dumps, hidden reasoning, or secrets into this
repository. See `docs/RESEARCH_LOOP_POLICY.md`.

## PR Scope

One issue should normally become one branch and one PR. Avoid mass imports.
Future foundation artifacts should land as separate PRs unless the dependency
surface is inseparable and still reviewable.

Run the repository checks before opening a PR:

```bash
cosheaf workspace info
cosheaf validate
cosheaf gate run
cosheaf gate run --pr-checklist .github/pull_request_template.md
git diff --check
```
