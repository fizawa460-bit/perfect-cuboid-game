#!/usr/bin/env python3
"""Verify both the historical link manifest and the current self-contained bundle."""
from __future__ import annotations

from pathlib import Path

COMPLETED_THROUGH = "Stage12-N1-2k"

HISTORICAL_DOCUMENT_ID = "PC-N1-REVIEW-2B-2K-20260806-1545-JST"
HISTORICAL_SOURCE_COMMIT = "5ae4057e8a83a23d7accee5b5145290e2a65e198"
HISTORICAL_MANIFEST = Path("docs/review/stage12-n1-2b-to-2k-review-manifest-20260806-1545.md")

CURRENT_DOCUMENT_ID = "PC-N1-CURRENT-20260806-1612-JST"
CURRENT_BUNDLE_ID = "PC-N1-2-PROOF-REVIEW-20260806-1612-R01"
CURRENT_SOURCE_COMMIT = "0e8bbc6e745ddf6d1f7c0ba3b21bb328a1fcc4d2"
CURRENT_CONTENT_SHA256 = "201cad458d172e0939e5508b78e6e06abe894d908390f0c1b54c51a16e63d586"
CURRENT_PAGE = Path("review/PC-N1-2-PROOF-REVIEW-20260806-R01.html")
STATUS = Path("docs/00_CURRENT_RESEARCH_STATUS.md")

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
        if not Path(path).is_file():
            raise SystemExit(f"source document is missing: {path}")

    forbidden_mutable = [
        "/blob/main/docs/stage12-n1-2",
        "/blob/master/docs/stage12-n1-2",
        "/blob/agent/stage12-n1-2b-average/docs/stage12-n1-2",
    ]
    for needle in forbidden_mutable:
        if needle in manifest:
            raise SystemExit(f"mutable historical review source found: {needle}")


def verify_current_bundle() -> None:
    status = STATUS.read_text(encoding="utf-8")
    page = CURRENT_PAGE.read_text(encoding="utf-8")

    for needle in (
        CURRENT_DOCUMENT_ID,
        CURRENT_BUNDLE_ID,
        COMPLETED_THROUGH,
        CURRENT_SOURCE_COMMIT,
        CURRENT_CONTENT_SHA256,
        str(CURRENT_PAGE),
    ):
        require(status, needle, STATUS)

    for needle in (
        f"BUNDLE_ID={CURRENT_BUNDLE_ID}",
        f"COMPLETED_THROUGH={COMPLETED_THROUGH}",
        f"SOURCE_SNAPSHOT_COMMIT={CURRENT_SOURCE_COMMIT}",
        f"CONTENT_SHA256={CURRENT_CONTENT_SHA256}",
        "LAST_SOURCE_DOCUMENT=docs/stage12-n1-2k-final-remainder.md",
        f"END_OF_BUNDLE={CURRENT_BUNDLE_ID}",
        "SOURCE_DOCUMENT_COUNT=11 | JSON_REPORT_COUNT=11 | AUDIT_SCRIPT_COUNT=11",
    ):
        require(page, needle, CURRENT_PAGE)

    if len(page.encode("utf-8")) <= 250_000:
        raise SystemExit("self-contained review page is unexpectedly small")


def main() -> None:
    verify_historical_manifest()
    verify_current_bundle()
    print("Stage12-N1 review sources verified")
    print(f"HISTORICAL_DOCUMENT_ID={HISTORICAL_DOCUMENT_ID}")
    print(f"CURRENT_BUNDLE_ID={CURRENT_BUNDLE_ID}")
    print(f"COMPLETED_THROUGH={COMPLETED_THROUGH}")
    print(f"CURRENT_SOURCE_SNAPSHOT_COMMIT={CURRENT_SOURCE_COMMIT}")
    print(f"CONTENT_SHA256={CURRENT_CONTENT_SHA256}")
    print(f"EMBEDDED_SOURCE_FILES={11 + 11 + 11}")


if __name__ == "__main__":
    main()
