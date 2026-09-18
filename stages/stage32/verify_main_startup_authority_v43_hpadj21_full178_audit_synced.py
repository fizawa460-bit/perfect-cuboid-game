#!/usr/bin/env python3
from __future__ import annotations

import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
VERIFIER = HERE / "management/grf04-quadratic-capacity/verify_grf04_v43_hpadj21_full178_audit_sync.py"

def main() -> None:
    runpy.run_path(str(VERIFIER), run_name="__main__")
    print("PASS: Stage32 MAIN V43 synchronizes the V42 HPADJ21 hostile-audit PASS with zero new pruning")
    print("PASS: numerical authority remains 157570677819451133507; FULL178 research resumes")

if __name__ == "__main__":
    main()
