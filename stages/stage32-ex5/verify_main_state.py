#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
BC2 = HERE / "breadth-cycle-2"
STATE_PATH = HERE / "MAIN-STATE.json"
RECEIPT_PATH = HERE / "ex5-12-hostile-audit-pass-receipt.json"
CERT_PATH = HERE / "ex5-11-terminal-route-decision-certificate.json"
HANDOFF_PATH = BC2 / "bc2-checkpoint-handoff.json"
PREFLIGHT_PATH = BC2 / "bc2-01-support-adapter-preflight.json"
PAIRING_PATH = BC2 / "bc2-01a-exceptional-pairing-bridge.json"

CYCLE1_OUTCOME = "FROZEN_BREADTH_PACKAGE_EXHAUSTED_WITHOUT_QUALIFIED_ROUTE"
CYCLE1_AUDIT_HEAD = "79c601b636857eaaaa97ad4c22e682e681341bad"
CYCLE1_AUDIT_REVIEW = 5141459384
CYCLE1_CLAIM_ID = "S32.EX5.BOUNDED_EXHAUSTION_CANDIDATE.V2"
CYCLE1_CLAIM_CORE = "6e9093c4fc25455a8c08b9cdb80fc73d127d3759c0b1edfab25b259dcec210a3"
CYCLE1_CERT_CANONICAL = "b0d0a81cf79448703d5e10d9280e6e19ac5f4f32dc31061c9c836d323bcebba7"
BC2_CLAIM_ID = "S32.EX5.BC2_NODE_SUPPORT_SPAN_CHECKPOINT.V1"
FAILED_BC2_HEAD = "a9b9f044b6abcbfe9de7bd334676f854b00d8053"
FAILED_BC2_REVIEW = 5149535554
PASSED_BC2_HEAD = "280776eb5803f69bcb28b5c1da5e546cc198b5a2"
PASSED_BC2_REVIEW = 5149663802
ROUTE_ID = "EX5R-SYMDIFF-NODE-SPAN-001"
NEXT_LEAF = "BC2-01B_RUNTIME_NODE_COORDINATE_BRIDGE"


def req(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


def canonical_without_field(obj: dict, field: str) -> str:
    cp = dict(obj)
    cp.pop(field, None)
    raw = json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    state = load(STATE_PATH)
    receipt = load(RECEIPT_PATH)
    cert = load(CERT_PATH)
    handoff = load(HANDOFF_PATH)
    preflight = load(PREFLIGHT_PATH)
    pairing = load(PAIRING_PATH)

    req(state["schema"] == "STAGE32EX5_MAIN_COMPACT_STATE_V3_BC2_AUDITED_CHECKPOINT", "schema drift")
    req(state["stage"] == "32EX5", "wrong stage")
    req(state["execution"]["main_command"] == "stage32ex5-mainbatch", "main command drift")
    req(state["execution"]["audit_command"] == "stage32ex5-audit", "audit command drift")
    req(state["execution"]["claim_sync_contract"] == "stages/stage32/proof/CLAIM-SYNC-CONTRACT.md", "claim-sync contract drift")

    bootstrap = state["bootstrap"]
    req(bootstrap["active_work_pr"] == 1726, "active PR drift")
    req(bootstrap["work_branch"] == "stage32ex5-bc2-btva-node-support-span", "work branch drift")
    req(bootstrap["merge_authorized"] is False, "merge authorization must remain a separate user action")

    auth = state["authority"]
    req(auth["current_bc2_authority"] == "AUDITED", "BC2 authority transition not consumed")
    req(auth["current_bc2_claim_id"] == BC2_CLAIM_ID, "BC2 claim id drift")
    req(auth["prior_cycle1_audited_authority_preserved"] is True, "Cycle1 authority provenance lost")
    req(auth["stage32_main_authority_unchanged"] is True, "Stage32 MAIN authority changed")

    prior = state["prior_audited_authority"]
    req(prior["breadth_cycle"] == "EX5_BREADTH_CYCLE_1", "prior breadth-cycle drift")
    req(prior["claim_id"] == CYCLE1_CLAIM_ID and prior["authority_status"] == "AUDITED", "prior claim authority drift")
    req(prior["terminal_outcome"] == CYCLE1_OUTCOME, "prior terminal outcome drift")
    req(prior["exact_head"] == CYCLE1_AUDIT_HEAD and prior["review_id"] == CYCLE1_AUDIT_REVIEW, "prior audit identity drift")
    req(prior["scope_firewall"] == "EX5_BREADTH_CYCLE_1_ONLY", "Cycle1 scope widened")
    req(prior["stage32_main_credit"] is False, "Cycle1 improperly promoted to MAIN")

    current = state["current"]
    req(current["status"] == "BC2_RETAINED_AUDITED_CHECKPOINT_MERGE_READY", "current status drift")
    req(current["breadth_cycle"] == "EX5_BREADTH_CYCLE_2_CANDIDATE", "current breadth-cycle drift")
    req(current["leaf"] == "BC2-01A_EXCEPTIONAL_PAIRING_BRIDGE", "current leaf drift")
    req(current["route_id"] == ROUTE_ID, "route id drift")
    req(current["next_route"] == NEXT_LEAF, "next leaf drift")
    req(current["blocker"] == "MISSING_EXACT_RUNTIME_EXCEPTIONAL_INDEX_TO_PROJECTIVE_NODE_COORDINATE_BRIDGE", "blocker drift")

    required_working = {
        "stages/stage32-ex5/breadth-cycle-2/bc2-checkpoint-handoff.json",
        "stages/stage32-ex5/breadth-cycle-2/bc2-01-support-adapter-preflight.json",
        "stages/stage32-ex5/breadth-cycle-2/bc2-01a-exceptional-pairing-bridge.json",
        "stages/stage32/proof/CLAIM-SYNC-CONTRACT.md",
        "stages/stage32/proof/CLAIM-REGISTRY.json",
        "stages/stage32/proof/LANE-ADAPTERS.json",
        "stages/stage32/proof/ACTIVE-FRONTIER.json",
    }
    req(required_working.issubset(set(state["current_leaf_working_set"])), "BC2/claim-sync working set incomplete")

    frontier = state["frontier"]
    for key in (
        "cycle1_audited_bounded_exhaustion_preserved",
        "bc2_materially_new_route_admitted",
        "bc2_00_first_pass_complete",
        "bc2_00_second_pass_dedup_complete",
        "bc2_01_support_adapter_preflight_complete",
        "bc2_01a_exceptional_pairing_bridge_complete",
        "retained_consolidation_claim_sync_required",
        "retained_consolidation_claim_sync_completed",
        "hostile_audit_pass_consumed",
        "authority_transition_sync_completed",
    ):
        req(frontier[key] is True, f"frontier completion flag lost: {key}")
    for key in (
        "bc2_01b_runtime_node_coordinate_bridge_complete",
        "runtime_calibration_complete",
        "btva_projective_span_replay_ready",
        "nontrivial_receiver_effect_obtained",
        "qualified_independent_route_established",
    ):
        req(frontier[key] is False, f"unsafe BC2 frontier promotion: {key}")

    rc = state["receiver_contract"]
    req(rc["row_count"] == 185, "receiver row-count drift")
    req(rc["status_counts"] == {"CLOSED": 5, "OPEN": 180, "UNKNOWN": 0, "CONDITIONAL": 0, "OUT_OF_SCOPE": 0}, "receiver status drift")
    req(rc["V6_O210_Q602_treated_as_definition_of_all_receivers"] is False, "receiver semantics widened")

    sync = state["claim_sync"]
    req(sync["trigger"] == "AUTHORITY_OR_AUDIT_TRANSITION", "claim-sync trigger drift")
    req(sync["current_audited_claim_id"] == BC2_CLAIM_ID, "claim-sync current audited claim drift")
    req(sync["audit_receipt_review_id"] == PASSED_BC2_REVIEW and sync["audit_receipt_exact_head"] == PASSED_BC2_HEAD, "claim-sync PASS receipt drift")
    req(sync["active_frontier_refs"] == ["S32.FULL178.NUMERICAL_CENSUS.V1", "S32.GOAL.STAGE32_CLOSURE.V1"], "EX5 active-frontier refs drift")
    req(sync["active_frontier_semantics_changed"] is False, "BC2 falsely claims new active-frontier semantics")
    req(sync["stage32_main_promotion"] is False, "claim-sync promoted BC2 to MAIN")

    credit = state["credit"]
    req(credit["level"] == "BC2_AUDITED_INFRASTRUCTURE_CHECKPOINT_NO_ROUTE_OR_RECEIVER_CREDIT", "BC2 credit ceiling drift")
    req(credit["prior_cycle1_audited_credit_preserved"] is True, "Cycle1 audited credit provenance lost")
    for key in (
        "current_bc2_mathematical_credit",
        "qualified_independent_stage32_route_established",
        "stage32_main_credit",
        "Q602_excluded",
        "O210_excluded",
        "receiver_credit",
        "theorem_credit",
        "endpoint_credit",
        "FULL178_complete",
        "EFF_discharged",
        "MB_discharged",
    ):
        req(credit[key] is False, f"unauthorized BC2 credit: {key}")

    audit = state["audit"]
    req(audit["status"] == "PASS_CONSUMED_BY_AUTHORITY_TRANSITION_SYNC", "audit consumption status drift")
    req(audit["candidate_pr"] == 1726, "audit PR drift")
    req(audit["exact_head"] == PASSED_BC2_HEAD and audit["review_id"] == PASSED_BC2_REVIEW, "PASS audit identity drift")
    req(audit["result"] == "PASS" and audit["reaudit_required"] is False, "PASS consumption gate drift")
    req(audit["prior_failed_exact_head"] == FAILED_BC2_HEAD and audit["prior_failed_review_id"] == FAILED_BC2_REVIEW, "prior FAIL provenance lost")
    req(audit["mathematical_blocking_contradiction_found"] is False, "audit history misclassified as mathematical contradiction")
    req(audit["pass_auto_merges"] is False and audit["pass_auto_promotes_to_stage32_main"] is False, "audit firewall lost")

    for key, value in state["firewalls"].items():
        req(value is False, f"firewall must remain false: {key}")

    # Preserve the exact prior Cycle1 hostile-audit evidence; BC2 authority transition must not rewrite it.
    req(receipt["schema"] == "STAGE32EX5_EX5_12_HOSTILE_AUDIT_PASS_RECEIPT_V1", "Cycle1 receipt schema drift")
    req(receipt["candidate_pr"] == 1710 and receipt["candidate_exact_head"] == CYCLE1_AUDIT_HEAD, "Cycle1 receipt target drift")
    req(receipt["audit_review_id"] == CYCLE1_AUDIT_REVIEW and receipt["audit_result"] == "PASS", "Cycle1 receipt PASS drift")
    req(receipt["claim_id"] == CYCLE1_CLAIM_ID and receipt["claim_core_sha256"] == CYCLE1_CLAIM_CORE, "Cycle1 claim identity drift")
    req(cert["terminal_decision"]["selected_outcome"] == CYCLE1_OUTCOME, "Cycle1 terminal artifact outcome drift")
    req(cert["canonical_sha256_without_this_field"] == CYCLE1_CERT_CANONICAL, "Cycle1 certificate canonical lock drift")
    req(canonical_without_field(cert, "canonical_sha256_without_this_field") == CYCLE1_CERT_CANONICAL, "Cycle1 certificate canonical replay drift")

    # The retained handoff is the immutable pre-audit evidence boundary for the same BC2 claim core.
    req(handoff["schema"] == "STAGE32EX5_BC2_CHECKPOINT_HANDOFF_V2_CLAIM_SYNC_REPAIR", "handoff schema drift")
    req(handoff["breadth_cycle"] == current["breadth_cycle"] and handoff["route_id"] == ROUTE_ID, "handoff/current route disagreement")
    req(handoff["current_routing"]["leaf"] == current["leaf"], "handoff/current leaf disagreement")
    req(handoff["current_routing"]["next_leaf"] == NEXT_LEAF, "handoff next leaf disagreement")
    req(handoff["current_routing"]["provisional_claim_id"] == BC2_CLAIM_ID, "handoff evidence-boundary claim id drift")
    req(handoff["cycle1_authority"]["replaced_or_widened_by_bc2"] is False, "Cycle1 authority overwritten by BC2")
    req(handoff["audit_repair"]["failed_exact_head"] == FAILED_BC2_HEAD and handoff["audit_repair"]["failed_review_id"] == FAILED_BC2_REVIEW, "handoff failed-audit provenance drift")
    for key, value in handoff["credit"].items():
        req(value is False, f"handoff unauthorized credit: {key}")
    for key, value in handoff["firewalls"].items():
        req(value is False, f"handoff firewall must remain false: {key}")

    req(preflight["route_id"] == ROUTE_ID, "BC2-01 route drift")
    req(preflight["status"] == "PREFLIGHT_CONTRACT_PASS_RUNTIME_CALIBRATION_PENDING", "BC2-01 status drift")
    req(preflight["firewalls"]["runtime_calibration_claimed"] is False, "runtime calibration falsely claimed")
    req(preflight["firewalls"]["mass_treated_as_labelled_support"] is False, "aggregate mass mislabeled as support")

    req(pairing["route_id"] == ROUTE_ID, "BC2-01A route drift")
    req(pairing["status"] == "PAIRING_LAST48_BRIDGE_PASS_NODE_COORDINATE_BRIDGE_PENDING", "BC2-01A status drift")
    req(pairing["next_leaf"]["id"] == NEXT_LEAF, "BC2-01A next leaf drift")
    req(pairing["pending"]["persisted_runtime_node_index_to_exact_projective_coordinate_table_found"] is False, "node-coordinate bridge falsely claimed")
    req(pairing["pending"]["btva_projective_span_replay_ready"] is False, "BTVA replay falsely ready")

    print("PASS: Stage32EX5 BC2 hostile-audit PASS consumed; retained checkpoint authority AUDITED")
    print(f"current_bc2_claim={BC2_CLAIM_ID}:AUDITED")
    print(f"audit_review={PASSED_BC2_REVIEW}")
    print(f"next_leaf={NEXT_LEAF}")
    print("bc2_route_receiver_credit=NO")
    print("stage32_main_credit=NO")
    print("merge=SEPARATE_USER_ACTION")


if __name__ == "__main__":
    main()
