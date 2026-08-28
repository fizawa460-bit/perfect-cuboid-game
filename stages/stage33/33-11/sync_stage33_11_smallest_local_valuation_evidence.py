#!/usr/bin/env python3
"""Overlay smallest-block local exact valuation evidence without exact closure."""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
CTRL=ROOT/"stages"/"stage33"/"controller.json"
HERE=ROOT/"stages"/"stage33"/"33-11"
LOCAL=HERE/"stage33-11-smallest-direct-exceptional-valuations.json"
WORK=HERE/"stage33-11-smallest-main-working-columns.json"
local=json.loads(LOCAL.read_text(encoding="utf-8")); work=json.loads(WORK.read_text(encoding="utf-8"))
if local.get("schema")!="STAGE33_11_SMALLEST_DIRECT_EXCEPTIONAL_VALUATIONS_V1": raise SystemExit("local schema moved")
if local.get("exact_local_consequence",{}).get("coverage")!="5/5": raise SystemExit("local coverage incomplete")
if local.get("exact_local_consequence",{}).get("all_five_exceptional_locus_differences")!="ZERO_EXACT": raise SystemExit("local difference moved")
if work.get("schema")!="STAGE33_11_SMALLEST_MAIN_WORKING_COLUMNS_V2": raise SystemExit("working schema moved")
if work.get("progress",{}).get("exact_exit_progress")!="0/26": raise SystemExit("refuse unaudited exact promotion")
if not work.get("audit_debt",{}).get("required"): raise SystemExit("audit debt missing")
c=json.loads(CTRL.read_text(encoding="utf-8"))
children={x["id"]:x for x in c["repair_children"]}; s11=children["33-11"]; s12=children["33-12"]
s11["smallest_local_exceptional_valuation_evidence"]={
    "directions":["A2_02","A2_03","A2_24","A2_25","A2_26"],
    "coverage":"5/5","all_48_blowup_centers_each":True,
    "exceptional_locus_galois_difference":"ZERO_EXACT_ALL_FIVE",
    "certificate_sha256":local["canonical_sha256"],
    "main_working_columns_sha256":work["canonical_sha256"],
    "exact_stage33_11_columns_promoted":0,
    "audit_debt_remaining":work["audit_debt"]["narrowed_to"],
}
for b in s11.get("branches",[]):
    if b.get("id")=="33-11c":
        b["main_status"]="SMALLEST_5_LOCAL_EXCEPTIONAL_VALUATIONS_EXACT_MAIN_WORKING_PURITY_DEBT_REMAINS"
        b["preferred_next_pointer"]="remaining-21-mixed-order-block-orbit-production"
s11["audit_required"]=True
s11["audit_passed"]=False
s11["exact_exit_progress"]="0/26"
s12["status"]="BLOCKED_PENDING_33_11_COMPLETE_EXACT_COVERAGE"; s12["prerequisites_satisfied"]=False
c["current_item"]="Stage33-11_MAIN_SMALLEST_5_LOCAL_VALUATIONS_DONE_REMAINING_BLOCK_NEXT"
c["next_item"]="Stage33-11_REMAINING_21_MIXED_ORDER_BLOCK_ORBIT_PRODUCTION"
c["next_expected_command"]="Stage33-main-batch"
c["merge_allowed"]=False; c["advance_allowed"]=False
c["stage33_08_released"]=False; c["stage33_08_release_allowed"]=False
c["stage33_40_released"]=False; c["stage33_40_release_allowed"]=False
c["theorem_credit"]=False; c["endpoint_credit"]=False; c["stage33_closed"]=False
cp=c.setdefault("controller_writeback_checkpoint",{})
cp["stage33_11_smallest_local_exceptional_valuation_sha256"]=local["canonical_sha256"]
cp["stage33_11_smallest_local_exceptional_valuation_coverage"]="5/5"
cp["stage33_11_smallest_exceptional_locus_difference"]="ZERO_EXACT_ALL_FIVE"
cp["stage33_11_smallest_main_working_columns_v2_sha256"]=work["canonical_sha256"]
cp["stage33_11_exact_exit_progress"]="0/26"; cp["stage33_12_released"]=False
CTRL.write_text(json.dumps(c,indent=2,sort_keys=False)+"\n",encoding="utf-8")
print("STAGE33_11_SMALLEST_LOCAL_VALUATIONS=5/5")
print("STAGE33_11_EXACT_PROGRESS=0/26")
print("NEXT=REMAINING_21_MIXED_ORDER_BLOCK_ORBIT_PRODUCTION")
