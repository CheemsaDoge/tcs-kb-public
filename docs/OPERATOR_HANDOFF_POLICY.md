# Operator Handoff Policy

Operator handoff bundles and `reviews/operator/` exports are public review
context only. They can help a maintainer inspect what an external operator
claims happened during an issue-focused session, but they do not change the
public KB accepted-knowledge boundary.

This policy applies to:

- operator-session records;
- operator handoff bundles;
- `reviews/operator/<handoff-id>.yaml` exports;
- references to downstream workspace handoff records; and
- summaries derived from operator handoff records.

## Authority Boundary

Operator handoff material is not:

- source metadata;
- human review;
- proof;
- verifier evidence;
- verifier pass;
- gate pass;
- accepted status;
- accepted refutation; or
- promotion authority.

Accepted public artifacts still require complete artifact-local source
metadata, validation, gate results, and maintainer human review under the
ordinary public KB policy.

## Allowed Use

A public KB PR may include an operator handoff export only as bounded public
review context, for example:

- to summarize which commands were reported as run;
- to point maintainers to draft artifacts, source-note proposals, or review
  context that still need ordinary review;
- to record skipped, failed, or missing checks explicitly; or
- to make follow-up recommendations visible without granting authority.

The handoff must be public-safe and must keep its limitations visible.

## Forbidden Use

Do not use an operator handoff to:

- fill accepted artifact `sources` or source-note metadata;
- mark `review.state: human_reviewed`;
- identify an operator, model, MCP adapter, provider, or handoff as a human
  reviewer;
- record a verifier pass without a real checker result;
- turn skipped, failed, unavailable, inconclusive, or missing checks into
  passes;
- move draft or review-context material into `kb/public/accepted/`;
- claim accepted status or accepted refutation; or
- justify promotion without maintainer review.

## Public-Safety Requirements

Public KB handoff records must not contain:

- private workspace paths or private artifact IDs;
- private context packs or full private KB text;
- API keys, bearer tokens, `.env` dumps, or environment dumps;
- hidden reasoning or chain-of-thought-like text;
- raw hosted-provider request or response payloads;
- unpublished private conjectures or proof attempts; or
- authority fields that claim accepted writes, human review, promotion, or
  verifier-result mutation occurred.

If a downstream workspace handoff references private material, keep it in the
workspace or private overlay. Do not copy it into this public KB.

## Review Checklist

When a public KB PR includes operator handoff material, reviewers should verify:

- the handoff is public-safe and contains no private workspace material;
- it is clearly labeled as review context only;
- source metadata for accepted artifacts remains complete and independent;
- human review remains a maintainer review record under `reviews/human/`;
- skipped, unavailable, failed, inconclusive, or missing checks are not counted
  as passes;
- verifier results are backed by real checker evidence when claimed;
- no accepted artifact depends on private, draft, or handoff-only material; and
- no promotion or accepted-status change is implied by the handoff alone.

`scripts/check_public_kb_policy.py` catches common structural mistakes, but it
does not prove that a handoff is complete, semantically correct, or adequate
for review. Human review remains required.
