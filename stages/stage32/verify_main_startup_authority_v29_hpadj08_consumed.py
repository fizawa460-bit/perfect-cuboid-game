#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
V29 = HERE / "management/hpadj08-main-disposition/verify_hpadj08_v29_main_bound_replacement.py"
CROSS = HERE / "proof/verify_cross_lane_demands.py"

STATE_BLOB = "bd663e70864d7279063fa4eea9745fdfa479346d"
STATE_CANON = "3cbaa6e0b6b54cd379ba8770cc8e45c56c8444c13814f325fb9737222e306ecc"
V29_BLOB = "c56fbdab6a90bd2b2603e365c261e19bc52c40e1"
CROSS_BLOB = "a09e213bad7f86a3dcd14c0794616a4805271eaa"

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
    req(blob(V29) == V29_BLOB, "V29 verifier drift")
    req(blob(CROSS) == CROSS_BLOB, "cross-lane verifier drift")
    raw = STATE.read_bytes()
    req(blob(STATE) == STATE_BLOB, "MAIN state blob drift")
    state = json.loads(raw.decode("utf-8"))
    req(state.get("canonical_sha256_without_this_field") == STATE_CANON, "MAIN state stored canonical drift")
    req(canon(state) == STATE_CANON, "MAIN state canonical drift")
    runpy.run_path(str(V29), run_name="__main__")
    runpy.run_path(str(CROSS), run_name="__main__")
    req(state["current"]["mainbatch_stop_gate"] == "REPLACEMENT_HEAD_HOSTILE_REAUDIT_REQUIRED", "MAIN stop gate")
    req(state["current_exact_frontier"]["authoritative_remaining_terminals"] == 6703403803993210101494, "MAIN authority")
    print("PASS: Stage32 MAIN V29 HPADJ08 certified-bound replacement authority")
    print("FULL178=ACTIVE_INCOMPLETE stop_gate=REPLACEMENT_HEAD_HOSTILE_REAUDIT_REQUIRED heavy_compute_authorized=false merge_authorized=false")

if __name__ == "__main__":
    main()
