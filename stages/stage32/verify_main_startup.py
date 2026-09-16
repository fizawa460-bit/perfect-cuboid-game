#!/usr/bin/env python3
from __future__ import annotations
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent

def main() -> None:
    runpy.run_path(str(HERE/"verify_main_startup_authority_v36_q_quadratic_audit_synced.py"), run_name="__main__")
    runpy.run_path(str(HERE/"verify_command_surface.py"), run_name="__main__")
    print("PASS: Stage32 MAIN V36 audit-sync active; V35 q-quadratic numerical authority retained and FULL178 reentry resumed")

if __name__=="__main__":
    main()
