# Source Notes

Source notes are durable bibliographic records for sources reused across public
KB artifacts. They help maintainers cite the same book, paper, or web source
consistently across small artifact PRs.

Source notes are repository metadata. Under the current framework policy, they
do not replace source metadata required inside accepted artifact YAML. Accepted
public artifacts still need complete artifact-local source metadata and human
review evidence.

## Directory Convention

Use one source note per durable source:

- `sources/books/` for books, textbooks, and stable book previews.
- `sources/papers/` for papers, preprints, proceedings papers, and technical
  reports.
- `sources/web/` for durable web references that are not better represented as
  books or papers.

This policy defines the convention only. Future PRs may add these directories
and individual source-note files as small, reviewable changes.

## Recommended Fields

Each source note should be concise and structured enough for a reviewer to
relocate the source:

- `id`: stable source-note identifier.
- `kind`: `book`, `paper`, `web`, or a similarly specific source kind.
- `title`: source title.
- `authors`: source authors or maintainers.
- `year`: publication year or version year when known.
- `edition_or_version`: edition, revision, preview version, arXiv version, or
  web page version when applicable.
- `url`: stable URL when available.
- `doi`: DOI when available.
- `arxiv`: arXiv identifier when available.
- `notes`: bibliographic or access notes.
- `artifact_usage_notes`: how artifacts in this repository use the source.

The repository may store source notes as Markdown, YAML, or another documented
format later. Until a schema is adopted, keep source notes human-readable and
reviewable.

## Locator Policy

Do not fabricate page, theorem, lemma, chapter, section, or equation locators.
If an exact locator is not confirmed, say so explicitly and use the most precise
verified locator available.

Examples of acceptable uncertainty:

- `Chapter 1, Section 1.3; exact preview page to be confirmed.`
- `Textbook source candidate; exact theorem number not yet confirmed.`
- `Web source reviewed on <date>; no stable section anchor found.`

Examples that are not acceptable:

- A guessed page number.
- A theorem number inferred from memory.
- A vague citation presented as exact.
- A source note used to make an accepted artifact look reviewed when no human
  review happened.

## Artifact Policy

Source notes are additional durable records. They do not weaken accepted
artifact requirements:

- Accepted public artifacts require complete source metadata.
- Accepted public artifacts require human review.
- Validation and gate success are not substitutes for human review.
- Source notes do not make LLM-generated content accepted.
- Source notes do not prove formal/informal semantic alignment.

Proof sketches remain explanatory and source-reviewed, not machine-checked.
They must not claim Lean, CSLib, mathlib, SAT, SMT, or other checker results
unless a real checker actually ran and recorded a result.

## Migration Guidance

Do not mass-migrate existing artifacts. Prefer small PRs:

1. Add one durable source note.
2. Point one or a few related artifacts to the note in prose or metadata when
   the current schema supports it.
3. Keep existing artifact-local source metadata intact unless the framework
   policy later supports source-note references as a validated substitute.
4. Update human review notes when bibliographic precision changes.
5. Run validation and gates before opening the PR.
