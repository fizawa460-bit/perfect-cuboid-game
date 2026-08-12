#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from stage15_6ak_outer_reconstruction import exhaustive_coordinate_scan, witness_report  # noqa: E402


def require(text: str, needle: str) -> None:
    if needle not in text:
        raise AssertionError(f"missing frozen statement: {needle}")


def main() -> None:
    scan = exhaustive_coordinate_scan(9)
    assert scan["product_square_candidates"] > 100
    assert scan["reconstructed"] == scan["product_square_candidates"]
    rows = witness_report()
    assert len(rows) == 3
    assert all(row["product"] == row["sqrt_product"] ** 2 for row in rows)

    evidence = json.loads((ROOT / "evidence/stage15_6ak_outer_reconstruction.json").read_text())
    assert evidence["product_square_toric_compatibility_iff"] is True
    assert evidence["outer_pair_reconstruction_unique"] is True
    assert evidence["naive_polynomial_outer_curve_sum_required"] is False

    result = (ROOT / "15-6ak/result.md").read_text()
    for needle in [
        "STAGE15_6AK_PRODUCT_SQUARE_TORIC_COMPATIBILITY_IFF=true",
        "STAGE15_6AK_TORIC_COMPATIBILITY=x*y*p*q_is_square",
        "STAGE15_6AK_OUTER_PAIR_RECONSTRUCTION_UNIQUE=true",
        "STAGE15_6AK_NAIVE_POLYNOMIAL_OUTER_CURVE_SUM_REQUIRED=false",
        "STAGE15_6AK_EXIT=GLOBAL_COORDINATE_PRODUCT_SQUARECLASS_DECOMPOSITION_READY",
    ]:
        require(result, needle)

    predecessor = (ROOT / "15-6aj/result.md").read_text()
    require(predecessor, "STAGE15_6AJ_EXIT=EXACT_PRODUCT_HEIGHT_AND_OUTER_RECONSTRUCTION_AUDIT_READY")

    print("STAGE15_6AK_VERIFY=PASS")
    print(scan)
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
