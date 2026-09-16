#!/usr/bin/env python3
from __future__ import annotations

import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
VERIFIER = HERE / "management/grf04-quadratic-capacity/verify_grf04_v36_q_quadratic_audit_sync.py"


def main() -> None:
    runpy.run_path(str(VERIFIER), run_name="__main__")
    print("PASS: Stage32 MAIN V36 process-sync retains V35 q-quadratic numerical authority and resumes FULL178")


if __name__ == "__main__":
    main()
