#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "stages/stage14/data/14-t64/square_lifted_cross_ratio_frozen.json"


def main() -> None:
    d = json.loads(DATA.read_text())
    b = d["boundary"]
    assert d["input"]["reciprocal_states"] == 560
    assert d["input"]["mixed_branch_separate"] is True
    assert b["STAGE14_T64"] == "COMPLETE_SQUARE_LIFTED_CROSS_RATIO_QUOTIENT_AND_JACOBI_FIBRATION"
    assert b["EXACT_RATIONAL_CROSS_RATIO_COORDINATE_PROVED"] is True
    assert b["FIXED_SQUARECLASS_EVEN_QUOTIENT_RATIONAL"] is True
    assert b["PHYSICAL_SQUARE_LIFT_JACOBI_QUARTIC_PROVED"] is True
    assert b["TRANSVERSE_EQUAL_SQUARECLASS_EQUALS_CROSS_RATIO_SQUARE_QUOTIENT"] is True
    assert b["SHARED_U_TRANSVERSE_JACOBI_SQUARE_LIFT_INCIDENCE_PROVED"] is False
    assert b["CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT"] == "7/8"
    assert b["TH18_NEEDED"] is False
    assert b["NEXT"] == "Stage14-t65"
    print("Stage14-t64 frozen boundary OK")


if __name__ == "__main__":
    main()
