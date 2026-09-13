#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
STAGE=HERE.parent
ROOT=STAGE.parents[1]
STATE=STAGE/"MAIN-STATE.json"
RECEIPT=STAGE/"management/post-certlift03-current-v22-composition-consumption-20260913.json"
REGISTRY=HERE/"CROSS-LANE-DEMANDS.json"
EX5_STATE=ROOT/"stages/stage32-ex5/CROSS-LANE-STATE.json"
MONITOR=STAGE/"management/hpadj-04/PRODUCER-MONITOR.json"

STATE_BLOB="bead809db3a008dd35d664a8923f06fecb7de5bb"
STATE_CANON="460b04ecb09d41c1082aee46795acf5da79454df42cc6126a7b92925977855aa"
RECEIPT_BLOB="7a9d84f6ca137740aba01b6983a02a229dc13036"
RECEIPT_CANON="4de6317e2bde395de5aaa58036148e8dc1df1330d614f2143d8e15e7ede2e935"
REGISTRY_BLOB="75982b910ae1f149bc55b766f22ddea77db1f49e"
REGISTRY_CANON="470168bccfd4130b7de28002f40277002fcf6eda7f8d917b2df57f88879d0668"
EX5_STATE_BLOB="0006aa15d3971d993eee4b3c33fc3a15004ce891"
EX5_STATE_CANON="4afb71a75c11647fe5dd0b27f080e4bdc90e970a33d45db46e0fa25a24b95f47"
MONITOR_BLOB="1b3e2bb96058a4e03dc522a16ca9a6ed8b80cab8"
MONITOR_CANON="d28370cb9af18ee5afd427e3445ae1a0765d6bd52e30aa2177c2f999ceafc123"

AUTH=47589703313957134649501
HPADJ_DEMAND="S32.DEMAND.HPADJ.EX5.FULL178_PICARD64.V1"
CUT192_DEMAND="S32.DEMAND.CUT192.EX5.DISJOINT_E8_PICARD64.V1"
HPADJ_V22_AUTH=47589703313957134804198
HPADJ_CHARGED=27104321327305699275487
OBSERVED_EX5_HEAD="d26a27e8564458f3d575ec58601b2226fc23944f"
BC2_37_AUDIT_REVIEW=5189412496
BC2_38_RUN=34742297972
BC2_38_JOB=103683975497

def req(v,m):
    if not v:
        raise SystemExit("FAIL: "+m)

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
    monitor=lock(MONITOR,MONITOR_BLOB,MONITOR_CANON)
    f=s["current_exact_frontier"]

    req(f["authoritative_remaining_strata"]==17128 and f["authoritative_remaining_terminals"]==AUTH,"authority drift")
    for k in ("cut191_main_pruning_credit","cut193_main_pruning_credit","cut194_main_pruning_credit","cut195_main_pruning_credit","cut196_main_pruning_credit","cut197_main_pruning_credit","cut198_main_pruning_credit","n358_main_pruning_credit"):
        req(f[k] is True,f"consumed credit drift {k}")
    req(f["certlift03_main_pruning_credit"] is True and f["certlift03_incremental_rejected_terminals"]==154697,"CERTLIFT coordination drift")
    req(f["cut199_main_pruning_credit"] is False,"CUT199 overcredit")
    req(f["n372_candidate_hostile_audited"] is True and f["n372_candidate_hostile_audit_review_id"]==5187357950,"N372 audit drift")
    req(f["n372_main_pruning_credit"] is False and f["n372_full178_credit"] is False and f["n372_effectivity_final_credit"] is False,"N372 overcredit")
    req(r["composition"]["double_charge"] is False and r["composition"]["cut199_main_pruning_credit"] is False,"CERTLIFT composition drift")
    req(f["full178_numerical_census_complete"] is False and f["stage32_closed"] is False,"closure drift")
    req(s["firewalls"]["replacement_head_hostile_reaudit_required"] is True and s["firewalls"]["merge_authorized"] is False,"authority firewall drift")

    old=demand(registry,CUT192_DEMAND)
    req(old["status"]=="SATISFIED" and old["satisfying_artifact"]["blob_sha1"]=="b8ff5a4b962c24a6e4f4bca5621cbdb79f6d4781","CUT192 retained demand drift")

    hp=demand(registry,HPADJ_DEMAND)
    req(hp["status"]=="OPEN" and hp["priority"]=="P0_BLOCKING_DOWNSTREAM","HPADJ demand state drift")
    req(hp["producer_lane"]=="EX5" and hp["consumer_lane"]=="MAIN" and hp["satisfying_artifact"] is None,"HPADJ routing drift")
    pop=hp["source_population_semantics"]
    req(pop["authority_exact_head"]=="f8039b4ce479a4b91f2f0547e7049f629e9be5f5" and pop["authority_hostile_reaudit_review_id"]==5188224290,"HPADJ authority lock drift")
    req(pop["authoritative_remaining_strata"]==17128 and pop["authoritative_remaining_terminals"]==HPADJ_V22_AUTH,"HPADJ source count drift")
    req(pop["affected_rows"]==178 and pop["charged_terminal_lower_bound"]==HPADJ_CHARGED,"HPADJ population count drift")
    req(pop["hpadj01_main_pruning_credit"] is False and pop["population_drift_forbidden"] is True,"HPADJ population firewall drift")

    req(ex5["open_producer_demands"]==[HPADJ_DEMAND] and ex5["highest_priority_open_demand"]==HPADJ_DEMAND,"EX5 demand mirror drift")
    req(ex5["coordination_priority"]=="P0_BLOCKING_DOWNSTREAM" and ex5["local_route_priority"]=="P2_NORMAL","EX5 priority mirror drift")
    req(ex5["local_route_deferred_while_demand_open"] is True,"EX5 defer rule drift")
    req(ex5["producer_acknowledged"] is False and ex5["producer_sync_required"] is True and ex5["producer_diversion_detected"] is True,"EX5 producer diversion state drift")
    obs=ex5["producer_observation"]
    req(obs["producer_pr"]==1776 and obs["observed_exact_head"]==OBSERVED_EX5_HEAD,"EX5 producer observation drift")
    req(obs["observed_registry_contains_hpadj_demand"] is False and obs["observed_open_producer_demands"]==[],"EX5 stale registry observation drift")
    req(obs["bc2_37_hostile_audit_review_id"]==BC2_37_AUDIT_REVIEW and obs["bc2_37_hostile_audit_consumed"] is True,"BC2-37 audit consumption drift")
    req(obs["bc2_38_execution_authorized"] is True and obs["bc2_38_workflow_run"]==BC2_38_RUN and obs["bc2_38_compute_job"]==BC2_38_JOB,"BC2-38 execution identity drift")
    req(obs["post_demand_new_lower_priority_research_detected"] is True,"EX5 diversion not recorded")
    repair=ex5["required_repair"]
    req(repair["stop_new_p2_research"] is True and repair["do_not_promote_bc2_38_to_main"] is True,"EX5 repair firewall drift")
    req(repair["synchronize_current_cross_lane_registry"] is True and repair["acknowledge_hpadj_p0_before_next_local_research"] is True,"EX5 sync repair drift")
    req(repair["next_producer_command"]=="stage32ex5-mainbatch","EX5 repair command drift")
    for k in ("demand_acknowledgement_grants_math_credit","demand_satisfaction_grants_math_credit","main_waiting_grants_math_credit","bc2_38_main_credit","effectivity_credit","integral_irreducible_carrier_credit","endpoint_credit","merge_authorized"):
        req(ex5["credit_firewall"][k] is False,f"EX5 credit firewall opened {k}")

    req(monitor["status"]=="EX5_P0_PREEMPTION_VIOLATION_MAIN_FAIL_CLOSED_WAIT","HPADJ04 monitor status drift")
    mo=monitor["producer_observation"]
    req(mo["producer_pr"]==1776 and mo["observed_exact_head"]==OBSERVED_EX5_HEAD,"monitor producer identity drift")
    req(mo["producer_cross_lane_sync_performed"] is False and mo["bc2_38_execution_authorized"] is True,"monitor producer sync drift")
    vio=monitor["violation"]
    req(vio["producer_diversion_violation_asserted"] is True and vio["new_lower_priority_research_after_demand_detected"] is True,"producer diversion assertion missing")
    req(vio["violated_contract_field"]=="producer_open_demand_must_preempt_lower_priority_local_work","producer contract identity drift")
    req(vio["local_route_priority"]=="P2_NORMAL" and vio["blocking_route_priority"]=="P0_BLOCKING_DOWNSTREAM","producer priority comparison drift")
    req(vio["bc2_38_must_not_be_promoted_to_main"] is True and vio["bc2_38_result_does_not_satisfy_hpadj_demand"] is True,"BC2-38 promotion firewall drift")
    ci=monitor["observed_ci"]
    req(ci["producer_head_main_startup_run"]==34742297976 and ci["producer_head_main_startup_conclusion"]=="FAILURE","producer MAIN startup failure evidence drift")
    req(ci["producer_head_claim_frontier_run"]==34742297971 and ci["producer_head_claim_frontier_conclusion"]=="FAILURE","producer claim frontier failure evidence drift")
    ng=monitor["next_gate"]
    req(ng["next_producer_command"]=="stage32ex5-mainbatch" and ng["main_remains_blocked"] is True,"producer repair sequencing drift")
    for k,v in monitor["firewalls"].items():
        req(v is False,f"HPADJ04 firewall opened {k}")

    print(json.dumps({
        "verdict":"PASS_STAGE32_CROSS_LANE_HPADJ_EX5_P0_PREEMPTION_VIOLATION_FAIL_CLOSED",
        "authoritative_remaining_terminals":AUTH,
        "open_p0_demand":HPADJ_DEMAND,
        "producer_lane":"EX5",
        "producer_pr":1776,
        "observed_producer_head":OBSERVED_EX5_HEAD,
        "producer_diversion_detected":True,
        "diverted_local_route":"BC2_38_REFINE_REMAINING_FRESH_UNKNOWN_SET",
        "bc2_38_main_credit":False,
        "required_producer_command":"stage32ex5-mainbatch",
        "main_waiting":True,
        "main_pruning_credit":False,
        "full178_complete":False,
        "replacement_head_hostile_reaudit_required":True,
        "merge_authorized":False
    },sort_keys=True))

if __name__=="__main__":
    main()
