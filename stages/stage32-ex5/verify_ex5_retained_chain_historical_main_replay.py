#!/usr/bin/env python3
"""Replay the retained EX5 evidence chain against its pre-remap management snapshots.

All retained EX5 leaf verifiers remain byte-for-byte unchanged. This wrapper supplies
the exact historical mutable MAIN routing and active-frontier bytes while replaying
them, then restores the live post-#1728 management files before current checks run.
"""
from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MAIN = ROOT / "stages/stage32/MAIN-STATE.json"
ACTIVE = ROOT / "stages/stage32/proof/ACTIVE-FRONTIER.json"
MAIN_SNAPSHOT = ROOT / "stages/stage32/proof/historical-routing-blobs/05e2942b4c893044688f16926b5e9837e59d8e9d.json"
ACTIVE_SNAPSHOT = ROOT / "stages/stage32/proof/historical-management-blobs/93dee109899185602d9e8e4bb200f614a3b421e0.json"
EX5 = ROOT / "stages/stage32-ex5"
VERIFIERS = [
    "verify_ex5_00_source_lock.py",
    "verify_ex5_01_receiver_ledger.py",
    "verify_ex5_02_coverage_graph.py",
    "verify_ex5_03_clean_room_routes.py",
    "verify_ex5_04_asset_dedup.py",
    "verify_ex5_05_route_scorecard.py",
    "verify_ex5_06_executable_route_contracts.py",
    "verify_ex5_07_xstage_preflight_01.py",
    "verify_ex5_07_efc_preflight_01.py",
    "verify_ex5_07_ehs_preflight_01.py",
    "verify_ex5_10_bounded_breadth_exhaustion.py",
    "verify_ex5_11_terminal_route_decision.py",
]


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def main() -> None:
    old_main = MAIN_SNAPSHOT.read_bytes()
    old_active = ACTIVE_SNAPSHOT.read_bytes()
    assert git_blob_sha1(old_main) == "05e2942b4c893044688f16926b5e9837e59d8e9d"
    assert git_blob_sha1(old_active) == "93dee109899185602d9e8e4bb200f614a3b421e0"
    live_main = MAIN.read_bytes()
    live_active = ACTIVE.read_bytes()
    try:
        MAIN.write_bytes(old_main)
        ACTIVE.write_bytes(old_active)
        for name in VERIFIERS:
            subprocess.run([sys.executable, str(EX5 / name)], cwd=ROOT, check=True)
    finally:
        MAIN.write_bytes(live_main)
        ACTIVE.write_bytes(live_active)
    assert MAIN.read_bytes() == live_main
    assert ACTIVE.read_bytes() == live_active
    print("PASS_EX5_RETAINED_CHAIN_HISTORICAL_MANAGEMENT_REPLAY_POST1728")


if __name__ == "__main__":
    main()
