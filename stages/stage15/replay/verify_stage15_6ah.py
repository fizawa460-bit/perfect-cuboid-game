#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from stage15_6ah_full_common_support import synthetic_report  # noqa: E402


def require(text: str, needle: str) -> None:
    if needle not in text:
        raise AssertionError(f"missing frozen statement: {needle}")


def main() -> None:
    report = synthetic_report()
    composite = report["composite"]
    zero = report["zero_overlap_guard"]

    assert composite["J"] == 65
    assert composite["J_plus"] == 5
    assert composite["J_minus"] == 13
    assert composite["residue_kernel_size"] == 65
    assert zero["J"] == 1
    assert zero["physical_witness"] is False
    assert zero["pair_square"]["lhs"] == zero["pair_square"]["rhs"]

    evidence = json.loads((ROOT / "evidence/stage15_6ah_full_common_support.json").read_text())
    assert evidence["full_common_support_modulus"] is True
    assert evidence["composite_support_crt_rootline"] is True
    assert evidence["pair_square_identity_independent_saving"] is False
    assert evidence["small_total_support_reconstruction"] is False
    assert evidence["nonclaims"]["global_pair_energy_saving_proved"] is False
    assert evidence["nonclaims"]["genus_one_theorem_opened"] is False

    result = (ROOT / "15-6ah/result.md").read_text()
    require(result, "STAGE15_6AH_FULL_COMMON_SUPPORT_MODULUS=true")
    require(result, "STAGE15_6AH_COMPOSITE_SUPPORT_CRT_ROOTLINE=true")
    require(result, "STAGE15_6AH_LARGE_TOTAL_SUPPORT_ENERGY_BOUND=true")
    require(result, "STAGE15_6AH_PAIR_SQUARE_IDENTITY=true")
    require(result, "STAGE15_6AH_PAIR_SQUARE_IDENTITY_INDEPENDENT_SAVING=false")
    require(result, "STAGE15_6AH_SMALL_TOTAL_SUPPORT_RECONSTRUCTION=false")
    require(result, "STAGE15_6AH_GLOBAL_PAIR_ENERGY_SAVING_PROVED=false")
    require(result, "STAGE15_6AH_EXIT=FULL_COMMON_SUPPORT_EXHAUSTED_SMALL_TOTAL_SUPPORT_ONE_POINT_GATE_READY")

    predecessor = (ROOT / "15-6ag/result.md").read_text()
    require(predecessor, "STAGE15_6AG_SMALL_OR_ZERO_OVERLAP_OPEN=true")
    require(predecessor, "STAGE15_6AG_GLOBAL_PAIR_ENERGY_SAVING_PROVED=false")

    arsenal = (ROOT.parent / ".." / "docs" / "stage14-arsenal.md").resolve().read_text()
    require(arsenal, "### AR-009")
    require(arsenal, "### AR-010")
    require(arsenal, "### AR-016")
    require(arsenal, "### AR-017")
    require(arsenal, "### AR-028")

    print("STAGE15_6AH_VERIFY=PASS")
    print("FULL_COMMON_SUPPORT_CRT_ROOTLINE=true")
    print("LARGE_TOTAL_SUPPORT_BOUND=N*B^o(1)*(1+W/L)")
    print("ZERO_SUPPORT_OPEN=true")
    print("PAIR_SQUARE_INDEPENDENT_SAVING=false")


if __name__ == "__main__":
    main()
