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
CERT = HERE / "e3-v91c1x-r5b3b3c4b2b2g-repaired-stage33-11f-26-column-closure.json"
RECEIPT = HERE / "c4b2b2g-hostile-audit-pass-consumption.json"

OLD_STATE_SHA = "5de9227fa4601bf3e64b86ddd416d907efadb194ad545a941bb8b5a0f6651933"
CERT_SHA = "e9b3bad7d1c74d40e0a4114659e4e2bb9c5866f1548a28204e3e2dd11ad2ed32"
SOURCE_LOCK_SHA = "3c493c5863a1506e48622ec9180119b6b80f5ee0642fe20515916749b3138957"
AUTH = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
AUDITED_HEAD = "8edfc08159cca1b95815278317873488075657f1"
AUDIT_REVIEW = 5151676010
AUDIT_AT = "2026-09-09T08:26:49Z"
AUDIT_MAIN = "e2da76d90a0994af5038023613c6c4084c4c507e"

OLD_CHECKPOINT = {
    "authority": "OPERATIONAL_ONLY_NOT_PROOF",
    "status": "V91C1X_C4B2B2G_REPAIRED_STAGE33_11F_26_COLUMN_CLOSURE_MAIN_COMPLETE_PENDING_HOSTILE_AUDIT",
    "frontier_certificate_sha256": CERT_SHA,
    "frontier": "V91C1X_R5B3B3C4B2B2G_REPAIRED_STAGE33_11F_26_COLUMN_CLOSURE",
    "consumed_c4b2b2f_hostile_reaudit_review": 5150755582,
    "consumed_c4b2b2f_hostile_reaudit_exact_head": "29f3dab7936b79f3f761af004dbedb10797802f3",
    "failure_category": "HOSTILE_AUDIT_REQUIRED_BEFORE_REPAIRED_STAGE33_11F_CLOSURE_CREDIT",
    "next_leaf": "V91C1X_R5_REPAIRED_STAGE33_11F_26_COLUMN_CLOSURE_HOSTILE_AUDIT",
    "historical_stage33_11f_26_column_closure_reuse_allowed": False,
    "repaired_stage33_11f_26_column_closure_materialized": True,
    "repaired_stage33_11f_26_column_closure_audited": False,
    "pr": 1722,
}

NEW_CHECKPOINT = {
    "authority": "OPERATIONAL_ONLY_NOT_PROOF",
    "status": "V91C1X_C4B2B2G_HOSTILE_AUDIT_PASS_CONSUMED_REPAIRED_STAGE33_11G_EXACT_EXIT_PENDING",
    "frontier_certificate_sha256": CERT_SHA,
    "frontier": "V91C1X_R5B3B3C4B2B2G_REPAIRED_STAGE33_11F_26_COLUMN_CLOSURE",
    "consumed_c4b2b2f_hostile_reaudit_review": 5150755582,
    "consumed_c4b2b2f_hostile_reaudit_exact_head": "29f3dab7936b79f3f761af004dbedb10797802f3",
    "consumed_c4b2b2g_hostile_audit_review": AUDIT_REVIEW,
    "consumed_c4b2b2g_hostile_audit_exact_head": AUDITED_HEAD,
    "repaired_stage33_11f_exact_audited_connecting_columns": "26/26",
    "failure_category": "REPAIRED_STAGE33_11G_EXACT_EXIT_NOT_YET_MATERIALIZED",
    "next_leaf": "RECONSTRUCT_STAGE33_11G_EXACT_EXIT_ON_REPAIRED_47_ACTUAL_PRIME_INVENTORY",
    "historical_stage33_11f_26_column_closure_reuse_allowed": False,
    "historical_stage33_11g_44_prime_exact_exit_reuse_allowed": False,
    "repaired_stage33_11f_26_column_closure_materialized": True,
    "repaired_stage33_11f_26_column_closure_audited": True,
    "stage33_11_closed_exact": False,
    "pr": 1722,
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
        raise SystemExit("C4B2B2G certificate lock moved")
    if cert["entry"]["authority"] != AUTH or cert["entry"]["stage33_progress"] != "6/11":
        raise SystemExit("C4B2B2G authority/progress moved")
    if cert["source_locks"]["stage33_11f_source_lock_sha256"] != SOURCE_LOCK_SHA:
        raise SystemExit("Stage33-11f source lock moved")
    summary = cert["summary"]
    if summary["repaired_exact_main_connecting_columns"] != "26/26" or summary["unresolved_connecting_columns"] != 0:
        raise SystemExit("C4B2B2G MAIN closure incomplete")
    if summary["repaired_exact_audited_connecting_columns"] != "0/26" or summary["stage33_11_closed_exact"]:
        raise SystemExit("recorded pre-audit C4B2B2G ceiling moved")

    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
    if receipt["schema"] != "STAGE33_C4B2B2G_HOSTILE_AUDIT_PASS_CONSUMPTION_RECEIPT_V1":
        raise SystemExit("receipt schema moved")
    expected = {
        "pr": 1722,
        "audited_exact_head": AUDITED_HEAD,
        "hostile_audit_review_id": AUDIT_REVIEW,
        "hostile_audit_submitted_at": AUDIT_AT,
        "hostile_audit_verdict": "PASS",
        "current_main_at_audit": AUDIT_MAIN,
        "c4b2b2g_certificate_sha256": CERT_SHA,
        "stage33_11f_source_lock_sha256": SOURCE_LOCK_SHA,
        "repaired_actual_height_one_prime_count": 47,
        "repaired_main_connecting_columns": "26/26",
        "repaired_hostile_audited_connecting_columns": "26/26",
        "unresolved_connecting_columns": 0,
    }
    for k, v in expected.items():
        if receipt[k] != v:
            raise SystemExit(f"receipt field moved: {k}")
    b = receipt["consumption_boundary"]
    if not b["mathematical_authority_unchanged"] or not b["stage33_progress_unchanged"]:
        raise SystemExit("receipt authority/progress boundary moved")
    if b["stage33_11_closed_exact"] or b["historical_44_slot_or_pseudo_prime_closure_reuse_allowed"] or b["historical_44_prime_stage33_11g_exact_exit_reuse_allowed"]:
        raise SystemExit("receipt closure/reuse firewall moved")


def check():
    assert_inputs()
    state, claimed = load_locked(STATE)
    if state["authority_sync"]["frontier_authority"] != AUTH or state["stage33_progress"] != "6/11":
        raise SystemExit("proof authority/progress moved")
    if state.get("work_checkpoint") != NEW_CHECKPOINT:
        raise SystemExit("C4B2B2G hostile-audit PASS not consumed in work_checkpoint")
    text = SYNC.read_text(encoding="utf-8")
    if sync_sha(text) != claimed:
        raise SystemExit("sync_main_state STATE_SHA not aligned")
    if state["firewalls"]["stage33_12_closed_exact"] or state["firewalls"]["stage33_13_released"] or state["firewalls"]["theorem_credit"] or state["firewalls"]["endpoint_credit"] or state["firewalls"]["merge_allowed"]:
        raise SystemExit("downstream firewall moved")
    print(json.dumps({"status":"PASS","main_state_sha":claimed,"audit_review":AUDIT_REVIEW,"audited_head":AUDITED_HEAD,"next_leaf":NEW_CHECKPOINT["next_leaf"],"stage33_progress":"6/11"}, sort_keys=True))


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

    proof_before = {k: v for k, v in state.items() if k not in {"canonical_sha256", "work_checkpoint"}}
    state["work_checkpoint"] = NEW_CHECKPOINT
    proof_after = {k: v for k, v in state.items() if k not in {"canonical_sha256", "work_checkpoint"}}
    if proof_before != proof_after:
        raise SystemExit("proof-relevant MAIN-STATE changed during audit consumption")

    new_sha = expected_state_sha(state)
    state["canonical_sha256"] = new_sha
    STATE.write_text(json.dumps(state, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
    text2, n = re.subn(r"^STATE_SHA='[0-9a-f]{64}'$", f"STATE_SHA='{new_sha}'", text, count=1, flags=re.M)
    if n != 1:
        raise SystemExit("failed to patch sync_main_state STATE_SHA")
    SYNC.write_text(text2, encoding="utf-8")
    print(json.dumps({"status":"WROTE","old_main_state_sha":claimed,"new_main_state_sha":new_sha}, sort_keys=True))


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
