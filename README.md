# TCS Public Knowledge Base

This repository is the public reusable theoretical computer science knowledge base for TCS-Cosheaf.

It contains public, citable definitions, constructions, reductions, counterexamples, and reviewed knowledge artifacts. It is intended to be mounted by user workspaces as a readonly KB root, with private research stored in a separate writable overlay.

## Layout

- `kb/public/definitions/`: public definition artifacts.
- `kb/public/theorems/`: public theorem artifacts after source and review policy is satisfied.
- `kb/public/constructions/`: public construction artifacts.
- `kb/public/reductions/`: public reduction artifacts.
- `kb/public/counterexamples/`: public counterexample artifacts.
- `sources/`: source notes and bibliographic metadata.
- `reviews/human/`: human review records.
- `reviews/ai/`: AI-assisted review notes.
- `reviews/gatekeeper/`: validation and gatekeeper review outputs.
- `docs/`: repository policies.

## Policy

This repository does not contain private conjectures, unpublished research ideas, or accepted LLM-generated artifacts without human review. New knowledge should normally begin as a GitHub issue and land as a small PR.

The seed artifacts in this repository are tiny `draft` examples. They are not accepted theorem artifacts.

## Local Commands

Install or otherwise make `cosheaf` available, then run:

```bash
cosheaf validate
```

Downstream workspaces should include this repository as a readonly public KB root and keep private work in a separate writable root.
