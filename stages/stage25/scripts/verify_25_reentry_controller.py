#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
controller_path = ROOT / "stages" / "stage25" / "25-reentry-controller.json"
roadmap_path = ROOT / "docs" / "stage25-reentry-roadmap.md"
operations_path = ROOT / "docs" / "stage25-reentry-operations.md"

controller = json.loads(controller_path.read_text(encoding="utf-8"))
roadmap = roadmap_path.read_text(encoding="utf-8")
operations = operations_path.read_text(encoding="utf-8")

assert controller["status"] == "BLOCKED_UNTIL_STAGE25_AUDITED_CLOSEOUT"
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
assert policy["next_route_serial"] == 8
assert policy["maximum_simultaneous_active_routes"] == 3
assert policy["route_ids_recycled"] is False
assert policy["parent_phase_audit_required_before_recursive_launch"] is True

gate = controller["stage26_gate"]
assert gate["stage26_allowed"] is False
assert gate["unresolved_internal_routes"] is True
assert controller["safety"]["stage25_current_deep_stop_rule_relaxed"] is False
assert controller["safety"]["closed_theorem_means_exploration_exhausted"] is False
assert "Stage25-reentry-main-batch" in roadmap and "Stage25-reentry-audit" in operations
assert "24 -> 23 -> 22 -> 21 -> 20" in roadmap

print("STAGE25_REENTRY_CONTROLLER=PASS")
print("STAGE25_CURRENT_STOP_RULE_UNCHANGED=PASS")
print("STAGE25_REENTRY_ORDER_24_23_22_21_20=PASS")
print("STAGE25_DERIVED_PROPAGATION_QUEUE=PASS")
print("STAGE26_GATE_INITIAL_BLOCK=PASS")
