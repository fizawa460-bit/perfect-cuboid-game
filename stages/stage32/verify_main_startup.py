#!/usr/bin/env python3
from __future__ import annotations

import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
AUTHORITY_VERIFIER = HERE / "verify_main_startup_authority_v11.py"
COMMAND_SURFACE_VERIFIER = HERE / "verify_command_surface.py"


def main() -> None:
    runpy.run_path(str(AUTHORITY_VERIFIER), run_name="__main__")
    runpy.run_path(str(COMMAND_SURFACE_VERIFIER), run_name="__main__")


if __name__ == "__main__":
    main()
