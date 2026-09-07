#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sympy as sp

from materialize_e3_v91c1x_r5b2b3a_24_side_exceptional_crossing_uniformizer_charts_v2 import (
    B2A, B2A_SHA, B2B1, B2B1_SHA, B2B2, B2B2_SHA,
    SIDE_SOURCE, SIDE_SOURCE_GIT_BLOB_SHA1, TARGET_SIDES, PARAMETERS, I,
    clean, csha, encode_element, encode_poly, git_blob_sha1, load_locked,
    side_signs, affine_node_and_side_forms, tangent_direction, rees_surface,
    rank_at, saturation_basis, combined_e_saturation_equals, OUT,
)


def principal_colon_generators(polys, f, variables):
    t = sp.Symbol("t_colon")
    G = sp.groebner(
        [t * g for g in polys] + [(1 - t) * f],
        t, *variables, order="lex", extension=I,
    )
    inter = [clean(g.as_expr()) for g in G.polys if not g.as_expr().has(t)]
    if not inter:
        raise SystemExit("intersection elimination returned no generators")
    quot = []
    for h in inter:
        q, r = sp.div(h, f, *variables, extension=I)
        q, r = clean(q), clean(r)
        if r != 0 or clean(h - f * q) != 0:
            raise SystemExit(f"intersection generator not divisible by colon divisor: {h}")
        quot.append(q)
    return sp.groebner(quot, *variables, order="grevlex", extension=I)


def first_nonvanishing_colon_witness(J, GJ, g, variables, point_sub):
    if clean(GJ.reduce(sp.expand(g))[1]) == 0:
        return sp.Integer(1), sp.Integer(1), True
    C = principal_colon_generators(J, g, variables)
    for p in C.polys:
        h = clean(p.as_expr())
        value = clean(h.subs(point_sub))
        if value == 0:
            continue
        if clean(GJ.reduce(sp.expand(h * g))[1]) != 0:
            raise SystemExit("colon witness failed exact multiplication membership")
        return h, value, False
    return None, None, False


def choose_local_uniformizer(strict_surface, strict_side, e, variables, crossing_sub):
    for idx, s in enumerate(strict_side):
        side_rank, _side_J = rank_at(strict_surface + [s], variables, crossing_sub)
        if side_rank != 5:
            continue
        cross_rank, cross_J = rank_at(strict_surface + [s, e], variables, crossing_sub)
        if cross_rank != 6:
            continue
        cross_det = clean(cross_J.det())
        cross_det_value = clean(cross_det.subs(crossing_sub))
        if cross_det_value == 0:
            continue

        J = list(strict_surface) + [s]
        GJ = sp.groebner(J, *variables, order="grevlex", extension=I)
        witnesses = []
        lam = cross_det
        lam_value = cross_det_value
        ok = True
        for gidx, g in enumerate(strict_side):
            h, value, already = first_nonvanishing_colon_witness(J, GJ, g, variables, crossing_sub)
            if h is None:
                ok = False
                break
            witnesses.append({
                "generator_index_0based": gidx,
                "already_in_surface_plus_s_ideal": already,
                "witness": h,
                "witness_at_crossing": value,
            })
            lam = clean(lam * h)
            lam_value = clean(lam_value * value)
        if not ok or lam_value == 0:
            continue

        Jsat = saturation_basis(J, lam, variables)
        if not all(clean(Jsat.reduce(sp.expand(g))[1]) == 0 for g in strict_side):
            continue
        return {
            "index": idx,
            "s": s,
            "side_rank": side_rank,
            "cross_rank": cross_rank,
            "cross_det": cross_det,
            "cross_det_value": cross_det_value,
            "colon_witnesses": witnesses,
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
    colon_witness_pass = 0

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
                raise SystemExit(f"no exact colon-localized side uniformizer at {eid} side {side}")
            sidx = chosen["index"]
            s_uniformizer = chosen["s"]
            local_principal_pass += 1
            transverse_pass += 1
            colon_witness_pass += 1

            combined_sat_ok = combined_e_saturation_equals(
                pull_surface, pull_side, strict_surface, strict_side, e, variables
            )
            if not combined_sat_ok:
                raise SystemExit(f"combined side proper-transform saturation mismatch {eid} side {side}")
            combined_sat_pass += 1

            witnesses_out = [{
                "strict_side_generator_index_0based": w["generator_index_0based"],
                "already_in_surface_plus_s_ideal": w["already_in_surface_plus_s_ideal"],
                "colon_witness_Qi": encode_poly(w["witness"], variables),
                "colon_witness_at_crossing_Qi": encode_element(w["witness_at_crossing"]),
            } for w in chosen["colon_witnesses"]]

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
                    "lambda_construction": "crossing transversality determinant times one nonvanishing exact colon witness for each strict-side generator modulo (surface,s)",
                    "crossing_transversality_determinant_Qi": encode_poly(chosen["cross_det"], variables),
                    "crossing_transversality_determinant_at_crossing_Qi": encode_element(chosen["cross_det_value"]),
                    "exact_colon_witnesses": witnesses_out,
                    "lambda_Qi": encode_poly(chosen["lambda"], variables),
                    "lambda_at_crossing_Qi": encode_element(chosen["lambda_value"]),
                },
                "exact_local_checks": {
                    "parameterized_side_point_matches_b2b1_node": True,
                    "side_tangent_selects_canonical_rees_chart": True,
                    "all_four_side_linear_pullbacks_equal_e_times_strict_generators": True,
                    "combined_surface_plus_side_pullback_e_saturation_equals_strict_transform_ideal": True,
                    "each_colon_witness_times_its_strict_side_generator_lies_in_surface_plus_selected_s_ideal": True,
                    "all_colon_witnesses_are_nonzero_at_the_crossing": True,
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
        "schema": "stage33.e3.v91c1x_r5b2b3a.a2_02_24_side_exceptional_crossing_uniformizer_charts.v3",
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
            "exact_colon_localizer_pass_count": colon_witness_pass,
            "localized_principal_side_uniformizer_pass_count": local_principal_pass,
            "side_exceptional_transversality_pass_count": transverse_pass,
        },
        "exact_consequence": {
            "all_24_target_side_exceptional_crossings_have_source_bound_rees_neighborhoods": crossing_total == 24,
            "all_24_crossings_have_exact_colon_localizers": colon_witness_pass == 24,
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
        "marker": "V91C1X_R5B2B3A_24_SIDE_EXCEPTIONAL_CROSSING_UNIFORMIZER_CHARTS_V3",
        "side_count": 4,
        "crossing_count": crossing_total,
        "combined_saturation_pass_count": combined_sat_pass,
        "exact_colon_localizer_pass_count": colon_witness_pass,
        "localized_principal_pass_count": local_principal_pass,
        "transversality_pass_count": transverse_pass,
        "certificate_sha256": cert["canonical_sha256"],
        "next_exact_leaf": cert["next_exact_leaf"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
