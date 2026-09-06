#!/usr/bin/env python3
"""Replay persisted in-PR V54 Goal4Q snapshot while V55 Goal4R is stacked provisionally."""
from __future__ import annotations
import json,runpy,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
SNAP=ROOT/'stages/stage35-ex/snapshots/MAIN-STATE-V54-86e6e7f0de0f.json'
V55='STAGE35_EX_PESCH_E1_STATE_V55_GOAL4R_VISIBLE_NUMERICAL_C2_H1_ZERO_PENDING_LATER_AUDIT'
V54='STAGE35_EX_PESCH_E1_STATE_V54_GOAL4Q_48NODE_PICARD_SUBLATTICE_PENDING_LATER_AUDIT'
SOURCE='86e6e7f0de0fd4441f7695b899115055b97e49e5'
OLD={'base',*{str(i) for i in range(10,33)},'32p','33g1','33g2','33','34','35','35g4a','35g4b','35g4c','35g4d','35g4e','35g4f','35g4g','35g4h','35g4i','35g4j','35g4k','35g4l','35g4m','35g4n','35g4o','35g4p'}
ALLOWED=OLD|{'35g4q'}
if len(sys.argv)!=2 or sys.argv[1] not in ALLOWED:raise SystemExit('usage: verify_stage35_ex_v55_legacy_replay.py target')
target=sys.argv[1]
real=json.loads(STATE.read_text())
assert real['schema']==V55
assert real['history_snapshot']['commit_sha']==SOURCE
assert real['history_snapshot']['schema']==V54
assert real['history_snapshot']['hostile_audited'] is False
assert real['last_audited_authority']['pr']==1633
assert real['claims']['goal4r_executed'] is True
assert real['claims']['E1_proved'] is False
snaptext=SNAP.read_text();snap=json.loads(snaptext)
assert snap['schema']==V54
assert snap['current']['unit']=='35EX-35_GOAL4Q_COMPACTIFICATION_PICARD_GALOIS_BRAUER_CANDIDATE_PREFLIGHT'
assert snap['claims']['goal4q_executed'] is True
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
            sys.argv=['verify_stage35_ex_v54_legacy_replay.py',target]
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_v54_legacy_replay.py'),run_name='__main__')
        else:
            sys.argv=['verify_stage35_ex_35_goal4q.py']
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_35_goal4q.py'),run_name='__main__')
    finally:sys.argv=oldargv
finally:Path.read_text=orig
print(f'PASS V55_PERSISTED_IN_PR_V54_REPLAY_{target}')
