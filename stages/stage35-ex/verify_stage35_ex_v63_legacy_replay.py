#!/usr/bin/env python3
"""Replay persisted V62 Goal4Y history while V63 Goal4Z is live."""
from __future__ import annotations
import json,runpy,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
SNAP=ROOT/'stages/stage35-ex/snapshots/MAIN-STATE-V62-67c4f6dafa63.json'
V63='STAGE35_EX_PESCH_E1_STATE_V63_GOAL4Z_ONE_EXPLICIT_BIQUATERNION_SECOND_QI_PRINCIPALIZATION_PENDING_AUDIT'
V62='STAGE35_EX_PESCH_E1_STATE_V62_GOAL4Y_TWO_ALGEBRAIC_BRAUER_CLASSES_WITH_BOUNDARY_RESIDUES_PENDING_EXPLICIT_SYMBOL_AND_AUDIT'
SOURCE='67c4f6dafa63896f68b97a217d71443388b6d1ee'
OLD={'base',*{str(i) for i in range(10,33)},'32p','33g1','33g2','33','34','35','35g4a','35g4b','35g4c','35g4d','35g4e','35g4f','35g4g','35g4h','35g4i','35g4j','35g4k','35g4l','35g4m','35g4n','35g4o','35g4p','35g4q','35g4r','35g4s','35g4t','35g4u','35g4v','35g4w','35g4x'}
ALLOWED=OLD|{'35g4y'}
if len(sys.argv)!=2 or sys.argv[1] not in ALLOWED:raise SystemExit('usage: verify_stage35_ex_v63_legacy_replay.py target')
target=sys.argv[1]
real=json.loads(STATE.read_text())
assert real['schema']==V63
assert real['history_snapshot']['commit_sha']==SOURCE
assert real['history_snapshot']['schema']==V62
assert real['history_snapshot']['hostile_audited'] is False
assert real['last_audited_authority']['pr']==1633
assert real['claims']['goal4z_executed'] is True
assert real['claims']['open_receiver_one_explicit_rational_symbol_representative_computed'] is True
assert real['claims']['open_receiver_explicit_rational_symbol_representative_count']==1
assert real['claims']['open_receiver_both_goal4y_explicit_symbols_materialized'] is False
assert real['claims']['open_receiver_local_evaluations_computed'] is False
assert real['claims']['brauer_manin_obstruction_obtained'] is False
assert real['claims']['E1_proved'] is False
snaptext=SNAP.read_text();snap=json.loads(snaptext)
assert snap['schema']==V62
assert snap['current']['unit']=='35EX-35_GOAL4Y_OPEN_RECEIVER_HS_PURITY_RESIDUE_TWO_CLASS_LIFT_PREFLIGHT'
assert snap['claims']['goal4y_executed'] is True
assert snap['claims']['open_receiver_two_independent_algebraic_brauer_classes_exist'] is True
assert snap['claims']['open_receiver_explicit_rational_symbol_representatives_computed'] is False
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
            sys.argv=['verify_stage35_ex_v62_legacy_replay.py',target]
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_v62_legacy_replay.py'),run_name='__main__')
        else:
            sys.argv=['verify_stage35_ex_35_goal4y.py']
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_35_goal4y.py'),run_name='__main__')
    finally:sys.argv=oldargv
finally:Path.read_text=orig
print(f'PASS V63_PERSISTED_V62_REPLAY_{target}')
