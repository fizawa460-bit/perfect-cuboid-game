#!/usr/bin/env python3
"""Replay persisted V61 Goal4X history while V62 Goal4Y is live."""
from __future__ import annotations
import json,runpy,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
SNAP=ROOT/'stages/stage35-ex/snapshots/MAIN-STATE-V61-0a8af929e004.json'
V62='STAGE35_EX_PESCH_E1_STATE_V62_GOAL4Y_TWO_ALGEBRAIC_BRAUER_CLASSES_WITH_BOUNDARY_RESIDUES_PENDING_EXPLICIT_SYMBOL_AND_AUDIT'
V61='STAGE35_EX_PESCH_E1_STATE_V61_GOAL4X_OPEN_PICARD_H1_Z2_SQUARED_PENDING_BRAUER_LIFT_AND_AUDIT'
SOURCE='0a8af929e004815bc9eb5749535885edda0835df'
OLD={'base',*{str(i) for i in range(10,33)},'32p','33g1','33g2','33','34','35','35g4a','35g4b','35g4c','35g4d','35g4e','35g4f','35g4g','35g4h','35g4i','35g4j','35g4k','35g4l','35g4m','35g4n','35g4o','35g4p','35g4q','35g4r','35g4s','35g4t','35g4u','35g4v','35g4w'}
ALLOWED=OLD|{'35g4x'}
if len(sys.argv)!=2 or sys.argv[1] not in ALLOWED:raise SystemExit('usage: verify_stage35_ex_v62_legacy_replay.py target')
target=sys.argv[1]
real=json.loads(STATE.read_text())
assert real['schema']==V62
assert real['history_snapshot']['commit_sha']==SOURCE
assert real['history_snapshot']['schema']==V61
assert real['history_snapshot']['hostile_audited'] is False
assert real['last_audited_authority']['pr']==1633
assert real['hostile_audit_repair']['review_id']==5124106960
assert real['claims']['goal4y_executed'] is True
assert real['claims']['open_receiver_unit_lattice_rank']==3
assert real['claims']['open_receiver_H1_two_class_transgression_trivial'] is True
assert real['claims']['open_receiver_two_independent_algebraic_brauer_classes_exist'] is True
assert real['claims']['open_receiver_purity_localization_residue_representatives_computed'] is True
assert real['claims']['open_receiver_algebraic_brauer_group_computed'] is False
assert real['claims']['brauer_manin_obstruction_obtained'] is False
assert real['claims']['E1_proved'] is False
snaptext=SNAP.read_text();snap=json.loads(snaptext)
assert snap['schema']==V61
assert snap['current']['unit']=='35EX-35_GOAL4X_OPEN_RECEIVER_BOUNDARY_PICARD_GALOIS_AND_ALGEBRAIC_BRAUER_PREFLIGHT'
assert snap['claims']['goal4x_executed'] is True
assert snap['claims']['open_receiver_Picard_rank']==35
assert snap['claims']['open_receiver_H1_Pic_structure']=='Z/2 x Z/2'
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
            sys.argv=['verify_stage35_ex_v61_legacy_replay.py',target]
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_v61_legacy_replay.py'),run_name='__main__')
        else:
            sys.argv=['verify_stage35_ex_35_goal4x.py']
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_35_goal4x.py'),run_name='__main__')
    finally:sys.argv=oldargv
finally:Path.read_text=orig
print(f'PASS V62_PERSISTED_V61_REPLAY_{target}')
