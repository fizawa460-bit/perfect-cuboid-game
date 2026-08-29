#!/usr/bin/env python3
from __future__ import annotations

import calibrate_generation14 as generation14

base = generation14.base
base.SCHEMA = "STAGE32_RESIDUAL32_01_RAW_ALL140_COST_AWARE_REMAINING_COMPLETION_SCOUT_V9"
base.REPRESENTATIVES = [
    {"m": 1, "genus": 0, "degree": 16, "exceptional_mass": 8},
    {"m": 4, "genus": 0, "degree": 12, "exceptional_mass": 8},
    {"m": 8, "genus": 0, "degree": 10, "exceptional_mass": 8},
]

if __name__ == "__main__":
    base.main()
