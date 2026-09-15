#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
SYNC = HERE / "H8C-03A-V25-CLAIM-SYNC.json"
STATE = REPO / "stages/stage32/MAIN-STATE.json"
CONTRACT = REPO / "stages/stage32/proof/CLAIM-SYNC-CONTRACT.md"
REGISTRY = REPO / "stages/stage32/proof/CLAIM-REGISTRY.json"
FRONTIER = REPO / "stages/stage32/proof/ACTIVE-FRONTIER.json"
ADAPTERS = REPO / "stages/stage32/proof/LANE-ADAPTERS.json"
CONSUMPTION = HERE / "H8C-03A-V25-MAIN-CONSUMPTION.json"

SYNC_BLOB = "ceb714bda5efbb6be1d9396327c7579764f25d82"
SYNC_CANON = "7f70a3eeae5b2dd4880e9a502d52baf81f6a2000b752343941dbc885cfa6f8be"
STATE_BLOB = "e0c256916815220746b3d53a81044889d8444749"
STATE_CANON = "a818ff8294ec5f2e1b7674b12cd86049b0c41a34dabc9d220d318bb0786aeb74"
CONTRACT_BLOB = "bbab1b565afbd2e767fc6cc4325c5167d42919b4"
REGISTRY_BLOB = "f3a884adc1c82aace81cb73d049ff14720ace862"
FRONTIER_BLOB = "4c251be4aa5c355481fe3bcfc71c292fb6389ba4"
ADAPTERS_BLOB = "c0ef34e5838e27046a20fed77063593009c56f40"
CONSUMPTION_BLOB = "dd55be9ec98345445ced8e86980ec94921d40097"
CONSUMPTION_CANON = "71976ef4a38d45d1b06374828b16fe9bcf193b99a5c3dcef356f7242d52286a9"
AUTH = 16747313051409592067289


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
    sync = locked_json(SYNC, SYNC_BLOB, SYNC_CANON)
    state = locked_json(STATE, STATE_BLOB, STATE_CANON)
    consumption = locked_json(CONSUMPTION, CONSUMPTION_BLOB, CONSUMPTION_CANON)
    req(CONTRACT.is_file() and blob(CONTRACT) == CONTRACT_BLOB, "claim-sync contract drift")
    locked_json(REGISTRY, REGISTRY_BLOB)
    frontier = locked_json(FRONTIER, FRONTIER_BLOB)
    locked_json(ADAPTERS, ADAPTERS_BLOB)

    req(sync["trigger"] == "AUTHORITY_OR_AUDIT_TRANSITION", "claim-sync trigger drift")
    req(sync["relevant_claim_ids"] == ["S32.FULL178.NUMERICAL_CENSUS.V1"], "claim-sync claim refs drift")
    d = sync["decision"]
    req(d["mathematical_claim_core_changed"] is False, "unexpected claim-core mutation")
    req(d["claim_registry_mutated"] is False, "unexpected registry mutation")
    req(d["active_frontier_mutated"] is False, "unexpected active-frontier mutation")
    req(d["lane_adapter_mutated"] is False, "unexpected lane-adapter mutation")
    req(d["main_state_numeric_authority_changed"] is True, "missing MAIN authority transition")

    full178 = find_claim(frontier, "S32.FULL178.NUMERICAL_CENSUS.V1")
    req(full178 is not None, "FULL178 claim missing")
    req(full178.get("frontier_status") == "ACTIVE_INCOMPLETE", "FULL178 frontier status drift")
    req(full178.get("audit_receipt", {}).get("status") == "NOT_AUDITED_GOAL", "FULL178 audit status drift")

    req(state["schema"] == "STAGE32_MAIN_COMPACT_STATE_V25_H8C03A_CONSUMED", "V25 MAIN schema drift")
    req(state["current_exact_frontier"]["authoritative_remaining_terminals"] == AUTH, "V25 MAIN authority drift")
    req(state["current_exact_frontier"]["full178_numerical_census_complete"] is False, "FULL178 completion overclaim")
    req(state["current"]["mainbatch_stop_gate"] == "REPLACEMENT_HEAD_HOSTILE_REAUDIT_REQUIRED", "replacement audit stop gate drift")
    req(state["firewalls"]["replacement_head_hostile_reaudit_required"] is True, "replacement audit firewall drift")

    req(consumption["promotion"]["claim_sync_scope"] == "MAIN_STATE_NUMERIC_AUTHORITY_ONLY__CLAIM_CORE_UNCHANGED", "consumption claim-sync scope drift")
    req(consumption["promotion"]["claim_dag_changed"] is False, "consumption claim-DAG mutation drift")
    req(consumption["accounting"]["post_consumption_certified_remaining_terminals_upper_bound"] == AUTH, "consumption authority drift")

    for key, value in sync["verification"].items():
        req(value is True, f"required verification disabled: {key}")
    for key, value in sync["firewalls"].items():
        req(value is False, f"claim-sync firewall unexpectedly true: {key}")

    print(json.dumps({
        "status": "PASS_H8C03A_V25_CLAIM_SYNC_NO_CORE_MUTATION",
        "trigger": "AUTHORITY_OR_AUDIT_TRANSITION",
        "claim_id": "S32.FULL178.NUMERICAL_CENSUS.V1",
        "full178_frontier_status": "ACTIVE_INCOMPLETE",
        "main_remaining_upper_bound": AUTH,
        "claim_core_changed": False,
        "claim_registry_mutated": False,
        "replacement_head_hostile_reaudit_required": True,
        "merge_authorized": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
