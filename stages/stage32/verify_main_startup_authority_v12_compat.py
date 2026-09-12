#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_main_startup_authority_v12.py"
EXPECTED_CANONICAL = "ff887d58b3869ec682966a8364c26c7fb3f8d913ef7b1493d6ee050f80fc5380"
EXPECTED_CLAIM_WORKFLOW_BLOB = "e496d4d01e9a9441d4059a69ffb935e75c7e9757"


def main() -> None:
    spec = importlib.util.spec_from_file_location("stage32_main_v12_base", BASE)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.EXPECTED_CANONICAL = EXPECTED_CANONICAL
    mod.EXPECTED_CLAIM_WORKFLOW_BLOB = EXPECTED_CLAIM_WORKFLOW_BLOB
    mod.main()


if __name__ == "__main__":
    main()
