#!/usr/bin/env python3
"""Overlay nine remaining cyclic-block representative local valuations."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
CTRL=ROOT/"stages"/"stage33"/"controller.json"
HERE=ROOT/"stages"/"stage33"/"33-11"
LOCAL=HERE/"stage33-11-remaining-representative-direct-exceptional-valuations.json"
x=json.loads(LOCAL.read_text(encoding="utf-8"))
if x.get("schema")!="STAGE33_11_REMAINING_REPRESENTATIVE_DIRECT_EXCEPTIONAL_VALUATIONS_V1": raise SystemExit("remaining representative local schema moved")
con=x.get("exact_local_consequence",{})
if con.get("coverage")!="9/9" or con.get("all_nine_representative_exceptional_locus_differences")!="ZERO_EXACT": raise SystemExit("remaining representative local coverage incomplete")
reps=["A2_04","A2_01","A2_07","A2_05","A2_10","A2_08","A2_09","A2_16","A2_15"]
if x.get("directions")!=reps: raise SystemExit("remaining representative ordering moved")
c=json.loads(CTRL.read_text(encoding="utf-8")); children={v["id"]:v for v in c["repair_children"]}; s11=children["33-11"]; s12=children["33-12"]
s11["remaining_block_representative_local_exceptional_valuation_evidence"]={"representatives":reps,"coverage":"9/9","all_48_blowup_centers_each":True,"exceptional_locus_galois_difference":"ZERO_EXACT_ALL_NINE_REPRESENTATIVES","certificate_sha256":x["canonical_sha256"],"exact_stage33_11_columns_promoted":0,"audit_debt_remaining":x["audit_debt"]["remaining"]}
for b in s11.get("branches",[]):
    if b.get("id")=="33-11c":
        b["main_status"]="ALL_14_WORKING_GENERATORS_LOCAL_EXCEPTIONAL_VALUATIONS_EXACT_PURITY_DEBT_REMAINS"
        b["preferred_next_pointer"]="main-working-map-retained-audit-debt-no-33-12-release"
s11["audit_required"]=True; s11["audit_passed"]=False; s11["exact_exit_progress"]="0/26"
s12["status"]="BLOCKED_PENDING_33_11_COMPLETE_EXACT_COVERAGE"; s12["prerequisites_satisfied"]=False
c["current_item"]="Stage33-11_MAIN_ALL_14_GENERATOR_LOCAL_VALUATIONS_DONE_AUDIT_DEBT_REMAINS"
c["next_item"]="Stage33-11_MAIN_WORKING_MAP_RETAINED_AUDIT_DEBT"
c["next_expected_command"]="Stage33-main-batch"
c["merge_allowed"]=False; c["advance_allowed"]=False
for k in ("stage33_08_released","stage33_08_release_allowed","stage33_40_released","stage33_40_release_allowed","theorem_credit","endpoint_credit","stage33_closed"):
    c[k]=False
cp=c.setdefault("controller_writeback_checkpoint",{})
cp["stage33_11_remaining_representative_local_exceptional_valuation_sha256"]=x["canonical_sha256"]
cp["stage33_11_remaining_representative_local_coverage"]="9/9"
cp["stage33_11_working_generator_local_coverage"]="14/14"
cp["stage33_11_exact_exit_progress"]="0/26"; cp["stage33_12_released"]=False
CTRL.write_text(json.dumps(c,indent=2,sort_keys=False)+"\n",encoding="utf-8")
print("STAGE33_11_REMAINING_REP_LOCAL_VALUATIONS=9/9")
print("STAGE33_11_WORKING_GENERATOR_LOCAL_VALUATIONS=14/14")
print("STAGE33_11_EXACT_PROGRESS=0/26")
