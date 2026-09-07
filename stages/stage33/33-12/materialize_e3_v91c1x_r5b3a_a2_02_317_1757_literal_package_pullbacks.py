#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

import materialize_e3_v91c1x_r5b2d2_swap23_317_cover_common_refinement as atlas

HERE = Path(__file__).resolve().parent
BF = HERE / "boundary-function-generator-source-lock.json"
V1A = HERE / "e3-v91c1a-a2-02-literal-boundary-seed-localization.json"
V1B = HERE / "e3-v91c1b-a2-02-resolved-valuation-carrier-preflight.json"
D2 = HERE / "e3-v91c1x-r5b2d2-swap23-317-cover-common-refinement.json"
OUT = HERE / "e3-v91c1x-r5b3a-a2-02-317-1757-literal-package-pullbacks.json"

BF_SHA = "aaacc000f2e5fbbe733789f5f2a19d6c2cb14b5d3a26d0b8e508eea1f3bc8c96"
V1A_SHA = "7f81ce5da7a4880cf0ffa048ab335fe2db9a643158d26144f45d0de22604b403"
V1B_SHA = "4398be760e937e1aba279af5fd099b029dc9998675503b5df7130e714ee81387"
D2_SHA = "3165eab3d08ed29dcba429ed9f397d49054739459b08507e6a63d1cba2d66cbb"
SOURCE = "A2_02"
EXPECTED_COMPONENTS = [
    "EXC_003", "EXC_004", "EXC_011", "EXC_012",
    "SIDE_002", "SIDE_004", "SIDE_006", "SIDE_008",
]
I = sp.I


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def linear_form(coefficients, X):
    if len(coefficients) != len(X):
        raise SystemExit(f"ambient coefficient length moved: {len(coefficients)}")
    return atlas.clean(sum(atlas.decode_element(z) * X[j] for j, z in enumerate(coefficients)))


def package_expression(package, X):
    numerator = sp.Integer(1)
    for factor in package["numerator_factors"]:
        numerator *= linear_form(factor["coefficients_Qi"], X) ** int(factor.get("exponent", 1))
    denominator = linear_form(package["denominator"]["coefficients_Qi"], X) ** int(package["denominator"]["exponent"])
    if numerator == 0 or denominator == 0:
        raise SystemExit(f"zero literal package expression: {package['component_id']}")
    return atlas.clean(numerator / denominator)


def e_order_poly(poly, e, u):
    P = sp.Poly(sp.expand(poly), e, *u, extension=I)
    terms = P.terms()
    if not terms:
        raise SystemExit("zero polynomial while taking exceptional order")
    return min(int(mon[0]) for mon, _coeff in terms)


def exceptional_leading_record(expr, e, u):
    num, den = sp.fraction(sp.cancel(expr))
    num = sp.expand(num)
    den = sp.expand(den)
    on = e_order_poly(num, e, u)
    od = e_order_poly(den, e, u)
    lead_num = atlas.clean((num / (e ** on)).subs(e, 0))
    lead_den = atlas.clean((den / (e ** od)).subs(e, 0))
    if lead_num == 0 or lead_den == 0:
        raise SystemExit("leading exceptional residue vanished after exact order removal")
    lead = atlas.encode_rational(atlas.clean(lead_num / lead_den), list(u))
    return on - od, lead


def build_certificate():
    bf = atlas.load_locked(BF, BF_SHA)
    v1a = atlas.load_locked(V1A, V1A_SHA)
    v1b = atlas.load_locked(V1B, V1B_SHA)
    d2 = atlas.load_locked(D2, D2_SHA)
    exc = atlas.load_locked(atlas.EXC, atlas.EXC_SHA)
    c2 = atlas.load_locked(atlas.C2, atlas.C2_SHA)

    matches = [r for r in bf["generator_records"] if r["source_direction"] == SOURCE]
    if len(matches) != 1:
        raise SystemExit("A2_02 source-lock selection ceased to be unique")
    source = matches[0]
    packages = source["component_packages"]
    if int(source["raw_order"]) != 2:
        raise SystemExit("A2_02 raw order moved")
    if [p["component_id"] for p in packages] != EXPECTED_COMPONENTS:
        raise SystemExit("A2_02 component package order moved")
    if v1a["literal_package_record"]["component_ids_in_source_order"] != EXPECTED_COMPONENTS:
        raise SystemExit("V91C1A component inventory moved")
    if v1b["a2_02_target"]["component_ids"] != EXPECTED_COMPONENTS:
        raise SystemExit("V91C1B component inventory moved")
    if d2["common_refinement_index"]["total_piece_count"] != 1757:
        raise SystemExit("R5B2D2 refinement count moved")
    if c2["finite_cover"]["total_cover_chart_count"] != 317:
        raise SystemExit("R5B2C2 cover count moved")

    X = sp.symbols("a1 a2 a3 b1 b2 b3 c")
    minor_rows = c2["smooth_complement_cover"]["minor_rows"]
    minor_ids = [r["minor_id"] for r in minor_rows]
    if len(minor_ids) != 29 or len(set(minor_ids)) != 29:
        raise SystemExit("smooth minor inventory moved")

    models = exc["exceptional_models"]
    expected_ids = [f"EXC_{i:03d}" for i in range(1, 49)]
    if [r["exceptional_id"] for r in models] != expected_ids:
        raise SystemExit("frozen exceptional inventory moved")
    metas = {r["exceptional_id"]: atlas.node_meta(r) for r in models}

    smooth_refinement = d2["smooth_cover_action"]["minor_action_rows"]
    if len(smooth_refinement) != 29:
        raise SystemExit("D2 smooth refinement inventory moved")

    package_rows = []
    total_source_chart_pullbacks = 0
    total_refinement_assignments = 0
    exceptional_order_chart_invariance_checks = 0

    for package in packages:
        component = package["component_id"]
        expr = package_expression(package, X)
        ambient_encoded = atlas.encode_rational(expr, list(X))
        ambient_sha = csha(ambient_encoded)

        smooth_descriptors = []
        smooth_formula_rows = []
        for mid in minor_ids:
            row = {
                "source_minor_id": mid,
                "source_chart_principal_open": f"D_+({mid})",
                "literal_package_pullback_Qi_sha256": ambient_sha,
            }
            smooth_formula_rows.append(row)
        for row in smooth_refinement:
            smooth_descriptors.append({
                "piece_id": row["common_refinement_piece_id"],
                "source_minor_id": row["source_minor_id_equal_to_pullback_open"],
                "literal_package_pullback_Qi_sha256": ambient_sha,
            })

        exceptional_formula_rows = []
        node_orders = {}
        source_chart_pullback_sha = {}
        for eid in expected_ids:
            orders = []
            for cp in range(6):
                e, u, _d, _nonp, blow = atlas.chart_blowdown(metas[eid], cp)
                pull = atlas.clean(expr.subs({X[j]: blow[j] for j in range(7)}, simultaneous=True))
                if pull == 0:
                    raise SystemExit(f"literal package pullback vanished identically: {component}/{eid}/D{cp}")
                encoded = atlas.encode_rational(pull, [e, *u])
                order, leading = exceptional_leading_record(pull, e, u)
                cid = atlas.chart_id(eid, cp)
                rec = {
                    "source_chart_id": cid,
                    "exceptional_order": order,
                    "literal_package_pullback_Qi_sha256": csha(encoded),
                    "leading_ratio_on_exceptional_P5_Qi_sha256": csha(leading),
                }
                exceptional_formula_rows.append(rec)
                source_chart_pullback_sha[cid] = rec["literal_package_pullback_Qi_sha256"]
                orders.append(order)
            if len(set(orders)) != 1:
                raise SystemExit(f"exceptional valuation depends on Rees standard chart: {component}/{eid}/{orders}")
            node_orders[eid] = orders[0]
            exceptional_order_chart_invariance_checks += 1

        refinement_descriptors = list(smooth_descriptors)
        for eid in expected_ids:
            for cp_source in range(6):
                source_chart = atlas.chart_id(eid, cp_source)
                for cp_target in range(6):
                    refinement_descriptors.append({
                        "piece_id": f"REF_{eid}_S{cp_source}_T{cp_target}",
                        "source_chart_id": source_chart,
                        "literal_package_pullback_Qi_sha256": source_chart_pullback_sha[source_chart],
                    })
        if len(refinement_descriptors) != 1757:
            raise SystemExit(f"1757-piece assignment count moved for {component}")

        source_chart_count = len(smooth_formula_rows) + len(exceptional_formula_rows)
        if source_chart_count != 317:
            raise SystemExit(f"317 source chart pullback count moved for {component}")
        total_source_chart_pullbacks += source_chart_count
        total_refinement_assignments += len(refinement_descriptors)

        package_rows.append({
            "component_id": component,
            "kind": package["kind"],
            "source_literal_package": {
                "numerator_factor_count": len(package["numerator_factors"]),
                "numerator_factor_exponents": [int(f.get("exponent", 1)) for f in package["numerator_factors"]],
                "denominator_exponent": int(package["denominator"]["exponent"]),
                "ambient_rational_function_Qi": ambient_encoded,
                "ambient_rational_function_Qi_sha256": ambient_sha,
            },
            "source_317_cover_pullbacks": {
                "smooth_chart_count": len(smooth_formula_rows),
                "exceptional_rees_chart_count": len(exceptional_formula_rows),
                "total_chart_count": source_chart_count,
                "smooth_rows_sha256": csha(smooth_formula_rows),
                "exceptional_rows_sha256": csha(exceptional_formula_rows),
                "exceptional_order_is_independent_of_standard_rees_chart_at_each_node": True,
                "exceptional_order_by_frozen_node": node_orders,
            },
            "common_refinement_pullback": {
                "piece_count": len(refinement_descriptors),
                "assignment_rows_sha256": csha(refinement_descriptors),
                "assignment_is_source_projection_of_317_cover_pullback": True,
            },
        })

    if total_source_chart_pullbacks != 8 * 317:
        raise SystemExit("total package/source-chart pullback count moved")
    if total_refinement_assignments != 8 * 1757:
        raise SystemExit("total package/refinement assignment count moved")
    if exceptional_order_chart_invariance_checks != 8 * 48:
        raise SystemExit("exceptional order chart-invariance check count moved")

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3a.a2_02_317_1757_literal_package_pullbacks.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3A_A2_02_317_1757_LITERAL_PACKAGE_PULLBACKS",
        "role": "EXACT_NONCREDIT_R5B3A_SOURCE_BOUND_LITERAL_A2_02_RESIDUE_FUNCTION_PACKAGE_PULLBACKS_ON_317_COVER_AND_SWAP23_COMMON_REFINEMENT",
        "entry": {
            "pr": 1695,
            "authority": "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT",
            "stage33_progress": "6/11",
        },
        "source_locks": {
            "boundary_function_generator_source_lock_sha256": BF_SHA,
            "v91c1a_literal_boundary_seed_sha256": V1A_SHA,
            "v91c1b_resolved_valuation_carrier_sha256": V1B_SHA,
            "r5b2d2_common_refinement_sha256": D2_SHA,
            "r5b2c2_cover_sha256": atlas.C2_SHA,
            "exceptional_p1_tangent_coordinates_sha256": atlas.EXC_SHA,
        },
        "a2_02_source": {
            "source_direction": SOURCE,
            "raw_order": 2,
            "component_count": 8,
            "component_ids_in_source_order": EXPECTED_COMPONENTS,
            "package_rows": package_rows,
        },
        "cover_indexed_materialization": {
            "source_cover_chart_count": 317,
            "common_refinement_piece_count": 1757,
            "literal_package_count": 8,
            "literal_package_source_chart_pullback_count": total_source_chart_pullbacks,
            "literal_package_common_refinement_assignment_count": total_refinement_assignments,
            "exceptional_order_standard_chart_invariance_check_count": exceptional_order_chart_invariance_checks,
            "all_8_literal_packages_have_exact_Qi_ambient_functions": True,
            "all_8_packages_pulled_back_to_all_317_source_charts": True,
            "all_8_packages_assigned_to_all_1757_common_refinement_pieces_via_source_projection": True,
            "exceptional_leading_ratios_replayable_on_all_288_rees_charts": True,
        },
        "construction_status": {
            "source_bound_literal_a2_02_component_package_functions_materialized": True,
            "cover_indexed_literal_package_pullbacks_materialized": True,
            "same_package_pullbacks_on_swap23_common_refinement_materialized": True,
            "single_global_a2_02_kummer_representative_assembled_from_the_eight_component_packages": False,
            "line_bundle_gm_1_cocycle_ell_ij_materialized": False,
            "square_root_1_cochain_r_ij_materialized": False,
            "literal_mu2_2_cocycle_materialized": False,
            "equivalent_unimodular_cech_glue_materialized": False,
            "same_representative_swap23_transport_materialized": False,
            "triple_overlap_action_difference_identity_verified": False,
        },
        "exact_consequence": {
            "r5b2d2_missing_literal_function_input_is_now_cover_indexed_at_the_eight_component_package_level": True,
            "source_projection_gives_exact_package_restrictions_on_each_of_1757_common_refinement_pieces": True,
            "this_does_not_by_itself_choose_a_global_kummer_or_cech_assembly_of_the_eight_residue_packages": True,
        },
        "next_missing_object": "SOURCE_BOUND_ASSEMBLY_RULE_COMBINING_THE_EIGHT_A2_02_COMPONENT_RESIDUE_FUNCTION_PACKAGES_INTO_ONE_317_COVER_INDEXED_CARTIER_KUMMER_REPRESENTATIVE_THEN_ELL_IJ_R_IJ_AND_TRIPLE_OVERLAP_ACTION_DIFFERENCE_IDENTITY",
        "next_exact_leaf": "V91C1X_R5B3B_ASSEMBLE_ONE_A2_02_CARTIER_KUMMER_REPRESENTATIVE_FROM_THE_EIGHT_COVER_INDEXED_LITERAL_PACKAGES",
        "credit_firewall": {
            "authority_promotion": False,
            "genuine_full_surface_h2_mu2_lift_credit": False,
            "h2_fixedness_credit": False,
            "marked_brauer_image_credit": False,
            "mask20_credit": False,
            "source_bound_dim5_credit": False,
            "stage33_close_credit": False,
            "stage33_release_credit": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "merge_allowed": False,
        },
    }
    cert["canonical_sha256"] = csha(cert)
    return cert


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    cert = build_certificate()
    if args.write:
        OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "success": True,
        "marker": cert["candidate"],
        "certificate_sha256": cert["canonical_sha256"],
        "source_cover_chart_count": cert["cover_indexed_materialization"]["source_cover_chart_count"],
        "common_refinement_piece_count": cert["cover_indexed_materialization"]["common_refinement_piece_count"],
        "literal_package_source_chart_pullback_count": cert["cover_indexed_materialization"]["literal_package_source_chart_pullback_count"],
        "literal_package_common_refinement_assignment_count": cert["cover_indexed_materialization"]["literal_package_common_refinement_assignment_count"],
        "global_kummer_representative_assembled": cert["construction_status"]["single_global_a2_02_kummer_representative_assembled_from_the_eight_component_packages"],
        "next_exact_leaf": cert["next_exact_leaf"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
