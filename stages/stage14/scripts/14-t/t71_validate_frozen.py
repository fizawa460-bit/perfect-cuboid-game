#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "stages/stage14/data/14-t71/gaussian_angular_square_split_frozen.json"


def main() -> None:
    d = json.loads(DATA.read_text())
    b = d["boundary"]
    c = d["checks"]
    assert d["stage"] == "14-t71"
    assert d["input"]["reciprocal_states"] == 560
    assert d["input"]["invisible_states"] == 419
    assert d["input"]["mutually_cayley_private_pairs"] == 5
    assert c["angular_gaussian_linearization_checks"] == 419
    assert c["gaussian_component_identity_checks"] == 419
    assert c["angular_cancellation_matrix_checks"] == 419
    assert c["signed_squareclass_split_checks"] == 419
    assert c["private_ell_signed_split_root_checks"] == 419
    assert c["same_kappa_four_cell_checks"] == 5
    assert c["J_kappa_coprime_checks"] == 5
    assert c["gaussian_component_transfer_checks"] == 13
    assert len(d["pair_profiles"]) == 5
    for p in d["pair_profiles"]:
        prod = 1
        for cell in p["cells"]:
            prod *= cell
        assert prod == p["kappa"]
        assert p["K_agree"] * p["K_switch"] == p["kappa"]
        assert p["J"] > 0
    g = d["synthetic_split_switch_guard"]
    assert g["kappa"] == 15
    assert g["K_agree"] == 1
    assert g["K_switch"] == 15
    assert g["cayley_common_support"] == 1
    assert b["STAGE14_T71"] == "COMPLETE_PHYSICAL_GAUSSIAN_ANGULAR_AND_SQUARECLASS_FOUR_CELL_TRANSFER_REDUCTION"
    assert b["MERGED_T70_IMPORTED"] is True
    assert b["MERGED_S7_31_GLOBAL_5_8_LEDGER_IMPORTED"] is True
    assert b["FIXED_U_DIRECTION_45_DEGREE_GAUSSIAN_LINEARIZATION_PROVED"] is True
    assert b["CAYLEY_SIGNED_SQUARECLASS_SPLIT_PROVED"] is True
    assert b["SAME_KAPPA_CAYLEY_SIGNED_FOUR_CELL_DECOMPOSITION_PROVED"] is True
    assert b["KAPPA_FOUR_CELL_REFINES_TO_GAUSSIAN_COMPONENT_TRANSFER"] is True
    assert b["CAYLEY_COMMON_SUPPORT_AND_KAPPA_TRANSFER_COPRIME"] is True
    assert b["CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT"] == "5/8"
    assert b["TH19_NEEDED"] is False
    assert b["T_ROUTE_BLOCKED_WAITING_FOR_TH19"] is False
    assert b["NEXT"] == "Stage14-t72"
    print("Stage14-t71 frozen boundary OK")


if __name__ == "__main__":
    main()
