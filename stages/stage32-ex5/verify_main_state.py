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
    req(s["schema"]=="STAGE32EX5_MAIN_COMPACT_STATE_V1_EX5_10_BOUNDED_EXHAUSTION_CLASSIFIED","schema drift")
    req(s["stage"]=="32EX5","wrong stage")
    req(s["execution"]["main_command"]=="stage32ex5-mainbatch","main command drift")
    req(s["bootstrap"]["active_work_pr"]==1710 and s["bootstrap"]["merge_authorized"] is False,"PR/merge contract drift")
    req(s["bootstrap"]["base_main_sha"]=="f2a89e613cdf91191a0aada9e90c9fc93373a6c6","freshness base drift")
    cc=s["completion_contract"]
    req(set(cc["allowed_terminal_outcomes"])=={"QUALIFIED_INDEPENDENT_STAGE32_ROUTE_ESTABLISHED","FROZEN_BREADTH_PACKAGE_EXHAUSTED_WITHOUT_QUALIFIED_ROUTE"},"terminal contract drift")
    req(cc["terminal_outcome"] is None,"terminal outcome pregranted")
    req(cc["bounded_exhaustion_is_global_no_route_theorem"] is False,"bounded/global firewall lost")
    req(cc["EX5_route_decision_closure_is_Stage32_full_target_closure"] is False,"EX5 closure cannot equal Stage32 closure")
    f=s["frontier"]
    for k in ["EX5_00_source_lock_complete","receiver_population_contract_complete","receiver_ledger_complete","receiver_ledger_coverage_certified","current_coverage_dependency_graph_complete","clean_room_candidate_universe_frozen","arsenal_dedup_complete","route_scorecard_complete","primary_route_selected","executable_route_contracts_complete","primary_microdiagnostic_complete","backup_1_preflight_complete","backup_2_preflight_complete","reserve_review_complete","frozen_breadth_package_exhausted"]: req(f[k] is True,f"completion flag lost {k}")
    for k in ["nontrivial_receiver_effect_obtained","qualified_independent_route_established","audit_ready_EX5_route_decision_closure","EX5_route_decision_closure"]: req(f[k] is False,f"future credit pregranted {k}")
    req(f["terminal_outcome"] is None,"frontier terminal outcome pregranted")
    r=s["route_families"]
    expected={
      "primary_route_blocker_code":"XSTAGE_MISSING_EXACT_NONEMPTY_MB_SUBSET_ADAPTER",
      "backup_1_blocker_code":"EFC_MISSING_SOURCE_BOUND_POPULATION_COMPLETE_FIXED_COMPONENT_THEOREM",
      "backup_2_blocker_code":"EHS_MISSING_SOURCE_BOUND_EXACT_LINEAR_SYSTEM_DIMENSION_ADAPTER",
      "reserve_1_blocker_code":"LGS_MISSING_POPULATION_WIDE_GLOBAL_TO_LOCAL_DEFECT_ADAPTER",
      "reserve_2_blocker_code":"MOD_MISSING_EXACT_178_ROW_MODULAR_OBJECT_PREIMAGE_ADAPTER"}
    for k,v in expected.items(): req(r[k]==v,f"route blocker drift {k}")
    for k in ["primary_route_status","backup_1_route_status","backup_2_route_status","reserve_1_route_status","reserve_2_route_status"]: req(r[k]=="BLOCKED",f"route status drift {k}")
    req(r["removed_or_rejected_route_status"]=={"EX5R-GAL-001":"INAPPLICABLE_WITH_SEMANTIC_MISMATCH","EX5R-ENUM-001":"DUPLICATE_WITH_EXACT_PARENT"},"removed route status drift")
    req(r["bounded_exhaustion_ledger"]=="stages/stage32-ex5/ex5-10-bounded-breadth-exhaustion-ledger.json","EX5-10 ledger path drift")
    req(r["bounded_exhaustion_verifier"]=="stages/stage32-ex5/verify_ex5_10_bounded_breadth_exhaustion.py","EX5-10 verifier path drift")
    req(r["next_selected_route_id"] is None and r["reserve_review_required"] is False,"post-review routing drift")
    rc=s["receiver_contract"]
    req(rc["row_count"]==185 and rc["status_counts"]=={"CLOSED":5,"OPEN":180,"UNKNOWN":0,"CONDITIONAL":0,"OUT_OF_SCOPE":0},"receiver ledger drift")
    req(rc["V6_O210_Q602_treated_as_definition_of_all_receivers"] is False,"V6 scope firewall lost")
    cur=s["current"]
    req(cur["status"]=="EX5_10_BOUNDED_BREADTH_PACKAGE_EXHAUSTION_CLASSIFIED_RETAINED","current status drift")
    req(cur["leaf"]=="EX5-11_TERMINAL_ROUTE_DECISION_CERTIFICATE","leaf drift")
    req(cur["subroute"]=="ASSEMBLE_BOUNDED_EXHAUSTION_TERMINAL_CERTIFICATE","subroute drift")
    req(s["current_leaf_working_set"]==["stages/stage32-ex5/ex5-10-bounded-breadth-exhaustion-ledger.json","stages/stage32-ex5/verify_ex5_10_bounded_breadth_exhaustion.py","stages/stage32-ex5/stage32-ex5.md","stages/stage32-ex5/ex5-03-clean-room-route-universe.json","stages/stage32-ex5/ex5-01-exact-receiver-ledger.json"],"working set drift")
    cr=s["credit"]
    req(cr["level"]=="EX5_10_BOUNDED_PACKAGE_EXHAUSTION_CLASSIFIED_NO_TERMINAL_CERTIFICATE","credit level drift")
    req(cr["bounded_package_exhaustion_classified"] is True,"bounded classification missing")
    req(cr["frozen_breadth_package_exhausted_without_qualified_route"] is False,"terminal outcome pregranted in credit")
    req(s["audit"]["status"]=="NOT_READY_INTERMEDIATE_EX5_10_UNAUDITED","audit status drift")
    for k,v in s["firewalls"].items(): req(v is False,f"firewall must remain false: {k}")
    print("PASS: Stage32EX5 EX5-10 bounded seven-family exhaustion classified; EX5-11 terminal certificate next")
if __name__=="__main__": main()
