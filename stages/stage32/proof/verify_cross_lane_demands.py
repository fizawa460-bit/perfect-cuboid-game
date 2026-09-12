#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE = HERE.parent
MAIN_STATE = STAGE / "MAIN-STATE.json"
DEMANDS = HERE / "CROSS-LANE-DEMANDS.json"
N357_RECEIPT = STAGE / "management/post-n357-composition-pass-consumption-20260912.json"
CUT195_RECEIPT = STAGE / "management/post-cut195-current-v14-composition-consumption-20260912.json"
V15_SYNC_RECEIPT = STAGE / "management/post-cut195-replacement-head-hostile-pass-merge-sync-20260912.json"

V16_STATE_BLOB = "514fd4d3e4ba8ab5e33b0ff9537350e82a123ce0"
V16_STATE_CANONICAL = "23918007afdf7b01c7736dfb938d3d51261d3f79939627df7737fa7de12ba882"
DEMANDS_BLOB = "bbf4fc2460bad22c65359bc17aa89f8717e259a2"
DEMANDS_CANONICAL = "ae916d01b2690b2f86f06c754c83d396f947d4d2ed5df0b3adbdc42d10c2e62a"
N357_RECEIPT_BLOB = "033500e397a0e9d6dfa04638ab765a861cc523b8"
N357_RECEIPT_CANONICAL = "9e5209b77b7852df66673827782bbd6c0def6651409b711aff6969c69b8a8a5f"
CUT195_RECEIPT_BLOB = "148ea573bb1f618baac33c0d1f8cc91678fbbca2"
CUT195_RECEIPT_CANONICAL = "e33fb30bef69ce3ef87f095b500ecd4a8a21b155a3d9c957836ed17c82ad6be9"
V15_SYNC_RECEIPT_BLOB = "a38be20bf4db3342eb0fcea91c6f8aed50b03b54"
V15_SYNC_RECEIPT_CANONICAL = "9c5ef3da7907eb37b36e30d2feb7d47194d8765f8fac4cf72b1f102159190f2c"
POST_CUT191 = 65396964990500233636101
POST_CUT194 = 65396964990500233609659
POST_N357 = 47598978285064933783643
POST_CUT195 = 47598978285064933757427
CUT194_INCREMENT = 26442
N357_INCREMENT = 17797986705435299826016
CUT195_INCREMENT = 26216

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit(f"FAIL: {msg}")

def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canonical(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()

def load_locked(path: Path, blob: str, canon: str) -> dict:
    req(git_blob(path) == blob, f"blob drift: {path}")
    obj = json.loads(path.read_text(encoding="utf-8"))
    req(obj["canonical_sha256_without_this_field"] == canon, f"stored canonical drift: {path}")
    req(canonical(obj) == canon, f"canonical drift: {path}")
    return obj

def main() -> None:
    state = load_locked(MAIN_STATE, V16_STATE_BLOB, V16_STATE_CANONICAL)
    demands = load_locked(DEMANDS, DEMANDS_BLOB, DEMANDS_CANONICAL)
    load_locked(N357_RECEIPT, N357_RECEIPT_BLOB, N357_RECEIPT_CANONICAL)
    load_locked(CUT195_RECEIPT, CUT195_RECEIPT_BLOB, CUT195_RECEIPT_CANONICAL)
    sync = load_locked(V15_SYNC_RECEIPT, V15_SYNC_RECEIPT_BLOB, V15_SYNC_RECEIPT_CANONICAL)

    req(demands["schema"] == "STAGE32_CROSS_LANE_DEMANDS_V1", "demand schema drift")
    open_demands = [d["demand_id"] for d in demands["demands"] if d["status"] == "OPEN"]
    req(open_demands == [], f"unexpected OPEN cross-lane demands: {open_demands}")
    req(all(d["status"] in {"OPEN", "SATISFIED", "OBSOLETE"} for d in demands["demands"]),
        "invalid demand status")
    req(demands["credit_firewall"]["demand_satisfied_is_mathematical_credit"] is False,
        "demand satisfaction self-granted mathematical credit")
    req(demands["credit_firewall"]["merge_authorized"] is False,
        "demand registry self-authorized merge")

    frontier = state["current_exact_frontier"]
    req(frontier["cut191_main_pruning_credit"] is True, "CUT191 credit lost")
    req(frontier["cut194_main_pruning_credit"] is True, "CUT194 credit lost")
    req(frontier["n357_main_pruning_credit"] is True, "N357 credit lost")
    req(frontier["cut195_main_pruning_credit"] is True, "CUT195 credit lost")
    req(frontier["cut193_main_pruning_credit"] is False, "CUT193 unauthorized credit")
    req(frontier["cut196_main_pruning_credit"] is False, "CUT196 unauthorized credit")
    req(frontier["cut191_remaining_terminals"] == POST_CUT191, "post-CUT191 drift")
    req(frontier["cut194_remaining_terminals"] == POST_CUT194, "post-CUT194 drift")
    req(frontier["n357_remaining_terminals"] == POST_N357, "post-N357 drift")
    req(frontier["cut195_remaining_terminals"] == POST_CUT195, "post-CUT195 drift")
    req(frontier["authoritative_remaining_terminals"] == POST_CUT195, "authority count drift")
    req(frontier["authoritative_remaining_strata"] == 17128, "authority strata drift")
    req(POST_CUT191 - CUT194_INCREMENT == POST_CUT194, "CUT194 arithmetic drift")
    req(POST_CUT194 - N357_INCREMENT == POST_N357, "N357 arithmetic drift")
    req(POST_N357 - CUT195_INCREMENT == POST_CUT195, "CUT195 arithmetic drift")

    auth = state["authority_sync"]
    req(auth["n357_post_sync_reaudit_status"] == "PASS", "N357 re-audit not PASS")
    req(auth["cut195_candidate_hostile_audit_status"] == "PASS", "CUT195 candidate audit not PASS")
    req(auth["cut195_current_v14_overlap_n357_terminals"] == 0, "CUT195/N357 overlap")
    req(auth["cut195_post_sync_reaudit_status"] == "PASS", "CUT195 replacement re-audit not PASS")
    req(auth["cut195_synchronized_head_hostile_audited"] is True, "CUT195 sync audit flag false")
    req(auth["cut195_audited_head_tree_equals_current_main_tree"] is True, "V15/main tree mismatch")

    req(sync["authority_projection"]["cut195_post_sync_reaudit_consumed"] is True,
        "V15 external audit not consumed")
    req(sync["authority_projection"]["full178_frontier_status"] == "ACTIVE_INCOMPLETE",
        "FULL178 frontier status drift")
    req(sync["cut196_observation"]["main_pruning_credit"] is False,
        "CUT196 observation self-granted credit")
    req(sync["cut196_observation"]["claim_frontier_ci_conclusion"] == "FAILURE",
        "CUT196 failed CI observation lost")

    req(frontier["full178_numerical_census_complete"] is False, "FULL178 incorrectly complete")
    req(frontier["stage32_closed"] is False, "Stage32 incorrectly closed")
    req(state["firewalls"]["merge_authorized"] is False, "merge authorized")

    print(json.dumps({
        "verdict": "PASS_STAGE32_CROSS_LANE_DEMAND_COORDINATION_V16",
        "open_demands": 0,
        "cut191_main_consumed": True,
        "cut194_main_consumed": True,
        "n357_main_consumed": True,
        "cut195_main_consumed": True,
        "cut195_replacement_head_reaudit_consumed": True,
        "cut196_main_credit": False,
        "authoritative_remaining_terminals": POST_CUT195,
        "full178_frontier": "ACTIVE_INCOMPLETE",
        "stage32_closed": False,
        "merge_authorized": False,
    }, sort_keys=True))

if __name__ == "__main__":
    main()
