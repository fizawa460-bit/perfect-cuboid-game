#!/usr/bin/env python3
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
state = json.loads((HERE / "MAIN-STATE.json").read_text(encoding="utf-8"))

assert state["schema"] == "STAGE32EX1_MAIN_COMPACT_STATE_V18_POST05G_COMMON_COVER_CORRESPONDENCE_CANDIDATE"
assert state["stage"] == "32EX1"

boot = state["bootstrap"]
assert boot["audited_predecessor_pr"] == 1688
assert boot["audited_predecessor_merge_sha"] == "6431ec2a90ed9260d4362d7146a9788cbc21c8d1"
assert boot["work_branch"] == "stage32ex1-ex1-05g-common-cover-correspondence"
assert boot["active_work_pr"] == 1700
assert boot["branch_base_main_sha"] == "6431ec2a90ed9260d4362d7146a9788cbc21c8d1"
assert boot["merge_authorized"] is False

fresh = state["freshness"]
assert fresh["branch_started_from_exact_main"] is True
assert fresh["freshness_sync_completed_at_05g_start"] is True
assert fresh["freshness_recheck_required_before_future_audit_or_promotion"] is True

cc = state["completion_contract"]
assert cc["allowed_terminal_outcomes"] == [
    "ALL_V6_GENUS1_CARRIERS_EXCLUDED",
    "GENUINE_SURVIVING_CARRIER_ESTABLISHED",
]
assert cc["finite_residual_ledger_is_terminal_success"] is False
assert cc["blocked_route_is_stage_exhaustion"] is False

prev = state["audited_checkpoint"]
assert prev["pr"] == 1688
assert prev["review_id"] == 5135375926
assert prev["exact_head"] == "93c455e1e69ed65fbfb553462fdcfbc8e2becbae"
assert prev["result"] == "PASS"
assert prev["merge_commit"] == "6431ec2a90ed9260d4362d7146a9788cbc21c8d1"
assert prev["audited_through_leaf"] == "EX1-05F"
assert prev["credit_ceiling"] == "INTERMEDIATE_BRANCH_EXCLUSION_AND_EXACT_BLOCKER_ONLY"
assert prev["exact_head_ci"] == {
    "run_id": 34163317320,
    "job_id": 101869390750,
    "result": "SUCCESS",
    "exact_checkout_identity": True,
    "clean_diff": True,
    "clean_status": True,
}

cur = state["current"]
assert cur["status"] == "EX1_05G_RETAINED_CANDIDATE_UNAUDITED"
assert cur["completed_subroute_candidate"] == "EX1-05G_H4_COMMON_COVER_CORRESPONDENCE_COUPLING"
assert cur["subroute"] == "EX1-05H_CORRESPONDENCE_DEFECT_TO_OFF_CUSP_RAMIFICATION_COUPLING"
assert cur["stop_semantics"] == "ACTIVE_NEXT_LEAF_NOT_STAGE_EXHAUSTION"

front = state["frontier"]
assert front["audited_EX1_00_through_EX1_05F_intermediate_branch_exclusion"] is True
assert front["h2_excluded_audited"] is True
assert front["h4_forced_audited"] is True
assert front["fixed_v6_projection_degrees_D_to_C2"] == [105, 81]
assert front["ramification_Q_range"] == [210, 266]
assert front["ramification_Q_state_count"] == 29
assert front["Q_states_excluded_by_EX1_05F"] == 0
assert front["common_cover_fixed_plane_uniform_candidate"] is True
assert front["rosati_Q_uniform_candidate"] == 602
assert front["Gamma_square_candidate"] == 15806
assert front["Gamma_sigma_candidate"] == 1204
assert front["Gamma_arithmetic_genus_candidate"] == 8090
assert front["Gamma_normalization_defect_formula_candidate"] == "7984-r"
assert front["Gamma_normalization_defect_range_candidate"] == [7956, 7984]
assert front["mod2_fixed_plane_survivor_count_candidate"] == 28
assert front["coarse_joint_product_cell_count_candidate"] == 812
assert front["Q_states_excluded_by_EX1_05G_candidate"] == 0
assert front["correspondence_defect_to_off_cusp_ramification_coupling_open"] is True
assert front["finite_residual_configuration_ledger_complete"] is False
assert front["all_residual_configurations_disposed"] is False
assert front["full_target_closure"] is False

arts = {x["leaf"]: x for x in state["checkpoint_artifacts"]}
for leaf in ["EX1-00","EX1-01","EX1-02","EX1-03","EX1-04","EX1-05A","EX1-05B","EX1-05C","EX1-05D","EX1-05E","EX1-05F"]:
    assert arts[leaf]["audit_status"] == "PASS_AS_PART_OF_PR1688"
assert arts["EX1-05G"] == {
    "leaf": "EX1-05G",
    "canonical_sha256": "5a1c30a64857b900f7523153f326c0742ad5cb4ef88e77b0748dd6c4e532be08",
    "audit_status": "PENDING",
}

credit = state["credit"]
assert credit["level"] == "AUDITED_EX1_00_THROUGH_05F_INTERMEDIATE_BRANCH_EXCLUSION__05G_CANDIDATE_UNAUDITED"
assert credit["audited_intermediate_branch_exclusion"] is True
assert credit["candidate_05g_common_cover_defect_ladder"] is True
assert credit["candidate_05g_nonpruning_boundary"] is True
assert credit["all_v6_genus1_carriers_excluded"] is False
assert credit["genuine_surviving_carrier_established"] is False
assert credit["full_target_closure"] is False
assert credit["stage32_main_credit"] is False

audit = state["audit"]
assert audit["prior_pass"]["review_id"] == 5135375926
assert audit["current_candidate_pr"] == 1700
assert audit["current_candidate_leaf"] == "EX1-05G_H4_COMMON_COVER_CORRESPONDENCE_COUPLING"
assert audit["current_candidate_status"] == "PENDING_FUTURE_CONSOLIDATION_HOSTILE_AUDIT"
assert audit["current_exact_head_for_audit"] is None
assert audit["pass_auto_merges"] is False
assert audit["pass_auto_promotes_to_stage32_main"] is False

fw = state["firewalls"]
for key in [
    "stage32_O210_specific_transvection_16_to_3_imported_without_adapter",
    "Q602_residue_survival_promoted_to_geometric_correspondence",
    "cartesian_812_cells_promoted_to_geometric_realizability",
    "Gamma_defect_identified_with_original_curve_delta_472",
    "projection_ramification_identified_with_intrinsic_delta",
    "off_cusp_ramification_numerical_assignment_promoted_to_map_existence",
    "full_target_closure_claimed",
    "stage32_main_credit",
    "Q602_excluded",
    "O210_excluded",
    "stage32_closed",
    "perfect_cuboid_existence_claim",
    "perfect_cuboid_nonexistence_claim",
]:
    assert fw[key] is False, key

print("Stage32EX1 MAIN-STATE replay PASS: audited 00..05F retained; 05G candidate records uniform Q_Rosati=602 and delta_Gamma=7984-r; next route 05H")
