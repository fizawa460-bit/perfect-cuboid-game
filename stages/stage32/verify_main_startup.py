#!/usr/bin/env python3
from __future__ import annotations
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent

def main() -> None:
    runpy.run_path(str(HERE/"verify_main_startup_authority_v37_full178_integer_lattice_routed.py"), run_name="__main__")
    runpy.run_path(str(HERE/"verify_command_surface.py"), run_name="__main__")
    print("PASS: Stage32 MAIN V37 routing active; numerical authority unchanged while 178 owns FULL178 integer-lattice scaleout")

if __name__=="__main__":
    main()
