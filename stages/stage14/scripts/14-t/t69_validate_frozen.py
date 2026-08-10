#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "stages/stage14/data/14-t69/noncanonical_cayley_support_frozen.json"


def main() -> None:
    d = json.loads(DATA.read_text())
    b = d["boundary"]
    s = d["frozen_pair_statistics"]
    assert d["input"]["reciprocal_states"] == 560
    assert d["input"]["invisible_states"] == 419
    assert d["input"]["mutually_cayley_private_pairs"] == 5
    assert d["checks"]["angular_factorization_checks"] == 419
    assert d["checks"]["full_cayley_largest_prime_checks"] == 419
    assert s["pairs_J_equals_radial_base"] == 1
    assert s["pairs_J_strictly_exceeds_radial_base"] == 4
    assert s["pairs_J_equals_one"] == 0
    assert s["max_frozen_J"] == 75
    assert s["max_frozen_extra_common_support"] == 65
    assert s["J_histogram"] == {"5": 1, "17": 1, "65": 2, "75": 1}
    assert d["synthetic_disjoint_support_guard"]["common_noncanonical_odd_support"] == 1
    assert d["synthetic_disjoint_support_guard"]["full_physical_reconstruction_claimed"] is False
    assert b["STAGE14_T69"] == "COMPLETE_NONCANONICAL_CAYLEY_FACTOR_AND_COMMON_SUPPORT_REDUCTION"
    assert b["NONCANONICAL_CAYLEY_COFACTORS_IDENTIFIED_WITH_ANGULAR_DEFICITS"] is True
    assert b["REDUCED_CAYLEY_SUPPORT_COPRIME_TO_KAPPA"] is True
    assert b["CANONICAL_ELL_UNIQUE_LARGEST_ODD_PRIME_OF_FULL_CAYLEY_PAIR"] is True
    assert b["ALL_NONCANONICAL_ODD_CAYLEY_PRIMES_LT_ELL"] is True
    assert b["NONCANONICAL_COMMON_SUPPORT_RESULTANT_DICTIONARY_PROVED"] is True
    assert b["SAME_SQUARECLASS_FORCES_NONTRIVIAL_NONCANONICAL_OVERLAP"] is False
    assert b["SHARED_U_PRIVATE_LARGEST_PRIME_CAYLEY_COMMON_MODULUS_ENERGY_PROVED"] is False
    assert b["CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT"] == "3/4"
    assert b["T69_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING"] is False
    assert b["TH18_CONSUMED"] is True
    assert b["TH19_NEEDED"] is False
    assert b["NEXT"] == "Stage14-t70"
    print("Stage14-t69 frozen boundary OK")


if __name__ == "__main__":
    main()
