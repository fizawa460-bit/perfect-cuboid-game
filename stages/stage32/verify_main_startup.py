#!/usr/bin/env python3
from __future__ import annotations
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
AUTHORITY_VERIFIER = HERE / "verify_main_startup_authority_v32_td01_audit_synced.py"

def main() -> None:
    runpy.run_path(str(AUTHORITY_VERIFIER), run_name="__main__")
    runpy.run_path(str(HERE / "verify_command_surface.py"), run_name="__main__")
    print("PASS: Stage32 MAIN V32 synchronizes hostile-audited V31 TD01 authority; HPADJ11 is audited and queued for separate replacement")

if __name__ == "__main__":
    main()
