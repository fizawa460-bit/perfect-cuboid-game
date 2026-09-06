#!/usr/bin/env python3
"""Replay persisted in-PR V49 Goal4L snapshot while V50 Goal4M is stacked provisionally."""
from __future__ import annotations
import json,runpy,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
SNAP=ROOT/'stages/stage35-ex/snapshots/MAIN-STATE-V49-7abf0a1bcf03.json'
V50='STAGE35_EX_PESCH_E1_STATE_V50_GOAL4M_STAGE14_GLOBAL_TRIPLE_SQRT_TRANSFER_PENDING_LATER_AUDIT'
V49='STAGE35_EX_PESCH_E1_STATE_V49_GOAL4L_STAGE14_PYTHAGOREAN_ELLIPTIC_RANKJUMP_RECEIVER_PENDING_LATER_AUDIT'
SOURCE='7abf0a1bcf03a4ea033bf89e753b71471d1532dd'
OLD={'base',*{str(i) for i in range(10,33)},'32p','33g1','33g2','33','34','35','35g4a','35g4b','35g4c','35g4d','35g4e','35g4f','35g4g','35g4h','35g4i','35g4j','35g4k'}
ALLOWED=OLD|{'35g4l'}
if len(sys.argv)!=2 or sys.argv[1] not in ALLOWED: raise SystemExit('usage: verify_stage35_ex_v50_legacy_replay.py target')
target=sys.argv[1]
real=json.loads(STATE.read_text())
assert real['schema']==V50
assert real['history_snapshot']['commit_sha']==SOURCE
assert real['history_snapshot']['schema']==V49
assert real['history_snapshot']['hostile_audited'] is False
assert real['last_audited_authority']['pr']==1633
assert real['claims']['goal4m_executed'] is True
assert real['claims']['E1_proved'] is False
snaptext=SNAP.read_text(); snap=json.loads(snaptext)
assert snap['schema']==V49
assert snap['current']['unit']=='35EX-35_GOAL4L_S31W01_ELLIPTIC_ADAPTER_AND_MOVING_FAMILY_TEST'
assert snap['claims']['goal4l_executed'] is True
assert snap['claims']['physical_endpoint_implies_positive_rank_specialization'] is True
assert snap['claims']['E1_proved'] is False
orig=Path.read_text; sr=STATE.resolve()
def patched(self:Path,*a,**k):
    if self.resolve()==sr:return snaptext
    return orig(self,*a,**k)
Path.read_text=patched
try:
    oldargv=sys.argv[:]
    try:
        if target in OLD:
            sys.argv=['verify_stage35_ex_v49_legacy_replay.py',target]
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_v49_legacy_replay.py'),run_name='__main__')
        else:
            sys.argv=['verify_stage35_ex_35_goal4l.py']
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_35_goal4l.py'),run_name='__main__')
    finally: sys.argv=oldargv
finally: Path.read_text=orig
print(f'PASS V50_PERSISTED_IN_PR_V49_REPLAY_{target}')
