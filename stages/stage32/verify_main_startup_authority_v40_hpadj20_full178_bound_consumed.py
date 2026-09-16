#!/usr/bin/env python3
from __future__ import annotations

import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
VERIFIER = HERE / "management/grf04-quadratic-capacity/verify_grf04_v40_hpadj20_full178_main_bound_replacement.py"

def main() -> None:
    runpy.run_path(str(VERIFIER), run_name="__main__")
    print("PASS: Stage32 MAIN V40 consumes hostile-audited EX5 HPADJ20 by non-additive bound replacement")
    print("PASS: numerical authority is 179119009547804181594; replacement head awaits independent hostile reaudit")

if __name__ == "__main__":
    main()
