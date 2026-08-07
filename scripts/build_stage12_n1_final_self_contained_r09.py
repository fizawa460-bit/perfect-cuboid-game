#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import html
import subprocess
from pathlib import Path

BUNDLE_ID = "PC-N1-2-FINAL-SELF-CONTAINED-20260807-R09"
COMPLETED_THROUGH = "Stage12-N1-3j"
SOURCE_SNAPSHOT_COMMIT = "d69a6e2ee352700660776f55a749eebb432552f9"
SOURCE_LEDGER_SHA256 = "800a664bf940e751cb1fafc7758a2692c6950eecb6ef94784738d276a4a0debe"
FINAL_MD = Path("docs/stage12-n1-2-final-r08-self-contained.md")
FINAL_HTML = Path("review/PC-N1-2-FINAL-SELF-CONTAINED-20260807-R09.html")

SOURCES = [
    (
        "Full self-contained proof bundle through Stage12-N1-3i",
        Path("docs/stage12-n1-2-final-r07-self-contained.md"),
        "22b437fc82e3e27fe68b6fd7caaa405850ee9637",
    ),
    (
        "Final weighted-l1 Euler-product and vertical-growth closure",
        Path("docs/stage12-n1-3j-weighted-l1-and-vertical-closure.md"),
        "a933a56da1f3f363048396dfa6fa7e16b582645d",
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
        ledger_lines.append(f"WORKTREE|{path.as_posix()}|{actual_blob}")

    ledger_hash = hashlib.sha256("\n".join(ledger_lines).encode("utf-8")).hexdigest()
    if ledger_hash != SOURCE_LEDGER_SHA256:
        raise SystemExit(
            f"source ledger mismatch: expected {SOURCE_LEDGER_SHA256}, got {ledger_hash}"
        )
    return verified


def build_markdown(sources: list[tuple[str, Path, str, str]]) -> str:
    preamble = f"""# Stage12-N1-2 Final R08 — self-contained proof text through 3j

> **BUNDLE_ID:** `{BUNDLE_ID}`
>
> **COMPLETED_THROUGH:** `{COMPLETED_THROUGH}`
>
> **SOURCE_SNAPSHOT_COMMIT:** `{SOURCE_SNAPSHOT_COMMIT}`
>
> **SOURCE_LEDGER_SHA256:** `{SOURCE_LEDGER_SHA256}`
>
> **DOCUMENT_STATUS:** `SELF_CONTAINED_AT_STATED_EXTERNAL_THEOREM_LEVEL_FINAL_TEXT`
>
> **COUNTING_TARGET:** primitive oriented count `C_prim(B)` only

## Purpose

This is the final self-contained Stage12-N1-2 proof text at the stated external-theorem boundary. It contains the complete R08 self-contained proof and the final Stage12-N1-3j detail closure.

The only theorem-level external input intentionally retained is the published finite-order Selberg--Delange theorem. Its working form and application checklist are already embedded in the parent proof. Stage12-N1-3j adds no new external theorem: it proves the weighted two-variable `l1` product step directly and separates the vertical-growth roles of `J_beta` and `L(s,chi_4)`.

The theorem asserted here remains

\\[
C_{{\\rm prim}}(B)
\\sim
\\frac{{\\kappa}}{{12\\pi}}B(\\log B)^3
=
\\frac{{\\eta}}{{12\\pi^2}}B(\\log B)^3,
\\]

for the primitive oriented count only.

## Final precedence

```text
ACTIVE_PARENT_PROOF=docs/stage12-n1-2-final-r07-self-contained.md
ACTIVE_FINAL_DETAIL_CLOSURE=docs/stage12-n1-3j-weighted-l1-and-vertical-closure.md
3I_EULER_PRODUCT_TO_GLOBAL_L1_ONE_LINE=EXPANDED_BY_3J
J_BETA_FUNCTIONAL_EQUATION_ASSUMED=false
J_BETA_VERTICAL_BOUND=ABSOLUTE_CONVERGENCE_ONLY
L_CHI4_VERTICAL_BOUND=FUNCTIONAL_EQUATION_STIRLING_PL
OLD_2P_ACTIVE_DEPENDENCY=NONE
SELBERG_DELANGE_THEOREM=EXTERNAL_PUBLISHED_THEOREM_LEVEL_INPUT
SELF_CONTAINMENT=COMPLETE_AT_STATED_EXTERNAL_THEOREM_LEVEL
ADDITIONAL_EXTERNAL_REVIEW=NOT_REQUIRED_AS_PROJECT_GATE
```

## Immutable source ledger

| source | path | Git blob SHA |
|---|---|---|
"""
    rows = "\n".join(
        f"| {label} | `{path.as_posix()}` | `{blob}` |"
        for label, path, blob, _ in sources
    )

    sections: list[str] = []
    total = len(sources)
    for index, (label, path, blob, text) in enumerate(sources, start=1):
        sections.append(
            f"""

---

# EMBEDDED SOURCE {index}/{total} — {label}

> **PATH:** `{path.as_posix()}`  
> **GIT_BLOB_SHA:** `{blob}`

{text.rstrip()}
"""
        )

    end = f"""

---

# Final state

```text
WEIGHTED_L1_DIRICHLET_SUBMULTIPLICATIVITY=CLOSED
EULER_PRODUCT_TO_GLOBAL_WEIGHTED_L1=CLOSED
VERTICAL_GROWTH_ROLE_SEPARATION=CLOSED
J_BETA_FUNCTIONAL_EQUATION_ASSUMED=false
OLD_2P_ACTIVE_DEPENDENCY=NONE
NEW_CENTRAL_MATHEMATICAL_GAP=NONE_IDENTIFIED
SELF_CONTAINMENT=COMPLETE_AT_STATED_EXTERNAL_THEOREM_LEVEL
THEOREM_SCOPE=PRIMITIVE_ORIENTED_COUNT_ONLY
CHECKPOINT=END_OF_MAIN
END_OF_BUNDLE={BUNDLE_ID}
```
"""
    return preamble + rows + "\n" + "".join(sections) + end


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
DOCUMENT_STATUS=SELF_CONTAINED_AT_STATED_EXTERNAL_THEOREM_LEVEL_FINAL_TEXT
CHECKPOINT=START_OF_MAIN</pre></div>
<h1>Stage12-N1-2 Final R08 — self-contained bundle R09</h1>
<p>This page contains the complete R08 proof plus the final weighted-l1 and vertical-growth detail closure.</p>
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
