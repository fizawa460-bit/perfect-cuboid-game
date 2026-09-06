#!/usr/bin/env python3
"""Replay persisted V57 Goal4T state while V58 Goal4U is the live provisional state."""
from __future__ import annotations
import json,runpy,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
SNAP=ROOT/'stages/stage35-ex/snapshots/MAIN-STATE-V57-0fb2d756eb85.json'
V58='STAGE35_EX_PESCH_E1_STATE_V58_GOAL4U_GEOMETRIC_PICARD_RANK64_PENDING_LATER_AUDIT'
V57='STAGE35_EX_PESCH_E1_STATE_V57_GOAL4T_HODGE_CAP_RHO_53_TO_64_PENDING_LATER_AUDIT'
SOURCE='0fb2d756eb8532020c35c94e050b7154bd8ca483'
OLD={'base',*{str(i) for i in range(10,33)},'32p','33g1','33g2','33','34','35','35g4a','35g4b','35g4c','35g4d','35g4e','35g4f','35g4g','35g4h','35g4i','35g4j','35g4k','35g4l','35g4m','35g4n','35g4o','35g4p','35g4q','35g4r','35g4s'}
ALLOWED=OLD|{'35g4t'}
if len(sys.argv)!=2 or sys.argv[1] not in ALLOWED:raise SystemExit('usage: verify_stage35_ex_v58_legacy_replay.py target')
target=sys.argv[1]
real=json.loads(STATE.read_text())
assert real['schema']==V58
assert real['history_snapshot']['commit_sha']==SOURCE
assert real['history_snapshot']['schema']==V57
assert real['history_snapshot']['hostile_audited'] is False
assert real['last_audited_authority']['pr']==1633
assert real['claims']['goal4u_executed'] is True
assert real['claims']['geometric_picard_rank_exact'] is True
assert real['claims']['geometric_picard_rank']==64
assert real['claims']['E1_proved'] is False
snaptext=SNAP.read_text();snap=json.loads(snaptext)
assert snap['schema']==V57
assert snap['current']['unit']=='35EX-35_GOAL4T_FULL_PICARD_RANK_GAP_AND_HODGE_CAP_PREFLIGHT'
assert snap['claims']['goal4t_executed'] is True
assert snap['claims']['geometric_picard_rank_upper_bound_64_obtained'] is True
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
            sys.argv=['verify_stage35_ex_v57_legacy_replay.py',target]
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_v57_legacy_replay.py'),run_name='__main__')
        else:
            sys.argv=['verify_stage35_ex_35_goal4t.py']
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_35_goal4t.py'),run_name='__main__')
    finally:sys.argv=oldargv
finally:Path.read_text=orig
print(f'PASS V58_PERSISTED_V57_REPLAY_{target}')
