#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
MAIN = "70265586b3f97be21c7621af73f443311f1f3fa3"
BLOCKER = "stages/stage32-ex2/EX2-04/ex2-04b-claim-sync-blocker.json"

s = json.loads(STATE.read_text())
s["schema"] = "STAGE32EX2_MAIN_COMPACT_STATE_V12_EX2_04B_RETAINED_CLAIM_SYNC_BLOCKED"

s["audit"]["status"] = "NOT_READY_EX2_04B_RETAINED_CLAIM_SYNC_BLOCKED_BY_INHERITED_MAIN_DAG_DRIFT"
s["audit"]["exact_head"] = None
s["audit"]["result"] = None
s["audit"]["review_id"] = None

a = s["authority"]
a["EX2_04A_verifier_blob_sha1"] = "2b31f8f8bc8d00555bb880d280ed33119bec095d"
a["EX2_04A_claim_status"] = "PROVISIONAL_CORE_SOURCE_LOCK_STALE_AFTER_VERIFIER_SCHEMA_REPAIR_REQUIRES_VERSIONING"
a["EX2_04B_third_section_subspace"] = "stages/stage32-ex2/EX2-04/third-section-valuation-separation.json"
a["EX2_04B_artifact_blob_sha1"] = "5e9cf16ece57162db995cb1b7014a9d583453202"
a["EX2_04B_artifact_canonical_sha256"] = "9d50dc72c467edce946427f1b74786464e1c6401ca86dab6af87bea792d23c70"
a["EX2_04B_candidate_claim_id"] = "S32.EX2.THREE_DIVISOR_SECTION_SUBSPACE.V1"
a["EX2_04B_claim_status"] = "RETAINED_SCRATCH_PENDING_CLAIM_SYNC_BLOCKED_BY_INHERITED_MAIN_DAG_DRIFT"
a["EX2_04B_claim_sync_blocker"] = BLOCKER
a["EX2_04B_claim_sync_blocker_canonical_sha256"] = "efdef1983868b1490fa6d76deddfb44be358c51f27a0db12fb98d7d1795f62ab"

f = s.setdefault("freshness", {})
f["current_main_observed_sha"] = MAIN
f["last_reconciled_current_main_sha"] = MAIN
f["unreconciled_main_commit_count"] = 0
f["stage32ex2_source_drift_in_intervening_main_commit"] = False
f["claim_dag_integrity_on_current_main"] = "FAIL_SOURCE_LOCKS_PREEXISTING_EX2_OVERLAY"
f["claim_dag_integrity_main_baseline_mismatch_count"] = 4

cs = s["claim_sync"]
cs["candidate_claim_id"] = "S32.EX2.THREE_DIVISOR_SECTION_SUBSPACE.V1"
cs["trigger"] = "RETAINED_CONSOLIDATION"
cs["checkpoint_claim_dag_complete"] = False
cs["claim_dag_integrity_verifier_passed"] = False
cs["current_main_reconciliation_required"] = True
cs["reconciled_current_main_sha"] = MAIN
cs["required_verification_run"] = "BLOCKED_UNTIL_CURRENT_MAIN_STAGE32_CLAIM_DAG_SOURCE_LOCK_INTEGRITY_IS_RESTORED"
cs["status"] = "BLOCKED_INHERITED_CURRENT_MAIN_CLAIM_DAG_SOURCE_LOCK_DRIFT"
cs["reason"] = "EX2-04B certifies a retained 3-dimensional divisor-theoretic section subspace, but mandatory claim-DAG synchronization cannot complete because exact current main already fails Stage32 claim-DAG source-lock integrity before the EX2 overlay. The claim-sync contract forbids carrying old hostile-audit credit onto changed claim cores; EX2 therefore does not rewrite or re-audit EX4/EX5 claims."
cs["blocker_certificate"] = BLOCKER
cs["inherited_current_main_mismatch_count"] = 4
cs["promotion_attempted"] = False
cs["stage32_main_authority_changed"] = False
cs["shared_claim_files_written_from_stale_branch"] = False

front = s["frontier"]
front["EX2_04B_third_section_line_outside_previous_pencil"] = True
front["EX2_04B_valuation_separator_curve_label_1based"] = 25
front["EX2_04B_previous_pencil_order_lower_bound"] = 6
front["EX2_04B_third_divisor_order"] = 4
front["EX2_04B_linear_independence_certified"] = True
front["certified_section_subspace_dimension"] = 3
front["complete_section_space_basis_obtained"] = False
front["EX2_04_finite_dimensional_section_reconstruction_active"] = False
front["EX2_04C_blocked_until_claim_sync"] = True

s["credit"]["level"] = "CERTIFIED_3D_DIVISOR_THEORETIC_SECTION_SUBSPACE_RETAINED_SCRATCH_PENDING_CLAIM_SYNC_PLUS_AUDITED_INTERMEDIATE_EX2_00_THROUGH_03F_NO_COMPLETE_H0_NO_MEMBER_CREDIT"
s["credit"]["stage32_main_credit"] = False

s["current"] = {
    "leaf": "EX2-04B_CLAIM_SYNC_BLOCKER_CHECKPOINT",
    "subroute": "WAIT_FOR_CURRENT_MAIN_STAGE32_CLAIM_DAG_INTEGRITY_REPAIR",
    "status": "EX2_04B_RETAINED_3D_SUBSPACE_CLAIM_SYNC_BLOCKED_INHERITED_MAIN_DAG_DRIFT",
    "objective": "Preserve the EX2-04B 3-dimensional divisor-theoretic section-subspace result without promotion. Do not enter EX2-04C until current-main Stage32 claim-DAG source-lock integrity is restored under versioned-claim and exact hostile-audit semantics.",
    "stop_semantics": "MANAGEMENT_GATE_ONLY_NOT_EX2_MATHEMATICAL_FAILURE_OR_STAGE_EXHAUSTION",
    "next_route_on_success": "AFTER_CURRENT_MAIN_CLAIM_DAG_INTEGRITY_REPAIR_RETRY_EX2_04B_CLAIM_SYNC_THEN_ENTER_EX2_04C",
    "next_route_on_block": "REMAIN_AT_EX2_04B_CLAIM_SYNC_BLOCKER_CHECKPOINT"
}
s["current_leaf_working_set"] = [
    "stages/stage32-ex2/EX2-04/third-section-valuation-separation.json",
    "stages/stage32-ex2/verify_ex2_04b_third_section_valuation_separation.py",
    BLOCKER,
    "stages/stage32-ex2/verify_ex2_04b_claim_sync_blocker.py",
    "stages/stage32/proof/CLAIM-SYNC-CONTRACT.md"
]

fw = s["firewalls"]
fw["three_dimensional_section_subspace_promoted_to_complete_H0"] = False
fw["ex2_04b_scratch_result_promoted_before_claim_sync"] = False
fw["inherited_main_claim_dag_drift_repaired_by_cross_lane_audit_credit_carry_forward"] = False
fw["claim_sync_blocker_bypassed"] = False
fw["stage32_main_credit"] = False
fw["Q602_excluded"] = False
fw["O210_excluded"] = False
fw["stage32_closed"] = False

STATE.write_text(json.dumps(s, indent=2, sort_keys=True) + "\n")
print("PASS applied Stage32EX2 V12 EX2-04B blocked checkpoint")
