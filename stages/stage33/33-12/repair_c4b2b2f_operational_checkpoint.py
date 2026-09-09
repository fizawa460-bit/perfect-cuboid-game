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
CERT = HERE / "e3-v91c1x-r5b3b3c4b2b2f-stage33-11e-actual-direct-prime-transport-replay.json"

OLD_STATE_SHA = "3c53225c087415a62deae70eadcf2287252b41cb872022cc26360e9d194f4b1c"
CERT_SHA = "b4e384e4f88fcb690193c8cfef8dbabf995c400696fe2ba73679fbc657d98480"
AUTH = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"

CHECKPOINT = {
    "authority": "OPERATIONAL_ONLY_NOT_PROOF",
    "status": "V91C1X_C4B2B2F_STAGE33_11E_ACTUAL_DIRECT_PRIME_TRANSPORT_REPLAY_COMPLETE_PENDING_HOSTILE_REAUDIT",
    "frontier_certificate_sha256": CERT_SHA,
    "frontier": "V91C1X_R5B3B3C4B2B2F_STAGE33_11E_ACTUAL_DIRECT_PRIME_TRANSPORT_REPLAY",
    "failure_category": "HOSTILE_REAUDIT_REQUIRED_BEFORE_STAGE33_11F_REUSE",
    "next_leaf": "V91C1X_R5_DIRECT_SUPPORT_PRIME_REPAIR_HOSTILE_REAUDIT_AFTER_OPERATIONAL_ROUTING_FIX",
    "historical_stage33_11f_26_column_closure_reuse_allowed": False,
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
        raise SystemExit("C4B2B2F certificate lock moved")
    if cert["entry"]["authority"] != AUTH or cert["entry"]["stage33_progress"] != "6/11":
        raise SystemExit("C4B2B2F authority/progress moved")
    xc = cert["exact_consequence"]
    if not xc["historical_stage33_11e_prime_level_transport_replay_succeeded"]:
        raise SystemExit("C4B2B2F replay not complete")
    if not xc["fresh_hostile_audit_required_before_reusing_stage33_11f"]:
        raise SystemExit("C4B2B2F hostile-audit firewall moved")
    if cert["summary"]["historical_stage33_11f_26_column_closure_reuse_allowed"]:
        raise SystemExit("33-11f reuse unexpectedly unlocked")


def sync_sha(text: str) -> str:
    m = re.search(r"^STATE_SHA='([0-9a-f]{64})'$", text, flags=re.M)
    if not m:
        raise SystemExit("sync_main_state STATE_SHA not found")
    return m.group(1)


def check():
    assert_cert()
    state, claimed = load_locked(STATE)
    if state["authority_sync"]["frontier_authority"] != AUTH:
        raise SystemExit("proof authority moved")
    if state.get("work_checkpoint") != CHECKPOINT:
        raise SystemExit("operational work_checkpoint not aligned to C4B2B2F hostile re-audit stop")
    text = SYNC.read_text(encoding="utf-8")
    if sync_sha(text) != claimed:
        raise SystemExit("sync_main_state STATE_SHA not aligned to MAIN-STATE")
    print(json.dumps({"status": "PASS", "main_state_sha": claimed, "frontier_certificate_sha256": CERT_SHA}, sort_keys=True))


def write():
    assert_cert()
    state, claimed = load_locked(STATE)
    if claimed not in {OLD_STATE_SHA, expected_state_sha(state)}:
        raise SystemExit("unexpected MAIN-STATE starting lock")
    if state["authority_sync"]["frontier_authority"] != AUTH:
        raise SystemExit("proof authority moved before repair")

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
    a = ap.parse_args()
    if a.write:
        write()
    check()


if __name__ == "__main__":
    main()
