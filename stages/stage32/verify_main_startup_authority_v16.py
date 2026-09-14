#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE_PATH = ROOT / "stages/stage32/MAIN-STATE.json"
PREDECESSOR_V15_PATH = ROOT / "stages/stage32/management/MAIN-STATE-V15-CUT195-PRE-REAUDIT.json"
RECEIPT_PATH = ROOT / "stages/stage32/management/post-cut195-v15-hostile-reaudit-pass-consumption-20260912.json"

EXPECTED_PREDECESSOR_V15_BLOB = "73cc6ef56647a4be9119e89bf42c8ba4d96d54c9"
EXPECTED_PREDECESSOR_V15_CANONICAL = "d61dd73ecf0c0fa6fc1a96ea37f284dac4d5beb65c88bff59d5cc25b87939193"
EXPECTED_STATE_BLOB = "1b46f01070f5bbf1b81ba5c84684dcaa1a459119"
EXPECTED_STATE_CANONICAL = "cd1865abe9918e1b5a64d2b9148f378a54cc24b203f16295ce256685164d3fd8"
EXPECTED_RECEIPT_BLOB = "cffa669d06d1d7cb73a7550b4df3e6572b8112e6"
EXPECTED_RECEIPT_CANONICAL = "1468c81e76e233f18f8433a36c3aae5a8a62d475e082924fc20a10f5c31bf0fa"

AUDITED_V15_HEAD = "fdc372e1666e1176d80953b6303b13b240da84c5"
AUDIT_REVIEW = 5185987769
MERGED_MAIN = "e4d3b8b83626526ffeccdbd9c956081735fe1a6e"
CUT196_HEAD = "85f4e988acf6446fa0d472208e21990621a650b4"
CUT196_CI = 34687223279
AUTH_STRATA = 17128
AUTH_TERMINALS = 47598978285064933757427


def fail(msg: str) -> None:
    raise SystemExit("FAIL: " + msg)


def req(cond: bool, msg: str) -> None:
    if not cond:
        fail(msg)


def blob_sha1(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def canonical(obj: dict) -> str:
    copy = dict(obj)
    copy.pop("canonical_sha256_without_this_field", None)
    payload = json.dumps(copy, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(payload).hexdigest()


def load_locked(path: Path, blob: str, can: str) -> dict:
    data = path.read_bytes()
    req(blob_sha1(data) == blob, f"blob mismatch: {path.relative_to(ROOT)}")
    obj = json.loads(data)
    req(obj.get("canonical_sha256_without_this_field") == can,
        f"stored canonical mismatch: {path.relative_to(ROOT)}")
    req(canonical(obj) == can, f"recomputed canonical mismatch: {path.relative_to(ROOT)}")
    return obj


def main() -> None:
    # Retain the exact V15 routing bytes inside the repository rather than
    # relying on Git history. This keeps shallow exact-head CI fail-closed.
    prev = load_locked(
        PREDECESSOR_V15_PATH,
        EXPECTED_PREDECESSOR_V15_BLOB,
        EXPECTED_PREDECESSOR_V15_CANONICAL,
    )
    req(prev.get("schema") == "STAGE32_MAIN_COMPACT_STATE_V15_CUT195_AUDITED_CONSUMED",
        "unexpected predecessor schema")
    prev_frontier = prev["current_exact_frontier"]
    req(prev_frontier["authoritative_remaining_strata"] == AUTH_STRATA,
        "predecessor strata drift")
    req(prev_frontier["authoritative_remaining_terminals"] == AUTH_TERMINALS,
        "predecessor terminals drift")
    req(prev["authority_sync"]["cut195_post_sync_reaudit_status"] == "PENDING",
        "predecessor did not require CUT195 replacement-head re-audit")
    req(prev_frontier["cut195_synchronized_head_hostile_audited"] is False,
        "predecessor self-awarded CUT195 replacement-head audit")

    receipt = load_locked(RECEIPT_PATH, EXPECTED_RECEIPT_BLOB, EXPECTED_RECEIPT_CANONICAL)
    req(receipt["status"] == "CONSUMED", "receipt not consumed")
    audit = receipt["external_audit"]
    req(audit["pr"] == 1788, "wrong audit PR")
    req(audit["audited_exact_head"] == AUDITED_V15_HEAD, "wrong audited V15 head")
    req(audit["review_id"] == AUDIT_REVIEW and audit["status"] == "PASS",
        "wrong V15 hostile re-audit identity/status")
    req(audit["merged_main_commit"] == MERGED_MAIN, "wrong merged-main identity")
    ci = audit["exact_head_ci"]
    req(ci == {
        "claim_frontier": 34685096528,
        "ex5_main_integrity": 34685096534,
        "main_startup": 34685096537,
        "stage36_authority": 34685096518,
        "stale_run_sweeper": 34685096570,
    }, "V15 exact-head CI identity drift")
    trans = receipt["authority_transition"]
    req(trans["mathematical_authority_changed"] is False,
        "audit consumption must not change numerical authority")
    req(trans["remaining_strata_before"] == trans["remaining_strata_after"] == AUTH_STRATA,
        "strata changed during audit consumption")
    req(trans["remaining_terminals_before"] == trans["remaining_terminals_after"] == AUTH_TERMINALS,
        "terminals changed during audit consumption")

    state = load_locked(STATE_PATH, EXPECTED_STATE_BLOB, EXPECTED_STATE_CANONICAL)
    req(state["schema"] == "STAGE32_MAIN_COMPACT_STATE_V16_CUT195_REAUDIT_CONSUMED",
        "unexpected V16 schema")
    req(state["authority_sync"]["current_repository_main"] == MERGED_MAIN,
        "V16 current-main source lock mismatch")
    req(state["authority_sync"]["cut195_post_sync_reaudit_status"] == "PASS",
        "CUT195 V15 replacement-head audit not consumed")
    req(state["authority_sync"]["cut195_post_sync_reaudit_review_id"] == AUDIT_REVIEW,
        "CUT195 V15 review mismatch")
    req(state["authority_sync"]["cut195_post_sync_reaudit_exact_head"] == AUDITED_V15_HEAD,
        "CUT195 V15 audited head mismatch")
    req(state["authority_sync"]["cut195_post_sync_reaudit_required"] is False,
        "CUT195 V15 audit still marked required")
    req(state["authority_sync"]["cut195_synchronized_head_hostile_audited"] is True,
        "CUT195 synchronized head not marked audited")
    frontier = state["current_exact_frontier"]
    req(frontier["authoritative_remaining_strata"] == AUTH_STRATA, "V16 strata drift")
    req(frontier["authoritative_remaining_terminals"] == AUTH_TERMINALS, "V16 terminals drift")
    req(frontier["cut195_main_pruning_credit"] is True, "CUT195 consumed credit lost")
    req(frontier["cut196_candidate_exact_head"] == CUT196_HEAD, "wrong CUT196 selected head")
    req(frontier["cut196_candidate_rejected_terminals"] == 27346, "wrong CUT196 candidate count")
    req(frontier["cut196_claim_frontier_ci_run"] == CUT196_CI, "wrong CUT196 CI run")
    req(frontier["cut196_claim_frontier_ci_status"] == "SUCCESS",
        "CUT196 exact-head CI must be successful before hostile audit")
    req(frontier["cut196_candidate_hostile_audited"] is False,
        "unaudited CUT196 candidate promoted")
    req(frontier["cut196_main_pruning_credit"] is False,
        "CUT196 MAIN pruning credit must remain false")
    req(frontier["full178_numerical_census_complete"] is False, "FULL178 falsely closed")
    req(frontier["stage32_closed"] is False, "Stage32 falsely closed")
    fw = state["firewalls"]
    for key in ("receiver_credit", "theorem_credit", "endpoint_credit",
                "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim",
                "merge_authorized"):
        req(fw[key] is False, f"firewall opened: {key}")

    print("PASS Stage32 MAIN V16 CUT195 re-audit consumption + CUT196 zero-credit frontier selection")


if __name__ == "__main__":
    main()
