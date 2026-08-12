#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from stage15_6aq_norm_core_gate import audit_growth  # noqa: E402


def require(text: str, needle: str) -> None:
    if needle not in text:
        raise AssertionError(f"missing frozen statement: {needle}")


def main() -> None:
    rows = audit_growth()
    assert len(rows) == 3
    assert rows[-1]["allowed_count"] > rows[0]["allowed_count"]
    assert rows[-1]["allowed_weighted_sum"] > rows[0]["allowed_weighted_sum"]

    evidence = json.loads((ROOT / "evidence/stage15_6aq_norm_core_gate.json").read_text())
    assert evidence["coordinate_core_obstruction_closed_at_fixed_k"] is True
    assert evidence["norm_core_value_count_subpolynomial"] is False
    assert evidence["naive_sum_k_minus_half_legal"] is False
    assert evidence["ar009_norm_core_recharge_allowed"] is False
    assert evidence["j1728_twist_height_route"]["identified"] is True
    assert evidence["j1728_twist_height_route"]["adapter_proved"] is False
    assert evidence["causal_half_power_rederived"] is False

    result = (ROOT / "15-6aq/result.md").read_text()
    for needle in [
        "STAGE15_6AQ_COORDINATE_CORE_OBSTRUCTION_CLOSED_AT_FIXED_k=true",
        "STAGE15_6AQ_NORM_CORE_VALUE_COUNT_SUBPOLYNOMIAL=false",
        "STAGE15_6AQ_NAIVE_SUM_k_MINUS_HALF_LEGAL_THINNING_PROOF=false",
        "STAGE15_6AQ_AR009_NORM_CORE_RECHARGE_ALLOWED=false",
        "STAGE15_6AQ_STAGE14_SH48_DIRECT_REUSE=false",
        "STAGE15_6AQ_J1728_TWIST_HEIGHT_ROUTE_IDENTIFIED=true",
        "STAGE15_6AQ_J1728_TWIST_HEIGHT_ADAPTER_PROVED=false",
        "STAGE15_6AQ_CAUSAL_HALF_POWER_REDERIVED=false",
        "STAGE15_6AQ_EXIT=J1728_TWIST_HEIGHT_OR_NORM_CORE_CORRELATION_THEOREM_GATE",
    ]:
        require(result, needle)

    predecessor = (ROOT / "15-6ap/result.md").read_text()
    require(predecessor, "STAGE15_6AP_EXIT=GLOBAL_NORM_CORE_AGGREGATION_AUDIT_READY")

    sh48 = (ROOT.parent / "stage14/14-sH48/result.md").read_text()
    require(sh48, "OFF_THE_SHELF_THEOREM_APPLICABLE=false")
    require(sh48, "FIXED_POWER_SAVING_PROVED=false")

    print("STAGE15_6AQ_VERIFY=PASS")
    print("COORDINATE_CORE_FIXED_K_CLOSED=true")
    print("NORM_CORE_GLOBAL_SUM_PROVED=false")
    print("CAUSAL_HALF_POWER_REDERIVED=false")


if __name__ == "__main__":
    main()
