#!/usr/bin/env python3
"""Replay persisted in-PR V55 Goal4R snapshot while V56 Goal4S is stacked provisionally."""
from __future__ import annotations
import json,runpy,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
SNAP=ROOT/'stages/stage35-ex/snapshots/MAIN-STATE-V55-296b98d9361f.json'
V56='STAGE35_EX_PESCH_E1_STATE_V56_GOAL4S_PURE_2PRIMARY_OVERLATTICE_GATE_PENDING_LATER_AUDIT'
V55='STAGE35_EX_PESCH_E1_STATE_V55_GOAL4R_VISIBLE_NUMERICAL_C2_H1_ZERO_PENDING_LATER_AUDIT'
SOURCE='296b98d9361fd0f06f05ef9464ff00a65b328d01'
OLD={'base',*{str(i) for i in range(10,33)},'32p','33g1','33g2','33','34','35','35g4a','35g4b','35g4c','35g4d','35g4e','35g4f','35g4g','35g4h','35g4i','35g4j','35g4k','35g4l','35g4m','35g4n','35g4o','35g4p','35g4q'}
ALLOWED=OLD|{'35g4r'}
if len(sys.argv)!=2 or sys.argv[1] not in ALLOWED:raise SystemExit('usage: verify_stage35_ex_v56_legacy_replay.py target')
target=sys.argv[1]
real=json.loads(STATE.read_text())
assert real['schema']==V56
assert real['history_snapshot']['commit_sha']==SOURCE
assert real['history_snapshot']['schema']==V55
assert real['history_snapshot']['hostile_audited'] is False
assert real['last_audited_authority']['pr']==1633
assert real['claims']['goal4s_executed'] is True
assert real['claims']['E1_proved'] is False
snaptext=SNAP.read_text();snap=json.loads(snaptext)
assert snap['schema']==V55
assert snap['current']['unit']=='35EX-35_GOAL4R_VISIBLE_DIVISOR_LATTICE_SATURATION_AND_C2_COHOMOLOGY_PREFLIGHT'
assert snap['claims']['goal4r_executed'] is True
orig=Path.read_text;sr=STATE.resolve()
def patched(self:Path,*a,**k):
    if self.resolve()==sr:return snaptext
    return orig(self,*a,**k)
Path.read_text=patched
try:
    oldargv=sys.argv[:]
    try:
        if target in OLD:
            sys.argv=['verify_stage35_ex_v55_legacy_replay.py',target]
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_v55_legacy_replay.py'),run_name='__main__')
        else:
            sys.argv=['verify_stage35_ex_35_goal4r.py']
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_35_goal4r.py'),run_name='__main__')
    finally:sys.argv=oldargv
finally:Path.read_text=orig
print(f'PASS V56_PERSISTED_IN_PR_V55_REPLAY_{target}')
