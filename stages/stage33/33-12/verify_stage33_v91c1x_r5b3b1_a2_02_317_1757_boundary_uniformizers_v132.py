#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import materialize_e3_v91c1x_r5b3b1_a2_02_317_1757_boundary_uniformizers as mat

HERE = Path(__file__).resolve().parent
CERT = HERE / "e3-v91c1x-r5b3b1-a2-02-317-1757-boundary-uniformizers.json"
CERT_SHA = "8a5dcb751b312a846a06fac88298166efe8c1fd91ed0988b3cb04a408cfc2654"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
COMPONENTS = [
    "EXC_003", "EXC_004", "EXC_011", "EXC_012",
    "SIDE_002", "SIDE_004", "SIDE_006", "SIDE_008",
]
NEXT = "V91C1X_R5B3B2_ASSEMBLE_AND_AUDIT_A2_02_TAME_SYMBOL_SUM_FROM_EIGHT_UNIFORMIZER_RESIDUE_FUNCTION_PAIRS"


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def main() -> None:
    stored = json.loads(CERT.read_text(encoding="utf-8"))
    claimed = stored.get("canonical_sha256")
    body = dict(stored)
    body.pop("canonical_sha256", None)
    if claimed != CERT_SHA or csha(body) != CERT_SHA:
        raise SystemExit("R5B3B1 canonical sha invalid")

    rebuilt = mat.build_certificate()
    if rebuilt != stored:
        raise SystemExit("R5B3B1 exact replay differs from stored certificate")

    if stored["schema"] != "stage33.e3.v91c1x_r5b3b1.a2_02_317_1757_boundary_uniformizers.v1":
        raise SystemExit("R5B3B1 schema moved")
    if stored["candidate"] != "V91C1X_R5B3B1_A2_02_8_BOUNDARY_UNIFORMIZERS_ON_317_1757":
        raise SystemExit("R5B3B1 candidate moved")
    if stored["entry"]["authority"] != AUTHORITY or stored["entry"]["stage33_progress"] != "6/11":
        raise SystemExit("authority or Stage33 progress moved")

    a2 = stored["a2_02_uniformizers"]
    if a2["source_direction"] != "A2_02" or a2["component_count"] != 8:
        raise SystemExit("A2_02 uniformizer direction/count moved")
    if a2["component_ids_in_source_order"] != COMPONENTS:
        raise SystemExit("A2_02 uniformizer component order moved")
    rows = a2["uniformizer_rows"]
    pairs = a2["paired_residue_function_uniformizer_rows"]
    if len(rows) != 8 or [r["component_id"] for r in rows] != COMPONENTS:
        raise SystemExit("A2_02 uniformizer rows moved")
    if len(pairs) != 8 or [r["component_id"] for r in pairs] != COMPONENTS:
        raise SystemExit("A2_02 formal Gersten pair rows moved")

    for row in rows:
        src = row["source_uniformizer"]
        if len(src["exact_factorized_ambient_rational_function_Qi_sha256"]) != 64:
            raise SystemExit(f"factorized uniformizer hash missing: {row['component_id']}")
        cover = row["source_317_cover_pullbacks"]
        if cover["smooth_chart_count"] != 29 or cover["exceptional_rees_chart_count"] != 288 or cover["total_chart_count"] != 317:
            raise SystemExit(f"317-cover uniformizer pullback count moved: {row['component_id']}")
        if cover["exceptional_order_is_independent_of_standard_rees_chart_at_each_node"] is not True:
            raise SystemExit(f"exceptional order chart-invariance lost: {row['component_id']}")
        if len(cover["exceptional_order_by_frozen_node"]) != 48:
            raise SystemExit(f"exceptional node order inventory moved: {row['component_id']}")
        ref = row["common_refinement_pullback"]
        if ref["piece_count"] != 1757 or ref["assignment_is_source_projection_of_317_cover_pullback"] is not True:
            raise SystemExit(f"1757-piece uniformizer assignment moved: {row['component_id']}")

    idx = stored["cover_indexed_materialization"]
    expected = {
        "source_cover_chart_count": 317,
        "common_refinement_piece_count": 1757,
        "uniformizer_count": 8,
        "uniformizer_source_chart_pullback_count": 2536,
        "uniformizer_common_refinement_assignment_count": 14056,
        "exceptional_order_standard_chart_invariance_check_count": 384,
        "linear_factor_standard_rees_pullback_check_count": 9216,
    }
    for key, value in expected.items():
        if idx[key] != value:
            raise SystemExit(f"R5B3B1 count moved: {key}")
    for key in [
        "all_8_uniformizers_have_exact_Qi_factorized_rational_functions",
        "all_8_uniformizers_pulled_back_to_all_317_source_charts",
        "all_8_uniformizers_assigned_to_all_1757_common_refinement_pieces_via_source_projection",
        "target_boundary_valuation_support_is_delta_identity_for_all_8",
        "all_exceptional_orders_replayed_on_all_288_rees_charts_per_uniformizer",
        "factorized_pullback_representation_avoids_unnecessary_symbolic_product_expansion",
    ]:
        if idx[key] is not True:
            raise SystemExit(f"R5B3B1 materialization invariant lost: {key}")

    for pair in pairs:
        if pair["pair_semantics"] != "FORMAL_GERSTEN_INPUT_PAIR_PI_D_AND_RESIDUE_FUNCTION_ONLY_NOT_YET_A_CERTIFIED_GLOBAL_SYMBOL_SUM":
            raise SystemExit(f"formal pair semantics moved: {pair['component_id']}")
        if len(pair["residue_function_Qi_sha256"]) != 64 or len(pair["boundary_uniformizer_factorized_Qi_sha256"]) != 64:
            raise SystemExit(f"formal pair hash missing: {pair['component_id']}")

    status = stored["construction_status"]
    for key in [
        "source_bound_a2_02_component_residue_functions_cover_indexed",
        "source_bound_a2_02_component_uniformizers_materialized",
        "cover_indexed_uniformizer_pullbacks_materialized",
        "eight_residue_function_uniformizer_pairs_materialized",
    ]:
        if status[key] is not True:
            raise SystemExit(f"R5B3B1 construction progress lost: {key}")
    for key in [
        "tame_symbol_sum_candidate_assembled",
        "offboundary_codimension_one_residue_cancellation_verified",
        "single_global_a2_02_kummer_or_brauer_representative_materialized",
        "line_bundle_gm_1_cocycle_ell_ij_materialized",
        "square_root_1_cochain_r_ij_materialized",
        "literal_mu2_2_cocycle_materialized",
        "equivalent_unimodular_cech_glue_materialized",
        "same_representative_swap23_transport_materialized",
        "triple_overlap_action_difference_identity_verified",
    ]:
        if status[key] is not False:
            raise SystemExit(f"R5B3B1 construction firewall violated: {key}")

    consequence = stored["exact_consequence"]
    for key in [
        "the_r5b3a_eight_residue_function_packages_now_have_matching_source_bound_boundary_uniformizers",
        "both_members_of_each_formal_pair_pi_D_and_residue_function_are_indexed_on_the_same_317_cover_and_1757_refinement",
        "this_removes_the_component_uniformizer_local_equation_gap_for_the_eight_a2_02_boundary_components",
        "this_does_not_by_itself_prove_that_the_formal_sum_of_tame_symbols_has_zero_residue_on_every_offboundary_codimension_one_prime",
    ]:
        if consequence[key] is not True:
            raise SystemExit(f"R5B3B1 exact consequence moved: {key}")

    if stored["next_exact_leaf"] != NEXT:
        raise SystemExit("R5B3B1 next routing moved")
    for key, value in stored["credit_firewall"].items():
        if value is not False:
            raise SystemExit(f"credit firewall violated: {key}")

    print(json.dumps({
        "success": True,
        "marker": "V91C1X_R5B3B1_A2_02_317_1757_BOUNDARY_UNIFORMIZERS_VERIFIED",
        "certificate_sha256": claimed,
        "uniformizer_source_chart_pullback_count": 2536,
        "uniformizer_common_refinement_assignment_count": 14056,
        "exceptional_order_standard_chart_invariance_check_count": 384,
        "linear_factor_standard_rees_pullback_check_count": 9216,
        "next_exact_leaf": NEXT,
        "stage33_progress": "6/11",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
