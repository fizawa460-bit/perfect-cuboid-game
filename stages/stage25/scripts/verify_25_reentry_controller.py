#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def data(rel: str):
    p = ROOT / rel
    assert p.exists(), f"missing {rel}"
    return json.loads(p.read_text(encoding="utf-8"))


def text(rel: str) -> str:
    p = ROOT / rel
    assert p.exists(), f"missing {rel}"
    return p.read_text(encoding="utf-8")


controller = data("stages/stage25/25-reentry-controller.json")
parent = data("stages/stage25/25-controller.json")
closeout = data("stages/stage25/25-70/controller.json")
roadmap = text("docs/stage25-reentry-roadmap.md")
operations = text("docs/stage25-reentry-operations.md")

# Immutable unlock contract.
assert controller["starts_after"]["stage25_checkpoint"] == 70
assert controller["starts_after"]["audit_verdict"] == "PASS"
assert controller["starts_after"]["closeout_merged"] is True
assert controller["starts_after"]["unresolved_repair_bypass_allowed"] is False
assert parent["status"] == "CLOSED"
assert parent["checkpoint_status"]["70"] == "PROVED_AUDITED_PASS"
assert parent["state"]["NEXT_STAGE"] == "Stage25-reentry"
assert closeout["audit_status"] == "PASS"
assert closeout["closeout_merged"] is True
assert closeout["stage25_reentry_unlocked"] is True

# Fixed phase plan and route identity discipline.
expected = {
    "10": "Stage25-um-r001a",
    "20": "Stage25-u24-r002a",
    "30": "Stage25-u23-r003a",
    "40": "Stage25-u22-r004a",
    "50": "Stage25-u21-r005a",
    "60": "Stage25-u20-r006a",
    "70": "Stage25-um-r007a",
}
assert list(controller["phases"]) == list(expected)
pattern = re.compile(r"^Stage25-(?:u\d+|um)-r0\d{2}[a-z]$")
for phase, task_id in expected.items():
    assert controller["phases"][phase]["task_id"] == task_id
    assert pattern.match(task_id), task_id
    assert task_id in roadmap
assert "Stage25-reentry-main-batch" in roadmap
assert "Stage25-reentry-audit" in operations
assert "24 -> 23 -> 22 -> 21 -> 20" in roadmap

policy = controller["derived_route_policy"]
assert policy["maximum_simultaneous_active_routes"] == 3
assert policy["route_ids_recycled"] is False
assert policy["parent_phase_audit_required_before_recursive_launch"] is True
route_re = re.compile(r"-r0(\d{2})[a-z]$")
serials = []
for item in controller.get("propagation_queue", []):
    m = route_re.search(item["route_id"])
    assert m, item["route_id"]
    serials.append(int(m.group(1)))
assert serials == [8, 9, 10, 11]
assert policy["next_route_serial"] == 12

# Every pre-phase70 phase/derived route must be hostile-audited and merged.
checks = [
    ("phase10_submission", 1002, "5cb7dc8792faf575c1e21fce8166f094af6d7b14"),
    ("phase20_submission", 1003, "1d88e8e3254a383620e221df8a1a1039ebeabcd4"),
    ("r008a_submission", 1004, "11075adf8e30c73e5058790ee6ed6e2a9b6c9e2b"),
    ("phase30_submission", 1005, "daf84757c185df6973936d2970a6307ab0bff62b"),
    ("r009a_submission", 1006, "4eb3349ee8ec02dcabb71bd1be3a48234356606b"),
    ("phase40_submission", 1007, "eebe4cd59caef804be76508f3773f2af6c7d47f2"),
    ("r010a_submission", 1008, "9d2e767697a33195e756af6b366cb6f0548494d3"),
    ("phase50_submission", 1009, "8765eb73db07da8afb8ad9b1f9a538ff8cd080ee"),
    ("r011a_submission", 1010, "e64f21621bb1b7062dfd21f186e6ed1bcc191272"),
    ("phase60_submission", 1011, "119afa00919f67bea8e3ba5515c0f9663aa9f2e2"),
]
for key, pr, merge_commit in checks:
    item = controller[key]
    assert item["audit_status"] == "PASS", key
    assert item["status"].startswith("AUDITED_PASS_MERGED"), (key, item["status"])
    assert item["advance_allowed"] is True, key
    assert item["merge_allowed"] is True, key
    assert item["pr"] == pr, key
    assert item["merge_commit"] == merge_commit, key

assert controller["phase60_submission"]["stage20_stage26_ready_interface"] is True
assert controller["phase60_submission"]["new_reusable_weapon_proved"] is True
assert controller["r011a_submission"]["geometric_manin_invariant_ledger_proved"] is True
assert controller["r011a_submission"]["common_dirichlet_pole_slot_ledger_proved"] is False
assert controller["r011a_submission"]["independent_factorization_proved"] is False

# Propagation queue is fully resolved before the handoff audit.
queue = controller["propagation_queue"]
assert [x["route_id"] for x in queue] == [
    "Stage25-um-r008a", "Stage25-um-r009a", "Stage25-um-r010a", "Stage25-um-r011a"
]
for item in queue:
    assert item["status"] == "AUDITED_PASS_MERGED"
    assert item["audit_required"] is True
    assert item["blocks_next_phase"] is False

# Phase70 package and Stage26 gate.
assert controller["current_phase"] == 70
p70 = controller["phase70_submission"]
assert p70["task_id"] == "Stage25-um-r007a"
for rel in (
    p70["result"], p70["handoff_registry"], p70["propagation_resolution"],
    p70["discovery_ledger"], p70["weapon_delta"], p70["stage26_handoff"],
    p70["verifier"], p70["workflow"],
):
    assert (ROOT / rel).exists(), rel
assert p70["derived_route_queue_has_unresolved_internal_route"] is False
assert p70["stage20_stage26_ready_interface"] is True
assert p70["backflow_synchronized"] is True
assert p70["stage26_allowed"] is False

status = controller["status"]
gate = controller["stage26_gate"]
assert gate["stage25_main_closed"] is True
assert gate["unresolved_internal_routes"] is False
assert gate["stage20_stage26_ready_interface"] is True
assert gate["backflow_synchronized"] is True
assert gate["stage26_allowed"] is False

if status == "PHASE70_SUBMITTED_PENDING_FRESH_AUDIT":
    assert controller["phases"]["70"]["status"] == "SUBMITTED_PENDING_FRESH_AUDIT"
    assert p70["audit_status"] == "PENDING"
    assert p70["advance_allowed"] is False
    assert p70["merge_allowed"] is False
    assert gate["all_reentry_phases_audited"] is False
    assert controller["next_expected_command"] == "Stage25-reentry-audit"
elif status == "PHASE70_AUDITED_PASS_AWAITING_MERGE":
    assert controller["phases"]["70"]["status"] == "AUDITED_PASS_AWAITING_MERGE"
    assert p70["audit_status"] == "PASS"
    assert p70["advance_allowed"] is True
    assert p70["merge_allowed"] is True
    assert gate["all_reentry_phases_audited"] is True
    # Stage26 remains false on the unmerged PR branch; merge is the final gate.
    assert gate["stage26_allowed"] is False
else:
    raise AssertionError(f"unexpected phase70 lifecycle: {status}")

assert controller["safety"]["finite_data_as_asymptotic_proof"] is False
assert controller["safety"]["audit_pass_auto_merges"] is False
assert controller["safety"]["stage25_current_deep_stop_rule_relaxed"] is False

print("STAGE25_REENTRY_CONTROLLER=PASS")
print("STAGE25_REENTRY_PHASE_ORDER=PASS")
print("STAGE25_REENTRY_ALL_PRIOR_AUDITS_MERGED=PASS")
print("STAGE25_DERIVED_PROPAGATION_QUEUE=RESOLVED")
print("STAGE20_STAGE26_READY_INTERFACE=PASS")
print("STAGE25_REENTRY_BACKFLOW_SYNCHRONIZED=PASS")
print("STAGE26_GATE=BLOCKED_PENDING_PHASE70_AUDIT_MERGE")
