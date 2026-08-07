#!/usr/bin/env python3
"""Verify frozen Stage12-N1 historical manifests and review bundles.

The source documents were archived after these bundles were frozen, and
00_CURRENT_RESEARCH_STATUS.md is intentionally mutable.  Verification of a
frozen bundle must therefore use its pinned URLs and embedded handshakes,
not require historical source paths or old status markers to remain in the
current working tree.
"""
from __future__ import annotations

from pathlib import Path

COMPLETED_THROUGH = "Stage12-N1-2k"

HISTORICAL_DOCUMENT_ID = "PC-N1-REVIEW-2B-2K-20260806-1545-JST"
HISTORICAL_SOURCE_COMMIT = "5ae4057e8a83a23d7accee5b5145290e2a65e198"
HISTORICAL_MANIFEST = Path(
    "docs/review/stage12-n1-2b-to-2k-review-manifest-20260806-1545.md"
)

CURRENT_BUNDLE_ID = "PC-N1-2-PROOF-REVIEW-20260806-1645-R02"
CURRENT_SOURCE_COMMIT = "8d6910e8e68145e474f92716460a1cc6f384ecf1"
CURRENT_CONTENT_SHA256 = "201cad458d172e0939e5508b78e6e06abe894d908390f0c1b54c51a16e63d586"
CURRENT_PAGE = Path("review/PC-N1-2-PROOF-REVIEW-20260806-R02.html")

EXPECTED_DOCS = [
    "docs/stage12-n1-2b-average.md",
    "docs/stage12-n1-2c-gao-zhao.md",
    "docs/stage12-n1-2d-modular-hyperbola.md",
    "docs/stage12-n1-2e-divisor-dyadic.md",
    "docs/stage12-n1-2f-main-term.md",
    "docs/stage12-n1-2g-uniform-error.md",
    "docs/stage12-n1-2h-poisson-split.md",
    "docs/stage12-n1-2i-exponent-budget.md",
    "docs/stage12-n1-2j-boundary-layers.md",
    "docs/stage12-n1-2k-final-remainder.md",
]


def require(text: str, needle: str, source: Path) -> None:
    if needle not in text:
        raise SystemExit(f"missing {needle!r} in {source}")


def verify_historical_manifest() -> None:
    manifest = HISTORICAL_MANIFEST.read_text(encoding="utf-8")
    require(manifest, HISTORICAL_DOCUMENT_ID, HISTORICAL_MANIFEST)
    require(manifest, COMPLETED_THROUGH, HISTORICAL_MANIFEST)
    require(manifest, HISTORICAL_SOURCE_COMMIT, HISTORICAL_MANIFEST)

    pinned_prefix = (
        "https://github.com/fizawa460-bit/perfect-cuboid-game/blob/"
        f"{HISTORICAL_SOURCE_COMMIT}/"
    )
    for path in EXPECTED_DOCS:
        require(manifest, pinned_prefix + path, HISTORICAL_MANIFEST)


def verify_current_bundle() -> None:
    page = CURRENT_PAGE.read_text(encoding="utf-8")

    main_start = page.index('<main id="review-bundle-main">')
    main_end = page.index("</main>", main_start)
    main = page[main_start:main_end]
    markers = (
        f"BUNDLE_ID={CURRENT_BUNDLE_ID}",
        f"COMPLETED_THROUGH={COMPLETED_THROUGH}",
        f"SOURCE_SNAPSHOT_COMMIT={CURRENT_SOURCE_COMMIT}",
        f"CONTENT_SHA256={CURRENT_CONTENT_SHA256}",
        "LAST_SOURCE_DOCUMENT=docs/stage12-n1-2k-final-remainder.md",
        f"END_OF_BUNDLE={CURRENT_BUNDLE_ID}",
    )
    for marker in markers:
        if main.count(marker) < 4:
            raise SystemExit(f"marker is not repeated four times inside main: {marker}")

    for checkpoint in (
        "CHECKPOINT=START_OF_MAIN",
        "CHECKPOINT=BEFORE_EMBEDDED_SOURCES",
        "CHECKPOINT=AFTER_EMBEDDED_SOURCES",
        "CHECKPOINT=END_OF_MAIN",
        "PAGE_STRUCTURE=ALL_HANDSHAKES_INSIDE_MAIN_R02",
        "SOURCE_DOCUMENT_COUNT=11 | JSON_REPORT_COUNT=11 | AUDIT_SCRIPT_COUNT=11",
        "audit_final_remainder_stage12_n1_2k.py",
    ):
        require(main, checkpoint, CURRENT_PAGE)

    if len(page.encode("utf-8")) <= 250_000:
        raise SystemExit("self-contained review page is unexpectedly small")


def main() -> None:
    verify_historical_manifest()
    verify_current_bundle()
    print("Stage12-N1 frozen review sources verified")
    print(f"HISTORICAL_DOCUMENT_ID={HISTORICAL_DOCUMENT_ID}")
    print(f"CURRENT_BUNDLE_ID={CURRENT_BUNDLE_ID}")
    print(f"COMPLETED_THROUGH={COMPLETED_THROUGH}")
    print(f"CURRENT_SOURCE_SNAPSHOT_COMMIT={CURRENT_SOURCE_COMMIT}")
    print(f"CONTENT_SHA256={CURRENT_CONTENT_SHA256}")
    print("HANDSHAKE_COPIES_INSIDE_MAIN=4")
    print(f"EMBEDDED_SOURCE_FILES={11 + 11 + 11}")


if __name__ == "__main__":
    main()
