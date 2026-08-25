#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
BASE_PATH = HERE.parent / "32-16" / "verify_predecessor_neighbor_regression.py"

spec = importlib.util.spec_from_file_location("stage32_16_regression_verifier", BASE_PATH)
base = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(base)

base.PLAN_SCHEMA = "STAGE32_D8_E20_A0_TIER114186_WORK_BALANCED_PLAN_V1"
base.OUT_SCHEMA = "STAGE32_17_PREDECESSOR_NEIGHBOR_EXACT_REGRESSION_V1"

if __name__ == "__main__":
    base.main()
