#!/usr/bin/env python3

import json
from pathlib import Path

EXPECTED = {
    "gaussian_primes": 74,
    "switched_states": 7272,
    "two_adic_absorption_checks": 25632,
    "delta_root_orientation_checks": 25632,
    "delta_root_multiplicity_enumerations": 24158,
    "gaussian_delta_divisor_extractions": 21952,
    "fixed_k_gaussian_peels": 21952,
    "quotient_form_cases": 76380,
    "quotient_form_identity_checks": 76380,
    "fixed_discriminant_checks": 76380,
    "primitive_form_checks": 76380,
    "primitive_transformed_coordinate_checks": 76380,
    "fixed_cofactor_prime_value_checks": 76380,
    "independent_form_regressions": 5390,
    "max_root_classes": 4,
    "max_delta0": 433,
    "max_k0": 433,
    "max_d": 617,
    "max_abs_s": 592,
    "max_form_coefficient": 115559450,
    "max_delta_gaussian_representation_count": 16,
}


def main():
    root = Path(__file__).resolve().parents[2]
    path = root / "data" / "14-t86" / "fixed_discriminant_prime_form_frozen.json"
    data = json.loads(path.read_text())

    for key, value in EXPECTED.items():
        assert data[key] == value, (key, data[key], value)

    b = data["boundary"]
    assert b["STAGE14_T86"] == "COMPLETE_COFACTOR_ROOT_LINE_TO_FIXED_DISCRIMINANT_FIXED_COFACTOR_PRIME_VALUE_FORM"
    assert b["DELTA_ROOT_OF_MINUS_ONE_PROVED"] is True
    assert b["COFACTOR_ROOT_LINE_QUOTIENT_FORM_PROVED"] is True
    assert b["SQUARE_QUOTIENT_NONLINEARITY_ELIMINATED"] is True
    assert b["FIXED_DISCRIMINANT_REDUCTION_PROVED"] is True
    assert b["FORM_DISCRIMINANT"] == "-4*d^2"
    assert b["PRIMITIVE_POSITIVE_DEFINITE_FORM_PROVED"] is True
    assert b["FIXED_COFACTOR_PRIME_VALUE_FORM_PROVED"] is True
    assert b["DELTA_GAUSSIAN_IDEAL_EXTRACTION_PROVED"] is True
    assert b["FIXED_K_GAUSSIAN_FACTOR_PEEL_PROVED"] is True
    assert b["TH24_CONSUMED"] is True
    assert b["TH24_TARGET_REOPENED"] is False
    assert b["TH25_NEEDED"] is True
    assert b["TH25_DISPATCHED"] is False
    assert b["CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT"] == "1/2"
    assert b["STRICT_SUBSQRT_POWER_SAVING_PROVED"] is False
    assert b["NEXT"] == "Stage14-t87"

    print("Stage14-t86 frozen boundary validated")


if __name__ == "__main__":
    main()
