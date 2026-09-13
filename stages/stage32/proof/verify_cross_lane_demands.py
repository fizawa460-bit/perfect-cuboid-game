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
CONSUMER=STAGE/"management/hpadj-05/CONSUMER-REENTRY.json"

STATE_BLOB="bead809db3a008dd35d664a8923f06fecb7de5bb"
STATE_CANON="460b04ecb09d41c1082aee46795acf5da79454df42cc6126a7b92925977855aa"
RECEIPT_BLOB="7a9d84f6ca137740aba01b6983a02a229dc13036"
RECEIPT_CANON="4de6317e2bde395de5aaa58036148e8dc1df1330d614f2143d8e15e7ede2e935"
REGISTRY_BLOB="e2949866d41a78ff9169bdb23a2fcefb6d0f5dcd"
REGISTRY_CANON="a5a85f824ba8fe466dbd13a7118bc0e95220cd5925d2af273653d86746a71228"
EX5_STATE_BLOB="99151c6b5402e2ed12dfe268bd497935d5be1b3c"
EX5_STATE_CANON="3400c1f6a145445b615a1c425b6f0637b0cbe2364626933a4d7fe385a3a2ee29"
MONITOR_BLOB="d3585fde4aae17769c3123341412f075f175e34a"
MONITOR_CANON="58e39b1554b2df236ad4122ae20f1f2815cfa4169066c64bae9e301af40cd4b6"
CONSUMER_BLOB="b6c1fb139fdb4189b8b5dbe351ace27f3a6748ad"
CONSUMER_CANON="a064c6d95aaf19f2b2b0515143722da50fdd307c7fbd608b98bcf0c9f2be9ee1"

AUTH=47589703313957134649501
HPADJ_DEMAND="S32.DEMAND.HPADJ.EX5.FULL178_PICARD64.V1"
CUT192_DEMAND="S32.DEMAND.CUT192.EX5.DISJOINT_E8_PICARD64.V1"
HPADJ_V22_AUTH=47589703313957134804198
HPADJ_CHARGED=27104321327305699275487
OBSERVED_EX5_HEAD="5a0194c68136e794cb22f5e53f024ea8d26bcd88"
BC2_38_EXEC_HEAD="d26a27e8564458f3d575ec58601b2226fc23944f"
BC2_38_RUN=34742297972
BC2_38_JOB=103683975497
REENTRY_HEAD="ff4eadbc88c40560c4e47399e745e1abe6aa2553"
RETAINED_REPLAY_HEAD="3721175b58c577863b391fe01ed2ff882b06ff19"
RETAINED_REPLAY_RUN=34749790481
RETAINED_REPLAY_JOB=103704104616

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
    consumer=lock(CONSUMER,CONSUMER_BLOB,CONSUMER_CANON)
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
    req(hp["status"]=="SATISFIED" and hp["priority"]=="P0_BLOCKING_DOWNSTREAM","HPADJ state drift")
    req(hp["producer_lane"]=="EX5" and hp["consumer_lane"]=="MAIN" and isinstance(hp["satisfying_artifact"],dict),"HPADJ routing drift")
    pop=hp["source_population_semantics"]
    req(pop["authority_exact_head"]=="f8039b4ce479a4b91f2f0547e7049f629e9be5f5" and pop["authoritative_remaining_terminals"]==HPADJ_V22_AUTH,"HPADJ source drift")
    req(pop["affected_rows"]==178 and pop["charged_terminal_lower_bound"]==HPADJ_CHARGED,"HPADJ population drift")
    req(pop["hpadj01_main_pruning_credit"] is False and pop["population_drift_forbidden"] is True,"HPADJ firewall drift")

    req(ex5["schema"]=="STAGE32_EX5_CROSS_LANE_COORDINATION_STATE_V7_HPADJ_SATISFIED_HISTORICAL_DIVERSION_PRESERVED","EX5 schema drift")
    req(ex5["open_producer_demands"]==[] and ex5["highest_priority_open_demand"] is None,"EX5 demand mirror drift")
    req(ex5["producer_acknowledged"] is True and ex5["producer_sync_required"] is False and ex5["producer_diversion_detected"] is True,"EX5 diversion drift")

    sat=hp["satisfying_artifact"]
    req(sat["blob_sha1"]=="3e21202c813220c59a6831dd7645f612112a2415" and sat["canonical_sha256"]=="34eef4777e706a2fec9b55e6473f469c9bbb0351ba0741d588c132d7772173cf","satisfaction receipt identity")
    handoff=lock(ROOT/sat["path"],sat["blob_sha1"],sat["canonical_sha256"])
    interface=lock(ROOT/sat["interface_path"],sat["interface_blob_sha1"],sat["interface_canonical_sha256"])
    req(sat["interface_blob_sha1"]=="8a30e3aa30777460f344eb19836dc725dd442329","producer interface identity")
    req(handoff["demand_id"]==HPADJ_DEMAND and interface["demand_id"]==HPADJ_DEMAND,"handoff demand identity")
    req(sat["audit_review_id"] is None and sat["audited_exact_head"] is None,"operational handoff asserted audit")
    req(handoff["source_population"]["charged_terminal_lower_bound"]==HPADJ_CHARGED and handoff["source_population"]["affected_rows"]==178,"handoff population identity")
    req(handoff["source_population"]["hpadj01_result_blob_sha1"]==pop["population_source_blob_sha1"],"handoff source identity")
    req(interface["population_cardinality_replay"]["charged_terminal_lower_bound"]==HPADJ_CHARGED and interface["population_cardinality_replay"]["affected_rows"]==178,"interface population identity")
    req(interface["terminal_identity_or_exact_rank_unrank_contract"]["rank_unrank_roundtrip_exact"] is True,"rank/unrank contract")
    req(interface["stored_10_exceptional_coordinate_identity"]["stored_exceptional_coordinate_count"]==10,"stored exceptional identity")
    im=interface["terminal_to_picard64_map"]
    req(im["inverse_denominator"]==8 and im["terminal_pairing_count"]==11 and im["free_pairing_parameter_count"]==53 and im["full_picard64_coordinate_count"]==64,"Picard64 map dimensions")
    req(interface["reconstructed_picard64_coordinate_identity"]["terminal_alone_asserts_completion_exists"] is False,"completion overclaim")
    req(all(v is False for v in handoff["credit_firewall"].values()) and all(v is False for v in interface["credit_firewall"].values()),"handoff credit promotion")

    req(sat["consumer_reentry_head"]==REENTRY_HEAD and sat["consumer_reentry_pr"]==1800,"consumer reentry identity")
    req(sat["consumer_reentry_receipt_path"]=="stages/stage32/management/hpadj-05/CONSUMER-REENTRY.json","consumer receipt path")
    req(sat["consumer_reentry_receipt_blob_sha1"]==CONSUMER_BLOB and sat["consumer_reentry_receipt_canonical_sha256"]==CONSUMER_CANON,"consumer receipt identity")
    req(consumer["status"]=="VALIDATED_OPERATIONAL_HANDOFF_NO_MATH_CREDIT" and consumer["demand_id"]==HPADJ_DEMAND,"consumer receipt status")
    req(consumer["consumer_reentry"]["operational_handoff_validated"] is True and consumer["consumer_reentry"]["producer_interface_rebuilt_by_main"] is False,"consumer reentry semantics")
    req(consumer["population_validation"]["affected_rows"]==178 and consumer["population_validation"]["charged_terminal_lower_bound"]==HPADJ_CHARGED,"consumer population validation")
    req(consumer["producer_retained_replay"]["retained_head"]==RETAINED_REPLAY_HEAD and consumer["producer_retained_replay"]["workflow_run"]==RETAINED_REPLAY_RUN and consumer["producer_retained_replay"]["job_id"]==RETAINED_REPLAY_JOB and consumer["producer_retained_replay"]["conclusion"]=="SUCCESS","producer retained replay receipt")
    req(consumer["consumer_reentry"]["next_mathematical_gap"]=="ACTUAL_INTEGRAL_IRREDUCIBLE_CARRIER_SEMANTICS","next mathematical gap")
    req(all(v is False for v in consumer["credit_firewall"].values()),"consumer credit firewall")

    req(ex5["historical_diversion_observation_preserved"] is True and ex5["coordination_repair_complete"] is True,"historical/current split")
    xo=ex5["producer_observation"]
    req(xo["producer_pr"]==1776 and xo["observed_exact_head"]==OBSERVED_EX5_HEAD,"EX5 head drift")
    req(xo["observed_registry_contains_hpadj_demand"] is False and xo["observed_open_producer_demands"]==[],"EX5 stale registry drift")
    req(xo["bc2_38_execution_head"]==BC2_38_EXEC_HEAD and xo["bc2_38_workflow_run"]==BC2_38_RUN and xo["bc2_38_compute_job"]==BC2_38_JOB,"BC2-38 identity drift")
    req(xo["bc2_38_execution_conclusion"]=="SUCCESS","BC2-38 not complete")
    req(xo["bc2_38_candidate_new_parent_unsat_count"]==4 and xo["bc2_38_candidate_remaining_unknown_count"]==30 and xo["bc2_38_candidate_sat_count"]==0,"BC2-38 result drift")
    req(xo["bc2_38_candidate_known_parent_unsat_lower_bound"]==7306,"BC2-38 lower bound drift")
    repair=ex5["required_repair"]
    req(repair["do_not_promote_or_audit_consume_bc2_38_before_coordination_repair"] is True and repair["quarantine_bc2_38_for_main_credit"] is True,"BC2-38 quarantine drift")
    for k in ("bc2_38_main_credit","bc2_38_178_credit","effectivity_credit","integral_irreducible_carrier_credit","endpoint_credit","merge_authorized"):
        req(ex5["credit_firewall"][k] is False,f"EX5 credit firewall opened {k}")

    req(mon["schema"]=="STAGE32_MAIN_HPADJ04_EX5_PRODUCER_SYNC_MONITOR_V5_CONSUMER_REENTRY_VALIDATED","monitor schema drift")
    req(mon["status"]=="HPADJ_CONSUMER_REENTRY_VALIDATED_OPERATIONAL_HISTORICAL_QUARANTINE_PRESERVED","monitor status drift")
    req(mon["current_handoff_observation"]["mainbatch_consumer_validation_performed"] is True,"monitor consumer validation")
    req(mon["current_handoff_observation"]["consumer_reentry_receipt_blob_sha1"]==CONSUMER_BLOB,"monitor consumer receipt")
    mo=mon["producer_observation"]
    req(mo["observed_exact_head"]==OBSERVED_EX5_HEAD and mo["bc2_38_execution_conclusion"]=="SUCCESS","monitor producer/result drift")
    req(mo["bc2_38_artifact_id"]==10313851431 and mo["bc2_38_checkpoint_blob_sha1"]=="91eca02054cd2dbf702dd4a7635398ef76ee832f","BC2-38 retained identity drift")
    vio=mon["violation"]
    req(vio["producer_diversion_violation_asserted"] is True and vio["bc2_38_retained_result_quarantined_for_main_credit"] is True,"quarantine assertion missing")
    req(vio["bc2_38_result_does_not_satisfy_hpadj_demand"] is True and vio["bc2_38_hostile_audit_must_not_bypass_coordination_repair"] is True,"promotion bypass firewall drift")
    ci=mon["observed_ci"]
    req(ci["producer_retained_replay_head"]==RETAINED_REPLAY_HEAD and ci["producer_retained_replay_run"]==RETAINED_REPLAY_RUN and ci["producer_retained_replay_job"]==RETAINED_REPLAY_JOB and ci["producer_retained_replay_conclusion"]=="SUCCESS","retained replay monitor drift")
    ng=mon["next_gate"]
    req(ng["main_remains_blocked"] is False and ng["next_main_mathematical_gap"]=="ACTUAL_INTEGRAL_IRREDUCIBLE_CARRIER_SEMANTICS","consumer reentry gate drift")
    req(ng["next_producer_command"]=="stage32ex5-audit" and ng["replacement_head_hostile_reaudit_still_required"] is True,"independent audit gate drift")
    for k,v in mon["firewalls"].items():
        req(v is False,f"HPADJ04 firewall opened {k}")

    print(json.dumps({
      "verdict":"PASS_STAGE32_HPADJ_MAIN_CONSUMER_REENTRY_VALIDATED",
      "authoritative_remaining_terminals":AUTH,
      "satisfied_p0_demand":HPADJ_DEMAND,
      "consumer_reentry_head":REENTRY_HEAD,
      "consumer_reentry_receipt_blob":CONSUMER_BLOB,
      "producer_retained_replay_head":RETAINED_REPLAY_HEAD,
      "producer_retained_replay_run":RETAINED_REPLAY_RUN,
      "bc2_38_main_credit":False,
      "bc2_38_quarantined":True,
      "main_consumer_reentry_required":False,
      "next_mathematical_gap":"ACTUAL_INTEGRAL_IRREDUCIBLE_CARRIER_SEMANTICS",
      "next_gap_owner":"32-02/MAIN_GEOMETRY",
      "full178_complete":False,
      "replacement_head_hostile_reaudit_required":True,
      "merge_authorized":False
    },sort_keys=True))

if __name__=="__main__":
    main()
