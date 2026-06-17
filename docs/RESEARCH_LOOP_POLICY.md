# Research Loop Policy

Research loop outputs are public review context only. They can help a
maintainer inspect bounded attempts, repeated failures, retry justification,
scanner results, and handoff context from a workspace, but they do not change
the public KB accepted-knowledge boundary.

Research loop outputs are not source metadata and not accepted proof.

This policy applies to:

- bounded research-loop runtime summaries;
- attempt-memory summaries;
- scanner reports;
- task packets and imported operator results;
- downstream workspace references to `.cosheaf/research-loops/`; and
- any `reviews/research-loop/` export that a maintainer explicitly decides to
  include as public review context.

## Authority Boundary

Research loop material is not:

- source metadata;
- accepted proof;
- human review;
- proof;
- verifier evidence;
- verifier pass;
- gate pass;
- accepted status;
- accepted refutation; or
- promotion authority.

Accepted public artifacts still require complete source metadata, validation,
gate results, and maintainer human review under the ordinary public KB policy.
Validation and gate success are not human review.

## Allowed Use

A public KB PR may include a research-loop export only as bounded public review
context, for example:

- to show which attempted directions failed and should not be repeated without
  justification;
- to point maintainers to draft proposals that still need ordinary source
  review;
- to record scanner findings or skipped checks explicitly; or
- to make a follow-up recommendation visible without granting authority.

The export must be public-safe and must keep its limitations visible.

## Forbidden Use

Do not use research-loop output to:

- fill accepted artifact `sources` or source-note metadata;
- mark `review.state: human_reviewed`;
- present a loop, agent, model, operator, or provider as a human reviewer;
- claim accepted proof or accepted refutation;
- record a verifier pass without real checker evidence;
- turn skipped, failed, unavailable, inconclusive, or missing checks into
  passes;
- move draft or review-context material into `kb/public/accepted/`; or
- justify promotion without maintainer review.

## Public-Safety Requirements

Public KB research-loop records must not contain:

- private workspace paths or private artifact IDs;
- private context packs or full private KB text;
- API keys, bearer tokens, `.env` dumps, or environment dumps;
- hidden reasoning or chain-of-thought-like text;
- raw hosted-provider request or response payloads;
- unpublished private conjectures or proof attempts; or
- authority fields that claim accepted writes, accepted proof, source metadata,
  human review, promotion, gate mutation, or verifier-result mutation occurred.

If a downstream workspace loop references private material, keep it in the
workspace or private overlay. Do not copy it into this public KB.

## Review Checklist

When a public KB PR includes research-loop material, reviewers should verify:

- the material is public-safe and contains no private workspace material;
- it is clearly labeled as review context only;
- accepted artifact source metadata remains complete and independent;
- human review remains a maintainer review record under `reviews/human/`;
- skipped, unavailable, failed, inconclusive, or missing checks are not counted
  as passes;
- verifier results are backed by real checker evidence when claimed;
- no accepted artifact depends on private, draft, or loop-only material; and
- no promotion or accepted-status change is implied by the loop alone.

`scripts/check_public_kb_policy.py` catches common structural mistakes,
including research-loop material claimed as source metadata or accepted proof,
but it does not prove that a loop is complete, semantically correct, or
adequate for review. Human review remains required.
