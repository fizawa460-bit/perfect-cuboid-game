#!/usr/bin/env python3
"""Align Stage33 MAIN operational checkpoint to the repaired Stage33-11g exact-exit candidate."""
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

OLD_STATE_SHA = "91c8c9380cd8de2da5f9e510b6e23ff6bf3b25cafc3f26ef4551563e72fcec9e"
AUTH = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
G_AUDIT_REVIEW = 5151676010
G_AUDITED_HEAD = "8edfc08159cca1b95815278317873488075657f1"
CANDIDATE = "V91C1X_R5B3B3C4B2B2H_REPAIRED_STAGE33_11G_EXACT_EXIT"
NEXT = "V91C1X_R5B3B3C4B2B2H_REPAIRED_STAGE33_11G_EXACT_EXIT_HOSTILE_AUDIT"


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_locked(path: Path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    if csha(body) != claimed:
        raise SystemExit(f"canonical mismatch: {path}")
    return obj, claimed


def sync_sha(text: str) -> str:
    m = re.search(r"^STATE_SHA='([0-9a-f]{64})'$", text, flags=re.M)
    if not m:
        raise SystemExit("sync_main_state STATE_SHA not found")
    return m.group(1)


def checkpoint_for(cert_sha: str):
    return {
        "authority": "OPERATIONAL_ONLY_NOT_PROOF",
        "status": "V91C1X_C4B2B2H_REPAIRED_STAGE33_11G_EXACT_EXIT_MAIN_COMPLETE_PENDING_HOSTILE_AUDIT",
        "frontier": CANDIDATE,
        "frontier_certificate_sha256": cert_sha,
        "consumed_c4b2b2f_hostile_reaudit_review": 5150755582,
        "consumed_c4b2b2f_hostile_reaudit_exact_head": "29f3dab7936b79f3f761af004dbedb10797802f3",
        "consumed_c4b2b2g_hostile_audit_review": G_AUDIT_REVIEW,
        "consumed_c4b2b2g_hostile_audit_exact_head": G_AUDITED_HEAD,
        "historical_stage33_11f_26_column_closure_reuse_allowed": False,
        "historical_stage33_11g_44_prime_exact_exit_reuse_allowed": False,
        "repaired_stage33_11f_26_column_closure_materialized": True,
        "repaired_stage33_11f_26_column_closure_audited": True,
        "repaired_stage33_11f_exact_audited_connecting_columns": "26/26",
        "repaired_stage33_11g_exact_exit_materialized": True,
        "repaired_stage33_11g_exact_exit_audited": False,
        "repaired_stage33_11g_exact_exit_condition_satisfied": True,
        "stage33_11_closed_exact": False,
        "failure_category": "HOSTILE_AUDIT_REQUIRED_BEFORE_REPAIRED_STAGE33_11G_EXACT_EXIT_CLOSE_CREDIT",
        "next_leaf": NEXT,
        "pr": 1722,
    }


def assert_cert():
    cert, claimed = load_locked(CERT)
    if cert.get("candidate") != CANDIDATE:
        raise SystemExit("C4B2B2H candidate identity moved")
    if cert.get("entry") != {"authority": AUTH, "stage33_progress": "6/11", "successor_pr": 1722}:
        raise SystemExit("C4B2B2H authority/progress/PR entry moved")
    ex = cert["exact_exit_reconstruction"]
    if ex["source_dimension_f2"] != 26 or ex["source_basis_columns_checked"] != "26/26":
        raise SystemExit("C4B2B2H source basis coverage moved")
    if ex["connecting_columns_exact_main"] != "26/26":
        raise SystemExit("C4B2B2H exact MAIN column coverage moved")
    if ex["connecting_columns_exact_hostile_audited_upstream"] != "26/26":
        raise SystemExit("C4B2B2H audited upstream coverage moved")
    if ex["unresolved_connecting_columns"] != 0:
        raise SystemExit("C4B2B2H unresolved columns remain")
    if ex["stage33_11_exact_exit_condition_reconstructed"] is not True:
        raise SystemExit("C4B2B2H exact-exit condition not reconstructed")
    if ex["stage33_11_closed_exact_candidate"] is not True:
        raise SystemExit("C4B2B2H exact-exit candidate flag moved")
    op = cert["operational_credit"]
    if op["hostile_audit_passed"] is not False or op["hostile_audit_required"] is not True:
        raise SystemExit("C4B2B2H hostile-audit boundary moved")
    if op["stage33_11_closed_exact"] is not False or op["repaired_stage33_11g_exact_exit_audited"] is not False:
        raise SystemExit("C4B2B2H operational close/audit ceiling moved")
    if op["next_exact_leaf"] != NEXT:
        raise SystemExit("C4B2B2H next leaf moved")
    if cert["credit_firewall"]["stage33_11_close_credit"] is not False:
        raise SystemExit("C4B2B2H close credit firewall moved")
    if cert["credit_firewall"]["merge_allowed"] is not False:
        raise SystemExit("C4B2B2H merge firewall moved")
    return cert, claimed


def assert_proof_authority(state: dict):
    if state.get("stage33_progress") != "6/11":
        raise SystemExit("Stage33 progress moved")
    if state.get("authority_sync", {}).get("frontier_authority") != AUTH:
        raise SystemExit("Stage33 mathematical authority moved")


def check():
    cert, cert_sha = assert_cert()
    state, claimed = load_locked(STATE)
    assert_proof_authority(state)
    expected = checkpoint_for(cert_sha)
    if state.get("work_checkpoint") != expected:
        raise SystemExit("operational work_checkpoint not aligned to C4B2B2H hostile-audit stop")
    text = SYNC.read_text(encoding="utf-8")
    if sync_sha(text) != claimed:
        raise SystemExit("sync_main_state STATE_SHA not aligned to MAIN-STATE")
    print(json.dumps({
        "status": "PASS",
        "main_state_sha": claimed,
        "frontier": CANDIDATE,
        "frontier_certificate_sha256": cert_sha,
        "stage33_11_closed_exact": False,
    }, sort_keys=True))


def write():
    cert, cert_sha = assert_cert()
    state, claimed = load_locked(STATE)
    assert_proof_authority(state)
    text = SYNC.read_text(encoding="utf-8")
    expected = checkpoint_for(cert_sha)

    if state.get("work_checkpoint") == expected:
        if sync_sha(text) != claimed:
            raise SystemExit("already-aligned checkpoint has stale sync_main_state STATE_SHA")
        print(json.dumps({"status": "NOOP_ALREADY_ALIGNED", "main_state_sha": claimed}, sort_keys=True))
        return

    if claimed != OLD_STATE_SHA:
        raise SystemExit(f"unexpected MAIN-STATE starting lock: {claimed}")
    wc = state.get("work_checkpoint", {})
    prior_required = {
        "authority": "OPERATIONAL_ONLY_NOT_PROOF",
        "status": "V91C1X_C4B2B2G_HOSTILE_AUDIT_PASS_CONSUMED_REPAIRED_STAGE33_11G_EXACT_EXIT_PENDING",
        "frontier": "V91C1X_R5B3B3C4B2B2G_REPAIRED_STAGE33_11F_26_COLUMN_CLOSURE",
        "frontier_certificate_sha256": "e9b3bad7d1c74d40e0a4114659e4e2bb9c5866f1548a28204e3e2dd11ad2ed32",
        "consumed_c4b2b2g_hostile_audit_review": G_AUDIT_REVIEW,
        "consumed_c4b2b2g_hostile_audit_exact_head": G_AUDITED_HEAD,
        "repaired_stage33_11f_26_column_closure_materialized": True,
        "repaired_stage33_11f_26_column_closure_audited": True,
        "repaired_stage33_11f_exact_audited_connecting_columns": "26/26",
        "historical_stage33_11f_26_column_closure_reuse_allowed": False,
        "historical_stage33_11g_44_prime_exact_exit_reuse_allowed": False,
        "stage33_11_closed_exact": False,
        "next_leaf": "RECONSTRUCT_STAGE33_11G_EXACT_EXIT_ON_REPAIRED_47_ACTUAL_PRIME_INVENTORY",
        "pr": 1722,
    }
    for key, value in prior_required.items():
        if wc.get(key) != value:
            raise SystemExit(f"unexpected pre-C4B2B2H work checkpoint: {key}")

    if sync_sha(text) != claimed:
        raise SystemExit("pre-alignment sync_main_state STATE_SHA mismatch")

    proof_before = {k: v for k, v in state.items() if k not in {"canonical_sha256", "work_checkpoint"}}
    state["work_checkpoint"] = expected
    proof_after = {k: v for k, v in state.items() if k not in {"canonical_sha256", "work_checkpoint"}}
    if proof_before != proof_after:
        raise SystemExit("proof-relevant MAIN-STATE changed")

    body = dict(state)
    body.pop("canonical_sha256", None)
    new_sha = csha(body)
    state["canonical_sha256"] = new_sha
    STATE.write_text(json.dumps(state, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")

    text2, n = re.subn(r"^STATE_SHA='[0-9a-f]{64}'$", f"STATE_SHA='{new_sha}'", text, count=1, flags=re.M)
    if n != 1:
        raise SystemExit("failed to patch sync_main_state STATE_SHA")
    SYNC.write_text(text2, encoding="utf-8")
    print(json.dumps({
        "status": "WROTE",
        "old_main_state_sha": claimed,
        "new_main_state_sha": new_sha,
        "frontier_certificate_sha256": cert_sha,
    }, sort_keys=True))


def main():
    ap = argparse.ArgumentParser()
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true")
    group.add_argument("--write", action="store_true")
    args = ap.parse_args()
    if args.write:
        write()
    check()


if __name__ == "__main__":
    main()
