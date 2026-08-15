#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
controller_path = ROOT / "stages" / "stage25" / "25-reentry-controller.json"
parent_path = ROOT / "stages" / "stage25" / "25-controller.json"
closeout_path = ROOT / "stages" / "stage25" / "25-70" / "controller.json"
audit_path = ROOT / "stages" / "stage25" / "25-70" / "audit.md"
roadmap_path = ROOT / "docs" / "stage25-reentry-roadmap.md"
operations_path = ROOT / "docs" / "stage25-reentry-operations.md"

controller = json.loads(controller_path.read_text(encoding="utf-8"))
parent = json.loads(parent_path.read_text(encoding="utf-8"))
closeout = json.loads(closeout_path.read_text(encoding="utf-8"))
audit = audit_path.read_text(encoding="utf-8")
roadmap = roadmap_path.read_text(encoding="utf-8")
operations = operations_path.read_text(encoding="utf-8")

assert controller["starts_after"]["stage25_checkpoint"] == 70
assert controller["starts_after"]["audit_verdict"] == "PASS"
assert controller["starts_after"]["unresolved_repair_bypass_allowed"] is False
assert list(controller["phases"]) == ["10", "20", "30", "40", "50", "60", "70"]

expected = {
    "10": "Stage25-um-r001a",
    "20": "Stage25-u24-r002a",
    "30": "Stage25-u23-r003a",
    "40": "Stage25-u22-r004a",
    "50": "Stage25-u21-r005a",
    "60": "Stage25-u20-r006a",
    "70": "Stage25-um-r007a",
}
pattern = re.compile(r"^Stage25-(?:u\d+|um)-r0\d{2}[a-z]$")
for phase, task_id in expected.items():
    assert controller["phases"][phase]["task_id"] == task_id
    assert pattern.match(task_id), task_id
    assert task_id in roadmap

policy = controller["derived_route_policy"]
assert policy["maximum_simultaneous_active_routes"] == 3
assert policy["route_ids_recycled"] is False
assert policy["parent_phase_audit_required_before_recursive_launch"] is True
assert policy["next_route_serial"] >= 8

# Route serial accounting is lifecycle-aware.  Before any derived route it is 8;
# once r008 is reserved, the next serial must advance to 9 rather than recycling.
route_serials = []
route_re = re.compile(r"-r0(\d{2})[a-z]$")
for item in controller.get("propagation_queue", []):
    route_id = item["route_id"]
    m = route_re.search(route_id)
    assert m, route_id
    route_serials.append(int(m.group(1)))
if route_serials:
    assert len(route_serials) == len(set(route_serials))
    assert policy["next_route_serial"] == max(route_serials) + 1
else:
    assert policy["next_route_serial"] == 8

gate = controller["stage26_gate"]
assert gate["stage26_allowed"] is False
assert gate["unresolved_internal_routes"] is True
assert controller["safety"]["stage25_current_deep_stop_rule_relaxed"] is False
assert controller["safety"]["closed_theorem_means_exploration_exhausted"] is False
assert "Stage25-reentry-main-batch" in roadmap and "Stage25-reentry-audit" in operations
assert "24 -> 23 -> 22 -> 21 -> 20" in roadmap

# Closeout evidence is invariant for every unlocked/research state.
status = controller["status"]
if status == "BLOCKED_UNTIL_STAGE25_AUDITED_CLOSEOUT":
    assert controller["current_phase"] is None
    assert controller["phases"]["10"]["status"] == "BLOCKED"
    assert gate["stage25_main_closed"] is False
    print("STAGE25_REENTRY_GATE=BLOCKED_VALID")
else:
    assert controller["starts_after"]["closeout_merged"] is True
    assert gate["stage25_main_closed"] is True
    evidence = controller["unlock_evidence"]
    assert evidence["checkpoint70_audit_verdict"] == "PASS"
    assert evidence["closeout_pr"] == 1000
    assert evidence["closeout_merge_commit"] == "12e1cb027e3123328702393ebdb3e3687ca0a169"
    assert evidence["main_stage25_closed"] is True

    assert parent["status"] == "CLOSED"
    assert parent["checkpoint_status"]["70"] == "PROVED_AUDITED_PASS"
    assert parent["state"]["CURRENT_CHECKPOINT"] == 70
    assert parent["state"]["MAIN_STATUS"] == "COMPLETE"
    assert parent["state"]["NEXT_STAGE"] == "Stage25-reentry"
    assert parent["checkpoint70"]["closeout_merged"] is True
    assert parent["last_audit"]["checkpoint"] == 70
    assert parent["last_audit"]["verdict"] == "PASS"
    assert parent["last_audit"]["pr"] == 1000

    assert closeout["audit_status"] == "PASS"
    assert closeout["closeout_merged"] is True
    assert closeout["stage25_reentry_unlocked"] is True
    assert closeout["next_stage"] == "Stage25-reentry"
    assert "AUDIT_VERDICT=PASS" in audit
    assert "STAGE25_CLOSEOUT_ACCEPTED=true" in audit

    if controller["current_phase"] == 10:
        assert status in (
            "PHASE10_READY_PENDING_SYNC_REAUDIT",
            "PHASE10_READY_AFTER_STAGE25_AUDITED_CLOSEOUT_MERGE",
            "PHASE10_SUBMITTED_PENDING_FRESH_AUDIT",
            "PHASE10_AUDITED_PASS_AWAITING_MERGE",
        )
        print("STAGE25_REENTRY_GATE=PHASE10_LIFECYCLE_VALID")
    elif controller["current_phase"] == 20:
        assert status == "PHASE20_SUBMITTED_PENDING_FRESH_AUDIT"
        assert controller["phases"]["10"]["status"] == "AUDITED_PASS_MERGED"
        p10 = controller["phase10_submission"]
        assert p10["audit_status"] == "PASS"
        assert p10["pr"] == 1002
        assert p10["merge_commit"] == "5cb7dc8792faf575c1e21fce8166f094af6d7b14"
        assert controller["phases"]["20"]["status"] == "SUBMITTED_PENDING_AUDIT"
        p20 = controller["phase20_submission"]
        assert p20["task_id"] == "Stage25-u24-r002a"
        assert p20["status"] == "SUBMITTED_PENDING_AUDIT"
        assert p20["audit_status"] == "PENDING"
        assert p20["advance_allowed"] is False
        assert p20["merge_allowed"] is False
        for rel in (
            p20["result"], p20["discovery_ledger"], p20["weapon_delta"],
            p20["directional_proof"], p20["directional_registry"],
            p20["backflow_proposals"], p20["verifier"], p20["workflow"],
        ):
            assert (ROOT / rel).exists(), rel
        assert p20["derived_routes_opened"] == []
        assert p20["queued_derived_routes"] == ["Stage25-um-r008a"]
        assert len(controller["propagation_queue"]) == 1
        queued = controller["propagation_queue"][0]
        assert queued["route_id"] == "Stage25-um-r008a"
        assert queued["parent_task"] == "Stage25-u24-r002a"
        assert queued["status"] == "QUEUED_UNTIL_PHASE20_AUDIT_PASS"
        assert queued["blocks_next_phase"] is True
        assert controller["next_expected_command"] == "Stage25-reentry-audit"
        print("STAGE25_REENTRY_GATE=PHASE20_SUBMITTED_PENDING_AUDIT_VALID")
    else:
        raise AssertionError(f"unsupported current phase lifecycle: {controller['current_phase']}")

print("STAGE25_REENTRY_CONTROLLER=PASS")
print("STAGE25_CURRENT_STOP_RULE_UNCHANGED=PASS")
print("STAGE25_REENTRY_ORDER_24_23_22_21_20=PASS")
print("STAGE25_DERIVED_PROPAGATION_QUEUE=PASS")
print("STAGE26_GATE_INITIAL_BLOCK=PASS")
