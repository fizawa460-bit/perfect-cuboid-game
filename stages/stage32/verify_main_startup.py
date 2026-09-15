#!/usr/bin/env python3
from __future__ import annotations
import runpy
from pathlib import Path
HERE=Path(__file__).resolve().parent
def main():
    runpy.run_path(str(HERE/"verify_main_startup_authority_v35_grf04_candidate.py"),run_name="__main__")
    runpy.run_path(str(HERE/"verify_command_surface.py"),run_name="__main__")
    print("PASS: Stage32 MAIN V35 retains independent GRF04 canonical-capacity LP candidate; V34 authority remains active pending hostile audit")
if __name__=="__main__": main()
