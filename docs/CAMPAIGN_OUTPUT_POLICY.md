# Campaign Output Policy

Campaign handoffs, campaign eval reports, scorecards, attempts, and
`operator_task_v2` packets are public review context only when they appear in
or near this repository.

They must not be used as:

- source metadata for an accepted artifact;
- accepted proof;
- accepted theorem or accepted refutation;
- human review;
- verifier pass;
- gate pass;
- accepted status; or
- promotion authority.

Campaign success, budget-stop accuracy, or eval pass means only that the
campaign surface produced a reviewable sidecar result. Accepted public
artifacts still require complete artifact-local source metadata, validation,
gates, and maintainer human review under the ordinary public KB promotion
policy.

Public KB campaign records must be marked `review_context_only: true` and must
not contain private workspace paths, private KB content, secrets, hidden
reasoning, raw provider payloads, or authority fields that claim accepted
writes, source metadata creation, human review creation, verifier mutation,
gate mutation, accepted status/refutation, or promotion.

`scripts/check_public_kb_policy.py` rejects common structural misuse of
campaign outputs, but it does not prove that a campaign output is complete,
semantically correct, or adequate for review. Human review remains required.
