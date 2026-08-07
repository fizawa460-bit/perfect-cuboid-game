#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import html
import subprocess
from pathlib import Path

BUNDLE_ID = "PC-N1-2-FINAL-FULL-REREVIEW-20260807-R04"
COMPLETED_THROUGH = "Stage12-N1-3e"
SOURCE_SNAPSHOT_COMMIT = "efe6ba788fa30e2c8f33b9cc98f99006dde34775"
SOURCE_LEDGER_SHA256 = "9938c98890850d545704128cb5a06c98cbc1422dfa14b0717a87abb1ea414435"
FINAL_MD = Path("docs/stage12-n1-2-final-r03.md")
FINAL_HTML = Path("review/PC-N1-2-FINAL-FULL-REREVIEW-20260807-R04.html")

SOURCES = [
    (
        "Definitions and counting convention",
        Path("docs/stage12-n1-3d-definition-sheet.md"),
        "b44f76a890363708d6274d14b7f7154894debc7b",
    ),
    (
        "Constant sheet",
        Path("docs/stage12-n1-3d-constant-sheet.md"),
        "3428f220c35c3625589dc44abf55819b48109631",
    ),
    (
        "Selberg--Delange reference lock",
        Path("docs/stage12-n1-3d-selberg-delange-reference-lock.md"),
        "23f887107b0babaadfcf6d6dc2e4255921c3651d",
    ),
    (
        "Integrated repaired proof R02",
        Path("docs/stage12-n1-2-final-r02.md"),
        "e343182e82d9ecacf844fa7e508662749d43b55b",
    ),
    (
        "Stage12-N1-3e local-gap closure",
        Path("docs/stage12-n1-3e-local-gap-closure.md"),
        "a61ba1fe84f49c92e4ccbcd5755ea1e3e0bf5ae5",
    ),
]


def git_blob_sha(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], text=True).strip()


def read_verified_sources() -> list[tuple[str, Path, str, str]]:
    verified: list[tuple[str, Path, str, str]] = []
    ledger_lines: list[str] = []
    for label, path, expected_blob in SOURCES:
        if not path.is_file():
            raise SystemExit(f"missing source: {path}")
        actual_blob = git_blob_sha(path)
        if actual_blob != expected_blob:
            raise SystemExit(
                f"source blob mismatch for {path}: expected {expected_blob}, got {actual_blob}"
            )
        text = path.read_text(encoding="utf-8")
        verified.append((label, path, actual_blob, text))
        ledger_lines.append(f"{path.as_posix()}|{actual_blob}")

    ledger_hash = hashlib.sha256("\n".join(ledger_lines).encode("utf-8")).hexdigest()
    if ledger_hash != SOURCE_LEDGER_SHA256:
        raise SystemExit(
            f"source ledger mismatch: expected {SOURCE_LEDGER_SHA256}, got {ledger_hash}"
        )
    return verified


def build_markdown(sources: list[tuple[str, Path, str, str]]) -> str:
    preamble = f"""# Stage12-N1-2 Final R03 — primitive oriented count, fully consolidated

> **BUNDLE_ID:** `{BUNDLE_ID}`
>
> **COMPLETED_THROUGH:** `{COMPLETED_THROUGH}`
>
> **SOURCE_SNAPSHOT_COMMIT:** `{SOURCE_SNAPSHOT_COMMIT}`
>
> **SOURCE_LEDGER_SHA256:** `{SOURCE_LEDGER_SHA256}`
>
> **DOCUMENT_STATUS:** `FULL_ZERO_BASE_REREVIEW_CANDIDATE`
>
> **COUNTING_TARGET:** `C_prim(B)` as defined in the embedded definition sheet

## Purpose and status

This is the single consolidated current proof source for a final zero-base re-review of

\\[
C_{{\\rm prim}}(B)
\\sim
\\frac{{\\kappa}}{{12\\pi}}B(\\log B)^3
=
\\frac{{\\eta}}{{12\\pi^2}}B(\\log B)^3.
\\]

It embeds, without silently rewriting their mathematical content, the definition sheet, constant sheet, reference lock, integrated repaired proof R02, and the Stage12-N1-3e supplement that closes the two local gaps identified by the limited R02 review.

Historical status labels inside embedded source documents describe the stage at which those documents were written. They do not replace the status of this consolidated file. The reviewer must audit the complete chain from zero and must not treat earlier `CLOSED` decisions as binding.

The theorem concerns the primitive **oriented** count defined below. It does not assert existence of a perfect cuboid, a canonical-count asymptotic, or an exact-one-face asymptotic.

## Immutable source ledger

| source | path | Git blob SHA |
|---|---|---|
"""
    ledger_rows = "\n".join(
        f"| {label} | `{path.as_posix()}` | `{blob}` |"
        for label, path, blob, _ in sources
    )

    sections: list[str] = []
    for index, (label, path, blob, text) in enumerate(sources, start=1):
        sections.append(
            f"""

---

# EMBEDDED SOURCE {index}/{len(sources)} — {label}

> **PATH:** `{path.as_posix()}`  
> **GIT_BLOB_SHA:** `{blob}`

{text.rstrip()}
"""
        )

    end = f"""

---

# Consolidated end marker

```text
CHECKPOINT=END_OF_MAIN
END_OF_BUNDLE={BUNDLE_ID}
```
"""
    return preamble + ledger_rows + "\n" + "".join(sections) + end


def build_html(markdown_text: str, content_sha256: str) -> str:
    return f"""<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{BUNDLE_ID}</title>
<style>
:root {{ color-scheme: light dark; }}
body {{ max-width: 1180px; margin: 0 auto; padding: 24px 18px 80px; font-family: system-ui, -apple-system, sans-serif; line-height: 1.55; }}
h1 {{ line-height: 1.25; }}
.meta {{ border: 2px solid currentColor; border-radius: 10px; padding: 16px; margin: 18px 0 28px; }}
pre {{ white-space: pre-wrap; overflow-wrap: anywhere; border: 1px solid #8888; border-radius: 8px; padding: 18px; background: #8881; }}
code {{ overflow-wrap: anywhere; }}
</style>
</head>
<body>
<main id="review-bundle-main">
<div class="meta"><pre>BUNDLE_ID={BUNDLE_ID}
COMPLETED_THROUGH={COMPLETED_THROUGH}
SOURCE_SNAPSHOT_COMMIT={SOURCE_SNAPSHOT_COMMIT}
SOURCE_LEDGER_SHA256={SOURCE_LEDGER_SHA256}
CONTENT_SHA256={content_sha256}
DOCUMENT_STATUS=FULL_ZERO_BASE_REREVIEW_CANDIDATE
CHECKPOINT=START_OF_MAIN</pre></div>
<h1>Stage12-N1-2 Final R03 — full zero-base re-review page</h1>
<p>This physical page contains the complete consolidated Markdown source. Review the entire page through the end marker.</p>
<pre>{html.escape(markdown_text)}</pre>
<div class="meta"><pre>CHECKPOINT=END_OF_MAIN
CONTENT_SHA256={content_sha256}
END_OF_BUNDLE={BUNDLE_ID}</pre></div>
</main>
</body>
</html>
"""


def main() -> None:
    sources = read_verified_sources()
    markdown_text = build_markdown(sources)
    content_sha256 = hashlib.sha256(markdown_text.encode("utf-8")).hexdigest()
    html_text = build_html(markdown_text, content_sha256)

    FINAL_MD.parent.mkdir(parents=True, exist_ok=True)
    FINAL_HTML.parent.mkdir(parents=True, exist_ok=True)
    FINAL_MD.write_text(markdown_text, encoding="utf-8")
    FINAL_HTML.write_text(html_text, encoding="utf-8")

    print(f"wrote {FINAL_MD} ({len(markdown_text.encode('utf-8'))} bytes)")
    print(f"wrote {FINAL_HTML} ({len(html_text.encode('utf-8'))} bytes)")
    print(f"CONTENT_SHA256={content_sha256}")


if __name__ == "__main__":
    main()
