#!/usr/bin/env python3
from __future__ import annotations

import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
AUTHORITY_VERIFIER = HERE / "verify_main_startup_authority_v25_h8c03a_consumed.py"

def main() -> None:
    runpy.run_path(str(AUTHORITY_VERIFIER), run_name="__main__")
    runpy.run_path(str(HERE / "verify_command_surface.py"), run_name="__main__")
    print("PASS: Stage32 MAIN startup V25 H8C-03A consumed replacement-head re-audit boundary")

if __name__ == "__main__":
    main()
