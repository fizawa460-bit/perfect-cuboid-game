#!/usr/bin/env python3
import json
from pathlib import Path

root = Path(__file__).resolve().parent
handoff = json.loads((root / "final-handoff.json").read_text())
controller = json.loads((root / "controller-delta.json").read_text())
audit = json.loads((root / "audit-state.json").read_text())

expected_classes = {
    "1_closed": 6,
    "2_active": 13,
    "3_active": 11,
    "4_dormant": 16,
}

assert handoff["source"]["source_frontier_count"] == 46
assert handoff["source"]["class_counts"] == expected_classes
assert handoff["source"]["active_source_entry_count"] == 24
assert handoff["source"]["active_source_entry_unmapped_count"] == 0
assert handoff["source"]["active_source_entry_duplicate_mapping_count"] == 0
assert handoff["source"]["dormant_reactivation_trigger_missing_count"] == 0
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
assert handoff["stage29_closed"] is True
assert handoff["perfect_cuboid_problem_status"] == "OPEN"
assert handoff["audit_required"] is False
assert handoff["merge_allowed"] is True
assert handoff["stage29_close_allowed"] is True

assert controller["proposal_only"] is False
assert controller["audit_applied"] is True
assert controller["stage29_closed"] is True
assert controller["perfect_cuboid_problem_status"] == "OPEN"
assert controller["automatic_next_stage"] is None
assert controller["audit_required"] is False
assert controller["merge_allowed"] is True
assert controller["stage29_close_allowed"] is True
assert controller["next_item"] == "NONE_AUTOMATIC"

assert audit["gap_scan_final_audited_pass"] is True
assert audit["source_frontier_count"] == 46
assert audit["source_class_counts"] == expected_classes
assert audit["active_source_entry_unmapped_count"] == 0
assert audit["active_source_entry_duplicate_mapping_count"] == 0
assert audit["final_active_kernel_count"] == 13
assert audit["final_kernel_class_counts"] == {"2": 4, "3": 9}
assert audit["hidden_class1_pending_count"] == 0
assert audit["dormant_reactivation_trigger_missing_count"] == 0
assert audit["parent_routes"]["attack"] == 11
assert audit["parent_routes"]["green"] == 1
assert audit["parent_routes"]["amber"] == 10
assert audit["P_over_M3_scale_known"] is False
assert audit["stage29_closed"] is True
assert audit["perfect_cuboid_problem_status"] == "OPEN"
assert audit["audit_required"] is False
assert audit["merge_allowed"] is True
assert audit["stage29_close_allowed"] is True
assert audit["perfect_cuboid_existence_claim"] is False
assert audit["perfect_cuboid_nonexistence_claim"] is False

print("Stage29-17 audited close verification: PASS")
