#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_main_startup_authority_v12.py"
EXPECTED_CANONICAL = "f173f8ac64259ac45a369bf4744720bed5f4283399f6030413f68c51e4899309"


def main() -> None:
    spec = importlib.util.spec_from_file_location("stage32_main_v12_base", BASE)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.EXPECTED_CANONICAL = EXPECTED_CANONICAL
    mod.main()


if __name__ == "__main__":
    main()
