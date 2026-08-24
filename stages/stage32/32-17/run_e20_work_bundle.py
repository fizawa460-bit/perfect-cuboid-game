#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
BASE_PATH = HERE.parent / "32-16" / "run_e20_work_bundle.py"

spec = importlib.util.spec_from_file_location("stage32_16_exact_bundle_runner", BASE_PATH)
base = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(base)

# Stage32-17 changes only the deterministic plan envelope. The source-locked
# exact solver, raw evidence construction, post-verification compaction,
# UNKNOWN semantics, and per-branch node limit are the audited Stage32-16 code.
base.PLAN_SCHEMA = "STAGE32_D8_E20_A0_TIER114186_WORK_BALANCED_PLAN_V1"

if __name__ == "__main__":
    base.main()
