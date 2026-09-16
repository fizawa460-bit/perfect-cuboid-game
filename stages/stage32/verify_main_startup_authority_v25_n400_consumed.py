#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
RECEIPT = HERE / "management/n400-main-consumption/N400-V25-MAIN-CONSUMPTION.json"
AUDIT_RECEIPT = HERE / "management/n400-main-consumption/N400-HOSTILE-AUDIT-PASS-RECEIPT.json"
REGISTRY = HERE / "proof/CROSS-LANE-DEMANDS.json"
MONITOR = HERE / "proof/ACTIVE-SPECIALIST-MONITOR-CONTRACT.json"
SYNTHESIS = HERE / "proof/PICARD64-PARITY-CROSS-LANE-SYNTHESIS-V1.json"
CLAIM_REGISTRY = HERE / "proof/CLAIM-REGISTRY.json"
ACTIVE_FRONTIER = HERE / "proof/ACTIVE-FRONTIER.json"

STATE_BLOB = "c6debd246e0a7f5bac2f5cce6c1d3cf80de3918c"
STATE_CANON = "82a0835b40910b1b3460f55da9d8d19e6252a919b43096772d54d62a41353cd2"
RECEIPT_BLOB = "e0eb8e7d0364dc11df0568d7bbd820488cd44678"
RECEIPT_CANON = "2b6d8d3c3f6eec99def1ee29d65e9a53d610c2c4696de4301d16ec37241ff205"
AUDIT_RECEIPT_BLOB = "c43a50a417cb62228860c0c230a27110939ed6e7"
AUDIT_RECEIPT_CANON = "201422333dd02f1e15c8fc9bb59b332651905f8b21c2d4cd9fa8c67005f1ccbb"
REGISTRY_BLOB = "454eca60149ae5c3121f79567d6b4a782d373369"
REGISTRY_CANON = "600e877e1d0764c4ac0687282d2836707e06b55d6248cf7a0c6fe5b845842161"
MONITOR_BLOB = "344aeaccb0c655f2e1def290eb68dab834aa5105"
SYNTHESIS_BLOB = "e41ee562f8a940ad5041d2d5e64228f2ada7a207"
SYNTHESIS_CANON = "20defc105e39fedaaf5243de55bf0c496ffa997566fec582595847da5a02c2ca"
CLAIM_REGISTRY_BLOB = "f3a884adc1c82aace81cb73d049ff14720ace862"
ACTIVE_FRONTIER_BLOB = "4c251be4aa5c355481fe3bcfc71c292fb6389ba4"
AUTH = 26876434389242951083886

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)

def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canon(obj: dict) -> str:
    cp = dict(obj); cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()

def locked_json(path: Path, b: str, c: str | None = None) -> dict:
    req(path.is_file(), f"missing {path}")
    req(blob(path) == b, f"blob drift {path}")
    obj = json.loads(path.read_text(encoding="utf-8"))
    if c:
        req(obj.get("canonical_sha256_without_this_field") == c, f"stored canonical drift {path}")
        req(canon(obj) == c, f"canonical drift {path}")
    return obj

def find_claim(node, claim_id: str):
    if isinstance(node, dict):
        if node.get("claim_id") == claim_id:
            return node
        for v in node.values():
            x = find_claim(v, claim_id)
            if x is not None: return x
    elif isinstance(node, list):
        for v in node:
            x = find_claim(v, claim_id)
            if x is not None: return x
    return None

def main() -> None:
    state = locked_json(STATE, STATE_BLOB, STATE_CANON)
    rec = locked_json(RECEIPT, RECEIPT_BLOB, RECEIPT_CANON)
    ar = locked_json(AUDIT_RECEIPT, AUDIT_RECEIPT_BLOB, AUDIT_RECEIPT_CANON)
    registry = locked_json(REGISTRY, REGISTRY_BLOB, REGISTRY_CANON)
    req(blob(MONITOR) == MONITOR_BLOB, "monitor drift")
    syn = locked_json(SYNTHESIS, SYNTHESIS_BLOB, SYNTHESIS_CANON)
    req(blob(CLAIM_REGISTRY) == CLAIM_REGISTRY_BLOB, "claim registry drift")
    frontier = locked_json(ACTIVE_FRONTIER, ACTIVE_FRONTIER_BLOB)

    req(state["schema"] == "STAGE32_MAIN_COMPACT_STATE_V25_N400_CONSUMED_AUDIT_REQUIRED", "schema")
    f = state["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == 17128, "strata")
    req(f["authoritative_remaining_terminals"] == AUTH, "terminal authority")
    req(f["authoritative_remaining_terminals_semantics"] == "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET", "authority semantics")
    req(f["n400_incremental_rejected_terminals"] == 5502, "N400 credit")
    req(f["n400_prior_consumed_v24_overlap_terminal_count"] == 0 and f["n400_double_charge"] is False, "N400 double-charge")
    req(f["n400_main_pruning_credit"] is True, "N400 MAIN credit")
    req(f["n400_producer_lane_subtraction_performed"] is False and f["n400_main_consumer_subtraction_performed"] is True, "lane ownership")
    req(state["current"]["mainbatch_stop_gate"] == "HOSTILE_AUDIT_V25_N400_MAIN_CONSUMPTION", "stop gate")
    req(state["current"]["next_exact_route"] == "STOP_PENDING_HOSTILE_AUDIT_OF_REPLACEMENT_MAIN_HEAD", "next route")
    req(state["firewalls"]["replacement_head_hostile_reaudit_required"] is True, "audit freeze")
    req(state["firewalls"]["merge_authorized"] is False, "merge firewall")

    req(ar["audit"]["status"] == "PASS" and ar["audit"]["review_id"] == 5203374607, "N400 audit receipt")
    req(rec["accounting"]["post_consumption_certified_remaining_terminals_upper_bound"] == AUTH, "receipt authority")
    req(rec["accounting"]["double_charge"] is False and rec["accounting"]["consume_exactly_once"] is True, "receipt accounting")

    byid = {d["demand_id"]: d for d in registry["demands"]}
    req(byid["S32.DEMAND.N398.178.MAIN.PARITY_SYNTHESIS.V1"]["status"] == "OBSOLETE", "N398 demand")
    req(byid["S32.DEMAND.N400.178.MAIN.COMPACT_CONSUMPTION.V1"]["status"] == "SATISFIED", "N400 demand")
    req(syn["status"] == "SUPERSEDED_BY_AUDITED_N400_MAIN_CONSUMPTION", "synthesis status")

    full178 = find_claim(frontier, "S32.FULL178.NUMERICAL_CENSUS.V1")
    req(full178 is not None and full178.get("frontier_status") == "ACTIVE_INCOMPLETE", "FULL178 frontier")
    req(full178.get("audit_receipt", {}).get("status") == "NOT_AUDITED_GOAL", "FULL178 claim overpromotion")

    print("PASS: Stage32 MAIN V25 N400 audited consumption boundary")
    print(f"remaining_strata=17128 remaining_terminals_upper_bound={AUTH}")
    print("N400=5502 consumed_once double_charge=false producer_subtraction=false")
    print("FULL178=ACTIVE_INCOMPLETE stop_gate=HOSTILE_AUDIT_V25_N400_MAIN_CONSUMPTION merge_authorized=false")

if __name__ == "__main__":
    main()
