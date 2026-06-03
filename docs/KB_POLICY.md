# Public KB Policy

This repository stores public, citable TCS knowledge only.

## Repository Boundary

This repository is the public reusable KB. It is writable only for public KB
maintainers through focused PRs. Downstream users should normally consume it
through
[`tcs-cosheaf-workspace-template`](https://github.com/CheemsaDoge/tcs-cosheaf-workspace-template),
where it is mounted readonly beside a writable private KB overlay.

Do not manually merge this public KB with the `tcs-cosheaf` framework repository
or with a private workspace. Private downstream artifacts may depend on public
artifacts here, but public artifacts here must not depend on downstream private
artifacts.

## Allowed Content

- Public definitions with clear terminology.
- Public constructions with cited sources or standard references.
- Public reductions, counterexamples, and theorem statements after review.
- Draft artifacts clearly marked with `status: draft`.
- Review records and gate outputs.

## Disallowed Content

- Private conjectures.
- Unpublished research ideas.
- Private proof attempts.
- Accepted theorem artifacts without source metadata.
- LLM-generated accepted artifacts without human review.
- Mass imports of papers or large batches that cannot be reviewed.

## Promotion

Draft artifacts may be promoted only after complete source metadata,
validation, gate results, and human review have been recorded. Passing
validation is not enough to mark an artifact accepted.
