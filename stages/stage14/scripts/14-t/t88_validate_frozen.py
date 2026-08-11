#!/usr/bin/env python3

import json
from pathlib import Path

EXPECTED = {
    "q_values_checked": 307,
    "primitive_q_rep_checks": 3224,
    "canonical_lpf_factor_recoveries": 3224,
    "max_primitive_q_reps": 16,
    "max_r2_over_4tau": 1.0,
    "product_reconstruction_states": 1473,
    "canonical_q_recovery_checks": 1473,
    "unique_norm_ell_divisor_checks": 1473,
    "endpoint_projective_checks": 2781,
    "max_endpoint_d": 21,
    "fixed_q_fiber_packets": 19191,
    "fixed_q_fiber_labels": 243504,
    "max_fixed_q_fiber": 128,
    "max_fixed_q_fiber_over_16tautau": 1.0,
}


def main():
    stage14 = Path(__file__).resolve().parents[2]
    path = stage14 / "data" / "14-t88" / "canonical_q_norm_fiber_frozen.json"
    data = json.loads(path.read_text())

    for key, value in EXPECTED.items():
        assert data[key] == value, (key, data[key], value)

    assert data["max_fixed_q_fiber_case"] == {
        "Q": 685, "k0": 13, "d": 1, "count": 128
    }

    b = data["boundary"]
    assert b["STAGE14_T88"] == "COMPLETE_ENDPOINT_SMALL_PROJECTIVE_SELECTOR_TO_CANONICAL_Q_NORM_FINITE_FIBER_REDUCTION"
    assert b["MERGED_T87_IMPORTED"] is True
    assert b["MERGED_TH25_CONSUMED"] is True
    assert b["CANONICAL_T84_PRIME_IDENTIFIED_WITH_T86_PI_PRIME"] is True
    assert b["ORIENTED_COVER_EQUALS_GAMMA_TIMES_FIXED_K_FACTOR"] is True
    assert b["CANONICAL_Q_VARIABLE_PROVED"] is True
    assert b["Q_DEFINITION"] == "Q=ell*delta0=N(gamma*pi)"
    assert b["ELL_RECOVERED_AS_Q_LPF"] is True
    assert b["ELL_EXPONENT_IN_Q"] == 1
    assert b["DELTA0_RECOVERED_FROM_Q"] is True
    assert b["FIXED_Q_GAUSSIAN_REPRESENTATION_COST"] == "Bo1"
    assert b["FIXED_Q_PHYSICAL_FIBER_MULTIPLICITY"] == "Bo1"
    assert b["RING_CLASS_FAMILY_COST_SURVIVES"] is False
    assert b["ONE_DIMENSIONAL_Q_ENERGY_BOUND"] == "X*Bo1"
    assert b["CANONICAL_LPF_CORE_ALONE_FIXED_POWER_SPARSE"] is False
    assert b["TH25_TARGET_REOPENED"] is False
    assert b["TH26_NEEDED"] is False
    assert b["CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT"] == "1/2"
    assert b["STRICT_SUBSQRT_POWER_SAVING_PROVED"] is False
    assert b["NEXT"] == "Stage14-t89"

    print("Stage14-t88 frozen boundary validated")


if __name__ == "__main__":
    main()
