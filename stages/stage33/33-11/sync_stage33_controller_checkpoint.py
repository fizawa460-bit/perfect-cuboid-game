#!/usr/bin/env python3
"""Synchronize the Stage33 controller to the exact Stage33-11 MAIN checkpoint.

Stage33-11 remains open with 0/26 named connecting columns materialized.  The
current exact checkpoint is the A2_26 smallest-block reduction: its finite-H1
value lies in a five-dimensional naturality envelope, and simultaneous cc/ct
restriction is injective there.  A deterministic five-bit quotient decoder is
materialized before this controller sync.  Parent/downstream firewalls remain
closed.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CTRL = ROOT / "stages" / "stage33" / "controller.json"
HERE = ROOT / "stages" / "stage33" / "33-11"
PROFILE = HERE / "stage33-11-smallest-block-target-images.json"
DECODER = HERE / "stage33-11-a2-26-restriction-decoder.json"
EXPECTED_PROFILE_SHA = "45e42d6f3577654df7a4126cad5e2eee651c38fdce3c5cf8289b5f96707f2edc"

profile = json.loads(PROFILE.read_text(encoding="utf-8"))
decoder = json.loads(DECODER.read_text(encoding="utf-8"))
if profile.get("canonical_sha256") != EXPECTED_PROFILE_SHA:
    raise SystemExit("Stage33-11c target-image profile source lock moved")
if decoder.get("schema") != "STAGE33_11_A2_26_CC_CT_RESTRICTION_DECODER_V1":
    raise SystemExit("Stage33-11c decoder schema moved")
if decoder["source_locks"].get("stage33_11_smallest_block_target_profile_sha256") != EXPECTED_PROFILE_SHA:
    raise SystemExit("Stage33-11c decoder no longer locks the target-image profile")
if not decoder["decoder"].get("all_32_coefficient_vectors_roundtrip_verified"):
    raise SystemExit("Stage33-11c decoder exhaustive roundtrip check missing")
if decoder["decoder"].get("joint_restriction_rank_on_allowed_space_f2") != 5:
    raise SystemExit("Stage33-11c A2_26 joint restriction rank moved")
if decoder["exact_consequence"].get("a2_26_connecting_column_materialized"):
    raise SystemExit("controller sync refuses an unreviewed A2_26 closure promotion")

c = json.loads(CTRL.read_text(encoding="utf-8"))

c["status"] = "STAGE33_01_TO_06_AUDITED_CLOSED_33_07_REPAIR_33_09_33_10_CLOSED_33_11_RUNNING_33_08_BLOCKED"

boot = c["main_batch_bootstrap_read_policy"]
boot["current_repair_child"] = "33-11"
boot["current_roadmap_section"] = "Stage33-11 — ARITHMETIC-LOCALIZATION-CONNECTING-MAP"
boot["immediate_predecessor_handoff"] = "stages/stage33/33-10/handoff.json"
boot["immediate_predecessor_required_status"] = "CLOSED_EXACT"
boot["current_child_required_input_certificate_ids"] = [
    "STAGE33_09_MARKED_PICARD_BRIDGE",
    "STAGE33_10_ABSOLUTE_H1_RECEIVER",
    "PROPER_GEOMETRIC_BR2_V4_MODULE_ACTION_CERTIFICATE",
    "FINITE_V4_H1_PROPER_BR2_CERTIFICATE_DIM16",
]

s7 = c["stage33_07"]
s7["stage33_10_main_evidence_status"] = "CLOSED_EXACT_HOSTILE_AUDIT_PASS"
s7["absolute_h1_receiver_exact_authoritative"] = True
s7["stage33_11_domain_and_codomain_released"] = True
s7["arithmetic_localization_connecting_map_computed"] = False
s7["connecting_matrix_columns_explicitly_materialized"] = 0
s7["arithmetic_hs_d2_computed"] = False

children = {x["id"]: x for x in c["repair_children"]}
s10 = children["33-10"]
s10["status"] = "CLOSED_EXACT_HOSTILE_AUDIT_PASS"
s10["audit_required"] = True
s10["audit_passed"] = True
s10["downstream_released"] = True
s10["hostile_audit_pr_review_verdict"] = "PASS_STAGE33_10_ABSOLUTE_H1_AND_GALOIS_DESCENT_ADAPTER"
s10["hostile_audit_review_submitted_at"] = "2026-08-28T04:50:42Z"
for b in s10.get("branches", []):
    if b.get("id") == "33-10e":
        b["main_status"] = "CLOSED_EXACT_HOSTILE_AUDIT_PASS"

s11 = children["33-11"]
s11["status"] = "RUNNING"
s11["pr"] = 1449
s11["prerequisites_satisfied"] = True
s11.pop("blocked_by", None)
s11["source_direction_exact_now"] = 0
s11["connecting_columns_explicitly_materialized"] = 0
s11["remote_magma_required_on_current_hot_path"] = False
s11["stage33_11a_global_naturality"] = {
    "status": "CLOSED_EXACT_NEGATIVE_ROUTE_RESULT",
    "Hom_H_A_to_K_dimension_f2": 24,
    "Hom_H_A_to_finite_H1_dimension_f2": 33,
    "global_naturality_alone_forces_zero": False,
    "certificate_sha256": "612b4e0c3a4f9a17d1ad079fa5a03987a9253aa2f30c315e85d97d25b60ffcbd",
}
s11["stage33_11b_symmetry_block_profile"] = {
    "status": "CLOSED_EXACT_PROFILE_NO_NAMED_COLUMN_CLOSURE",
    "universal_kernel_to_K_dimension_f2": 10,
    "universal_kernel_to_finite_H1_dimension_f2": 14,
    "common_universal_kernel_dimension_f2": 10,
    "named_basis_directions_forced_zero": [],
    "distinct_named_cyclic_source_submodules": 12,
    "certificate_sha256": "6856ec7defea97732ea443d351d9283ef19e386e13c4c8b90a0d1545bd135390",
    "workflow_run": 33155495938,
}
s11["stage33_11c_a2_26_reduction"] = {
    "status": "RUNNING_EXACT_FIVE_BIT_RESTRICTION_DECODER_READY",
    "smallest_cyclic_blocks_1based": [[2], [3], [24, 25, 26]],
    "raw_order2_liftable_smallest_directions_1based": [2, 3, 24, 25, 26],
    "target_image_profile_sha256": EXPECTED_PROFILE_SHA,
    "a2_26_shape": "K2,2_FOUR_CYCLE",
    "a2_26_edges": ["X_0125", "X_0126", "X_0131", "X_0132"],
    "a2_26_K_allowed_value_dimension_f2": 3,
    "a2_26_finite_H1_allowed_value_dimension_f2": 5,
    "a2_26_cc_restriction_rank_f2": 3,
    "a2_26_ct_restriction_rank_f2": 2,
    "a2_26_joint_cc_ct_restriction_rank_f2": 5,
    "a2_26_joint_cc_ct_restriction_kernel_dimension_f2": 0,
    "a2_26_five_quotient_bits_determine_finite_H1_value": True,
    "decoder_certificate_sha256": decoder["canonical_sha256"],
    "decoder_observation_coordinates": decoder["decoder"]["canonical_observation_coordinates"],
    "all_32_decoder_roundtrips_verified": True,
    "connecting_column_materialized": False,
    "next_exact_task": "A2_26_EXPLICIT_CC_CT_GERSTEN_GALOIS_DIFFERENCE_BITS",
}
for b in s11["branches"]:
    if b["id"] == "33-11a":
        b["main_status"] = "CLOSED_EXACT_NEGATIVE_ROUTE_RESULT_HOM_DIMS_24_33"
    elif b["id"] == "33-11b":
        b["main_status"] = "CLOSED_EXACT_PROFILE_COMMON_KERNEL_DIM10_NO_NAMED_COLUMN_FORCED"
    elif b["id"] == "33-11c":
        b["main_status"] = "RUNNING_A2_26_FIVE_BIT_RESTRICTION_DECODER_READY"
        b["smallest_cyclic_blocks_1based"] = [[2], [3], [24, 25, 26]]
        b["preferred_next_pointer"] = "component-A2_26"

s12 = children["33-12"]
s12["status"] = "BLOCKED_PENDING_33_11_COMPLETE_EXACT_COVERAGE"
s12["prerequisites_satisfied"] = False
s12["blocked_by"] = "33-11_OPEN_0_OF_26_NAMED_CONNECTING_COLUMNS"

c["current_item"] = "Stage33-11_ARITHMETIC_LOCALIZATION_CONNECTING_MAP_RUNNING"
c["audit_required"] = False
c["merge_allowed"] = False
c["advance_allowed"] = True
c["advance_scope"] = "STAGE33_11_ONLY_ADVANCE_A2_26_EXPLICIT_CC_CT_BITS_KEEP_33_12_33_08_33_40_BLOCKED"
c["next_item"] = "Stage33-11c_A2_26_EXPLICIT_CC_CT_GERSTEN_DIFFERENCE_BITS"
c["next_expected_command"] = "Stage33-main-batch"

c["controller_writeback_checkpoint"] = {
    "pr": 1449,
    "stage33_10_hostile_audit_pass": True,
    "stage33_11_status": "RUNNING",
    "stage33_11a_Hom_A_K_dimension_f2": 24,
    "stage33_11a_Hom_A_finite_H1_dimension_f2": 33,
    "stage33_11b_common_universal_kernel_dimension_f2": 10,
    "stage33_11b_named_directions_forced_zero": [],
    "stage33_11c_target_profile_sha256": EXPECTED_PROFILE_SHA,
    "stage33_11c_a2_26_K_allowed_dimension_f2": 3,
    "stage33_11c_a2_26_finite_H1_allowed_dimension_f2": 5,
    "stage33_11c_a2_26_joint_cc_ct_restriction_kernel_dimension_f2": 0,
    "stage33_11c_a2_26_decoder_sha256": decoder["canonical_sha256"],
    "stage33_11c_a2_26_five_bit_decoder_ready": True,
    "stage33_11_certified_named_connecting_progress": "0/26",
    "stage33_11_next_branch": "33-11c_A2_26_EXPLICIT_CC_CT_GERSTEN_DIFFERENCE_BITS",
    "stage33_11_current_hot_path_remote_cas": False,
    "stage33_progress": "6/11",
    "stage33_08_released": False,
    "theorem_credit": False,
    "endpoint_credit": False,
}

# Global firewalls remain unchanged/false.
c["stage33_08_released"] = False
c["stage33_08_release_allowed"] = False
c["stage33_40_released"] = False
c["stage33_40_release_allowed"] = False
c["theorem_credit"] = False
c["endpoint_credit"] = False
c["stage33_closed"] = False
c["brauer_manin_set_empty_proved"] = False
c["perfect_cuboid_existence_claim"] = False
c["perfect_cuboid_nonexistence_claim"] = False

CTRL.write_text(json.dumps(c, indent=2, sort_keys=False) + "\n", encoding="utf-8")
print("STAGE33_CONTROLLER_SYNC=PASS")
print("CURRENT_ITEM=" + c["current_item"])
print("NEXT_ITEM=" + c["next_item"])
print("A2_26_FIVE_BIT_DECODER=READY")
print("STAGE33_11_PROGRESS=0/26")
