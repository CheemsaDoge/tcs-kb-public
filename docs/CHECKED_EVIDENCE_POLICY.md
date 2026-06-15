# Checked Evidence Policy

This repository may record checked counterexample evidence and research-run
provenance as review context, but neither surface changes the accepted
knowledge boundary.

## Scope

Checked counterexample evidence is a public, reviewable record that a specified
method checked a candidate counterexample. It is different from:

- a `candidate_counterexample`, which is proposed evidence only;
- verifier requests, which ask for checks but are not results;
- verifier evidence, which records tool output but is not human review;
- research-run records, which record operator provenance.

Research-run records may show which commands an operator ran and which outputs
were referenced. They are provenance only.

## Authority Boundary

Checked evidence and research-run records are not:

- proof;
- human review;
- accepted status;
- accepted refutation;
- verifier pass;
- gate pass;
- promotion authority;
- a substitute for source metadata.

Accepted public artifacts still require complete source metadata, validation,
gate results, and human review under the normal public KB policy.

## Accepted Paths

Do not write unreviewed checked evidence, provider output, agent output, or
research-run dumps into accepted public KB artifact paths.

Accepted artifacts may reference checked evidence only when maintainers have
reviewed the evidence, confirmed it is public and citable or otherwise
appropriate for public review context, and preserved the limitations. Such a
reference still does not replace source metadata or human review.

Research-run records must not contain private workspace material, unreviewed
provider dumps, API keys, hidden reasoning, `.env` content, or full private KB
text. Public KB PRs that include run records or review exports must confirm
that the records are public-safe.

## Candidate Vs Checked Evidence

PRs must distinguish:

- `candidate_counterexample`: a proposed counterexample or failure witness
  that still needs checking;
- `checked_counterexample_evidence`: a durable evidence record describing the
  check method, result, support references, checker label, timestamp, and
  limitations.

Do not describe a candidate as checked unless a checked evidence record exists.
Do not describe checked evidence as an accepted refutation unless the accepted
knowledge lifecycle has separately reviewed and updated the relevant artifact.

## Skipped And Inconclusive Results

Skipped, unavailable, inconclusive, error, or failed checks must remain visibly
non-pass. A skipped Lean, SAT, SMT, verifier, provider, network, or operator
step is not evidence that a statement was checked successfully.

## Review Checklist

When checked evidence or run records are included in a public KB PR, reviewers
should verify:

- the record is public and does not leak private workspace material;
- source metadata for accepted artifacts remains complete;
- candidate evidence is not mislabeled as checked evidence;
- checked evidence keeps method, support, result, and limitations visible;
- skipped or inconclusive rows are not counted as passes;
- no AI, provider, or agent review is marked as human review;
- no accepted artifact depends on private or draft material;
- no promotion or accepted-status change is implied by evidence alone.

