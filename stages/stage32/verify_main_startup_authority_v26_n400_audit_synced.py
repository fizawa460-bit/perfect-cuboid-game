#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
SYNC_RECEIPT = HERE / "management/n400-main-consumption/N400-V26-HOSTILE-AUDIT-PASS-SYNC.json"
SYNC_VERIFIER = HERE / "management/n400-main-consumption/verify_n400_v26_audit_sync.py"
N400_RECEIPT = HERE / "management/n400-main-consumption/N400-V25-MAIN-CONSUMPTION.json"
N400_AUDIT = HERE / "management/n400-main-consumption/N400-HOSTILE-AUDIT-PASS-RECEIPT.json"
REGISTRY = HERE / "proof/CROSS-LANE-DEMANDS.json"
MONITOR = HERE / "proof/ACTIVE-SPECIALIST-MONITOR-CONTRACT.json"
CLAIM_REGISTRY = HERE / "proof/CLAIM-REGISTRY.json"
ACTIVE_FRONTIER = HERE / "proof/ACTIVE-FRONTIER.json"
LANE_ADAPTERS = HERE / "proof/LANE-ADAPTERS.json"

STATE_BLOB = "9242ffc2d44d68b7c6e3a3946fa26f18288fe51b"
STATE_CANON = "39b66cb72dd60900158e60cbca9e0c8dbd15bff3d77f7d9ed2fd096e0f12b9dd"
SYNC_RECEIPT_BLOB = "8f0603116bb3bb0e203651ecfb07c8e0bbe6c3f0"
SYNC_RECEIPT_CANON = "6e6fb0ff4a24603b856029ee93aab5c9db182bdb103bfc8004ae26fcc8253b52"
SYNC_VERIFIER_BLOB = "1145f1fe16048130164556754a2b4ae35cab45af"
N400_RECEIPT_BLOB = "e0eb8e7d0364dc11df0568d7bbd820488cd44678"
N400_RECEIPT_CANON = "2b6d8d3c3f6eec99def1ee29d65e9a53d610c2c4696de4301d16ec37241ff205"
N400_AUDIT_BLOB = "c43a50a417cb62228860c0c230a27110939ed6e7"
N400_AUDIT_CANON = "201422333dd02f1e15c8fc9bb59b332651905f8b21c2d4cd9fa8c67005f1ccbb"
REGISTRY_BLOB = "619c4c415dee38c0539c9d91d6881a3d7b31d46c"
REGISTRY_CANON = "9ace76a55e717dec9f39151e694e78a00250fa08a0a804373faded45196ab7e4"
MONITOR_BLOB = "e8f058eb5daf33fb471bbda522650c5926433e97"
CLAIM_REGISTRY_BLOB = "f3a884adc1c82aace81cb73d049ff14720ace862"
ACTIVE_FRONTIER_BLOB = "4c251be4aa5c355481fe3bcfc71c292fb6389ba4"
LANE_ADAPTERS_BLOB = "c0ef34e5838e27046a20fed77063593009c56f40"
AUDITED_REPLACEMENT_HEAD = "f80b2c87979a980716c9fa3c9b2649f168e0fff8"
AUDITED_REVIEW = 5204417753
AUTH = 26876434389242951083886
STRATA = 17128
CUT201_DEMAND = "S32.DEMAND.CUT201.CUT.MAIN.V26_CURRENT_AUTHORITY_ADAPTER.V1"


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canon(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def locked_json(path: Path, expected_blob: str, expected_canon: str | None = None) -> dict:
    req(path.is_file(), f"missing {path}")
    req(blob(path) == expected_blob, f"blob drift {path}")
    obj = json.loads(path.read_text(encoding="utf-8"))
    if expected_canon is not None:
        req(obj.get("canonical_sha256_without_this_field") == expected_canon, f"stored canonical drift {path}")
        req(canon(obj) == expected_canon, f"canonical drift {path}")
    return obj


def find_claim(node, claim_id: str):
    if isinstance(node, dict):
        if node.get("claim_id") == claim_id:
            return node
        for v in node.values():
            x = find_claim(v, claim_id)
            if x is not None:
                return x
    elif isinstance(node, list):
        for v in node:
            x = find_claim(v, claim_id)
            if x is not None:
                return x
    return None


def main() -> None:
    state = locked_json(STATE, STATE_BLOB, STATE_CANON)
    sync = locked_json(SYNC_RECEIPT, SYNC_RECEIPT_BLOB, SYNC_RECEIPT_CANON)
    req(blob(SYNC_VERIFIER) == SYNC_VERIFIER_BLOB, "V26 sync verifier drift")
    n400 = locked_json(N400_RECEIPT, N400_RECEIPT_BLOB, N400_RECEIPT_CANON)
    audit = locked_json(N400_AUDIT, N400_AUDIT_BLOB, N400_AUDIT_CANON)
    registry = locked_json(REGISTRY, REGISTRY_BLOB, REGISTRY_CANON)
    monitor = locked_json(MONITOR, MONITOR_BLOB)
    req(blob(CLAIM_REGISTRY) == CLAIM_REGISTRY_BLOB, "claim registry drift")
    frontier = locked_json(ACTIVE_FRONTIER, ACTIVE_FRONTIER_BLOB)
    req(blob(LANE_ADAPTERS) == LANE_ADAPTERS_BLOB, "lane adapters drift")

    req(state["schema"] == "STAGE32_MAIN_COMPACT_STATE_V26_N400_AUDIT_SYNCED", "schema")
    f = state["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == STRATA, "strata")
    req(f["authoritative_remaining_terminals"] == AUTH, "terminal authority")
    req(f["authoritative_remaining_terminals_semantics"] == "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET", "authority semantics")
    req(f["n400_incremental_rejected_terminals"] == 5502, "N400 credit")
    req(f["n400_prior_consumed_v24_overlap_terminal_count"] == 0 and f["n400_double_charge"] is False, "N400 overlap")
    req(f["n400_producer_lane_subtraction_performed"] is False and f["n400_main_consumer_subtraction_performed"] is True, "N400 lane ownership")
    req(f["n400_v25_replacement_hostile_audited"] is True, "replacement audit not synchronized")
    req(f["n400_v25_replacement_audited_exact_head"] == AUDITED_REPLACEMENT_HEAD, "replacement audited head")
    req(f["n400_v25_replacement_hostile_audit_review_id"] == AUDITED_REVIEW, "replacement audit review")
    req(state["current"]["mainbatch_stop_gate"] == "NONE", "stop gate")
    req(state["current"]["next_exact_route"] == "FULL178_THEN_EFFECTIVITY_MULTIBRANCH_AND_FINAL_SYNTHESIS", "next route")
    req(state["firewalls"]["replacement_head_hostile_reaudit_required"] is False, "reaudit firewall stale")
    for key in ("effectivity_released", "endpoint_credit", "full178_complete", "merge_authorized", "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim", "receiver_credit", "route_credit", "stage32_closed", "theorem_credit"):
        req(state["firewalls"][key] is False, f"firewall unexpectedly true: {key}")

    req(sync["audited_boundary"]["status"] == "PASS", "sync receipt status")
    req(sync["audited_boundary"]["exact_head"] == AUDITED_REPLACEMENT_HEAD, "sync receipt exact head")
    req(sync["audited_boundary"]["review_id"] == AUDITED_REVIEW, "sync receipt review")
    req(sync["authority_accounting"]["additional_pruning_credit_consumed"] == 0, "sync added pruning")
    req(sync["authority_accounting"]["post_sync_remaining_terminals_upper_bound"] == AUTH, "sync authority")
    req(sync["claim_sync"]["immutable_claim_core_mutation_required"] is False, "claim core mutation")
    req(sync["routing_after_sync"]["heavy_compute_authorized"] is False, "heavy authorization")

    req(audit["audit"]["status"] == "PASS" and audit["audit"]["review_id"] == 5203374607, "producer audit receipt")
    req(n400["accounting"]["post_consumption_certified_remaining_terminals_upper_bound"] == AUTH, "N400 receipt authority")
    req(n400["accounting"]["consume_exactly_once"] is True and n400["accounting"]["double_charge"] is False, "N400 receipt accounting")

    byid = {d["demand_id"]: d for d in registry["demands"]}
    req(byid["S32.DEMAND.N398.178.MAIN.PARITY_SYNTHESIS.V1"]["status"] == "OBSOLETE", "N398 demand")
    req(byid["S32.DEMAND.N400.178.MAIN.COMPACT_CONSUMPTION.V1"]["status"] == "SATISFIED", "N400 demand")
    req(byid[CUT201_DEMAND]["status"] == "OPEN", "CUT201 V26 adapter demand")
    req(byid[CUT201_DEMAND]["source_population_semantics"]["credited_incremental_rejected_terminals"] == 0, "CUT201 premature credit")
    req(byid[CUT201_DEMAND]["source_population_semantics"]["current_v26_subset_identity_proved"] is False, "CUT201 subset overpromotion")
    req(byid[CUT201_DEMAND]["source_population_semantics"]["current_v26_overlap_accounting_proved"] is False, "CUT201 overlap overpromotion")
    consumed = [x for x in registry.get("audited_result_consumption", []) if x.get("result_id") == "S32.N400.N396_REJECTED_5502.COMPACT_MAIN_CONSUMPTION.V1"]
    req(len(consumed) == 1, "N400 consumption ledger cardinality")
    req(consumed[0].get("credited_incremental_rejected_terminals") == 5502, "N400 ledger credit")
    req(consumed[0].get("double_charge") is False and consumed[0].get("prior_consumed_overlap_terminals") == 0, "N400 ledger overlap")

    req(monitor["schema"] == "STAGE32_ACTIVE_SPECIALIST_MONITOR_CONTRACT_V3_CUT201_V26_ADAPTER_PENDING", "monitor schema")
    by_lane = {x["lane"]: x for x in monitor["active_specialists"]}
    req(by_lane["CUT"]["pending_main_handoff_ids"] == [CUT201_DEMAND], "CUT201 monitor handoff")
    req(monitor["credit_firewall"]["duplicate_pruning_credit_authorized"] is False, "duplicate pruning firewall")

    full178 = find_claim(frontier, "S32.FULL178.NUMERICAL_CENSUS.V1")
    req(full178 is not None and full178.get("frontier_status") == "ACTIVE_INCOMPLETE", "FULL178 frontier")
    req(full178.get("audit_receipt", {}).get("status") == "NOT_AUDITED_GOAL", "FULL178 overpromotion")

    print("PASS: Stage32 MAIN V26 N400 hostile-audit sync authority + CUT201 V26 adapter routing")
    print(f"remaining_strata={STRATA} remaining_terminals_upper_bound={AUTH}")
    print("N400=5502 consumed_once replacement_audit=PASS additional_sync_credit=0")
    print("CUT201=25538 audited CUT candidate current_V26_credit=0 adapter_demand=OPEN")
    print("FULL178=ACTIVE_INCOMPLETE stop_gate=NONE heavy_compute_authorized=false merge_authorized=false")


if __name__ == "__main__":
    main()
