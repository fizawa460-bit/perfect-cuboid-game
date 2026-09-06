#!/usr/bin/env python3
"""Replay persisted V56 Goal4S state while V57 Goal4T is the live provisional state."""
from __future__ import annotations
import json,runpy,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
SNAP=ROOT/'stages/stage35-ex/snapshots/MAIN-STATE-V56-b9d997a7b1ed.json'
V57='STAGE35_EX_PESCH_E1_STATE_V57_GOAL4T_HODGE_CAP_RHO_53_TO_64_PENDING_LATER_AUDIT'
V56='STAGE35_EX_PESCH_E1_STATE_V56_GOAL4S_PURE_2PRIMARY_NUMERICAL_DISCRIMINANT_PENDING_LATER_AUDIT'
SOURCE='b9d997a7b1edf0cf56d95a77dcd733fe96bbce85'
OLD={'base',*{str(i) for i in range(10,33)},'32p','33g1','33g2','33','34','35','35g4a','35g4b','35g4c','35g4d','35g4e','35g4f','35g4g','35g4h','35g4i','35g4j','35g4k','35g4l','35g4m','35g4n','35g4o','35g4p','35g4q','35g4r'}
ALLOWED=OLD|{'35g4s'}
if len(sys.argv)!=2 or sys.argv[1] not in ALLOWED:raise SystemExit('usage: verify_stage35_ex_v57_legacy_replay.py target')
target=sys.argv[1]
real=json.loads(STATE.read_text())
assert real['schema']==V57
assert real['history_snapshot']['commit_sha']==SOURCE
assert real['history_snapshot']['schema']==V56
assert real['history_snapshot']['hostile_audited'] is False
assert real['last_audited_authority']['pr']==1633
assert real['claims']['goal4t_executed'] is True
assert real['claims']['missing_picard_rank_upper_bound_11_obtained'] is True
assert real['claims']['E1_proved'] is False
snaptext=SNAP.read_text();snap=json.loads(snaptext)
assert snap['schema']==V56
assert snap['current']['unit']=='35EX-35_GOAL4S_PICARD_OVERLATTICE_DISCRIMINANT_AND_2PRIMARY_SATURATION_PREFLIGHT'
assert snap['claims']['goal4s_executed'] is True
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
            sys.argv=['verify_stage35_ex_v56_legacy_replay.py',target]
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_v56_legacy_replay.py'),run_name='__main__')
        else:
            sys.argv=['verify_stage35_ex_35_goal4s.py']
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_35_goal4s.py'),run_name='__main__')
    finally:sys.argv=oldargv
finally:Path.read_text=orig
print(f'PASS V57_PERSISTED_V56_REPLAY_{target}')
