#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "stages/stage14/data/14-t65/cayley_divisor_lock_frozen.json"


def main() -> None:
    d = json.loads(DATA.read_text())
    b = d["boundary"]
    assert d["input"]["reciprocal_states"] == 560
    assert d["input"]["invisible_states"] == 419
    assert d["input"]["mixed_branch_separate"] is True
    assert b["STAGE14_T65"] == "COMPLETE_CAYLEY_RADIAL_DIVISOR_LOCK_AND_EXACT_S_FIBER_RIGIDITY"
    assert b["CAYLEY_RADIAL_FACTOR_IDENTITY_PROVED"] is True
    assert b["ODD_DELTA_SURVIVES_REDUCED_CAYLEY_NUMERATOR"] is True
    assert b["ODD_ELL_H_SURVIVES_REDUCED_CAYLEY_DENOMINATOR"] is True
    assert b["SHARED_U_EXACT_CROSS_RATIO_FIBER_MULTIPLICITY_PROVED"] is True
    assert b["CAYLEY_PLUS_MINUS_GCD_DIVIDES_2KAPPA"] is True
    assert b["SHARED_U_CAYLEY_SQUARE_SCALE_DIVISOR_INCIDENCE_PROVED"] is False
    assert b["CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT"] == "7/8"
    assert b["TH18_NEEDED"] is False
    assert b["NEXT"] == "Stage14-t66"
    print("Stage14-t65 frozen boundary OK")


if __name__ == "__main__":
    main()
