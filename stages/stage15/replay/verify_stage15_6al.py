#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from stage15_6al_coordinate_cells import actual_witness_report, exhaustive_cell_scan  # noqa: E402


def require(text: str, needle: str) -> None:
    if needle not in text:
        raise AssertionError(f"missing frozen statement: {needle}")


def main() -> None:
    scan = exhaustive_cell_scan(8)
    assert scan["checked"] > 100
    rows = actual_witness_report()
    assert len(rows) == 3
    assert all(row["kappa"] == row["agree"] * row["switch"] for row in rows)
    assert all(__import__("math").gcd(row["k"], row["kappa"]) == 1 for row in rows)

    evidence = json.loads((ROOT / "evidence/stage15_6al_coordinate_cells.json").read_text())
    assert evidence["four_cells_pairwise_coprime"] is True
    assert evidence["norm_core_coordinate_core_coprime"] is True
    assert evidence["coordinate_core_rootline_adapter"] is True

    result = (ROOT / "15-6al/result.md").read_text()
    for needle in [
        "STAGE15_6AL_COMMON_COORDINATE_CORE_DEFINED=true",
        "STAGE15_6AL_FOUR_CELLS_PAIRWISE_COPRIME=true",
        "STAGE15_6AL_NORM_CORE_COORDINATE_CORE_COPRIME=true",
        "STAGE15_6AL_COORDINATE_CORE_ROOTLINE_ADAPTER=true",
        "STAGE15_6AL_EXIT=COORDINATE_CORE_SIZE_DICHOTOMY_READY",
    ]:
        require(result, needle)

    predecessor = (ROOT / "15-6ak/result.md").read_text()
    require(predecessor, "STAGE15_6AK_EXIT=GLOBAL_COORDINATE_PRODUCT_SQUARECLASS_DECOMPOSITION_READY")

    print("STAGE15_6AL_VERIFY=PASS")
    print(scan)
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
