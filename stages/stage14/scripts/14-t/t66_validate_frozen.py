#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "stages/stage14/data/14-t66/primewise_cayley_crt_frozen.json"


def main() -> None:
    d = json.loads(DATA.read_text())
    b = d["boundary"]
    assert d["input"]["reciprocal_states"] == 560
    assert d["input"]["invisible_states"] == 419
    assert d["input"]["mixed_branch_separate"] is True
    assert b["STAGE14_T66"] == "COMPLETE_PRIMEWISE_CAYLEY_ALLOCATION_AND_OPPOSITE_SIGN_ROOT_LINE_REDUCTION"
    assert b["CAYLEY_GCD_ODD_PART_EQUALS_GCD_KAPPA_V"] is True
    assert b["ODD_PHYSICAL_RADIAL_MODULUS_COPRIME_TO_KAPPA"] is True
    assert b["OPPOSITE_SIGN_QUADRATIC_ROOT_CONGRUENCES_PROVED"] is True
    assert b["CRT_ROOT_LINE_MULTIPLICITY"] == "Bo1"
    assert b["PLUS_AND_MINUS_HAVE_SAME_LEGENDRE_SPLITTING_CONDITION"] is True
    assert b["CANONICAL_LARGEST_PRIME_TAG_RETAINED"] is True
    assert b["SHARED_U_CANONICAL_PRIME_TAGGED_OPPOSITE_SIGN_QUADRATIC_ROOT_LINE_ENERGY_PROVED"] is False
    assert b["CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT"] == "7/8"
    assert b["TH18_NEEDED"] is True
    assert b["TH18_REQUESTED_OBJECT"] == "CanonicalPrimeTaggedOppositeSignQuadraticRootLargeSieve"
    assert b["NEXT"] == "Stage14-t67"
    print("Stage14-t66 frozen boundary OK")


if __name__ == "__main__":
    main()
