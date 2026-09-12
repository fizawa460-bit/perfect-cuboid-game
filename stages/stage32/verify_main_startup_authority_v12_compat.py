#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_main_startup_authority_v12.py"
EXPECTED_CANONICAL = "ee451b06cfe5052cbedde107f09e13cfc232647edf88de84cf02fb81c4ed94c6"


def main() -> None:
    spec = importlib.util.spec_from_file_location("stage32_main_v12_base", BASE)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.EXPECTED_CANONICAL = EXPECTED_CANONICAL
    mod.main()


if __name__ == "__main__":
    main()
