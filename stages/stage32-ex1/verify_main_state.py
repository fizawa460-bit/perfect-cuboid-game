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
assert front["h2_two_single_sign_choices_candidate"] == 3
assert front["h2_one_single_plus_triple_choices_candidate"] == 3
assert front["h2_choices_excluded_by_capacity_candidate"] == 5
assert front["h2_choices_after_capacity_candidate"] == 1
assert front["h2_unique_capacity_survivor_candidate"].startswith("M=<u,v>")
assert front["h2_excluded_candidate"] is True
assert front["h4_forced_candidate"] is True
assert front["ramification_Q_range_candidate"] == [210, 266]
assert front["ramification_Q_state_count_candidate"] == 29
assert front["Q_states_excluded_by_EX1_05F_candidate"] == 0
assert front["all_residual_configurations_disposed"] is False
assert front["full_target_closure"] is False

arts = {x["leaf"]: x["canonical_sha256"] for x in state["checkpoint_artifacts"]}
assert arts["EX1-05A"] == "b5b3a2b26d4ac7f14ebcb8670f0176363bd1c7921266a1693642638145d61a21"
assert arts["EX1-05B"] == "c0532ef30aee662954f035a0dc5c87f4cfa8ff7f471632efa7d266a8152405f1"
assert arts["EX1-05C"] == "51464451c233eaee4148ded8c6dbb38e84944c01677eced9d6dc8af7219b846f"
assert arts["EX1-05D"] == "ee3d86380cdedce792cf0b90061e2ee02e67f453e1b834c5908fc3e287c73b28"
assert arts["EX1-05E"] == "bdd1a6a84c10cf124d5ceaf75f3de234659f5d0433cbd1c859a3da65328342df"
assert arts["EX1-05F"] == "8b8ee58b63078b48389cb817ea6b6bf0171c9a323b5705dcdbc99242a27958ef"

audit = state["audit"]
assert audit["status"] == "REPAIR_COMPLETE_AWAITING_EXACT_HEAD_CI_AND_REAUDIT"
assert audit["candidate_pr"] == 1688
assert audit["failed_review"]["review_id"] == 5134451242
assert audit["failed_review"]["exact_head"] == "9f88c89eb85daf82700bb463755f97073c5cfcae"
assert len(audit["failed_review"]["blocking_findings"]) == 2
assert audit["repair_05c_six_subgroup_exhaustion_complete"] is True
assert audit["digest_chain_repaired_after_ci_discovery"] is True
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

print("Stage32EX1 MAIN-STATE replay PASS: six-subgroup repair and digest-chain repair recorded; hostile re-audit still required")
