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
V21_PATH = H / "33-12/j2-order4-swap-functional-source-v21.json"
V21_SHA = "19c464602d6ad1b6c32b0b08c50a6bcc55b8e606642a5ae52e7f51fdc2f12366"
V22_PATH = H / "33-12/j2-kummer-source-target-module-source-first-v22.json"
V22_SHA = "e51a5f13a17cf7c24e789dd4feedf6797db5cfa89486046c9a96692abe96ef2c"
V23_PATH = H / "33-12/j2-kummer-target-h1-coordinate41-trace-v23.json"
V23_SHA = "7718ea63eafa5561bfb2acaf1fb957c9d1767a609036d1a97bee36e9114ed003"
V24_PATH = H / "33-12/j2-raw-h1-not-kummer-target-v24.json"
V24_SHA = "9d104c7d4054b5d92f1df382654b152c30ca0be6ef267aa028fe8b9d78a4687d"
V25_PATH = H / "33-12/j2-genuine-h2-mu2-kummer-adapter-v25.json"
V25_SHA = "d2f8e087939401e3427056d6deeffa5bdb3433ad6e1801993be4978c3baff65c"
V25_AUDIT_PATH = H / "33-12/v25-hostile-audit-pass-receipt.json"
V25_AUDIT_SHA = "444c038d1bbe1396d312d68d7a7cdfb71509db4419fd35839088dfe53c5066da"

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
        assert isinstance(checkpoint.get("current_action"), str) and checkpoint["current_action"]
    return checkpoint


c = json.loads((H / "controller.json").read_text())
v10 = load_canonical(V10_AUDIT_PATH, V10_AUDIT_SHA)
v20audit = load_canonical(V20_AUDIT_PATH, V20_AUDIT_SHA)
v20 = load_canonical(V20_PATH, V20_SHA)
v21 = load_canonical(V21_PATH, V21_SHA)
v22 = load_canonical(V22_PATH, V22_SHA)
v23 = load_canonical(V23_PATH, V23_SHA)
v24 = load_canonical(V24_PATH, V24_SHA)
v25 = load_canonical(V25_PATH, V25_SHA)
v25audit = load_canonical(V25_AUDIT_PATH, V25_AUDIT_SHA)
checkpoint = load_work_checkpoint()
s = c["stage33_12"]
q = c["current"]

assert not RETIRED_HANDOFF.exists(), "MAIN-BATCH-HANDOFF.md is retired; use MAIN-STATE.work_checkpoint"

assert c["schema"] == "STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V59_NAMED_J2_GENUINE_H2_MU2_ADAPTER_MATERIALIZED_PIC2_HS_D2_OPEN"
assert c["stage33_progress"] == "6/11"
assert q["unit"] == "33-12"
assert q["logical_internal_branch"] == "33-13_FINITE_V4_KUMMER_MATRIX_REPAIR"
assert q["substep"] == "MATERIALIZE_ACTUAL_CECH_LOCAL_LATTICES_PIC2_AND_HS_D2"
assert q["active_missing_interface"] == "ACTUAL_CECH_LOCAL_RANK2_LATTICES_OVERLAP_TRANSITIONS_PIC_MOD2_DEFECT_AND_HS_D2_FOR_LAMBDA_D"
assert q["next_exact_leaf"] == c["next_item"] == c["execution"]["next_item"]

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
assert v21["status"] == "PASS_EXACT_SOURCE_FIRST_NAMED_FUNCTIONAL_MATERIALIZED"
assert not any(v21["anti_inference"].values())
assert s["corrected_J2_order4_swap_functional_source_certificate_sha256"] == V21_SHA
assert s["corrected_J2_order4_two_bit_value_source_locked"] is True
assert s["corrected_J2_order4_two_bit_value_f2"] == [0, 1]
assert s["corrected_J2_order4_lift_actual_s3_behavior_source_locked"] is True
assert s["corrected_J2_proper_Br2_14D_coordinate_materialized"] is True
assert s["corrected_J2_proper_Br2_14D_coordinate_f2"] == v21["named_full_surface_source"]["proper14_f2"]
assert s["corrected_J2_retained_10D_domain_coordinate_materialized"] is True
assert s["corrected_J2_retained_10D_domain_coordinate_f2"] == v21["named_full_surface_source"]["retained10_f2"]
assert v22["status"] == "FAIL_EXACT_SOURCE_FIRST_J2_TARGET_UNREACHABLE"
assert v22["locked_named_j2"]["separating_functional_support_1based"] == [41]
assert s["corrected_J2_source_first_v4_compatibility_replay_certificate_sha256"] == V22_SHA
assert s["corrected_J2_source_first_reachable_H1_dimension_f2"] == 13
assert s["corrected_J2_source_first_locked_target_reachable"] is False
assert v23["status"] == "PASS_EXACT_TARGET_ADAPTER_GAP_TRACED_TO_H1_BASIS41"
assert v23["separating_coordinate"]["H1_basis41_raw_pic2_ct_support_1based"] == [9, 11, 19]
assert s["corrected_J2_target_h1_coordinate41_trace_certificate_sha256"] == V23_SHA
assert v24["status"] == "PASS_EXACT_RAW_H1_SCOPE_SEPARATED_FROM_MISSING_KUMMER_ADAPTER"
assert v24["exact_scope_separation"]["raw_cech_H1_may_be_used_as_named_kummer_boundary"] is False
assert s["corrected_J2_raw_h1_not_kummer_target_v24_sha256"] == V24_SHA
assert s["corrected_J2_actual_kummer_target_materialized"] is False
assert s["corrected_J2_named_source_target_relation_materialized"] is False
assert s["finite_v4_kummer_columns_materialized"] == 0
assert s["finite_v4_kummer_named_relation_rank_f2"] == 0
assert v25["status"] == "PASS_EXACT_CURRENT_NAMED_J2_GENUINE_H2_MU2_LIFT_ADAPTER_MATERIALIZED_CONNECTING_COCYCLE_OPEN"
assert v25["current_named_source"]["retained10_mask_decimal"] == 6
assert v25["current_named_source"]["two_bit_value_a_b"] == [0, 1]
assert v25["genuine_h2_mu2_adapter"]["full_surface_named_j2_h2_mu2_lift_materialized"] is True
assert v25["genuine_h2_mu2_adapter"]["historical_kummer_glue_used"] is False
assert v25["genuine_h2_mu2_adapter"]["raw_weight15_h1_used_as_kummer_boundary"] is False
assert v25["remaining_interface"]["standard_kummer_columns_materialized"] == 0
assert v25audit["status"] == "PASS_HOSTILE_AUDIT"
assert v25audit["audit_review_id"] == 5090434903
assert v25audit["audited_head_sha"] == "9a01ec5a5c87782e44f1bffe91cc85e89db25fa1"
assert s["corrected_J2_genuine_h2_mu2_adapter_certificate_sha256"] == V25_SHA
assert s["corrected_J2_v25_hostile_audit_pass_receipt_sha256"] == V25_AUDIT_SHA
assert s["corrected_J2_genuine_full_surface_h2_mu2_lift_materialized"] is True
assert s["corrected_J2_genuine_h2_mu2_adapter_historical_kummer_glue_used"] is False
assert s["corrected_J2_genuine_h2_mu2_adapter_raw_weight15_h1_used_as_kummer_boundary"] is False

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
assert c["advance_scope"] == "STAGE33_12_CECH_PIC2_HS_D2_ONLY"
assert c["next_item"] == q["next_exact_leaf"] == c["execution"]["next_item"]
assert c["next_expected_command"] == "Stage33-main-batch"
assert c["merge_allowed"] is False
assert c["theorem_credit"] is False
assert c["receiver_credit"] is False
assert c["endpoint_credit"] is False
assert c["perfect_cuboid_existence_claim"] is False
assert c["perfect_cuboid_nonexistence_claim"] is False

out = {
    "schema": "STAGE33_MAIN_COMPACT_STATE_V15_NAMED_J2_GENUINE_H2_MU2_ADAPTER_MATERIALIZED_PIC2_HS_D2_OPEN",
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
out["locked_facts"]["order4_two_bit_quotient"]["named_J2_source_selected"] = True
out["locked_facts"]["actual_swap_mixed_discriminant_descent"]["named_J2_source_selected"] = True
out["locked_facts"]["named_J2_order4_functional_source"] = {
    "status": v21["status"],
    "proper14_f2": v21["named_full_surface_source"]["proper14_f2"],
    "proper14_mask_decimal": 25,
    "retained10_f2": v21["named_full_surface_source"]["retained10_f2"],
    "retained10_mask_decimal": 6,
    "two_bit_value_a_b": [0, 1],
    "swap12_fixed": True,
    "swap13_fixed": True,
    "order4_element_itself_claimed_fixed": False,
    "source_first": True,
    "sha256": V21_SHA,
}
out["locked_facts"]["named_J2_source_target_adapter_gap"] = {
    "target_reachable": False,
    "reachable_H1_dimension_f2": 13,
    "separating_H1_support_1based": [41],
    "basis41_raw_pic2_cc_support_1based": [],
    "basis41_raw_pic2_ct_support_1based": [9, 11, 19],
    "source_coordinate_or_label_in_blocker": False,
    "v22_sha256": V22_SHA,
    "v23_sha256": V23_SHA,
}
out["locked_facts"]["raw_H1_scope_firewall"] = {
    "status": v24["status"],
    "raw_weight15_H1_class_exact": True,
    "raw_weight15_H1_authorized_as_named_kummer_target": False,
    "actual_kummer_target_materialized": False,
    "sha256": V24_SHA,
}
out["locked_facts"]["v25_genuine_H2_mu2_adapter"] = {
    "status": v25["status"],
    "audit_review_id": v25audit["audit_review_id"],
    "audited_head_sha": v25audit["audited_head_sha"],
    "named_J2_retained10_mask_decimal": 6,
    "two_bit_value_a_b": [0, 1],
    "full_surface_named_j2_h2_mu2_lift_materialized": True,
    "lift_class": v25["genuine_h2_mu2_adapter"]["kc_lift_class"],
    "old_weight15_target_restored": False,
    "historical_kummer_glue_used": False,
    "standard_kummer_columns_materialized": 0,
    "v25_sha256": V25_SHA,
    "audit_sha256": V25_AUDIT_SHA,
}
out["authority_changes"].update({
    "named_order4_source_gap": "CLOSED_EXACT_SOURCE_FIRST_V21",
    "named_J2_proper_Br2_source_coordinate": "MATERIALIZED_EXACT_SOURCE_FIRST_V21",
    "historical_mask6": "NUMERICALLY_MATCHES_BUT_HISTORICAL_BINDING_NOT_REUSED",
    "J2_named_Kummer_source_target_relation": "REVOKED_RELATION_NOT_RESTORED_TARGET_ADAPTER_REPLAY_REQUIRED",
    "old_weight15_raw_H1_as_named_kummer_target": "REVOKED_SCOPE_V24_RAW_H1_EVIDENCE_RETAINED",
    "genuine_H2_mu2_named_J2_adapter": "PROMOTED_EXACT_HOSTILE_AUDITED_V25",
})
out["resolved_investigations"].update({
    "named_order4_functional_swap_behavior": "CLOSED_EXACT_SOURCE_FIRST_V21",
    "source_first_v4_extension_reachability": "CLOSED_EXACT_FAIL_TARGET_AT_H1_COORDINATE41_V22",
    "target_h1_coordinate41_raw_trace": "CLOSED_EXACT_CT_PIC2_SUPPORT_9_11_19_V23",
    "raw_h1_vs_kummer_target_scope": "CLOSED_EXACT_V24_GENUINE_KUMMER_ADAPTER_MISSING",
    "genuine_h2_mu2_named_j2_adapter": "CLOSED_EXACT_HOSTILE_AUDITED_V25",
})
out["do_not_use"] = [
    "the historical Picard-adjoint certificate as authority for the matching mask 6",
    "semantic u1 invariance as proof that the order-4 element itself is fixed",
    "target compatibility to select or relabel the source",
    "the revoked historical C2+C3=h_J2 relation before exact target-adapter replay",
    "A_T[2] coefficients copied directly as proper-Br2 dual coefficients",
]
out["open_datum"] = {
    "named_J2_order4_two_bit_value_source_locked": True,
    "named_J2_order4_functional_actual_s3_behavior_source_locked": True,
    "named_J2_proper_Br2_source_coordinate_materialized": True,
    "retained10_named_J2_source_coordinate_materialized": True,
    "genuine_H2_mu2_kummer_adapter_materialized": True,
    "genuine_H2_mu2_kummer_adapter_required": False,
    "actual_cech_local_rank2_lattices_materialized": False,
    "pic_mod2_defect_1cocycle_materialized": False,
    "hs_d2_2cocycle_materialized": False,
    "v4_connecting_cocycle_materialized": False,
    "named_J2_source_target_relation_materialized": False,
    "named_source_target_relation_rank_f2": 0,
    "matrix_standard_columns_materialized": 0,
    "target_h1_basis41_adapter_repair_required": False,
}
out["current_leaf_working_set"] = [
    "stages/stage33/33-12/j2-genuine-h2-mu2-kummer-adapter-v25.json",
    "stages/stage33/33-12/verify_j2_genuine_h2_mu2_kummer_adapter_v25.py",
    "stages/stage33/33-12/v25-hostile-audit-pass-receipt.json",
    "stages/stage33/33-12/j2-corrected-explicit-cech-mu2-lift.json",
    "stages/stage33/33-12/j2-full-surface-mu2-zero-defect-contract.json",
    "stages/stage33/33-12/j2-cc-actual-cech-global-square-overlap.json",
    "stages/stage33/33-12/j2-ct-six-kc-support-fullpic64-pullbacks.json",
]
out["anti_loop_reopen_policy"] = {
    "ordinary_main_rule": "V25 hostile-audited promotion fixes the genuine full-surface H2(mu2) lift lambda_D for the exact current named J2. Do not reopen the source, old weight-15 H1 target, C2+C3, or historical Kummer glue. Continue only with actual Cech local lattices/overlaps, marked Pic/2 defect, and HS d2/V4 connecting cocycle.",
    "reopen_only_if": [
        "a pinned V21-V25 source lock or V25 audit receipt fails replay",
        "the exact V21 projection or marked Brauer coordinate changes",
        "the actual Cech compactification/local-lattice convention changes",
        "the user explicitly requests hostile audit or historical revalidation",
    ],
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
