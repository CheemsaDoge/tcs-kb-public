# Operator And MCP Policy

This repository may use operator, Codex, MCP, provider, research-run, checked
evidence, or strategy-plan outputs as public review context. None of those
outputs changes the accepted knowledge boundary.

## Authority Boundary

Operator and MCP outputs are not:

- human review;
- source metadata;
- proof;
- verifier pass;
- gate pass;
- checked formalization evidence;
- accepted status;
- accepted refutation;
- promotion authority.

Accepted public artifacts still require complete artifact-local source
metadata, validation, gate results, and maintainer human review under the
normal public KB policy.

## Allowed Use

A public KB PR may include operator or MCP output only as bounded review
context, for example:

- a research-run record listing commands that were run;
- a strategy review export describing candidate next steps;
- a draft source-note or draft artifact proposal;
- a checked-evidence record that preserves method, support, result, and
  limitations.

These records must be public-safe and must not include private workspace
material, private context packs, API keys, `.env` contents, hidden reasoning,
unreviewed provider dumps, or full private KB text.

## Forbidden Use

Do not use operator, Codex, MCP, provider, LLM, or agent output to:

- mark `review.state: human_reviewed`;
- fill structured review authority fields such as `reviewer_kind`,
  `review_source`, `origin`, or `created_by` as if they were human reviewers;
- record a verifier result as pass without a real checker result;
- turn skipped, unavailable, failed, or inconclusive rows into passes;
- move draft or review-context material into `kb/public/accepted/`;
- justify accepted promotion without maintainer review.

The public KB policy guard rejects accepted artifacts that structurally claim
operator/model output as human review and rejects verifier-pass records that
structurally identify operator/model output as the checker authority.

## Downstream Workspace Boundary

Downstream workspaces should mount this public KB readonly and keep private
operator output in their private overlay or ignored runtime paths. A downstream
operator record should enter this public KB only through an explicit public KB
PR after maintainers confirm that it is public, useful as review context, and
free of private material.

Do not manually merge framework, public KB, and private workspace repositories
into one mixed tree.
