#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import html
import subprocess
from dataclasses import dataclass
from pathlib import Path

BUNDLE_ID = "PC-N1-2-FINAL-SELF-CONTAINED-20260807-R08"
COMPLETED_THROUGH = "Stage12-N1-3i"
SOURCE_SNAPSHOT_COMMIT = "27129350052dd7110e2a01386793cdb416bca639"
SOURCE_LEDGER_SHA256 = "239cc5c81d5cb6aa4881e745d52f56f4337cabc972cd839dd803c24bc59ae076"
HISTORICAL_PROVENANCE_COMMIT = "8d6910e8e68145e474f92716460a1cc6f384ecf1"
FINAL_MD = Path("docs/stage12-n1-2-final-r07-self-contained.md")
FINAL_HTML = Path("review/PC-N1-2-FINAL-SELF-CONTAINED-20260807-R08.html")


@dataclass(frozen=True)
class Source:
    label: str
    path: str
    expected_blob: str
    ref: str | None = None

    @property
    def locator(self) -> str:
        return self.ref if self.ref is not None else "WORKTREE"


SOURCES = [
    Source(
        "Active consolidated proof through Stage12-N1-3g",
        "docs/stage12-n1-2-final-r05.md",
        "ccdf97313c361862535f3aab59ed207caae38e08",
    ),
    Source(
        "Active rectangle-error derivation",
        "docs/stage12-n1-3a-rectangular-error-repair.md",
        "fb4a7a52fcb2cf55005c155b0534abf3a986fe42",
    ),
    Source(
        "Historical origin of the parameter sum and multiplicity G",
        "docs/stage12-n1-2b-average.md",
        "0430d010472314f0c88e78189493f652c261b3ef",
        HISTORICAL_PROVENANCE_COMMIT,
    ),
    Source(
        "Historical exact divisor expansion of G",
        "docs/stage12-n1-2e-divisor-dyadic.md",
        "e8783ee5577419b9f8aeff1e93a3c4aaf44a7feb",
        HISTORICAL_PROVENANCE_COMMIT,
    ),
    Source(
        "Historical derivation of kappa and the three-variable local factors",
        "docs/stage12-n1-2f-main-term.md",
        "5ba2f0844446a57dd524034fd9cd186f7a00fcb1",
        HISTORICAL_PROVENANCE_COMMIT,
    ),
    Source(
        "Historical primitive-first derivation of A_rs, beta and gamma",
        "docs/stage12-n1-2j-boundary-layers.md",
        "111107ce0346606cb8a73b4c50e1841386f4cf23",
        HISTORICAL_PROVENANCE_COMMIT,
    ),
    Source(
        "Historical derivation of eta and its comparison with kappa",
        "docs/stage12-n1-2k-final-remainder.md",
        "48b28e84034c17e242998ab313775b0894908515",
        HISTORICAL_PROVENANCE_COMMIT,
    ),
    Source(
        "Active zero-base provenance, vertical-growth and radial-boundary closure",
        "docs/stage12-n1-3h-zero-base-provenance-closure.md",
        "7683303f47ef8d6d4d10f1bb1501657020956cfd",
    ),
    Source(
        "Active final reference closure: beta bound, cross norm, Selberg--Delange map",
        "docs/stage12-n1-3i-final-reference-closure.md",
        "20641b2f3101e7bc18cf9e425c1b7b020b439cf7",
    ),
]


def run_text(*args: str) -> str:
    return subprocess.check_output(list(args), text=True).strip()


def read_source(source: Source) -> tuple[str, str]:
    if source.ref is None:
        path = Path(source.path)
        if not path.is_file():
            raise SystemExit(f"missing worktree source: {source.path}")
        actual_blob = run_text("git", "hash-object", source.path)
        text = path.read_text(encoding="utf-8")
    else:
        object_name = f"{source.ref}:{source.path}"
        actual_blob = run_text("git", "rev-parse", object_name)
        text = subprocess.check_output(
            ["git", "show", object_name], text=True, encoding="utf-8"
        )
    if actual_blob != source.expected_blob:
        raise SystemExit(
            f"source blob mismatch for {source.locator}:{source.path}: "
            f"expected {source.expected_blob}, got {actual_blob}"
        )
    return actual_blob, text


def read_verified_sources() -> list[tuple[Source, str, str]]:
    verified: list[tuple[Source, str, str]] = []
    ledger_lines: list[str] = []
    for source in SOURCES:
        blob, text = read_source(source)
        verified.append((source, blob, text))
        ledger_lines.append(f"{source.locator}|{source.path}|{blob}")
    ledger_payload = "\n".join(ledger_lines)
    ledger_hash = hashlib.sha256(ledger_payload.encode("utf-8")).hexdigest()
    if ledger_hash != SOURCE_LEDGER_SHA256:
        raise SystemExit(
            f"source ledger mismatch: expected {SOURCE_LEDGER_SHA256}, got {ledger_hash}"
        )
    return verified


def build_markdown(sources: list[tuple[Source, str, str]]) -> str:
    preamble = f"""# Stage12-N1-2 Final R07 — self-contained proof bundle

> **BUNDLE_ID:** `{BUNDLE_ID}`
>
> **COMPLETED_THROUGH:** `{COMPLETED_THROUGH}`
>
> **SOURCE_SNAPSHOT_COMMIT:** `{SOURCE_SNAPSHOT_COMMIT}`
>
> **SOURCE_LEDGER_SHA256:** `{SOURCE_LEDGER_SHA256}`
>
> **HISTORICAL_PROVENANCE_COMMIT:** `{HISTORICAL_PROVENANCE_COMMIT}`
>
> **DOCUMENT_STATUS:** `SELF_CONTAINED_AT_STATED_EXTERNAL_THEOREM_LEVEL`
>
> **COUNTING_TARGET:** primitive oriented count `C_prim(B)` only

## Purpose

This is the final single-document self-contained source for the Stage12-N1-2 primitive oriented asymptotic

\\[
C_{{\\rm prim}}(B)
\\sim
\\frac{{\\kappa}}{{12\\pi}}B(\\log B)^3
=
\\frac{{\\eta}}{{12\\pi^2}}B(\\log B)^3.
\\]

The bundle physically includes the active proof, the derivation of the corrected rectangle exponent, the historical definitions needed to reconstruct `G`, `beta`, `gamma`, `kappa` and `eta`, the explicit radial lower-limit and vertical-growth closure, and the final direct proofs of `B_beta(X)<<X` and the coprime cross-correction weighted norm.

Selberg--Delange itself remains an external published theorem; its exact working form and the mapping of every hypothesis used here are stated in Stage12-N1-3i. No unpublished or superseded Stage12-N1-2p step is required by the active proof.

## Precedence and supersession

```text
ACTIVE_CURRENT_PROOF=docs/stage12-n1-2-final-r05.md
ACTIVE_RECTANGLE_DERIVATION=Stage12-N1-3a Lemma 3a.1
ACTIVE_VERTICAL_AND_RADIAL_BOUNDARY=Stage12-N1-3h
ACTIVE_FINAL_REFERENCE_CLOSURE=Stage12-N1-3i
3A_REFERENCES_TO_OLD_2P_INPUTS=SUPERSEDED_BY_3I
2F_FORMAL_RAW_ASYMPTOTIC=PROVENANCE_ONLY
2K_OLD_FIXED_CIRCLE_REMAINDER=SUPERSEDED_BY_3B_AND_3E
2K_OLD_SHALLOW_BOUND=SUPERSEDED_BY_3G
3A_OLD_RETAINED_MIN_RS_APPLICATION=SUPERSEDED_BY_3F
OLD_2P_ACTIVE_DEPENDENCY=NONE
SUPERSEDED_FIXED_BC_KERNEL=NOT_USED
SPECIFIC_3_5_ZERO_FREE_REMAINDER=NOT_USED
```

## Immutable source ledger

| role | locator | path | Git blob SHA |
|---|---|---|---|
"""
    rows = "\n".join(
        f"| {source.label} | `{source.locator}` | `{source.path}` | `{blob}` |"
        for source, blob, _ in sources
    )
    sections: list[str] = []
    total = len(sources)
    for index, (source, blob, text) in enumerate(sources, start=1):
        sections.append(
            f"""

---

# EMBEDDED SOURCE {index}/{total} — {source.label}

> **LOCATOR:** `{source.locator}`  
> **PATH:** `{source.path}`  
> **GIT_BLOB_SHA:** `{blob}`

{text.rstrip()}
"""
        )
    end = f"""

---

# Final closure marker

```text
CHECKPOINT=END_OF_MAIN
SELF_CONTAINMENT=COMPLETE_AT_STATED_EXTERNAL_THEOREM_LEVEL
OLD_2P_ACTIVE_DEPENDENCY=NONE
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
HISTORICAL_PROVENANCE_COMMIT={HISTORICAL_PROVENANCE_COMMIT}
CONTENT_SHA256={content_sha256}
DOCUMENT_STATUS=SELF_CONTAINED_AT_STATED_EXTERNAL_THEOREM_LEVEL
CHECKPOINT=START_OF_MAIN</pre></div>
<h1>Stage12-N1-2 Final R07 — self-contained bundle R08</h1>
<p>This page contains the complete consolidated Markdown and all active closure material. Selberg--Delange is the only external theorem-level input; its working statement and application checklist are embedded in Stage12-N1-3i.</p>
<pre>{html.escape(markdown_text)}</pre>
<div class="meta"><pre>CHECKPOINT=END_OF_MAIN
CONTENT_SHA256={content_sha256}
SELF_CONTAINMENT=COMPLETE_AT_STATED_EXTERNAL_THEOREM_LEVEL
OLD_2P_ACTIVE_DEPENDENCY=NONE
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
