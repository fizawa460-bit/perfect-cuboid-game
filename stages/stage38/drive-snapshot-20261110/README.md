# Stage38 Drive source mirror (2026-11-10)

[Machine-readable complete manifest](MANIFEST.json): **83 source files across 4 explicitly listed folders**, not a repository-wide/Drive-wide enumeration.

| Folder | Drive items | Files | Stored form |
| --- | ---: | ---: | --- |
| [Stage38 root](https://drive.google.com/drive/folders/1MFh08y2Z7HEy3PtZLuQjkwrZHtfnL1is) | 52 | 50 | 49 text sources in `root38/bundle-00.json` through `bundle-09.json`; 1 ZIP as Base64 |
| [01_reference](https://drive.google.com/drive/folders/17wTdsxwGCFYRp7O2cmmUYUgvoyEn49cx) | 29 | 28 | 26 source texts in `reference38/bundle-00.json` through `bundle-05.json`; 1 ZIP Base64; 1 native Google Docs text snapshot |
| [02_audit](https://drive.google.com/drive/folders/1R-gTOfdxeH9EZexmblTE9KcHOxf-GsFs) | 2 | 2 | `audit38/bundle-00.json` |
| [claude_code_handoff_1T](https://drive.google.com/drive/folders/1-X6l158m-UN8yCrMdO9tiTCU_Q4Wp3Pg) | 3 | 3 | `handoff1T/bundle-00.json` |

All **80 text files** are embedded as individual `{title,id,url,mime,size,modified,content}` records in JSON bundles, preserving the complete retrieved text with source IDs. All source scripts can be reconstructed as separate files with [extract_bundle.py](extract_bundle.py).

Two ZIP files have been copied as fully reversible `.zip.base64` source files. Restore with `base64 -d filename.zip.base64 > filename.zip`. The native Google Doc `LOG_OPENAI_MATH_STAGE38_REVIEW` was copied as its current text paragraphs with a revision ID, not a layout-identical export.

Source chronology: Stage38 L1 **CLOSED**, L2 externally promoted results **R-19, R-21, R-22** (as reported by Drive), L3 1G–1T **frozen unreviewed candidates**, and Stage38 **CLOSED_FOR_NOW**. Stage36 resumed as 36R and reached **PARKED_PROVISIONAL** in its separate 2026-10-16 folder. No Campedelli receiver or perfect-cuboid closure is asserted.

**Important:** the copies of `CAMPEDELLI_RESULTS.md`, `CAMPEDELLI_WORKING.md`, and `00_INDEX.md` in Stage38 root reach only R-14 / log 0C. The subsequent authoritative RESULTS, WORKING, INDEX and 0D–1T logs are in external Claude Docs and are not present here. Do not present these historical Drive snapshots as those live documents.

The mirror is a **source transfer**, not a mathematical review or theorem promotion. Google Drive remains the original-source authority.
