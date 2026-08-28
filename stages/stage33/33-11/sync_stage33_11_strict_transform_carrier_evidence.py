#!/usr/bin/env python3
"""Overlay finite strict-transform carrier evidence into Stage33 controller."""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
CTRL=ROOT/"stages"/"stage33"/"controller.json"
CERT=ROOT/"stages"/"stage33"/"33-11"/"stage33-11-all-generator-strict-transform-carriers.json"
c=json.loads(CTRL.read_text(encoding="utf-8")); x=json.loads(CERT.read_text(encoding="utf-8"))
if x.get("schema")!="STAGE33_11_ALL_GENERATOR_STRICT_TRANSFORM_CARRIERS_V1": raise SystemExit("carrier schema moved")
summary=x.get("summary",{}); debt=x.get("audit_debt",{})
if summary.get("working_generator_coverage")!="14/14": raise SystemExit("carrier coverage incomplete")
if not summary.get("all_14_strict_transform_differences_zero_at_carrier_level"): raise SystemExit("strict carrier transport not exact")
if not debt.get("required"): raise SystemExit("carrier prime-refinement debt must remain")
children={z["id"]:z for z in c["repair_children"]}; s11=children["33-11"]; s12=children["33-12"]
s11["strict_transform_carrier_evidence"]={
 "coverage":"14/14",
 "certificate_sha256":x["canonical_sha256"],
 "distinct_global_normalized_linear_carriers":summary["distinct_global_normalized_linear_carriers"],
 "strict_transform_difference":"ZERO_EXACT_CARRIER_LEVEL_ALL_14",
 "exceptional_locus_difference":"ZERO_EXACT_ALL_14_WORKING_GENERATORS",
 "remaining_audit_debt":"FINITE_CARRIER_PRIME_REFINEMENT_ONLY",
 "audit_question":debt["narrowed_to"],
 "exact_stage33_11_columns_promoted":0,
}
for b in s11.get("branches",[]):
    if b.get("id")=="33-11c":
        b["main_status"]="ALL_14_STRICT_TRANSFORM_CARRIERS_EXACT_FINITE_PRIME_REFINEMENT_DEBT_ONLY"
        b["preferred_next_pointer"]="finite-carrier-prime-refinement-main-working"
s11["connecting_columns_exact_audited"]=0
s11["exact_exit_progress"]="0/26"
s11["audit_required"]=True
s12["status"]="BLOCKED_PENDING_33_11_COMPLETE_EXACT_COVERAGE"
s12["prerequisites_satisfied"]=False
c["current_item"]="Stage33-11_MAIN_STRICT_TRANSFORM_CARRIERS_MATERIALIZED_FINITE_PRIME_REFINEMENT_DEBT"
c["next_item"]="Stage33-11_MAIN_FINITE_CARRIER_PRIME_REFINEMENT"
c["next_expected_command"]="Stage33-main-batch"
c["merge_allowed"]=False;c["advance_allowed"]=False
c["stage33_08_released"]=False;c["stage33_08_release_allowed"]=False
c["stage33_40_released"]=False;c["stage33_40_release_allowed"]=False
c["theorem_credit"]=False;c["endpoint_credit"]=False;c["stage33_closed"]=False
c["perfect_cuboid_existence_claim"]=False;c["perfect_cuboid_nonexistence_claim"]=False
ck=c.setdefault("controller_writeback_checkpoint",{})
ck["stage33_11_strict_transform_carrier_sha256"]=x["canonical_sha256"]
ck["stage33_11_strict_transform_carrier_coverage"]="14/14"
ck["stage33_11_strict_transform_carrier_difference"]="ZERO_EXACT_CARRIER_LEVEL_ALL_14"
ck["stage33_11_remaining_purity_debt"]="FINITE_CARRIER_PRIME_REFINEMENT_ONLY"
ck["stage33_11_exact_exit_progress"]="0/26";ck["stage33_12_released"]=False
CTRL.write_text(json.dumps(c,indent=2,sort_keys=False)+"\n",encoding="utf-8")
print("STAGE33_11_STRICT_TRANSFORM_CARRIER_COVERAGE=14/14")
print("STRICT_TRANSFORM_DIFFERENCE=ZERO_EXACT_CARRIER_LEVEL_ALL_14")
print("REMAINING_AUDIT_DEBT=FINITE_CARRIER_PRIME_REFINEMENT_ONLY")
print("STAGE33_11_EXACT_PROGRESS=0/26")
