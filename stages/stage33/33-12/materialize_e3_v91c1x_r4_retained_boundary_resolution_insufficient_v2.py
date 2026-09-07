#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
STATE = S33 / "MAIN-STATE.json"
R2 = HERE / "e3-v91c1x-r2-literal-mu2-or-unimodular-cech-glue-contract.json"
R3 = HERE / "e3-v91c1x-r3-cover-indexed-a2-02-representative-bounded-preflight.json"
LOCAL = HERE / "e3-v91c1x-r4-a2-02-local-chart-inventory.json"
EXCSEL = HERE / "e3-v91c1x-r4-exceptional-chart-selector.json"
SIDE_PRODUCER = S33 / "33-07" / "materialize_mixed_order_side_ambient_function_lifts.py"
EXC_PRODUCER = S33 / "33-07" / "materialize_mixed_order_exceptional_ambient_tangent_function_lifts.py"
OUT = HERE / "e3-v91c1x-r4-retained-boundary-resolution-insufficient-for-cover-indexed-h2.json"

OLD_STATE_SHA = "a29b5ab67e170fd45408d3c248cd5aaf3a148c67d6f8a90e22816cbd870d71bb"
R2_SHA = "912f00e0b680c39cdd0b99fb92174b5b45858dceeda4019799260869238766c1"
R3_SHA = "e631d91eaa40a9f73b33e53ceff25745824f8ad6380d88d956424e29e9bd040e"
LOCAL_SHA = "68f61b79b07027e97b4822c4f074cd52f65cf05473475fe964fd0b6785e8c53d"
EXCSEL_SHA = "588660e35a653581e7f152f80583a0b8fcf2d12085613938ddacb1dae6fe2110"
PR = 1682

CAND = "V91C1X_R4_RETAINED_BOUNDARY_RESOLUTION_DATA_INSUFFICIENT_FOR_COVER_INDEXED_A2_02_H2_REPRESENTATIVE"
MISSING = "NEW_SOURCE_BOUND_A2_02_FINITE_COVER_WITH_LITERAL_LOCAL_EQUATIONS_UNIFORMIZERS_OVERLAP_TRANSITIONS_AND_SWAP23_COMMON_REFINEMENT_SUFFICIENT_TO_MATERIALIZE_Z_IJK_ELL_IJ_R_IJ_AND_TRIPLE_OVERLAP_IDENTITY"
NEXT = "V91C1X_R5_FIND_OR_CONSTRUCT_SOURCE_BOUND_A2_02_FINITE_COVER_LOCAL_EQUATION_UNIFORMIZER_OVERLAP_GLUE_PACKAGE"
COMPONENTS = [
    "EXC_003", "EXC_004", "EXC_011", "EXC_012",
    "SIDE_002", "SIDE_004", "SIDE_006", "SIDE_008",
]


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def file_sha256(path: Path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_locked(path: Path, expected: str):
    obj = json.loads(path.read_text(encoding="utf-8"))
    claimed = obj["canonical_sha256"]
    body = dict(obj)
    body.pop("canonical_sha256")
    actual = csha(body)
    assert claimed == expected == actual, (str(path), claimed, actual, expected)
    return obj


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    state = load_locked(STATE, OLD_STATE_SHA)
    load_locked(R2, R2_SHA)
    load_locked(R3, R3_SHA)
    local = load_locked(LOCAL, LOCAL_SHA)
    excsel = load_locked(EXCSEL, EXCSEL_SHA)

    assert local["components"] == COMPONENTS
    cq = local["construction_questions"]
    assert cq["rows_expose_edge_ids"] is True
    assert cq["rows_expose_cover_or_overlap_indices"] is False
    assert cq["side_rows_expose_component_local_equation_beyond_D"] is False
    assert cq["exceptional_rows_expose_component_local_equation_beyond_R0_R1"] is False
    for key in [
        "accepted_source_representative_materialized",
        "equivalent_unimodular_cech_glue_materialized",
        "literal_mu2_2_cocycle_materialized",
        "swap23_common_refinement_materialized",
        "h2_fixedness_credit",
        "mask20_credit",
        "theorem_credit",
        "merge_allowed",
    ]:
        assert local["credit_firewall"][key] is False, key

    assert excsel["targets"] == COMPONENTS[:4]
    flags = excsel["bounded_schema_flags"]
    assert flags["cover_or_overlap_key_seen"] is False
    assert flags["uniformizer_or_local_equation_key_seen"] is False
    assert flags["transition_or_glue_key_seen"] is False
    assert flags["tangent_or_coordinate_key_seen"] is True
    efw = excsel["interpretation_firewall"]
    for key in [
        "selector_proves_open_cover",
        "selector_proves_overlap_transition",
        "selector_proves_component_uniformizer",
        "accepted_source_h2_mu2_representative_materialized",
        "literal_mu2_2_cocycle_materialized",
        "equivalent_unimodular_cech_glue_materialized",
        "swap23_common_refinement_materialized",
        "h2_fixedness_credit",
        "mask20_credit",
        "theorem_credit",
        "merge_allowed",
    ]:
        assert efw[key] is False, key

    side_text = SIDE_PRODUCER.read_text(encoding="utf-8")
    exc_text = EXC_PRODUCER.read_text(encoding="utf-8")
    assert "boundary-function ambient lift, not yet a global Gersten/Brauer lift" in side_text
    assert "This still is not a global Gersten/Brauer lift" in exc_text
    assert "global compatibility across all 72 boundary components remain" in exc_text

    cert = {
        "schema": "STAGE33_E3_V91C1X_R4_RETAINED_BOUNDARY_RESOLUTION_INSUFFICIENT_V1",
        "candidate": CAND,
        "credit": "NONCREDIT_CONSTRUCTION_BLOCKER",
        "pr": PR,
        "inputs": {
            "r2_contract": {"path": str(R2.relative_to(S33.parent.parent)), "canonical_sha256": R2_SHA},
            "r3_preflight": {"path": str(R3.relative_to(S33.parent.parent)), "canonical_sha256": R3_SHA},
            "local_chart_inventory": {"path": str(LOCAL.relative_to(S33.parent.parent)), "canonical_sha256": LOCAL_SHA},
            "exceptional_chart_selector": {"path": str(EXCSEL.relative_to(S33.parent.parent)), "canonical_sha256": EXCSEL_SHA},
            "side_ambient_lift_producer": {
                "path": str(SIDE_PRODUCER.relative_to(S33.parent.parent)),
                "file_sha256": file_sha256(SIDE_PRODUCER),
                "declared_scope": "BOUNDARY_FUNCTION_AMBIENT_LIFT_NOT_YET_GLOBAL_GERSTEN_BRAUER_LIFT",
            },
            "exceptional_ambient_tangent_lift_producer": {
                "path": str(EXC_PRODUCER.relative_to(S33.parent.parent)),
                "file_sha256": file_sha256(EXC_PRODUCER),
                "declared_scope": "NOT_GLOBAL_GERSTEN_BRAUER_LIFT_GLOBAL_72_COMPONENT_COMPATIBILITY_FIREWALLED",
            },
        },
        "bounded_scope": {
            "a2_02_components": COMPONENTS,
            "inspected_chain": "R4_COMPACT_A2_02_LOCAL_INVENTORY_PLUS_EXCEPTIONAL_SELECTOR_PLUS_EXACT_SIDE_AND_EXCEPTIONAL_AMBIENT_LIFT_PRODUCERS",
            "repository_wide_search_claim": False,
            "repository_wide_absence_claim": False,
            "mathematical_nonexistence_claim": False,
            "route_mathematically_impossible_claim": False,
        },
        "bounded_findings": {
            "ambient_residue_functions_retained": True,
            "edge_ids_retained": True,
            "exceptional_tangent_coordinate_models_retained": True,
            "finite_cover_materialized": False,
            "overlap_indices_materialized": False,
            "component_uniformizers_materialized": False,
            "literal_local_equations_materialized": False,
            "overlap_transitions_materialized": False,
            "equivalent_unimodular_cech_glue_materialized": False,
            "literal_mu2_2_cocycle_materialized": False,
            "swap23_common_refinement_materialized": False,
            "line_bundle_gm_1_cocycle_ell_ij_materialized": False,
            "square_root_1_cochain_r_ij_materialized": False,
            "triple_overlap_identity_verified": False,
        },
        "exact_consequence": "THE_INSPECTED_RETAINED_BOUNDARY_RESOLUTION_CHAIN_IS_INSUFFICIENT_TO_MATERIALIZE_THE_R2_ACCEPTED_COVER_INDEXED_A2_02_H2_REPRESENTATIVE",
        "next_missing_object": MISSING,
        "next_exact_leaf_after_audit": NEXT,
        "credit_firewall": {
            "accepted_source_h2_representative_credit": False,
            "h2_fixedness_credit": False,
            "mask20_credit": False,
            "sign_b1_h2_fixedness_credit": False,
            "sign_a2_h2_fixedness_credit": False,
            "source_bound_dim5_credit": False,
            "marked_brauer_image_credit": False,
            "stage33_close_credit": False,
            "stage33_release_credit": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
            "merge_allowed": False,
        },
        "audit_checkpoint": {
            "mathematically_substantial_checkpoint": True,
            "hostile_audit_required": True,
            "audit_pass_credit": False,
            "merge_allowed": False,
            "next_expected_command": "HOSTILE_AUDIT_PR_1682_V91C1X_R4_NEGATIVE_CHECKPOINT_EXACT_HEAD",
        },
        "stage33_progress": "6/11",
    }
    cert["canonical_sha256"] = csha(cert)

    state["schema"] = "STAGE33_MAIN_COMPACT_STATE_V53_V91C1X_R4_RETAINED_BOUNDARY_RESOLUTION_INSUFFICIENT_CHECKPOINT"
    state["authority_sync"]["branch_candidate_frontier"] = CAND
    state["authority_sync"]["status"] = "V91C1V_AUTHORITY_R4_RETAINED_BOUNDARY_RESOLUTION_INSUFFICIENT_PENDING_GROUPED_HOSTILE_AUDIT"
    state["branch_exact_frontier_candidate"] = "stages/stage33/33-12/e3-v91c1x-r4-retained-boundary-resolution-insufficient-for-cover-indexed-h2.json"
    state["candidate_audit_gate"] = {
        "candidate": CAND,
        "candidate_certificate": state["branch_exact_frontier_candidate"],
        "candidate_certificate_sha256": cert["canonical_sha256"],
        "pr": PR,
        "status": "PENDING_GROUPED_HOSTILE_AUDIT_R4_NEGATIVE_CHECKPOINT",
        "audit_pass_credit": False,
        "mathematical_authority_promoted": False,
        "hostile_audit_verdict": None,
        "hostile_audit_review_node": None,
        "hostile_audit_submitted_at": None,
        "exact_audited_head": None,
        "merged": False,
        "merge_allowed": False,
    }
    state["continuation_provenance"]["x_r4_retained_boundary_resolution_construction"] = {
        "pr": PR,
        "candidate": CAND,
        "certificate_sha256": cert["canonical_sha256"],
        "inspected_chain_insufficient_for_r2_representative": True,
        "repository_wide_absence_claim": False,
        "mathematical_nonexistence_claim": False,
        "finite_cover_materialized": False,
        "equivalent_unimodular_cech_glue_materialized": False,
        "literal_mu2_2_cocycle_materialized": False,
        "swap23_common_refinement_materialized": False,
        "triple_overlap_identity_verified": False,
        "next_missing_object": MISSING,
    }
    state["continuation_provenance"]["grouped_hostile_audit_policy"] = {
        "same_pr": PR,
        "r1_r2_r3_grouped_audit_complete": True,
        "r4_negative_construction_checkpoint_materialized": True,
        "hostile_audit_still_required_before_authority_credit_or_merge": True,
        "current_stop_reason": "R4_EXACT_CONSTRUCTION_BLOCKER_REACHED_GROUPED_HOSTILE_AUDIT_REQUIRED",
        "stop_when": ["GROUPED_HOSTILE_AUDIT_COMPLETED"],
    }
    state["current"] = {
        "active_missing_interface": MISSING,
        "logical_internal_branch": "33-13_FINITE_V4_KUMMER_MATRIX_REPAIR",
        "next_exact_leaf": NEXT,
        "substep": "E3_V91C1X_R4_RETAINED_BOUNDARY_RESOLUTION_INSUFFICIENT_CHECKPOINT",
        "unit": "33-12",
    }
    state["current_exact_frontier"]["a2_02_r4_retained_boundary_resolution_insufficiency_materialized"] = True
    state["current_exact_frontier"]["a2_02_r4_finite_cover_materialized"] = False
    state["current_exact_frontier"]["a2_02_r4_overlap_indices_materialized"] = False
    state["current_exact_frontier"]["a2_02_r4_component_uniformizers_materialized"] = False
    state["current_exact_frontier"]["a2_02_r4_literal_local_equations_materialized"] = False
    state["current_exact_frontier"]["a2_02_r4_overlap_transitions_materialized"] = False
    state["current_leaf_working_set"] = [
        "docs/research-os/policies/repository-asset-discovery.md",
        "docs/arsenal/index.json",
        "docs/arsenal/cards/provisional/S33-PW04.md",
        "docs/arsenal/cards/provisional/S33-PW07.md",
        "docs/arsenal/cards/provisional/S33-PW08.md",
        "stages/stage33/33-12/e3-v91c1x-r2-literal-mu2-or-unimodular-cech-glue-contract.json",
        "stages/stage33/33-12/e3-v91c1x-r3-cover-indexed-a2-02-representative-bounded-preflight.json",
        "stages/stage33/33-12/e3-v91c1x-r4-retained-boundary-resolution-insufficient-for-cover-indexed-h2.json",
        "stages/stage33/33-12/e3-v91c1x-r4-a2-02-local-chart-inventory.json",
        "stages/stage33/33-12/diagnose_e3_v91c1x_r4_exceptional_chart_selector.py",
        "stages/stage33/33-07/materialize_mixed_order_side_ambient_function_lifts.py",
        "stages/stage33/33-07/materialize_mixed_order_exceptional_ambient_tangent_function_lifts.py",
    ]
    state["execution_gate"] = {
        "advance_allowed": False,
        "advance_scope": "GROUPED_HOSTILE_AUDIT_V91C1X_R4_RETAINED_BOUNDARY_RESOLUTION_INSUFFICIENT_CHECKPOINT",
        "next_expected_command": "HOSTILE_AUDIT_PR_1682_V91C1X_R4_NEGATIVE_CHECKPOINT_EXACT_HEAD",
        "stop_semantics": "STOP_FOR_GROUPED_HOSTILE_AUDIT_NO_R5_OR_DOWNSTREAM_CREDIT",
    }
    state["work_checkpoint"] = {
        "authority": "V91C1V_HOSTILE_REAUDITED_MERGED",
        "status": "V91C1X_R4_RETAINED_BOUNDARY_RESOLUTION_INSUFFICIENT_PENDING_GROUPED_HOSTILE_AUDIT",
    }
    state["stage33_progress"] = "6/11"

    for key in [
        "a2_02_accepted_source_representative_materialized",
        "a2_02_equivalent_unimodular_cech_glue_materialized",
        "a2_02_literal_mu2_2_cocycle_materialized",
        "a2_02_cover_action_or_common_refinement_materialized",
        "a2_02_line_bundle_gm_1_cocycle_ell_ij_materialized",
        "a2_02_square_root_1_cochain_r_ij_materialized",
        "a2_02_triple_overlap_action_difference_identity_verified",
        "a2_02_marked_brauer_image_must_be_swap23_fixed",
        "a2_02_marked_brauer_image_excluded_from_mask20",
        "a2_02_source_bound_stabilizer_fixed_subspace_materialized",
        "a2_02_marked_brauer_image_computed",
        "e3_genuine_full_surface_h2_mu2_lift_materialized",
        "e3_kummer_column_materialized",
    ]:
        assert state["current_exact_frontier"][key] is False, key
    for key in [
        "stage33_12_closed_exact",
        "stage33_13_released",
        "receiver_credit",
        "theorem_credit",
        "endpoint_credit",
        "merge_allowed",
    ]:
        assert state["firewalls"][key] is False, key

    state.pop("canonical_sha256")
    state["canonical_sha256"] = csha(state)

    if args.write:
        OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        STATE.write_text(json.dumps(state, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")

    print(json.dumps({
        "success": True,
        "marker": "V114_R4_RETAINED_BOUNDARY_RESOLUTION_INSUFFICIENT_CHECKPOINT",
        "certificate_sha256": cert["canonical_sha256"],
        "state_sha256": state["canonical_sha256"],
        "candidate": CAND,
        "next_missing_object": MISSING,
        "advance_allowed": False,
        "next_expected_command": state["execution_gate"]["next_expected_command"],
        "stage33_progress": "6/11",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
