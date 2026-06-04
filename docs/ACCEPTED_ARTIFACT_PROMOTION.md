# Accepted Artifact Promotion Checklist

This repository may prepare tiny public KB artifact candidates as drafts, but accepted knowledge requires real human review. Validation and gate results are not a substitute for maintainer review.

## Current Pilot Candidate

- Artifact: `definition.graph`
- Current required status before review: `draft`
- Current required review state before review: `requested`
- Human review request: `reviews/human/review.definition.graph.md`

## Promotion Preconditions

Before promotion, a maintainer must verify and record that:

- the artifact statement matches the cited source;
- source metadata is complete;
- the artifact contains no private idea, conjecture, proof attempt, or unpublished research note;
- the artifact is suitable for the public KB;
- dependencies are public only;
- validation and gate checks pass.

Only after those requirements are genuinely satisfied should the maintainer update the review evidence and run:

```bash
cosheaf artifact promote definition.graph
```

Do not run promotion while `review.state` is `requested`, and do not mark an artifact as `human_reviewed` unless a human maintainer has actually completed the review.
