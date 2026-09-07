#!/usr/bin/env python3
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
state = json.loads((HERE / "MAIN-STATE.json").read_text())

assert state["stage"] == "32EX1"
assert state["bootstrap"]["active_work_pr"] == 1688
assert state["bootstrap"]["merge_authorized"] is False

cc = state["completion_contract"]
assert cc["allowed_terminal_outcomes"] == [
    "ALL_V6_GENUS1_CARRIERS_EXCLUDED",
    "GENUINE_SURVIVING_CARRIER_ESTABLISHED",
]
assert cc["finite_residual_ledger_is_terminal_success"] is False
assert cc["blocked_route_is_stage_exhaustion"] is False

cur = state["current"]
assert cur["status"] == "REPAIR_COMPLETE_AWAITING_EXACT_HEAD_CI_AND_REAUDIT"
assert cur["subroute"] == "EX1-05G_H4_COMMON_COVER_CORRESPONDENCE_COUPLING"
assert cur["resume_05g_before_reaudit"] is False

front = state["frontier"]
assert front["h2_full_stabilizer_choices_total_candidate"] == 6
assert front["h2_choices_excluded_by_capacity_candidate"] == 5
assert front["h2_choices_after_capacity_candidate"] == 1
assert front["h2_excluded_candidate"] is True
assert front["h4_forced_candidate"] is True
assert front["ramification_Q_range_candidate"] == [210, 266]
assert front["ramification_Q_state_count_candidate"] == 29
assert front["Q_states_excluded_by_EX1_05F_candidate"] == 0
assert front["all_residual_configurations_disposed"] is False
assert front["full_target_closure"] is False

arts = {x["leaf"]: x["canonical_sha256"] for x in state["checkpoint_artifacts"]}
assert arts["EX1-05C"] == "51464451c233eaee4148ded8c6dbb38e84944c01677eced9d6dc8af7219b846f"
assert arts["EX1-05D"] == "6c432739b1e02c58ddfc8f9e0ca3d9695604e84e5dbc12f407185074ae174612"
assert arts["EX1-05E"] == "0f7c63f90ace7974249aae2f387ff8a49650d6fba489923bd13f48d28e431701"
assert arts["EX1-05F"] == "ad116cc0729f0200bf578b363a47a5a166651e9e1dab215529d8cc6a64562778"

audit = state["audit"]
assert audit["status"] == "REPAIR_COMPLETE_AWAITING_EXACT_HEAD_CI_AND_REAUDIT"
assert audit["candidate_pr"] == 1688
assert audit["failed_review"]["review_id"] == 5134451242
assert audit["failed_review"]["exact_head"] == "9f88c89eb85daf82700bb463755f97073c5cfcae"
assert len(audit["failed_review"]["blocking_findings"]) == 2
assert audit["exact_head_ci_required"] is True
assert audit["exact_head_ci_observed_success"] is False
assert audit["pass_auto_merges"] is False
assert audit["pass_auto_promotes_to_stage32_main"] is False

fw = state["firewalls"]
for key in [
    "full_target_closure_claimed",
    "stage32_main_credit",
    "Q602_excluded",
    "O210_excluded",
    "stage32_closed",
    "perfect_cuboid_existence_claim",
    "perfect_cuboid_nonexistence_claim",
]:
    assert fw[key] is False

print("Stage32EX1 MAIN-STATE replay PASS: 05C six-subgroup repair recorded; exact-head CI and hostile re-audit still required")
