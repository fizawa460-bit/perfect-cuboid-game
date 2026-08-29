#!/usr/bin/env python3
from __future__ import annotations

import calibrate_representatives as base

base.SCHEMA = "STAGE32_RESIDUAL32_01_RAW_ALL140_COST_AWARE_CALIBRATION_V7"
base.KNOWN_LABEL_ORDER = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
base.EXPECTED_ACTIVE_ROWS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
base.EXPECTED_MODULI = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
base.EXPECTED_PREFIX_ACTIONS = [1, 2, 2, 2, 2, 1, 1, 1, 1, 2, 1]

if __name__ == "__main__":
    base.main()
