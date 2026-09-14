#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE = HERE.parent
STATE = STAGE / "MAIN-STATE.json"
HISTORICAL_STATE = HERE / "historical-routing-blobs" / "bead809db3a008dd35d664a8923f06fecb7de5bb.json"
HISTORICAL_VERIFIER = HERE / "verify_cross_lane_demands_v23_historical.py"

CURRENT_STATE_BLOB = "b8df16056625db5fbb1947f1e927593de258f1ff"
CURRENT_STATE_CANON = "bdaab3df8871e656652e5c1f78f972405081a45b8d5e421cc4a9bacddef3bf5d"
HISTORICAL_STATE_BLOB = "bead809db3a008dd35d664a8923f06fecb7de5bb"
HISTORICAL_VERIFIER_BLOB = "56f66941608e6883e3110ca370cda5dac043e968"
CURRENT_AUTH = 26876434389242951089388
HPADJ_CREDIT = 20713268924714183560113
HPADJ_SOURCE_REVIEW = 5191822227
V24_AUDIT_REVIEW = 5191916561
V24_AUDITED_HEAD = "3c5915dee248660a2821f2ebe9c24e20b0ad1647"

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)

def blob(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def canon(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()

def main() -> None:
    req(blob(STATE) == CURRENT_STATE_BLOB, "current V24 synced MAIN-STATE blob drift")
    state = json.loads(STATE.read_text(encoding="utf-8"))
    req(state.get("canonical_sha256_without_this_field") == CURRENT_STATE_CANON, "current V24 synced MAIN-STATE stored canonical drift")
    req(canon(state) == CURRENT_STATE_CANON, "current V24 synced MAIN-STATE canonical drift")
    f = state["current_exact_frontier"]
    req(f["authoritative_remaining_terminals"] == CURRENT_AUTH, "current V24 terminal authority drift")
    req(f["authoritative_remaining_terminals_semantics"] == "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET", "V24 authority semantics drift")
    req(f["hpadj07_main_pruning_credit"] is True, "HPADJ07 MAIN credit not consumed")
    req(f["hpadj07_certified_rejected_terminals_lower_bound"] == HPADJ_CREDIT, "HPADJ07 consumed lower bound drift")
    req(f["hpadj07_hostile_audit_review_id"] == HPADJ_SOURCE_REVIEW, "HPADJ07 source audit review drift")
    req(f["hpadj07_v24_hostile_audited"] is True, "V24 audit PASS not synchronized")
    req(f["hpadj07_v24_hostile_audit_review_id"] == V24_AUDIT_REVIEW, "V24 audit review drift")
    req(f["hpadj07_v24_audited_exact_head"] == V24_AUDITED_HEAD, "V24 audited head drift")
    req(f["hpadj07_double_charge"] is False, "HPADJ07 double charge")
    req(f["full178_numerical_census_complete"] is False and f["stage32_closed"] is False, "closure overclaim")
    req(state["current"]["mainbatch_stop_gate"] == "NONE", "stale MAIN stop gate")
    req(state["firewalls"]["replacement_head_hostile_reaudit_required"] is False, "stale replacement-head audit firewall")
    req(state["firewalls"]["merge_authorized"] is False, "merge firewall")

    req(HISTORICAL_STATE.is_file() and blob(HISTORICAL_STATE) == HISTORICAL_STATE_BLOB, "historical V23 state snapshot drift")
    req(HISTORICAL_VERIFIER.is_file() and blob(HISTORICAL_VERIFIER) == HISTORICAL_VERIFIER_BLOB, "historical cross-lane verifier drift")

    current_bytes = STATE.read_bytes()
    try:
        STATE.write_bytes(HISTORICAL_STATE.read_bytes())
        runpy.run_path(str(HISTORICAL_VERIFIER), run_name="__main__")
    finally:
        STATE.write_bytes(current_bytes)

    req(blob(STATE) == CURRENT_STATE_BLOB, "current V24 synced MAIN-STATE restore failed")
    print("PASS: Stage32 cross-lane demand DAG retained across HPADJ07 V24 audit synchronization")
    print("HPADJ07=MAIN_LOWER_BOUND_CREDIT_CONSUMED_AND_AUDITED; FULL178 remains active incomplete")

if __name__ == "__main__":
    main()
