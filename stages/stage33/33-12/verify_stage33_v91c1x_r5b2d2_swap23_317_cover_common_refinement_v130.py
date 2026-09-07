#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import materialize_e3_v91c1x_r5b2d2_swap23_317_cover_common_refinement as mat

HERE = Path(__file__).resolve().parent
CERT = HERE / "e3-v91c1x-r5b2d2-swap23-317-cover-common-refinement.json"
NEXT = "V91C1X_R5B3_MATERIALIZE_LITERAL_A2_02_MU2_OR_EQUIVALENT_GLUE_ON_THE_SWAP23_COMMON_REFINEMENT"
MISSING = "SOURCE_BOUND_LITERAL_A2_02_REPRESENTATIVE_ON_THE_1757_PIECE_COMMON_REFINEMENT_THEN_ELL_IJ_R_IJ_AND_TRIPLE_OVERLAP_ACTION_DIFFERENCE_IDENTITY"


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def main() -> None:
    stored = json.loads(CERT.read_text(encoding="utf-8"))
    claimed = stored.get("canonical_sha256")
    body = dict(stored)
    body.pop("canonical_sha256", None)
    if claimed != csha(body):
        raise SystemExit("R5B2D2 canonical sha invalid")

    rebuilt = mat.build_certificate()
    if rebuilt != stored:
        raise SystemExit("R5B2D2 exact replay differs from stored certificate")

    if stored["schema"] != "stage33.e3.v91c1x_r5b2d2.swap23_317_cover_common_refinement.v1":
        raise SystemExit("R5B2D2 schema moved")
    if stored["entry"]["authority"] != "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT":
        raise SystemExit("authority moved")
    if stored["entry"]["stage33_progress"] != "6/11":
        raise SystemExit("Stage33 progress moved")

    action = stored["source_bound_swap23"]
    if action["coordinate_permutation_zero_based"] != [0, 2, 1, 3, 5, 4, 6]:
        raise SystemExit("swap23 permutation moved")
    for key in ["involutive", "node_action_is_permutation_of_48_frozen_nodes", "node_action_is_involutive"]:
        if action[key] is not True:
            raise SystemExit(f"swap23 action invariant lost: {key}")

    smooth = stored["smooth_cover_action"]
    if smooth["smooth_minor_chart_count"] != 29 or smooth["smooth_common_refinement_piece_count"] != 29:
        raise SystemExit("smooth cover counts moved")
    if smooth["pullback_action_is_permutation"] is not True or smooth["pullback_action_is_involutive"] is not True:
        raise SystemExit("smooth pullback action lost")

    exc = stored["exceptional_common_refinement"]
    expected = {
        "source_node_count": 48,
        "source_rees_chart_count_per_node": 6,
        "acted_target_rees_chart_count_per_node": 6,
        "piece_count_per_node": 36,
        "total_exceptional_refinement_piece_count": 1728,
        "tangent_derivative_invertibility_check_count": 48,
        "source_chart_global_tau_blowdown_compatibility_check_count": 288,
        "pulled_target_localizer_center_unit_check_count": 2304,
    }
    for key, value in expected.items():
        if exc[key] != value:
            raise SystemExit(f"exceptional refinement count moved: {key}")

    idx = stored["common_refinement_index"]
    if idx["smooth_piece_count"] != 29 or idx["exceptional_piece_count"] != 1728 or idx["total_piece_count"] != 1757:
        raise SystemExit("1757-piece refinement count moved")
    for key in [
        "equals_1757",
        "covers_whole_resolved_surface",
        "each_piece_refines_one_source_317_cover_chart",
        "each_piece_refines_one_swap23_pulled_back_317_cover_chart",
        "source_projection_maps_materialized",
        "acted_projection_maps_materialized",
    ]:
        if idx[key] is not True:
            raise SystemExit(f"common refinement invariant lost: {key}")

    trans = stored["transition_compatibility"]
    for key in ["smooth_smooth", "exceptional_exceptional_same_node", "smooth_exceptional"]:
        if trans[key] is not True:
            raise SystemExit(f"transition compatibility lost: {key}")

    consequence = stored["exact_consequence"]
    for key in [
        "swap23_pullback_of_all_29_smooth_chart_domains_materialized",
        "swap23_action_on_all_48_exceptional_centers_materialized",
        "swap23_lift_to_all_288_source_rees_charts_materialized",
        "explicit_source_bound_common_refinement_of_original_and_swap23_pulled_317_covers_materialized",
        "all_common_refinement_projection_maps_materialized",
        "double_overlap_transition_compatibility_verified",
    ]:
        if consequence[key] is not True:
            raise SystemExit(f"exact consequence lost: {key}")

    status = stored["construction_status"]
    for key in ["source_bound_swap23_coordinate_action_materialized", "swap23_pullback_of_each_317_chart_domain_materialized", "cover_action_or_common_refinement_materialized"]:
        if status[key] is not True:
            raise SystemExit(f"construction progress lost: {key}")
    for key in ["same_representative_transport_materialized", "line_bundle_gm_1_cocycle_ell_ij_materialized", "square_root_1_cochain_r_ij_materialized", "literal_mu2_2_cocycle_materialized", "equivalent_unimodular_cech_glue_materialized", "triple_overlap_action_difference_identity_verified"]:
        if status[key] is not False:
            raise SystemExit(f"construction firewall violated: {key}")

    if stored["next_missing_object"] != MISSING or stored["next_exact_leaf"] != NEXT:
        raise SystemExit("next routing moved")
    for key, value in stored["credit_firewall"].items():
        if value is not False:
            raise SystemExit(f"credit firewall violated: {key}")

    print(json.dumps({
        "success": True,
        "marker": "V91C1X_R5B2D2_SWAP23_317_COVER_COMMON_REFINEMENT_VERIFIED",
        "certificate_sha256": claimed,
        "common_refinement_piece_count": 1757,
        "next_exact_leaf": NEXT,
        "stage33_progress": "6/11",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
