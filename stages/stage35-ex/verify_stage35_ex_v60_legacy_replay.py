#!/usr/bin/env python3
"""Replay persisted V59 Goal4V state while V60 Goal4W is the live provisional state."""
from __future__ import annotations
import json,runpy,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
SNAP=ROOT/'stages/stage35-ex/snapshots/MAIN-STATE-V59-67db3d433102.json'
V60='STAGE35_EX_PESCH_E1_STATE_V60_GOAL4W_FULL_PICARD_H1_ZERO_ALGEBRAIC_BRAUER_CONSTANT_ONLY_PENDING_LATER_AUDIT'
V59='STAGE35_EX_PESCH_E1_STATE_V59_GOAL4V_FULL_PICARD_GALOIS_MODULE_PENDING_LATER_AUDIT'
SOURCE='67db3d433102bf00ca686427a29e5c835cf997ac'
OLD={'base',*{str(i) for i in range(10,33)},'32p','33g1','33g2','33','34','35','35g4a','35g4b','35g4c','35g4d','35g4e','35g4f','35g4g','35g4h','35g4i','35g4j','35g4k','35g4l','35g4m','35g4n','35g4o','35g4p','35g4q','35g4r','35g4s','35g4t','35g4u'}
ALLOWED=OLD|{'35g4v'}
if len(sys.argv)!=2 or sys.argv[1] not in ALLOWED:raise SystemExit('usage: verify_stage35_ex_v60_legacy_replay.py target')
target=sys.argv[1]
real=json.loads(STATE.read_text())
assert real['schema']==V60
assert real['history_snapshot']['commit_sha']==SOURCE
assert real['history_snapshot']['schema']==V59
assert real['history_snapshot']['hostile_audited'] is False
assert real['last_audited_authority']['pr']==1633
assert real['claims']['goal4w_executed'] is True
assert real['claims']['full_picard_galois_module_computed'] is True
assert real['claims']['full_Picard_H1_computed'] is True
assert real['claims']['full_Picard_H1_trivial'] is True
assert real['claims']['algebraic_brauer_group_computed'] is True
assert real['claims']['algebraic_brauer_quotient_trivial'] is True
assert real['claims']['E1_proved'] is False
snaptext=SNAP.read_text();snap=json.loads(snaptext)
assert snap['schema']==V59
assert snap['current']['unit']=='35EX-35_GOAL4V_FULL_PICARD_GALOIS_MODULE_MARKED_BASIS_ADAPTER_PREFLIGHT'
assert snap['claims']['goal4v_executed'] is True
assert snap['claims']['full_picard_galois_module_computed'] is True
assert snap['claims']['full_Picard_H1_computed'] is False
assert snap['claims']['E1_proved'] is False
orig=Path.read_text;sr=STATE.resolve()
def patched(self:Path,*a,**k):
    if self.resolve()==sr:return snaptext
    return orig(self,*a,**k)
Path.read_text=patched
try:
    oldargv=sys.argv[:]
    try:
        if target in OLD:
            sys.argv=['verify_stage35_ex_v59_legacy_replay.py',target]
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_v59_legacy_replay.py'),run_name='__main__')
        else:
            sys.argv=['verify_stage35_ex_35_goal4v.py']
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_35_goal4v.py'),run_name='__main__')
    finally:sys.argv=oldargv
finally:Path.read_text=orig
print(f'PASS V60_PERSISTED_V59_REPLAY_{target}')
