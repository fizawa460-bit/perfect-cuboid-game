#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
M = json.loads((ROOT / "final-gap-matrix.json").read_text())
C = json.loads((ROOT / "controller-delta.json").read_text())

assert M["source_frontier_count"] == 46
assert M["source_class_counts"] == {"1": 6, "2": 13, "3": 11, "4": 16}
assert M["final_kernel_counts"] == {"total": 13, "class2": 4, "class3": 9}
assert len(M["class2_kernels"]) == 4
assert len(M["class3_kernels"]) == 9
assert len(set(M["class2_kernels"] + M["class3_kernels"])) == 13
assert M["hidden_class1_found"] is False
assert M["hidden_class1_pending_count"] == 0
assert M["new_active_receiver_found"] is False
assert M["new_active_kernel_found"] is False
assert M["new_decisive_global_theorem_found"] is False
assert M["dormant_reactivated_count"] == 0
assert M["parent_routes"] == {"attack": 11, "green": 1, "amber": 10}
assert M["P_over_M3_scale_known"] is False

claims = M["fresh_external_claims"]
assert claims["family_count"] == 2
assert claims["rejected_count"] == 1
assert claims["sourcelock_pending_count"] == 1
assert len(claims["items"]) == 2
assert all(item["route_credit"] is False for item in claims["items"])

same_measure = M["structure_radar_absorption"]["same_measure_and_sieve_cards"]
assert same_measure["owner"] == "K16-C3-M3-LOCAL-TO-GLOBAL"
assert same_measure["new_kernel_created"] is False
moving = M["structure_radar_absorption"]["moving_family_cards"]
assert moving["new_kernel_created"] is False

assert C["proposal_only"] is True
assert C["audit_applied"] is False
assert C["status"] == "SUBMITTED_PENDING_FRESH_AUDIT"
assert C["final_active_kernel_count"] == 13
assert C["final_class2_kernel_count"] == 4
assert C["final_class3_kernel_count"] == 9
assert C["hidden_class1_pending_count"] == 0
assert C["audit_required"] is True
assert C["merge_allowed"] is False
assert C["advance_allowed"] is False
assert C["next_item_after_audit_pass"] == "29-17_STAGE29_FINAL_HANDOFF_AND_CLOSE"
assert C["perfect_cuboid_existence_claim"] is False
assert C["perfect_cuboid_nonexistence_claim"] is False

print("GAP_SCAN_FINAL structural verification: PASS")
