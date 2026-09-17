#!/usr/bin/env python3
from __future__ import annotations
import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
STATE = ROOT / "stages/stage32/MAIN-STATE.json"
RECEIPT = HERE / "HPADJ08-V29-MAIN-BOUND-REPLACEMENT.json"
CLAIM_SYNC = HERE / "HPADJ08-V29-CLAIM-SYNC.json"
CLAIM = ROOT / "stages/stage32/proof/CLAIM-REGISTRY.json"
FRONTIER = ROOT / "stages/stage32/proof/ACTIVE-FRONTIER.json"
LANES = ROOT / "stages/stage32/proof/LANE-ADAPTERS.json"

STATE_BLOB = "bd663e70864d7279063fa4eea9745fdfa479346d"
STATE_CANON = "3cbaa6e0b6b54cd379ba8770cc8e45c56c8444c13814f325fb9737222e306ecc"
RECEIPT_BLOB = "68a01142d0af4285d2a7801bf0e6808321ee689c"
RECEIPT_CANON = "9b7dde35f57960a1535b0dad5853ebeb75fe6d996902a653de1059fde0764f4d"
CLAIM_SYNC_BLOB = "7a98c733ee4ace141c89e40826f717f2462ebf95"
CLAIM_SYNC_CANON = "1f0f197f25d9fd059b52e8783d3615552edb9de5579eb6a66f00af879d312acb"
CLAIM_BLOB = "f3a884adc1c82aace81cb73d049ff14720ace862"
FRONTIER_BLOB = "4c251be4aa5c355481fe3bcfc71c292fb6389ba4"
LANES_BLOB = "c0ef34e5838e27046a20fed77063593009c56f40"

PRE_V28 = 26876434389242951065128
SOURCE_V24 = 26876434389242951089388
SAFE = 20173030585249740987894
POST = 6703403803993210101494
TIGHTEN = 20173030585249740963634
PRODUCER_HEAD = "36eab50192cf80ec5ed48aba40f4a56076759fea"
PRODUCER_REVIEW = 5208789388
ADAPTER_BLOB = "57bda3c27a9a2a7df2741e23a91c7a26ce3c7cc0"
ADAPTER_CANON = "14de9512d0ad1449b80b89f660ccbfd6d9e0864702e9b711234e8697596ff7c1"
PRODUCER_VERIFIER_BLOB = "65ed09517e1d37c318ca8c8798f10294ed5c6270"

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

def git_head(root: Path) -> str:
    return subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()

def verify_producer(root: Path) -> None:
    root = root.resolve()
    req(git_head(root) == PRODUCER_HEAD, "producer exact head")
    adapter = root / "stages/stage32-ex5/hpadj-08_ex5/CURRENT-MAIN-NO-DOUBLE-CHARGE-ADAPTER.json"
    pv = root / "stages/stage32-ex5/hpadj-08_ex5/verify_hpadj08_current_main_adapter.py"
    a = locked_json(adapter, ADAPTER_BLOB, ADAPTER_CANON)
    req(blob(pv) == PRODUCER_VERIFIER_BLOB, "producer verifier blob")
    acct = a["set_theoretic_accounting"]
    req(acct["current_main_pre_adapter_remaining_terminals_upper_bound"] == SOURCE_V24, "producer V24 source")
    req(acct["safe_current_main_incremental_rejected_terminals_lower_bound"] == SAFE, "producer safe increment")
    req(acct["candidate_post_adapter_remaining_terminals_upper_bound"] == POST, "producer post bound")
    req(acct["no_double_charge_proved_for_stated_lower_bound"] is True, "producer double-charge proof")
    subprocess.check_call([sys.executable, str(pv)], cwd=str(root))

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--producer-root", type=Path)
    args = ap.parse_args()

    state = locked_json(STATE, STATE_BLOB, STATE_CANON)
    receipt = locked_json(RECEIPT, RECEIPT_BLOB, RECEIPT_CANON)
    sync = locked_json(CLAIM_SYNC, CLAIM_SYNC_BLOB, CLAIM_SYNC_CANON)
    locked_json(CLAIM, CLAIM_BLOB)
    frontier = locked_json(FRONTIER, FRONTIER_BLOB)
    locked_json(LANES, LANES_BLOB)

    req(state["schema"] == "STAGE32_MAIN_COMPACT_STATE_V29_HPADJ08_BOUND_REPLACEMENT_PENDING_REAUDIT", "state schema")
    f = state["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == 17128, "strata")
    req(f["authoritative_remaining_terminals"] == POST, "terminal authority")
    req(f["authoritative_remaining_terminals_semantics"] == "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET", "authority semantics")
    req(f["pre_hpadj08_v28_remaining_terminals_upper_bound"] == PRE_V28, "predecessor bound")
    req(f["hpadj08_source_v24_remaining_terminals_upper_bound"] == SOURCE_V24, "source V24 bound")
    req(f["hpadj08_safe_v24_incremental_rejected_terminals_lower_bound"] == SAFE, "safe increment")
    req(f["hpadj08_independent_post_adapter_remaining_terminals_upper_bound"] == POST, "post bound")
    req(f["hpadj08_certified_numeric_bound_tightening_vs_v28"] == TIGHTEN, "numeric tightening")
    req(f["hpadj08_composition_rule"] == "MIN_OF_INDEPENDENT_CERTIFIED_UPPER_BOUNDS__NO_ADDITIVE_STACKING", "composition rule")
    req(f["hpadj08_exact_incremental_rejected_set_vs_v28_claimed"] is False, "exact-set overclaim")
    req(f["hpadj08_additive_subtraction_against_v28_performed"] is False, "additive stacking")
    req(f["hpadj08_double_charge"] is False, "double charge")
    req(state["current"]["mainbatch_stop_gate"] == "REPLACEMENT_HEAD_HOSTILE_REAUDIT_REQUIRED", "stop gate")
    req(state["firewalls"]["replacement_head_hostile_reaudit_required"] is True, "reaudit firewall")
    for key in ("effectivity_released","endpoint_credit","full178_complete","merge_authorized",
                "perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim",
                "receiver_credit","route_credit","stage32_closed","theorem_credit"):
        req(state["firewalls"][key] is False, f"firewall unexpectedly true: {key}")

    a = receipt["accounting"]
    req(a["pre_transition_v28_remaining_terminals_upper_bound"] == PRE_V28, "receipt V28")
    req(a["hpadj08_source_v24_remaining_terminals_upper_bound"] == SOURCE_V24, "receipt V24")
    req(a["hpadj08_safe_v24_incremental_rejected_terminals_lower_bound"] == SAFE, "receipt safe")
    req(a["post_transition_certified_remaining_terminals_upper_bound"] == POST, "receipt post")
    req(a["certified_numeric_bound_tightening_vs_v28"] == TIGHTEN, "receipt tightening")
    req(a["composition_rule"] == "MIN_OF_INDEPENDENT_CERTIFIED_UPPER_BOUNDS__NO_ADDITIVE_STACKING", "receipt composition")
    req(a["additive_subtraction_from_v28_performed"] is False, "receipt additive stacking")
    req(a["n400_or_cut201_subtracted_again_against_hpadj08_bound"] is False, "receipt N400/CUT201 double charge")
    req(a["h8c03a_subtracted_against_hpadj08_bound"] is False, "receipt H8C03A stacking")
    req(a["double_charge"] is False, "receipt double charge")
    req(min(PRE_V28, POST) == POST, "min composition arithmetic")
    req(SOURCE_V24 - SAFE == POST, "producer arithmetic")
    req(PRE_V28 - POST == TIGHTEN, "tightening arithmetic")

    req(receipt["source_locks"]["hpadj08_ex5_current_main_adapter"]["audited_exact_head"] == PRODUCER_HEAD, "producer audit head")
    req(receipt["source_locks"]["hpadj08_ex5_current_main_adapter"]["hostile_audit_review_id"] == PRODUCER_REVIEW, "producer audit review")
    req(receipt["promotion"]["main_numeric_bound_replacement_consumed"] is True, "numeric authority not consumed")
    req(receipt["promotion"]["exact_incremental_main_pruning_credit_consumed"] is False, "exact pruning credit overclaim")
    req(receipt["promotion"]["claim_dag_changed"] is False, "claim DAG changed")
    req(receipt["promotion"]["replacement_head_hostile_reaudit_required"] is True, "receipt re-audit gate")

    req(sync["decision"]["mathematical_claim_core_changed"] is False, "claim core mutation")
    req(sync["decision"]["claim_registry_mutated"] is False, "claim registry mutation")
    req(sync["decision"]["active_frontier_mutated"] is False, "active frontier mutation")
    req(sync["decision"]["lane_adapter_mutated"] is False, "lane adapter mutation")
    req(sync["decision"]["main_state_numeric_authority_changed"] is True, "numeric authority sync missing")
    req(sync["authority_boundary"]["remaining_terminals_upper_bound"] == POST, "claim-sync bound")
    req(sync["authority_boundary"]["full178_complete"] is False, "claim-sync FULL178 overclaim")

    full178 = find_claim(frontier, "S32.FULL178.NUMERICAL_CENSUS.V1")
    req(full178 is not None, "FULL178 frontier claim missing")
    req(full178.get("frontier_status") == "ACTIVE_INCOMPLETE", "FULL178 frontier promotion")
    req(full178.get("audit_receipt", {}).get("status") == "NOT_AUDITED_GOAL", "FULL178 audit promotion")

    if args.producer_root is not None:
        verify_producer(args.producer_root)

    print(json.dumps({
        "verdict":"PASS_V29_HPADJ08_BOUND_REPLACEMENT",
        "remaining_strata":17128,
        "remaining_terminals_upper_bound":POST,
        "numeric_bound_tightening_vs_v28":TIGHTEN,
        "composition":"MIN_NO_ADDITIVE_STACKING",
        "producer_exact_replay":args.producer_root is not None,
        "full178_status":"ACTIVE_INCOMPLETE",
        "replacement_head_hostile_reaudit_required":True,
        "merge_authorized":False
    }, sort_keys=True))

if __name__ == "__main__":
    main()
