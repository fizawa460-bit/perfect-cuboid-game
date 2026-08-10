#!/usr/bin/env python3

import json
from pathlib import Path

EXPECTED = {
    "gaussian_primes": 116,
    "switched_states": 19200,
    "synthetic_fixed_u_packet_lifts": 51982,
    "selector_cases": 9163,
    "gcd_norm_checks": 9163,
    "square_quotient_checks": 9163,
    "mod_d2_lift_checks": 9163,
    "character_tensor_checks": 9163,
    "product_hyperbola_checks": 9163,
    "delta_square_hyperbola_checks": 9163,
    "quarter_selector_delta_checks": 9163,
    "delta_mod4_support_checks": 51982,
    "independent_unit_residue_checks": 17030,
    "independent_square_root_multiplicity_checks": 3672,
    "max_root_classes": 8,
    "max_selector_d": 165,
}


def main():
    stage14 = Path(__file__).resolve().parents[2]
    path = stage14 / "data" / "14-t85" / "selector_delta_rootlift_frozen.json"
    data = json.loads(path.read_text())

    assert data["stage"] == "14-t85"
    assert data["ell_limit"] == 1500
    for key, value in EXPECTED.items():
        assert data[key] == value, (key, data[key], value)

    assert data["max_selector_delta_product_ratio"] < 1.0
    assert data["max_selector_delta_square_ratio"] < 1.0
    assert data["max_selector_delta_quarter_ratio"] < 1.0

    b = data["boundary"]
    assert b["STAGE14_T85"] == "COMPLETE_SELECTOR_DELTA_COPRIMALITY_MODULUS_SQUARE_ROOT_LIFT_AND_SQUARE_QUOTIENT_REDUCTION"
    assert b["VERTICAL_COORDINATE_COPRIME_TO_BINARY_NORM"] is True
    assert b["SELECTOR_DIVISOR_COPRIME_TO_DELTA"] is True
    assert b["BINARY_NORM_SQUARE_ROOT_LIFT_MOD_D2"] is True
    assert b["ROOT_CLASS_MULTIPLICITY"] == "Bo1"
    assert b["SELECTOR_ROOT_LIFT_QUADRATIC_CHARACTER_EXPANSION_PROVED"] is True
    assert b["PRIME_COFACTOR_QUADRATIC_CHARACTER_TENSORIZATION_PROVED"] is True
    assert b["VERTICAL_DIVISOR_CONDITION_EQUIVALENT_TO_ROOT_LIFT_PLUS_SQUARE_QUOTIENT"] is True
    assert b["SELECTOR_DELTA_PRODUCT_HYPERBOLA_PROVED"] is True
    assert b["SELECTOR_DELTA_QUARTER_DICHOTOMY_PROVED"] is True
    assert b["SELECTOR_DELTA_SQUARED_HYPERBOLA_PROVED"] is True
    assert b["ROOT_LIFT_SQUARE_QUOTIENT_PHYSICAL_ENERGY_PROVED"] is False
    assert b["TH24_NEEDED"] is True
    assert b["TH24_TARGET_REOPENED"] is False
    assert b["TH25_NEEDED"] is False
    assert b["CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT"] == "1/2"
    assert b["STRICT_SUBSQRT_POWER_SAVING_PROVED"] is False
    assert b["NEXT"] == "Stage14-t86"

    print("Stage14-t85 frozen boundary validated")


if __name__ == "__main__":
    main()
