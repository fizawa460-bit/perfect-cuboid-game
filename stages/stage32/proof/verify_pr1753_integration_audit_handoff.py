#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HANDOFF = ROOT / "stages/stage32/proof/PR1753-INTEGRATION-AUDIT-HANDOFF.json"
MAIN_STATE = ROOT / "stages/stage32/MAIN-STATE.json"
CHECKPOINT = ROOT / "stages/stage32/management/post-n355-n356-candidate-checkpoint-20260910.json"

h = json.loads(HANDOFF.read_text())
m = json.loads(MAIN_STATE.read_text())
c = json.loads(CHECKPOINT.read_text())

assert h["schema"] == "STAGE32_PR1753_INTEGRATION_AUDIT_HANDOFF_V1"
assert h["pr"] == 1753
assert h["mode"] == "INTEGRATION_ONLY_CLOSEOUT_AUDIT_FREEZE"

scope = h["audit_scope"]
assert scope["integration_only"] is True
assert scope["new_stage32_mathematical_credit"] is False
assert scope["new_n356_credit"] is False
assert scope["n356_promotion_in_pr1753"] is False
assert scope["substantive_research_frozen_on_pr1753"] is True

ms = m["authority_sync"]
front = m["current_exact_frontier"]
cur = m["current"]
fw = m["firewalls"]

assert ms["stage32_main_integration_pr"] == 1753
assert ms["n356_candidate_status"] == "AUDIT_REQUIRED"
assert ms["n356_audit_credit_consumed"] is False
assert front["n356_status"] == "AUDIT_REQUIRED"
assert front["n356_main_pruning_credit"] is False
assert front["authoritative_remaining_strata"] == 17128
assert front["authoritative_remaining_terminals"] == 66462870551188628549910
assert front["full178_goal_frontier_status"] == "ACTIVE_INCOMPLETE"
assert front["stage32_closed"] is False
assert cur["mainbatch_stop_gate"] == "BEFORE_N356_PROMOTION"
assert cur["stacked_candidate_audit_status"] == "AUDIT_REQUIRED"
assert fw["n356_self_promoted_to_audited"] is False
assert fw["n356_credit_exceeds_external_audit"] is False
assert fw["merge_authorized"] is False
assert fw["stage32_closed"] is False
assert fw["theorem_credit"] is False
assert fw["receiver_credit"] is False
assert fw["endpoint_credit"] is False

ca = c["authority"]
cfw = c["firewalls"]
cn = c["n356"]
assert ca["authoritative_remaining_strata"] == 17128
assert ca["authoritative_remaining_terminals"] == 66462870551188628549910
assert ca["n356_status"] == "AUDIT_REQUIRED"
assert ca["n356_authority_credit"] is False
assert cn["main_pruning_credit"] is False
assert cn["external_hostile_audit_required"] is True
assert cn["candidate_remaining_strata"] == 17128
assert cn["candidate_remaining_terminals"] == 65396964990500233636214
assert cn["candidate_incremental_rejected_terminals"] == 1065905560688394913696
assert cfw["merge_authorized"] is False
assert cfw["stage32_closed"] is False

hc = h["n356_carryover"]
assert hc["status"] == "AUDIT_REQUIRED"
assert hc["authority_credit_consumed"] is False
assert hc["main_pruning_credit"] is False
assert hc["candidate_counts_replace_authoritative_n355_frontier"] is False
assert hc["deferred_to_next_stage32_main_pr"] is True
assert hc["candidate_remaining_strata"] == cn["candidate_remaining_strata"]
assert hc["candidate_remaining_terminals"] == cn["candidate_remaining_terminals"]
assert hc["candidate_incremental_rejected_terminals"] == cn["candidate_incremental_rejected_terminals"]

hf = h["authoritative_frontier"]
assert hf["remaining_strata"] == front["authoritative_remaining_strata"]
assert hf["remaining_terminals"] == front["authoritative_remaining_terminals"]
assert hf["full178_status"] == front["full178_goal_frontier_status"]
assert hf["stage32_closed"] is False

for key, value in h["firewalls"].items():
    if key in {"n356_self_promoted", "n356_credit_exceeds_external_audit", "full178_complete", "stage32_closed", "theorem_credit", "receiver_credit", "endpoint_credit", "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim", "merge_authorized"}:
        assert value is False

policy_merge = h["repo_workflow_policy_merge_commit"]
subprocess.run(["git", "merge-base", "--is-ancestor", policy_merge, "HEAD"], check=True)

print(json.dumps({
    "verdict": "PASS_PR1753_INTEGRATION_AUDIT_HANDOFF",
    "integration_only": True,
    "authoritative_remaining_strata": front["authoritative_remaining_strata"],
    "authoritative_remaining_terminals": front["authoritative_remaining_terminals"],
    "n356_status": front["n356_status"],
    "n356_main_pruning_credit": front["n356_main_pruning_credit"],
    "n356_deferred_to_next_pr": hc["deferred_to_next_stage32_main_pr"],
    "merge_authorized": False
}, sort_keys=True))
