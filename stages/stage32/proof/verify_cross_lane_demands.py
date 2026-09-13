#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path

HERE=Path(__file__).resolve().parent
STAGE=HERE.parent
ROOT=STAGE.parents[1]
STATE=STAGE/"MAIN-STATE.json"
RECEIPT=STAGE/"management/post-certlift03-current-v22-composition-consumption-20260913.json"
REGISTRY=HERE/"CROSS-LANE-DEMANDS.json"
EX5_STATE=ROOT/"stages/stage32-ex5/CROSS-LANE-STATE.json"

STATE_BLOB="bead809db3a008dd35d664a8923f06fecb7de5bb"
STATE_CANON="460b04ecb09d41c1082aee46795acf5da79454df42cc6126a7b92925977855aa"
RECEIPT_BLOB="7a9d84f6ca137740aba01b6983a02a229dc13036"
RECEIPT_CANON="4de6317e2bde395de5aaa58036148e8dc1df1330d614f2143d8e15e7ede2e935"
REGISTRY_BLOB="75982b910ae1f149bc55b766f22ddea77db1f49e"
REGISTRY_CANON="470168bccfd4130b7de28002f40277002fcf6eda7f8d917b2df57f88879d0668"
EX5_STATE_BLOB="4f5b88d6ac546c2489e0325c20c881dc722c772d"
EX5_STATE_CANON="a17fb31f9bf222f0b7d7307f0f62a4ddcc68ec0459762ec07365384057332d76"

AUTH=47589703313957134649501
HPADJ_DEMAND="S32.DEMAND.HPADJ.EX5.FULL178_PICARD64.V1"
CUT192_DEMAND="S32.DEMAND.CUT192.EX5.DISJOINT_E8_PICARD64.V1"
HPADJ_V22_AUTH=47589703313957134804198
HPADJ_CHARGED=27104321327305699275487

def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)

def blob(p):
    r=p.read_bytes()
    return hashlib.sha1(b"blob "+str(len(r)).encode()+b"\0"+r).hexdigest()

def canon(o):
    c=dict(o)
    c.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(c,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def lock(p,b,c):
    req(p.is_file(),f"missing {p.relative_to(ROOT)}")
    req(blob(p)==b,f"blob drift {p.relative_to(ROOT)}")
    o=json.loads(p.read_text())
    req(o.get("canonical_sha256_without_this_field")==c,f"stored canonical drift {p.relative_to(ROOT)}")
    req(canon(o)==c,f"canonical drift {p.relative_to(ROOT)}")
    return o

def demand(registry,demand_id):
    hits=[d for d in registry["demands"] if d.get("demand_id")==demand_id]
    req(len(hits)==1,f"demand identity drift {demand_id}")
    return hits[0]

def main():
    s=lock(STATE,STATE_BLOB,STATE_CANON)
    r=lock(RECEIPT,RECEIPT_BLOB,RECEIPT_CANON)
    registry=lock(REGISTRY,REGISTRY_BLOB,REGISTRY_CANON)
    ex5=lock(EX5_STATE,EX5_STATE_BLOB,EX5_STATE_CANON)
    f=s["current_exact_frontier"]

    req(f["authoritative_remaining_strata"]==17128 and f["authoritative_remaining_terminals"]==AUTH,"authority drift")
    for k in ("cut191_main_pruning_credit","cut193_main_pruning_credit","cut194_main_pruning_credit","cut195_main_pruning_credit","cut196_main_pruning_credit","cut197_main_pruning_credit","cut198_main_pruning_credit","n358_main_pruning_credit"):
        req(f[k] is True,f"consumed credit drift {k}")
    req(f["certlift03_main_pruning_credit"] is True and f["certlift03_incremental_rejected_terminals"]==154697,"CERTLIFT coordination drift")
    req(f["cut199_main_pruning_credit"] is False,"CUT199 overcredit")
    req(f["n372_candidate_hostile_audited"] is True and f["n372_candidate_hostile_audit_review_id"]==5187357950,"N372 audit drift")
    req(f["n372_current_authority_rebased"] is True and f["n372_current_authority_witness"] is True and f["n372_survives_batch_cut193_cut197_cut198"] is True and f["n372_survives_certlift03"] is True,"N372 current authority drift")
    req(f["n372_main_pruning_credit"] is False and f["n372_full178_credit"] is False and f["n372_effectivity_final_credit"] is False,"N372 overcredit")
    req(r["composition"]["double_charge"] is False and r["composition"]["cut199_main_pruning_credit"] is False,"CERTLIFT composition drift")
    req(r["claim_sync"]["semantic_claim_core_changed"] is False and r["claim_sync"]["active_frontier_remap"] is False,"claim sync semantic drift")
    req(f["full178_numerical_census_complete"] is False and f["stage32_closed"] is False,"closure drift")
    req(s["firewalls"]["replacement_head_hostile_reaudit_required"] is True,"replacement re-audit gate missing")
    req(s["firewalls"]["merge_authorized"] is False,"merge authorized")

    old=demand(registry,CUT192_DEMAND)
    req(old["status"]=="SATISFIED" and old["producer_lane"]=="EX5" and old["consumer_lane"]=="CUT","CUT192 retained demand drift")
    req(old["satisfying_artifact"]["blob_sha1"]=="b8ff5a4b962c24a6e4f4bca5621cbdb79f6d4781","CUT192 receipt drift")

    hp=demand(registry,HPADJ_DEMAND)
    req(hp["status"]=="OPEN","HPADJ demand not OPEN")
    req(hp["priority"]=="P0_BLOCKING_DOWNSTREAM","HPADJ demand priority drift")
    req(hp["producer_lane"]=="EX5" and hp["consumer_lane"]=="MAIN","HPADJ routing drift")
    req(hp["satisfying_artifact"] is None,"HPADJ demand unexpectedly satisfied")
    pop=hp["source_population_semantics"]
    req(pop["authority_exact_head"]=="f8039b4ce479a4b91f2f0547e7049f629e9be5f5","HPADJ authority head drift")
    req(pop["authority_hostile_reaudit_review_id"]==5188224290,"HPADJ authority review drift")
    req(pop["authoritative_remaining_strata"]==17128 and pop["authoritative_remaining_terminals"]==HPADJ_V22_AUTH,"HPADJ source authority count drift")
    req(pop["population_source_blob_sha1"]=="520b6b0f230e23fb5ea34b80fef591cfa5f9be4b","HPADJ source blob drift")
    req(pop["population_source_canonical_sha256"]=="9773c11e87de149b5b56438fd1c86929aa54a971601bf8306855fd0f8a303506","HPADJ source canonical drift")
    req(pop["affected_rows"]==178 and pop["charged_terminal_lower_bound"]==HPADJ_CHARGED,"HPADJ population count drift")
    req(pop["hpadj01_main_pruning_credit"] is False and pop["population_drift_forbidden"] is True,"HPADJ credit/population firewall drift")

    req(ex5["open_producer_demands"]==[HPADJ_DEMAND],"EX5 open-demand mirror drift")
    req(CUT192_DEMAND in ex5["satisfied_producer_demands"],"EX5 lost CUT192 satisfied demand")
    req(ex5["highest_priority_open_demand"]==HPADJ_DEMAND,"EX5 priority mirror drift")
    req(ex5["coordination_priority"]=="P0_BLOCKING_DOWNSTREAM","EX5 coordination priority drift")
    req(ex5["local_route_deferred_while_demand_open"] is True and ex5["producer_acknowledged"] is True,"EX5 producer acknowledgement/defer drift")
    req(ex5["source_population_lock"]["affected_rows"]==178 and ex5["source_population_lock"]["charged_terminal_lower_bound"]==HPADJ_CHARGED,"EX5 population lock drift")
    for k in ("demand_acknowledgement_grants_math_credit","demand_satisfaction_grants_math_credit","effectivity_credit","integral_irreducible_carrier_credit","endpoint_credit","merge_authorized"):
        req(ex5["credit_firewall"][k] is False,f"EX5 credit firewall opened {k}")

    print(json.dumps({
        "verdict":"PASS_STAGE32_CROSS_LANE_DEMAND_COORDINATION_V23_CERTLIFT03_HPADJ_EX5_P0",
        "authoritative_remaining_terminals":AUTH,
        "open_p0_demand":HPADJ_DEMAND,
        "producer_lane":"EX5",
        "hpadj_source_rows":178,
        "hpadj_charged_terminal_lower_bound":HPADJ_CHARGED,
        "ex5_local_route_deferred":True,
        "demand_grants_math_credit":False,
        "full178_complete":False,
        "replacement_head_hostile_reaudit_required":True,
        "merge_authorized":False
    },sort_keys=True))

if __name__=="__main__":
    main()
