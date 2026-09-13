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
MONITOR=STAGE/"management/hpadj-04/PRODUCER-MONITOR.json"

STATE_BLOB="bead809db3a008dd35d664a8923f06fecb7de5bb"
STATE_CANON="460b04ecb09d41c1082aee46795acf5da79454df42cc6126a7b92925977855aa"
RECEIPT_BLOB="7a9d84f6ca137740aba01b6983a02a229dc13036"
RECEIPT_CANON="4de6317e2bde395de5aaa58036148e8dc1df1330d614f2143d8e15e7ede2e935"
REGISTRY_BLOB="75982b910ae1f149bc55b766f22ddea77db1f49e"
REGISTRY_CANON="470168bccfd4130b7de28002f40277002fcf6eda7f8d917b2df57f88879d0668"
EX5_STATE_BLOB="9935b06a5f9073ca4bb1b3d8e58b6f81f20a5bd6"
EX5_STATE_CANON="9f1a814a4a13181f98e85e7d42fc8dc66e1c6ad84508f651576ae5e7d2599e7c"
MONITOR_BLOB="c48f22a3567ce813881d9072a33cbaf48019d67a"
MONITOR_CANON="c8d671b441c489b30e3153218b4174f72b2daf214567ee5e100067ce92d2cdd3"

AUTH=47589703313957134649501
HPADJ_DEMAND="S32.DEMAND.HPADJ.EX5.FULL178_PICARD64.V1"
CUT192_DEMAND="S32.DEMAND.CUT192.EX5.DISJOINT_E8_PICARD64.V1"
HPADJ_V22_AUTH=47589703313957134804198
HPADJ_CHARGED=27104321327305699275487
OBSERVED_EX5_HEAD="5a0194c68136e794cb22f5e53f024ea8d26bcd88"
BC2_38_EXEC_HEAD="d26a27e8564458f3d575ec58601b2226fc23944f"
BC2_38_RUN=34742297972
BC2_38_JOB=103683975497

def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)

def blob(p):
    r=p.read_bytes()
    return hashlib.sha1(b"blob "+str(len(r)).encode()+b"\0"+r).hexdigest()

def canon(o):
    c=dict(o); c.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(c,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def lock(p,b,c):
    req(p.is_file(),f"missing {p.relative_to(ROOT)}")
    req(blob(p)==b,f"blob drift {p.relative_to(ROOT)}")
    o=json.loads(p.read_text())
    req(o.get("canonical_sha256_without_this_field")==c,f"stored canonical drift {p.relative_to(ROOT)}")
    req(canon(o)==c,f"canonical drift {p.relative_to(ROOT)}")
    return o

def demand(registry,did):
    hits=[d for d in registry["demands"] if d.get("demand_id")==did]
    req(len(hits)==1,f"demand identity drift {did}")
    return hits[0]

def main():
    s=lock(STATE,STATE_BLOB,STATE_CANON)
    r=lock(RECEIPT,RECEIPT_BLOB,RECEIPT_CANON)
    registry=lock(REGISTRY,REGISTRY_BLOB,REGISTRY_CANON)
    ex5=lock(EX5_STATE,EX5_STATE_BLOB,EX5_STATE_CANON)
    mon=lock(MONITOR,MONITOR_BLOB,MONITOR_CANON)
    f=s["current_exact_frontier"]

    req(f["authoritative_remaining_strata"]==17128 and f["authoritative_remaining_terminals"]==AUTH,"authority drift")
    for k in ("cut191_main_pruning_credit","cut193_main_pruning_credit","cut194_main_pruning_credit","cut195_main_pruning_credit","cut196_main_pruning_credit","cut197_main_pruning_credit","cut198_main_pruning_credit","n358_main_pruning_credit"):
        req(f[k] is True,f"consumed credit drift {k}")
    req(f["certlift03_main_pruning_credit"] is True and f["certlift03_incremental_rejected_terminals"]==154697,"CERTLIFT drift")
    req(f["cut199_main_pruning_credit"] is False,"CUT199 overcredit")
    req(r["composition"]["double_charge"] is False,"double charge")
    req(f["full178_numerical_census_complete"] is False and f["stage32_closed"] is False,"closure drift")
    req(s["firewalls"]["replacement_head_hostile_reaudit_required"] is True and s["firewalls"]["merge_authorized"] is False,"authority firewall drift")

    old=demand(registry,CUT192_DEMAND)
    req(old["status"]=="SATISFIED" and old["satisfying_artifact"]["blob_sha1"]=="b8ff5a4b962c24a6e4f4bca5621cbdb79f6d4781","CUT192 drift")
    hp=demand(registry,HPADJ_DEMAND)
    req(hp["status"]=="OPEN" and hp["priority"]=="P0_BLOCKING_DOWNSTREAM","HPADJ state drift")
    req(hp["producer_lane"]=="EX5" and hp["consumer_lane"]=="MAIN" and hp["satisfying_artifact"] is None,"HPADJ routing drift")
    pop=hp["source_population_semantics"]
    req(pop["authority_exact_head"]=="f8039b4ce479a4b91f2f0547e7049f629e9be5f5" and pop["authoritative_remaining_terminals"]==HPADJ_V22_AUTH,"HPADJ source drift")
    req(pop["affected_rows"]==178 and pop["charged_terminal_lower_bound"]==HPADJ_CHARGED,"HPADJ population drift")
    req(pop["hpadj01_main_pruning_credit"] is False and pop["population_drift_forbidden"] is True,"HPADJ firewall drift")

    req(ex5["schema"]=="STAGE32_EX5_CROSS_LANE_COORDINATION_STATE_V6_HPADJ_OPEN_BC2_38_RETAINED_QUARANTINED","EX5 schema drift")
    req(ex5["open_producer_demands"]==[HPADJ_DEMAND] and ex5["highest_priority_open_demand"]==HPADJ_DEMAND,"EX5 demand mirror drift")
    req(ex5["producer_acknowledged"] is False and ex5["producer_sync_required"] is True and ex5["producer_diversion_detected"] is True,"EX5 diversion drift")
    xo=ex5["producer_observation"]
    req(xo["producer_pr"]==1776 and xo["observed_exact_head"]==OBSERVED_EX5_HEAD,"EX5 head drift")
    req(xo["observed_registry_contains_hpadj_demand"] is False and xo["observed_open_producer_demands"]==[],"EX5 stale registry drift")
    req(xo["bc2_38_execution_head"]==BC2_38_EXEC_HEAD and xo["bc2_38_workflow_run"]==BC2_38_RUN and xo["bc2_38_compute_job"]==BC2_38_JOB,"BC2-38 identity drift")
    req(xo["bc2_38_execution_conclusion"]=="SUCCESS","BC2-38 not complete")
    req(xo["bc2_38_candidate_new_parent_unsat_count"]==4 and xo["bc2_38_candidate_remaining_unknown_count"]==30 and xo["bc2_38_candidate_sat_count"]==0,"BC2-38 result drift")
    req(xo["bc2_38_candidate_known_parent_unsat_lower_bound"]==7306,"BC2-38 lower bound drift")
    repair=ex5["required_repair"]
    req(repair["do_not_promote_or_audit_consume_bc2_38_before_coordination_repair"] is True and repair["quarantine_bc2_38_for_main_credit"] is True,"BC2-38 quarantine drift")
    req(repair["next_producer_command"]=="stage32ex5-mainbatch","producer command drift")
    for k in ("bc2_38_main_credit","bc2_38_178_credit","effectivity_credit","integral_irreducible_carrier_credit","endpoint_credit","merge_authorized"):
        req(ex5["credit_firewall"][k] is False,f"EX5 credit firewall opened {k}")

    req(mon["schema"]=="STAGE32_MAIN_HPADJ04_EX5_PRODUCER_SYNC_MONITOR_V4_BC2_38_RETAINED_QUARANTINED","monitor schema drift")
    req(mon["status"]=="EX5_BC2_38_RETAINED_P0_PREEMPTION_VIOLATION_QUARANTINED_MAIN_WAIT","monitor status drift")
    mo=mon["producer_observation"]
    req(mo["observed_exact_head"]==OBSERVED_EX5_HEAD and mo["bc2_38_execution_conclusion"]=="SUCCESS","monitor producer/result drift")
    req(mo["bc2_38_artifact_id"]==10313851431 and mo["bc2_38_checkpoint_blob_sha1"]=="91eca02054cd2dbf702dd4a7635398ef76ee832f","BC2-38 retained identity drift")
    vio=mon["violation"]
    req(vio["producer_diversion_violation_asserted"] is True and vio["bc2_38_retained_result_quarantined_for_main_credit"] is True,"quarantine assertion missing")
    req(vio["bc2_38_result_does_not_satisfy_hpadj_demand"] is True and vio["bc2_38_hostile_audit_must_not_bypass_coordination_repair"] is True,"promotion bypass firewall drift")
    ci=mon["observed_ci"]
    req(ci["producer_retained_head_main_startup_conclusion"]=="FAILURE" and ci["producer_retained_head_claim_frontier_conclusion"]=="FAILURE","producer governance failure evidence drift")
    req(ci["producer_retained_head_ex5_integrity_conclusion"]=="SUCCESS" and ci["producer_retained_head_stale_run_sweeper_conclusion"]=="SUCCESS","producer retained CI drift")
    req(mon["next_gate"]["next_producer_command"]=="stage32ex5-mainbatch" and mon["next_gate"]["main_remains_blocked"] is True,"next gate drift")
    for k,v in mon["firewalls"].items():
        req(v is False,f"HPADJ04 firewall opened {k}")

    print(json.dumps({
      "verdict":"PASS_STAGE32_CROSS_LANE_HPADJ_EX5_BC2_38_RETAINED_QUARANTINED",
      "authoritative_remaining_terminals":AUTH,
      "open_p0_demand":HPADJ_DEMAND,
      "producer_pr":1776,
      "observed_producer_head":OBSERVED_EX5_HEAD,
      "bc2_38_candidate_unsat":4,
      "bc2_38_candidate_unknown":30,
      "bc2_38_main_credit":False,
      "bc2_38_quarantined":True,
      "required_producer_command":"stage32ex5-mainbatch",
      "main_waiting":True,
      "full178_complete":False,
      "replacement_head_hostile_reaudit_required":True,
      "merge_authorized":False
    },sort_keys=True))

if __name__=="__main__":
    main()
