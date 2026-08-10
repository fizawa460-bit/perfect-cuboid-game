#!/usr/bin/env python3

import json
from pathlib import Path

EXPECTED = {
    "gaussian_primes": 147,
    "switched_states": 32168,
    "norm_identity_checks": 32168,
    "primitive_gcd_checks": 32168,
    "lpf_checks": 32168,
    "lpf_exponent_checks": 32168,
    "super_sqrt_checks": 32168,
    "support_mod4_checks": 32168,
    "reconstruction_checks": 32168,
    "short_cofactor_checks": 32168,
    "divisor_quotient_checks": 180032,
    "quarter_dichotomy_checks": 180032,
    "fixed_norm_representation_checks": 5000,
    "max_primitive_representations": 32,
    "max_representation_norm": 1105,
}


def main():
    root = Path(__file__).resolve().parents[3]
    path = root / "data" / "14-t84" / "primitive_binary_norm_lpf_frozen.json"
    data = json.loads(path.read_text())

    for key, value in EXPECTED.items():
        assert data[key] == value, (key, data[key], value)

    assert data["max_representation_ratio"] <= 1.0
    assert data["max_short_cofactor_ratio"] < 1.0
    assert data["max_quarter_ratio"] <= 1.0

    b = data["boundary"]
    assert b["STAGE14_T84"] == "COMPLETE_PRIMITIVE_BINARY_NORM_SUPER_SQRT_LPF_AND_SHORT_COFACTOR_REDUCTION"
    assert b["PRIMITIVE_SWITCHED_BINARY_NORM_PROVED"] is True
    assert b["CANONICAL_ELL_RECOVERED_AS_BINARY_NORM_LPF"] is True
    assert b["CANONICAL_ELL_EXPONENT_ONE_IN_BINARY_NORM"] is True
    assert b["CANONICAL_PRIME_INDEPENDENT_CHOICE_ELIMINATED"] is True
    assert b["SHORT_COVER_NORM_COFACTOR_PROVED"] is True
    assert b["FIXED_ORIENTATION_PI_V_RECONSTRUCTION_UNIQUE"] is True
    assert b["BILINEAR_PI_V_MULTIPLICITY_ELIMINATED"] is True
    assert b["TH23_TARGET_REOPENED"] is False
    assert b["TH24_NEEDED"] is True
    assert b["TH24_DISPATCHED"] is False
    assert b["CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT"] == "1/2"
    assert b["STRICT_SUBSQRT_POWER_SAVING_PROVED"] is False
    assert b["NEXT"] == "Stage14-t85"

    print("Stage14-t84 frozen boundary validated")


if __name__ == "__main__":
    main()
