#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE = HERE.parent
ROOT = STAGE.parents[1]
STATE = STAGE / "MAIN-STATE.json"
PREDECESSOR = STAGE / "management/MAIN-STATE-V17-CUT196-PRE-REAUDIT.json"
RECEIPT = STAGE / "management/post-cut196-v17-hostile-reaudit-pass-consumption-20260912.json"

STATE_BLOB = "48a3b18671ddd85a8b0916a8be1d9f611c38b534"
STATE_CANONICAL = "8590ba2d6a8d9e5250f5849a5052a3abeef43884eee2e237d5372dd61f841bef"
PREDECESSOR_BLOB = "157acdb438bfbde40a71a5974effbd097bff05df"
PREDECESSOR_CANONICAL = "a21faa5b3c3f5be259d8c5bc7ffa6f7aac827b911256e7a916e0bf9ea8e85de9"
RECEIPT_BLOB = "e9948350c09dfd769e6cf05297731fb499c2d677"
RECEIPT_CANONICAL = "e93fdfdd9405de44c6db459aa59a073f097da8fd3ffb2c34479ed63f543f1cb3"

POST_CUT191 = 65396964990500233636101
CUT194_INCREMENT = 26442
POST_CUT194 = 65396964990500233609659
N357_INCREMENT = 17797986705435299826016
POST_N357 = 47598978285064933783643
CUT195_INCREMENT = 26216
POST_CUT195 = 47598978285064933757427
CUT196_INCREMENT = 27346
POST_CUT196 = 47598978285064933730081

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)

def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canonical(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()

def load_locked(path: Path, blob: str, can: str) -> dict:
    req(path.is_file(), f"missing {path.relative_to(ROOT)}")
    req(git_blob(path) == blob, f"blob drift {path.relative_to(ROOT)}")
    obj = json.loads(path.read_text(encoding="utf-8"))
    req(obj.get("canonical_sha256_without_this_field") == can,
        f"stored canonical drift {path.relative_to(ROOT)}")
    req(canonical(obj) == can, f"canonical drift {path.relative_to(ROOT)}")
    return obj

def main() -> None:
    prev = load_locked(PREDECESSOR, PREDECESSOR_BLOB, PREDECESSOR_CANONICAL)
    receipt = load_locked(RECEIPT, RECEIPT_BLOB, RECEIPT_CANONICAL)
    state = load_locked(STATE, STATE_BLOB, STATE_CANONICAL)

    pf = prev["current_exact_frontier"]
    req(pf["authoritative_remaining_terminals"] == POST_CUT196,
        "predecessor CUT196 authority drift")
    req(pf["cut196_main_pruning_credit"] is True,
        "predecessor CUT196 MAIN credit missing")
    req(pf["cut196_synchronized_head_hostile_audited"] is False,
        "predecessor replacement audit self-awarded")

    f = state["current_exact_frontier"]
    req(f["cut191_main_pruning_credit"] is True, "CUT191 lost MAIN credit")
    req(f["cut194_main_pruning_credit"] is True, "CUT194 lost MAIN credit")
    req(f["n357_main_pruning_credit"] is True, "N357 lost MAIN credit")
    req(f["cut195_main_pruning_credit"] is True, "CUT195 lost MAIN credit")
    req(f["cut193_main_pruning_credit"] is False, "CUT193 gained unauthorized MAIN credit")
    req(f["cut196_main_pruning_credit"] is True, "CUT196 lost MAIN credit")
    req(f["cut196_synchronized_head_hostile_audited"] is True,
        "CUT196 replacement-head audit not consumed")
    req(f["cut197_main_pruning_credit"] is False,
        "CUT197 gained unauthorized MAIN credit")
    req(f["cut197_candidate_hostile_audited"] is False,
        "CUT197 gained unauthorized hostile audit")
    req(f["cut197_retained_result_frozen"] is False,
        "CUT197 retained freeze self-awarded")
    req(f["authoritative_remaining_strata"] == 17128, "strata drift")
    req(f["authoritative_remaining_terminals"] == POST_CUT196,
        "terminal authority changed during audit synchronization")
    req(f["full178_numerical_census_complete"] is False,
        "FULL178 incorrectly closed")
    req(f["stage32_closed"] is False, "Stage32 incorrectly closed")

    req(POST_CUT191 - CUT194_INCREMENT == POST_CUT194, "CUT194 arithmetic drift")
    req(POST_CUT194 - N357_INCREMENT == POST_N357, "N357 arithmetic drift")
    req(POST_N357 - CUT195_INCREMENT == POST_CUT195, "CUT195 arithmetic drift")
    req(POST_CUT195 - CUT196_INCREMENT == POST_CUT196, "CUT196 arithmetic drift")

    ra = receipt["authority"]
    req(ra["authority_before_and_after_same"] is True,
        "audit synchronization changed authority")
    req(ra["before_remaining_terminals"] == POST_CUT196 and
        ra["after_remaining_terminals"] == POST_CUT196,
        "audit-sync terminal receipt drift")
    c = receipt["cut197_frontier"]
    req(c["pr"] == 1798 and
        c["observed_exact_head"] == "c23df92827f7be9dbe9ca28cd240a576581b1763",
        "CUT197 selection identity drift")
    req(c["heavy_workflow_run"] == 34691947196 and
        c["heavy_workflow_status"] == "SUCCESS",
        "CUT197 heavy evidence drift")
    req(c["retained_result_frozen"] is False and
        c["hostile_audit_status"] == "NOT_AUDITED" and
        c["stage32_main_pruning_credit"] is False,
        "CUT197 zero-credit firewall drift")

    auth = state["authority_sync"]
    req(auth["cut196_post_sync_reaudit_status"] == "PASS",
        "CUT196 replacement re-audit PASS missing")
    req(auth["cut196_post_sync_reaudit_review_id"] == 5186409565,
        "CUT196 replacement re-audit review drift")
    req(auth["cut197_candidate_hostile_audit_status"] == "NOT_AUDITED",
        "CUT197 audit status drift")
    req(auth["cut197_main_pruning_credit_consumed"] is False,
        "CUT197 consumption flag drift")

    fw = state["firewalls"]
    req(fw["merge_authorized"] is False, "merge authorized")
    req(fw["receiver_credit"] is False and fw["theorem_credit"] is False and
        fw["endpoint_credit"] is False, "final-chain firewall opened")

    print(json.dumps({
        "verdict":"PASS_STAGE32_CROSS_LANE_DEMAND_COORDINATION_V18",
        "cut191_main_consumed":True,
        "cut194_main_consumed":True,
        "n357_main_consumed":True,
        "cut195_main_consumed":True,
        "cut196_main_consumed":True,
        "cut193_main_credit":False,
        "cut197_main_credit":False,
        "cut197_heavy_success":True,
        "cut197_retained_result_frozen":False,
        "authoritative_remaining_terminals":POST_CUT196,
        "full178_complete":False,
        "merge_authorized":False
    }, sort_keys=True))

if __name__ == "__main__":
    main()
