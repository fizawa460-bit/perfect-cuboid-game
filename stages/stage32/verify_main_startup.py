#!/usr/bin/env python3
from __future__ import annotations
import runpy
from pathlib import Path
HERE=Path(__file__).resolve().parent
def main():
    runpy.run_path(str(HERE/"verify_main_startup_authority_v34_hpadj11_audit_synced.py"),run_name="__main__")
    runpy.run_path(str(HERE/"verify_command_surface.py"),run_name="__main__")
    print("PASS: Stage32 MAIN V34 synchronizes hostile-audited V33 HPADJ11 authority; FULL178 remains active/incomplete")
if __name__=="__main__": main()
