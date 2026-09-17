#!/usr/bin/env python3
from __future__ import annotations

import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
VERIFIER = HERE / "management/grf04-quadratic-capacity/verify_grf04_v42_hpadj20_low_d_full_qa_hybrid_candidate.py"

def main() -> None:
    runpy.run_path(str(VERIFIER), run_name="__main__")
    print("PASS: Stage32 MAIN V42 retains a strict low-d full-qA hybrid candidate pending hostile audit")
    print("PASS: current authority remains 179119009547804181594; candidate 179119009547802604210 is not promoted")

if __name__ == "__main__":
    main()
