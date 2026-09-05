# Context-safe repository file inspection

## Trigger

Open this policy only when a task may require reading a repository file whose size or representation could materially inflate assistant/chat context, or when a file is known/suspected to contain generated, encoded, compressed, minified, binary-like, single-line, or otherwise opaque payloads.

This policy governs **how** repository files are inspected. It does not authorize broader repository traversal and does not weaken Stage-local startup, source-lock, or authority rules.

## Hard gate before whole-file reads

Before whole-fetching or whole-opening any repository file, establish its byte size from metadata **without reading the target file contents**.

Acceptable metadata paths include:

- local clone: `git cat-file -s <ref>:<path>` or `git ls-tree -l <ref> -- <path>`;
- GitHub: immediate-parent directory listing or non-recursive tree metadata and the target entry's `size` field.

Do not fetch the target file itself merely to learn its size.

Apply all of the following rules:

1. If byte size is unknown, treat the file as unsafe for a whole-file read.
2. Files `>= 65536` bytes (64 KiB) must not be whole-fetched into assistant/chat context.
3. **Size alone is not a safety test.** Generated, encoded, compressed, minified, binary-like, single-line, or opaque-payload files must not be whole-fetched when the active question can be answered through a compact adapter, loader, verifier, hash, locator, or bounded structured output — even when the repository blob itself is small.
4. Do not use line-range fetching as a workaround for a suspected encoded/minified/single-line payload. One logical line may contain the entire object.
5. Never expand Base64, Base85, compressed retained payloads, packed matrices, or equivalent opaque blobs into assistant/chat context merely to inspect them.

## Preferred inspection pattern

Make the repository or runner perform the heavy read and emit only the smallest deterministic result needed for the active leaf. Prefer, in order:

1. an existing loader, adapter, certifier, or verifier;
2. locked blob/canonical hashes plus already-retained metadata;
3. a tiny repo-side script that imports/decodes the payload and prints bounded JSON/text;
4. exact locator extraction for named fields, rows, ranks, witnesses, supports, hashes, or counts;
5. bounded structured excerpts only when the file representation is known to be context-safe.

Compact outputs should contain only task-relevant values such as dimensions, ranks, supports, selected rows, canonical hashes, witness labels, boolean checks, or exact source locators. Do not print the underlying retained payload unless the task explicitly requires it and it independently passes this policy.

## Permanent whole-fetch denylist

The following retained files must not be whole-fetched into assistant/chat context and must not be inspected via line-range fetching as a workaround:

- `stages/stage33/33-07/picard_base_rows_retained.py`
- `stages/stage33/33-07/stage32_picard_marking_retained.py`

Use their existing loaders/adapters, locked hashes/metadata, or a lightweight repo-side verifier instead.

The denylist is representation-based, not byte-threshold-based: a compact Python wrapper can still hide a much larger encoded or compressed retained object.

## Stop conditions

Stop direct inspection and switch to a compact repo-side method when any of the following holds:

- size metadata is unavailable;
- the file crosses the 64 KiB threshold;
- content is generated/encoded/compressed/minified/binary-like/opaque;
- a single line may contain a large packed payload;
- the tool would return substantially more data than the active question requires.

If no compact method can establish the required fact, record that limitation rather than consuming an unbounded payload.

## Relationship to other repository rules

Repository discovery remains search-first and non-recursive under `AGENTS.md`. This policy does not permit recursive/full-tree acquisition. Stage-local authority still determines which files are relevant, and source-lock/certificate rules still determine which results may receive research credit.
