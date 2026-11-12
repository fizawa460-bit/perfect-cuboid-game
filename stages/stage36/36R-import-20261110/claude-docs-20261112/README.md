# Stage36 / Stage38 Claude Docs snapshot (2026-11-12)

The Drive 36R `00_START-HERE` names five Claude Docs as the live authority for RESULTS,
WORKING, INDEX and LOG. They were not in GitHub. This folder copies them, exported on
2026-11-12 through the Claude Docs connector. GitHub is now the authority.

Content was copied as exported. Nothing was edited or re-certified.

| File | Claude Docs id | Doc revision | Format |
|---|---|---|---|
| `RESULTS.md` | `dcb03d7b-1596-44fa-97f8-dae72a9d434b` | 20 | Markdown export. R-1 to R-23, plus the Stage38-L1 closure. |
| `WORKING.pdf` / `WORKING.txt` | `f6e71910-0ece-4bf7-a3aa-233099283357` | 27 | PDF export, plus text extracted with `pdftotext -layout`. |
| `INDEX.pdf` / `INDEX.txt` | `7dc1abd2-281e-4f24-a85e-5c50221b0f1e` | 59 | PDF export, plus extracted text. Logs to 1T and L1. |
| `LOG.md` | `ceefcc13-248b-4187-992e-847c93123030` | 59 | Markdown export. Main log 0D to 1T. |
| `LOG-L1.md` | `f2b35121-4ebb-4d87-be2a-d5e1b9aae631` | 22 | Markdown export. Stage38 L1-00 to L1-1E (CLOSED). |

WORKING and INDEX are stored as PDF because the connector returned their Markdown export only
inline; it was too short to be saved as a file. Writing that inline text out by hand risked
copying errors, so PDF was used instead.

Status: Stage36 is frozen (`../../STAGE36-FROZEN-20261112.md`). These are records, not new
claims. Labels such as "candidate" or "unreviewed" inside the docs keep their meaning.
