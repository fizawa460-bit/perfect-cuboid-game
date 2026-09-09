#!/usr/bin/env python3
"""Replay immutable EX5-00 against its exact pre-remap MAIN routing snapshot."""
from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MAIN = ROOT / "stages/stage32/MAIN-STATE.json"
SNAPSHOT = ROOT / "stages/stage32/proof/historical-routing-blobs/05e2942b4c893044688f16926b5e9837e59d8e9d.json"
ORIGINAL = ROOT / "stages/stage32-ex5/verify_ex5_00_source_lock.py"


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def main() -> None:
    old = SNAPSHOT.read_bytes()
    assert git_blob_sha1(old) == "05e2942b4c893044688f16926b5e9837e59d8e9d"
    live = MAIN.read_bytes()
    try:
        MAIN.write_bytes(old)
        subprocess.run([sys.executable, str(ORIGINAL)], cwd=ROOT, check=True)
    finally:
        MAIN.write_bytes(live)
    assert MAIN.read_bytes() == live
    print("PASS_EX5_00_HISTORICAL_MAIN_ROUTING_REPLAY_POST1728")


if __name__ == "__main__":
    main()
