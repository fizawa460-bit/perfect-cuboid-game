#!/usr/bin/env python3
from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
SCRIPTS = ROOT / "stages" / "stage15" / "scripts"
sys.path.insert(0, str(SCRIPTS))

from stage15_6ae_single_square_trigger import witness_report


def main() -> None:
    evidence_path = ROOT / "stages" / "stage15" / "evidence" / "stage15_6ae_single_square_trigger.json"
    evidence = json.loads(evidence_path.read_text())
    assert evidence["minimal_real_receiver"] is True
    assert evidence["one_primitive_pair_host"] is True
    assert evidence["binary_quartic_norm_projection"] is True
    assert evidence["binary_quartic_norm_projection_sufficient"] is False
    assert evidence["arsenal_direct_count_match"] is False
    assert evidence["stage14_s7_48_direct_reuse"] is False
    assert evidence["private_gaussian_modulus_recharge_forbidden"] is True
    assert evidence["low_core_global_count_proved"] is False
    assert evidence["causal_thinning_exponent_derived"] is False

    rows = witness_report()
    assert len(rows) >= 3
    for row in rows:
        assert row["transfer_lhs"] == row["transfer_rhs"]
        assert row["quartic_left_cleared"] == row["quartic_right_cleared"]

    result = (ROOT / "stages" / "stage15" / "15-6ae" / "result.md").read_text()
    locks = [
        "STAGE15_6AE_MINIMAL_REAL_RECEIVER=true",
        "STAGE15_6AE_ONE_PRIMITIVE_PAIR_HOST=true",
        "STAGE15_6AE_BINARY_QUARTIC_NORM_PROJECTION=true",
        "STAGE15_6AE_BINARY_QUARTIC_NORM_PROJECTION_SUFFICIENT=false",
        "STAGE15_6AE_ARSENAL_DIRECT_COUNT_MATCH=false",
        "STAGE15_6AE_STAGE14_S7_48_DIRECT_REUSE=false",
        "STAGE15_6AE_PRIVATE_GAUSSIAN_MODULUS_RECHARGE_FORBIDDEN=true",
        "STAGE15_6AE_AR009_RETRIGGERED=false",
        "STAGE15_6AE_LOW_CORE_GLOBAL_COUNT_PROVED=false",
        "STAGE15_6AE_CAUSAL_THINNING_EXPONENT_DERIVED=false",
        "STAGE15_6AE_EXIT=ONE_PAIR_ANISOTROPIC_GAUSSIAN_SQUARE_RECEIVER_READY",
    ]
    for lock in locks:
        assert lock in result, lock

    print("STAGE15_6AE_REPLAY=PASS")


if __name__ == "__main__":
    main()
