#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STAGE = ROOT / "stages/stage32"
STATE = STAGE / "MAIN-STATE.json"
CUT = STAGE / "full178-cut"
MGMT = STAGE / "management/post-cut191-hostile-pass-consumption-20260911.json"

PRE_N356_REMAIN = 66462870551188628549910
POST_N356_REMAIN = 65396964990500233636214
POST_CUT191_REMAIN = 65396964990500233636101
CUT191_COUNT = 113

EXPECTED = {
    "state_blob": "a4a44db9c928d614ffb4c936726dc03c267ae3c5",
    "state_canonical": "9167620fab303b3bf8ffa6fcae2e2201bcd4d8e3b0c7ad2b41f6263a4dfd0106",
    "cut_checkpoint_blob": "a90042ec931cb487ae6be852524db5a4537862f4",
    "cut_checkpoint_canonical": "1e681c456dc30342346d134f5e0d89150573f8a756cbd808c309d2af89821fdd",
    "cut_handoff_blob": "016c92ea002bf8e5a04836933b6bb1729fa9aa7d",
    "cut_handoff_canonical": "a779e5aa5b8e01c373f356302b8da371fe349f7e1c08f5840b499c02b22645ba",
    "cut_historical_verifier_blob": "c0e54907ca4ec0bce9302113ef89fb6e935834f7",
    "cut_pass_blob": "57ab3aa10ea40300f80622d57c8738edc2fa4bff",
    "cut_pass_canonical": "5667fbf15a2472dcb8fb972b32639c2fc6a69d0b6bffe5ccc6d032685c43f629",
    "management_blob": "8bea39e443d7996a8958c95005206d6ff349fa52",
    "management_canonical": "f1c59f708190f99ef87422eabc443a5c9df981438a5e647c93dc5052fc5fe6a2",
}


def git_blob_sha(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def load_canonical(path: Path, canonical: str) -> dict:
    obj = json.loads(path.read_text())
    assert obj["canonical_sha256_without_this_field"] == canonical, path
    assert csha(obj) == canonical, path
    return obj


def assert_blob(path: Path, expected: str) -> None:
    actual = git_blob_sha(path)
    assert actual == expected, f"{path}: {actual}!={expected}"


def main() -> None:
    # The transition is stacked on the hostile-audited #1781 authority head.
    # Until this MAIN transition itself is externally audited, the parent V11
    # MAIN-STATE remains byte-exact and no unreviewed startup-authority mutation
    # is accepted here.
    assert_blob(STATE, EXPECTED["state_blob"])
    state = load_canonical(STATE, EXPECTED["state_canonical"])
    assert state["schema"] == "STAGE32_MAIN_COMPACT_STATE_V11_N356_AUDITED_CONSUMED"
    frontier = state["current_exact_frontier"]
    assert frontier["authoritative_remaining_strata"] == 17128
    assert frontier["authoritative_remaining_terminals"] == POST_N356_REMAIN
    assert frontier["n356_main_pruning_credit"] is True
    assert frontier["n357_main_pruning_credit"] is False

    checkpoint_path = CUT / "CUT191-first-block-closure-checkpoint.json"
    handoff_path = CUT / "CUT191-AUDIT-HANDOFF.json"
    verifier_path = CUT / "verify_cut191_exact_head_audit.py"
    pass_path = CUT / "CUT191-HOSTILE-AUDIT-PASS.json"
    assert_blob(checkpoint_path, EXPECTED["cut_checkpoint_blob"])
    assert_blob(handoff_path, EXPECTED["cut_handoff_blob"])
    assert_blob(verifier_path, EXPECTED["cut_historical_verifier_blob"])
    assert_blob(pass_path, EXPECTED["cut_pass_blob"])
    assert_blob(MGMT, EXPECTED["management_blob"])

    checkpoint = load_canonical(checkpoint_path, EXPECTED["cut_checkpoint_canonical"])
    handoff = load_canonical(handoff_path, EXPECTED["cut_handoff_canonical"])
    audit_pass = load_canonical(pass_path, EXPECTED["cut_pass_canonical"])
    mgmt = load_canonical(MGMT, EXPECTED["management_canonical"])

    assert audit_pass["status"] == "PASS"
    assert audit_pass["pr"] == 1779
    assert audit_pass["review_id"] == 5177635336
    assert audit_pass["audited_exact_head"] == "c1bba42b8b61040ce567037cf864fcfb3e6a1746"
    assert audit_pass["exact_head_workflow_run"] == 34588749601

    credit = checkpoint["credit"]
    assert credit["stage32_main_pruning_candidate"] is True
    assert credit["stage32_main_pruning_candidate_terminals"] == CUT191_COUNT
    assert credit["stage32_main_pruning_credit"] is False
    assert checkpoint["population_preimage"]["first_block_rank_range"] == [0, 112]
    assert checkpoint["population_preimage"]["rank_unrank_replay_count"] == 113
    assert checkpoint["coverage_certificate"]["covered_parent_count"] == 7336
    assert checkpoint["coverage_certificate"]["sat_parent_count"] == 0
    assert checkpoint["coverage_certificate"]["unknown_parent_count"] == 0

    assert handoff["claim_candidate"]["stage32_main_pruning_candidate_terminals"] == 113
    assert handoff["claim_candidate"]["n356_assumed_consumed"] is False

    # Exact overlap replay against already-consumed N356.
    sums = checkpoint["population_preimage"]["n355_group_sums_on_first_block"]
    assert sums == [0, 1, 1]
    a, b, c = sums
    d = checkpoint["target"]["d"]
    e = checkpoint["target"]["e"]
    lhs = b - c
    rhs = 3 * d - e
    assert (a, b, c, d, e, lhs, rhs) == (0, 1, 1, 8, 8, 0, 16)
    assert lhs <= rhs
    # Thus N356 rejects none of the 113 CUT191 terminals; the CUT191 saving is
    # fully incremental after N356, with no double charge.
    assert POST_N356_REMAIN == PRE_N356_REMAIN - 1065905560688394913696
    assert POST_CUT191_REMAIN == POST_N356_REMAIN - CUT191_COUNT

    assert mgmt["n356_overlap_replay"]["n356_preserves_all_113_cut191_terminals"] is True
    assert mgmt["n356_overlap_replay"]["double_charge"] is False
    assert mgmt["authority"]["cut191_main_pruning_credit"] is True
    assert mgmt["authority"]["cut191_incremental_rejected_terminals"] == CUT191_COUNT
    assert mgmt["authority"]["authoritative_remaining_strata"] == 17128
    assert mgmt["authority"]["authoritative_remaining_terminals"] == POST_CUT191_REMAIN
    assert mgmt["authority"]["full178_complete"] is False
    assert mgmt["route"]["owner"] == "stage32-01-178-mainbatch"

    for key, value in mgmt["firewalls"].items():
        if key == "whole_g1_d008_e8_stratum_closed":
            assert value is False
        elif isinstance(value, bool):
            assert value is False, key

    print(json.dumps({
        "verdict": "PASS_STAGE32_MAIN_CUT191_CONSUMPTION_CANDIDATE",
        "pre_cut_authority": POST_N356_REMAIN,
        "cut191_incremental_reject": CUT191_COUNT,
        "post_cut_authority": POST_CUT191_REMAIN,
        "remaining_strata": 17128,
        "n356_overlap": "DISJOINT_N356_PRESERVES_ALL_113",
        "full178_complete": False,
        "main_transition_hostile_audit_required": True,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
