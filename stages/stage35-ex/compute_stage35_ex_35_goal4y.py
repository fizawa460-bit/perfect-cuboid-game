#!/usr/bin/env python3
"""Compute Goal4Y against the persisted V61 Goal4X state while V62 is live."""
from __future__ import annotations
import runpy
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
SNAP=ROOT/'stages/stage35-ex/snapshots/MAIN-STATE-V61-0a8af929e004.json'
CORE=ROOT/'stages/stage35-ex/probe_goal4y_two_class_lift.py'
snaptext=SNAP.read_text()
orig=Path.read_text
sr=STATE.resolve()
def patched(self:Path,*a,**k):
    if self.resolve()==sr:
        return snaptext
    return orig(self,*a,**k)
Path.read_text=patched
try:
    ns=runpy.run_path(str(CORE))
finally:
    Path.read_text=orig
out=ns['out']
assert out['success'] is True
