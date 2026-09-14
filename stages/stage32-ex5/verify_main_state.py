#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
ARCH = HERE / "archive" / "startup-surface-20260914"
ARCH_VERIFIER = ARCH / "verify_main_state_v5_pre_startup_collapse.py"
TMP_VERIFIER = HERE / ".verify_main_state_v5_pre_startup_collapse.py"

ARCH_VERIFIER_BLOB = "fa20238eb372100520a2ca76523ca63d3b3f9c5f"
RESTORE = {
    "README.md": "62ec5465089fffe316c64a179162bdd337ae8305",
    "MAIN-START-HERE.md": "47581a734da21dac3d2cabc4dc520d5be1310a49",
    "CURRENT-ROADMAP.md": "b733127cc0c17d45ad9f03525d04fecf46b29bbb",
    "CURRENT-AUDIT-CONTRACT.md": "ea133bb1a43bb417f049afe7d28eafcee702e0c4",
}
RETIRED = (
    "README.md",
    "MAIN-START-HERE.md",
    "MAINBATCH-OPERATIONS.md",
    "CROSS-LANE-STATE.json",
    "CURRENT-ROADMAP.md",
    "CURRENT-AUDIT-CONTRACT.md",
    "AUDIT-CONTRACT.md",
)


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def main() -> None:
    req(all(not (HERE / name).exists() for name in RETIRED),
        "retired EX5 startup surface leaked into live root before V5 replay")
    req(ARCH_VERIFIER.is_file() and blob(ARCH_VERIFIER) == ARCH_VERIFIER_BLOB,
        "archived V5 verifier drift")
    for name, expected in RESTORE.items():
        p = ARCH / name
        req(p.is_file() and blob(p) == expected, f"archived V5 startup input drift: {name}")

    old_tmp = TMP_VERIFIER.read_bytes() if TMP_VERIFIER.exists() else None
    old_live = {name: (HERE / name).read_bytes() if (HERE / name).exists() else None for name in RESTORE}
    try:
        for name in RESTORE:
            (HERE / name).write_bytes((ARCH / name).read_bytes())
        TMP_VERIFIER.write_bytes(ARCH_VERIFIER.read_bytes())
        runpy.run_path(str(TMP_VERIFIER), run_name="__main__")
    finally:
        for name, raw in old_live.items():
            p = HERE / name
            if raw is None:
                if p.exists():
                    p.unlink()
            else:
                p.write_bytes(raw)
        if old_tmp is None:
            if TMP_VERIFIER.exists():
                TMP_VERIFIER.unlink()
        else:
            TMP_VERIFIER.write_bytes(old_tmp)

    req(all(not (HERE / name).exists() for name in RETIRED),
        "retired EX5 startup surface leaked after V5 compatibility replay")
    print("PASS: retained EX5 V5 mathematical state replayed against archived startup projection only")
    print("live_startup=LANE-ADAPTERS -> stages/stage32-ex5/MAIN-STATE.json")


if __name__ == "__main__":
    main()
