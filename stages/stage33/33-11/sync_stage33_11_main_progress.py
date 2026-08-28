#!/usr/bin/env python3
"""Overlay MAIN development progress after the exact Stage33-11 checkpoint sync."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CTRL = ROOT / "stages" / "stage33" / "controller.json"
HERE = ROOT / "stages" / "stage33" / "33-11"
A26 = HERE / "stage33-11-a2-26-main-working-column.json"
SMALL = HERE / "stage33-11-smallest-main-working-columns.json"
BLOCKS = HERE / "stage33-11-remaining-block-representatives.json"

w = json.loads(A26.read_text(encoding="utf-8"))
s = json.loads(SMALL.read_text(encoding="utf-8"))
r = json.loads(BLOCKS.read_text(encoding="utf-8"))
if w.get("schema") != "STAGE33_11_A2_26_MAIN_WORKING_COLUMN_V1":
    raise SystemExit("A2_26 MAIN working certificate schema moved")
if s.get("schema") != "STAGE33_11_SMALLEST_MAIN_WORKING_COLUMNS_V1":
    raise SystemExit("smallest MAIN working package schema moved")
if r.get("schema") != "STAGE33_11_REMAINING_BLOCK_REPRESENTATIVES_V1":
    raise SystemExit("remaining block representative schema moved")
if s.get("progress", {}).get("main_working_progress") != "5/26":
    raise SystemExit("smallest MAIN working progress moved")
if s.get("progress", {}).get("exact_exit_progress") != "0/26":
    raise SystemExit("MAIN overlay cannot promote exact closure")
if r.get("remaining_named_direction_count") != 21:
    raise SystemExit("remaining named direction count moved")
if not s.get("audit_debt", {}).get("required"):
    raise SystemExit("smallest MAIN working package must retain audit debt")

debt = s["audit_debt"]["directions"]
c = json.loads(CTRL.read_text(encoding="utf-8"))
children = {x["id"]: x for x in c["repair_children"]}
s11 = children["33-11"]
s12 = children["33-12"]

s11["status"] = "RUNNING_MAIN_5_OF_26_REMAINING_BLOCKS_PROFILED_AUDIT_DEBT"
s11["connecting_columns_explicitly_materialized"] = 5
s11["connecting_columns_main_working"] = 5
s11["connecting_columns_exact_audited"] = 0
s11["main_working_progress"] = "5/26"
s11["exact_exit_progress"] = "0/26"
s11["audit_debt_columns"] = debt
s11["smallest_main_working_columns"] = {
    "certificate_sha256": s["canonical_sha256"],
    "directions": debt,
    "working_absolute_value": "ZERO",
    "audit_required": True,
    "audit_question": s["audit_debt"]["question"],
}
s11["a2_26_main_working_column"] = {
    "certificate_sha256": w["canonical_sha256"],
    "working_absolute_value": w["main_working_convention"]["absolute_connecting_class_working_value"],
    "stronger_visible_boundary_certificate_available": True,
}
s11["remaining_block_reduction"] = {
    "certificate_sha256": r["canonical_sha256"],
    "remaining_named_directions": r["remaining_named_direction_count"],
    "remaining_cyclic_blocks": r["remaining_distinct_cyclic_submodule_count"],
    "priority_representatives_1based": r["priority_representatives_1based"],
    "priority_representative_names": r["priority_representative_names"],
}
for b in s11.get("branches", []):
    if b.get("id") == "33-11c":
        b["main_status"] = "RUNNING_MAIN_5_OF_26_REMAINING_BLOCK_REPRESENTATIVES_READY_AUDIT_DEBT"
        b["preferred_next_pointer"] = "first-remaining-block-representative"

s12["status"] = "BLOCKED_PENDING_33_11_COMPLETE_EXACT_COVERAGE"
s12["prerequisites_satisfied"] = False
s12["blocked_by"] = "33-11_EXACT_OPEN_0_OF_26_MAIN_WORKING_5_OF_26"

c["current_item"] = "Stage33-11_ARITHMETIC_LOCALIZATION_CONNECTING_MAP_RUNNING_MAIN_5_OF_26_BLOCKS_PROFILED"
c["audit_required"] = True
c["merge_allowed"] = False
c["advance_allowed"] = True
c["advance_scope"] = "STAGE33_11_MAIN_ATTACK_REMAINING_BLOCK_REPRESENTATIVES_WITH_SMALLEST_FIVE_AUDIT_DEBT"
c["next_item"] = "Stage33-11c_FIRST_REMAINING_BLOCK_REPRESENTATIVE"
c["next_expected_command"] = "Stage33-main-batch"
checkpoint = c.setdefault("controller_writeback_checkpoint", {})
checkpoint["stage33_11_main_working_progress"] = "5/26"
checkpoint["stage33_11_exact_exit_progress"] = "0/26"
checkpoint["stage33_11_audit_debt_columns"] = debt
checkpoint["stage33_11_smallest_main_working_columns_sha256"] = s["canonical_sha256"]
checkpoint["stage33_11_remaining_block_representatives_sha256"] = r["canonical_sha256"]
checkpoint["stage33_11_remaining_cyclic_blocks"] = r["remaining_distinct_cyclic_submodule_count"]
checkpoint["stage33_11_priority_representative_names"] = r["priority_representative_names"]
checkpoint["stage33_11_next_branch"] = "33-11c_FIRST_REMAINING_BLOCK_REPRESENTATIVE"

CTRL.write_text(json.dumps(c, indent=2, sort_keys=False) + "\n", encoding="utf-8")
print("STAGE33_11_MAIN_PROGRESS=5/26")
print("STAGE33_11_EXACT_PROGRESS=0/26")
print("REMAINING_BLOCKS=" + str(r["remaining_distinct_cyclic_submodule_count"]))
print("NEXT=FIRST_REMAINING_BLOCK_REPRESENTATIVE")
