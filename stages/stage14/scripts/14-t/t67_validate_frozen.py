#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "stages/stage14/data/14-t67/canonical_root_modulus_frozen.json"


def main() -> None:
    d = json.loads(DATA.read_text())
    b = d["boundary"]
    assert d["input"]["reciprocal_states"] == 560
    assert d["input"]["invisible_states"] == 419
    assert d["input"]["mixed_branch_separate"] is True
    assert b["STAGE14_T67"] == "COMPLETE_CANONICAL_ROOT_MODULUS_COLLAPSE_AND_PRIVATE_PRIME_REDUCTION"
    assert b["CANONICAL_ROOT_MODULUS_DEFINED"] is True
    assert b["CANONICAL_ELL_RECOVERED_FROM_ROOT_MODULUS"] is True
    assert b["ODD_DELTA_RECOVERED_FROM_ROOT_MODULUS"] is True
    assert b["ROOT_SIDE_ALLOCATION_RECOVERED_FROM_M"] is True
    assert b["CANONICAL_ROOT_MODULUS_SUPER_SQRT_BAND_PROVED"] is True
    assert b["SAME_ROOT_MODULUS_SQUARECLASS_ENERGY_NEAR_LINEAR"] is True
    assert b["SAME_CANONICAL_ELL_SQUARECLASS_ENERGY_NEAR_LINEAR"] is True
    assert b["NESTED_CANONICAL_PRIME_INCIDENCE_NEAR_LINEAR"] is True
    assert b["PRIVATE_CANONICAL_PRIME_PAIR_REDUCTION_PROVED"] is True
    assert b["SHARED_U_PRIVATE_CANONICAL_PRIME_ROOT_MODULUS_ENERGY_PROVED"] is False
    assert b["CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT"] == "7/8"
    assert b["TH18_NEEDED"] is True
    assert b["TH18_REQUESTED_OBJECT"] == "PrivateCanonicalPrimeOppositeSignRootModulusLargeSieve"
    assert b["NEXT"] == "Stage14-t68"
    print("Stage14-t67 frozen boundary OK")


if __name__ == "__main__":
    main()
