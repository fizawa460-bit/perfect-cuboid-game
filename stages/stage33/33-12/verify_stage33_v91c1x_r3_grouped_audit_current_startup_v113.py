#!/usr/bin/env python3
"""Historical V113 entrypoint retained for workflow compatibility.

R1-R3 grouped audit is already PASS/merged.  Current startup authority is V53/R4,
so every live caller of this historical filename delegates to V114 and may not
recreate the old pending-audit state.
"""
from __future__ import annotations
import subprocess, sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
subprocess.run([sys.executable,str(HERE/'verify_stage33_v91c1x_r4_negative_checkpoint_v114.py')],check=True)
print('V113_COMPAT_DELEGATES_TO_V114_R4_CURRENT_STARTUP')
