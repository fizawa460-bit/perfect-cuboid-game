#!/usr/bin/env python3
"""Replay persisted V58 Goal4U state while V59 Goal4V is the live provisional state."""
from __future__ import annotations
import json,runpy,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
SNAP=ROOT/'stages/stage35-ex/snapshots/MAIN-STATE-V58-addbe2cd7f0d.json'
V59='STAGE35_EX_PESCH_E1_STATE_V59_GOAL4V_FULL_PICARD_GALOIS_MODULE_PENDING_LATER_AUDIT'
V58='STAGE35_EX_PESCH_E1_STATE_V58_GOAL4U_GEOMETRIC_PICARD_RANK64_PENDING_LATER_AUDIT'
SOURCE='addbe2cd7f0d16a1414319a5a2a8386a4d0d7720'
OLD={'base',*{str(i) for i in range(10,33)},'32p','33g1','33g2','33','34','35','35g4a','35g4b','35g4c','35g4d','35g4e','35g4f','35g4g','35g4h','35g4i','35g4j','35g4k','35g4l','35g4m','35g4n','35g4o','35g4p','35g4q','35g4r','35g4s','35g4t'}
ALLOWED=OLD|{'35g4u'}
if len(sys.argv)!=2 or sys.argv[1] not in ALLOWED:raise SystemExit('usage: verify_stage35_ex_v59_legacy_replay.py target')
target=sys.argv[1]
real=json.loads(STATE.read_text())
assert real['schema']==V59
assert real['history_snapshot']['commit_sha']==SOURCE
assert real['history_snapshot']['schema']==V58
assert real['history_snapshot']['hostile_audited'] is False
assert real['last_audited_authority']['pr']==1633
assert real['claims']['goal4v_executed'] is True
assert real['claims']['full_geometric_picard_group_computed'] is True
assert real['claims']['full_integral_marked_picard_isomorphism_for_stage35ex_computed'] is True
assert real['claims']['full_picard_galois_module_computed'] is True
assert real['claims']['full_Picard_H1_computed'] is False
assert real['claims']['E1_proved'] is False
snaptext=SNAP.read_text();snap=json.loads(snaptext)
assert snap['schema']==V58
assert snap['current']['unit']=='35EX-35_GOAL4U_COORDINATE_RAMIFICATION_DIVISOR_CLASS_RANK_AUGMENTATION_PREFLIGHT'
assert snap['claims']['goal4u_executed'] is True
assert snap['claims']['geometric_picard_rank_exact'] is True
assert snap['claims']['geometric_picard_rank']==64
assert snap['claims']['full_picard_galois_module_computed'] is False
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
            sys.argv=['verify_stage35_ex_v58_legacy_replay.py',target]
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_v58_legacy_replay.py'),run_name='__main__')
        else:
            sys.argv=['verify_stage35_ex_35_goal4u.py']
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_35_goal4u.py'),run_name='__main__')
    finally:sys.argv=oldargv
finally:Path.read_text=orig
print(f'PASS V59_PERSISTED_V58_REPLAY_{target}')
