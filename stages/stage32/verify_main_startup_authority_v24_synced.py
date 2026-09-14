#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
RECEIPT = HERE / "management/hpadj-07/HPADJ07-V24-HOSTILE-AUDIT-PASS-SYNC.json"
CLAIM_REGISTRY = HERE / "proof/CLAIM-REGISTRY.json"
ACTIVE_FRONTIER = HERE / "proof/ACTIVE-FRONTIER.json"
LANE_ADAPTERS = HERE / "proof/LANE-ADAPTERS.json"

STATE_BLOB = "b8df16056625db5fbb1947f1e927593de258f1ff"
STATE_CANON = "bdaab3df8871e656652e5c1f78f972405081a45b8d5e421cc4a9bacddef3bf5d"
RECEIPT_BLOB = "37a1d7ed1af5d715220fd3c78e292f84eecbca72"
RECEIPT_CANON = "9594be3af8ed976adbbd513cd776652e76fc92285cc3c875617cd3a10604f56e"
CLAIM_REGISTRY_BLOB = "f3a884adc1c82aace81cb73d049ff14720ace862"
ACTIVE_FRONTIER_BLOB = "4c251be4aa5c355481fe3bcfc71c292fb6389ba4"
LANE_ADAPTERS_BLOB = "f0d364e24e16633149f2ac5f26e44f3acb0e73fe"
AUDITED_HEAD = "3c5915dee248660a2821f2ebe9c24e20b0ad1647"
AUDIT_REVIEW = 5191916561
AUTH = 26876434389242951089388

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

def locked_json(path: Path, b: str, c: str | None = None) -> dict:
    req(path.is_file(), f"missing {path}")
    req(blob(path) == b, f"blob drift {path}")
    obj = json.loads(path.read_text(encoding="utf-8"))
    if c is not None:
        req(obj.get("canonical_sha256_without_this_field") == c, f"stored canonical drift {path}")
        req(canon(obj) == c, f"canonical drift {path}")
    return obj

def find_claim(node, claim_id: str):
    if isinstance(node, dict):
        if node.get("claim_id") == claim_id:
            return node
        for value in node.values():
            found = find_claim(value, claim_id)
            if found is not None:
                return found
    elif isinstance(node, list):
        for value in node:
            found = find_claim(value, claim_id)
            if found is not None:
                return found
    return None

def main() -> None:
    state = locked_json(STATE, STATE_BLOB, STATE_CANON)
    receipt = locked_json(RECEIPT, RECEIPT_BLOB, RECEIPT_CANON)
    registry = locked_json(CLAIM_REGISTRY, CLAIM_REGISTRY_BLOB)
    frontier = locked_json(ACTIVE_FRONTIER, ACTIVE_FRONTIER_BLOB)
    locked_json(LANE_ADAPTERS, LANE_ADAPTERS_BLOB)

    req(state["schema"] == "STAGE32_MAIN_COMPACT_STATE_V24_HPADJ07_AUDIT_SYNCED", "schema")
    f = state["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == 17128, "strata authority")
    req(f["authoritative_remaining_terminals"] == AUTH, "terminal authority")
    req(f["authoritative_remaining_terminals_semantics"] == "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET", "authority semantics")
    req(f["hpadj07_main_pruning_credit"] is True, "HPADJ07 consumed credit")
    req(f["hpadj07_v24_hostile_audited"] is True, "V24 hostile audit")
    req(f["hpadj07_v24_audited_exact_head"] == AUDITED_HEAD, "V24 audit head")
    req(f["hpadj07_v24_hostile_audit_review_id"] == AUDIT_REVIEW, "V24 audit review")
    req(f["full178_numerical_census_complete"] is False and f["stage32_closed"] is False, "closure overclaim")
    req(state["current"]["mainbatch_stop_gate"] == "NONE", "stale stop gate")
    req(state["current"]["next_exact_route"] == "FULL178_THEN_EFFECTIVITY_MULTIBRANCH_AND_FINAL_SYNTHESIS", "next route")
    req(state["firewalls"]["replacement_head_hostile_reaudit_required"] is False, "stale re-audit firewall")
    for key in ("effectivity_released","endpoint_credit","full178_complete","merge_authorized","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim","receiver_credit","route_credit","stage32_closed","theorem_credit"):
        req(state["firewalls"][key] is False, f"firewall unexpectedly true: {key}")

    req(receipt["audited_boundary"]["exact_head"] == AUDITED_HEAD, "receipt head")
    req(receipt["audited_boundary"]["review_id"] == AUDIT_REVIEW, "receipt review")
    req(receipt["audited_boundary"]["status"] == "PASS", "receipt status")
    req(receipt["authority_accounting"]["additional_pruning_credit_consumed"] == 0, "unexpected new pruning")
    req(receipt["routing_after_sync"]["heavy_compute_authorized"] is False, "unexpected heavy authorization")

    full178 = find_claim(frontier, "S32.FULL178.NUMERICAL_CENSUS.V1")
    req(full178 is not None and full178.get("frontier_status") == "ACTIVE_INCOMPLETE", "FULL178 frontier promotion")
    req(full178.get("audit_receipt", {}).get("status") == "NOT_AUDITED_GOAL", "FULL178 audit promotion")
    reg_full178 = find_claim(registry, "S32.FULL178.NUMERICAL_CENSUS.V1")
    req(reg_full178 is not None and reg_full178.get("authority_status") == "DECLARED_GOAL", "FULL178 registry promotion")

    print("PASS: Stage32 MAIN V24 HPADJ07 hostile-audit sync boundary")
    print(f"remaining_strata=17128 remaining_terminals_upper_bound={AUTH}")
    print("FULL178=ACTIVE_INCOMPLETE stop_gate=NONE heavy_compute_authorized=false merge_authorized=false")

if __name__ == "__main__":
    main()
