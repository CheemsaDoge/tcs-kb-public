# Source Note Policy

Source notes provide durable bibliographic records for sources reused across
public KB artifacts. They make citation practice more consistent, but they do
not weaken accepted-artifact requirements.

The detailed convention is in `docs/SOURCE_NOTES.md`.

## One Note Per Durable Source

Use one source note per durable book, paper, or web source:

- `sources/books/` for books, textbooks, and stable book previews;
- `sources/papers/` for papers, preprints, proceedings papers, and technical reports;
- `sources/web/` for durable web references.

Each source note should record source identity, authors, year, edition or
version, URL/DOI/arXiv when applicable, notes, and artifact usage notes.

## Artifact Metadata Still Required

Under current framework policy, source notes do not replace artifact-local
source metadata. Accepted public artifacts still require complete source
metadata in the artifact YAML and human review evidence under `reviews/human/`.

## Locator Discipline

Do not fabricate page, theorem, lemma, chapter, section, or equation locators.
If an exact locator is not confirmed, record the uncertainty and use the most
precise verified locator available.

## Review Boundary

Source notes are not human review records. Validation or gate success is not
human review. A source note can support review, but it cannot make an artifact
accepted by itself.

Proof sketches remain explanatory and source-reviewed, not machine-checked.
Formal links remain metadata unless a real checker runs and records evidence.
