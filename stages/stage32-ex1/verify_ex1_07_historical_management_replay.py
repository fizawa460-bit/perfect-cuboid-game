#!/usr/bin/env python3
"""Replay immutable audited EX1-07 against its exact pre-remap management snapshots.

The audited EX1-07 verifier is intentionally unchanged. Post-#1728 MAIN routing moved,
so this wrapper temporarily supplies the exact hash-locked MAIN-STATE and active-frontier
bytes that the immutable verifier audited, then restores the live post-remap files.
"""
from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MAIN = ROOT / "stages/stage32/MAIN-STATE.json"
FRONTIER = ROOT / "stages/stage32/proof/ACTIVE-FRONTIER.json"
MAIN_SNAPSHOT = ROOT / "stages/stage32/proof/historical-routing-blobs/05e2942b4c893044688f16926b5e9837e59d8e9d.json"
FRONTIER_SNAPSHOT = ROOT / "stages/stage32/proof/historical-management-blobs/93dee109899185602d9e8e4bb200f614a3b421e0.json"
ORIGINAL = ROOT / "stages/stage32-ex1/verify_ex1_07_current_main_v6_carrier_promotion_adapter.py"


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def main() -> None:
    main_old = MAIN_SNAPSHOT.read_bytes()
    frontier_old = FRONTIER_SNAPSHOT.read_bytes()
    assert git_blob_sha1(main_old) == "05e2942b4c893044688f16926b5e9837e59d8e9d"
    assert git_blob_sha1(frontier_old) == "93dee109899185602d9e8e4bb200f614a3b421e0"

    main_live = MAIN.read_bytes()
    frontier_live = FRONTIER.read_bytes()
    try:
        MAIN.write_bytes(main_old)
        FRONTIER.write_bytes(frontier_old)
        subprocess.run([sys.executable, str(ORIGINAL)], cwd=ROOT, check=True)
    finally:
        MAIN.write_bytes(main_live)
        FRONTIER.write_bytes(frontier_live)

    assert MAIN.read_bytes() == main_live
    assert FRONTIER.read_bytes() == frontier_live
    print("PASS_EX1_07_HISTORICAL_MANAGEMENT_REPLAY_POST1728")


if __name__ == "__main__":
    main()
