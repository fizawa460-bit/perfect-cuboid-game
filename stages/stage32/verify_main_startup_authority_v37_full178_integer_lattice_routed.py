#!/usr/bin/env python3
from __future__ import annotations

import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
VERIFIER = HERE / "management/grf04-quadratic-capacity/verify_grf04_v37_full178_integer_lattice_routing.py"


def main() -> None:
    runpy.run_path(str(VERIFIER), run_name="__main__")
    print("PASS: Stage32 MAIN V37 keeps V35 q-quadratic authority unchanged and routes FULL178 integer-lattice scaleout to 32-01-178")


if __name__ == "__main__":
    main()
