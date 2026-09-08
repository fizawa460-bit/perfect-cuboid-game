#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import materialize_e3_v91c1x_r5b3a_a2_02_317_1757_literal_package_pullbacks as mat

HERE = Path(__file__).resolve().parent
CERT = HERE / "e3-v91c1x-r5b3a-a2-02-317-1757-literal-package-pullbacks.json"
CERT_SHA = "b694cd2aee502e13186cbe68e65ddce7a845e54e546c8cf548c1386ac5a71d31"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
COMPONENTS = [
    "EXC_003", "EXC_004", "EXC_011", "EXC_012",
    "SIDE_002", "SIDE_004", "SIDE_006", "SIDE_008",
]
MISSING = "SOURCE_BOUND_ASSEMBLY_RULE_COMBINING_THE_EIGHT_A2_02_COMPONENT_RESIDUE_FUNCTION_PACKAGES_INTO_ONE_317_COVER_INDEXED_CARTIER_KUMMER_REPRESENTATIVE_THEN_ELL_IJ_R_IJ_AND_TRIPLE_OVERLAP_ACTION_DIFFERENCE_IDENTITY"
NEXT = "V91C1X_R5B3B_ASSEMBLE_ONE_A2_02_CARTIER_KUMMER_REPRESENTATIVE_FROM_THE_EIGHT_COVER_INDEXED_LITERAL_PACKAGES"


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def main() -> None:
    stored = json.loads(CERT.read_text(encoding="utf-8"))
    claimed = stored.get("canonical_sha256")
    body = dict(stored)
    body.pop("canonical_sha256", None)
    if claimed != CERT_SHA or csha(body) != CERT_SHA:
        raise SystemExit("R5B3A canonical sha invalid")

    rebuilt = mat.build_certificate()
    if rebuilt != stored:
        raise SystemExit("R5B3A exact replay differs from stored certificate")

    if stored["schema"] != "stage33.e3.v91c1x_r5b3a.a2_02_317_1757_literal_package_pullbacks.v1":
        raise SystemExit("R5B3A schema moved")
    if stored["candidate"] != "V91C1X_R5B3A_A2_02_317_1757_LITERAL_PACKAGE_PULLBACKS":
        raise SystemExit("R5B3A candidate moved")
    if stored["entry"]["authority"] != AUTHORITY or stored["entry"]["stage33_progress"] != "6/11":
        raise SystemExit("authority or Stage33 progress moved")

    source = stored["a2_02_source"]
    if source["source_direction"] != "A2_02" or source["raw_order"] != 2:
        raise SystemExit("A2_02 source direction/raw order moved")
    if source["component_count"] != 8 or source["component_ids_in_source_order"] != COMPONENTS:
        raise SystemExit("A2_02 component inventory moved")
    rows = source["package_rows"]
    if len(rows) != 8 or [r["component_id"] for r in rows] != COMPONENTS:
        raise SystemExit("A2_02 package rows moved")

    for row in rows:
        src = row["source_literal_package"]
        if not src["ambient_rational_function_Qi"] or len(src["ambient_rational_function_Qi_sha256"]) != 64:
            raise SystemExit(f"literal Q(i) function missing: {row['component_id']}")
        cover = row["source_317_cover_pullbacks"]
        if cover["smooth_chart_count"] != 29 or cover["exceptional_rees_chart_count"] != 288 or cover["total_chart_count"] != 317:
            raise SystemExit(f"317-cover package pullback count moved: {row['component_id']}")
        if cover["exceptional_order_is_independent_of_standard_rees_chart_at_each_node"] is not True:
            raise SystemExit(f"exceptional order chart-invariance lost: {row['component_id']}")
        if len(cover["exceptional_order_by_frozen_node"]) != 48:
            raise SystemExit(f"exceptional node order inventory moved: {row['component_id']}")
        ref = row["common_refinement_pullback"]
        if ref["piece_count"] != 1757 or ref["assignment_is_source_projection_of_317_cover_pullback"] is not True:
            raise SystemExit(f"1757-piece package assignment moved: {row['component_id']}")

    idx = stored["cover_indexed_materialization"]
    expected = {
        "source_cover_chart_count": 317,
        "common_refinement_piece_count": 1757,
        "literal_package_count": 8,
        "literal_package_source_chart_pullback_count": 2536,
        "literal_package_common_refinement_assignment_count": 14056,
        "exceptional_order_standard_chart_invariance_check_count": 384,
    }
    for key, value in expected.items():
        if idx[key] != value:
            raise SystemExit(f"R5B3A count moved: {key}")
    for key in [
        "all_8_literal_packages_have_exact_Qi_ambient_functions",
        "all_8_packages_pulled_back_to_all_317_source_charts",
        "all_8_packages_assigned_to_all_1757_common_refinement_pieces_via_source_projection",
        "exceptional_leading_ratios_replayable_on_all_288_rees_charts",
    ]:
        if idx[key] is not True:
            raise SystemExit(f"cover-indexed materialization invariant lost: {key}")

    status = stored["construction_status"]
    for key in [
        "source_bound_literal_a2_02_component_package_functions_materialized",
        "cover_indexed_literal_package_pullbacks_materialized",
        "same_package_pullbacks_on_swap23_common_refinement_materialized",
    ]:
        if status[key] is not True:
            raise SystemExit(f"R5B3A construction progress lost: {key}")
    for key in [
        "single_global_a2_02_kummer_representative_assembled_from_the_eight_component_packages",
        "line_bundle_gm_1_cocycle_ell_ij_materialized",
        "square_root_1_cochain_r_ij_materialized",
        "literal_mu2_2_cocycle_materialized",
        "equivalent_unimodular_cech_glue_materialized",
        "same_representative_swap23_transport_materialized",
        "triple_overlap_action_difference_identity_verified",
    ]:
        if status[key] is not False:
            raise SystemExit(f"R5B3A construction firewall violated: {key}")

    consequence = stored["exact_consequence"]
    for key in [
        "r5b2d2_missing_literal_function_input_is_now_cover_indexed_at_the_eight_component_package_level",
        "source_projection_gives_exact_package_restrictions_on_each_of_1757_common_refinement_pieces",
        "this_does_not_by_itself_choose_a_global_kummer_or_cech_assembly_of_the_eight_residue_packages",
    ]:
        if consequence[key] is not True:
            raise SystemExit(f"R5B3A exact consequence moved: {key}")

    if stored["next_missing_object"] != MISSING or stored["next_exact_leaf"] != NEXT:
        raise SystemExit("R5B3A next routing moved")
    for key, value in stored["credit_firewall"].items():
        if value is not False:
            raise SystemExit(f"credit firewall violated: {key}")

    print(json.dumps({
        "success": True,
        "marker": "V91C1X_R5B3A_A2_02_317_1757_LITERAL_PACKAGE_PULLBACKS_VERIFIED",
        "certificate_sha256": claimed,
        "literal_package_source_chart_pullback_count": 2536,
        "literal_package_common_refinement_assignment_count": 14056,
        "exceptional_order_standard_chart_invariance_check_count": 384,
        "next_exact_leaf": NEXT,
        "stage33_progress": "6/11",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
