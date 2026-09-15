#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
SYNC = HERE / "management/hpadj08-main-disposition/verify_hpadj08_v30_audit_sync.py"
CROSS = HERE / "proof/verify_cross_lane_demands.py"
RECEIPT = HERE / "management/hpadj08-main-disposition/HPADJ08-V30-HOSTILE-AUDIT-PASS-SYNC.json"

STATE_BLOB = "76bf5e3d9d97297ff5fbee2bf4826a78d125e171"
STATE_CANON = "bfa2441840bcf60ca70ef6cb288f8721310cdcc78e9f0724a197d35e60e79b21"
SYNC_BLOB = "07839c5809bd3d43f409df396484a10870718af1"
CROSS_BLOB = "59a4ff83deac96d59b9633230e2ad4a24d2c089f"
RECEIPT_BLOB = "45f636707149b05cbf18dd209194de515ee729f8"
RECEIPT_CANON = "c57e3614ef0111ba35490f48ea707cd7c47d34865e6b85fa336462794867a773"

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)

def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canon(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()

def main() -> None:
    req(blob(SYNC) == SYNC_BLOB, "V30 audit-sync verifier drift")
    req(blob(CROSS) == CROSS_BLOB, "cross-lane verifier drift")
    req(blob(RECEIPT) == RECEIPT_BLOB, "V30 audit-sync receipt blob drift")
    rec = json.loads(RECEIPT.read_text(encoding="utf-8"))
    req(rec.get("canonical_sha256_without_this_field") == RECEIPT_CANON, "V30 receipt stored canonical")
    req(canon(rec) == RECEIPT_CANON, "V30 receipt canonical")
    raw = STATE.read_bytes()
    req(blob(STATE) == STATE_BLOB, "MAIN state blob drift")
    state = json.loads(raw.decode("utf-8"))
    req(state.get("canonical_sha256_without_this_field") == STATE_CANON, "MAIN state stored canonical drift")
    req(canon(state) == STATE_CANON, "MAIN state canonical drift")
    runpy.run_path(str(SYNC), run_name="__main__")
    runpy.run_path(str(CROSS), run_name="__main__")
    req(state["current"]["mainbatch_stop_gate"] == "NONE", "MAIN stop gate")
    req(state["current_exact_frontier"]["authoritative_remaining_terminals"] == 6703403803993210101494, "MAIN authority")
    req(state["firewalls"]["replacement_head_hostile_reaudit_required"] is False, "audit freeze")
    print("PASS: Stage32 MAIN V30 HPADJ08 audit-synced certified-bound authority")
    print("FULL178=ACTIVE_INCOMPLETE stop_gate=NONE heavy_compute_authorized=false merge_authorized=false")

if __name__ == "__main__":
    main()
