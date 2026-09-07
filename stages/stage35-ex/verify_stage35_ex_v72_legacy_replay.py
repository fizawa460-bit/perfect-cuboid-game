#!/usr/bin/env python3
"""Replay persisted V71 history while V72 Goal4AI is live."""
from __future__ import annotations
import json,runpy,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
SNAP=ROOT/'stages/stage35-ex/snapshots/MAIN-STATE-V71-a8d275311cbd.json'
V72='STAGE35_EX_PESCH_E1_STATE_V72_GOAL4AI_DEGREE31_HOMOGENEOUS_PRINCIPALIZATION_EXISTENCE_PROVED_LITERAL_SECTION_COEFFICIENTS_PENDING_AUDIT'
V71='STAGE35_EX_PESCH_E1_STATE_V71_GOAL4AH_DEGREE31_RR_EFFECTIVITY_PROVED_LITERAL_F_B_PENDING_AUDIT'
OLD71={'base',*{str(i) for i in range(10,33)},'32p','33g1','33g2','33','34','35','35g4a','35g4b','35g4c','35g4d','35g4e','35g4f','35g4g','35g4h','35g4i','35g4j','35g4k','35g4l','35g4m','35g4n','35g4o','35g4p','35g4q','35g4r','35g4s','35g4t','35g4u','35g4v','35g4w','35g4x','35g4y','35g4z','35g4aa','35g4ab','35g4ac','35g4ad','35g4ae','35g4af','35g4ag'}
ALLOWED=OLD71|{'35g4ah'}
if len(sys.argv)!=2 or sys.argv[1] not in ALLOWED: raise SystemExit('usage: verify_stage35_ex_v72_legacy_replay.py target')
target=sys.argv[1]
real=json.loads(STATE.read_text())
assert real['schema']==V72
assert real['history_snapshot']['schema']==V71
assert real['history_snapshot']['path']=='stages/stage35-ex/snapshots/MAIN-STATE-V71-a8d275311cbd.json'
assert real['history_snapshot']['commit_sha']=='a8d275311cbd5805f73f8e070ed14d65e8eae075'
assert real['history_snapshot']['snapshot_file_commit_sha']=='49ed2417c3de101bf6c62dc7c483de686f69693c'
assert real['history_snapshot']['hostile_audited'] is False
assert real['last_audited_authority']['pr']==1633
assert real['claims']['goal4ai_executed'] is True
assert real['claims']['open_receiver_second_class_homogeneous_principalization_existence_proved'] is True
assert real['claims']['open_receiver_second_class_explicit_F_B_computed'] is False
assert real['claims']['E1_proved'] is False

snaptext=SNAP.read_text(); snap=json.loads(snaptext)
assert snap['schema']==V71
assert snap['current']['unit']=='35EX-35_GOAL4AH_SECOND_CLASS_QI_CYCLIC_DEGREE31_SURVIVOR_EFFECTIVITY_AND_PRINCIPAL_FUNCTION_SYNTHESIS_PREFLIGHT'
assert snap['claims']['goal4ah_executed'] is True
assert snap['claims']['open_receiver_second_class_degree31_effectivity_proved'] is True
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
        if target in OLD71:
            sys.argv=['verify_stage35_ex_v71_legacy_replay.py',target]
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_v71_legacy_replay.py'),run_name='__main__')
        else:
            sys.argv=['verify_stage35_ex_35_goal4ah.py']
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_35_goal4ah.py'),run_name='__main__')
    finally: sys.argv=oldargv
finally: Path.read_text=orig
print(f'PASS V72_PERSISTED_V71_REPLAY_{target}')
