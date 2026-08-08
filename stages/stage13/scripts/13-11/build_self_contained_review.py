#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import html
import json
import subprocess
from pathlib import Path

BUNDLE_ID = "STAGE13-FINAL-SELF-CONTAINED-20260808-R01"
COMPLETED_THROUGH = "Stage13-11"
DOCUMENT_STATUS = "SELF_CONTAINED_STAGE13_ONLY_WITH_DECLARED_STAGE12_R09_INPUT"
OUTPUT_HTML = Path("review/STAGE13-FINAL-SELF-CONTAINED-20260808-R01.html")
OUTPUT_MANIFEST = Path("stages/stage13/data/13-11/review_bundle_manifest.json")
GENERATED_PATHS = {OUTPUT_HTML.as_posix(), OUTPUT_MANIFEST.as_posix()}

STATIC_SOURCES = [
    Path("stages/stage13/README.md"),
    Path("stages/stage13/roadmap.md"),
    Path("stages/stage13/policy.md"),
    Path("stages/stage13/main.md"),
    Path("stages/stage13/13-11-review-bundle.md"),
]


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True).strip()


def git_blob_sha(path: Path) -> str:
    return git("hash-object", str(path))


def changed_paths(commit: str) -> set[str]:
    output = git("show", "--pretty=format:", "--name-only", commit)
    return {line.strip() for line in output.splitlines() if line.strip()}


def source_snapshot_commit() -> str:
    commit = git("rev-parse", "HEAD")
    while True:
        paths = changed_paths(commit)
        if paths and paths.issubset(GENERATED_PATHS):
            commit = git("rev-parse", f"{commit}^")
            continue
        return commit


def source_paths() -> list[Path]:
    paths = list(STATIC_SOURCES)
    paths.extend(sorted(Path("stages/stage13/initial").glob("*.md")))

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

    # The packaging code is itself reviewable, but generated 13-11 outputs are
    # excluded to avoid recursive self-embedding.
    paths.append(Path(__file__).resolve().relative_to(Path.cwd().resolve()))

    unique = {path.as_posix(): path for path in paths}
    return [unique[key] for key in sorted(unique)]


def read_sources(paths: list[Path]) -> tuple[list[dict], str]:
    rows: list[dict] = []
    ledger_lines: list[str] = []
    for path in paths:
        if not path.is_file():
            raise SystemExit(f"missing source: {path}")
        blob = git_blob_sha(path)
        text = path.read_text(encoding="utf-8")
        rows.append({
            "path": path.as_posix(),
            "blob_sha": blob,
            "bytes": len(text.encode("utf-8")),
            "text": text,
        })
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

This is the single-file review target for **Stage13 only**. It physically embeds
the canonical Stage13 mathematical source, Stage13 policy/status/initial sources,
and every active Stage13 audit script and report predating 13-11.

Stage12 source text, manifests, archive material, scripts and reports are not
embedded and are not part of this review. Stage13 may cite the already-frozen
Stage12 R09 theorem as a declared prior input. The reviewer should audit whether
Stage13 uses that stated input correctly, but should not re-audit Stage12 itself.

## Declared prior input boundary

The only prior-stage theorem-level input relevant here is the frozen Stage12 R09
primitive oriented asymptotic, as stated inside the Stage13 sources. Its proof is
outside this bundle. No Stage12 file is embedded.

STAGE12_SOURCE_EMBEDDED=false
STAGE12_REVIEW_IN_SCOPE=false
STAGE12_R09_DECLARED_PRIOR_INPUT=true

## Required review questions

1. Are the Stage13 primitive canonical definitions and exactly-one inclusion-exclusion correct?
2. Is the canonical chamber / Gelfand--Leray directional factor derived correctly?
3. Are the arithmetic factors direction-neutral where Stage13 claims they are?
4. Given the declared Stage12 R09 input, is the Stage12-to-Stage13 projection/bridge used correctly, including the factor 1/2?
5. Are pair and triple overlaps genuinely lower order at the claimed scale?
6. Does the Stage13 main theorem
   N_q(B) ~ [kappa I_q/(3 pi^3)] B(log B)^3
   follow from the embedded Stage13 chain plus the declared prior input?
7. Does the normalized limit equal
   2.431684750178191 : 1.115756428951881 : 1,
   and is the finite near-2:1:1 regime correctly described as pre-asymptotic?
8. Are all non-claims respected: no perfect-cuboid existence result, no explicit
   convergence rate, no effective threshold, and no monotonicity theorem?

## Verdict protocol

Return exactly one top-level classification:

CLOSED
  No fatal or major Stage13 mathematical gap is found at the declared input boundary.

REPAIRABLE
  The central Stage13 route appears viable, but one or more local major gaps require repair.

OPEN
  A fatal Stage13 gap, invalid central implication, or unsupported theorem-level step is found.

UNREADABLE_SOURCE
  The complete physical Stage13 bundle cannot be read or its checkpoints cannot be verified.

For REPAIRABLE or OPEN, enumerate findings as FATAL / MAJOR / MINOR and cite the
embedded Stage13 source path and nearest section/function. Do not mark a stylistic
issue or the deliberate exclusion of Stage12 proof text as a Stage13 mathematical failure.

## Scope locks

REVIEW_SCOPE=STAGE13_ONLY
STAGE12_SOURCE_EMBEDDED=false
STAGE12_REVIEW_IN_SCOPE=false
STAGE12_R09_DECLARED_PRIOR_INPUT=true
STAGE13_CANONICAL_WORKING_FILE=stages/stage13/main.md
PERFECT_CUBOID_EXISTENCE_CLAIM=false
EXPLICIT_CONVERGENCE_RATE_CLAIM=false
MONOTONICITY_CLAIM=false
INDEPENDENT_PUBLICATION_REVIEW_COMPLETED=false

CHECKPOINT=BEFORE_EMBEDDED_SOURCES

## Immutable Stage13 source ledger

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
            f"\n\n---\n\n# EMBEDDED SOURCE {i}/{len(rows)}\n\n"
            f"PATH={row['path']}\nGIT_BLOB_SHA={row['blob_sha']}\n\n"
            f"{row['text'].rstrip()}\n"
        )

    end = f"""\n\n---\n\nCHECKPOINT=AFTER_EMBEDDED_SOURCES\n
## Final bundle state

STAGE13_11=SELF_CONTAINED_STAGE13_ONLY_REVIEW_BUNDLE
STAGE13_MATHEMATICS_CHANGED_BY_13_11=false
STAGE13_COMPLETE=true
REVIEW_SCOPE=STAGE13_ONLY_WITH_DECLARED_STAGE12_R09_INPUT
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
REVIEW_SCOPE=STAGE13_ONLY
CHECKPOINT=START_OF_MAIN</pre></div>
<h1>Stage13 final self-contained review bundle R01</h1>
<p>Only Stage13 review material is physically embedded below. No Stage12 source file is embedded.</p>
<pre>{escaped}</pre>
<div class="meta"><pre>CHECKPOINT=END_OF_MAIN
CONTENT_SHA256={content_sha}
END_OF_BUNDLE={BUNDLE_ID}</pre></div>
</main>
</body>
</html>
"""


def main() -> None:
    snapshot = source_snapshot_commit()
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
        "sources": [{k: row[k] for k in ("path", "blob_sha", "bytes")} for row in rows],
        "review_protocol": {
            "allowed_verdicts": ["CLOSED", "REPAIRABLE", "OPEN", "UNREADABLE_SOURCE"],
            "review_scope": "stage13_only",
            "stage12_source_embedded": False,
            "stage12_review_in_scope": False,
            "stage12_r09_declared_prior_input": True,
            "perfect_cuboid_existence_claim": False,
            "explicit_convergence_rate_claim": False,
            "monotonicity_claim": False,
        },
        "status": {
            "STAGE13_11_complete": True,
            "mathematics_changed": False,
            "physical_single_html": True,
            "external_runtime_dependencies": False,
            "stage13_only_bundle": True,
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
