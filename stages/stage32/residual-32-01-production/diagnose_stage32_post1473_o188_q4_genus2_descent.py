#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

CUSP_BUDGET_EXPECTED = "318ac76ca5baf9e5f7f7a2300628b432f3b5fbb718f2bd21bc7a4f13b9cf3328"
V4_QUOTIENT_EXPECTED = "2869208e7509d7b79378264ea1982299b0f1745b1a54c5856cfbba0754567ce5"


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_canonical(path: Path, expected: str) -> dict:
    data = json.loads(path.read_text())
    claimed = data.get("canonical_sha256_without_this_field")
    body = dict(data)
    body.pop("canonical_sha256_without_this_field", None)
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise ValueError(f"canonical source moved for {path}: claimed={claimed} actual={actual}")
    return data


def rh_target_ramification(g_source: int, degree: int, g_target: int) -> int:
    return (2 * g_source - 2) - degree * (2 * g_target - 2)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cusp-budget", required=True, type=Path)
    ap.add_argument("--v4-quotient", required=True, type=Path)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    budget = load_canonical(args.cusp_budget, CUSP_BUDGET_EXPECTED)
    quotient = load_canonical(args.v4_quotient, V4_QUOTIENT_EXPECTED)

    fixed = budget["fixed_target"]
    if fixed != {"row_id": "g1-d186", "d": 186, "e": 266, "z": [-15, 62, -44, 26, 32]}:
        raise ValueError("fixed V6 target moved")
    sym = budget["o188_consequences"]["qprime_4_symmetric_profile"]
    if sym["projection_degrees"] != [93, 93] or sym["ramification_totals"] != [8, 8]:
        raise ValueError("q'=4 symmetric projection profile moved")

    qgeo = quotient["quotient_geometry"]
    if not qgeo["X8_to_C0_etale"] or qgeo["X8_to_C0_degree"] != 4 or qgeo["genus_C0"] != 2:
        raise ValueError("V4 quotient geometry moved")
    if qgeo["C0_to_X4_degree"] != 2 or qgeo["genus_X4"] != 0:
        raise ValueError("hyperelliptic quotient geometry moved")
    if qgeo["C0_to_X4_total_fixed_points"] != 6 or not qgeo["six_quotient_cusps_are_Weierstrass_points"]:
        raise ValueError("six-cusp Weierstrass geometry moved")

    O = 188
    qprime = 4
    genus_N = 1
    # Beauville double cover Y->N has O simple branch points.
    genus_Y = 1 + O // 2
    if 2 * genus_Y - 2 != 2 * (2 * genus_N - 2) + O or genus_Y != 95:
        raise ValueError("Beauville genus arithmetic regression")

    degree_D_to_X8 = 93
    ramification_D_to_X8 = 8
    # D->Y and X8->C0 are both etale V4 torsors of degree four.  An equivariant
    # projection D->X8 descends to f:Y->C0; the square is a morphism of V4
    # torsors and hence Cartesian.  Degree is unchanged and ramification pulls
    # back fourfold.
    degree_Y_to_C0 = degree_D_to_X8
    ramification_Y_to_C0 = ramification_D_to_X8 // qprime
    if ramification_D_to_X8 % qprime:
        raise ValueError("D projection ramification did not descend integrally")
    if degree_Y_to_C0 != 93 or ramification_Y_to_C0 != 2:
        raise ValueError("genus-two descent arithmetic regression")
    if rh_target_ramification(genus_Y, degree_Y_to_C0, 2) != ramification_Y_to_C0:
        raise ValueError("genus-two descended Riemann--Hurwitz mismatch")

    B = {
        "contact_histogram": {"m1": 187, "m2": 38, "m3": 1},
        "unique_defect_contact_m": 3,
        "Y_ramification_points_over_defect_N_branch": 1,
        "f_local_degrees_at_support": [3],
        "f_ramification_divisor_shape": "2*P",
        "f_total_ramification": 2,
        "f_branch_values": "one of the six quotient cusps / Weierstrass points for each projection",
    }
    C = {
        "contact_histogram": {"m1": 188, "m2": 37, "m4": 1},
        "unique_defect_contact_m": 4,
        "Y_ramification_points_over_defect_N_branch": 2,
        "f_local_degrees_at_support": [2, 2],
        "f_ramification_divisor_shape": "P+P'",
        "f_total_ramification": 2,
        "f_branch_values": "the two support points map to one quotient cusp / Weierstrass point for each projection",
    }

    # Compose with the hyperelliptic degree-two map h:C0->X(4)=P1.
    composite_degree = 2 * degree_Y_to_C0
    composite_R = rh_target_ramification(genus_Y, composite_degree, 0)
    if composite_degree != 186 or composite_R != 560:
        raise ValueError("degree-186 hyperelliptic composite arithmetic regression")
    # Pullback of the six simple branch points of h contributes 6*93=558;
    # the residual two is precisely ramification of f.
    if 6 * 93 + ramification_Y_to_C0 != composite_R:
        raise ValueError("six-cusp composite ramification budget mismatch")

    B_special_cycle_lengths = sorted([6] + [2] * 90)
    C_special_cycle_lengths = sorted([4, 4] + [2] * 89)
    ordinary_cycle_lengths = [2] * 93
    if sum(B_special_cycle_lengths) != 186 or sum(C_special_cycle_lengths) != 186 or sum(ordinary_cycle_lengths) != 186:
        raise ValueError("composite local cycle partition regression")

    result = {
        "schema": "STAGE32_POST1473_O188_Q4_GENUS2_DESCENT_REPLAY_V1",
        "stage": 32,
        "status": "PASS",
        "source_locks": {
            "audited_cusp_budget_canonical_sha256": CUSP_BUDGET_EXPECTED,
            "v4_cusp_quotient_canonical_sha256": V4_QUOTIENT_EXPECTED,
        },
        "qprime4_symmetric_descent": {
            "full_V4": True,
            "genus_N": genus_N,
            "O": O,
            "genus_Y": genus_Y,
            "D_to_Y_degree_etale": 4,
            "X8_to_C0_degree_etale": 4,
            "genus_C0": 2,
            "D_to_X8_projection_degrees": [93, 93],
            "D_to_X8_ramification_totals": [8, 8],
            "Y_to_C0_descended_degrees": [93, 93],
            "Y_to_C0_ramification_totals": [2, 2],
            "same_source_ramification_support_for_two_descended_maps_in_B_C": True,
        },
        "B": B,
        "C": C,
        "hyperelliptic_composite": {
            "target": "X(4)=P1",
            "degree_each": composite_degree,
            "total_ramification_each": composite_R,
            "branch_values": 6,
            "all_branch_values_are_images_of_the_six_Weierstrass_cusps": True,
            "ordinary_branch_value_cycle_lengths": ordinary_cycle_lengths,
            "B_special_branch_value_cycle_lengths": B_special_cycle_lengths,
            "C_special_branch_value_cycle_lengths": C_special_cycle_lengths,
            "note": "Cycle lengths describe local indices of the degree-186 composite over the special/ordinary cusp branch values; they are not a global monodromy existence certificate."
        },
        "firewall": "receiver-specific geometric reduction only; V4 quotient certificate is not yet hostile-audited, retained boundary labels are not yet identified with the six abstract cusp orbits, and B/C remain OPEN",
    }
    result["canonical_sha256_without_this_field"] = csha(result)
    text = json.dumps(result, sort_keys=True, separators=(",", ":"))
    print(text)
    if args.output:
        args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
