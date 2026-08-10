#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "stages/stage14/data/14-t68/private_canonical_residue_frozen.json"


def main() -> None:
    d = json.loads(DATA.read_text())
    b = d["boundary"]
    assert d["input"]["reciprocal_states"] == 560
    assert d["input"]["invisible_states"] == 419
    assert d["input"]["mixed_branch_separate"] is True
    assert b["STAGE14_T68"] == "COMPLETE_CANONICAL_CROSS_RESULTANT_DICTIONARY_AND_PRIVATE_PRIME_TRANSFER_NOGO"
    assert b["MERGED_S7_29_GLOBAL_3_4_LEDGER_IMPORTED"] is True
    assert b["CANONICAL_CROSS_RESULTANT_DICTIONARY_PROVED"] is True
    assert b["PRIVATE_ELL_FORCES_CROSS_DETERMINANT"] is False
    assert b["CROSS_FACTOR_CONTAMINATION_NEAR_LINEAR"] is True
    assert b["MUTUALLY_CAYLEY_PRIVATE_PAIR_DEFINED"] is True
    assert b["CANONICAL_PRIME_DETERMINANT_SPACING_AVAILABLE"] is False
    assert b["CANONICAL_PRIME_LOCAL_SQUARE_TEST_IDENTICALLY_COHERENT_ON_KAPPA_FIBER"] is True
    assert b["PRIVATE_CANONICAL_ROOT_ORIENTATION_TRANSFERS_TO_OTHER_STATE"] is False
    assert b["SHARED_U_MUTUALLY_CAYLEY_PRIVATE_SQUARE_SCALE_ENERGY_PROVED"] is False
    assert b["CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT"] == "3/4"
    assert b["NEW_WHOLE_FAMILY_POWER_SAVING_PROVED"] is True
    assert b["T68_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING"] is False
    assert b["TH18_PREVIOUS_REQUEST_SUPERSEDED"] is True
    assert b["TH18_NEEDED"] is False
    assert b["NEXT"] == "Stage14-t69"
    print("Stage14-t68 frozen boundary OK")


if __name__ == "__main__":
    main()
