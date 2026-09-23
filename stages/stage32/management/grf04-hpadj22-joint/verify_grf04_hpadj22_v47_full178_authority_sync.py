#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
STATE=ROOT/"stages/stage32/MAIN-STATE.json"
PROD=ROOT/"stages/stage32/residual-32-01-production/state.json"
ACTIVE=ROOT/"stages/stage32/proof/ACTIVE-FRONTIER.json"
REGISTRY=ROOT/"stages/stage32/proof/CLAIM-REGISTRY.json"
ADAPTERS=ROOT/"stages/stage32/proof/LANE-ADAPTERS.json"
FINAL=ROOT/"stages/stage32/FINAL-CHECK.json"
GOAL=ROOT/"stages/stage32/GOAL_AND_STOP_CONTRACT.md"
RECEIPT=HERE/"GRF04-HPADJ22-V47-FULL178-AUTHORITY-SYNC.json"

RECEIPT_BLOB="e05c27a247d61cfa58c500c011f4e71ccaefd655"
RECEIPT_CANON="40109b916cf8403205691d7cc05635ce18b61dacfc8577e64da86105b1045094"
PROD_BLOB="4660a1ba3bc7b96237c0723cf48a47da7185fead"
ACTIVE_BLOB="2515c3591f9ccf88474b7cfdf6f9c7bf54ec8798"
REGISTRY_BLOB="862e12ddf95e02c5d4907adba76e73e99400cd92"
ADAPTERS_BLOB="d44fc98a0777ccd739142e44b5c597710563a333"
FINAL_BLOB="761a775989615a28f57054d1794c273eb2ed0c59"
GOAL_BLOB="336d6680af220a1eacce9b24d08a96ace12c4848"
AUDITED_HEAD="620b90d1ca1f5316d55b88b2620f78eeba1949c7"
AUDIT_REVIEW=5287562192
RUN_ID=35816698218
ARTIFACT_ID=10733557553
ARTIFACT_ZIP_SHA256="a0930b1291b6ac43a53e510cf22a89d9e0b248dfd0895ccbf0316463a34367fa"
AGG_CANON="9de69a0af40f11f67f8d41cbf1cd82161357d3f0c417b999d7c8d969ec57c422"
OLD_BOUND=138652739800650593494
NEW_BOUND=128645575147764659235
TIGHTENING=10007164652885934259

def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)

def blob(p:Path)->str:
    b=p.read_bytes()
    return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()

def canon(o:dict)->str:
    x=dict(o);x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def load_locked_json(path:Path,expected_blob:str,label:str):
    req(path.is_file(),"missing "+label)
    req(blob(path)==expected_blob,label+" blob drift")
    return json.loads(path.read_text(encoding="utf-8"))

def main():
    rec=load_locked_json(RECEIPT,RECEIPT_BLOB,"V47 authority-sync receipt")
    req(rec.get("canonical_sha256_without_this_field")==RECEIPT_CANON and canon(rec)==RECEIPT_CANON,"receipt canonical")
    req(rec["status"]=="HOSTILE_AUDITED_FULL178_EXACT_AGGREGATE_RETAINED_FOR_AUTHORITY_SYNC","receipt status")
    ex=rec["execution"]
    req(ex["pr"]==1826 and ex["exact_head"]==AUDITED_HEAD and ex["workflow_run_id"]==RUN_ID and ex["aggregate_artifact_id"]==ARTIFACT_ID,"execution identity")
    req(ex["artifact_zip_sha256"]==ARTIFACT_ZIP_SHA256 and ex["aggregate_canonical_sha256"]==AGG_CANON,"artifact identity")
    au=rec["hostile_audit"]
    req(au["status"]=="PASS" and au["review_id"]==AUDIT_REVIEW and au["audited_exact_head"]==AUDITED_HEAD and au["authority_sync_permitted"] is True,"audit binding")
    cov=rec["coverage"]
    req(cov=={"bands":8,"chunks_per_band":4,"row_windows":3,"parents":96,"rows":178,"row_chunk_certificates":2967,"gaps":0,"overlaps":0,"all_bands_strict":True},"coverage")
    a=rec["authority"]
    req(int(a["predecessor_upper_bound"])==OLD_BOUND and int(a["same_population_joint_upper_bound"])==NEW_BOUND and int(a["exact_tightening"])==TIGHTENING,"authority totals")
    req(OLD_BOUND-NEW_BOUND==TIGHTENING and NEW_BOUND<OLD_BOUND,"strict tightening arithmetic")
    req(a["composition_rule"]=="SAME_POPULATION_EXACT_INTERSECTION_BOUND_REPLACEMENT__NO_ADDITIVE_SUBTRACTION","composition")
    req(a["additive_subtraction"] is False and a["min_of_counts"] is False and a["statistical_independence"] is False and a["double_charge"] is False,"composition firewalls")

    prod=load_locked_json(PROD,PROD_BLOB,"FULL178 production state")
    req(prod["schema"]=="STAGE32_RESIDUAL32_01_PRODUCTION_STATE_V71_FULL178_AUDIT_SYNCED","production schema")
    req(prod["FULL_D176_D192_NUMERICAL_ORBIT_CENSUS"] is True and prod["R29_LG2_NUMERICAL_COMPONENT_COMPLETE"] is True and prod["full178_numerical_picard_leaf_checks_complete"] is True,"production completion flags")
    req(prod["R29_LG2"]=="NOT_DISCHARGED" and prod["THEOREM_CREDIT"] is False and prod["RECEIVER_CREDIT"] is False,"production downstream firewall")

    active=load_locked_json(ACTIVE,ACTIVE_BLOB,"active frontier")
    by={c["claim_id"]:c for c in active["claims"]}
    num=by["S32.FULL178.NUMERICAL_CENSUS.V2"]
    req(num["authority_status"]=="AUDITED" and num["frontier_status"]=="AUDITED_TRUE" and num["blockers"]==[],"active numerical claim status")
    req(num["audit_receipt"]=={"status":"PASS","pr":1826,"review_id":AUDIT_REVIEW,"exact_head":AUDITED_HEAD},"active numerical audit")
    goal=by["S32.GOAL.STAGE32_CLOSURE.V2"]
    req(goal["authority_status"]=="DECLARED_GOAL" and "S32.FULL178.NUMERICAL_CENSUS.V2" in goal["requires"],"closure successor goal")
    req(len(goal["blockers"])>=3,"closure blockers preserved")

    reg=load_locked_json(REGISTRY,REGISTRY_BLOB,"claim registry")
    rb={c["claim_id"]:c for c in reg["claims"]}
    milestone=rb["S32.PROOF.NUMERICAL_CENSUS.V1"]
    req(milestone["authority_status"]=="AUDITED","reserved numerical milestone")
    req(milestone["audit_receipt"]=={"status":"PASS","pr":1826,"review_id":AUDIT_REVIEW,"exact_head":AUDITED_HEAD},"reserved milestone audit")
    req("STAGE32_CLOSED=true." in milestone["does_not_prove"],"milestone closure firewall")

    adapters=load_locked_json(ADAPTERS,ADAPTERS_BLOB,"lane adapters")
    lanes={x["lane"]:x for x in adapters["lanes"]}
    req("S32.FULL178.NUMERICAL_CENSUS.V2" in lanes["MAIN"]["active_frontier_refs"],"MAIN numerical ref")
    req(lanes["32-01-178"]["active_frontier_refs"]==["S32.FULL178.NUMERICAL_CENSUS.V2"],"178 numerical ref")
    req(lanes["CUT"]["active_frontier_refs"]==["S32.FULL178.NUMERICAL_CENSUS.V2"],"CUT numerical ref")
    req(lanes["MB"]["active_frontier_refs"]==["S32.GOAL.STAGE32_CLOSURE.V2"],"MB closure ref")

    final=load_locked_json(FINAL,FINAL_BLOB,"FINAL-CHECK")
    req(final["declared_stage32_closure_goal"]=="S32.GOAL.STAGE32_CLOSURE.V2","final closure goal")
    req(final["current_expected_status"]=="NOT_READY","final remains not ready")
    req(final["required_milestones"][0]["required_claim_id"]=="S32.PROOF.NUMERICAL_CENSUS.V1","final numerical slot")

    req(blob(GOAL)==GOAL_BLOB,"goal contract drift")

    st=json.loads(STATE.read_text(encoding="utf-8"))
    req(canon(st)==st.get("canonical_sha256_without_this_field"),"MAIN state canonical")
    req(st["schema"]=="STAGE32_MAIN_COMPACT_STATE_V47_GRF04_HPADJ22_FULL178_AUDIT_SYNCED","MAIN schema")
    f=st["current_exact_frontier"]
    req(f["authoritative_remaining_strata"]==17128 and f["authoritative_remaining_terminals"]==NEW_BOUND,"MAIN authority")
    req(f["authoritative_remaining_terminals_semantics"]=="CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET","MAIN authority semantics")
    req(f["full178_numerical_census_complete"] is True,"MAIN census completion")
    req(f["v47_grf04_hpadj22_joint_upper_bound"]==NEW_BOUND and f["v47_exact_tightening_vs_v46"]==TIGHTENING,"V47 frontier totals")
    req(st["current"]["next_exact_route"]=="EFFECTIVITY_AND_MULTIBRANCH_THEN_FINAL_SYNTHESIS","next route")
    req(st["current"]["active_missing_interface"]=="EFFECTIVITY_MULTIBRANCH_AND_FINAL_MILESTONE_CHAIN","missing interface")
    locks=st["source_locks"]["v47_grf04_hpadj22_full178_authority_sync"]
    req(locks["receipt_blob_sha1"]==RECEIPT_BLOB and locks["production_state_blob_sha1"]==PROD_BLOB and locks["active_frontier_blob_sha1"]==ACTIVE_BLOB and locks["claim_registry_blob_sha1"]==REGISTRY_BLOB and locks["lane_adapters_blob_sha1"]==ADAPTERS_BLOB,"MAIN V47 locks")
    for k in ("full178_complete","effectivity_released","receiver_credit","route_credit","theorem_credit","endpoint_credit","stage32_closed","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim","merge_authorized"):
        req(st["firewalls"][k] is False,"downstream firewall "+k)
    print("PASS: Stage32 MAIN V47 consumes hostile-audited FULL178 numerical census and advances only to effectivity/multibranch")
if __name__=="__main__":
    main()
