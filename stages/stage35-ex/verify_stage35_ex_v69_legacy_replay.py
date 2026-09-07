#!/usr/bin/env python3
"""Replay persisted V68 Goal4AE history while V69 Goal4AF is live."""
from __future__ import annotations
import json,runpy,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
SNAP=ROOT/'stages/stage35-ex/snapshots/MAIN-STATE-V68-00d4c9bf9bb3.json'
V69='STAGE35_EX_PESCH_E1_STATE_V69_GOAL4AF_C5_MARKED_PICARD_ADAPTER_COMPUTED_TARGET_SPAN_BLOCKED_GENERAL_QI_PRINCIPAL_FUNCTION_PENDING_AUDIT'
V68='STAGE35_EX_PESCH_E1_STATE_V68_GOAL4AE_C5K_NAME_COLLISION_REPAIRED_DIRECT_S_IMAGEINPIC_PENDING_AUDIT'
SOURCE='00d4c9bf9bb37781c81954fb41f22e97d721995b'
OLD={'base',*{str(i) for i in range(10,33)},'32p','33g1','33g2','33','34','35','35g4a','35g4b','35g4c','35g4d','35g4e','35g4f','35g4g','35g4h','35g4i','35g4j','35g4k','35g4l','35g4m','35g4n','35g4o','35g4p','35g4q','35g4r','35g4s','35g4t','35g4u','35g4v','35g4w','35g4x','35g4y','35g4z','35g4aa','35g4ab','35g4ac','35g4ad'}
ALLOWED=OLD|{'35g4ae'}
if len(sys.argv)!=2 or sys.argv[1] not in ALLOWED: raise SystemExit('usage: verify_stage35_ex_v69_legacy_replay.py target')
target=sys.argv[1]
real=json.loads(STATE.read_text())
assert real['schema']==V69
assert real['history_snapshot']['commit_sha']==SOURCE
assert real['history_snapshot']['schema']==V68
assert real['history_snapshot']['hostile_audited'] is False
assert real['last_audited_authority']['pr']==1633
assert real['claims']['goal4af_executed'] is True
assert real['claims']['open_receiver_second_class_C5_pair_marked_picard_adapter_computed'] is True
assert real['claims']['open_receiver_second_class_target_span_with_C5_pairs_computed'] is True
assert real['claims']['open_receiver_second_class_target_in_augmented_C5_marked_span'] is False
assert real['claims']['open_receiver_second_class_explicit_F_B_computed'] is False
assert real['claims']['E1_proved'] is False
snaptext=SNAP.read_text(); snap=json.loads(snaptext)
assert snap['schema']==V68
assert snap['current']['unit']=='35EX-35_GOAL4AE_SECOND_CLASS_QI_CYCLIC_C5K_NAME_COLLISION_DIRECT_S_IMAGEINPIC_ROUTE_REPAIR'
assert snap['claims']['goal4ae_executed'] is True
assert snap['claims']['open_receiver_second_class_C5_pair_marked_picard_adapter_computed'] is False
assert snap['claims']['open_receiver_second_class_target_span_with_C5_pairs_computed'] is False
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
            sys.argv=['verify_stage35_ex_v68_legacy_replay.py',target]
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_v68_legacy_replay.py'),run_name='__main__')
        else:
            sys.argv=['verify_stage35_ex_35_goal4ae.py']
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_35_goal4ae.py'),run_name='__main__')
    finally: sys.argv=oldargv
finally: Path.read_text=orig
print(f'PASS V69_PERSISTED_V68_REPLAY_{target}')
