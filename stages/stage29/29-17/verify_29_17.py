#!/usr/bin/env python3
import json
from pathlib import Path

root = Path(__file__).resolve().parent
handoff = json.loads((root / "final-handoff.json").read_text())
controller = json.loads((root / "controller-delta.json").read_text())

assert handoff["source"]["source_frontier_count"] == 46
assert handoff["source"]["class_counts"] == {
    "1_closed": 6,
    "2_active": 13,
    "3_active": 11,
    "4_dormant": 16,
}
assert len(handoff["final_active_kernels"]["class2"]) == 4
assert len(handoff["final_active_kernels"]["class3"]) == 9
all_kernels = handoff["final_active_kernels"]["class2"] + handoff["final_active_kernels"]["class3"]
assert len(all_kernels) == 13
assert len(set(all_kernels)) == 13
assert handoff["parent_routes"] == {
    "attack_route_count": 11,
    "green_route_count": 1,
    "amber_route_count": 10,
    "green_route": "J12-POP-INTERACTION",
}
assert handoff["terminal_facts"]["P_over_M3_scale_known"] is False
assert handoff["terminal_facts"]["pesch_e1_currently_proved"] is False
assert handoff["terminal_facts"]["pesch_e1_if_proved_as_stated_implies_perfect_cuboid_nonexistence"] is True
assert handoff["terminal_facts"]["hidden_class1_pending_count"] == 0
assert handoff["terminal_facts"]["perfect_cuboid_existence_claim"] is False
assert handoff["terminal_facts"]["perfect_cuboid_nonexistence_claim"] is False
assert handoff["audit_required"] is True
assert handoff["merge_allowed"] is False
assert handoff["stage29_close_allowed"] is False
assert controller["proposal_only"] is True
assert controller["audit_applied"] is False
assert controller["perfect_cuboid_problem_status"] == "OPEN"
assert controller["automatic_next_stage"] is None
assert controller["audit_required"] is True
assert controller["stage29_close_allowed"] is False

print("Stage29-17 submission accounting: PASS")
