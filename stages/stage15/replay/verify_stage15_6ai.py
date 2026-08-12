#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from stage15_6ai_genus_one_model import scan_outer_pairs, witness_report  # noqa: E402


def require(text: str, needle: str) -> None:
    if needle not in text:
        raise AssertionError(f"missing frozen statement: {needle}")


def main() -> None:
    scan = scan_outer_pairs(50)
    assert scan["checked"] > 100
    assert scan["min_discriminant_marker"] > 0
    assert scan["distinct_cross_ratios"] > 20

    rows = witness_report()
    assert len(rows) == 3
    assert all(row["q1"] == 0 and row["q2"] == 0 for row in rows)
    assert len({tuple(row["cross_ratio"]) for row in rows}) >= 2

    evidence = json.loads((ROOT / "evidence/stage15_6ai_genus_one_model.json").read_text())
    cls = evidence["classification"]
    assert evidence["exact_model"] == "TWO_QUADRICS_IN_P3"
    assert cls["qbar_universal_diagonal_form"] is True
    assert cls["pencil_roots_distinct"] is True
    assert cls["geometrically_smooth"] is True
    assert cls["geometrically_integral"] is True
    assert cls["geometric_genus"] == 1
    assert cls["physical_singular_conic_branch"] is False
    assert evidence["arsenal"]["direct_genus_one_count_match"] is False
    assert evidence["nonclaims"]["genus_one_counting_theorem_applied"] is False
    assert evidence["nonclaims"]["height_measure_adapter_proved"] is False

    result = (ROOT / "15-6ai/result.md").read_text()
    for needle in [
        "STAGE15_6AI_EXACT_MODEL=TWO_QUADRICS_IN_P3",
        "STAGE15_6AI_PHYSICAL_PENCIL_ROOTS_DISTINCT=true",
        "STAGE15_6AI_PHYSICAL_CURVE_SMOOTH=true",
        "STAGE15_6AI_GEOMETRICALLY_INTEGRAL=true",
        "STAGE15_6AI_GEOMETRIC_GENUS=1",
        "STAGE15_6AI_PHYSICAL_SINGULAR_CONIC_BRANCH=false",
        "STAGE15_6AI_MOVING_OUTER_GEOMETRY=true",
        "STAGE15_6AI_GENUS_ONE_COUNTING_THEOREM_APPLIED=false",
        "STAGE15_6AI_HEIGHT_MEASURE_ADAPTER_PROVED=false",
        "STAGE15_6AI_EXIT=SMOOTH_MOVING_GENUS_ONE_FAMILY_HEIGHT_AUDIT_READY",
    ]:
        require(result, needle)

    predecessor = (ROOT / "15-6ah/result.md").read_text()
    require(predecessor, "STAGE15_6AH_EXIT=FULL_COMMON_SUPPORT_EXHAUSTED_SMALL_TOTAL_SUPPORT_ONE_POINT_GATE_READY")

    print("STAGE15_6AI_VERIFY=PASS")
    print("EXACT_MODEL=TWO_QUADRICS_IN_P3")
    print("PHYSICAL_CURVE_SMOOTH=true")
    print("GEOMETRIC_GENUS=1")
    print("PHYSICAL_SINGULAR_CONIC_BRANCH=false")
    print("HEIGHT_MEASURE_ADAPTER_PROVED=false")


if __name__ == "__main__":
    main()
