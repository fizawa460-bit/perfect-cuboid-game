#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp

from materialize_e3_v91c1x_r5b2b3a_24_side_exceptional_crossing_uniformizer_charts_v3 import (
    B2A,
    B2A_SHA,
    B2B1,
    B2B1_SHA,
    TARGET_SIDES,
    PARAMETERS,
    I,
    clean,
    csha,
    encode_element,
    encode_poly,
    load_locked,
    side_signs,
    affine_node_and_side_forms,
    rees_surface,
)
from materialize_e3_v91c1x_r5b2b2_full_16_exceptional_rees_charts import decode_element

HERE = Path(__file__).resolve().parent
S07 = HERE.parent / "33-07"
R5A = HERE / "e3-v91c1x-r5a-a2-02-component-p1-atlas-seeds.json"
B3A = HERE / "e3-v91c1x-r5b2b3a-a2-02-24-side-exceptional-crossing-uniformizer-charts.json"
SIDE_SOURCE = S07 / "materialize_mixed_order_side_ambient_function_lifts.py"
OUT = HERE / "e3-v91c1x-r5b2b3b-a2-02-four-side-away-from-exceptional-glue.json"

R5A_SHA = "76e63baad22a88f7c2b93d31930785c3b4eafe785fdc6de950756b169be7c9ce"
B3A_SHA = "2b4a9e291a9413f03fce9216ee94674d0f6802d0f61dc493784809fb75c1f693"
SIDE_SOURCE_SHA256 = "00075c19b97260cbfd51d508d5bfe649724e0333d133e0b8d71c0ec8d6cea797"
COORD_NAMES = ["a1", "a2", "a3", "b1", "b2", "b3", "c"]
AWAY_VAR_NAMES = ["a1", "a2", "a3", "b1", "b2", "b3"]


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def monic_gcd(exprs, t):
    nonzero = [sp.Poly(clean(x), t, domain=sp.QQ) for x in exprs if clean(x) != 0]
    if not nonzero:
        raise SystemExit("all Jacobian minors vanished identically")
    g = nonzero[0]
    for p in nonzero[1:]:
        g = sp.gcd(g, p)
    return clean(g.monic().as_expr())


def affine_away_chart(side: int):
    e1, e2, e3 = side_signs(side)
    a1, a2, a3, b1, b2, b3 = sp.symbols("a1 a2 a3 b1 b2 b3")
    variables = [a1, a2, a3, b1, b2, b3]
    c = clean(b3 + 1)  # D=c-b3=1
    surface = [
        clean(a1**2 + a2**2 - b3**2),
        clean(a2**2 + a3**2 - b1**2),
        clean(a1**2 + a3**2 - b2**2),
        clean(a1**2 + a2**2 + a3**2 - c**2),
    ]
    side_forms = [
        clean(a1),
        clean(a2 + e1 * b3),
        clean(a3 + e2 * b2),
        clean(b1 + e3 * c),
    ]
    opposite = [
        clean(a2 - e1 * b3),
        clean(a3 - e2 * b2),
        clean(b1 - e3 * c),
    ]
    rho = clean(opposite[0] * opposite[1] * opposite[2])

    if clean(surface[0] - (a1**2 + side_forms[1] * opposite[0])) != 0:
        raise SystemExit(f"F1 branch factorization drift on side {side}")
    if clean(surface[2] - (a1**2 + side_forms[2] * opposite[1])) != 0:
        raise SystemExit(f"F3 branch factorization drift on side {side}")
    if clean((surface[3] - surface[1]) - (a1**2 + side_forms[3] * opposite[2])) != 0:
        raise SystemExit(f"F4-F2 branch factorization drift on side {side}")

    t = sp.Symbol("t")
    param = {
        a1: sp.Integer(0),
        a2: clean(-e1 * (t**2 - 1) / 2),
        a3: clean(-e2 * t),
        b1: clean(-e3 * (t**2 + 1) / 2),
        b2: t,
        b3: clean((t**2 - 1) / 2),
    }
    if any(clean(f.subs(param)) != 0 for f in surface + side_forms):
        raise SystemExit(f"away side parametrization misses equations on side {side}")
    crossing_poly = clean(t * (t**4 - 1))
    expected_rho = clean(-2 * e1 * e2 * e3 * crossing_poly)
    if clean(rho.subs(param) - expected_rho) != 0:
        raise SystemExit(f"away localizer/crossing polynomial mismatch on side {side}")

    J4 = sp.Matrix([[sp.diff(f, v) for v in variables] for f in surface])
    surface_minor_values = [
        clean(J4[:, list(cols)].det().subs(param))
        for cols in itertools.combinations(range(len(variables)), 4)
    ]
    surface_gcd = monic_gcd(surface_minor_values, t)
    if clean(surface_gcd - crossing_poly) != 0:
        raise SystemExit(f"surface smoothness degeneracy moved on side {side}: {surface_gcd}")

    J5 = sp.Matrix([[sp.diff(f, v) for v in variables] for f in surface + [a1]])
    uniformizer_minor_values = [
        clean(J5[:, list(cols)].det().subs(param))
        for cols in itertools.combinations(range(len(variables)), 5)
    ]
    uniformizer_gcd = monic_gcd(uniformizer_minor_values, t)
    if clean(uniformizer_gcd - crossing_poly) != 0:
        raise SystemExit(f"Cartier-uniformizer degeneracy moved on side {side}: {uniformizer_gcd}")

    return {
        "side": side,
        "signs": (e1, e2, e3),
        "variables": variables,
        "c": c,
        "surface": surface,
        "side_forms": side_forms,
        "opposite": opposite,
        "rho": rho,
        "t": t,
        "param": param,
        "crossing_poly": crossing_poly,
        "surface_gcd": surface_gcd,
        "uniformizer_gcd": uniformizer_gcd,
    }


def crossing_affine_vector(local_row, sub):
    point = sp.Matrix([decode_element(x) for x in local_row["node_point_ambient_P6_L_basis"]])
    pivot = int(local_row["affine_patch_pivot_coordinate_0based"])
    if clean(point[pivot]) == 0:
        raise SystemExit("crossing affine pivot vanished")
    q = [clean(x / point[pivot]) for x in point]
    nonpivot = [j for j in range(7) if j != pivot]
    d = sp.symbols("d0:6")
    affine = list(q)
    affine[pivot] = sp.Integer(1)
    for k, j in enumerate(nonpivot):
        affine[j] = clean(q[j] + d[k])
    return point, pivot, nonpivot, d, q, [clean(x.subs(sub)) for x in affine]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    r5a = load_locked(R5A, R5A_SHA)
    b2a = load_locked(B2A, B2A_SHA)
    b2b1 = load_locked(B2B1, B2B1_SHA)
    b3a = load_locked(B3A, B3A_SHA)
    actual_side_source_sha = file_sha256(SIDE_SOURCE)
    if actual_side_source_sha != SIDE_SOURCE_SHA256:
        raise SystemExit(f"side ambient lift source moved: {actual_side_source_sha}")
    if r5a["exact_constructive_signal"]["side_chart_parameter"] != "t=N/D=b2/(c-b3)":
        raise SystemExit("R5A target side inverse moved")
    if b2a["target_side_components"] != [f"SIDE_{x:03d}" for x in TARGET_SIDES]:
        raise SystemExit("B2A target sides moved")
    if b3a["schema"] != "stage33.e3.v91c1x_r5b2b3a.a2_02_24_side_exceptional_crossing_uniformizer_charts.v3":
        raise SystemExit("B3A schema moved")
    if b3a["side_exceptional_crossing_count"] != 24:
        raise SystemExit("B3A crossing count moved")

    local_by_eid = {r["exceptional_id"]: r for r in b2b1["local_germ_rows"]}
    b3a_side_rows = {int(r["side_index_1based"]): r for r in b3a["crossing_neighborhood_rows"]}

    away_rows = []
    overlap_rows = []
    selected_zero_count = 0
    roundtrip_count = 0
    uniformizer_transition_count = 0

    for side in TARGET_SIDES:
        aw = affine_away_chart(side)
        e1, e2, e3 = aw["signs"]
        variables = aw["variables"]
        t = aw["t"]
        param_row = [clean(aw["param"][v]) for v in variables]
        away_rows.append({
            "component_id": f"SIDE_{side:03d}",
            "side_index_1based": side,
            "family": "A1",
            "frozen_signs": {"e1": e1, "e2": e2, "e3": e3},
            "projective_patch": {
                "condition": "D=c-b3 != 0",
                "normalization": "D=c-b3=1",
                "affine_coordinate_order": AWAY_VAR_NAMES,
                "eliminated_coordinate": "c=b3+1",
            },
            "surface_equations": [encode_poly(f, variables) for f in aw["surface"]],
            "side_ideal_generators": [encode_poly(f, variables) for f in aw["side_forms"]],
            "literal_side_uniformizer": "a1",
            "opposite_branch_unit_factors": [encode_poly(f, variables) for f in aw["opposite"]],
            "away_localizer_rho": encode_poly(aw["rho"], variables),
            "principalization_identities": [
                "F1=a1^2+(a2+e1*b3)*(a2-e1*b3)",
                "F3=a1^2+(a3+e2*b2)*(a3-e2*b2)",
                "F4-F2=a1^2+(b1+e3*c)*(b1-e3*c)",
            ],
            "localized_principalization_consequence": "on D(rho), the full selected-side ideal on the surface equals the principal Cartier ideal (a1)",
            "side_parameter": {
                "parameter": "t=b2=N/D=u/v",
                "parameter_variable": "t",
                "affine_embedding_in_coordinate_order": [encode_poly(x, [t]) for x in param_row],
                "finite_crossing_polynomial": encode_poly(aw["crossing_poly"], [t]),
                "rho_restriction": encode_poly(clean(aw["rho"].subs(aw["param"])), [t]),
                "finite_crossing_parameters": ["0", "1", "-1", "i", "-i"],
                "infinity_crossing_removed_by_D_patch": True,
            },
            "jacobian_coverage": {
                "surface_rank4_maximal_minor_gcd_on_side": encode_poly(aw["surface_gcd"], [t]),
                "surface_plus_a1_rank5_maximal_minor_gcd_on_side": encode_poly(aw["uniformizer_gcd"], [t]),
                "both_degeneracy_sets_equal_the_five_finite_crossings": True,
                "surface_smooth_on_D_times_rho_nonzero_side_locus": True,
                "a1_is_regular_parameter_on_D_times_rho_nonzero_side_locus": True,
            },
            "coverage_consequence": "this single affine principal neighborhood covers SIDE minus its six exceptional crossing points",
        })

        side_row = b3a_side_rows[side]
        if side_row["crossing_neighborhood_count"] != 6:
            raise SystemExit(f"B3A side crossing count moved for {side}")
        if [r["side_parameter"] for r in side_row["crossing_neighborhoods"]] != PARAMETERS:
            raise SystemExit(f"B3A side crossing order moved for {side}")

        for crossing in side_row["crossing_neighborhoods"]:
            eid = crossing["exceptional_id"]
            local_row = local_by_eid[eid]
            chart_p = int(crossing["canonical_rees_chart_pivot_displacement_index_0based"])
            d2, e, u, nonp, sub, pull_surface, strict_surface = rees_surface(local_row, chart_p)
            _point2, _pivot2, _nonpivot2, d_check, side_forms = affine_node_and_side_forms(local_row, side)
            if list(d2) != list(d_check):
                raise SystemExit("local displacement convention moved")
            pull_side = [clean(f.subs(sub)) for f in side_forms]
            strict_side = [clean(f / e) for f in pull_side]
            if any(clean(f - e * sf) != 0 for f, sf in zip(pull_side, strict_side)):
                raise SystemExit(f"side strict division drift {eid} side {side}")

            selected = int(crossing["selected_side_uniformizer_generator_index_0based"])
            if selected != 0:
                raise SystemExit(f"B3A selected non-a1 crossing uniformizer at {eid} side {side}: {selected}")
            selected_zero_count += 1
            if encode_poly(strict_side[0], [e, *u]) != crossing["literal_side_uniformizer_Qi"]:
                raise SystemExit(f"B3A literal a1/e uniformizer mismatch {eid} side {side}")

            point, pivot, nonpivot, d, q, affine_rees = crossing_affine_vector(local_row, sub)
            if nonpivot != _nonpivot2 or list(d) != list(d2):
                raise SystemExit("crossing ambient reconstruction convention moved")
            D_cross = clean(affine_rees[6] - affine_rees[5])
            o1_cross = clean(affine_rees[1] - e1 * affine_rees[5])
            o2_cross = clean(affine_rees[2] - e2 * affine_rees[4])
            o3_cross = clean(affine_rees[3] - e3 * affine_rees[6])
            rho_cross = clean(o1_cross * o2_cross * o3_cross)
            if clean(affine_rees[0] - e * strict_side[0]) != 0:
                raise SystemExit(f"a1 blowup transition failed {eid} side {side}")

            away_full = [
                aw["variables"][0], aw["variables"][1], aw["variables"][2],
                aw["variables"][3], aw["variables"][4], aw["variables"][5], aw["c"],
            ]
            pivot_value = away_full[pivot]
            delta_num = {}
            for k, j in enumerate(nonpivot):
                delta_num[k] = clean(away_full[j] - q[j] * pivot_value)
            e_num = delta_num[chart_p]

            # Verify the rational inverse after substituting crossing -> away, using a common D_cross denominator.
            cross_to_away = {aw["variables"][k]: clean(affine_rees[k] / D_cross) for k in range(6)}
            if clean((aw["c"].subs(cross_to_away)) - affine_rees[6] / D_cross) != 0:
                raise SystemExit(f"away c reconstruction failed {eid} side {side}")
            pivot_sub = clean(pivot_value.subs(cross_to_away))
            e_num_sub = clean(e_num.subs(cross_to_away))
            if clean(e_num_sub / pivot_sub - e) != 0:
                raise SystemExit(f"away-to-Rees inverse e roundtrip failed {eid} side {side}")
            for kk, j in enumerate(nonp):
                num_sub = clean(delta_num[j if False else nonpivot.index(j)].subs(cross_to_away))
                if clean(num_sub / e_num_sub - u[kk]) != 0:
                    raise SystemExit(f"away-to-Rees inverse u roundtrip failed {eid} side {side} u{kk}")
            roundtrip_count += 1

            away_a1_from_cross = clean(affine_rees[0] / D_cross)
            if clean(away_a1_from_cross - (e / D_cross) * strict_side[0]) != 0:
                raise SystemExit(f"side uniformizer unit transition failed {eid} side {side}")
            uniformizer_transition_count += 1

            overlap_rows.append({
                "side_component_id": f"SIDE_{side:03d}",
                "exceptional_id": eid,
                "side_parameter": crossing["side_parameter"],
                "crossing_open_source": crossing["cross_overlap_map"]["source"],
                "canonical_rees_chart_id": crossing["canonical_rees_chart_id"],
                "crossing_source_condition": crossing["distinguished_open"]["condition"],
                "overlap_subopen_condition": "lambda != 0 AND e != 0 AND D_cross != 0 AND rho_cross != 0",
                "crossing_variables": ["e", "u0", "u1", "u2", "u3", "u4"],
                "D_cross_Qi": encode_poly(D_cross, [e, *u]),
                "rho_cross_Qi": encode_poly(rho_cross, [e, *u]),
                "cross_to_away_map": {
                    "away_coordinate_order": AWAY_VAR_NAMES,
                    "common_denominator_Qi": encode_poly(D_cross, [e, *u]),
                    "numerators_Qi": [encode_poly(affine_rees[k], [e, *u]) for k in range(6)],
                    "c_is_reconstructed_as_b3_plus_1": True,
                },
                "away_to_cross_inverse_template": {
                    "node_affine_pivot_coordinate_0based": pivot,
                    "pivot_value_in_away_chart": encode_poly(pivot_value, variables),
                    "rees_e_numerator": encode_poly(e_num, variables),
                    "rees_e_denominator": encode_poly(pivot_value, variables),
                    "rees_u_numerators_in_u_order": [
                        encode_poly(delta_num[nonpivot.index(j)], variables) for j in nonp
                    ],
                    "rees_u_common_denominator": encode_poly(e_num, variables),
                },
                "side_uniformizer_transition": {
                    "away_uniformizer": "a1/D",
                    "crossing_uniformizer": "a1_aff/e",
                    "unit_multiplier_cross_to_away": "e/D_cross",
                    "exact_identity": "(a1_aff/D_cross)=(e/D_cross)*(a1_aff/e)",
                },
                "exact_checks": {
                    "b3a_selected_uniformizer_is_strict_a1": True,
                    "crossing_to_away_and_away_to_cross_maps_roundtrip_exactly": True,
                    "away_c_equals_b3_plus_1": True,
                    "side_uniformizers_differ_by_the_explicit_unit_e_over_D_cross": True,
                    "overlap_is_a_subopen_of_the_b3a_lambda_crossing_open": True,
                },
            })

    if len(away_rows) != 4 or len(overlap_rows) != 24:
        raise SystemExit("R5B2B3B row counts moved")
    if selected_zero_count != 24 or roundtrip_count != 24 or uniformizer_transition_count != 24:
        raise SystemExit("R5B2B3B exact overlap check counts moved")

    cert = {
        "schema": "stage33.e3.v91c1x_r5b2b3b.a2_02_four_side_away_from_exceptional_glue.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B2B3B_A2_02_FOUR_SIDE_AWAY_FROM_EXCEPTIONAL_GLUE",
        "role": "EXACT_NONCREDIT_R5B2B3B_SOURCE_BOUND_FOUR_TARGET_SIDE_STRICT_TRANSFORM_COVER_AND_CROSSING_GLUE",
        "entry": {
            "pr": 1684,
            "authority": "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT",
            "stage33_progress": "6/11",
            "r5a_canonical_sha256": R5A_SHA,
            "r5b2a_canonical_sha256": B2A_SHA,
            "r5b2b1_canonical_sha256": B2B1_SHA,
            "r5b2b3a_canonical_sha256": B3A_SHA,
        },
        "source_locks": {
            "r5a_path": str(R5A.relative_to(HERE.parent.parent.parent)),
            "r5a_sha256": R5A_SHA,
            "r5b2a_path": str(B2A.relative_to(HERE.parent.parent.parent)),
            "r5b2a_sha256": B2A_SHA,
            "r5b2b1_path": str(B2B1.relative_to(HERE.parent.parent.parent)),
            "r5b2b1_sha256": B2B1_SHA,
            "r5b2b3a_path": str(B3A.relative_to(HERE.parent.parent.parent)),
            "r5b2b3a_sha256": B3A_SHA,
            "side_ambient_lift_source_path": "stages/stage33/33-07/materialize_mixed_order_side_ambient_function_lifts.py",
            "side_ambient_lift_source_sha256": SIDE_SOURCE_SHA256,
            "side_ambient_lift_source_actual_sha256": actual_side_source_sha,
            "surface_model": "a1^2+a2^2=b3^2; a2^2+a3^2=b1^2; a1^2+a3^2=b2^2; a1^2+a2^2+a3^2=c^2",
        },
        "target_side_components": [f"SIDE_{x:03d}" for x in TARGET_SIDES],
        "away_side_chart_count": 4,
        "crossing_glue_overlap_count": 24,
        "away_side_charts": away_rows,
        "crossing_glue_overlaps": overlap_rows,
        "exact_check_counts": {
            "away_chart_principalization_count": 4,
            "away_chart_smoothness_and_cartier_rank_coverage_count": 4,
            "crossing_selected_strict_a1_uniformizer_count": selected_zero_count,
            "crossing_away_rational_roundtrip_count": roundtrip_count,
            "explicit_side_uniformizer_unit_transition_count": uniformizer_transition_count,
        },
        "exact_consequence": {
            "four_target_side_away_from_exceptional_neighborhoods_materialized": True,
            "each_away_neighborhood_is_one_source_bound_affine_principal_chart": True,
            "each_away_chart_covers_exactly_the_side_minus_its_six_exceptional_crossings": True,
            "all_24_crossing_open_to_away_chart_overlap_maps_materialized": True,
            "all_24_overlap_maps_have_exact_rational_inverses": True,
            "all_24_overlap_uniformizer_transitions_are_explicit_units": True,
            "four_target_side_full_strict_transform_neighborhood_covers_materialized": True,
            "finite_surface_cover_materialized": False,
            "surface_all_double_overlap_transitions_materialized": False,
            "swap23_cover_action_or_common_refinement_materialized": False,
        },
        "construction_status": {
            "full_16_exceptional_rees_atlases_materialized": True,
            "four_target_side_crossing_neighborhood_atlases_materialized": True,
            "four_target_side_away_from_exceptional_neighborhoods_materialized": True,
            "four_target_side_full_strict_transform_neighborhoods_materialized": True,
            "side_to_exceptional_cross_overlap_maps_at_all_24_crossings_materialized": True,
            "finite_surface_cover_materialized": False,
            "surface_all_double_overlap_transitions_materialized": False,
            "swap23_cover_action_or_common_refinement_materialized": False,
        },
        "next_missing_object": "SOURCE_BOUND_FINITE_SURFACE_NEIGHBORHOOD_COVER_EXTENDING_THE_BOUNDARY_COMPONENT_CHARTS_OFF_THE_FOUR_TARGET_SIDES_WITH_ALL_REQUIRED_DOUBLE_OVERLAPS_THEN_SWAP23_COMMON_REFINEMENT",
        "next_exact_leaf": "V91C1X_R5B2C_EXTEND_BOUNDARY_NEIGHBORHOODS_TO_A_FINITE_SURFACE_COVER_AND_MATERIALIZE_ALL_DOUBLE_OVERLAPS",
        "credit_firewall": {
            "finite_surface_cover_credit": False,
            "h2_fixedness_credit": False,
            "mask20_credit": False,
            "source_bound_dim5_credit": False,
            "marked_brauer_image_credit": False,
            "stage33_close_credit": False,
            "stage33_release_credit": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "merge_allowed": False,
        },
    }
    cert["canonical_sha256"] = csha(cert)
    if args.write:
        OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "success": True,
        "marker": "V91C1X_R5B2B3B_FOUR_SIDE_AWAY_FROM_EXCEPTIONAL_GLUE",
        "away_side_chart_count": 4,
        "crossing_glue_overlap_count": 24,
        "crossing_selected_strict_a1_uniformizer_count": selected_zero_count,
        "crossing_away_rational_roundtrip_count": roundtrip_count,
        "explicit_side_uniformizer_unit_transition_count": uniformizer_transition_count,
        "certificate_sha256": cert["canonical_sha256"],
        "next_exact_leaf": cert["next_exact_leaf"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
