#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from stage15_6am_coordinate_core_split import threshold_regression, witness_report  # noqa: E402


def require(text: str, needle: str) -> None:
    if needle not in text:
        raise AssertionError(f"missing frozen statement: {needle}")


def main() -> None:
    scan = threshold_regression(24)
    assert scan["checked"] == 24 * 24
    rows = witness_report()
    assert len(rows) == 3
    assert all(row["alpha_marker"]["genus"] == 1 for row in rows)
    assert all(row["beta_marker"]["genus"] == 1 for row in rows)
    assert all(row["alpha_marker"]["resultant_fg"] != 0 for row in rows)

    evidence = json.loads((ROOT / "evidence/stage15_6am_coordinate_core_split.json").read_text())
    assert evidence["fixed_anchor_kappa_unique"] is True
    assert evidence["large_coordinate_core_sqrt_collapse"] is True
    assert evidence["small_kappa_quartic_separable"] is True
    assert evidence["small_kappa_quartic_geometric_genus"] == 1
    assert evidence["small_kappa_global_count_proved"] is False

    result = (ROOT / "15-6am/result.md").read_text()
    for needle in [
        "STAGE15_6AM_LARGE_COORDINATE_CORE_BOUND=true",
        "STAGE15_6AM_LARGE_COORDINATE_CORE_SQRT_COLLAPSE=true",
        "STAGE15_6AM_HIGH_BRANCH_THRESHOLD=kappa^2>=Z*W",
        "STAGE15_6AM_SMALL_KAPPA_ONE_POINT_QUARTIC=true",
        "STAGE15_6AM_SMALL_KAPPA_QUARTIC_GEOMETRIC_GENUS=1",
        "STAGE15_6AM_EXIT=LARGE_COORDINATE_CORE_CONTROLLED_SMALL_KAPPA_QUARTIC_THEOREM_GATE",
    ]:
        require(result, needle)

    predecessor = (ROOT / "15-6al/result.md").read_text()
    require(predecessor, "STAGE15_6AL_EXIT=COORDINATE_CORE_SIZE_DICHOTOMY_READY")

    print("STAGE15_6AM_VERIFY=PASS")
    print(scan)
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
