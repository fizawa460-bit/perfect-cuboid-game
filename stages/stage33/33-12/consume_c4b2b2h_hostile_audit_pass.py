#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE33 = HERE.parent
STATE = STAGE33 / "MAIN-STATE.json"
SYNC = STAGE33 / "sync_main_state.py"
CERT = HERE / "e3-v91c1x-r5b3b3c4b2b2h-repaired-stage33-11g-exact-exit.json"
RECEIPT = HERE / "c4b2b2h-hostile-audit-pass-consumption.json"

OLD_STATE_SHA = "5cdffdf866d2933b41173bef9842da417e29064f1605925911099939e9992aa8"
CERT_SHA = "5c37431587bf30ccd11f3212db1ef6ecc2f4bd134b439303386fce1bc6089ae6"
AUTH = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
AUDITED_HEAD = "0e6af14e8b806eb857b8a8844f206a118008a15f"
AUDIT_REVIEW = 5152927668
AUDIT_AT = "2026-09-09T10:21:50Z"
AUDIT_MAIN = "e2da76d90a0994af5038023613c6c4084c4c507e"

OLD_CHECKPOINT = {
    "authority": "OPERATIONAL_ONLY_NOT_PROOF",
    "consumed_c4b2b2f_hostile_reaudit_exact_head": "29f3dab7936b79f3f761af004dbedb10797802f3",
    "consumed_c4b2b2f_hostile_reaudit_review": 5150755582,
    "consumed_c4b2b2g_hostile_audit_exact_head": "8edfc08159cca1b95815278317873488075657f1",
    "consumed_c4b2b2g_hostile_audit_review": 5151676010,
    "failure_category": "HOSTILE_AUDIT_REQUIRED_BEFORE_REPAIRED_STAGE33_11G_EXACT_EXIT_CLOSE_CREDIT",
    "frontier": "V91C1X_R5B3B3C4B2B2H_REPAIRED_STAGE33_11G_EXACT_EXIT",
    "frontier_certificate_sha256": CERT_SHA,
    "historical_stage33_11f_26_column_closure_reuse_allowed": False,
    "historical_stage33_11g_44_prime_exact_exit_reuse_allowed": False,
    "next_leaf": "V91C1X_R5B3B3C4B2B2H_REPAIRED_STAGE33_11G_EXACT_EXIT_HOSTILE_AUDIT",
    "pr": 1722,
    "repaired_stage33_11f_26_column_closure_audited": True,
    "repaired_stage33_11f_26_column_closure_materialized": True,
    "repaired_stage33_11f_exact_audited_connecting_columns": "26/26",
    "repaired_stage33_11g_exact_exit_audited": False,
    "repaired_stage33_11g_exact_exit_condition_satisfied": True,
    "repaired_stage33_11g_exact_exit_materialized": True,
    "stage33_11_closed_exact": False,
    "status": "V91C1X_C4B2B2H_REPAIRED_STAGE33_11G_EXACT_EXIT_MAIN_COMPLETE_PENDING_HOSTILE_AUDIT",
}

NEW_CHECKPOINT = {
    "authority": "OPERATIONAL_ONLY_NOT_PROOF",
    "consumed_c4b2b2f_hostile_reaudit_exact_head": "29f3dab7936b79f3f761af004dbedb10797802f3",
    "consumed_c4b2b2f_hostile_reaudit_review": 5150755582,
    "consumed_c4b2b2g_hostile_audit_exact_head": "8edfc08159cca1b95815278317873488075657f1",
    "consumed_c4b2b2g_hostile_audit_review": 5151676010,
    "consumed_c4b2b2h_hostile_audit_exact_head": AUDITED_HEAD,
    "consumed_c4b2b2h_hostile_audit_review": AUDIT_REVIEW,
    "failure_category": "STAGE33_12_SEPARATE_RELEASE_SUMMARY_DECISION_REQUIRED",
    "frontier": "V91C1X_R5B3B3C4B2B2H_REPAIRED_STAGE33_11G_EXACT_EXIT",
    "frontier_certificate_sha256": CERT_SHA,
    "historical_stage33_11f_26_column_closure_reuse_allowed": False,
    "historical_stage33_11g_44_prime_exact_exit_reuse_allowed": False,
    "next_leaf": "STAGE33_12_SEPARATE_RELEASE_SUMMARY_DECISION",
    "pr": 1722,
    "repaired_stage33_11f_26_column_closure_audited": True,
    "repaired_stage33_11f_26_column_closure_materialized": True,
    "repaired_stage33_11f_exact_audited_connecting_columns": "26/26",
    "repaired_stage33_11g_exact_exit_audited": True,
    "repaired_stage33_11g_exact_exit_condition_satisfied": True,
    "repaired_stage33_11g_exact_exit_materialized": True,
    "stage33_11_closed_exact": True,
    "status": "V91C1X_C4B2B2H_HOSTILE_AUDIT_PASS_CONSUMED_REPAIRED_STAGE33_11_EXACT_CLOSED_STAGE33_12_DECISION_PENDING",
}


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_locked(path: Path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    if csha(body) != claimed:
        raise SystemExit(f"canonical mismatch: {path}")
    return obj, claimed


def expected_state_sha(state: dict) -> str:
    body = dict(state)
    body.pop("canonical_sha256", None)
    return csha(body)


def sync_sha(text: str) -> str:
    m = re.search(r"^STATE_SHA='([0-9a-f]{64})'$", text, flags=re.M)
    if not m:
        raise SystemExit("sync_main_state STATE_SHA not found")
    return m.group(1)


def assert_inputs():
    cert, claimed = load_locked(CERT)
    if claimed != CERT_SHA:
        raise SystemExit("C4B2B2H certificate lock moved")
    if cert.get("candidate") != "V91C1X_R5B3B3C4B2B2H_REPAIRED_STAGE33_11G_EXACT_EXIT":
        raise SystemExit("C4B2B2H candidate identity moved")
    if cert.get("entry") != {"authority": AUTH, "stage33_progress": "6/11", "successor_pr": 1722}:
        raise SystemExit("C4B2B2H authority/progress/PR entry moved")
    inv = cert["inventory_boundary"]
    if inv["canonical_actual_height_one_prime_inventory"] != 47:
        raise SystemExit("repaired prime inventory moved")
    if inv["historical_44_slot_prime_inventory_reused_as_is"] or inv["historical_stage33_11g_44_prime_exact_exit_reused_as_is"]:
        raise SystemExit("historical 44-prime reuse firewall moved")
    ex = cert["exact_exit_reconstruction"]
    if ex["source_basis_columns_checked"] != "26/26" or ex["connecting_columns_exact_main"] != "26/26":
        raise SystemExit("C4B2B2H exact-exit columns incomplete")
    if ex["connecting_columns_exact_hostile_audited_upstream"] != "26/26" or ex["unresolved_connecting_columns"] != 0:
        raise SystemExit("C4B2B2H audited-upstream boundary moved")
    if not ex["stage33_11_exact_exit_condition_reconstructed"] or not ex["stage33_11_closed_exact_candidate"]:
        raise SystemExit("C4B2B2H exact-exit candidate incomplete")
    op = cert["operational_credit"]
    if op["hostile_audit_passed"] or op["repaired_stage33_11g_exact_exit_audited"] or op["stage33_11_closed_exact"]:
        raise SystemExit("pre-audit C4B2B2H self-promotion detected")
    replay = cert["independent_exit_replay"]
    if replay["E_L_splitting_used"] or replay["finite_v4_shortcut_used"] or replay["carrier_level_substitute_used"] or replay["historical_pseudo_prime_substitute_used"]:
        raise SystemExit("C4B2B2H exact semantics firewall moved")

    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
    expected = {
        "schema": "STAGE33_C4B2B2H_HOSTILE_AUDIT_PASS_CONSUMPTION_RECEIPT_V1",
        "pr": 1722,
        "audited_exact_head": AUDITED_HEAD,
        "hostile_audit_review_id": AUDIT_REVIEW,
        "hostile_audit_submitted_at": AUDIT_AT,
        "hostile_audit_verdict": "PASS",
        "current_main_at_audit": AUDIT_MAIN,
        "c4b2b2h_certificate_sha256": CERT_SHA,
        "repaired_actual_height_one_prime_count": 47,
        "repaired_main_connecting_columns": "26/26",
        "repaired_hostile_audited_connecting_columns": "26/26",
        "unresolved_connecting_columns": 0,
        "repaired_stage33_11g_exact_exit_condition_satisfied": True,
        "stage33_11_close_credit_granted": True,
    }
    for key, value in expected.items():
        if receipt.get(key) != value:
            raise SystemExit(f"receipt field moved: {key}")
    b = receipt["consumption_boundary"]
    required_true = [
        "mathematical_authority_unchanged",
        "stage33_progress_unchanged",
        "repaired_stage33_11g_exact_exit_audited",
        "stage33_11_closed_exact",
        "stage33_12_separate_decision_required",
    ]
    if not all(b.get(k) is True for k in required_true):
        raise SystemExit("receipt positive boundary moved")
    required_false = [
        "historical_44_slot_or_pseudo_prime_closure_reuse_allowed",
        "historical_44_prime_stage33_11g_exact_exit_reuse_allowed",
        "stage33_12_released",
        "theorem_credit",
        "receiver_credit",
        "endpoint_credit",
        "perfect_cuboid_credit",
        "merge_allowed",
    ]
    if any(b.get(k) is not False for k in required_false):
        raise SystemExit("receipt firewall moved")
    if b.get("next_action") != "STAGE33_12_SEPARATE_RELEASE_SUMMARY_DECISION":
        raise SystemExit("receipt next action moved")


def assert_top_level_firewalls(state: dict):
    fw = state["firewalls"]
    for key in ["stage33_12_closed_exact", "stage33_13_released", "theorem_credit", "receiver_credit", "endpoint_credit", "merge_allowed"]:
        if fw.get(key) is not False:
            raise SystemExit(f"downstream firewall moved: {key}")
    if fw.get("stage33_07_reclosed") is not False or fw.get("stage33_08_released") is not False:
        raise SystemExit("Stage33-07/08 firewall moved")


def check():
    assert_inputs()
    state, claimed = load_locked(STATE)
    if state["authority_sync"]["frontier_authority"] != AUTH or state["stage33_progress"] != "6/11":
        raise SystemExit("proof authority/progress moved")
    if state.get("work_checkpoint") != NEW_CHECKPOINT:
        raise SystemExit("C4B2B2H hostile-audit PASS not consumed in work_checkpoint")
    assert_top_level_firewalls(state)
    text = SYNC.read_text(encoding="utf-8")
    if sync_sha(text) != claimed:
        raise SystemExit("sync_main_state STATE_SHA not aligned")
    print(json.dumps({
        "status": "PASS",
        "main_state_sha": claimed,
        "audit_review": AUDIT_REVIEW,
        "audited_head": AUDITED_HEAD,
        "stage33_11_closed_exact": True,
        "next_leaf": NEW_CHECKPOINT["next_leaf"],
        "stage33_progress": "6/11",
    }, sort_keys=True))


def write():
    assert_inputs()
    state, claimed = load_locked(STATE)
    text = SYNC.read_text(encoding="utf-8")
    if state.get("work_checkpoint") == NEW_CHECKPOINT:
        if sync_sha(text) != claimed:
            raise SystemExit("already-consumed checkpoint has stale sync STATE_SHA")
        return
    if claimed != OLD_STATE_SHA or state.get("work_checkpoint") != OLD_CHECKPOINT:
        raise SystemExit("unexpected pre-consumption MAIN-STATE checkpoint")
    if sync_sha(text) != claimed:
        raise SystemExit("pre-consumption sync STATE_SHA mismatch")
    if state["authority_sync"]["frontier_authority"] != AUTH or state["stage33_progress"] != "6/11":
        raise SystemExit("proof authority/progress moved before consumption")
    assert_top_level_firewalls(state)

    proof_before = {k: v for k, v in state.items() if k not in {"canonical_sha256", "work_checkpoint"}}
    state["work_checkpoint"] = NEW_CHECKPOINT
    proof_after = {k: v for k, v in state.items() if k not in {"canonical_sha256", "work_checkpoint"}}
    if proof_before != proof_after:
        raise SystemExit("proof-relevant MAIN-STATE changed during C4B2B2H audit consumption")

    new_sha = expected_state_sha(state)
    state["canonical_sha256"] = new_sha
    STATE.write_text(json.dumps(state, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
    text2, n = re.subn(r"^STATE_SHA='[0-9a-f]{64}'$", f"STATE_SHA='{new_sha}'", text, count=1, flags=re.M)
    if n != 1:
        raise SystemExit("failed to patch sync_main_state STATE_SHA")
    SYNC.write_text(text2, encoding="utf-8")
    print(json.dumps({"status": "WROTE", "old_main_state_sha": claimed, "new_main_state_sha": new_sha}, sort_keys=True))


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true")
    g.add_argument("--write", action="store_true")
    args = ap.parse_args()
    if args.write:
        write()
    check()


if __name__ == "__main__":
    main()
