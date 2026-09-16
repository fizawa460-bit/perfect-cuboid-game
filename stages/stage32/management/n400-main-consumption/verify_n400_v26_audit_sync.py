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
RECEIPT = HERE / "N400-V26-HOSTILE-AUDIT-PASS-SYNC.json"
CLAIM_REGISTRY = ROOT / "stages/stage32/proof/CLAIM-REGISTRY.json"
ACTIVE_FRONTIER = ROOT / "stages/stage32/proof/ACTIVE-FRONTIER.json"
LANE_ADAPTERS = ROOT / "stages/stage32/proof/LANE-ADAPTERS.json"

AUDITED_HEAD = "f80b2c87979a980716c9fa3c9b2649f168e0fff8"
AUDITED_REVIEW = 5204417753
AUDITED_STATE_BLOB = "c6debd246e0a7f5bac2f5cce6c1d3cf80de3918c"
AUDITED_STATE_CANON = "82a0835b40910b1b3460f55da9d8d19e6252a919b43096772d54d62a41353cd2"
CURRENT_STATE_BLOB = "9242ffc2d44d68b7c6e3a3946fa26f18288fe51b"
CURRENT_STATE_CANON = "39b66cb72dd60900158e60cbca9e0c8dbd15bff3d77f7d9ed2fd096e0f12b9dd"
RECEIPT_BLOB = "8f0603116bb3bb0e203651ecfb07c8e0bbe6c3f0"
RECEIPT_CANON = "6e6fb0ff4a24603b856029ee93aab5c9db182bdb103bfc8004ae26fcc8253b52"
CLAIM_REGISTRY_BLOB = "f3a884adc1c82aace81cb73d049ff14720ace862"
ACTIVE_FRONTIER_BLOB = "4c251be4aa5c355481fe3bcfc71c292fb6389ba4"
LANE_ADAPTERS_BLOB = "c0ef34e5838e27046a20fed77063593009c56f40"
AUTH = 26876434389242951083886
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
    ap.add_argument("--audited-v25-root", type=Path)
    args = ap.parse_args()

    if args.audited_v25_root is not None:
        audited = args.audited_v25_root.resolve()
        req(audited.is_dir(), "missing hostile-audited V25 checkout")
        req(head(audited) == AUDITED_HEAD, "hostile-audited V25 exact head drift")
        old = locked_json(audited / "stages/stage32/MAIN-STATE.json", AUDITED_STATE_BLOB, AUDITED_STATE_CANON)
        oldf = old["current_exact_frontier"]
        req(old["schema"] == "STAGE32_MAIN_COMPACT_STATE_V25_N400_CONSUMED_AUDIT_REQUIRED", "audited V25 schema")
        req(old["current"]["mainbatch_stop_gate"] == "HOSTILE_AUDIT_V25_N400_MAIN_CONSUMPTION", "audited V25 stop gate")
        req(old["firewalls"]["replacement_head_hostile_reaudit_required"] is True, "audited V25 re-audit firewall")
        req(oldf["authoritative_remaining_strata"] == STRATA, "audited V25 strata")
        req(oldf["authoritative_remaining_terminals"] == AUTH, "audited V25 authority")
        req(oldf["n400_incremental_rejected_terminals"] == 5502, "audited V25 N400 credit")
        req(oldf["n400_prior_consumed_v24_overlap_terminal_count"] == 0 and oldf["n400_double_charge"] is False, "audited V25 overlap")
        req(oldf["n400_producer_lane_subtraction_performed"] is False and oldf["n400_main_consumer_subtraction_performed"] is True, "audited V25 lane ownership")

    receipt = locked_json(RECEIPT, RECEIPT_BLOB, RECEIPT_CANON)
    boundary = receipt["audited_boundary"]
    req(boundary["status"] == "PASS", "receipt audit status")
    req(boundary["review_id"] == AUDITED_REVIEW, "receipt review")
    req(boundary["exact_head"] == AUDITED_HEAD, "receipt exact head")
    req(boundary["main_state_blob_sha1"] == AUDITED_STATE_BLOB, "receipt reviewed state blob")
    req(boundary["main_state_canonical_sha256"] == AUDITED_STATE_CANON, "receipt reviewed state canonical")
    req(boundary["merge_ready_freshness"] == "CLEAR", "receipt freshness")
    acct = receipt["authority_accounting"]
    req(acct["additional_pruning_credit_consumed"] == 0, "sync must not add pruning credit")
    req(acct["pre_sync_remaining_terminals_upper_bound"] == AUTH and acct["post_sync_remaining_terminals_upper_bound"] == AUTH, "sync authority changed")
    req(acct["n400_consumed_terminals"] == 5502 and acct["n400_prior_consumed_overlap_terminals"] == 0, "N400 accounting drift")
    req(acct["double_charge"] is False, "double charge")
    req(acct["producer_lane_subtraction_performed"] is False and acct["main_consumer_subtraction_performed"] is True, "lane subtraction drift")
    req(receipt["claim_sync"]["immutable_claim_core_mutation_required"] is False, "unexpected claim-core mutation")
    req(receipt["routing_after_sync"]["heavy_compute_authorized"] is False, "unexpected heavy authorization")
    req(all(v is False for v in receipt["firewalls"].values()), "receipt broad-credit firewall")

    req(blob(CLAIM_REGISTRY) == CLAIM_REGISTRY_BLOB, "claim registry drift")
    frontier = locked_json(ACTIVE_FRONTIER, ACTIVE_FRONTIER_BLOB)
    req(blob(LANE_ADAPTERS) == LANE_ADAPTERS_BLOB, "lane adapters drift")
    full178 = find_claim(frontier, "S32.FULL178.NUMERICAL_CENSUS.V1")
    req(full178 is not None, "missing FULL178 active-frontier claim")
    req(full178.get("frontier_status") == "ACTIVE_INCOMPLETE", "FULL178 frontier promoted")
    req(full178.get("audit_receipt", {}).get("status") == "NOT_AUDITED_GOAL", "FULL178 audit promoted")

    state = locked_json(STATE, CURRENT_STATE_BLOB, CURRENT_STATE_CANON)
    f = state["current_exact_frontier"]
    req(state["schema"] == "STAGE32_MAIN_COMPACT_STATE_V26_N400_AUDIT_SYNCED", "synced schema")
    req(f["authoritative_remaining_strata"] == STRATA and f["authoritative_remaining_terminals"] == AUTH, "synced authority")
    req(f["authoritative_remaining_terminals_semantics"] == "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET", "authority semantics")
    req(f["n400_v25_replacement_hostile_audited"] is True, "audit PASS not synchronized")
    req(f["n400_v25_replacement_audited_exact_head"] == AUDITED_HEAD, "synced audited head")
    req(f["n400_v25_replacement_hostile_audit_review_id"] == AUDITED_REVIEW, "synced audit review")
    req(state["authority_sync"]["v25_n400_replacement_hostile_audit_status"] == "PASS", "authority sync status")
    req(state["current"]["mainbatch_stop_gate"] == "NONE", "MAIN stop gate not released")
    req(state["current"]["next_exact_route"] == "FULL178_THEN_EFFECTIVITY_MULTIBRANCH_AND_FINAL_SYNTHESIS", "next route")
    req(state["firewalls"]["replacement_head_hostile_reaudit_required"] is False, "stale re-audit firewall")
    req(f["full178_numerical_census_complete"] is False and f["stage32_closed"] is False, "closure overclaim")
    for key in ("effectivity_released", "endpoint_credit", "full178_complete", "merge_authorized", "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim", "receiver_credit", "route_credit", "stage32_closed", "theorem_credit"):
        req(state["firewalls"][key] is False, f"firewall unexpectedly true: {key}")

    lock = state["source_locks"]["n400_v26_audit_sync"]
    req(lock["reviewed_exact_head"] == AUDITED_HEAD, "state reviewed head lock")
    req(lock["reviewed_main_state_blob_sha1"] == AUDITED_STATE_BLOB, "state reviewed blob lock")
    req(lock["hostile_audit_review_id"] == AUDITED_REVIEW and lock["hostile_audit_status"] == "PASS", "state audit receipt lock")
    req(lock["audit_sync_receipt_blob_sha1"] == RECEIPT_BLOB, "state receipt blob lock")
    req(lock["claim_registry_blob_sha1"] == CLAIM_REGISTRY_BLOB, "state registry lock")
    req(lock["active_frontier_blob_sha1"] == ACTIVE_FRONTIER_BLOB, "state frontier lock")
    req(lock["lane_adapters_blob_sha1"] == LANE_ADAPTERS_BLOB, "state lane adapter lock")

    print(json.dumps({"verdict":"PASS_V26_N400_HOSTILE_AUDIT_SYNC","audited_exact_head":AUDITED_HEAD,"review_id":AUDITED_REVIEW,"remaining_strata":STRATA,"remaining_terminals_upper_bound":AUTH,"additional_pruning_credit":0,"full178_status":"ACTIVE_INCOMPLETE","next_route":"FULL178_THEN_EFFECTIVITY_MULTIBRANCH_AND_FINAL_SYNTHESIS","heavy_compute_authorized":False,"merge_authorized":False}, sort_keys=True))


if __name__ == "__main__":
    main()
