#!/usr/bin/env python3
"""Replay persisted V60 Goal4W history while V61 Goal4X is live."""
from __future__ import annotations
import json,runpy,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
SNAP=ROOT/'stages/stage35-ex/snapshots/MAIN-STATE-V60-87a1c4e6268f.json'
V61='STAGE35_EX_PESCH_E1_STATE_V61_GOAL4X_OPEN_PICARD_H1_Z2_SQUARED_PENDING_BRAUER_LIFT_AND_AUDIT'
V60='STAGE35_EX_PESCH_E1_STATE_V60_GOAL4W_PROPER_SURFACE_H1_ZERO_OPEN_RECEIVER_BRAUER_UNTESTED_PENDING_LATER_AUDIT'
SOURCE='87a1c4e6268f76c642964dbcb5d0cd4be4e7c425'
OLD={'base',*{str(i) for i in range(10,33)},'32p','33g1','33g2','33','34','35','35g4a','35g4b','35g4c','35g4d','35g4e','35g4f','35g4g','35g4h','35g4i','35g4j','35g4k','35g4l','35g4m','35g4n','35g4o','35g4p','35g4q','35g4r','35g4s','35g4t','35g4u','35g4v'}
ALLOWED=OLD|{'35g4w'}
if len(sys.argv)!=2 or sys.argv[1] not in ALLOWED:raise SystemExit('usage: verify_stage35_ex_v61_legacy_replay.py target')
target=sys.argv[1]
real=json.loads(STATE.read_text())
assert real['schema']==V61
assert real['history_snapshot']['commit_sha']==SOURCE
assert real['history_snapshot']['schema']==V60
assert real['history_snapshot']['hostile_audited'] is False
assert real['last_audited_authority']['pr']==1633
assert real['hostile_audit_repair']['review_id']==5124106960
assert real['claims']['goal4x_executed'] is True
assert real['claims']['open_receiver_Picard_group_computed'] is True
assert real['claims']['open_receiver_Picard_rank']==35
assert real['claims']['open_receiver_H1_Pic_computed'] is True
assert real['claims']['open_receiver_H1_Pic_structure']=='Z/2 x Z/2'
assert real['claims']['open_receiver_algebraic_brauer_group_computed'] is False
assert real['claims']['brauer_manin_obstruction_obtained'] is False
assert real['claims']['E1_proved'] is False
snaptext=SNAP.read_text();snap=json.loads(snaptext)
assert snap['schema']==V60
assert snap['current']['unit']=='35EX-35_GOAL4W_FULL_PICARD_H1_AND_ALGEBRAIC_BRAUER_PREFLIGHT'
assert snap['claims']['goal4w_executed'] is True
assert snap['claims']['proper_surface_full_Picard_H1_trivial'] is True
assert snap['claims']['proper_surface_algebraic_brauer_quotient_trivial'] is True
assert snap['claims']['open_receiver_Picard_group_computed'] is False
assert snap['claims']['open_receiver_algebraic_brauer_group_computed'] is False
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
            sys.argv=['verify_stage35_ex_v60_legacy_replay.py',target]
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_v60_legacy_replay.py'),run_name='__main__')
        else:
            sys.argv=['verify_stage35_ex_35_goal4w.py']
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_35_goal4w.py'),run_name='__main__')
    finally:sys.argv=oldargv
finally:Path.read_text=orig
print(f'PASS V61_PERSISTED_V60_REPLAY_{target}')
