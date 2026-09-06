#!/usr/bin/env python3
"""Replay persisted in-PR V48 Goal4K snapshot while V49 Goal4L is stacked provisionally."""
from __future__ import annotations
import json,runpy,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
SNAP=ROOT/'stages/stage35-ex/snapshots/MAIN-STATE-V48-cf6dc82649e3.json'
V49='STAGE35_EX_PESCH_E1_STATE_V49_GOAL4L_STAGE14_PYTHAGOREAN_ELLIPTIC_RANKJUMP_RECEIVER_PENDING_LATER_AUDIT'
V48='STAGE35_EX_PESCH_E1_STATE_V48_GOAL4K_RATIO_DISCRIMINANT_GENUS_ONE_QUOTIENT_PENDING_LATER_AUDIT'
SOURCE='cf6dc82649e347558ccf4413402c2000e2b436ac'
OLD={'base',*{str(i) for i in range(10,33)},'32p','33g1','33g2','33','34','35','35g4a','35g4b','35g4c','35g4d','35g4e','35g4f','35g4g','35g4h','35g4i','35g4j'}
ALLOWED=OLD|{'35g4k'}
if len(sys.argv)!=2 or sys.argv[1] not in ALLOWED: raise SystemExit('usage: verify_stage35_ex_v49_legacy_replay.py target')
target=sys.argv[1]
real=json.loads(STATE.read_text())
assert real['schema']==V49
assert real['history_snapshot']['commit_sha']==SOURCE
assert real['history_snapshot']['schema']==V48
assert real['history_snapshot']['hostile_audited'] is False
assert real['last_audited_authority']['pr']==1633
assert real['claims']['goal4l_executed'] is True
assert real['claims']['physical_endpoint_implies_positive_rank_specialization'] is True
assert real['claims']['E1_proved'] is False
snaptext=SNAP.read_text(); snap=json.loads(snaptext)
assert snap['schema']==V48
assert snap['claims']['goal4k_executed'] is True
assert snap['claims']['new_exact_genus_one_receiver_obtained'] is True
orig=Path.read_text; sr=STATE.resolve()
def patched(self:Path,*a,**k):
    if self.resolve()==sr:return snaptext
    return orig(self,*a,**k)
Path.read_text=patched
try:
    oldargv=sys.argv[:]
    try:
        if target in OLD:
            sys.argv=['verify_stage35_ex_v48_legacy_replay.py',target]
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_v48_legacy_replay.py'),run_name='__main__')
        else:
            sys.argv=['verify_stage35_ex_35_goal4k.py']
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_35_goal4k.py'),run_name='__main__')
    finally: sys.argv=oldargv
finally: Path.read_text=orig
print(f'PASS V49_PERSISTED_IN_PR_V48_REPLAY_{target}')
