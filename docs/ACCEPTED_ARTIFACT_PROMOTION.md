# Accepted Artifact Promotion Checklist

This repository may prepare tiny public KB artifact candidates as drafts, but accepted knowledge requires real human review. Validation and gate results are not a substitute for maintainer review.

## Current Accepted Layout

Accepted public artifacts live under `kb/public/accepted/`:

- `definitions/` for accepted definition artifacts;
- `theorems/` for accepted theorem artifacts;
- `proofs/` for accepted proof or proof-sketch artifacts.

Draft public proof artifacts live under `kb/public/draft/proofs/` until they
are reviewed and promoted. Do not infer accepted status from a type-specific
public KB directory outside `accepted/`; the artifact `status` field and the
status/path gate determine whether an artifact is accepted.

## Promotion Preconditions

Before promotion, a maintainer must verify and record that:

- the artifact statement matches the cited source;
- source metadata is complete;
- the artifact contains no private idea, conjecture, proof attempt, or unpublished research note;
- the artifact is suitable for the public KB;
- dependencies are public only;
- validation and gate checks pass.

Only after those requirements are genuinely satisfied should the maintainer update the review evidence and run the artifact-specific promotion command:

```bash
cosheaf artifact promote <artifact-id>
```

Do not run promotion while `review.state` is `requested`, and do not mark an artifact as `human_reviewed` unless a human maintainer has actually completed the review.
