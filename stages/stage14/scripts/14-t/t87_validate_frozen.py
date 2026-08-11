#!/usr/bin/env python3

import json
from pathlib import Path

EXPECTED = {
    "group_order_checks": 16,
    "projective_classes_total": 372,
    "gaussian_unit_residue_checks": 7912,
    "ring_class_order_checks": 10,
    "reduced_form_classes_total": 74,
    "projective_incidence_checks": 422208,
    "projective_identity_triples": 11632,
    "annulus_line_checks": 2232,
    "annulus_line_points": 68336,
}


def main():
    stage14 = Path(__file__).resolve().parents[2]
    path = stage14 / "data" / "14-t87" / "projective_line_conductor_endpoint_frozen.json"
    data = json.loads(path.read_text())

    for key, value in EXPECTED.items():
        assert data[key] == value, (key, data[key], value)

    assert abs(data["max_line_bound_ratio"] - 2.2507283950710675) < 1e-15
    assert data["max_line_bound_case"] == {
        "d": 29,
        "L": 800,
        "class": [0, 1],
        "count": 128,
    }

    b = data["boundary"]
    assert b["STAGE14_T87"] == "COMPLETE_PROJECTIVE_RING_CLASS_BRIDGE_AND_FIXED_POWER_CONDUCTOR_ENDPOINT_COLLAPSE"
    assert b["PROJECTIVE_GAUSSIAN_SELECTOR_GROUP_REENTERED"] is True
    assert b["EXACT_GAMMA_A_PRIME_PROJECTIVE_INCIDENCE"] is True
    assert b["PROJECTIVE_GROUP_ORDER_SCALE"] == "d*Bo1"
    assert b["T86_FORM_DISCRIMINANT_RING_CLASS_IDENTIFIED"] is True
    assert b["RING_CLASS_NUMBER_SCALE"] == "d*Bo1"
    assert b["PROJECTIVE_CLASS_IS_INDEX_D_LATTICE"] is True
    assert b["PROJECTIVE_ANNULUS_LATTICE_BOUND"] == "L/d+sqrt(L)+1"
    assert b["FIXED_POWER_D_PROJECTIVE_LATTICE_SAVING_PROVED"] is True
    assert b["HARD_SELECTOR_CONDUCTOR_ENDPOINT"] == "d=Bo1"
    assert b["HARD_PROJECTIVE_GROUP_SIZE"] == "Bo1"
    assert b["HARD_RING_CLASS_NUMBER"] == "Bo1"
    assert b["TH25_NEEDED"] is True
    assert b["TH25_TARGET_REOPENED"] is False
    assert b["TH26_NEEDED"] is False
    assert b["CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT"] == "1/2"
    assert b["STRICT_SUBSQRT_POWER_SAVING_PROVED"] is False
    assert b["NEXT"] == "Stage14-t88"

    print("Stage14-t87 frozen boundary validated")


if __name__ == "__main__":
    main()
