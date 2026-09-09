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

OLD_STATE_SHA = "f4c442670386b7ac270e95dd36070415ae2b542df313769023e7d86c3534a7b4"
CERT_SHA = "e9b3bad7d1c74d40e0a4114659e4e2bb9c5866f1548a28204e3e2dd11ad2ed32"
AUTH = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
CONSTRUCTION_AUDIT_REVIEW = 5150130766
CONSTRUCTION_AUDITED_HEAD = "e4a861a13819e60e9e7d7eece8e5c1d90748b68d"
CURRENT_AUDIT_REVIEW = 5150755582
CURRENT_AUDITED_HEAD = "29f3dab7936b79f3f761af004dbedb10797802f3"

CHECKPOINT = {
    "authority": "OPERATIONAL_ONLY_NOT_PROOF",
    "status": "V91C1X_C4B2B2G_REPAIRED_STAGE33_11F_26_COLUMN_CLOSURE_MAIN_COMPLETE_PENDING_HOSTILE_AUDIT",
    "frontier_certificate_sha256": CERT_SHA,
    "frontier": "V91C1X_R5B3B3C4B2B2G_REPAIRED_STAGE33_11F_26_COLUMN_CLOSURE",
    "consumed_c4b2b2f_hostile_reaudit_review": CURRENT_AUDIT_REVIEW,
    "consumed_c4b2b2f_hostile_reaudit_exact_head": CURRENT_AUDITED_HEAD,
    "failure_category": "HOSTILE_AUDIT_REQUIRED_BEFORE_REPAIRED_STAGE33_11F_CLOSURE_CREDIT",
    "next_leaf": "V91C1X_R5_REPAIRED_STAGE33_11F_26_COLUMN_CLOSURE_HOSTILE_AUDIT",
    "historical_stage33_11f_26_column_closure_reuse_allowed": False,
    "repaired_stage33_11f_26_column_closure_materialized": True,
    "repaired_stage33_11f_26_column_closure_audited": False,
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


def assert_cert():
    cert, claimed = load_locked(CERT)
    if claimed != CERT_SHA:
        raise SystemExit("C4B2B2G certificate lock moved")
    if cert["entry"]["authority"] != AUTH or cert["entry"]["stage33_progress"] != "6/11":
        raise SystemExit("C4B2B2G authority/progress moved")
    locks = cert["source_locks"]
    if (
        locks["c4b2b2f_hostile_reaudit_review"] != CONSTRUCTION_AUDIT_REVIEW
        or locks["c4b2b2f_hostile_reaudit_exact_head"] != CONSTRUCTION_AUDITED_HEAD
    ):
        raise SystemExit("C4B2B2G construction provenance moved")
    summary = cert["summary"]
    if summary["repaired_exact_main_connecting_columns"] != "26/26":
        raise SystemExit("C4B2B2G repaired MAIN closure incomplete")
    if summary["repaired_exact_audited_connecting_columns"] != "0/26":
        raise SystemExit("C4B2B2G audit ceiling unexpectedly moved")
    if summary["unresolved_connecting_columns"] != 0 or summary["stage33_11_closed_exact"]:
        raise SystemExit("C4B2B2G closure/audit boundary moved")
    if summary["next_exact_leaf"] != CHECKPOINT["next_leaf"]:
        raise SystemExit("C4B2B2G next leaf moved")
    xc = cert["exact_consequence"]
    if not xc["repaired_stage33_11f_26_column_closure_reconstructed"] or not xc["prime_level_repair_propagated_to_all_26_columns"]:
        raise SystemExit("C4B2B2G exact consequence incomplete")
    if not xc["authority_unchanged"] or not xc["stage33_progress_unchanged"] or xc["stage33_11_closed_exact"]:
        raise SystemExit("C4B2B2G credit firewall moved")


def sync_sha(text: str) -> str:
    m = re.search(r"^STATE_SHA='([0-9a-f]{64})'$", text, flags=re.M)
    if not m:
        raise SystemExit("sync_main_state STATE_SHA not found")
    return m.group(1)


def check():
    assert_cert()
    state, claimed = load_locked(STATE)
    if state["authority_sync"]["frontier_authority"] != AUTH or state["stage33_progress"] != "6/11":
        raise SystemExit("proof authority/progress moved")
    if state.get("work_checkpoint") != CHECKPOINT:
        raise SystemExit("operational work_checkpoint not aligned to C4B2B2G hostile-audit stop")
    text = SYNC.read_text(encoding="utf-8")
    if sync_sha(text) != claimed:
        raise SystemExit("sync_main_state STATE_SHA not aligned to MAIN-STATE")
    print(json.dumps({"status": "PASS", "main_state_sha": claimed, "frontier_certificate_sha256": CERT_SHA}, sort_keys=True))


def write():
    assert_cert()
    state, claimed = load_locked(STATE)
    if claimed != OLD_STATE_SHA:
        raise SystemExit(f"unexpected MAIN-STATE starting lock: {claimed}")
    if state["authority_sync"]["frontier_authority"] != AUTH or state["stage33_progress"] != "6/11":
        raise SystemExit("proof authority/progress moved before alignment")

    proof_before = {k: v for k, v in state.items() if k not in {"canonical_sha256", "work_checkpoint"}}
    state["work_checkpoint"] = CHECKPOINT
    proof_after = {k: v for k, v in state.items() if k not in {"canonical_sha256", "work_checkpoint"}}
    if proof_before != proof_after:
        raise SystemExit("proof-relevant MAIN-STATE changed")

    new_sha = expected_state_sha(state)
    state["canonical_sha256"] = new_sha
    STATE.write_text(json.dumps(state, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")

    text = SYNC.read_text(encoding="utf-8")
    old_sync_sha = sync_sha(text)
    if old_sync_sha != claimed:
        raise SystemExit(f"sync_main_state old STATE_SHA mismatch: {old_sync_sha} != {claimed}")
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
