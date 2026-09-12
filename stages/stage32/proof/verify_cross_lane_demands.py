#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE = HERE.parent
ROOT = STAGE.parents[1]
STATE = STAGE / "MAIN-STATE.json"
RECEIPT = STAGE / "management/post-n358-current-v18-composition-consumption-20260912.json"

STATE_BLOB = "acad022fe90b4d72edeac5f9d7ba08930decdff2"
STATE_CANONICAL = "2f0ed49bd3640f4f7158176bc435344d46785928e20c4ce67173305eb3974771"
RECEIPT_BLOB = "efa87a1b62cc698745f87814cd8f9eb9fe95dbd2"
RECEIPT_CANONICAL = "27c50848e19c242389298b6a23d7c5b6a8ea86afd97c36ced16905adc66a5bdc"

POST_CUT191 = 65396964990500233636101
CUT194_INCREMENT = 26442
POST_CUT194 = 65396964990500233609659
N357_INCREMENT = 17797986705435299826016
POST_N357 = 47598978285064933783643
CUT195_INCREMENT = 26216
POST_CUT195 = 47598978285064933757427
CUT196_INCREMENT = 27346
POST_CUT196 = 47598978285064933730081
N358_INCREMENT = 9274971107798843958
POST_N358 = 47589703313957134886123

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)

def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canonical(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()

def load_locked(path: Path, blob: str, can: str) -> dict:
    req(path.is_file(), f"missing {path.relative_to(ROOT)}")
    req(git_blob(path) == blob, f"blob drift {path.relative_to(ROOT)}")
    obj = json.loads(path.read_text(encoding="utf-8"))
    req(obj.get("canonical_sha256_without_this_field") == can, f"stored canonical drift {path.relative_to(ROOT)}")
    req(canonical(obj) == can, f"canonical drift {path.relative_to(ROOT)}")
    return obj

def main() -> None:
    state = load_locked(STATE, STATE_BLOB, STATE_CANONICAL)
    receipt = load_locked(RECEIPT, RECEIPT_BLOB, RECEIPT_CANONICAL)

    f = state["current_exact_frontier"]
    req(f["cut191_main_pruning_credit"] is True, "CUT191 lost MAIN credit")
    req(f["cut194_main_pruning_credit"] is True, "CUT194 lost MAIN credit")
    req(f["n357_main_pruning_credit"] is True, "N357 lost MAIN credit")
    req(f["cut195_main_pruning_credit"] is True, "CUT195 lost MAIN credit")
    req(f["cut196_main_pruning_credit"] is True, "CUT196 lost MAIN credit")
    req(f["n358_main_pruning_credit"] is True, "N358 MAIN credit missing")
    req(f["cut193_main_pruning_credit"] is False, "CUT193 gained unauthorized MAIN credit")
    req(f["cut197_main_pruning_credit"] is False, "CUT197 gained unauthorized MAIN credit")
    req(f["authoritative_remaining_strata"] == 17128, "strata drift")
    req(f["authoritative_remaining_terminals"] == POST_N358, "terminal authority drift")
    req(f["full178_numerical_census_complete"] is False, "FULL178 incorrectly closed")
    req(f["stage32_closed"] is False, "Stage32 incorrectly closed")

    req(POST_CUT191 - CUT194_INCREMENT == POST_CUT194, "CUT194 arithmetic drift")
    req(POST_CUT194 - N357_INCREMENT == POST_N357, "N357 arithmetic drift")
    req(POST_N357 - CUT195_INCREMENT == POST_CUT195, "CUT195 arithmetic drift")
    req(POST_CUT195 - CUT196_INCREMENT == POST_CUT196, "CUT196 arithmetic drift")
    req(POST_CUT196 - N358_INCREMENT == POST_N358, "N358 arithmetic drift")

    rr = receipt["current_v18_composition_replay"]
    req(rr["n357_overlap_terminals"] == 0, "N358/N357 overlap drift")
    req(all(x["n358_overlap_terminals"] == 0 for x in rr["consumed_cut_targets"]), "N358/consumed-cut overlap drift")
    req(rr["already_consumed_cut_total_terminals"] == 80117, "consumed-cut total drift")
    req(rr["double_charge"] is False, "N358 double-charge flag set")
    req(receipt["authority"]["after_remaining_terminals"] == POST_N358, "receipt authority drift")

    auth = state["authority_sync"]
    req(auth["n358_candidate_hostile_audit_status"] == "PASS", "N358 hostile audit PASS missing")
    req(auth["n358_main_pruning_credit_consumed"] is True, "N358 consumption flag false")
    req(auth["n358_post_sync_reaudit_status"] == "PENDING", "N358 replacement audit self-awarded")
    req(auth["cut197_main_pruning_credit_consumed"] is False, "CUT197 consumption flag drift")

    fw = state["firewalls"]
    req(fw["merge_authorized"] is False, "merge authorized")
    req(fw["receiver_credit"] is False and fw["theorem_credit"] is False and fw["endpoint_credit"] is False,
        "final-chain firewall opened")

    print(json.dumps({
        "verdict":"PASS_STAGE32_CROSS_LANE_DEMAND_COORDINATION_V19",
        "cut191_main_consumed":True,
        "cut194_main_consumed":True,
        "n357_main_consumed":True,
        "cut195_main_consumed":True,
        "cut196_main_consumed":True,
        "n358_main_consumed":True,
        "cut193_main_credit":False,
        "cut197_main_credit":False,
        "n358_overlap_consumed_main_terminals":0,
        "authoritative_remaining_terminals":POST_N358,
        "full178_complete":False,
        "merge_authorized":False
    }, sort_keys=True))

if __name__ == "__main__":
    main()
