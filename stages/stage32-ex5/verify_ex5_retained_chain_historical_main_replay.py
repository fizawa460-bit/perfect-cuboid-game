#!/usr/bin/env python3
"""Replay the retained EX5 evidence chain against its pre-remap MAIN routing snapshot.

All retained EX5 leaf verifiers remain byte-for-byte unchanged. This wrapper only
supplies the exact historical mutable MAIN routing state while replaying them, then
restores the live post-#1728 MAIN state before current routing/claim checks run.
"""
from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MAIN = ROOT / "stages/stage32/MAIN-STATE.json"
SNAPSHOT = ROOT / "stages/stage32/proof/historical-routing-blobs/05e2942b4c893044688f16926b5e9837e59d8e9d.json"
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
    old = SNAPSHOT.read_bytes()
    assert git_blob_sha1(old) == "05e2942b4c893044688f16926b5e9837e59d8e9d"
    live = MAIN.read_bytes()
    try:
        MAIN.write_bytes(old)
        for name in VERIFIERS:
            subprocess.run([sys.executable, str(EX5 / name)], cwd=ROOT, check=True)
    finally:
        MAIN.write_bytes(live)
    assert MAIN.read_bytes() == live
    print("PASS_EX5_RETAINED_CHAIN_HISTORICAL_MAIN_REPLAY_POST1728")


if __name__ == "__main__":
    main()
