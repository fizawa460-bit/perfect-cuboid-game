#!/usr/bin/env python3
from __future__ import annotations

import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
VERIFIER = HERE / "management/grf04-quadratic-capacity/verify_grf04_v37_full178_integer_lattice_routing.py"


def main() -> None:
    runpy.run_path(str(VERIFIER), run_name="__main__")
    print("PASS: Stage32 MAIN V37 keeps numerical authority unchanged and records the V37-synced FULL178 handoff pending MAIN MIN-composition decision")


if __name__ == "__main__":
    main()
