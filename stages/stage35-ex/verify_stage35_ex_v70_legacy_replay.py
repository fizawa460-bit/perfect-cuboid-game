#!/usr/bin/env python3
"""Replay persisted V69 history while V70 Goal4AG is live."""
from __future__ import annotations
import json,runpy,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
SNAP=ROOT/'stages/stage35-ex/snapshots/MAIN-STATE-V69-8bed9082aeeb.json'
V70='STAGE35_EX_PESCH_E1_STATE_V70_GOAL4AG_HOMOGENEOUS_DEGREE25_TO30_PRINCIPALIZATION_EXCLUDED_DEGREE31_SURVIVES_RETAINED_CURVE_TEST_PENDING_AUDIT'
V69='STAGE35_EX_PESCH_E1_STATE_V69_GOAL4AF_C5_MARKED_PICARD_ADAPTER_COMPUTED_TARGET_SPAN_BLOCKED_GENERAL_QI_PRINCIPAL_FUNCTION_PENDING_AUDIT'
SOURCE='8bed9082aeeb893b3c34c5fc0da4103415d215f1'
OLD69={'base',*{str(i) for i in range(10,33)},'32p','33g1','33g2','33','34','35','35g4a','35g4b','35g4c','35g4d','35g4e','35g4f','35g4g','35g4h','35g4i','35g4j','35g4k','35g4l','35g4m','35g4n','35g4o','35g4p','35g4q','35g4r','35g4s','35g4t','35g4u','35g4v','35g4w','35g4x','35g4y','35g4z','35g4aa','35g4ab','35g4ac','35g4ad','35g4ae'}
ALLOWED=OLD69|{'35g4af'}
if len(sys.argv)!=2 or sys.argv[1] not in ALLOWED: raise SystemExit('usage: verify_stage35_ex_v70_legacy_replay.py target')
target=sys.argv[1]
real=json.loads(STATE.read_text())
assert real['schema']==V70
assert real['history_snapshot']['commit_sha']==SOURCE
assert real['history_snapshot']['schema']==V69
assert real['history_snapshot']['snapshot_file_commit_sha']=='634a10efa9e04fe6aea836d213edf9f3544dba71'
assert real['history_snapshot']['hostile_audited'] is False
assert real['last_audited_authority']['pr']==1633
assert real['claims']['goal4ag_executed'] is True
assert real['claims']['open_receiver_second_class_noneffective_through_degree']==30
assert real['claims']['open_receiver_second_class_first_retained_curve_survivor_degree']==31
assert real['claims']['open_receiver_second_class_degree31_effectivity_proved'] is False
assert real['claims']['open_receiver_second_class_explicit_F_B_computed'] is False
assert real['claims']['E1_proved'] is False
snaptext=SNAP.read_text(); snap=json.loads(snaptext)
assert snap['schema']==V69
assert snap['current']['unit']=='35EX-35_GOAL4AF_SECOND_CLASS_QI_CYCLIC_C5_DIRECT_MARKED_PICARD_TARGET_SPAN'
assert snap['claims']['goal4af_executed'] is True
assert snap['claims']['open_receiver_second_class_target_span_with_C5_pairs_computed'] is True
assert snap['claims']['open_receiver_second_class_explicit_F_B_computed'] is False
assert snap['claims']['E1_proved'] is False
orig=Path.read_text; sr=STATE.resolve()
def patched(self:Path,*a,**k):
    if self.resolve()==sr:return snaptext
    return orig(self,*a,**k)
Path.read_text=patched
try:
    oldargv=sys.argv[:]
    try:
        if target in OLD69:
            sys.argv=['verify_stage35_ex_v69_legacy_replay.py',target]
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_v69_legacy_replay.py'),run_name='__main__')
        else:
            sys.argv=['verify_stage35_ex_35_goal4af.py']
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_35_goal4af.py'),run_name='__main__')
    finally: sys.argv=oldargv
finally: Path.read_text=orig
print(f'PASS V70_PERSISTED_V69_REPLAY_{target}')
