#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "BC2-41-MAIN-DISPOSITION.json"
MAIN_STATE = ROOT / "stages/stage32/MAIN-STATE.json"
CROSS_LANE = ROOT / "stages/stage32/proof/CROSS-LANE-DEMANDS.json"

EXPECTED_RECEIPT_CANON = "88f23dd5676157331c4f212eeae745ead0b51db4dddeacbedd1cf14f2749fd12"
EXPECTED_MAIN_CANON = "39b66cb72dd60900158e60cbca9e0c8dbd15bff3d77f7d9ed2fd096e0f12b9dd"
EXPECTED_CROSS_LANE_CANON = "600e877e1d0764c4ac0687282d2836707e06b55d6248cf7a0c6fe5b845842161"
PRODUCER_HEAD = "98f13bd5527e53c5e77e7f85c72b3fa46db19d9f"
CANDIDATE_PATH = "stages/stage32-ex5/breadth-cycle-2/bc2-41-first-e8-block-main-subtraction-adapter-candidate.json"
EXPECTED_CANDIDATE_BLOB = "12791a4300afac6ce8b5324982d2ac63208dd4e7"
EXPECTED_CANDIDATE_CANON = "cd40eb0e9b380eb219d94fd75d44b457bcdb3d1edee83f1c9a56cac38415628a"
CUT191_RESULT_ID = "S32.CUT191.FIRST_BLOCK.113_TERMINAL_PRUNING.V1"
AUTHORITY = 26876434389242951083886


def req(value: bool, msg: str) -> None:
    if not value:
        raise SystemExit("FAIL: " + msg)


def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def ensure_commit(sha: str) -> None:
    try:
        subprocess.check_call(
            ["git", "cat-file", "-e", f"{sha}^{{commit}}"],
            cwd=ROOT,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        subprocess.check_call(["git", "fetch", "--no-tags", "origin", sha], cwd=ROOT)


def producer_json() -> dict:
    ensure_commit(PRODUCER_HEAD)
    blob = subprocess.check_output(
        ["git", "rev-parse", f"{PRODUCER_HEAD}:{CANDIDATE_PATH}"],
        cwd=ROOT,
        text=True,
    ).strip()
    req(blob == EXPECTED_CANDIDATE_BLOB, "BC2-41 producer candidate blob drift")
    raw = subprocess.check_output(
        ["git", "show", f"{PRODUCER_HEAD}:{CANDIDATE_PATH}"],
        cwd=ROOT,
        text=True,
    )
    return json.loads(raw)


def main() -> None:
    r = json.loads(RECEIPT.read_text())
    m = json.loads(MAIN_STATE.read_text())
    x = json.loads(CROSS_LANE.read_text())
    c = producer_json()

    req(r["canonical_sha256_without_this_field"] == EXPECTED_RECEIPT_CANON, "receipt declared canonical")
    req(canonical(r) == EXPECTED_RECEIPT_CANON, "receipt canonical replay")
    req(m["canonical_sha256_without_this_field"] == EXPECTED_MAIN_CANON, "MAIN declared canonical")
    req(canonical(m) == EXPECTED_MAIN_CANON, "MAIN canonical replay")
    req(x["canonical_sha256_without_this_field"] == EXPECTED_CROSS_LANE_CANON, "cross-lane declared canonical")
    req(canonical(x) == EXPECTED_CROSS_LANE_CANON, "cross-lane canonical replay")

    req(c["canonical_sha256_without_this_field"] == EXPECTED_CANDIDATE_CANON, "BC2-41 candidate declared canonical")
    req(canonical(c) == EXPECTED_CANDIDATE_CANON, "BC2-41 candidate canonical replay")
    target = c["target"]
    req(target["row_id"] == "g1-d008" and target["g"] == 1 and target["d"] == 8 and target["e"] == 8, "BC2-41 row identity")
    req(target["block_index"] == 0, "BC2-41 block index")
    req(target["terminal_rank_range"] == [0, 112] and target["terminal_count"] == 113, "BC2-41 rank set")
    req(c["candidate_consequence"]["main_terminal_subtraction_candidate"] == 113, "BC2-41 candidate cardinality")
    req(c["candidate_consequence"]["main_terminal_subtraction_authorized"] is False, "BC2-41 producer must not self-authorize MAIN subtraction")

    cut191 = next((z for z in x["audited_result_consumption"] if z.get("result_id") == CUT191_RESULT_ID), None)
    req(cut191 is not None, "CUT191 consumed-result record missing")
    req(cut191["producer_lane"] == "CUT", "CUT191 producer lane")
    req(cut191["main_consumed"] is True, "CUT191 not marked MAIN-consumed")
    req(cut191["main_consumption_required"] is True, "CUT191 consumption contract")
    req(cut191["main_consumption_audit_review_id"] == 5177949195, "CUT191 MAIN-consumption review")
    req(cut191["main_synchronized_exact_head"] == "6d63d798adb50dd4efc5f0d5abc553b3dfa23060", "CUT191 synchronized MAIN head")
    req(cut191["main_synchronized_reaudit_review_id"] == 5178420739, "CUT191 synchronized re-audit review")

    cut191_semantics = None
    for demand in x["demands"]:
        sp = demand.get("source_population_semantics") or {}
        if "consumed_cut191_first_block_rank_range" in sp:
            cut191_semantics = sp
            break
    req(cut191_semantics is not None, "CUT191 first-block rank semantics missing")
    req(cut191_semantics["degree_e"] == 8, "CUT191 degree")
    req(cut191_semantics["consumed_cut191_first_block_rank_range"] == [0, 112], "CUT191 consumed rank range")
    req(cut191_semantics["cut191_main_credit_already_consumed"] is True, "CUT191 credit not marked consumed")

    frontier = m["current_exact_frontier"]
    req(frontier["cut191_main_pruning_credit"] is True, "current MAIN does not retain CUT191 credit")
    req(frontier["authoritative_remaining_strata"] == 17128, "MAIN strata authority drift")
    req(frontier["authoritative_remaining_terminals"] == AUTHORITY, "MAIN terminal authority drift")
    req(frontier["authoritative_remaining_terminals_semantics"] == "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET", "MAIN authority semantics")

    candidate_ranks = set(range(target["terminal_rank_range"][0], target["terminal_rank_range"][1] + 1))
    cut191_ranks = set(range(cut191_semantics["consumed_cut191_first_block_rank_range"][0], cut191_semantics["consumed_cut191_first_block_rank_range"][1] + 1))
    overlap = candidate_ranks & cut191_ranks
    incremental = candidate_ranks - cut191_ranks
    req(candidate_ranks == cut191_ranks, "BC2-41/CUT191 exact rank-set equality")
    req(len(overlap) == 113, "BC2-41/CUT191 overlap count")
    req(len(incremental) == 0, "BC2-41 unexpectedly contains incremental ranks")

    oa = r["overlap_accounting"]
    req(oa["exact_rank_set_equality"] is True, "receipt exact-rank equality")
    req(oa["overlap_terminal_count"] == 113, "receipt overlap count")
    req(oa["incremental_new_terminal_count"] == 0, "receipt incremental count")
    req(oa["double_charge_if_subtracted_again"] is True, "receipt double-charge classification")
    req(oa["main_terminal_subtraction_authorized"] is False, "receipt subtraction firewall")

    auth = r["authority"]
    req(auth["remaining_terminals_before"] == AUTHORITY and auth["remaining_terminals_after"] == AUTHORITY, "receipt authority must remain unchanged")
    req(auth["remaining_strata_before"] == 17128 and auth["remaining_strata_after"] == 17128, "receipt strata must remain unchanged")
    req(auth["authority_mutated"] is False, "receipt authority mutation firewall")
    req(all(v is False for v in r["credit_firewall"].values()), "receipt credit firewall")

    print("PASS_BC2_41_MAIN_DISPOSITION_FULL_OVERLAP_ZERO_INCREMENTAL_CREDIT")
    print("candidate=113 overlap_with_consumed_CUT191=113 incremental=0 authority_unchanged=YES")


if __name__ == "__main__":
    main()
