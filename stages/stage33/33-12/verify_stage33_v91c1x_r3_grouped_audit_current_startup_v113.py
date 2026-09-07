#!/usr/bin/env python3
"""Historical V113 entrypoint retained for workflow compatibility.

R1-R3 grouped audit is already PASS/merged and R4 hostile audit is PASS/merged.
Current startup authority is V54/R5-active, so every live caller of this
historical filename delegates to V115 and may not recreate an old audit stop.
"""
from __future__ import annotations
import subprocess, sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
subprocess.run([sys.executable,str(HERE/'verify_stage33_v91c1x_r5_active_v115.py')],check=True)
print('V113_COMPAT_DELEGATES_TO_V115_R5_CURRENT_STARTUP')
