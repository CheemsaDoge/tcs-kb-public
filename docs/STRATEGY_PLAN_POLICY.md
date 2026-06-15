# Strategy Plan Policy

Strategy plans are public review context only. They can help maintainers see
which bounded steps, commands, blockers, and references were considered while
preparing a public KB PR, but they do not change the accepted knowledge
boundary.

This policy applies to strategy plans, strategy review exports, and references
to strategy task graphs in this public KB.

## Authority Boundary

Strategy plans are not:

- source metadata;
- validation success;
- gate success;
- verifier evidence;
- checked counterexample evidence;
- human review;
- proof or accepted refutation;
- accepted status;
- promotion authority.

Accepted public artifacts still require complete source metadata, validation,
gate results, and human review under the normal public KB policy. A strategy
plan may point reviewers to those records, but it cannot replace them.

## Public And Private Boundaries

Do not copy private strategy plans, private context packs, private research-run
records, private proof attempts, or downstream workspace notes into this public
KB.

A public KB PR may include a strategy review export only when maintainers have
confirmed that it is public-safe and contains no private workspace material,
secrets, hidden reasoning, API keys, unreviewed provider dumps, or full private
KB text. The export must remain clearly non-authoritative review context.

## Candidate And Checked Evidence

Strategy plans may reference candidate counterexamples or checked
counterexample evidence, but the labels must remain distinct:

- `candidate_counterexample` is proposed evidence only;
- checked counterexample evidence requires a separate checked-evidence record
  with method, result, support references, checker label, and limitations.

Checked evidence can support maintainer review, but it does not by itself
create accepted refutation, accepted status, verifier pass, gate pass, human
review, or promotion authority.

## Review Checklist

When a public KB PR includes strategy-plan material, reviewers should verify:

- the strategy material is public-safe and does not leak private workspace
  context;
- it does not claim proof, accepted refutation, accepted status, human review,
  verifier pass, gate pass, or promotion authority;
- source metadata for accepted artifacts remains complete;
- validation and gate results are still run and reported separately;
- candidate counterexamples are not mislabeled as checked evidence;
- checked evidence references preserve method, result, support, and
  limitations;
- skipped, unavailable, failed, or inconclusive rows are not counted as passes;
- no hosted-provider, LLM, or agent output is marked as human review.

## Downstream Workspace Boundary

Downstream workspaces should keep local strategy plans under ignored runtime
paths or private workspace records. A downstream strategy plan should enter this
public KB only through an explicit public-KB PR after maintainers confirm that
it is public, useful as review context, and free of private material.

Do not add a strategy plan to justify promoting a draft artifact. Promotion
still requires the ordinary accepted-artifact workflow.
