#!/usr/bin/env python3
"""Build/check compact Stage33 MAIN V11 after V10 hostile-audit PASS.

The compact state projects the detailed controller and the two post-V10 audit
receipts only. Older exact facts remain controller-locked and are not reopened.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

H = Path(__file__).resolve().parent
OUT = H / "MAIN-STATE.json"

AUDIT_PATH = H / "33-12/v10-hostile-audit-pass-receipt.json"
AUDIT_SHA = "b8de80e3f06f655e03c347a3c29dd904c86a1a54689d5e4b80627bfcda56faf7"
GAP_PATH = H / "33-12/j2-named-order4-actual-s3-source-lock-gap-v10.json"
GAP_SHA = "e369c1f6705e5442200c053aa5c4d7ce46de8b87b52338f04eb78ff1fa6dddb1"


def csha(x):
    return hashlib.sha256(
        json.dumps(x, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_canonical(path: Path, expected: str):
    x = json.loads(path.read_text())
    body = dict(x)
    got = body.pop("canonical_sha256")
    assert got == expected == csha(body), path
    return x


c = json.loads((H / "controller.json").read_text())
audit = load_canonical(AUDIT_PATH, AUDIT_SHA)
gap = load_canonical(GAP_PATH, GAP_SHA)
s = c["stage33_12"]
q = c["current"]

assert c["schema"] == "STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V55_V10_AUDIT_PASS_NAMED_ORDER4_SOURCE_GAP"
assert c["stage33_progress"] == "6/11"
assert q["unit"] == "33-12"
assert q["logical_internal_branch"] == "33-13_FINITE_V4_KUMMER_MATRIX_REPAIR"
assert q["substep"] == "IDENTIFY_NAMED_J2_ORDER4_LIFT_WITH_ACTUAL_S3_ACTION"
assert q["active_missing_interface"] == "SOURCE_LOCKED_NAMED_J2_ORDER4_LIFT_IN_RETAINED_MIXED_248_BASIS_WITH_ACTUAL_SWAP_IMAGES_MISSING"
assert q["next_exact_leaf"] == gap["next_exact_leaf"]

assert audit["status"] == "PASS_HOSTILE_AUDIT"
assert audit["audit_review_id"] == 5083583438
assert audit["audited_head_sha"] == "088a0e5eae448616a5dc7f2c05369e4debf0bd4e"
assert audit["merge_commit_sha"] == "9b97f0795d297e8afdbea56e3bf6ff3608c78639"
assert audit["pass_boundary"]["named_j2_source_label_selected"] is False
assert audit["pass_boundary"]["kummer_standard_columns_materialized"] == 0

assert gap["status"] == "PASS_EXACT_V10_POST_AUDIT_SOURCE_LOCK_GAP_REFINED_NO_LABEL_INFERENCE"
assert gap["authoritative_v10_facts"]["unique_joint_s3_fixed_candidate_retained10_mask_decimal"] == 6
assert gap["authoritative_v10_facts"]["unique_joint_s3_fixed_candidate_proper14_mask_decimal"] == 25
assert gap["authoritative_v10_facts"]["named_j2_order4_lift_selected"] is False
assert gap["no_inference"]["unique_joint_s3_fixed_candidate_implies_named_j2_mask6"] is False
assert gap["no_inference"]["semantic_u1_fixed_implies_named_order4_lift_fixed"] is False
assert gap["no_inference"]["target_compatibility_may_select_source_label"] is False

assert s["v10_hostile_audit_pass_receipt_sha256"] == AUDIT_SHA
assert s["v10_post_audit_named_order4_source_gap_sha256"] == GAP_SHA
assert s["actual_indlist_to_magma_picard_basis_bridge_materialized"] is True
assert s["actual_swap_mixed_discriminant_actions_materialized"] is True
assert s["corrected_J2_order4_affine_candidate_count"] == 4
assert s["corrected_J2_order4_unique_joint_s3_fixed_retained10_mask_decimal"] == 6
assert s["corrected_J2_order4_unique_joint_s3_fixed_proper14_mask_decimal"] == 25
assert s["historical_picard_adjoint_mask6_reused_as_named_J2_source"] is False
assert s["corrected_J2_order4_lift_actual_s3_behavior_source_locked"] is False
assert s["corrected_J2_proper_Br2_14D_coordinate_materialized"] is False
assert s["corrected_J2_retained_10D_domain_coordinate_materialized"] is False
assert s["corrected_J2_named_source_target_relation_materialized"] is False
assert s["finite_v4_kummer_columns_materialized"] == 0
assert s["finite_v4_kummer_named_relation_rank_f2"] == 0

assert c["audit_required"] is False
assert c["audit_status"] == "PASS"
assert c["audit_scope"] == audit["audit_scope"]
assert c["audit_review_id"] == audit["audit_review_id"]
assert c["audit_head_sha"] == audit["audited_head_sha"]
assert c["last_completed_audit_scope"] == audit["audit_scope"]
assert c["last_completed_audit_review_id"] == audit["audit_review_id"]
assert c["last_completed_audit_head_sha"] == audit["audited_head_sha"]
assert c["current_exact_promotion_audit_required"] is False
assert c["advance_allowed"] is True
assert c["advance_scope"] == "STAGE33_12_NAMED_J2_ORDER4_SOURCE_LOCK_CONTINUATION_ONLY"
assert c["next_item"] == gap["next_exact_leaf"]
assert c["next_expected_command"] == "Stage33-main-batch"
assert c["merge_allowed"] is False
assert c["theorem_credit"] is False
assert c["receiver_credit"] is False
assert c["endpoint_credit"] is False
assert c["perfect_cuboid_existence_claim"] is False
assert c["perfect_cuboid_nonexistence_claim"] is False

out = {
    "schema": "STAGE33_MAIN_COMPACT_STATE_V11_V10_AUDIT_PASS_NAMED_ORDER4_SOURCE_GAP",
    "role": "ORDINARY_MAIN_STARTUP_PROJECTION_NOT_A_PROOF_CERTIFICATE",
    "detailed_machine_authority": "stages/stage33/controller.json",
    "controller_schema": c["schema"],
    "stage33_progress": c["stage33_progress"],
    "current": {
        k: q[k]
        for k in [
            "unit",
            "logical_internal_branch",
            "substep",
            "active_missing_interface",
            "next_exact_leaf",
        ]
    },
    "locked_facts": {
        "v10_hostile_audit": {
            "status": audit["status"],
            "review_id": audit["audit_review_id"],
            "audited_head_sha": audit["audited_head_sha"],
            "merge_commit_sha": audit["merge_commit_sha"],
            "sha256": AUDIT_SHA,
        },
        "qpic_marked_picard_bridge": {
            "status": "SOURCE_LOCKED_CERTIFIED_EXACT",
            "raw_bridge_sha256": s["actual_indlist_to_magma_picard_basis_bridge_raw_sha256"],
            "certified_bridge_sha256": s["actual_indlist_to_magma_picard_basis_bridge_certified_sha256"],
            "receipt_sha256": s["qpic_bridge_local_recertification_receipt_sha256"],
        },
        "actual_swap_mixed_discriminant_descent": {
            "status": "MATERIALIZED_EXACT_HOSTILE_AUDITED",
            "moduli": s["actual_swap_mixed_discriminant_moduli"],
            "s3_braid_exact": s["actual_swap_mixed_discriminant_s3_braid_exact"],
            "semantic_u1_fixed_by_both_swaps": True,
            "candidate_count": s["corrected_J2_order4_affine_candidate_count"],
            "unique_joint_fixed_retained10_mask_decimal": 6,
            "unique_joint_fixed_proper14_mask_decimal": 25,
            "named_J2_source_selected": False,
            "sha256": s["actual_swap_mixed_discriminant_descent_certificate_sha256"],
        },
        "post_audit_named_order4_source_gap": {
            "status": gap["status"],
            "minimal_missing_object": gap["minimal_missing_object"]["primary"],
            "targeted_pinned_source_cross_marking_found": gap["targeted_source_audit"]["literal_named_J2_cross_marking_found_in_pinned_cuboids_source"],
            "sha256": GAP_SHA,
        },
        "historical_picard_adjoint_candidate": {
            "mask_decimal": s["historical_picard_adjoint_mask_decimal"],
            "proper14_f2": s["historical_picard_adjoint_proper_Br2_14D_coordinate_f2"],
            "retained10_f2": s["historical_picard_adjoint_retained_10D_domain_coordinate_f2"],
            "authoritative_named_J2_source": False,
            "independently_rederived_as_unique_joint_s3_fixed_candidate": True,
            "sha256": s["historical_picard_adjoint_proper_Br2_certificate_sha256"],
        },
        "named_J2_semantic_orientation": {
            "label": s["corrected_J2_named_semantic_discriminant_label"],
            "marked_Kc_coordinate_f2": s["corrected_J2_named_semantic_discriminant_coordinate_f2"],
            "sha256": s["corrected_J2_named_semantic_discriminant_orientation_certificate_sha256"],
        },
        "named_J2_raw_75D_target": {
            "nonzero": s["corrected_J2_named_V4_H1_target_nonzero"],
            "weight": s["corrected_J2_named_V4_H1_target_coordinate_weight"],
            "sha256": s["corrected_J2_named_V4_H1_target_certificate_sha256"],
        },
    },
    "authority_changes": {
        "v10_hostile_audit": "PASS_PROMOTED_TO_MACHINE_STATE",
        "ordinary_main_gate": "RELEASED_FOR_NAMED_ORDER4_SOURCE_LOCK_CONTINUATION_ONLY",
        "actual_INDLIST_to_historical_Magma_Picard_basis_bridge": "SOURCE_LOCKED_CERTIFIED_EXACT",
        "actual_swap12_swap13_on_mixed_discriminant_basis": "MATERIALIZED_EXACT_HOSTILE_AUDITED",
        "historical_mask6": "UNIQUE_JOINT_S3_FIXED_CANDIDATE_NOT_NAMED_SOURCE",
        "J2_picard_adjoint_named_source_binding": "REVOKED_EXACT_DO_NOT_REVIVE_FROM_HISTORY",
        "J2_named_Kummer_source_target_relation": "REVOKED_EXACT_DO_NOT_USE",
    },
    "resolved_investigations": {
        "qpic_bridge_reacquisition": "CLOSED_EXACT_DO_NOT_REOPEN",
        "retained_smith_substitute_for_qpic": "REJECTED_DO_NOT_REOPEN",
        "geometric_sign_census_for_candidate_selection": "INSUFFICIENT_DO_NOT_REPEAT",
        "actual_s3_candidate_enumeration": "CLOSED_EXACT_DO_NOT_REPEAT",
        "pinned_Verification_exact_name_search_Magma_interface_load_Qtriv": "DONE_NO_MATCH",
    },
    "do_not_use": [
        "historical mask 6 as authoritative named J2 source without a new source-locked lift label",
        "unique S3-fixed candidate implies named J2 unless named order-4 lift S3 behavior is proved",
        "semantic u1 invariance implies named J2 order-4 lift invariance",
        "target compatibility to select the source label",
        "C2+C3=h_J2",
        "mask 742 or 736 as J2 merely from compatibility",
        "A_T[2] coefficients copied directly as proper-Br2 dual coefficients",
        "retained Smith V as the literal 64x64 qPic marking",
    ],
    "open_datum": {
        "named_J2_order4_to_mixed_248_cross_marking_source_locked": False,
        "named_J2_order4_lift_actual_s3_behavior_source_locked": False,
        "named_J2_proper_Br2_source_coordinate_materialized": False,
        "retained10_named_J2_source_coordinate_materialized": False,
        "named_J2_source_target_relation_materialized": False,
        "named_source_target_relation_rank_f2": 0,
        "matrix_standard_columns_materialized": 0,
        "actual_indlist_to_magma_picard_basis_bridge_materialized": True,
        "actual_swap_mixed_discriminant_actions_materialized": True,
    },
    "current_leaf_working_set": [
        "stages/stage33/33-12/v10-hostile-audit-pass-receipt.json",
        "stages/stage33/33-12/j2-named-order4-actual-s3-source-lock-gap-v10.json",
        "stages/stage33/33-12/verify_j2_named_order4_actual_s3_source_lock_gap_v10.py",
        "stages/stage33/33-12/j2-actual-swap-mixed-discriminant-descent.json",
        "stages/stage33/33-12/j2-marked-order4-lift-label-gap.json",
        "stages/stage33/33-12/j2-cv-d2-semantic-orientation.json",
        "stages/stage33/33-12/j2-order4-brauer-lift-reduction.json",
    ],
    "anti_loop_reopen_policy": {
        "ordinary_main_rule": (
            "V10 hostile audit passed the literal qPic bridge and actual mixed-discriminant S3 action. "
            "Do not reacquire qPic, rerun Smith/sign/S3 substitutes, or select mask 6 from symmetry alone. "
            "Proceed only from a genuinely new source-locked named-J2 order-4 cross-marking/direct source row."
        ),
        "reopen_only_if": [
            "the pinned upstream source lock changes",
            "the V10 hostile-audit receipt or exact S3 certificate fails replay",
            "a new source-locked named J2 order-4 cross-marking/direct row becomes available",
            "the user explicitly requests hostile audit or historical revalidation",
        ],
    },
    "execution_gate": {
        "audit_required": c["audit_required"],
        "audit_status": c["audit_status"],
        "audit_scope": c["audit_scope"],
        "audit_review_id": c["audit_review_id"],
        "audit_head_sha": c["audit_head_sha"],
        "last_completed_audit_scope": c["last_completed_audit_scope"],
        "last_completed_audit_review_id": c["last_completed_audit_review_id"],
        "last_completed_audit_head_sha": c["last_completed_audit_head_sha"],
        "advance_allowed": c["advance_allowed"],
        "advance_scope": c["advance_scope"],
        "next_expected_command": c["next_expected_command"],
    },
    "firewalls": {
        "stage33_12_closed_exact": False,
        "stage33_07_reclosed": False,
        "stage33_08_released": False,
        "theorem_credit": False,
        "receiver_credit": False,
        "endpoint_credit": False,
        "perfect_cuboid_existence_claim": False,
        "perfect_cuboid_nonexistence_claim": False,
        "merge_allowed": False,
    },
}
out["canonical_sha256"] = csha(out)
rendered = json.dumps(out, sort_keys=True, separators=(",", ":")) + "\n"

ap = argparse.ArgumentParser()
ap.add_argument("--check", action="store_true")
a = ap.parse_args()
if a.check:
    assert OUT.exists() and OUT.read_text() == rendered, "MAIN-STATE.json is stale; run sync_main_state.py"
    print(json.dumps({"success": True, "mode": "check", "canonical_sha256": out["canonical_sha256"]}, sort_keys=True))
else:
    OUT.write_text(rendered)
    print(json.dumps({"success": True, "mode": "write", "canonical_sha256": out["canonical_sha256"]}, sort_keys=True))
