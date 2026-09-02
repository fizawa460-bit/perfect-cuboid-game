#!/usr/bin/env python3
"""Build/check compact Stage33 MAIN state while preserving one operational checkpoint."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

H = Path(__file__).resolve().parent
OUT = H / "MAIN-STATE.json"
RETIRED_HANDOFF = H / "MAIN-BATCH-HANDOFF.md"

V10_AUDIT_PATH = H / "33-12/v10-hostile-audit-pass-receipt.json"
V10_AUDIT_SHA = "5bef940bf55dd480acb8fc3a75415470d28ee9eaa1473c3476d8bd6463ca89e1"
V20_AUDIT_PATH = H / "33-12/v20-hostile-audit-pass-receipt.json"
V20_AUDIT_SHA = "2d65169174d636a93d68f7c2fe4dd1fef322dcd7598459253460631648dd9927"
V20_PATH = H / "33-12/j2-order4-named-functional-quotient-v20.json"
V20_SHA = "1b53db254c381721c0c648bab41c276ec79f69f6e1f81235993936df3e25232e"

EMPTY_CHECKPOINT = {
    "status": "EMPTY",
    "authority": "OPERATIONAL_ONLY_NOT_PROOF",
}


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


def load_work_checkpoint():
    if not OUT.exists():
        return dict(EMPTY_CHECKPOINT)
    current = json.loads(OUT.read_text())
    checkpoint = current.get("work_checkpoint", EMPTY_CHECKPOINT)
    assert isinstance(checkpoint, dict)
    assert checkpoint.get("authority") == "OPERATIONAL_ONLY_NOT_PROOF"
    assert checkpoint.get("status") in {"EMPTY", "ACTIVE_UNPROMOTED"}
    if checkpoint["status"] == "EMPTY":
        assert checkpoint == EMPTY_CHECKPOINT
    else:
        assert isinstance(checkpoint.get("observations"), list) and checkpoint["observations"]
        assert isinstance(checkpoint.get("anti_repeat"), list)
        assert isinstance(checkpoint.get("next_action"), str) and checkpoint["next_action"]
    return checkpoint


c = json.loads((H / "controller.json").read_text())
v10 = load_canonical(V10_AUDIT_PATH, V10_AUDIT_SHA)
v20audit = load_canonical(V20_AUDIT_PATH, V20_AUDIT_SHA)
v20 = load_canonical(V20_PATH, V20_SHA)
checkpoint = load_work_checkpoint()
s = c["stage33_12"]
q = c["current"]

assert not RETIRED_HANDOFF.exists(), "MAIN-BATCH-HANDOFF.md is retired; use MAIN-STATE.work_checkpoint"

assert c["schema"] == "STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V56_V20_AUDIT_PASS_TWO_BIT_NAMED_ORDER4_GAP"
assert c["stage33_progress"] == "6/11"
assert q["unit"] == "33-12"
assert q["logical_internal_branch"] == "33-13_FINITE_V4_KUMMER_MATRIX_REPAIR"
assert q["substep"] == "SOURCE_LOCK_NAMED_J2_ORDER4_TWO_BIT_ACTUAL_SWAP_BEHAVIOR"
assert q["active_missing_interface"] == "SOURCE_LOCKED_NAMED_J2_ORDER4_LIFT_TWO_BIT_QUOTIENT_VALUE_OR_ACTUAL_SWAP_IMAGES_MISSING"
assert q["next_exact_leaf"] == v20audit["next_exact_leaf"]

assert v10["status"] == "PASS_HOSTILE_AUDIT"
assert v20audit["status"] == "PASS_HOSTILE_AUDIT"
assert v20audit["audit_review_id"] == 5086169445
assert v20audit["audited_pr"] == 1485
assert v20audit["audited_head_sha"] == "2f3a511f945a22c1df58eaf68553cbb70d4a207c"
assert v20audit["merge_commit_sha"] == "dc6b19ea5944c1c249f6d9534a095ffad9ae8f67"
assert v20audit["pass_boundary"]["named_column_relevant_quotient_dimension_f2"] == 2
assert v20audit["pass_boundary"]["named_column_candidate_masks_retained10"] == [4, 5, 6, 7]
assert v20audit["pass_boundary"]["actual_s3_orbits_retained10"] == [[6], [4, 5, 7]]
assert v20audit["pass_boundary"]["named_j2_source_label_selected"] is False
assert v20audit["pass_boundary"]["named_75d_column_materialized"] is False
assert v20audit["pass_boundary"]["kummer_standard_columns_materialized"] == 0

assert v20["status"] == "PASS_EXACT_NAMED_COLUMN_GAP_REDUCED_TO_TWO_BITS"
assert v20["exact_quotient"]["named_column_relevant_quotient_dimension_f2"] == 2
assert [x["retained10_mask_decimal"] for x in v20["exact_quotient"]["affine_plane_records"]] == [4, 5, 6, 7]
assert v20["actual_s3_action_on_two_bit_quotient"]["orbits"] == [[6], [4, 5, 7]]
assert v20["actual_s3_action_on_two_bit_quotient"]["named_mask_selected"] is False

assert s["v20_hostile_audit_pass_receipt_sha256"] == V20_AUDIT_SHA
assert s["corrected_J2_order4_rows20_67_source_lock_sha256"] == "04b47064db73e02068aa51301c94ab0576d927c0b71b2d3df093012028f061d2"
assert s["corrected_J2_order4_source_coordinate_v18_sha256"] == "a0378a7d7191d537347435d11002faa3692f91781dd15f53fe3063443e9d50d1"
assert s["corrected_J2_order4_integral_correction_torsor_v19_sha256"] == "3ee11e0ecdc855083a4260c2ae4f24ef4c160a7e26a48fd3872369d117118576"
assert s["corrected_J2_order4_named_functional_quotient_v20_sha256"] == V20_SHA
assert s["corrected_J2_order4_missing_BigK_pullback_rows_1based"] == []
assert s["corrected_J2_order4_correction_torsor_dimension_f2"] == 14
assert s["corrected_J2_order4_correction_count"] == 16384
assert s["corrected_J2_order4_distinct_proper14_functionals"] == 16
assert s["corrected_J2_order4_preimages_per_proper14_functional"] == 1024
assert s["corrected_J2_order4_named_column_relevant_quotient_dimension_f2"] == 2
assert s["corrected_J2_order4_named_column_relevant_masks_retained10"] == [4, 5, 6, 7]
assert s["corrected_J2_order4_named_column_relevant_s3_orbits"] == [[6], [4, 5, 7]]
assert s["corrected_J2_order4_two_bit_value_source_locked"] is False
assert s["corrected_J2_order4_lift_actual_s3_behavior_source_locked"] is False
assert s["corrected_J2_proper_Br2_14D_coordinate_materialized"] is False
assert s["corrected_J2_retained_10D_domain_coordinate_materialized"] is False
assert s["corrected_J2_named_source_target_relation_materialized"] is False
assert s["finite_v4_kummer_columns_materialized"] == 0
assert s["finite_v4_kummer_named_relation_rank_f2"] == 0

assert c["audit_required"] is False
assert c["audit_status"] == "PASS"
assert c["audit_scope"] == v20audit["audit_scope"]
assert c["audit_review_id"] == v20audit["audit_review_id"]
assert c["audit_head_sha"] == v20audit["audited_head_sha"]
assert c["last_completed_audit_scope"] == v20audit["audit_scope"]
assert c["last_completed_audit_review_id"] == v20audit["audit_review_id"]
assert c["last_completed_audit_head_sha"] == v20audit["audited_head_sha"]
assert c["current_exact_promotion_audit_required"] is False
assert c["advance_allowed"] is True
assert c["advance_scope"] == "STAGE33_12_NAMED_J2_ORDER4_TWO_BIT_SOURCE_LOCK_CONTINUATION_ONLY"
assert c["next_item"] == v20audit["next_exact_leaf"]
assert c["next_expected_command"] == "Stage33-main-batch"
assert c["merge_allowed"] is False
assert c["theorem_credit"] is False
assert c["receiver_credit"] is False
assert c["endpoint_credit"] is False
assert c["perfect_cuboid_existence_claim"] is False
assert c["perfect_cuboid_nonexistence_claim"] is False

out = {
    "schema": "STAGE33_MAIN_COMPACT_STATE_V12_V20_AUDIT_PASS_TWO_BIT_NAMED_ORDER4_GAP",
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
            "status": v10["status"],
            "review_id": v10["audit_review_id"],
            "audited_head_sha": v10["audited_head_sha"],
            "merge_commit_sha": v10["merge_commit_sha"],
            "sha256": V10_AUDIT_SHA,
        },
        "v20_hostile_audit": {
            "status": v20audit["status"],
            "review_id": v20audit["audit_review_id"],
            "audited_pr": v20audit["audited_pr"],
            "audited_head_sha": v20audit["audited_head_sha"],
            "merge_commit_sha": v20audit["merge_commit_sha"],
            "sha256": V20_AUDIT_SHA,
        },
        "order4_two_bit_quotient": {
            "status": "HOSTILE_AUDITED_EXACT",
            "correction_torsor_dimension_f2": s["corrected_J2_order4_correction_torsor_dimension_f2"],
            "correction_count": s["corrected_J2_order4_correction_count"],
            "distinct_proper14_functionals": s["corrected_J2_order4_distinct_proper14_functionals"],
            "preimages_per_proper14_functional": s["corrected_J2_order4_preimages_per_proper14_functional"],
            "named_column_relevant_quotient_dimension_f2": s["corrected_J2_order4_named_column_relevant_quotient_dimension_f2"],
            "candidate_masks_retained10": s["corrected_J2_order4_named_column_relevant_masks_retained10"],
            "actual_s3_orbits_retained10": s["corrected_J2_order4_named_column_relevant_s3_orbits"],
            "unique_joint_fixed_retained10_mask_decimal": 6,
            "named_J2_source_selected": False,
            "sha256": V20_SHA,
        },
        "qpic_marked_picard_bridge": {
            "status": "SOURCE_LOCKED_CERTIFIED_EXACT",
            "certified_bridge_sha256": s["actual_indlist_to_magma_picard_basis_bridge_certified_sha256"],
        },
        "actual_swap_mixed_discriminant_descent": {
            "status": "MATERIALIZED_EXACT_HOSTILE_AUDITED",
            "candidate_count": 4,
            "unique_joint_fixed_retained10_mask_decimal": 6,
            "named_J2_source_selected": False,
            "sha256": s["actual_swap_mixed_discriminant_descent_certificate_sha256"],
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
        "v20_v17_v20_chain": "PASS_PROMOTED_TO_MACHINE_STATE",
        "named_order4_source_gap": "REDUCED_FROM_14_BIT_CORRECTION_SELECTOR_TO_TWO_BIT_QUOTIENT",
        "ordinary_main_gate": "RELEASED_FOR_NAMED_ORDER4_TWO_BIT_SOURCE_LOCK_CONTINUATION_ONLY",
        "historical_mask6": "UNIQUE_JOINT_S3_FIXED_CANDIDATE_NOT_NAMED_SOURCE",
        "J2_named_Kummer_source_target_relation": "REVOKED_EXACT_DO_NOT_USE",
    },
    "resolved_investigations": {
        "rows20_67_reacquisition": "CLOSED_EXACT_DO_NOT_REPEAT",
        "order4_correction_half_lift_enumeration": "CLOSED_EXACT_DO_NOT_REPEAT",
        "qpic_bridge_reacquisition": "CLOSED_EXACT_DO_NOT_REOPEN",
        "retained_smith_substitute_for_qpic": "REJECTED_DO_NOT_REOPEN",
        "geometric_sign_census_for_candidate_selection": "INSUFFICIENT_DO_NOT_REPEAT",
        "actual_s3_candidate_enumeration": "CLOSED_EXACT_DO_NOT_REPEAT",
    },
    "do_not_use": [
        "historical mask 6 as authoritative named J2 source without a new source-locked named order-4 lift action",
        "unique S3-fixed candidate implies named J2 unless named order-4 lift S3 behavior is proved",
        "semantic u1 invariance implies named J2 order-4 lift invariance",
        "target compatibility to select the source label",
        "C2+C3=h_J2",
        "mask 742 or 736 as J2 merely from compatibility",
        "A_T[2] coefficients copied directly as proper-Br2 dual coefficients",
        "the ten invisible correction-fiber bits as a reason to reopen the v19 enumeration",
    ],
    "open_datum": {
        "named_J2_order4_two_bit_value_source_locked": False,
        "named_J2_order4_lift_actual_s3_behavior_source_locked": False,
        "named_J2_proper_Br2_source_coordinate_materialized": False,
        "retained10_named_J2_source_coordinate_materialized": False,
        "named_J2_source_target_relation_materialized": False,
        "named_source_target_relation_rank_f2": 0,
        "matrix_standard_columns_materialized": 0,
    },
    "current_leaf_working_set": [
        "stages/stage33/33-12/v20-hostile-audit-pass-receipt.json",
        "stages/stage33/33-12/j2-order4-named-functional-quotient-v20.json",
        "stages/stage33/33-12/verify_j2_order4_named_functional_quotient_v20.py",
        "stages/stage33/33-12/j2-actual-swap-mixed-discriminant-descent.json",
        "stages/stage33/33-12/j2-marked-order4-lift-label-gap.json",
        "stages/stage33/33-12/j2-cv-d2-semantic-orientation.json",
        "stages/stage33/33-12/j2-order4-brauer-lift-reduction.json",
    ],
    "anti_loop_reopen_policy": {
        "ordinary_main_rule": (
            "The #1485 hostile audit promoted the v17-v20 exact chain and reduced the named-column gap to two bits. "
            "Do not reacquire source rows, rerun the correction/half-lift enumeration, reopen qPic/Smith/sign/S3 substitutes, "
            "or select mask 6 from symmetry alone. Proceed only from a genuinely source-locked named J2 order-4 lift "
            "swap12/swap13 behavior or equivalent two-bit value."
        ),
        "reopen_only_if": [
            "a promoted v17-v20 source lock or the #1485 audit receipt fails replay",
            "the pinned upstream source lock changes",
            "a new exact adapter materially changes the named order-4 lift semantics",
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
    "work_checkpoint": checkpoint,
}
out["canonical_sha256"] = csha(out)
rendered = json.dumps(out, sort_keys=True, separators=(",", ":")) + "\n"

ap = argparse.ArgumentParser()
ap.add_argument("--check", action="store_true")
a = ap.parse_args()
if a.check:
    assert OUT.exists() and OUT.read_text() == rendered, "MAIN-STATE.json is stale; run sync_main_state.py"
    print(json.dumps({
        "success": True,
        "mode": "check",
        "canonical_sha256": out["canonical_sha256"],
        "work_checkpoint_status": checkpoint["status"],
    }, sort_keys=True))
else:
    OUT.write_text(rendered)
    print(json.dumps({
        "success": True,
        "mode": "write",
        "canonical_sha256": out["canonical_sha256"],
        "work_checkpoint_status": checkpoint["status"],
    }, sort_keys=True))
