#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from stage15_6ap_kappa_coupling import audit_examples, exponent_ledger  # noqa: E402


def require(text: str, needle: str) -> None:
    if needle not in text:
        raise AssertionError(f"missing frozen statement: {needle}")


def main() -> None:
    rows = audit_examples()
    assert rows
    ledger = exponent_ledger()
    assert ledger["ZW_exp_before_height"] == Fraction(5, 8)
    assert ledger["B_exp_after_height"] == Fraction(5, 8)
    assert ledger["k_exp_after_height"] == Fraction(-1, 2)

    evidence = json.loads((ROOT / "evidence/stage15_6ap_kappa_coupling.json").read_text())
    assert evidence["kappa_value_count_multiplied"] is False
    assert evidence["small_kappa_fixed_k_count_proved"] is True
    assert evidence["coordinate_core_dichotomy_quantitatively_closed"] is True
    assert evidence["norm_core_global_sum_proved"] is False

    result = (ROOT / "15-6ap/result.md").read_text()
    for needle in [
        "STAGE15_6AP_KAPPA_VALUE_COUNT_MULTIPLIED=false",
        "STAGE15_6AP_SMALL_KAPPA_FIXED_K_COUNT_PROVED=true",
        "STAGE15_6AP_FIXED_K_DYADIC_BOUND=k^(1/8)*(Z*W)^(5/8)*B^epsilon",
        "STAGE15_6AP_FIXED_K_PHYSICAL_BOUND=B^(5/8+epsilon)*k^(-1/2)",
        "STAGE15_6AP_COORDINATE_CORE_DICHOTOMY_QUANTITATIVELY_CLOSED=true",
        "STAGE15_6AP_NORM_CORE_GLOBAL_SUM_PROVED=false",
        "STAGE15_6AP_EXIT=GLOBAL_NORM_CORE_AGGREGATION_AUDIT_READY",
    ]:
        require(result, needle)

    predecessor = (ROOT / "15-6ao/result.md").read_text()
    require(predecessor, "STAGE15_6AO_EXIT=TWO_SIDED_KAPPA_FIBER_COUPLING_READY")

    print("STAGE15_6AP_VERIFY=PASS")
    print("KAPPA_COUNT_MULTIPLIED=false")
    print("FIXED_K_EXPONENT=5/8")
    print("NORM_CORE_GLOBAL_SUM_PROVED=false")


if __name__ == "__main__":
    main()
