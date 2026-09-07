#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp

from materialize_e3_v91c1x_r5b2b2_full_16_exceptional_rees_charts import (
    I,
    clean,
    csha,
    decode_element,
    encode_element,
    encode_poly,
    load_locked,
    reconstruct_local_germ,
)

HERE = Path(__file__).resolve().parent
S07 = HERE.parent / "33-07"
B2A = HERE / "e3-v91c1x-r5b2a-a2-02-target-side-incidence-closure.json"
B2B1 = HERE / "e3-v91c1x-r5b2b1-a2-02-full-closure-local-germs.json"
B2B2 = HERE / "e3-v91c1x-r5b2b2-a2-02-full-16-exceptional-rees-charts.json"
SIDE_SOURCE = S07 / "certify_boundary_side_p1_crossing_coordinates.py"
OUT = HERE / "e3-v91c1x-r5b2b3a-a2-02-24-side-exceptional-crossing-uniformizer-charts.json"

B2A_SHA = "dc3c875eaa006f89386749e332e0e4559c2af0b0a4cb0fe9aa97aecbf0944534"
B2B1_SHA = "02f0362bce42716a18ff709e350587775cd7edbdcc99d71af39b49b01c63651d"
B2B2_SHA = "305841c0d906c4d65aa08d6acac5e821991dabc364bd7f5890fa75f06dbde98e"
SIDE_SOURCE_GIT_BLOB_SHA1 = "02682d9d7648e683b9d26fca86efba02118ba8a3"
TARGET_SIDES = [2, 4, 6, 8]
PARAMETERS = ["0", "infinity", "1", "-1", "i", "-i"]


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def side_signs(side: int):
    if not 1 <= side <= 8:
        raise SystemExit(f"B2B3A only accepts A1 sides, got {side}")
    r = side - 1
    e1 = 1 if (r // 4) == 0 else -1
    e2 = 1 if ((r // 2) % 2) == 0 else -1
    e3 = 1 if (r % 2) == 0 else -1
    return e1, e2, e3


def side_param_vector(side: int, parameter: str, h: sp.Symbol):
    e1, e2, e3 = side_signs(side)
    if parameter == "infinity":
        u, v = sp.Integer(1), h
    else:
        t0 = {"0": 0, "1": 1, "-1": -1, "i": I, "-i": -I}[parameter]
        u, v = t0 + h, sp.Integer(1)
    X = clean(u * u - v * v)
    Y = clean(2 * u * v)
    Z = clean(u * u + v * v)
    return [
        sp.Integer(0),
        clean(-e1 * X),
        clean(-e2 * Y),
        clean(-e3 * Z),
        Y,
        X,
        Z,
    ]


def side_homogeneous_linear_forms(side: int, x):
    e1, e2, e3 = side_signs(side)
    a1, a2, a3, b1, b2, b3, c = x
    return [
        clean(a1),
        clean(a2 + e1 * b3),
        clean(a3 + e2 * b2),
        clean(b1 + e3 * c),
    ]


def affine_node_and_side_forms(local_row, side: int):
    point = sp.Matrix([decode_element(x) for x in local_row["node_point_ambient_P6_L_basis"]])
    pivot = int(local_row["affine_patch_pivot_coordinate_0based"])
    if clean(point[pivot]) == 0:
        raise SystemExit(f"affine pivot vanished for {local_row['exceptional_id']}")
    q = sp.Matrix([clean(x / point[pivot]) for x in point])
    nonpivot = [j for j in range(7) if j != pivot]
    d = sp.symbols("d0:6")
    affine = list(q)
    affine[pivot] = sp.Integer(1)
    for k, j in enumerate(nonpivot):
        affine[j] = clean(q[j] + d[k])
    forms = side_homogeneous_linear_forms(side, affine)
    if any(clean(f.subs({x: 0 for x in d})) != 0 for f in forms):
        raise SystemExit(f"side does not pass through node {local_row['exceptional_id']} side {side}")
    return point, pivot, nonpivot, d, [clean(f) for f in forms]


def tangent_direction(local_row, side: int, parameter: str):
    h = sp.Symbol("h_side")
    P = side_param_vector(side, parameter, h)
    pivot = int(local_row["affine_patch_pivot_coordinate_0based"])
    if clean(P[pivot].subs(h, 0)) == 0:
        raise SystemExit(f"frozen side parameter misses affine pivot {local_row['exceptional_id']} {side} {parameter}")
    q_param = [clean(x / P[pivot]) for x in P]
    point = [decode_element(x) for x in local_row["node_point_ambient_P6_L_basis"]]
    q_node = [clean(x / point[pivot]) for x in point]
    if any(clean(q_param[j].subs(h, 0) - q_node[j]) != 0 for j in range(7)):
        raise SystemExit(f"parameter/node mismatch {local_row['exceptional_id']} side {side} {parameter}")
    nonpivot = [j for j in range(7) if j != pivot]
    direction = [clean(sp.diff(q_param[j], h).subs(h, 0)) for j in nonpivot]
    if all(x == 0 for x in direction):
        raise SystemExit(f"zero tangent direction {local_row['exceptional_id']} side {side} {parameter}")
    return direction


def rees_surface(local_row, chart_p: int):
    d, gens, orders = reconstruct_local_germ(local_row)
    e = sp.Symbol("e")
    u = sp.symbols("u0:5")
    nonp = [j for j in range(6) if j != chart_p]
    sub = {d[chart_p]: e}
    for k, j in enumerate(nonp):
        sub[d[j]] = e * u[k]
    pullbacks = [clean(g.subs(sub)) for g in gens]
    strict = [clean(g / (e ** order)) for g, order in zip(pullbacks, orders)]
    return d, e, u, nonp, sub, pullbacks, strict


def rank_at(polys, variables, point_sub):
    J = sp.Matrix([[sp.diff(f, v) for v in variables] for f in polys])
    return int(J.subs(point_sub).rank()), J


def saturation_basis(polys, unit, variables):
    z = sp.Symbol("z_loc")
    G = sp.groebner(list(polys) + [1 - z * unit], z, *variables, order="lex", extension=I)
    elim = [clean(g.as_expr()) for g in G.polys if not g.as_expr().has(z)]
    if not elim:
        raise SystemExit("empty saturation elimination basis")
    return sp.groebner(elim, *variables, order="grevlex", extension=I)


def ideals_equal_by_groebner(a, b, variables):
    Ga = sp.groebner(list(a), *variables, order="grevlex", extension=I)
    Gb = sp.groebner(list(b), *variables, order="grevlex", extension=I)
    return (
        all(clean(Ga.reduce(sp.expand(f))[1]) == 0 for f in b)
        and all(clean(Gb.reduce(sp.expand(f))[1]) == 0 for f in a)
    )


def combined_e_saturation_equals(pull_surface, pull_side, strict_surface, strict_side, e, variables):
    z = sp.Symbol("z_e_sat")
    G = sp.groebner(list(pull_surface) + list(pull_side) + [1 - z * e], z, *variables, order="lex", extension=I)
    elim = [clean(g.as_expr()) for g in G.polys if not g.as_expr().has(z)]
    if not elim:
        return False
    return ideals_equal_by_groebner(elim, list(strict_surface) + list(strict_side), variables)


def nonzero_maximal_minors(jacobian, point_sub):
    out = []
    for cols in itertools.combinations(range(jacobian.cols), jacobian.rows):
        det = clean(jacobian[:, list(cols)].det())
        value = clean(det.subs(point_sub))
        if value != 0:
            out.append((list(cols), det, value))
    if not out:
        raise SystemExit("no nonzero maximal Jacobian minor on crossing")
    return out


def choose_local_uniformizer(strict_surface, strict_side, e, variables, crossing_sub):
    for idx, s in enumerate(strict_side):
        side_rank, side_J = rank_at(strict_surface + [s], variables, crossing_sub)
        if side_rank != 5:
            continue
        cross_rank, cross_J = rank_at(strict_surface + [s, e], variables, crossing_sub)
        if cross_rank != 6:
            continue
        cross_det = clean(cross_J.det())
        cross_det_value = clean(cross_det.subs(crossing_sub))
        if cross_det_value == 0:
            continue
        minors = nonzero_maximal_minors(side_J, crossing_sub)
        lam = cross_det
        lam_value = cross_det_value
        for _cols, det, value in minors:
            lam = clean(lam * det)
            lam_value = clean(lam_value * value)
        if lam_value == 0:
            raise SystemExit("localizer product unexpectedly vanished at crossing")
        Jsat = saturation_basis(strict_surface + [s], lam, variables)
        localized_full_side_ok = all(clean(Jsat.reduce(sp.expand(f))[1]) == 0 for f in strict_side)
        if localized_full_side_ok:
            return {
                "index": idx,
                "s": s,
                "side_rank": side_rank,
                "cross_rank": cross_rank,
                "cross_det": cross_det,
                "cross_det_value": cross_det_value,
                "minors": minors,
                "lambda": lam,
                "lambda_value": lam_value,
            }
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    b2a = load_locked(B2A, B2A_SHA)
    b2b1 = load_locked(B2B1, B2B1_SHA)
    b2b2 = load_locked(B2B2, B2B2_SHA)
    actual_side_source_blob = git_blob_sha1(SIDE_SOURCE)
    if actual_side_source_blob != SIDE_SOURCE_GIT_BLOB_SHA1:
        raise SystemExit(f"side parametrization source moved: {actual_side_source_blob}")
    if b2a["target_side_components"] != [f"SIDE_{x:03d}" for x in TARGET_SIDES]:
        raise SystemExit("B2A target side set moved")
    if b2a["incidence_pair_count"] != 24 or b2a["side_incident_exceptional_closure_count"] != 16:
        raise SystemExit("B2A incidence inventory moved")
    if b2b2["total_standard_rees_chart_count"] != 96 or b2b2["t_saturation_exact_check_count"] != 96:
        raise SystemExit("B2B2 Rees atlas moved")

    local_by_eid = {r["exceptional_id"]: r for r in b2b1["local_germ_rows"]}
    b2b2_by_eid = {r["exceptional_id"]: r for r in b2b2["exceptional_rows"]}
    side_rows_out = []
    crossing_total = 0
    combined_sat_pass = 0
    local_principal_pass = 0
    transverse_pass = 0

    for side_row in b2a["side_rows"]:
        side = int(side_row["side_index_1based"])
        if side not in TARGET_SIDES:
            raise SystemExit(f"unexpected target side {side}")
        if side_row["crossing_parameters_in_frozen_order"] != PARAMETERS or side_row["crossing_count"] != 6:
            raise SystemExit(f"crossing order moved for side {side}")
        e1, e2, e3 = side_signs(side)
        crossings_out = []

        for crossing in side_row["crossings"]:
            eid = crossing["exceptional_id"]
            parameter = crossing["side_parameter"]
            local_row = local_by_eid[eid]
            _point, _affine_pivot, _affine_nonpivot, d, side_forms = affine_node_and_side_forms(local_row, side)
            direction = tangent_direction(local_row, side, parameter)
            valid_pivots = [j for j, x in enumerate(direction) if clean(x) != 0]
            chart_p = valid_pivots[0]
            d2, e, u, nonp, sub, pull_surface, strict_surface = rees_surface(local_row, chart_p)
            if list(d2) != list(d):
                raise SystemExit("displacement variable convention drift")

            pull_side = [clean(f.subs(sub)) for f in side_forms]
            strict_side = []
            for f in pull_side:
                sf = clean(f / e)
                try:
                    sp.Poly(sf, e, *u, extension=I)
                except sp.PolynomialError as ex:
                    raise SystemExit(f"side Rees division failed {eid} side {side}: {ex}")
                if clean(f - e * sf) != 0:
                    raise SystemExit(f"side pullback not exactly e times strict equation {eid} side {side}")
                strict_side.append(sf)

            stored_chart = b2b2_by_eid[eid]["charts"][chart_p]
            if stored_chart["pivot_displacement_index_0based"] != chart_p:
                raise SystemExit("B2B2 chart ordering moved")
            if [encode_poly(f, [e, *u]) for f in strict_surface] != stored_chart["strict_transform_generators_Qi"]:
                raise SystemExit(f"B2B2 strict surface chart mismatch {eid} chart {chart_p}")

            pivot_dir = direction[chart_p]
            u_values = [clean(direction[j] / pivot_dir) for j in nonp]
            crossing_sub = {e: sp.Integer(0), **{u[k]: u_values[k] for k in range(5)}}
            if any(clean(f.subs(crossing_sub)) != 0 for f in strict_surface + strict_side):
                raise SystemExit(f"crossing point misses strict ideals {eid} side {side} chart {chart_p}")

            variables = [e, *u]
            surface_rank, _surface_J = rank_at(strict_surface, variables, crossing_sub)
            if surface_rank != 4:
                raise SystemExit(f"resolved surface not smooth at crossing {eid} side {side}: rank {surface_rank}")

            chosen = choose_local_uniformizer(strict_surface, strict_side, e, variables, crossing_sub)
            if chosen is None:
                raise SystemExit(f"no strict-side generator gives localized principal ideal at {eid} side {side}")
            sidx = chosen["index"]
            s_uniformizer = chosen["s"]
            local_principal_pass += 1
            transverse_pass += 1

            combined_sat_ok = combined_e_saturation_equals(
                pull_surface, pull_side, strict_surface, strict_side, e, variables
            )
            if not combined_sat_ok:
                raise SystemExit(f"combined side proper-transform saturation mismatch {eid} side {side}")
            combined_sat_pass += 1

            minors_out = [{
                "column_indices_0based": cols,
                "minor_Qi": encode_poly(det, variables),
                "minor_at_crossing_Qi": encode_element(value),
            } for cols, det, value in chosen["minors"]]

            crossings_out.append({
                "exceptional_id": eid,
                "side_parameter": parameter,
                "side_parameter_index_1based": int(crossing["side_parameter_index_1based"]),
                "canonical_rees_chart_pivot_displacement_index_0based": chart_p,
                "canonical_rees_chart_id": stored_chart["chart_id"],
                "valid_standard_rees_chart_pivots_from_side_tangent": valid_pivots,
                "side_tangent_displacement_direction_Qi": [encode_element(x) for x in direction],
                "crossing_rees_chart_point": {
                    "e_Qi": encode_element(sp.Integer(0)),
                    "u_Qi_in_chart_order": [encode_element(x) for x in u_values],
                },
                "side_strict_transform_generators_Qi": [encode_poly(f, variables) for f in strict_side],
                "selected_side_uniformizer_generator_index_0based": sidx,
                "literal_side_uniformizer_Qi": encode_poly(s_uniformizer, variables),
                "literal_exceptional_uniformizer": "e",
                "surface_jacobian_rank_at_crossing": surface_rank,
                "surface_plus_side_uniformizer_jacobian_rank_at_crossing": chosen["side_rank"],
                "surface_plus_side_plus_exceptional_jacobian_rank_at_crossing": chosen["cross_rank"],
                "distinguished_open": {
                    "condition": "lambda != 0",
                    "lambda_construction": "crossing transversality determinant times every side-Jacobian maximal minor nonzero at the crossing",
                    "crossing_transversality_determinant_Qi": encode_poly(chosen["cross_det"], variables),
                    "crossing_transversality_determinant_at_crossing_Qi": encode_element(chosen["cross_det_value"]),
                    "nonzero_side_jacobian_maximal_minors": minors_out,
                    "lambda_Qi": encode_poly(chosen["lambda"], variables),
                    "lambda_at_crossing_Qi": encode_element(chosen["lambda_value"]),
                },
                "exact_local_checks": {
                    "parameterized_side_point_matches_b2b1_node": True,
                    "side_tangent_selects_canonical_rees_chart": True,
                    "all_four_side_linear_pullbacks_equal_e_times_strict_generators": True,
                    "combined_surface_plus_side_pullback_e_saturation_equals_strict_transform_ideal": True,
                    "on_D_lambda_surface_plus_selected_s_equals_full_strict_side_ideal": True,
                    "lambda_is_nonzero_at_the_crossing": True,
                    "selected_s_is_literal_local_side_uniformizer": True,
                    "e_is_literal_local_exceptional_uniformizer": True,
                    "side_and_exceptional_are_transverse_regular_parameters_on_resolved_surface": True,
                },
                "cross_overlap_map": {
                    "source": f"{stored_chart['chart_id']}_SIDE_{side:03d}_DLAMBDA",
                    "target": stored_chart["chart_id"],
                    "open_embedding": "localize the same Rees chart at lambda",
                    "ambient_chart_variable_map": {str(v): str(v) for v in variables},
                    "exceptional_uniformizer_transition": "e_target=e_source",
                    "side_uniformizer_transition": "s_source=the selected literal side strict-transform polynomial in target (e,u0,...,u4)",
                },
            })
            crossing_total += 1

        if len(crossings_out) != 6:
            raise SystemExit(f"side {side} crossing neighborhood count moved")
        side_rows_out.append({
            "component_id": f"SIDE_{side:03d}",
            "side_index_1based": side,
            "family": "A1",
            "frozen_signs": {"e1": e1, "e2": e2, "e3": e3},
            "homogeneous_side_ideal_generators": [
                "a1",
                f"a2+({e1})*b3",
                f"a3+({e2})*b2",
                f"b1+({e3})*c",
            ],
            "source_parametrization": "[0,-e1*(u^2-v^2),-e2*(2uv),-e3*(u^2+v^2),2uv,u^2-v^2,u^2+v^2]",
            "crossing_neighborhood_count": 6,
            "crossing_neighborhoods": crossings_out,
        })

    if crossing_total != 24:
        raise SystemExit(f"expected 24 crossing opens, got {crossing_total}")

    cert = {
        "schema": "stage33.e3.v91c1x_r5b2b3a.a2_02_24_side_exceptional_crossing_uniformizer_charts.v2",
        "stage": "33-12",
        "candidate": "V91C1X_R5B2B3A_A2_02_24_SIDE_EXCEPTIONAL_CROSSING_UNIFORMIZER_CHARTS",
        "role": "EXACT_NONCREDIT_R5B2B3A_SOURCE_BOUND_SIDE_EXCEPTIONAL_CROSSING_NEIGHBORHOOD_CONSTRUCTION",
        "entry": {
            "pr": 1684,
            "authority": "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT",
            "stage33_progress": "6/11",
            "r5b2a_canonical_sha256": B2A_SHA,
            "r5b2b1_canonical_sha256": B2B1_SHA,
            "r5b2b2_canonical_sha256": B2B2_SHA,
        },
        "source_locks": {
            "r5b2a_incidence_path": "stages/stage33/33-12/e3-v91c1x-r5b2a-a2-02-target-side-incidence-closure.json",
            "r5b2a_incidence_sha256": B2A_SHA,
            "r5b2b1_local_germs_path": "stages/stage33/33-12/e3-v91c1x-r5b2b1-a2-02-full-closure-local-germs.json",
            "r5b2b1_local_germs_sha256": B2B1_SHA,
            "r5b2b2_rees_atlas_path": "stages/stage33/33-12/e3-v91c1x-r5b2b2-a2-02-full-16-exceptional-rees-charts.json",
            "r5b2b2_rees_atlas_sha256": B2B2_SHA,
            "side_parametrization_source_path": "stages/stage33/33-07/certify_boundary_side_p1_crossing_coordinates.py",
            "side_parametrization_source_git_blob_sha1": SIDE_SOURCE_GIT_BLOB_SHA1,
            "side_parametrization_source_actual_git_blob_sha1": actual_side_source_blob,
        },
        "target_side_components": [f"SIDE_{x:03d}" for x in TARGET_SIDES],
        "target_side_count": 4,
        "side_exceptional_crossing_count": crossing_total,
        "crossing_neighborhood_rows": side_rows_out,
        "exact_check_counts": {
            "combined_pullback_e_saturation_pass_count": combined_sat_pass,
            "localized_principal_side_uniformizer_pass_count": local_principal_pass,
            "side_exceptional_transversality_pass_count": transverse_pass,
        },
        "exact_consequence": {
            "all_24_target_side_exceptional_crossings_have_source_bound_rees_neighborhoods": crossing_total == 24,
            "all_24_crossings_have_literal_local_side_uniformizers": local_principal_pass == 24,
            "all_24_crossings_have_literal_exceptional_uniformizer_e": True,
            "all_24_crossings_have_exact_side_to_exceptional_cross_overlap_open_embeddings": True,
            "all_24_side_strict_transform_ideals_are_verified_by_combined_e_saturation": combined_sat_pass == 24,
            "all_24_side_exceptional_pairs_are_transverse_regular_parameters_on_the_resolved_surface": transverse_pass == 24,
            "four_target_side_full_strict_transform_neighborhoods_are_covered_away_from_exceptional_crossings": False,
        },
        "construction_status": {
            "full_16_exceptional_rees_atlases_materialized": True,
            "four_target_side_crossing_neighborhood_atlases_materialized": True,
            "side_component_uniformizers_at_all_24_side_exceptional_crossings_materialized": True,
            "side_to_exceptional_cross_overlap_maps_at_all_24_crossings_materialized": True,
            "four_target_side_away_from_exceptional_neighborhoods_materialized": False,
            "four_target_side_full_strict_transform_neighborhoods_materialized": False,
            "finite_surface_cover_materialized": False,
            "surface_all_double_overlap_transitions_materialized": False,
        },
        "next_missing_object": "SOURCE_BOUND_AWAY_FROM_EXCEPTIONAL_NEIGHBORHOODS_COVERING_THE_FOUR_TARGET_SIDE_STRICT_TRANSFORMS_PLUS_OVERLAP_MAPS_TO_THE_24_CROSSING_OPENS",
        "next_exact_leaf": "V91C1X_R5B2B3B_COVER_FOUR_TARGET_SIDE_STRICT_TRANSFORMS_AWAY_FROM_EXCEPTIONAL_CROSSINGS_AND_GLUE_TO_24_CROSSING_OPENS",
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
        "marker": "V91C1X_R5B2B3A_24_SIDE_EXCEPTIONAL_CROSSING_UNIFORMIZER_CHARTS_V2",
        "side_count": 4,
        "crossing_count": crossing_total,
        "combined_saturation_pass_count": combined_sat_pass,
        "localized_principal_pass_count": local_principal_pass,
        "transversality_pass_count": transverse_pass,
        "certificate_sha256": cert["canonical_sha256"],
        "next_exact_leaf": cert["next_exact_leaf"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
