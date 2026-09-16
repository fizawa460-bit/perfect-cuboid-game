#!/usr/bin/env python3
from __future__ import annotations
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent

def main() -> None:
    runpy.run_path(str(HERE/"verify_main_startup_authority_v35_q_quadratic_consumed.py"), run_name="__main__")
    runpy.run_path(str(HERE/"verify_command_surface.py"), run_name="__main__")
    print("PASS: Stage32 MAIN V35 q-quadratic numerical authority active; replacement-head hostile reaudit required before further promotion")

if __name__=="__main__":
    main()
