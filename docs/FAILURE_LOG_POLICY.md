# Failure Log Policy

Artifact-level `failure_log` entries are public research memory. They can help
maintainers and downstream users avoid repeating known dead directions, source
locator mistakes, failed formalization mappings, or reviewed counterexample
search attempts. They are not proof, refutation, verifier evidence, human
review, gate success, accepted status, or promotion evidence by themselves.

This policy applies to failure-log entries stored in this public KB. Downstream
workspace-private failure memory belongs in the downstream private KB, not in
this repository.

## Appropriate Uses

Failure logs may be appropriate in draft public artifacts when they record
public, reviewable information such as:

- a source locator that was checked and found unsuitable;
- a proof-sketch or definition convention that was rejected during review;
- a formal-library symbol or import mapping that did not align with the
  artifact convention;
- a verifier or counterexample-search direction that failed without producing
  checked evidence;
- a maintainer-reviewed limitation that future contributors should see before
  attempting the same direction again.

Failure logs may appear in accepted public artifacts only when the entry is
public, citable or reviewable, relevant to the accepted artifact, and reviewed
as part of the ordinary accepted-artifact workflow. Accepted-path failure logs
must be maintained with the same care as other accepted artifact metadata:
complete source context where relevant, public-only dependencies, validation,
gates, and human review.

## Draft Versus Accepted Failure Memory

Draft failure memory is working review context. It can explain what a maintainer
or contributor tried while preparing a public artifact, but it must remain
clearly non-authoritative.

Accepted failure memory is reviewed public metadata. It can document a known
failed direction or limitation for an accepted artifact, but it still does not
become proof, refutation, verifier success, checked counterexample evidence, or
human review by itself.

Changing `failure_log.status` to `resolved`, `superseded`, `invalidated`, or
`archived` does not prove the artifact, refute the artifact, complete human
review, or promote the artifact. It only records the state of that failure
memory entry.

## Disallowed Content

Do not add failure-log entries that contain:

- private conjectures, private proof attempts, unpublished research ideas, or
  downstream workspace material;
- secrets, credentials, API keys, private provider prompts, or private context;
- unreviewed LLM, hosted-provider, or agent failure dumps in accepted public
  paths;
- claims that a failure log is human review, checker evidence, accepted
  knowledge, or promotion evidence;
- claims that a candidate counterexample is checked without separate checked
  counterexample evidence and review;
- source locators, theorem numbers, page numbers, or formal-library symbols
  that are guessed or presented as confirmed without review.

Provider, agent, or model output may support a draft proposal only when it is
kept out of accepted knowledge and reviewed by a maintainer. It must preserve
its origin and limitations.

## Review Requirements

When a PR adds or changes failure-log entries, reviewers should check:

- the entry is public and does not leak private workspace material;
- `origin`, `attempt_kind`, `status`, and `limitations` are explicit;
- the entry does not claim proof, refutation, verifier success, human review,
  gate success, accepted status, or promotion evidence;
- source-related failures include real locators or explicit uncertainty;
- verifier, formal-link, SAT, SMT, Lean, mathlib, CSLib, and counterexample
  language is not overstated;
- accepted-path entries have human review evidence and satisfy the ordinary
  accepted-artifact policy.

Validation and gate success remain workflow checks. They are not human review
and do not make failure memory accepted public knowledge.

## Downstream Workspace Boundary

Downstream workspaces should mount this public KB readonly and keep local
failure memory in their private writable KB overlay. A downstream private
failure log should enter this public KB only through an explicit public-KB PR
after maintainers confirm that it is public, useful, source/review disciplined,
and free of private context.

Do not copy a downstream private artifact into this repository just to preserve
failure memory. Prepare a focused public PR instead.
