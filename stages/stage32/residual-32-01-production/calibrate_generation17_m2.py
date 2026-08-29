#!/usr/bin/env python3
from __future__ import annotations

import calibrate_generation14 as generation14

base = generation14.base
base.SCHEMA = "STAGE32_RESIDUAL32_01_RAW_ALL140_COST_AWARE_M2_COMPLETION_SCOUT_V8"
base.REPRESENTATIVES = [
    {"m": 2, "genus": 0, "degree": 8, "exceptional_mass": 8},
]

if __name__ == "__main__":
    base.main()
