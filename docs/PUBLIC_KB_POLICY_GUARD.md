# Public KB Policy Guard

`scripts/check_public_kb_policy.py` is a repository-local CI guard for common
public KB policy mistakes. It complements `cosheaf validate` and
`cosheaf gate run`; it does not replace human review.

The guard checks public KB YAML records for:

- accepted artifacts without source metadata;
- accepted artifacts without human review metadata;
- public artifacts depending on private artifacts;
- skipped verifier results presented as passes;
- operator, MCP, provider, LLM, or agent output structurally claimed as human
  review;
- operator, MCP, provider, LLM, or agent output structurally claimed as
  verifier-pass authority;
- operator handoff records structurally claimed as accepted artifact source
  metadata;
- operator handoff exports under `reviews/operator/` that contain private
  paths, secrets, hidden reasoning, raw provider payload markers, or authority
  fields set to true;
- checked formalizations without checker evidence;
- private-looking paths, tags, or explicit private/unpublished markers inside
  public KB records.

Run it locally with:

```bash
python scripts/check_public_kb_policy.py
python scripts/check_public_kb_policy.py --self-test
```

The self-test creates temporary positive and negative fixtures. Negative
fixtures must fail; the positive fixture must pass.

This guard does not prove source correctness, formal/informal semantic
alignment, or theorem validity. Human review remains required for accepted
public artifacts, and validation/gate success is not human review.
It also does not prove that artifact `failure_log` entries are complete,
source-reviewed, or semantically correct; reviewers must apply
`docs/FAILURE_LOG_POLICY.md` when failure memory is added or changed.
Operator policy is documented in `docs/OPERATOR_POLICY.md` and
`docs/OPERATOR_HANDOFF_POLICY.md`; the guard only checks common
authority-spoofing and public-safety patterns and does not replace maintainer
review.

`formal-libs/lean-libraries.example.yaml` is a local metadata manifest used by
G10 to resolve planned `library_ref` values. It is not checker evidence and
does not make planned CSLib links checked.
