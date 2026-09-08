#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
STATE_PATH=HERE/"MAIN-STATE.json"
RECEIPT_PATH=HERE/"ex5-12-hostile-audit-pass-receipt.json"
CERT_PATH=HERE/"ex5-11-terminal-route-decision-certificate.json"
OUTCOME="FROZEN_BREADTH_PACKAGE_EXHAUSTED_WITHOUT_QUALIFIED_ROUTE"
AUDIT_HEAD="79c601b636857eaaaa97ad4c22e682e681341bad"
AUDIT_REVIEW=5141459384
CLAIM_ID="S32.EX5.BOUNDED_EXHAUSTION_CANDIDATE.V2"
CLAIM_CORE="6e9093c4fc25455a8c08b9cdb80fc73d127d3759c0b1edfab25b259dcec210a3"
CERT_CANONICAL="b0d0a81cf79448703d5e10d9280e6e19ac5f4f32dc31061c9c836d323bcebba7"

def req(c,m):
    if not c:
        raise SystemExit(f"FAIL: {m}")

def canonical_without_field(obj, field):
    cp=dict(obj)
    cp.pop(field,None)
    raw=json.dumps(cp,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()

def main():
    s=json.loads(STATE_PATH.read_text())
    r=json.loads(RECEIPT_PATH.read_text())
    cert=json.loads(CERT_PATH.read_text())

    req(s["schema"]=="STAGE32EX5_MAIN_COMPACT_STATE_V1_EX5_12_AUDITED_BOUNDED_EXHAUSTION_CLOSURE","schema drift")
    req(s["stage"]=="32EX5","wrong stage")
    req(s["execution"]["main_command"]=="stage32ex5-mainbatch" and s["execution"]["audit_command"]=="stage32ex5-audit","command contract drift")
    req(s["bootstrap"]["active_work_pr"]==1710 and s["bootstrap"]["merge_authorized"] is False,"PR/merge contract drift")

    cc=s["completion_contract"]
    req(set(cc["allowed_terminal_outcomes"])=={"QUALIFIED_INDEPENDENT_STAGE32_ROUTE_ESTABLISHED",OUTCOME},"terminal outcome contract drift")
    req(cc["terminal_outcome"]==OUTCOME,"terminal outcome drift")
    req(cc["bounded_exhaustion_is_global_no_route_theorem"] is False,"bounded/global firewall lost")
    req(cc["blocked_route_is_stage_exhaustion"] is False,"blocked route promoted to exhaustion")
    req(cc["EX5_route_decision_closure_is_Stage32_full_target_closure"] is False,"EX5/Stage32 closure collapse")

    f=s["frontier"]
    for k in ["EX5_00_source_lock_complete","receiver_population_contract_complete","receiver_ledger_complete",
              "receiver_ledger_coverage_certified","current_coverage_dependency_graph_complete",
              "clean_room_candidate_universe_frozen","arsenal_dedup_complete","route_scorecard_complete",
              "primary_route_selected","executable_route_contracts_complete","primary_microdiagnostic_complete",
              "backup_1_preflight_complete","backup_2_preflight_complete","reserve_review_complete",
              "terminal_certificate_assembled","frozen_breadth_package_exhausted",
              "audit_ready_EX5_route_decision_closure","hostile_audit_pass","EX5_route_decision_closure"]:
        req(f[k] is True,f"completion/audit flag lost {k}")
    req(f["qualified_independent_route_established"] is False and f["nontrivial_receiver_effect_obtained"] is False,
        "receiver/route effect invented")
    req(f["terminal_outcome"]==OUTCOME,"frontier outcome drift")

    rc=s["receiver_contract"]
    req(rc["row_count"]==185 and rc["status_counts"]=={"CLOSED":5,"OPEN":180,"UNKNOWN":0,"CONDITIONAL":0,"OUT_OF_SCOPE":0},
        "receiver ledger drift")
    req(rc["V6_O210_Q602_treated_as_definition_of_all_receivers"] is False,"V6 special context widened")

    routes=s["route_families"]
    expected={
      "primary_route_blocker_code":"XSTAGE_MISSING_EXACT_NONEMPTY_MB_SUBSET_ADAPTER",
      "backup_1_blocker_code":"EFC_MISSING_SOURCE_BOUND_POPULATION_COMPLETE_FIXED_COMPONENT_THEOREM",
      "backup_2_blocker_code":"EHS_MISSING_SOURCE_BOUND_EXACT_LINEAR_SYSTEM_DIMENSION_ADAPTER",
      "reserve_1_blocker_code":"LGS_MISSING_POPULATION_WIDE_GLOBAL_TO_LOCAL_DEFECT_ADAPTER",
      "reserve_2_blocker_code":"MOD_MISSING_EXACT_178_ROW_MODULAR_OBJECT_PREIMAGE_ADAPTER"
    }
    for k,v in expected.items():
        req(routes[k]==v,f"route blocker drift {k}")
    for k in ["primary_route_status","backup_1_route_status","backup_2_route_status","reserve_1_route_status","reserve_2_route_status"]:
        req(routes[k]=="BLOCKED",f"route status drift {k}")
    req(routes["removed_or_rejected_route_status"]=={
        "EX5R-GAL-001":"INAPPLICABLE_WITH_SEMANTIC_MISMATCH",
        "EX5R-ENUM-001":"DUPLICATE_WITH_EXACT_PARENT"},"removed route status drift")

    cur=s["current"]
    req(cur["status"]=="EX5_ROUTE_DECISION_CLOSURE_BOUNDED_EXHAUSTION_AUDITED","current status drift")
    req(cur["leaf"]=="EX5-12_AUDITED_BOUNDED_TERMINAL_HOLD","leaf drift")
    req(cur["subroute"]=="STOPPED_REENTRY_REQUIRES_NEW_BREADTH_INPUT_OR_EXPLICIT_MAIN_ROUTE_ADAPTER","subroute drift")

    cr=s["credit"]
    req(cr["level"]=="EX5_ROUTE_DECISION_CLOSURE_AUDITED_FROZEN_BREADTH_PACKAGE_EXHAUSTED_WITHOUT_QUALIFIED_ROUTE","credit level drift")
    req(cr["frozen_breadth_package_exhausted_without_qualified_route"] is True and cr["EX5_route_decision_closure"] is True,
        "audited EX5 closure credit missing")
    req(cr["stage32_main_credit"] is False and cr["Q602_excluded"] is False and cr["O210_excluded"] is False,
        "external credit leak")
    req(cr["receiver_credit"] is False and cr["theorem_credit"] is False and cr["endpoint_credit"] is False,
        "credit-layer leak")

    a=s["audit"]
    req(a["status"]=="PASS_CONSUMED_BY_AUTHORITY_TRANSITION_SYNC","audit sync status drift")
    req(a["candidate_pr"]==1710 and a["exact_head"]==AUDIT_HEAD and a["review_id"]==AUDIT_REVIEW and a["result"]=="PASS",
        "audit receipt drift")
    req(a["selected_terminal_outcome"]==OUTCOME,"audit outcome drift")
    req(a["pass_auto_merges"] is False and a["pass_auto_promotes_to_stage32_main"] is False,"audit firewall lost")

    req(r["schema"]=="STAGE32EX5_EX5_12_HOSTILE_AUDIT_PASS_RECEIPT_V1","receipt schema drift")
    req(r["candidate_pr"]==1710 and r["candidate_exact_head"]==AUDIT_HEAD and r["audit_review_id"]==AUDIT_REVIEW and r["audit_result"]=="PASS",
        "receipt identity drift")
    req(r["claim_id"]==CLAIM_ID and r["claim_core_sha256"]==CLAIM_CORE,"receipt claim identity drift")
    req(r["authority_transition"]=="PROVISIONAL_TO_AUDITED_ON_UNCHANGED_CLAIM_CORE","authority transition drift")
    req(r["promotion_ceiling"]["EX5_route_decision_closure"] is True and r["promotion_ceiling"]["stage32_main_promotion"] is False,
        "receipt promotion ceiling drift")

    req(cert["terminal_decision"]["selected_outcome"]==OUTCOME,"terminal artifact outcome drift")
    req(cert["canonical_sha256_without_this_field"]==CERT_CANONICAL,"terminal certificate canonical lock drift")
    req(canonical_without_field(cert,"canonical_sha256_without_this_field")==CERT_CANONICAL,"terminal certificate canonical replay drift")
    req(cert["terminal_decision"]["hostile_audit_pass_present"] is False and cert["terminal_decision"]["EX5_route_decision_closure"] is False,
        "audited candidate artifact was rewritten to self-authorize")

    for k,v in s["firewalls"].items():
        req(v is False,f"firewall must remain false: {k}")
    req(s["route_anti_loop"]["audited_fact_available"] is True,"route anti-loop audited fact missing")
    req(s["route_anti_loop"]["stage32_main_mathematical_frontier_changed"] is False,"MAIN frontier changed by EX5 local closure")
    req(s["route_anti_loop"]["explicit_main_promotion_adapter_present"] is False,"implicit EX->MAIN promotion")

    print("PASS: Stage32EX5 EX5-12 hostile-audit PASS consumed; bounded EX5 route-decision closure audited, no Stage32 MAIN credit")

if __name__=="__main__":
    main()
