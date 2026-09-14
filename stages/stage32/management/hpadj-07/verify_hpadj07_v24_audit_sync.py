#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
STATE = ROOT / "stages/stage32/MAIN-STATE.json"
RECEIPT = HERE / "HPADJ07-V24-HOSTILE-AUDIT-PASS-SYNC.json"
CLAIM_REGISTRY = ROOT / "stages/stage32/proof/CLAIM-REGISTRY.json"
ACTIVE_FRONTIER = ROOT / "stages/stage32/proof/ACTIVE-FRONTIER.json"
LANE_ADAPTERS = ROOT / "stages/stage32/proof/LANE-ADAPTERS.json"

AUDITED_HEAD = "3c5915dee248660a2821f2ebe9c24e20b0ad1647"
AUDITED_REVIEW = 5191916561
AUDITED_STATE_BLOB = "c7fac09b774d8fc75ba3daa1b9320dbb66b81a6d"
AUDITED_STATE_CANON = "22e2ae97041b175bc5901572d2490f6d14ad1dd34cf96687f955679be92e4d12"
CURRENT_STATE_BLOB = "b8df16056625db5fbb1947f1e927593de258f1ff"
CURRENT_STATE_CANON = "bdaab3df8871e656652e5c1f78f972405081a45b8d5e421cc4a9bacddef3bf5d"
RECEIPT_BLOB = "37a1d7ed1af5d715220fd3c78e292f84eecbca72"
RECEIPT_CANON = "9594be3af8ed976adbbd513cd776652e76fc92285cc3c875617cd3a10604f56e"
CLAIM_REGISTRY_BLOB = "f3a884adc1c82aace81cb73d049ff14720ace862"
ACTIVE_FRONTIER_BLOB = "4c251be4aa5c355481fe3bcfc71c292fb6389ba4"
LANE_ADAPTERS_BLOB = "f0d364e24e16633149f2ac5f26e44f3acb0e73fe"
AUTH = 26876434389242951089388
STRATA = 17128

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

def head(root: Path) -> str:
    return subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()

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
    ap = argparse.ArgumentParser()
    ap.add_argument("--audited-v24-root", required=True, type=Path)
    args = ap.parse_args()
    audited = args.audited_v24_root.resolve()

    req(audited.is_dir(), "missing hostile-audited V24 checkout")
    req(head(audited) == AUDITED_HEAD, "hostile-audited V24 exact head drift")
    old = locked_json(audited / "stages/stage32/MAIN-STATE.json", AUDITED_STATE_BLOB, AUDITED_STATE_CANON)
    oldf = old["current_exact_frontier"]
    req(old["schema"] == "STAGE32_MAIN_COMPACT_STATE_V24_HPADJ07_LOWER_BOUND_CONSUMED", "audited V24 schema")
    req(old["current"]["mainbatch_stop_gate"] == "V24_HPADJ07_REPLACEMENT_HEAD_HOSTILE_REAUDIT", "audited V24 stop gate")
    req(old["firewalls"]["replacement_head_hostile_reaudit_required"] is True, "audited V24 re-audit firewall")
    req(oldf["authoritative_remaining_strata"] == STRATA, "audited V24 strata")
    req(oldf["authoritative_remaining_terminals"] == AUTH, "audited V24 terminal authority")
    req(oldf["authoritative_remaining_terminals_semantics"] == "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET", "audited V24 authority semantics")
    req(oldf["full178_numerical_census_complete"] is False and oldf["stage32_closed"] is False, "audited V24 closure overclaim")

    receipt = locked_json(RECEIPT, RECEIPT_BLOB, RECEIPT_CANON)
    boundary = receipt["audited_boundary"]
    req(boundary["status"] == "PASS", "receipt audit status")
    req(boundary["review_id"] == AUDITED_REVIEW, "receipt review")
    req(boundary["exact_head"] == AUDITED_HEAD, "receipt exact head")
    req(boundary["main_state_blob_sha1"] == AUDITED_STATE_BLOB, "receipt reviewed state blob")
    req(boundary["main_state_canonical_sha256"] == AUDITED_STATE_CANON, "receipt reviewed state canonical")
    req(receipt["authority_accounting"]["additional_pruning_credit_consumed"] == 0, "sync must not add pruning credit")
    req(receipt["authority_accounting"]["pre_sync_remaining_terminals_upper_bound"] == AUTH, "receipt pre authority")
    req(receipt["authority_accounting"]["post_sync_remaining_terminals_upper_bound"] == AUTH, "receipt post authority")
    req(receipt["claim_sync"]["immutable_claim_core_mutation_required"] is False, "unexpected claim core mutation")
    req(receipt["routing_after_sync"]["heavy_compute_authorized"] is False, "unexpected heavy authorization")
    req(all(v is False for v in receipt["firewalls"].values()), "receipt broad-credit firewall")

    locked_json(CLAIM_REGISTRY, CLAIM_REGISTRY_BLOB)
    frontier = locked_json(ACTIVE_FRONTIER, ACTIVE_FRONTIER_BLOB)
    locked_json(LANE_ADAPTERS, LANE_ADAPTERS_BLOB)
    full178 = find_claim(frontier, "S32.FULL178.NUMERICAL_CENSUS.V1")
    req(full178 is not None, "missing FULL178 active-frontier claim")
    req(full178.get("frontier_status") == "ACTIVE_INCOMPLETE", "FULL178 frontier status was promoted")
    req(full178.get("audit_receipt", {}).get("status") == "NOT_AUDITED_GOAL", "FULL178 audit receipt was promoted")

    state = locked_json(STATE, CURRENT_STATE_BLOB, CURRENT_STATE_CANON)
    f = state["current_exact_frontier"]
    req(state["schema"] == "STAGE32_MAIN_COMPACT_STATE_V24_HPADJ07_AUDIT_SYNCED", "synced schema")
    req(f["authoritative_remaining_strata"] == STRATA, "synced strata")
    req(f["authoritative_remaining_terminals"] == AUTH, "synced terminal authority")
    req(f["authoritative_remaining_terminals_semantics"] == "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET", "synced authority semantics")
    req(f["hpadj07_v24_hostile_audited"] is True, "V24 audit PASS not synchronized")
    req(f["hpadj07_v24_audited_exact_head"] == AUDITED_HEAD, "V24 audited head")
    req(f["hpadj07_v24_hostile_audit_review_id"] == AUDITED_REVIEW, "V24 audit review")
    req(state["authority_sync"]["v24_hpadj07_hostile_audit_status"] == "PASS", "authority sync audit status")
    req(state["authority_sync"]["v24_hpadj07_exact_head"] == AUDITED_HEAD, "authority sync exact head")
    req(state["authority_sync"]["v24_hpadj07_hostile_audit_review_id"] == AUDITED_REVIEW, "authority sync review")
    req(state["current"]["mainbatch_stop_gate"] == "NONE", "MAIN stop gate not released")
    req(state["current"]["next_exact_route"] == "FULL178_THEN_EFFECTIVITY_MULTIBRANCH_AND_FINAL_SYNTHESIS", "next route")
    req(state["firewalls"]["replacement_head_hostile_reaudit_required"] is False, "stale re-audit firewall")
    req(f["full178_numerical_census_complete"] is False and f["stage32_closed"] is False, "closure overclaim")
    for key in ("effectivity_released","endpoint_credit","full178_complete","merge_authorized","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim","receiver_credit","route_credit","stage32_closed","theorem_credit"):
        req(state["firewalls"][key] is False, f"firewall unexpectedly true: {key}")

    lock = state["source_locks"]["hpadj07_v24_audit_sync"]
    req(lock["reviewed_exact_head"] == AUDITED_HEAD, "state reviewed head lock")
    req(lock["reviewed_main_state_blob_sha1"] == AUDITED_STATE_BLOB, "state reviewed blob lock")
    req(lock["hostile_audit_review_id"] == AUDITED_REVIEW and lock["hostile_audit_status"] == "PASS", "state audit receipt lock")
    req(lock["audit_sync_receipt_blob_sha1"] == RECEIPT_BLOB, "state receipt blob lock")
    req(lock["claim_registry_blob_sha1"] == CLAIM_REGISTRY_BLOB, "state registry lock")
    req(lock["active_frontier_blob_sha1"] == ACTIVE_FRONTIER_BLOB, "state frontier lock")
    req(lock["lane_adapters_blob_sha1"] == LANE_ADAPTERS_BLOB, "state lane adapter lock")

    print(json.dumps({
        "verdict":"PASS_V24_HPADJ07_HOSTILE_AUDIT_SYNC",
        "audited_exact_head":AUDITED_HEAD,
        "review_id":AUDITED_REVIEW,
        "remaining_strata":STRATA,
        "remaining_terminals_upper_bound":AUTH,
        "additional_pruning_credit":0,
        "full178_status":"ACTIVE_INCOMPLETE",
        "next_route":"FULL178_THEN_EFFECTIVITY_MULTIBRANCH_AND_FINAL_SYNTHESIS",
        "heavy_compute_authorized":False,
        "merge_authorized":False,
    }, sort_keys=True))

if __name__ == "__main__":
    main()
