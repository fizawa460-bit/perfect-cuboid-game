#!/usr/bin/env python3
"""Verify frozen and repaired Stage12-N1 review bundles."""
from __future__ import annotations

import hashlib
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

REPAIRED_BUNDLE_ID = "PC-N1-2-REPAIRED-PROOF-20260807-R02"
REPAIRED_COMPLETED_THROUGH = "Stage12-N1-3d"
REPAIRED_SOURCE_COMMIT = "08a3bc0b8428f9c620269da9b488e8b849cf909c"
REPAIRED_LEDGER_SHA256 = (
    "26528cd336fe4b6ce5bc70bdca368ad605f29f711bec71e34a6427d98b3560dc"
)
REPAIRED_LAST_SOURCE = "docs/stage12-n1-2-final-r02.md"
REPAIRED_STATUS = "REPAIRED_CANDIDATE_PENDING_INDEPENDENT_REAUDIT"
REPAIRED_MANIFEST = Path(
    "docs/review/stage12-n1-2-repaired-review-manifest-20260807-r02.md"
)
REPAIRED_PAGE = Path("review/PC-N1-2-REPAIRED-PROOF-20260807-R02.html")
REPAIRED_SOURCES = [
    (
        Path("docs/stage12-n1-3d-definition-sheet.md"),
        "b44f76a890363708d6274d14b7f7154894debc7b",
    ),
    (
        Path("docs/stage12-n1-3d-constant-sheet.md"),
        "3428f220c35c3625589dc44abf55819b48109631",
    ),
    (
        Path("docs/stage12-n1-3d-selberg-delange-reference-lock.md"),
        "23f887107b0babaadfcf6d6dc2e4255921c3651d",
    ),
    (
        Path("docs/stage12-n1-2-final-r02.md"),
        "e343182e82d9ecacf844fa7e508662749d43b55b",
    ),
]
ARCHIVED_2J = Path(
    "docs/archive/stage12-n1-2/stage12-n1-2j-boundary-layers.md"
)
LEGACY_FINAL = Path("docs/stage12-n1-2-final.md")


def require(text: str, needle: str, source: Path) -> None:
    if needle not in text:
        raise SystemExit(f"missing {needle!r} in {source}")


def git_blob_sha(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


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


def verify_frozen_current_bundle() -> None:
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
            raise SystemExit(
                f"marker is not repeated four times inside frozen main: {marker}"
            )

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
        raise SystemExit("frozen self-contained review page is unexpectedly small")


def verify_repaired_source_ledger() -> None:
    ledger_lines: list[str] = []
    for path, expected_blob in REPAIRED_SOURCES:
        data = path.read_bytes()
        actual_blob = git_blob_sha(data)
        if actual_blob != expected_blob:
            raise SystemExit(
                f"repaired source blob mismatch for {path}: "
                f"expected {expected_blob}, got {actual_blob}"
            )
        text = data.decode("utf-8")
        if "\x0c" in text:
            raise SystemExit(f"form-feed control character found in {path}")
        ledger_lines.append(f"{path.as_posix()}\t{expected_blob}")

    ledger = "\n".join(ledger_lines) + "\n"
    actual_ledger_sha = hashlib.sha256(ledger.encode("utf-8")).hexdigest()
    if actual_ledger_sha != REPAIRED_LEDGER_SHA256:
        raise SystemExit(
            "repaired source ledger SHA mismatch: "
            f"expected {REPAIRED_LEDGER_SHA256}, got {actual_ledger_sha}"
        )


def verify_repaired_manifest() -> None:
    manifest = REPAIRED_MANIFEST.read_text(encoding="utf-8")
    for needle in (
        REPAIRED_BUNDLE_ID,
        REPAIRED_COMPLETED_THROUGH,
        REPAIRED_SOURCE_COMMIT,
        REPAIRED_LEDGER_SHA256,
        REPAIRED_LAST_SOURCE,
        REPAIRED_STATUS,
        "MAJOR_04=CLOSED_BY_STAGE12_N1_3D",
        "CLARIFICATION_01=CLOSED_BY_STAGE12_N1_3D_REFERENCE_LOCK",
    ):
        require(manifest, needle, REPAIRED_MANIFEST)

    pinned_prefix = (
        "https://github.com/fizawa460-bit/perfect-cuboid-game/blob/"
        f"{REPAIRED_SOURCE_COMMIT}/"
    )
    for path, blob_sha in REPAIRED_SOURCES:
        require(manifest, pinned_prefix + path.as_posix(), REPAIRED_MANIFEST)
        require(manifest, blob_sha, REPAIRED_MANIFEST)


def verify_repaired_bundle() -> None:
    page = REPAIRED_PAGE.read_text(encoding="utf-8")
    if "\x0c" in page:
        raise SystemExit("form-feed control character found in repaired HTML")

    main_start = page.index('<main id="review-bundle-main">')
    main_end = page.index("</main>", main_start)
    main = page[main_start:main_end]

    markers = (
        f"BUNDLE_ID={REPAIRED_BUNDLE_ID}",
        f"COMPLETED_THROUGH={REPAIRED_COMPLETED_THROUGH}",
        f"SOURCE_SNAPSHOT_COMMIT={REPAIRED_SOURCE_COMMIT}",
        f"SOURCE_LEDGER_SHA256={REPAIRED_LEDGER_SHA256}",
        f"LAST_SOURCE_DOCUMENT={REPAIRED_LAST_SOURCE}",
        f"THEOREM_STATUS={REPAIRED_STATUS}",
        f"END_OF_BUNDLE={REPAIRED_BUNDLE_ID}",
    )
    for marker in markers:
        if main.count(marker) < 4:
            raise SystemExit(
                f"marker is not repeated four times inside repaired main: {marker}"
            )

    for checkpoint in (
        "CHECKPOINT=START_OF_MAIN",
        "CHECKPOINT=BEFORE_PROOF",
        "CHECKPOINT=AFTER_PROOF",
        "CHECKPOINT=END_OF_MAIN",
        "PAGE_STRUCTURE=ALL_HANDSHAKES_INSIDE_MAIN_R02",
        "SOURCE_DOCUMENT_COUNT=4",
        "BUNDLE_SELF_CONTAINED=true",
        "C_prim(B) = sum_{k&lt;=B} mu(k) C_raw(floor(B/k))",
        "eta=pi kappa",
        "C_lambda^(0)=8 eta/pi^2",
        "SUPERSEDED_NOT_REQUIRED",
        "arbitrary fixed log-power",
        "independent re-audit pending",
    ):
        require(main, checkpoint, REPAIRED_PAGE)

    for _path, blob_sha in REPAIRED_SOURCES:
        require(main, blob_sha, REPAIRED_PAGE)

    # Marker and section coverage above is the primary truncation guard.  Keep a
    # modest floor only to catch an accidentally empty shell; unlike the frozen
    # source-dump bundle, this R02 page intentionally summarizes four pinned
    # source documents instead of embedding hundreds of kilobytes verbatim.
    if len(page.encode("utf-8")) <= 12_000:
        raise SystemExit("repaired self-contained review page is unexpectedly small")


def verify_minor_repairs() -> None:
    archived_2j = ARCHIVED_2J.read_text(encoding="utf-8")
    if "\x0c" in archived_2j:
        raise SystemExit("form-feed control character remains in archived 2j")
    require(
        archived_2j,
        r"1+\frac{2t(p-1)}{p+1}",
        ARCHIVED_2J,
    )

    legacy_final = LEGACY_FINAL.read_text(encoding="utf-8")
    require(legacy_final, "SUPERSEDED_BY_STAGE12_N1_2_FINAL_R02", LEGACY_FINAL)
    require(legacy_final, "docs/stage12-n1-2-final-r02.md", LEGACY_FINAL)


def main() -> None:
    verify_historical_manifest()
    verify_frozen_current_bundle()
    verify_repaired_source_ledger()
    verify_repaired_manifest()
    verify_repaired_bundle()
    verify_minor_repairs()

    print("Stage12-N1 frozen and repaired review sources verified")
    print(f"HISTORICAL_DOCUMENT_ID={HISTORICAL_DOCUMENT_ID}")
    print(f"FROZEN_BUNDLE_ID={CURRENT_BUNDLE_ID}")
    print(f"REPAIRED_BUNDLE_ID={REPAIRED_BUNDLE_ID}")
    print(f"REPAIRED_COMPLETED_THROUGH={REPAIRED_COMPLETED_THROUGH}")
    print(f"REPAIRED_SOURCE_SNAPSHOT_COMMIT={REPAIRED_SOURCE_COMMIT}")
    print(f"REPAIRED_SOURCE_LEDGER_SHA256={REPAIRED_LEDGER_SHA256}")
    print("REPAIRED_HANDSHAKE_COPIES_INSIDE_MAIN=4")
    print(f"REPAIRED_SOURCE_DOCUMENTS={len(REPAIRED_SOURCES)}")
    print("CONTROL_CHARACTER_CHECK=PASS")


if __name__ == "__main__":
    main()
