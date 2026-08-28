#!/usr/bin/env python3
"""Freeze PR #1449 as a Stage33-11 audit handoff without promoting exact credit."""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
CTRL=ROOT/"stages"/"stage33"/"controller.json"
HAND=ROOT/"stages"/"stage33"/"33-11"/"audit-handoff-current-pr.json"
c=json.loads(CTRL.read_text(encoding="utf-8"))
h=json.loads(HAND.read_text(encoding="utf-8"))
if h.get("schema")!="STAGE33_11_AUDIT_HANDOFF_CURRENT_PR_V1": raise SystemExit("audit handoff schema moved")
children={z["id"]:z for z in c["repair_children"]}
s11=children["33-11"]; s12=children["33-12"]
s11["status"]="AUDIT_HANDOFF_MAIN_FROZEN_PENDING_HOSTILE_AUDIT"
s11["audit_required"]=True
s11["audit_passed"]=False
s11["repair_required"]=True
s11["main_working_progress"]="26/26"
s11["exact_exit_progress"]="0/26"
s11["connecting_columns_exact_audited"]=0
s11["main_working_map_complete"]=True
s11["main_working_map_exact_authoritative"]=False
s11["audit_handoff"]={
    "file":"stages/stage33/33-11/audit-handoff-current-pr.json",
    "pr":1449,
    "mode":"AUDIT_HANDOFF",
    "main_progression_frozen_in_this_pr":True,
    "remaining_purity_debt":"FINITE_CARRIER_PRIME_REFINEMENT_ONLY"
}
for b in s11.get("branches",[]):
    if b.get("id")=="33-11c":
        b["main_status"]="FROZEN_FOR_AUDIT_FINITE_CARRIER_PRIME_REFINEMENT_DEBT_ONLY"
        b["preferred_next_pointer"]="hostile-audit-current-pr-no-main-extension"
s12["status"]="BLOCKED_PENDING_33_11_COMPLETE_EXACT_COVERAGE"
s12["prerequisites_satisfied"]=False
c["current_item"]="Stage33-11_AUDIT_HANDOFF_PR1449_MAIN_FROZEN"
c["next_item"]="Stage33-11_HOSTILE_AUDIT_CURRENT_PR"
c["next_expected_command"]="Stage33-audit"
c["audit_required"]=True
c["merge_allowed"]=False
c["advance_allowed"]=False
c["stage33_08_released"]=False;c["stage33_08_release_allowed"]=False
c["stage33_40_released"]=False;c["stage33_40_release_allowed"]=False
c["theorem_credit"]=False;c["endpoint_credit"]=False;c["stage33_closed"]=False
c["perfect_cuboid_existence_claim"]=False;c["perfect_cuboid_nonexistence_claim"]=False
ck=c.setdefault("controller_writeback_checkpoint",{})
ck["stage33_11_mode"]="AUDIT_HANDOFF"
ck["stage33_11_main_progression_frozen_in_pr1449"]=True
ck["stage33_11_next_expected_command"]="Stage33-audit"
ck["stage33_11_exact_exit_progress"]="0/26"
ck["stage33_12_released"]=False
CTRL.write_text(json.dumps(c,indent=2,sort_keys=False)+"\n",encoding="utf-8")
print("STAGE33_11_MODE=AUDIT_HANDOFF")
print("MAIN_PROGRESSION_FROZEN_IN_PR1449=true")
print("NEXT_EXPECTED_COMMAND=Stage33-audit")
print("EXACT_EXIT_PROGRESS=0/26")
