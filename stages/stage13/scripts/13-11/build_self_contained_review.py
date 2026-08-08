#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import html
import json
import subprocess
from pathlib import Path

BUNDLE_ID = "STAGE13-FINAL-SELF-CONTAINED-20260808-R01"
COMPLETED_THROUGH = "Stage13-11"
DOCUMENT_STATUS = "SELF_CONTAINED_AT_FROZEN_STAGE12_INPUT_BOUNDARY"
OUTPUT_HTML = Path("review/STAGE13-FINAL-SELF-CONTAINED-20260808-R01.html")
OUTPUT_MANIFEST = Path("stages/stage13/data/13-11/review_bundle_manifest.json")

STATIC_SOURCES = [
    Path("stages/stage12/final.md"),
    Path("stages/stage12/manifest-r09.md"),
    Path("stages/stage13/README.md"),
    Path("stages/stage13/roadmap.md"),
    Path("stages/stage13/policy.md"),
    Path("stages/stage13/main.md"),
]


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True).strip()


def git_blob_sha(path: Path) -> str:
    return git("hash-object", str(path))


def source_paths() -> list[Path]:
    paths = list(STATIC_SOURCES)
    paths.extend(sorted(Path("stages/stage13/initial").glob("*.md")))

    # Include every active Stage13 audit/reproducibility asset that predates
    # Stage13-11. 13-11 output is intentionally excluded to avoid recursion.
    for root in (Path("stages/stage13/scripts"), Path("stages/stage13/data")):
        for path in sorted(root.rglob("*")):
            if not path.is_file():
                continue
            rel = path.relative_to(root)
            if rel.parts and rel.parts[0] == "13-11":
                continue
            if path.suffix not in {".py", ".json", ".md", ".txt"}:
                continue
            paths.append(path)

    # Embed the builder itself so an external reviewer can inspect how the
    # physical page was assembled.
    paths.append(Path(__file__).resolve().relative_to(Path.cwd().resolve()))

    unique: dict[str, Path] = {}
    for path in paths:
        unique[path.as_posix()] = path
    return [unique[key] for key in sorted(unique)]


def read_sources(paths: list[Path]) -> tuple[list[dict], str]:
    rows: list[dict] = []
    ledger_lines: list[str] = []
    for path in paths:
        if not path.is_file():
            raise SystemExit(f"missing source: {path}")
        blob = git_blob_sha(path)
        text = path.read_text(encoding="utf-8")
        rows.append(
            {
                "path": path.as_posix(),
                "blob_sha": blob,
                "bytes": len(text.encode("utf-8")),
                "text": text,
            }
        )
        ledger_lines.append(f"{path.as_posix()}|{blob}")
    ledger = "\n".join(ledger_lines)
    return rows, hashlib.sha256(ledger.encode("utf-8")).hexdigest()


def build_payload(rows: list[dict], snapshot: str, ledger_sha: str) -> str:
    preamble = f"""# Stage13 final self-contained review bundle R01

BUNDLE_ID={BUNDLE_ID}
COMPLETED_THROUGH={COMPLETED_THROUGH}
SOURCE_SNAPSHOT_COMMIT={snapshot}
SOURCE_LEDGER_SHA256={ledger_sha}
DOCUMENT_STATUS={DOCUMENT_STATUS}
CHECKPOINT=START_OF_MAIN

## Review purpose

This is the single-file Stage13 review target. It physically embeds the canonical
Stage13 mathematical source, Stage13 policy/status documents, every active
Stage13 audit script and JSON report, and the frozen Stage12 final theorem plus
its R09 manifest as the explicit prior-stage input boundary.

The reviewer should audit Stage13 from zero **at that stated Stage12 input
boundary**. Re-proving all of Stage12 is outside this bundle's scope; checking
that Stage13 correctly states and uses the frozen Stage12 theorem is in scope.

## Required review questions

1. Are the primitive canonical definitions and exact-one inclusion-exclusion correct?
2. Is the canonical chamber / Gelfand--Leray directional factor derived correctly?
3. Are the arithmetic factors used as direction-neutral where claimed?
4. Is the Stage12 oriented-count to Stage13 canonical-count bridge valid, including the factor 1/2?
5. Are pair and triple overlaps genuinely lower order at the claimed scale?
6. Does the main theorem
   N_q(B) ~ [kappa I_q/(3 pi^3)] B(log B)^3
   follow from the embedded chain?
7. Does the normalized limit equal
   2.431684750178191 : 1.115756428951881 : 1,
   and is the finite near-2:1:1 regime correctly described as pre-asymptotic?
8. Are all non-claims respected: no perfect-cuboid existence result, no explicit
   convergence rate, no effective threshold, and no monotonicity theorem?

## Verdict protocol

Return exactly one top-level classification:

CLOSED
  No fatal or major mathematical gap is found at the stated input boundary.

REPAIRABLE
  The central route appears viable, but one or more local major gaps require repair.

OPEN
  A fatal gap, invalid central implication, or unsupported theorem-level step is found.

UNREADABLE_SOURCE
  The complete physical bundle cannot be read or its checkpoints cannot be verified.

For REPAIRABLE or OPEN, enumerate findings as FATAL / MAJOR / MINOR and cite the
embedded source path and nearest section/function. Do not mark a stylistic issue
as mathematical failure.

## Scope locks

STAGE12_REPROOF_REQUIRED=false
STAGE12_FROZEN_THEOREM_IS_PRIOR_INPUT=true
STAGE13_CANONICAL_WORKING_FILE=stages/stage13/main.md
PERFECT_CUBOID_EXISTENCE_CLAIM=false
EXPLICIT_CONVERGENCE_RATE_CLAIM=false
MONOTONICITY_CLAIM=false
INDEPENDENT_PUBLICATION_REVIEW_COMPLETED=false

CHECKPOINT=BEFORE_EMBEDDED_SOURCES

## Immutable source ledger

| # | path | Git blob SHA | bytes |
|---:|---|---|---:|
"""
    table = "\n".join(
        f"| {i} | `{row['path']}` | `{row['blob_sha']}` | {row['bytes']} |"
        for i, row in enumerate(rows, start=1)
    )

    sections: list[str] = []
    for i, row in enumerate(rows, start=1):
        sections.append(
            f"""\n\n---\n\n# EMBEDDED SOURCE {i}/{len(rows)}\n\nPATH={row['path']}\nGIT_BLOB_SHA={row['blob_sha']}\n\n{row['text'].rstrip()}\n"""
        )

    end = f"""\n\n---\n\nCHECKPOINT=AFTER_EMBEDDED_SOURCES\n
## Final bundle state

STAGE13_11=SELF_CONTAINED_REVIEW_BUNDLE
STAGE13_MATHEMATICS_CHANGED_BY_13_11=false
STAGE13_COMPLETE=true
REVIEW_SCOPE=ZERO_BASE_AT_FROZEN_STAGE12_INPUT_BOUNDARY
CHECKPOINT=END_OF_MAIN
END_OF_BUNDLE={BUNDLE_ID}
"""
    return preamble + table + "".join(sections) + end


def build_html(payload: str, snapshot: str, ledger_sha: str, content_sha: str) -> str:
    escaped = html.escape(payload)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{BUNDLE_ID}</title>
<style>
:root {{ color-scheme: light dark; }}
body {{ max-width: 1240px; margin: 0 auto; padding: 24px 18px 80px; font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; line-height: 1.5; }}
h1 {{ line-height: 1.2; }}
.meta {{ border: 2px solid currentColor; border-radius: 10px; padding: 14px; margin: 18px 0 24px; }}
pre {{ white-space: pre-wrap; overflow-wrap: anywhere; border: 1px solid #8888; border-radius: 8px; padding: 16px; background: #8881; }}
</style>
</head>
<body>
<main id="review-bundle-main">
<div class="meta"><pre>BUNDLE_ID={BUNDLE_ID}
COMPLETED_THROUGH={COMPLETED_THROUGH}
SOURCE_SNAPSHOT_COMMIT={snapshot}
SOURCE_LEDGER_SHA256={ledger_sha}
CONTENT_SHA256={content_sha}
DOCUMENT_STATUS={DOCUMENT_STATUS}
CHECKPOINT=START_OF_MAIN</pre></div>
<h1>Stage13 final self-contained review bundle R01</h1>
<p>All review material is physically embedded below. No JavaScript, external stylesheet, iframe, or runtime repository fetch is required.</p>
<pre>{escaped}</pre>
<div class="meta"><pre>CHECKPOINT=END_OF_MAIN
CONTENT_SHA256={content_sha}
END_OF_BUNDLE={BUNDLE_ID}</pre></div>
</main>
</body>
</html>
"""


def main() -> None:
    snapshot = git("rev-parse", "HEAD")
    rows, ledger_sha = read_sources(source_paths())
    payload = build_payload(rows, snapshot, ledger_sha)
    content_sha = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    page = build_html(payload, snapshot, ledger_sha, content_sha)

    OUTPUT_HTML.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_HTML.write_text(page, encoding="utf-8")

    manifest = {
        "bundle_id": BUNDLE_ID,
        "completed_through": COMPLETED_THROUGH,
        "document_status": DOCUMENT_STATUS,
        "source_snapshot_commit": snapshot,
        "source_ledger_sha256": ledger_sha,
        "content_sha256": content_sha,
        "html_path": OUTPUT_HTML.as_posix(),
        "html_bytes": len(page.encode("utf-8")),
        "source_count": len(rows),
        "sources": [
            {k: row[k] for k in ("path", "blob_sha", "bytes")}
            for row in rows
        ],
        "review_protocol": {
            "allowed_verdicts": ["CLOSED", "REPAIRABLE", "OPEN", "UNREADABLE_SOURCE"],
            "stage12_reproof_required": False,
            "stage12_frozen_theorem_is_prior_input": True,
            "perfect_cuboid_existence_claim": False,
            "explicit_convergence_rate_claim": False,
            "monotonicity_claim": False,
        },
        "status": {
            "STAGE13_11_complete": True,
            "mathematics_changed": False,
            "physical_single_html": True,
            "external_runtime_dependencies": False,
        },
    }
    OUTPUT_MANIFEST.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(f"BUNDLE_ID={BUNDLE_ID}")
    print(f"SOURCE_SNAPSHOT_COMMIT={snapshot}")
    print(f"SOURCE_LEDGER_SHA256={ledger_sha}")
    print(f"CONTENT_SHA256={content_sha}")
    print(f"SOURCE_COUNT={len(rows)}")
    print(f"HTML_BYTES={len(page.encode('utf-8'))}")
    print(f"WROTE={OUTPUT_HTML}")
    print(f"WROTE={OUTPUT_MANIFEST}")


if __name__ == "__main__":
    main()
