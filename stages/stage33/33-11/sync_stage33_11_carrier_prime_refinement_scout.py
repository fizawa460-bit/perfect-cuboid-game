#!/usr/bin/env python3
"""Overlay finite carrier prime-refinement scout into Stage33 controller."""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
CTRL=ROOT/"stages"/"stage33"/"controller.json"
CERT=ROOT/"stages"/"stage33"/"33-11"/"stage33-11-carrier-prime-refinement-scout.json"
c=json.loads(CTRL.read_text()); x=json.loads(CERT.read_text())
if x.get("schema")!="STAGE33_11_CARRIER_PRIME_REFINEMENT_SCOUT_V1": raise SystemExit("prime-refinement scout schema moved")
s=x["summary"]
if s.get("carrier_count")!=30 or not s.get("all_unresolved_carriers_explicitly_enumerated"): raise SystemExit("prime-refinement inventory incomplete")
children={z["id"]:z for z in c["repair_children"]}; s11=children["33-11"]; s12=children["33-12"]
s11["carrier_prime_refinement_scout"]={
 "certificate_sha256":x["canonical_sha256"],
 "carrier_count":30,
 "cc_orbit_count":s["cc_orbit_count"],
 "forced_refinement_carrier_count":s["forced_refinement_carrier_count"],
 "unresolved_carrier_count":s["unresolved_carrier_count"],
 "unresolved_carrier_ids":s["unresolved_carrier_ids"],
 "status":"FINITE_UNRESOLVED_CARRIER_LIST_EXACTLY_ENUMERATED",
 "exact_stage33_11_columns_promoted":0,
}
for b in s11.get("branches",[]):
    if b.get("id")=="33-11c":
        b["main_status"]="CARRIER_PRIME_REFINEMENT_SCOUT_DONE_FINITE_UNRESOLVED_LIST"
        b["preferred_next_pointer"]="factor-unresolved-carrier-orbit-representatives"
s11["connecting_columns_exact_audited"]=0;s11["exact_exit_progress"]="0/26";s11["audit_required"]=True
s12["status"]="BLOCKED_PENDING_33_11_COMPLETE_EXACT_COVERAGE";s12["prerequisites_satisfied"]=False
c["current_item"]="Stage33-11_MAIN_CARRIER_PRIME_REFINEMENT_SCOUT_DONE"
c["next_item"]="Stage33-11_MAIN_FACTOR_UNRESOLVED_CARRIER_ORBIT_REPRESENTATIVES"
c["next_expected_command"]="Stage33-main-batch"
c["merge_allowed"]=False;c["advance_allowed"]=False
c["stage33_08_released"]=False;c["stage33_08_release_allowed"]=False;c["stage33_40_released"]=False;c["stage33_40_release_allowed"]=False
c["theorem_credit"]=False;c["endpoint_credit"]=False;c["stage33_closed"]=False
c["perfect_cuboid_existence_claim"]=False;c["perfect_cuboid_nonexistence_claim"]=False
ck=c.setdefault("controller_writeback_checkpoint",{})
ck["stage33_11_carrier_prime_refinement_scout_sha256"]=x["canonical_sha256"]
ck["stage33_11_carrier_prime_refinement_total"]=30
ck["stage33_11_carrier_prime_refinement_forced"]=s["forced_refinement_carrier_count"]
ck["stage33_11_carrier_prime_refinement_unresolved"]=s["unresolved_carrier_count"]
ck["stage33_11_exact_exit_progress"]="0/26";ck["stage33_12_released"]=False
CTRL.write_text(json.dumps(c,indent=2,sort_keys=False)+"\n")
print(f"CARRIERS=30 FORCED={s['forced_refinement_carrier_count']} UNRESOLVED={s['unresolved_carrier_count']}")
print("STAGE33_11_EXACT_PROGRESS=0/26")
