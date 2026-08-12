#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from stage15_6aj_height_bridge import exhaustive_gcd_scan, witness_report  # noqa: E402


def require(text: str, needle: str) -> None:
    if needle not in text:
        raise AssertionError(f"missing frozen statement: {needle}")


def main() -> None:
    scan = exhaustive_gcd_scan(18)
    assert scan["checked"] > 1000
    assert scan["gamma2"] > 0 and scan["gamma4"] > 0
    rows = witness_report()
    assert len(rows) == 3
    assert all(row["kZW"] <= 2 * row["R"] for row in rows)

    evidence = json.loads((ROOT / "evidence/stage15_6aj_height_bridge.json").read_text())
    assert evidence["raw_gcd_factorization"] == "G=gamma*h_alpha*h_beta"
    assert evidence["gamma_values"] == [2, 4]
    assert evidence["forward_height_measure_adapter_proved"] is True
    assert evidence["genus_one_counting_theorem_applied"] is False

    result = (ROOT / "15-6aj/result.md").read_text()
    for needle in [
        "STAGE15_6AJ_RAW_GCD_FACTORIZATION=true",
        "STAGE15_6AJ_EXACT_PHYSICAL_HEIGHT_FACTORIZATION=true",
        "STAGE15_6AJ_PRODUCT_HEIGHT_CUTOFF=k*N(z)*N(w)<=2B",
        "STAGE15_6AJ_FORWARD_HEIGHT_MEASURE_ADAPTER_PROVED=true",
        "STAGE15_6AJ_NAIVE_SUM_OVER_OUTER_CURVES_LICENSED=false",
        "STAGE15_6AJ_EXIT=EXACT_PRODUCT_HEIGHT_AND_OUTER_RECONSTRUCTION_AUDIT_READY",
    ]:
        require(result, needle)

    predecessor = (ROOT / "15-6ai/result.md").read_text()
    require(predecessor, "STAGE15_6AI_EXIT=SMOOTH_MOVING_GENUS_ONE_FAMILY_HEIGHT_AUDIT_READY")

    print("STAGE15_6AJ_VERIFY=PASS")
    print(scan)
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
