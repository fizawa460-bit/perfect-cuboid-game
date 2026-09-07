#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

import materialize_e3_v91c1x_r5b2d2_swap23_317_cover_common_refinement as atlas
import materialize_e3_v91c1x_r5b3a_a2_02_317_1757_literal_package_pullbacks as pkg

HERE = Path(__file__).resolve().parent
S07 = HERE.parent / "33-07"
UNIFORMIZER_PRODUCER = S07 / "certify_72_boundary_weak_approximation_uniformizers.py"
UNIFORMIZERS = S07 / "boundary-weak-approximation-uniformizers-72.json"
R5B3A = HERE / "e3-v91c1x-r5b3a-a2-02-317-1757-literal-package-pullbacks.json"
D2 = HERE / "e3-v91c1x-r5b2d2-swap23-317-cover-common-refinement.json"
OUT = HERE / "e3-v91c1x-r5b3b1-a2-02-317-1757-boundary-uniformizers.json"

UNIFORMIZER_PRODUCER_BLOB_SHA1 = "b108921184eb45dbd416035839371984bd6ef738"
R5B3A_SHA = "b694cd2aee502e13186cbe68e65ddce7a845e54e546c8cf548c1386ac5a71d31"
D2_SHA = "3165eab3d08ed29dcba429ed9f397d49054739459b08507e6a63d1cba2d66cbb"
SOURCE = "A2_02"
COMPONENTS = [
    "EXC_003", "EXC_004", "EXC_011", "EXC_012",
    "SIDE_002", "SIDE_004", "SIDE_006", "SIDE_008",
]


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha1(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load_canonical(path: Path, expected: str | None = None) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    claimed = obj.get("canonical_sha256")
    if not claimed:
        raise SystemExit(f"missing canonical sha: {path}")
    body = dict(obj)
    body.pop("canonical_sha256")
    actual = csha(body)
    if claimed != actual:
        raise SystemExit(f"canonical mismatch: {path.name}")
    if expected is not None and claimed != expected:
        raise SystemExit(f"source lock moved: {path.name}")
    return obj


def linear_form(encoded, X):
    if len(encoded) != len(X):
        raise SystemExit("uniformizer ambient coefficient width moved")
    return atlas.clean(sum(atlas.decode_element(z) * X[j] for j, z in enumerate(encoded)))


def uniformizer_expression(component: str, rec: dict, X):
    if component.startswith("EXC_"):
        expr = linear_form(rec["ambient_linear_form_Qi"], X)
    else:
        num = linear_form(rec["side_numerator_linear_form_Qi"], X)
        den = sp.Integer(1)
        for row in rec["denominator_exceptional_linear_forms_Qi"]:
            den *= linear_form(row, X)
        expr = atlas.clean(num / den)
    if expr == 0:
        raise SystemExit(f"zero uniformizer expression: {component}")
    return expr


def build_certificate() -> dict:
    if git_blob_sha1(UNIFORMIZER_PRODUCER.read_bytes()) != UNIFORMIZER_PRODUCER_BLOB_SHA1:
        raise SystemExit("72-boundary uniformizer producer blob moved")

    uni = load_canonical(UNIFORMIZERS)
    r5b3a = load_canonical(R5B3A, R5B3A_SHA)
    d2 = load_canonical(D2, D2_SHA)
    exc = atlas.load_locked(atlas.EXC, atlas.EXC_SHA)
    c2 = atlas.load_locked(atlas.C2, atlas.C2_SHA)

    if uni["schema"] != "STAGE33_07_BOUNDARY_WEAK_APPROXIMATION_UNIFORMIZERS_72_V1":
        raise SystemExit("uniformizer schema moved")
    if uni["boundary_counts"] != {
        "side": 24,
        "exceptional": 48,
        "total": 72,
        "side_exceptional_incidence_edges": 144,
        "incident_exceptionals_per_side": 6,
    }:
        raise SystemExit("72-boundary inventory moved")
    if uni["exact_checks"]["full_72_by_72_boundary_valuation_matrix_is_identity"] is not True:
        raise SystemExit("I72 boundary valuation certificate lost")
    if uni["offboundary_unit_condition"]["therefore_all_72_uniformizers_have_valuation_zero_on_all_24_offboundary_primes"] is not True:
        raise SystemExit("uniformizer offboundary unit prefix lost")

    valuation_rows = {r["uniformizer_for"]: r for r in uni["boundary_valuation_identity_certificate"]}
    if any(valuation_rows[c]["nonzero_boundary_valuations"] != {c: 1} for c in COMPONENTS):
        raise SystemExit("target uniformizer boundary valuation support moved")

    exc_rows = {r["boundary_component_id"]: r for r in uni["exceptional_uniformizers"]}
    side_rows = {r["boundary_component_id"]: r for r in uni["side_uniformizers"]}
    if not all(c in exc_rows for c in COMPONENTS[:4]) or not all(c in side_rows for c in COMPONENTS[4:]):
        raise SystemExit("A2_02 target uniformizer inventory incomplete")

    if r5b3a["a2_02_source"]["component_ids_in_source_order"] != COMPONENTS:
        raise SystemExit("R5B3A component order moved")
    package_by_component = {r["component_id"]: r for r in r5b3a["a2_02_source"]["package_rows"]}
    if set(package_by_component) != set(COMPONENTS):
        raise SystemExit("R5B3A package inventory moved")

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
    expected_eids = [f"EXC_{i:03d}" for i in range(1, 49)]
    if [r["exceptional_id"] for r in models] != expected_eids:
        raise SystemExit("frozen exceptional inventory moved")
    metas = {r["exceptional_id"]: atlas.node_meta(r) for r in models}

    smooth_refinement = d2["smooth_cover_action"]["minor_action_rows"]
    if len(smooth_refinement) != 29:
        raise SystemExit("D2 smooth refinement inventory moved")

    rows = []
    pair_rows = []
    total_source_chart_pullbacks = 0
    total_refinement_assignments = 0
    exceptional_order_checks = 0

    for component in COMPONENTS:
        source_rec = exc_rows[component] if component.startswith("EXC_") else side_rows[component]
        expr = uniformizer_expression(component, source_rec, X)
        ambient_encoded = atlas.encode_rational(expr, list(X))
        ambient_sha = csha(ambient_encoded)

        smooth_formula_rows = [
            {
                "source_minor_id": mid,
                "source_chart_principal_open": f"D_+({mid})",
                "boundary_uniformizer_pullback_Qi_sha256": ambient_sha,
            }
            for mid in minor_ids
        ]
        smooth_descriptors = [
            {
                "piece_id": r["common_refinement_piece_id"],
                "source_minor_id": r["source_minor_id_equal_to_pullback_open"],
                "boundary_uniformizer_pullback_Qi_sha256": ambient_sha,
            }
            for r in smooth_refinement
        ]

        exceptional_formula_rows = []
        node_orders = {}
        source_chart_sha = {}
        for eid in expected_eids:
            orders = []
            for cp in range(6):
                e, u, _d, _nonp, blow = atlas.chart_blowdown(metas[eid], cp)
                pull = atlas.clean(expr.subs({X[j]: blow[j] for j in range(7)}, simultaneous=True))
                if pull == 0:
                    raise SystemExit(f"uniformizer pullback vanished identically: {component}/{eid}/D{cp}")
                encoded = atlas.encode_rational(pull, [e, *u])
                order, leading = pkg.exceptional_leading_record(pull, e, u)
                cid = atlas.chart_id(eid, cp)
                rec = {
                    "source_chart_id": cid,
                    "exceptional_order": int(order),
                    "boundary_uniformizer_pullback_Qi_sha256": csha(encoded),
                    "leading_ratio_on_exceptional_P5_Qi_sha256": csha(leading),
                }
                exceptional_formula_rows.append(rec)
                source_chart_sha[cid] = rec["boundary_uniformizer_pullback_Qi_sha256"]
                orders.append(int(order))
            if len(set(orders)) != 1:
                raise SystemExit(f"uniformizer exceptional order depends on Rees chart: {component}/{eid}/{orders}")
            expected_order = 1 if component.startswith("EXC_") and component == eid else 0
            if orders[0] != expected_order:
                raise SystemExit(f"uniformizer exceptional order mismatch: {component}/{eid}/{orders[0]} != {expected_order}")
            node_orders[eid] = orders[0]
            exceptional_order_checks += 1

        refinement_descriptors = list(smooth_descriptors)
        for eid in expected_eids:
            for cp_source in range(6):
                source_chart = atlas.chart_id(eid, cp_source)
                for cp_target in range(6):
                    refinement_descriptors.append({
                        "piece_id": f"REF_{eid}_S{cp_source}_T{cp_target}",
                        "source_chart_id": source_chart,
                        "boundary_uniformizer_pullback_Qi_sha256": source_chart_sha[source_chart],
                    })
        if len(refinement_descriptors) != 1757:
            raise SystemExit(f"1757-piece uniformizer assignment count moved: {component}")

        source_chart_count = len(smooth_formula_rows) + len(exceptional_formula_rows)
        if source_chart_count != 317:
            raise SystemExit(f"317 source-chart uniformizer count moved: {component}")
        total_source_chart_pullbacks += source_chart_count
        total_refinement_assignments += len(refinement_descriptors)

        if component.startswith("EXC_"):
            source_summary = {
                "type": "EXCEPTIONAL",
                "rational_uniformizer_expression": source_rec["rational_uniformizer_expression"],
                "boundary_valuation_support": source_rec["boundary_valuation_support"],
                "node_linear_order_exactly_one": source_rec["node_linear_order_exactly_one"],
            }
        else:
            source_summary = {
                "type": "SIDE",
                "rational_uniformizer_expression": source_rec["rational_uniformizer_expression"],
                "incident_exceptional_ids": source_rec["incident_exceptional_ids"],
                "corrected_boundary_valuation_support": source_rec["corrected_boundary_valuation_support"],
                "incident_node_orders_exactly_one": source_rec["incident_node_orders_exactly_one"],
            }

        rows.append({
            "component_id": component,
            "source_uniformizer": {
                **source_summary,
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
        pair_rows.append({
            "component_id": component,
            "residue_function_Qi_sha256": package_by_component[component]["source_literal_package"]["ambient_rational_function_Qi_sha256"],
            "boundary_uniformizer_Qi_sha256": ambient_sha,
            "pair_semantics": "FORMAL_GERSTEN_INPUT_PAIR_PI_D_AND_RESIDUE_FUNCTION_ONLY_NOT_YET_A_CERTIFIED_GLOBAL_SYMBOL_SUM",
        })

    if total_source_chart_pullbacks != 8 * 317:
        raise SystemExit("total uniformizer/source-chart count moved")
    if total_refinement_assignments != 8 * 1757:
        raise SystemExit("total uniformizer/refinement assignment count moved")
    if exceptional_order_checks != 8 * 48:
        raise SystemExit("exceptional uniformizer order check count moved")

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b1.a2_02_317_1757_boundary_uniformizers.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B1_A2_02_8_BOUNDARY_UNIFORMIZERS_ON_317_1757",
        "role": "EXACT_NONCREDIT_R5B3B1_SOURCE_BOUND_A2_02_BOUNDARY_UNIFORMIZERS_PAIRED_WITH_RESIDUE_FUNCTION_PACKAGES_ON_317_COVER_AND_1757_SWAP23_REFINEMENT",
        "entry": {
            "pr": 1695,
            "authority": "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT",
            "stage33_progress": "6/11",
        },
        "source_locks": {
            "boundary_uniformizer_producer_blob_sha1": UNIFORMIZER_PRODUCER_BLOB_SHA1,
            "generated_72_boundary_uniformizer_canonical_sha256": uni["canonical_sha256"],
            "r5b3a_literal_package_pullbacks_sha256": R5B3A_SHA,
            "r5b2d2_common_refinement_sha256": D2_SHA,
            "r5b2c2_cover_sha256": atlas.C2_SHA,
            "exceptional_p1_tangent_coordinates_sha256": atlas.EXC_SHA,
        },
        "a2_02_uniformizers": {
            "source_direction": SOURCE,
            "component_count": 8,
            "component_ids_in_source_order": COMPONENTS,
            "uniformizer_rows": rows,
            "paired_residue_function_uniformizer_rows": pair_rows,
        },
        "cover_indexed_materialization": {
            "source_cover_chart_count": 317,
            "common_refinement_piece_count": 1757,
            "uniformizer_count": 8,
            "uniformizer_source_chart_pullback_count": total_source_chart_pullbacks,
            "uniformizer_common_refinement_assignment_count": total_refinement_assignments,
            "exceptional_order_standard_chart_invariance_check_count": exceptional_order_checks,
            "all_8_uniformizers_have_exact_Qi_rational_functions": True,
            "all_8_uniformizers_pulled_back_to_all_317_source_charts": True,
            "all_8_uniformizers_assigned_to_all_1757_common_refinement_pieces_via_source_projection": True,
            "target_boundary_valuation_support_is_delta_identity_for_all_8": True,
            "all_exceptional_orders_replayed_on_all_288_rees_charts_per_uniformizer": True,
        },
        "construction_status": {
            "source_bound_a2_02_component_residue_functions_cover_indexed": True,
            "source_bound_a2_02_component_uniformizers_materialized": True,
            "cover_indexed_uniformizer_pullbacks_materialized": True,
            "eight_residue_function_uniformizer_pairs_materialized": True,
            "tame_symbol_sum_candidate_assembled": False,
            "offboundary_codimension_one_residue_cancellation_verified": False,
            "single_global_a2_02_kummer_or_brauer_representative_materialized": False,
            "line_bundle_gm_1_cocycle_ell_ij_materialized": False,
            "square_root_1_cochain_r_ij_materialized": False,
            "literal_mu2_2_cocycle_materialized": False,
            "equivalent_unimodular_cech_glue_materialized": False,
            "same_representative_swap23_transport_materialized": False,
            "triple_overlap_action_difference_identity_verified": False,
        },
        "exact_consequence": {
            "the_r5b3a_eight_residue_function_packages_now_have_matching_source_bound_boundary_uniformizers": True,
            "both_members_of_each_formal_pair_pi_D_and_residue_function_are_indexed_on_the_same_317_cover_and_1757_refinement": True,
            "this_removes_the_component_uniformizer_local_equation_gap_for_the_eight_a2_02_boundary_components": True,
            "this_does_not_by_itself_prove_that_the_formal_sum_of_tame_symbols_has_zero_residue_on_every_offboundary_codimension_one_prime": True,
        },
        "next_missing_object": "EXACT_TAME_SYMBOL_OR_CECH_ASSEMBLY_FROM_THE_EIGHT_PAIRS_PI_D_AND_F_D_WITH_ALL_OFFBOUNDARY_CODIMENSION_ONE_RESIDUES_ZERO_THEN_ELL_IJ_R_IJ_AND_TRIPLE_OVERLAP_ACTION_DIFFERENCE_IDENTITY",
        "next_exact_leaf": "V91C1X_R5B3B2_ASSEMBLE_AND_AUDIT_A2_02_TAME_SYMBOL_SUM_FROM_EIGHT_UNIFORMIZER_RESIDUE_FUNCTION_PAIRS",
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
            "hostile_audit_credit": False,
            "merge_allowed": False,
        },
    }
    cert["canonical_sha256"] = csha(cert)
    return cert


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    cert = build_certificate()
    if args.write:
        OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "success": True,
        "candidate": cert["candidate"],
        "canonical_sha256": cert["canonical_sha256"],
        "uniformizer_count": 8,
        "source_chart_pullbacks": cert["cover_indexed_materialization"]["uniformizer_source_chart_pullback_count"],
        "refinement_assignments": cert["cover_indexed_materialization"]["uniformizer_common_refinement_assignment_count"],
        "exceptional_order_checks": cert["cover_indexed_materialization"]["exceptional_order_standard_chart_invariance_check_count"],
        "stage33_progress": "6/11",
        "next_exact_leaf": cert["next_exact_leaf"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
