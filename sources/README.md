# Sources

Use this directory for source notes, bibliographic metadata, and
source-ingestion records. Do not bulk-import papers. Add sources in small
reviewable batches tied to GitHub issues.

See `../docs/SOURCE_NOTES.md` for the source-note convention.

Planned source-note subdirectories:

- `books/`
- `papers/`
- `web/`

Source notes do not replace the source metadata currently required inside
accepted artifact YAML. Accepted public artifacts still require complete source
metadata, validation and gate results, and human review evidence.

Backlog rows that only have a broad or placeholder source should be marked
`needs_source` until a durable source note and artifact-local source metadata
are available. Rows that have a source note but still lack an exact page,
section, theorem, or URL locator should be marked `needs_source_locator`.
