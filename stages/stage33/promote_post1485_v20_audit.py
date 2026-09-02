#!/usr/bin/env python3
"""Promote the hostile-audited #1485 v17-v20 boundary into Stage33 authority."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

H = Path(__file__).resolve().parent
C_PATH = H / "controller.json"
R_PATH = H / "33-12/v20-hostile-audit-pass-receipt.json"
HANDOFF = H / "MAIN-BATCH-HANDOFF.md"

OLD_SCHEMA = "STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V55_V10_AUDIT_PASS_NAMED_ORDER4_SOURCE_GAP"
NEW_SCHEMA = "STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V56_V20_AUDIT_PASS_TWO_BIT_NAMED_ORDER4_GAP"
AUDIT_SCOPE = "STAGE33_12_V17_V20_ORDER4_TWO_BIT_GAP_HOSTILE_AUDIT"
AUDIT_HEAD = "2f3a511f945a22c1df58eaf68553cbb70d4a207c"
AUDIT_REVIEW = 5086169445
MERGE_COMMIT = "dc6b19ea5944c1c249f6d9534a095ffad9ae8f67"
RECEIPT_SHA = "2d65169174d636a93d68f7c2fe4dd1fef322dcd7598459253460631648dd9927"
NEXT = "SOURCE_LOCK_NAMED_J2_ORDER4_LIFT_ACTUAL_SWAP12_SWAP13_BEHAVIOR_OR_EQUIVALENT_TWO_BIT_VALUE_A_B; DO_NOT_SELECT_MASK6_WITHOUT_SOURCE"


def csha(x):
    return hashlib.sha256(
        json.dumps(x, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def canonical(path: Path, expected: str):
    x = json.loads(path.read_text())
    b = dict(x)
    got = b.pop("canonical_sha256")
    assert got == expected == csha(b), path
    return x


def build_receipt():
    return {
        "schema": "STAGE33_V20_HOSTILE_AUDIT_PASS_RECEIPT_V1",
        "stage": "33",
        "status": "PASS_HOSTILE_AUDIT",
        "audit_scope": AUDIT_SCOPE,
        "audit_review_id": AUDIT_REVIEW,
        "audited_pr": 1485,
        "audited_branch": "stage33-post1483-order4-pullback-two-row-extraction",
        "audited_head_sha": AUDIT_HEAD,
        "merged_to_main": True,
        "merge_commit_sha": MERGE_COMMIT,
        "source_locks": {
            "v17_row20_row67_source_lock_sha256": "04b47064db73e02068aa51301c94ab0576d927c0b71b2d3df093012028f061d2",
            "v18_source_coordinate_blocker_sha256": "a0378a7d7191d537347435d11002faa3692f91781dd15f53fe3063443e9d50d1",
            "v19_integral_correction_torsor_sha256": "3ee11e0ecdc855083a4260c2ae4f24ef4c160a7e26a48fd3872369d117118576",
            "v20_named_functional_quotient_sha256": "1b53db254c381721c0c648bab41c276ec79f69f6e1f81235993936df3e25232e",
            "actual_swap_mixed_discriminant_descent_sha256": "93dc99201a04fdec7c8ad8369409e7cb593ae7f8fba44b772df1b2cc1d29cfa3"
        },
        "audit_evidence": {
            "exact_checkpoint_run_id": 33596903107,
            "exact_checkpoint_run_number": 505,
            "v17_v20_all_proof_replay_complete": True,
            "artifact_run_id": 33590282972,
            "artifact_id": 9831504749,
            "artifact_zip_sha256": "b2168e79c62a32498f87aa9d5d1904ca937afee22caabf5db765592a44a61a5d",
            "artifact_payload_canonical_sha256": "9bf2fe321557c3e8c76ab693dbbd6bec055095f4fec95b84b29db61c4f22e9e8"
        },
        "pass_boundary": {
            "rows20_67_source_locked": True,
            "all_required_order4_rows_materialized": True,
            "raw_numerator_divisible_by_2_not_4": True,
            "correction_rank_f2": 50,
            "correction_affine_dimension_f2": 14,
            "correction_count": 16384,
            "distinct_proper14_functionals": 16,
            "preimages_per_functional": 1024,
            "named_column_relevant_quotient_dimension_f2": 2,
            "named_column_candidate_masks_retained10": [4, 5, 6, 7],
            "actual_s3_orbits_retained10": [[6], [4, 5, 7]],
            "named_j2_order4_lift_actual_s3_behavior_source_locked": False,
            "named_j2_source_label_selected": False,
            "named_75d_column_materialized": False,
            "kummer_standard_columns_materialized": 0,
            "stage33_12_closed_exact": False
        },
        "firewall": {
            "unique_joint_s3_fixed_candidate_implies_named_j2": False,
            "semantic_u1_fixed_implies_order4_lift_fixed": False,
            "target_compatibility_may_select_source_label": False,
            "historical_mask6_promoted_as_named_j2": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "merge_allowed_for_continuation_pr": False
        },
        "next_exact_leaf": NEXT
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--continuation-pr", type=int, default=1488)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()

    canonical(H / "33-12/j2-order4-row20-row67-exact-source-lock-v17.json",
              "04b47064db73e02068aa51301c94ab0576d927c0b71b2d3df093012028f061d2")
    canonical(H / "33-12/j2-order4-source-coordinate-v18.json",
              "a0378a7d7191d537347435d11002faa3692f91781dd15f53fe3063443e9d50d1")
    canonical(H / "33-12/j2-order4-integral-correction-torsor-v19.json",
              "3ee11e0ecdc855083a4260c2ae4f24ef4c160a7e26a48fd3872369d117118576")
    canonical(H / "33-12/j2-order4-named-functional-quotient-v20.json",
              "1b53db254c381721c0c648bab41c276ec79f69f6e1f81235993936df3e25232e")

    receipt = build_receipt()
    assert csha(receipt) == RECEIPT_SHA
    receipt_out = dict(receipt)
    receipt_out["canonical_sha256"] = RECEIPT_SHA
    receipt_text = json.dumps(receipt_out, indent=2, sort_keys=True) + "\n"

    c = json.loads(C_PATH.read_text())
    if c["schema"] == OLD_SCHEMA:
        assert c["stage33_progress"] == "6/11"
        assert c["stage33_12"]["finite_v4_kummer_columns_materialized"] == 0
        assert c["stage33_12"]["corrected_J2_proper_Br2_14D_coordinate_materialized"] is False
        assert c["stage33_12"]["corrected_J2_order4_lift_actual_s3_behavior_source_locked"] is False
    else:
        assert c["schema"] == NEW_SCHEMA

    s = c["stage33_12"]
    q = c["current"]

    c["schema"] = NEW_SCHEMA
    c["audit_required"] = False
    c["audit_status"] = "PASS"
    c["audit_scope"] = AUDIT_SCOPE
    c["audit_review_id"] = AUDIT_REVIEW
    c["audit_head_sha"] = AUDIT_HEAD
    c["last_completed_audit_scope"] = AUDIT_SCOPE
    c["last_completed_audit_review_id"] = AUDIT_REVIEW
    c["last_completed_audit_head_sha"] = AUDIT_HEAD
    c["current_exact_promotion_audit_required"] = False
    c["current_exact_promotion_scope"] = "V17_V20_HOSTILE_AUDIT_PASS_PROMOTED_TWO_BIT_GAP_ONLY_NO_NAMED_LABEL_NO_COLUMN"
    c["advance_allowed"] = True
    c["advance_scope"] = "STAGE33_12_NAMED_J2_ORDER4_TWO_BIT_SOURCE_LOCK_CONTINUATION_ONLY"
    c["next_item"] = NEXT
    c["next_expected_command"] = "Stage33-main-batch"
    c["merge_allowed"] = False

    c["execution"].update({
        "audit_required": False,
        "audit_status": "PASS",
        "audit_scope": AUDIT_SCOPE,
        "audit_review_id": AUDIT_REVIEW,
        "audit_head_sha": AUDIT_HEAD,
        "advance_allowed": True,
        "advance_scope": c["advance_scope"],
        "next_item": NEXT,
        "next_expected_command": "Stage33-main-batch",
        "heavy_actions_authorized": False,
        "merge_allowed": False
    })

    q.update({
        "unit": "33-12",
        "logical_internal_branch": "33-13_FINITE_V4_KUMMER_MATRIX_REPAIR",
        "substep": "SOURCE_LOCK_NAMED_J2_ORDER4_TWO_BIT_ACTUAL_SWAP_BEHAVIOR",
        "active_missing_interface": "SOURCE_LOCKED_NAMED_J2_ORDER4_LIFT_TWO_BIT_QUOTIENT_VALUE_OR_ACTUAL_SWAP_IMAGES_MISSING",
        "next_exact_leaf": NEXT,
        "status": "CURRENT"
    })

    c["loop_state"].update({
        "last_cycle_route_status": "V20_AUDIT_PASS_TWO_BIT_NAMED_ORDER4_SOURCE_GAP",
        "last_new_view": (
            "#1485 hostile audit promoted the exact v17-v20 chain. All required source rows are locked; "
            "the integral correction torsor is 14D but its named-column image is exactly a two-bit affine plane "
            "[4,5,6,7]. The only unresolved source datum is the named order-4 lift's actual swap12/swap13 behavior "
            "or equivalent two-bit value; mask 6 is not selected."
        ),
        "stagnation_count": 0
    })

    c["pending_audit_boundary"] = {
        "status": "PASS_COMPLETED",
        "scope": AUDIT_SCOPE,
        "target": "PR_1485_HEAD_2F3A511F_HOSTILE_AUDITED_AND_MERGED",
        "continuation_pr": a.continuation_pr,
        "new_pr_before_pass": False,
        "new_pr_after_pass": True,
        "ordinary_main_forbidden_until_pass": False,
        "mathematical_leaf_extension_in_this_repair": True
    }

    s.update({
        "v20_hostile_audit_pass_receipt": "stages/stage33/33-12/v20-hostile-audit-pass-receipt.json",
        "v20_hostile_audit_pass_receipt_sha256": RECEIPT_SHA,
        "corrected_J2_order4_rows20_67_source_lock_certificate": "stages/stage33/33-12/j2-order4-row20-row67-exact-source-lock-v17.json",
        "corrected_J2_order4_rows20_67_source_lock_sha256": "04b47064db73e02068aa51301c94ab0576d927c0b71b2d3df093012028f061d2",
        "corrected_J2_order4_source_coordinate_v18_certificate": "stages/stage33/33-12/j2-order4-source-coordinate-v18.json",
        "corrected_J2_order4_source_coordinate_v18_sha256": "a0378a7d7191d537347435d11002faa3692f91781dd15f53fe3063443e9d50d1",
        "corrected_J2_order4_integral_correction_torsor_v19_certificate": "stages/stage33/33-12/j2-order4-integral-correction-torsor-v19.json",
        "corrected_J2_order4_integral_correction_torsor_v19_sha256": "3ee11e0ecdc855083a4260c2ae4f24ef4c160a7e26a48fd3872369d117118576",
        "corrected_J2_order4_named_functional_quotient_v20_certificate": "stages/stage33/33-12/j2-order4-named-functional-quotient-v20.json",
        "corrected_J2_order4_named_functional_quotient_v20_sha256": "1b53db254c381721c0c648bab41c276ec79f69f6e1f81235993936df3e25232e",
        "corrected_J2_order4_missing_BigK_pullback_rows_1based": [],
        "corrected_J2_order4_candidate_dual_normalization": (
            "raw n4 has even but not mod4-zero Gram pairings; solve (n4+2r)G_S=0 mod4. "
            "Each integral corrected order-4 lift gives a proper14 functional. After cc/ct invariance, "
            "the named-column image is the exact two-bit affine plane (a,b,1,0,0,0,0,0,0,0)."
        ),
        "corrected_J2_order4_correction_rank_f2": 50,
        "corrected_J2_order4_correction_torsor_dimension_f2": 14,
        "corrected_J2_order4_correction_count": 16384,
        "corrected_J2_order4_distinct_proper14_functionals": 16,
        "corrected_J2_order4_preimages_per_proper14_functional": 1024,
        "corrected_J2_order4_named_column_relevant_quotient_dimension_f2": 2,
        "corrected_J2_order4_named_column_relevant_masks_retained10": [4, 5, 6, 7],
        "corrected_J2_order4_named_column_relevant_s3_orbits": [[6], [4, 5, 7]],
        "corrected_J2_order4_two_bit_value_source_locked": False,
        "corrected_J2_order4_route_status": "AUDITED_TWO_BIT_NAMED_LIFT_SWAP_SOURCE_GAP",
        "minimal_missing_exact_datum": "SOURCE_LOCKED_NAMED_J2_ORDER4_LIFT_TWO_BIT_VALUE_A_B_OR_ACTUAL_SWAP12_SWAP13_BEHAVIOR",
        "status": "OPEN_CURRENT_V20_AUDITED_TWO_BIT_SOURCE_GAP"
    })

    for item in s.get("logical_internal_sequence", []):
        if item.get("id") == "33-13":
            item["status"] = "CURRENT_V20_AUDITED_TWO_BIT_NAMED_ORDER4_GAP_STANDARD_COLUMNS_0_OF_10"

    assert c["stage33_progress"] == "6/11"
    assert s["finite_v4_kummer_columns_materialized"] == 0
    assert s["finite_v4_kummer_named_relation_rank_f2"] == 0
    assert s["corrected_J2_proper_Br2_14D_coordinate_materialized"] is False
    assert s["corrected_J2_retained_10D_domain_coordinate_materialized"] is False
    assert s["corrected_J2_named_source_target_relation_materialized"] is False
    assert s["corrected_J2_order4_lift_actual_s3_behavior_source_locked"] is False
    assert s["corrected_J2_order4_two_bit_value_source_locked"] is False
    assert s["closed_exact"] is False
    assert c["release_gates"]["stage33_12_closed_exact"] is False
    assert c["release_gates"]["stage33_07_reclosed"] is False
    assert c["release_gates"]["stage33_08_released"] is False
    assert c["theorem_credit"] is False
    assert c["receiver_credit"] is False
    assert c["endpoint_credit"] is False
    assert c["perfect_cuboid_existence_claim"] is False
    assert c["perfect_cuboid_nonexistence_claim"] is False
    assert c["merge_allowed"] is False

    controller_text = json.dumps(c, sort_keys=True, separators=(",", ":")) + "\n"
    handoff_text = "# Stage33 MAIN batch handoff\n\nstatus: EMPTY\n"

    if a.check:
        assert R_PATH.exists() and R_PATH.read_text() == receipt_text
        assert C_PATH.read_text() == controller_text
        assert HANDOFF.read_text() == handoff_text
        print(json.dumps({"success": True, "mode": "check", "receipt_sha256": RECEIPT_SHA}, sort_keys=True))
        return

    R_PATH.write_text(receipt_text)
    C_PATH.write_text(controller_text)
    HANDOFF.write_text(handoff_text)
    print(json.dumps({"success": True, "mode": "write", "receipt_sha256": RECEIPT_SHA}, sort_keys=True))


if __name__ == "__main__":
    main()
