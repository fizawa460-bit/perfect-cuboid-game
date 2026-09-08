#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
STATE_PATH=HERE/"MAIN-STATE.json"

def req(c,m):
    if not c: raise SystemExit(f"FAIL: {m}")

def main():
    s=json.loads(STATE_PATH.read_text())
    req(s["schema"]=="STAGE32EX5_MAIN_COMPACT_STATE_V1_EX5_07_XSTAGE_BLOCKED","schema drift")
    req(s["stage"]=="32EX5","wrong stage")
    req(s["execution"]["main_command"]=="stage32ex5-mainbatch","main command drift")
    req(s["bootstrap"]["active_work_pr"]==1710 and s["bootstrap"]["merge_authorized"] is False,"PR/merge contract drift")
    req(s["bootstrap"]["base_main_sha"]=="f2a89e613cdf91191a0aada9e90c9fc93373a6c6","freshness base drift")
    cc=s["completion_contract"]
    req(set(cc["allowed_terminal_outcomes"])=={"QUALIFIED_INDEPENDENT_STAGE32_ROUTE_ESTABLISHED","FROZEN_BREADTH_PACKAGE_EXHAUSTED_WITHOUT_QUALIFIED_ROUTE"},"terminal contract drift")
    req(cc["blocked_route_is_stage_exhaustion"] is False,"blocked route cannot exhaust stage")
    req(cc["EX5_route_decision_closure_is_Stage32_full_target_closure"] is False,"EX5 closure cannot equal Stage32 closure")
    f=s["frontier"]
    for k in ["EX5_00_source_lock_complete","receiver_population_contract_complete","receiver_ledger_complete","receiver_ledger_coverage_certified","current_coverage_dependency_graph_complete","clean_room_candidate_universe_frozen","arsenal_dedup_complete","route_scorecard_complete","primary_route_selected","executable_route_contracts_complete","primary_microdiagnostic_complete"]: req(f[k] is True,f"completion flag lost {k}")
    for k in ["nontrivial_receiver_effect_obtained","qualified_independent_route_established","frozen_breadth_package_exhausted","audit_ready_EX5_route_decision_closure","EX5_route_decision_closure"]: req(f[k] is False,f"future credit pregranted {k}")
    req(f["terminal_outcome"] is None,"terminal outcome pregranted")
    r=s["route_families"]
    req(r["primary_route_id"]=="EX5R-XSTAGE-001" and r["primary_route_status"]=="BLOCKED","XSTAGE status drift")
    req(r["primary_route_blocker_code"]=="XSTAGE_MISSING_EXACT_NONEMPTY_MB_SUBSET_ADAPTER","blocker drift")
    req(r["next_selected_route_id"]=="EX5R-EFC-001","EFC must be next")
    req(r["primary_microdiagnostic_artifact"]=="stages/stage32-ex5/ex5-07-xstage-preflight-01.json","artifact path drift")
    req(r["primary_microdiagnostic_verifier"]=="stages/stage32-ex5/verify_ex5_07_xstage_preflight_01.py","verifier path drift")
    req(r["backup_route_ids"]==["EX5R-EFC-001","EX5R-EHS-001"],"backup drift")
    req(r["scratch_results_authoritative"] is False,"scratch authority drift")
    rc=s["receiver_contract"]
    req(rc["row_count"]==185 and rc["status_counts"]=={"CLOSED":5,"OPEN":180,"UNKNOWN":0,"CONDITIONAL":0,"OUT_OF_SCOPE":0},"receiver ledger drift")
    req(rc["V6_O210_Q602_treated_as_definition_of_all_receivers"] is False,"V6 scope firewall lost")
    cur=s["current"]
    req(cur["status"]=="EX5_07_XSTAGE_PREFLIGHT_BLOCKED_RETAINED","current status drift")
    req(cur["leaf"]=="EX5-07_PRIMARY_ROUTE_MICRODIAGNOSTIC","leaf drift")
    req(cur["subroute"]=="EXECUTE_EFC_PREFLIGHT_01_AFTER_XSTAGE_BLOCKED","subroute drift")
    req(cur["next_route_on_block"]=="EX5R-EHS-001","EFC blocker must move EHS")
    req(s["current_leaf_working_set"]==["stages/stage32-ex5/ex5-07-xstage-preflight-01.json","stages/stage32-ex5/verify_ex5_07_xstage_preflight_01.py","stages/stage32-ex5/ex5-06-executable-route-contracts.json","stages/stage32-ex5/ex5-04-repository-asset-dedup.json","stages/stage32-ex5/ex5-01-exact-receiver-ledger.json"],"working set drift")
    req(s["credit"]["level"]=="EX5_07_XSTAGE_TYPED_BLOCKER_NO_RECEIVER_EFFECT","credit level drift")
    req(s["audit"]["status"]=="NOT_READY_INTERMEDIATE_EX5_07_UNAUDITED","audit status drift")
    for k,v in s["firewalls"].items(): req(v is False,f"firewall must remain false: {k}")
    print("PASS: Stage32EX5 state through XSTAGE-PREFLIGHT-01 blocker; EFC selected next")
if __name__=="__main__": main()
