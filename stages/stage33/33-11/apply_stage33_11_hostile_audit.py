#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CTRL = ROOT / "stages" / "stage33" / "controller.json"
AUDIT = ROOT / "stages" / "stage33" / "33-11" / "audit-state.json"

a = json.loads(AUDIT.read_text(encoding="utf-8"))
if a.get("schema") != "STAGE33_11_HOSTILE_AUDIT_STATE_V1":
    raise SystemExit("Stage33-11 hostile audit schema moved")
if a.get("verdict") != "FAIL_REPAIR_REQUIRED":
    raise SystemExit("hostile audit overlay only supports the recorded FAIL verdict")
if a.get("exact_progress_after_audit") != "0/26":
    raise SystemExit("hostile audit exact progress moved")
if a.get("merge_allowed") or a.get("advance_allowed") or not a.get("repair_required"):
    raise SystemExit("hostile audit firewalls moved")

c = json.loads(CTRL.read_text(encoding="utf-8"))
children = {x["id"]: x for x in c["repair_children"]}
s11 = children["33-11"]
s12 = children["33-12"]

c["status"] = "STAGE33_01_TO_06_AUDITED_CLOSED_33_07_REPAIR_33_09_33_10_CLOSED_33_11_HOSTILE_AUDIT_FAIL_REPAIR_REQUIRED_33_08_BLOCKED"
c["repair_required"] = True

s11["status"] = "HOSTILE_AUDIT_FAIL_UNPROVEN_EQUIVARIANT_GLOBAL_LIFT_PINS"
s11["source_direction_exact_now"] = 0
s11["connecting_columns_explicitly_materialized"] = 0
s11["connecting_columns_exact_audited"] = 0
s11["exact_exit_progress"] = "0/26"
s11["main_working_map_exact_authoritative"] = False
s11["audit_required"] = False
s11["audit_passed"] = False
s11["repair_required"] = True
s11["hostile_audit"] = {
    "verdict": "FAIL_REPAIR_REQUIRED",
    "audit_state": "stages/stage33/33-11/audit-state.json",
    "audited_head": a["audited_head"],
    "retained_exact_boundary": "A2_26_FIVE_DIMENSION_FINITE_H1_REDUCTION_PLUS_FIVE_BIT_DECODER_PLUS_VISIBLE_BOUNDARY_V4_FIXITY",
    "rejected_working_assumptions": [
        "PIN_OFFBOUNDARY_PURITY_CORRECTION_Q_DEFINED_V4_FIXED_PENDING_AUDIT",
        "PIN_Q_DEFINED_GLOBAL_GERSTEN_REPRESENTATIVE_PENDING_AUDIT",
    ],
    "failure_reason": "VISIBLE_BOUNDARY_V4_FIXED_DOES_NOT_IMPLY_V4_FIXED_GLOBAL_GERSTEN_LIFT_OR_OFFBOUNDARY_CORRECTION; ASSUMING_SUCH_A_LIFT_FORCES_THE_CONNECTING_OBSTRUCTION_ZERO_BY_CONSTRUCTION",
    "nonzero_connecting_map_claimed": False,
}
for b in s11.get("branches", []):
    if b.get("id") == "33-11c":
        b["main_status"] = "REPAIR_A2_26_COMPUTE_ACTUAL_GERSTEN_GALOIS_DIFFERENCE_BITS"
        b["preferred_next_pointer"] = "A2_26_EXPLICIT_CC_CT_GERSTEN_GALOIS_DIFFERENCE_BITS"

s12["status"] = "BLOCKED_PENDING_33_11_COMPLETE_EXACT_COVERAGE"
s12["prerequisites_satisfied"] = False
s12["blocked_by"] = "33-11_HOSTILE_AUDIT_FAIL_EXACT_PROGRESS_0_OF_26"

c["current_item"] = "Stage33-11_HOSTILE_AUDIT_FAIL_REPAIR_A2_26_EXPLICIT_DIFFERENCE_BITS"
c["audit_required"] = False
c["merge_allowed"] = False
c["advance_allowed"] = False
c["advance_scope"] = "REPAIR_CURRENT_33_11_ONLY_NO_33_12_NO_33_08_NO_33_40_PLUS"
c["repair_scope_allowed"] = "STAGE33_11_ONLY"
c["next_item"] = "Stage33-11c_A2_26_COMPUTE_EXPLICIT_CC_CT_GERSTEN_GALOIS_DIFFERENCE_BITS"
c["next_expected_command"] = "Stage33-main-batch"

c["stage33_08_released"] = False
c["stage33_08_release_allowed"] = False
c["stage33_40_released"] = False
c["stage33_40_release_allowed"] = False
c["theorem_credit"] = False
c["endpoint_credit"] = False
c["stage33_closed"] = False
c["brauer_manin_set_empty_proved"] = False
c["perfect_cuboid_existence_claim"] = False
c["perfect_cuboid_nonexistence_claim"] = False

cp = c.setdefault("controller_writeback_checkpoint", {})
cp["pr"] = 1449
cp["hostile_audit_verdict"] = "FAIL_REPAIR_REQUIRED"
cp["hostile_audit_state"] = "stages/stage33/33-11/audit-state.json"
cp["hostile_audit_audited_head"] = a["audited_head"]
cp["stage33_11_status"] = "HOSTILE_AUDIT_FAIL_REPAIR_REQUIRED"
cp["stage33_11_certified_named_connecting_progress"] = "0/26"
cp["stage33_11_retained_a2_26_five_bit_decoder"] = True
cp["stage33_11_rejected_working_zero_map_as_exact_evidence"] = True
cp["stage33_11_next_branch"] = "A2_26_EXPLICIT_CC_CT_GERSTEN_GALOIS_DIFFERENCE_BITS"
cp["stage33_08_released"] = False
cp["theorem_credit"] = False
cp["endpoint_credit"] = False

CTRL.write_text(json.dumps(c, indent=2, sort_keys=False) + "\n", encoding="utf-8")
print("STAGE33_11_HOSTILE_AUDIT=FAIL_REPAIR_REQUIRED")
print("STAGE33_11_EXACT_PROGRESS=0/26")
print("NEXT_ITEM=" + c["next_item"])
