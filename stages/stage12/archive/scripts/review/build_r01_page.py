#!/usr/bin/env python3
"""Build a single, self-contained Stage12-N1-2 proof-review HTML page.

The generated page embeds the complete Stage12-N1-2 through 2k research notes,
their JSON audit reports, and the audit scripts.  It intentionally requires no
secondary link traversal, so an external reviewer can inspect one immutable URL.
"""
from __future__ import annotations

import argparse
import hashlib
import html
from pathlib import Path

BUNDLE_ID = "PC-N1-2-PROOF-REVIEW-20260806-1612-R01"
COMPLETED_THROUGH = "Stage12-N1-2k"
SOURCE_SNAPSHOT_COMMIT = "0e8bbc6e745ddf6d1f7c0ba3b21bb328a1fcc4d2"
LAST_SOURCE_DOCUMENT = "docs/stage12-n1-2k-final-remainder.md"
DEFAULT_OUTPUT = Path("review/PC-N1-2-PROOF-REVIEW-20260806-R01.html")

DOCUMENTS = [
    ("Stage12-N1-2", "docs/stage12-n1-2-hyperbola.md"),
    ("Stage12-N1-2b", "docs/stage12-n1-2b-average.md"),
    ("Stage12-N1-2c", "docs/stage12-n1-2c-gao-zhao.md"),
    ("Stage12-N1-2d", "docs/stage12-n1-2d-modular-hyperbola.md"),
    ("Stage12-N1-2e", "docs/stage12-n1-2e-divisor-dyadic.md"),
    ("Stage12-N1-2f", "docs/stage12-n1-2f-main-term.md"),
    ("Stage12-N1-2g", "docs/stage12-n1-2g-uniform-error.md"),
    ("Stage12-N1-2h", "docs/stage12-n1-2h-poisson-split.md"),
    ("Stage12-N1-2i", "docs/stage12-n1-2i-exponent-budget.md"),
    ("Stage12-N1-2j", "docs/stage12-n1-2j-boundary-layers.md"),
    ("Stage12-N1-2k", "docs/stage12-n1-2k-final-remainder.md"),
]

REPORTS = [
    ("Stage12-N1-2 report", "data/shared_p_hyperbola_stage12_n1_2_report.json"),
    ("Stage12-N1-2b report", "data/shared_p_average_stage12_n1_2b_report.json"),
    ("Stage12-N1-2c report", "data/gao_zhao_compatibility_stage12_n1_2c_report.json"),
    ("Stage12-N1-2d report", "data/modular_hyperbola_stage12_n1_2d_report.json"),
    ("Stage12-N1-2e report", "data/divisor_dyadic_stage12_n1_2e_report.json"),
    ("Stage12-N1-2f report", "data/main_term_stage12_n1_2f_report.json"),
    ("Stage12-N1-2g report", "data/uniform_error_stage12_n1_2g_report.json"),
    ("Stage12-N1-2h report", "data/poisson_split_stage12_n1_2h_report.json"),
    ("Stage12-N1-2i report", "data/exponent_budget_stage12_n1_2i_report.json"),
    ("Stage12-N1-2j report", "data/boundary_layers_stage12_n1_2j_report.json"),
    ("Stage12-N1-2k report", "data/final_remainder_stage12_n1_2k_report.json"),
]

SCRIPTS = [
    ("Stage12-N1-2 audit", "scripts/audit_shared_p_hyperbola_stage12_n1_2.py"),
    ("Stage12-N1-2b audit", "scripts/audit_shared_p_average_stage12_n1_2b.py"),
    ("Stage12-N1-2c audit", "scripts/audit_gao_zhao_compatibility_stage12_n1_2c.py"),
    ("Stage12-N1-2d audit", "scripts/audit_modular_hyperbola_stage12_n1_2d.py"),
    ("Stage12-N1-2e audit", "scripts/audit_divisor_dyadic_stage12_n1_2e.py"),
    ("Stage12-N1-2f audit", "scripts/audit_main_term_stage12_n1_2f.py"),
    ("Stage12-N1-2g audit", "scripts/audit_uniform_error_stage12_n1_2g.py"),
    ("Stage12-N1-2h audit", "scripts/audit_poisson_split_stage12_n1_2h.py"),
    ("Stage12-N1-2i audit", "scripts/audit_exponent_budget_stage12_n1_2i.py"),
    ("Stage12-N1-2j audit", "scripts/audit_boundary_layers_stage12_n1_2j.py"),
    ("Stage12-N1-2k audit", "scripts/audit_final_remainder_stage12_n1_2k.py"),
]

PREFACE = r"""
REVIEW_SCOPE=Stage12-N1-2 proof chain only
NOT_A_WHOLE_RESEARCH_REVIEW=true

This bundle is self-contained for reviewing the analytic derivation beginning
with the Stage12-N1-2 hyperbolic-coordinate reduction and ending at
Stage12-N1-2k.  It does not ask the reviewer to reconcile every earlier
empirical, spherical-integral, N2, or algebraic-geometric research note.

Required distinctions:
1. The object reviewed is the primitive oriented count defined by the included
   Stage12-N1-2 chain.  It is not a count of perfect cuboids.
2. Raw counts include imprimitive scale copies.  Primitive counts are related
   by the exact global Möbius operation developed in the included chain.
3. "Oriented" and any later exact-multiplicity interpretation must not be
   silently identified unless the included definitions justify it.
4. Finite computations are regression checks and algebraic certificates; they
   are not substitutes for the analytic estimates.
5. Stage12-N1-2f states that the repeated-side contribution is identically zero.

The final claim presented for adversarial review is

C_prim(B) ~ (kappa/(12*pi)) * B * (log B)^3.

The reviewer must test whether the complete included chain actually proves this
at the stated standard-theorem-application level, including all assumptions,
uniformity, summation, smoothing, parity, local factors, and endpoint terms.
""".strip()

REVIEW_PROTOCOL = r"""
REVIEW_PROTOCOL

Before reviewing, report exactly:
- BUNDLE_ID
- COMPLETED_THROUGH
- SOURCE_SNAPSHOT_COMMIT
- CONTENT_SHA256
- LAST_SOURCE_DOCUMENT
- END_OF_BUNDLE

If any header value is missing, or END_OF_BUNDLE at the bottom is not visible,
return UNREADABLE_SOURCE and do not review from memory or inference.

All required Stage12-N1-2 through 2k documents and audit artifacts are embedded
below.  Do not require secondary GitHub link traversal.

Review adversarially.  Generic conclusions such as "looks correct" are not a
completed review.  For every issue, provide severity FATAL / MAJOR / MINOR /
CLARIFICATION, exact stage and passage, the missing argument, and whether it is
repairable with existing tools or requires a new argument.

The final verdict must be exactly one of:
- CLOSED
- REPAIRABLE
- OPEN
- UNREADABLE_SOURCE

Priority checks:
- exact definition of the counted object and all reindexings;
- Möbius inversion and parity / 2-adic factors;
- coverage and overlap of core, wing, shallow, and terminal regions;
- dependence of O-constants on all moduli and on r,s;
- legitimacy of changing summation order and taking absolute values;
- Ramanujan and exponent-pair estimates, smoothing and endpoints;
- fixed-(r,s) primitive-circle reduction and its uniform averaging;
- hypotheses of the cited multivariable mean-value theorem;
- beta-weight domination and Euler-product pole order;
- every local factor in eta = pi*kappa;
- whether the final asymptotic follows for exactly the defined oriented count.
""".strip()


def read_text(path: str) -> str:
    file_path = Path(path)
    if not file_path.is_file():
        raise FileNotFoundError(path)
    return file_path.read_text(encoding="utf-8")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def slug(text: str) -> str:
    return "".join(character.lower() if character.isalnum() else "-" for character in text).strip("-")


def source_block(kind: str, title: str, path: str, text: str, *, expanded: bool) -> str:
    digest = sha256_text(text)
    escaped = html.escape(text)
    block_id = slug(f"{kind}-{title}")
    if expanded:
        return f"""
<section id="{block_id}" class="source-block">
  <h2>{html.escape(title)}</h2>
  <p class="source-meta">TYPE={kind} | PATH={html.escape(path)} | SHA256={digest} | BYTES={len(text.encode('utf-8'))}</p>
  <pre>{escaped}</pre>
</section>
"""
    return f"""
<details id="{block_id}" class="source-block">
  <summary>{html.escape(title)} — {html.escape(path)}</summary>
  <p class="source-meta">TYPE={kind} | PATH={html.escape(path)} | SHA256={digest} | BYTES={len(text.encode('utf-8'))}</p>
  <pre>{escaped}</pre>
</details>
"""


def build_page() -> str:
    loaded_documents = [(title, path, read_text(path)) for title, path in DOCUMENTS]
    loaded_reports = [(title, path, read_text(path)) for title, path in REPORTS]
    loaded_scripts = [(title, path, read_text(path)) for title, path in SCRIPTS]

    canonical_parts = [PREFACE, REVIEW_PROTOCOL]
    for kind, sources in (
        ("DOCUMENT", loaded_documents),
        ("JSON_REPORT", loaded_reports),
        ("AUDIT_SCRIPT", loaded_scripts),
    ):
        for title, path, text in sources:
            canonical_parts.append(f"===== {kind}: {title} | {path} =====\n{text}")
    canonical_payload = "\n\n".join(canonical_parts)
    content_sha256 = sha256_text(canonical_payload)

    toc_items = "\n".join(
        f'<li><a href="#{slug(f"DOCUMENT-{title}")}">{html.escape(title)}</a></li>'
        for title, _, _ in loaded_documents
    )
    document_html = "\n".join(
        source_block("DOCUMENT", title, path, text, expanded=True)
        for title, path, text in loaded_documents
    )
    report_html = "\n".join(
        source_block("JSON_REPORT", title, path, text, expanded=False)
        for title, path, text in loaded_reports
    )
    script_html = "\n".join(
        source_block("AUDIT_SCRIPT", title, path, text, expanded=False)
        for title, path, text in loaded_scripts
    )

    return f"""<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{BUNDLE_ID}</title>
<style>
:root {{ color-scheme: light dark; }}
body {{ max-width: 1120px; margin: 0 auto; padding: 24px; font-family: system-ui, -apple-system, sans-serif; line-height: 1.55; }}
header, .protocol, .scope {{ border: 2px solid currentColor; border-radius: 10px; padding: 18px; margin-bottom: 22px; }}
h1, h2, h3 {{ line-height: 1.25; }}
code, pre {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }}
pre {{ white-space: pre-wrap; overflow-wrap: anywhere; border: 1px solid #8888; border-radius: 8px; padding: 16px; background: #8881; }}
.source-meta {{ font-size: .82rem; overflow-wrap: anywhere; }}
details {{ margin: 12px 0; border: 1px solid #8888; border-radius: 8px; padding: 10px 14px; }}
summary {{ cursor: pointer; font-weight: 700; }}
nav {{ columns: 2; margin-bottom: 28px; }}
.badge {{ display: inline-block; border: 1px solid currentColor; border-radius: 999px; padding: 2px 9px; margin: 2px; font-family: ui-monospace, monospace; }}
footer {{ margin-top: 36px; padding: 20px; border-top: 4px solid currentColor; font-family: ui-monospace, monospace; overflow-wrap: anywhere; }}
</style>
</head>
<body>
<header>
<h1>Stage12-N1-2 proof-review bundle</h1>
<div class="badge">BUNDLE_ID={BUNDLE_ID}</div>
<div class="badge">COMPLETED_THROUGH={COMPLETED_THROUGH}</div>
<p><strong>SOURCE_SNAPSHOT_COMMIT={SOURCE_SNAPSHOT_COMMIT}</strong></p>
<p><strong>CONTENT_SHA256={content_sha256}</strong></p>
<p><strong>LAST_SOURCE_DOCUMENT={LAST_SOURCE_DOCUMENT}</strong></p>
<p>SOURCE_DOCUMENT_COUNT={len(loaded_documents)} | JSON_REPORT_COUNT={len(loaded_reports)} | AUDIT_SCRIPT_COUNT={len(loaded_scripts)}</p>
</header>
<section class="scope"><h2>Scope and prerequisite statement</h2><pre>{html.escape(PREFACE)}</pre></section>
<section class="protocol"><h2>Mandatory review protocol</h2><pre>{html.escape(REVIEW_PROTOCOL)}</pre></section>
<nav><h2>Embedded research documents</h2><ol>{toc_items}</ol></nav>
<main>
<h1>Part I — Complete mathematical notes</h1>
{document_html}
<h1>Part II — Complete deterministic JSON reports</h1>
<p>These reports are embedded for consistency and finite-regression checking.  They do not replace proof.</p>
{report_html}
<h1>Part III — Complete audit scripts</h1>
<p>These scripts are embedded so a code-capable reviewer can inspect exactly what the finite checks establish.</p>
{script_html}
</main>
<footer>
<p>END_OF_BUNDLE={BUNDLE_ID}</p>
<p>CONTENT_SHA256={content_sha256}</p>
<p>SOURCE_SNAPSHOT_COMMIT={SOURCE_SNAPSHOT_COMMIT}</p>
</footer>
</body>
</html>
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    page = build_page()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(page, encoding="utf-8")
    print(f"wrote {args.output} ({len(page.encode('utf-8'))} bytes)")


if __name__ == "__main__":
    main()
