# Cross-Check Report Policy

Workflow cross-check reports, workflow evidence reports, workflow gap reports,
checker-run sidecars, and checker/cross-check eval outputs are public review
context only when they appear in or near this repository.

They may help maintainers inspect a public KB PR by showing what a workflow or
checker surface reported, but they do not change the accepted knowledge
boundary.

These records must not be used as:

- source metadata for an accepted artifact;
- accepted proof;
- accepted theorem or accepted refutation;
- human review;
- verifier pass;
- gate pass;
- accepted status;
- promotion authority.

Skipped, unsupported, unavailable, and inconclusive checker outputs are not
passes. A checked-pass result is still not human review, source metadata,
accepted status, or proof authority.

If a public KB PR includes cross-check material, it must be public-safe review
context. It must not contain private workspace paths, private KB content,
secrets, hidden reasoning, raw provider payloads, or authority fields that
claim accepted writes, source metadata creation, human review creation,
verifier mutation, gate mutation, or promotion.

Accepted public artifacts still require complete source metadata, validation,
gates, and maintainer human review under the ordinary public KB promotion
policy. Cross-check reports can point to gaps that reviewers should resolve,
but the reports cannot resolve those gaps by themselves.
