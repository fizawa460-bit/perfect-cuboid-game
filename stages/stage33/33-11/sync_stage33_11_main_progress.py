#!/usr/bin/env python3
"""Overlay MAIN development progress after the exact Stage33-11 checkpoint sync."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CTRL = ROOT / "stages" / "stage33" / "controller.json"
WORKING = ROOT / "stages" / "stage33" / "33-11" / "stage33-11-a2-26-main-working-column.json"

w = json.loads(WORKING.read_text(encoding="utf-8"))
if w.get("schema") != "STAGE33_11_A2_26_MAIN_WORKING_COLUMN_V1":
    raise SystemExit("A2_26 MAIN working certificate schema moved")
if not w.get("progress", {}).get("main_working_column_materialized"):
    raise SystemExit("A2_26 MAIN working column missing")
if w.get("progress", {}).get("exact_audited_column_materialized"):
    raise SystemExit("MAIN overlay cannot promote exact closure")
if not w.get("audit_debt", {}).get("required"):
    raise SystemExit("A2_26 audit debt must remain explicit")

c = json.loads(CTRL.read_text(encoding="utf-8"))
children = {x["id"]: x for x in c["repair_children"]}
s11 = children["33-11"]
s12 = children["33-12"]

s11["status"] = "RUNNING_MAIN_1_OF_26_AUDIT_DEBT"
s11["connecting_columns_explicitly_materialized"] = 1
s11["connecting_columns_main_working"] = 1
s11["connecting_columns_exact_audited"] = 0
s11["main_working_progress"] = "1/26"
s11["exact_exit_progress"] = "0/26"
s11["audit_debt_columns"] = ["A2_26"]
s11["a2_26_main_working_column"] = {
    "certificate_sha256": w["canonical_sha256"],
    "working_absolute_value": w["main_working_convention"]["absolute_connecting_class_working_value"],
    "audit_required": True,
    "audit_question": w["audit_debt"]["question"],
}
for b in s11.get("branches", []):
    if b.get("id") == "33-11c":
        b["main_status"] = "RUNNING_MAIN_1_OF_26_A2_26_WORKING_AUDIT_DEBT"
        b["preferred_next_pointer"] = "component-A2_25"

s12["status"] = "BLOCKED_PENDING_33_11_COMPLETE_EXACT_COVERAGE"
s12["prerequisites_satisfied"] = False
s12["blocked_by"] = "33-11_EXACT_OPEN_0_OF_26_MAIN_WORKING_1_OF_26"

c["current_item"] = "Stage33-11_ARITHMETIC_LOCALIZATION_CONNECTING_MAP_RUNNING_MAIN_1_OF_26"
c["audit_required"] = True
c["merge_allowed"] = False
c["advance_allowed"] = True
c["advance_scope"] = "STAGE33_11_MAIN_CONTINUE_NEXT_NAMED_DIRECTION_WITH_A2_26_AUDIT_DEBT"
c["next_item"] = "Stage33-11c_A2_25_MAIN_CONNECTING_COLUMN"
c["next_expected_command"] = "Stage33-main-batch"
checkpoint = c.setdefault("controller_writeback_checkpoint", {})
checkpoint["stage33_11_main_working_progress"] = "1/26"
checkpoint["stage33_11_exact_exit_progress"] = "0/26"
checkpoint["stage33_11_audit_debt_columns"] = ["A2_26"]
checkpoint["stage33_11_a2_26_main_working_column_sha256"] = w["canonical_sha256"]
checkpoint["stage33_11_next_branch"] = "33-11c_A2_25_MAIN_CONNECTING_COLUMN"

CTRL.write_text(json.dumps(c, indent=2, sort_keys=False) + "\n", encoding="utf-8")
print("STAGE33_11_MAIN_PROGRESS=1/26")
print("STAGE33_11_EXACT_PROGRESS=0/26")
print("NEXT=A2_25")
