#!/usr/bin/env python3

import json
from pathlib import Path

EXPECTED = {
    "ell_values": 51,
    "delta0_values": 22,
    "packet_q_checks": 4753,
    "label_checks": 337696,
    "linear_determinant_checks": 104,
    "weighted_q_packets": 4551,
    "max_weight": 192,
    "max_weight_over_32_tau_tau": 1.0,
    "max_abs_r": 24,
    "max_abs_t": 24,
    "max_Q": 88357,
    "max_delta0": 149,
    "max_ell": 593,
}


def main():
    root = Path(__file__).resolve().parents[4]
    path = root / "stages" / "stage14" / "data" / "14-t89" / "strong_gap_q_weight_frozen.json"
    data = json.loads(path.read_text())

    for key, value in EXPECTED.items():
        assert data[key] == value, (key, data[key], value)

    assert data["max_weight_case"] == {"h": 1, "k0": 25, "Q": 1285}

    b = data["boundary"]
    assert b["STAGE14_T89"] == "COMPLETE_STRONG_FIXED_U_Q_GAP_AND_SHORT_COVER_MASK_ABSORPTION"
    assert b["FULL_T65_FIXED_U_SEPARATION_RESTORED"] is True
    assert b["STRONG_Q_LPF_GAP"] == "ell^2>2*h*k0*Q"
    assert b["Q_BUDGET_EQUIVALENCE"] == "h*k0*Q<=2B"
    assert b["COVER_LINEAR_FORM_CHART_PROVED"] is True
    assert b["COVER_LINEAR_FORM_DETERMINANT"] == "2*k0"
    assert b["SHORT_COVER_NORM_IDENTITY"] == "r^2+t^2=2*k0*delta0"
    assert b["T74_SHORT_R_T_BOUNDS_AUTOMATIC_FROM_STRONG_Q_GAP"] is True
    assert b["T74_SHORT_COFACTOR_BOUND_AUTOMATIC"] is True
    assert b["T74_ELL_C_HYPERBOLA_AUTOMATIC"] is True
    assert b["T75_T78_ANGULAR_HYPERBOLA_AUTOMATIC"] is True
    assert b["PHYSICAL_COMPLETION_BOUNDED_Q_WEIGHT_PROVED"] is True
    assert b["PHYSICAL_Q_WEIGHT_SUP_NORM"] == "Bo1"
    assert b["ONE_DIMENSIONAL_WEIGHTED_Q_KERNEL_PROVED"] is True
    assert b["TH25_COMPLETE"] is True
    assert b["TH25_TARGET_REOPENED"] is False
    assert b["TH26_NEEDED"] is False
    assert b["CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT"] == "1/2"
    assert b["STRICT_SUBSQRT_POWER_SAVING_PROVED"] is False
    assert b["NEXT"] == "Stage14-t90"

    print("Stage14-t89 frozen boundary validated")


if __name__ == "__main__":
    main()
