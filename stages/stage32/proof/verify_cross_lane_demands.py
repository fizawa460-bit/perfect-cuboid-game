#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ARCH = HERE / "historical-routing-blobs"
ARCH_VERIFIER = ARCH / "VERIFY-CROSS-LANE-DEMANDS-V24-PRE-EX5-STARTUP-COLLAPSE.py"
TMP_VERIFIER = HERE / ".verify_cross_lane_demands_v24_pre_ex5_startup_collapse.py"
EX5_STATE = ROOT / "stages/stage32-ex5/CROSS-LANE-STATE.json"
ARCH_EX5_STATE = ROOT / "stages/stage32-ex5/archive/startup-surface-20260914/CROSS-LANE-STATE.json"

ARCH_VERIFIER_BLOB = "add0e8d511295c6aeca1364f3901cda930407307"
ARCH_EX5_STATE_BLOB = "99151c6b5402e2ed12dfe268bd497935d5be1b3c"


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def main() -> None:
    req(not EX5_STATE.exists(), "retired EX5 CROSS-LANE-STATE leaked into live root")
    req(ARCH_VERIFIER.is_file() and blob(ARCH_VERIFIER) == ARCH_VERIFIER_BLOB,
        "archived V24 cross-lane verifier drift")
    req(ARCH_EX5_STATE.is_file() and blob(ARCH_EX5_STATE) == ARCH_EX5_STATE_BLOB,
        "archived EX5 coordination snapshot drift")

    old_state = EX5_STATE.read_bytes() if EX5_STATE.exists() else None
    old_tmp = TMP_VERIFIER.read_bytes() if TMP_VERIFIER.exists() else None
    try:
        EX5_STATE.write_bytes(ARCH_EX5_STATE.read_bytes())
        TMP_VERIFIER.write_bytes(ARCH_VERIFIER.read_bytes())
        runpy.run_path(str(TMP_VERIFIER), run_name="__main__")
    finally:
        if old_state is None:
            if EX5_STATE.exists():
                EX5_STATE.unlink()
        else:
            EX5_STATE.write_bytes(old_state)
        if old_tmp is None:
            if TMP_VERIFIER.exists():
                TMP_VERIFIER.unlink()
        else:
            TMP_VERIFIER.write_bytes(old_tmp)

    req(not EX5_STATE.exists() if old_state is None else EX5_STATE.read_bytes() == old_state,
        "EX5 coordination snapshot leaked after historical replay")
    print("PASS: current cross-lane authority replayed with retired EX5 mirror supplied transiently only")


if __name__ == "__main__":
    main()
