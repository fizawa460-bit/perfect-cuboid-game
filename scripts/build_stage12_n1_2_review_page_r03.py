#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

import build_stage12_n1_2_review_page as base

BUNDLE_ID = "PC-N1-2-PROOF-REVIEW-20260806-1845-R03"
COMPLETED_THROUGH = "Stage12-N1-2n"
SOURCE_SNAPSHOT_COMMIT = "d362b3e809cc3db6b9c79eadce5ff06a5c6ab4a8"
LAST_SOURCE_DOCUMENT = "docs/stage12-n1-2n-coupled-region.md"
DEFAULT_OUTPUT = Path("review/PC-N1-2-PROOF-REVIEW-20260806-R03.html")

EXTRA_DOCUMENTS = [
    ("Stage12-N1-2l", "docs/stage12-n1-2l-dlb-hypotheses.md"),
    ("Stage12-N1-2m", "docs/stage12-n1-2m-iterated-selberg-delange.md"),
    ("Stage12-N1-2n", "docs/stage12-n1-2n-coupled-region.md"),
]
EXTRA_REPORTS = [
    ("Stage12-N1-2l report", "data/dlb_hypotheses_stage12_n1_2l_report.json"),
    ("Stage12-N1-2m report", "data/iterated_selberg_delange_stage12_n1_2m_report.json"),
    ("Stage12-N1-2n report", "data/coupled_region_stage12_n1_2n_report.json"),
]
EXTRA_SCRIPTS = [
    ("Stage12-N1-2l audit", "scripts/audit_dlb_hypotheses_stage12_n1_2l.py"),
    ("Stage12-N1-2m audit", "scripts/audit_iterated_selberg_delange_stage12_n1_2m.py"),
    ("Stage12-N1-2n audit", "scripts/audit_coupled_region_stage12_n1_2n.py"),
]

ROUND1_RESPONSE = r"""
ROUND_1_RESPONSE_MAP

Round 1 consensus was REPAIRABLE rather than CLOSED.
Accepted principal objections:
1. Stage12-N1-2k invoked de la Bretèche without verifying P2/P3.
2. The fixed-(r,s) remainder and outer averaging needed explicit uniform control.
3. The relation between the old 2h-2i Poisson route and the final route was ambiguous.

Repairs under review:
- 2l withdraws the old CLOSED classification and audits the exact P1-P3 hypotheses.
- 2m replaces the unverified multivariable theorem step with one-variable beta
  Dirichlet series, an absolutely convergent coprimality correction, and iterated
  Selberg-Delange.
- 2n transfers the rectangular estimates to the coupled radial/height region by
  dyadic decomposition and Abel/Stieltjes summation.
- 2n classifies 2h-2i as superseded audit history, not part of the final proof route.
- eta=pi*kappa remains an exact local-factor identity; numerical products are
  diagnostic only.

Current status is deliberately not CLOSED:
REPAIRED_PROOF_CHAIN_PENDING_ROUND2_ADVERSARIAL_REVIEW
""".strip()

PREFACE = r"""
REVIEW_SCOPE=Stage12-N1-2 proof chain, Round 2 repair review
NOT_A_WHOLE_RESEARCH_REVIEW=true
FINAL_ROUTE=Stage12-N1-2j -> 2k -> 2l -> 2m -> 2n
SUPERSEDED_AUDIT_ROUTE=Stage12-N1-2h -> 2i

The counted object is the primitive oriented count defined in the included notes,
not perfect cuboids and not the exact-one count N1 by itself.

Candidate conclusion:
C_prim(B) ~ (kappa/(12*pi)) * B * (log B)^3.

Do not assume the repair succeeded. Verify whether 2l-2n actually fix the
Round 1 objections and whether the revised route introduces any new FATAL or
MAJOR gap.
""".strip()

PROTOCOL = r"""
ROUND_2_ADVERSARIAL_REVIEW_PROTOCOL

Before reviewing, report exactly:
- BUNDLE_ID
- COMPLETED_THROUGH
- SOURCE_SNAPSHOT_COMMIT
- CONTENT_SHA256
- LAST_SOURCE_DOCUMENT
- END_OF_BUNDLE
- CHECKPOINT=START_OF_MAIN
- CHECKPOINT=END_OF_MAIN

If any item is unavailable, return UNREADABLE_SOURCE and do not infer missing text.

Review all embedded notes through 2n, focusing on the repair patch:
A. Does 2l correctly reject the unverified direct de la Bretèche application?
B. Does 2m rigorously factor the beta two-variable series into one-variable
   factors and an absolutely convergent coprimality correction?
C. Are the one-variable Selberg-Delange estimates uniform enough for iteration?
D. Does 2n legitimately transfer rectangular estimates to h(r^2+s^2)<=2B?
E. Are shallow, arc, diagonal, parity and floor endpoints truly o(B(log B)^3)?
F. Is it correct that 2h-2i are no longer required by the final proof route?
G. Does eta=pi*kappa remain exact with all local and front factors?

For each issue provide FATAL / MAJOR / MINOR / CLARIFICATION, exact location,
missing argument, and repairability. Final verdict must be exactly CLOSED,
REPAIRABLE, OPEN, or UNREADABLE_SOURCE.
""".strip()


def marker(label: str, content_sha: str) -> str:
    return f'''<section class="protocol machine-readable-handshake" data-checkpoint="{label}">
<h2>Machine-readable bundle handshake — {label}</h2>
<pre>BUNDLE_ID={BUNDLE_ID}
COMPLETED_THROUGH={COMPLETED_THROUGH}
SOURCE_SNAPSHOT_COMMIT={SOURCE_SNAPSHOT_COMMIT}
CONTENT_SHA256={content_sha}
LAST_SOURCE_DOCUMENT={LAST_SOURCE_DOCUMENT}
END_OF_BUNDLE={BUNDLE_ID}
PAGE_STRUCTURE=ALL_HANDSHAKES_INSIDE_MAIN_R03
CHECKPOINT={label}</pre>
</section>'''


def build_page() -> str:
    base.BUNDLE_ID = BUNDLE_ID
    base.COMPLETED_THROUGH = COMPLETED_THROUGH
    base.SOURCE_SNAPSHOT_COMMIT = SOURCE_SNAPSHOT_COMMIT
    base.LAST_SOURCE_DOCUMENT = LAST_SOURCE_DOCUMENT
    base.DOCUMENTS = list(base.DOCUMENTS) + EXTRA_DOCUMENTS
    base.REPORTS = list(base.REPORTS) + EXTRA_REPORTS
    base.SCRIPTS = list(base.SCRIPTS) + EXTRA_SCRIPTS
    base.PREFACE = PREFACE + "\n\n" + ROUND1_RESPONSE
    base.REVIEW_PROTOCOL = PROTOCOL
    page = base.build_page()

    content_sha = page.split("CONTENT_SHA256=", 1)[1].split("<", 1)[0]
    page = page.replace("<body>\n<header>", "<body>\n<main id=\"review-bundle-main\">\n" + marker("START_OF_MAIN", content_sha) + "\n<header>", 1)
    page = page.replace("\n<main>\n<h1>Part I", "\n" + marker("BEFORE_EMBEDDED_SOURCES", content_sha) + "\n<h1>Part I", 1)
    page = page.replace("\n</main>\n<footer>", "\n" + marker("AFTER_EMBEDDED_SOURCES", content_sha) + "\n<footer>", 1)
    page = page.replace("\n</footer>\n</body>", "\n</footer>\n" + marker("END_OF_MAIN", content_sha) + "\n</main>\n</body>", 1)
    return page


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
