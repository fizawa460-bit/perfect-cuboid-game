#!/usr/bin/env python3
"""Verify the canonical Stage12-N1 review status and versioned manifest."""
from __future__ import annotations

from pathlib import Path

DOCUMENT_ID = "PC-N1-REVIEW-2B-2K-20260806-1545-JST"
COMPLETED_THROUGH = "Stage12-N1-2k"
SOURCE_COMMIT = "5ae4057e8a83a23d7accee5b5145290e2a65e198"
MANIFEST = Path("docs/review/stage12-n1-2b-to-2k-review-manifest-20260806-1545.md")
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


def main() -> None:
    manifest = MANIFEST.read_text(encoding="utf-8")
    status = STATUS.read_text(encoding="utf-8")

    for source, text in ((MANIFEST, manifest), (STATUS, status)):
        require(text, DOCUMENT_ID, source)
        require(text, COMPLETED_THROUGH, source)
        require(text, SOURCE_COMMIT, source)

    require(status, str(MANIFEST), STATUS)

    pinned_prefix = (
        "https://github.com/fizawa460-bit/perfect-cuboid-game/blob/"
        f"{SOURCE_COMMIT}/"
    )
    for path in EXPECTED_DOCS:
        require(manifest, pinned_prefix + path, MANIFEST)
        if not Path(path).is_file():
            raise SystemExit(f"source document is missing: {path}")

    forbidden_mutable = [
        "/blob/main/docs/stage12-n1-2",
        "/blob/master/docs/stage12-n1-2",
        "/blob/agent/stage12-n1-2b-average/docs/stage12-n1-2",
    ]
    for needle in forbidden_mutable:
        if needle in manifest:
            raise SystemExit(f"mutable review source found: {needle}")

    print("Stage12-N1 review manifest verified")
    print(f"DOCUMENT_ID={DOCUMENT_ID}")
    print(f"COMPLETED_THROUGH={COMPLETED_THROUGH}")
    print(f"SOURCE_SNAPSHOT_COMMIT={SOURCE_COMMIT}")
    print(f"PINNED_DOCUMENTS={len(EXPECTED_DOCS)}")


if __name__ == "__main__":
    main()
