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
    assert b["STAGE14_T65"] == "COMPLETE_CAYLEY_CANONICAL_PRIME_RECOVERY_AND_SQUARE_SCALE_DIVISOR_REDUCTION"
    assert b["CAYLEY_DENOMINATOR_ELL_COFACTOR_LT_ELL_OVER_2"] is True
    assert b["CANONICAL_ELL_EQUALS_LARGEST_ODD_PRIME_FACTOR"] is True
    assert b["SHARED_U_EXACT_CROSS_RATIO_FIBER_MULTIPLICITY"] == "O(1)"
    assert b["CANONICAL_PRIME_TAGGED_QUADRATIC_NORM_FORM_PROVED"] is True
    assert b["SHARED_U_CANONICAL_PRIME_TAGGED_CAYLEY_SQUARE_SCALE_INCIDENCE_PROVED"] is False
    assert b["CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT"] == "7/8"
    assert b["TH18_NEEDED"] is False
    assert b["NEXT"] == "Stage14-t66"
    print("Stage14-t65 R2 frozen boundary OK")

if __name__ == "__main__":
    main()
