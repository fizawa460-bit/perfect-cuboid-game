#!/usr/bin/env python3
"""Replay persisted V64 Goal4AA history while V65 Goal4AB is live."""
from __future__ import annotations
import json,runpy,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
SNAP=ROOT/'stages/stage35-ex/snapshots/MAIN-STATE-V64-691e934b0f7b.json'
V65='STAGE35_EX_PESCH_E1_STATE_V65_GOAL4AB_LOW_DEGREE_RR_FEEDERS_BLOCKED_GENERAL_QI_PRINCIPAL_FUNCTION_PENDING_AUDIT'
V64='STAGE35_EX_PESCH_E1_STATE_V64_GOAL4AA_LINEAR_HYPERPLANE_PRODUCT_ROUTE_BLOCKED_GENERAL_QI_PRINCIPAL_FUNCTION_PENDING_AUDIT'
SOURCE='691e934b0f7b2048cc4c862d3aeea6873c784b52'
OLD={'base',*{str(i) for i in range(10,33)},'32p','33g1','33g2','33','34','35','35g4a','35g4b','35g4c','35g4d','35g4e','35g4f','35g4g','35g4h','35g4i','35g4j','35g4k','35g4l','35g4m','35g4n','35g4o','35g4p','35g4q','35g4r','35g4s','35g4t','35g4u','35g4v','35g4w','35g4x','35g4y','35g4z'}
ALLOWED=OLD|{'35g4aa'}
if len(sys.argv)!=2 or sys.argv[1] not in ALLOWED: raise SystemExit('usage: verify_stage35_ex_v65_legacy_replay.py target')
target=sys.argv[1]
real=json.loads(STATE.read_text())
assert real['schema']==V65
assert real['history_snapshot']['commit_sha']==SOURCE
assert real['history_snapshot']['schema']==V64
assert real['history_snapshot']['hostile_audited'] is False
assert real['last_audited_authority']['pr']==1633
assert real['claims']['goal4ab_executed'] is True
assert real['claims']['open_receiver_second_class_all_43_degree16_linear_sections_completed'] is True
assert real['claims']['open_receiver_second_class_linear_section_divisor_span_rank']==31
assert real['claims']['open_receiver_second_class_low_degree_C4_C5_nonlinear_elimination_route_blocked'] is True
assert real['claims']['open_receiver_second_class_explicit_F_B_computed'] is False
assert real['claims']['brauer_manin_obstruction_obtained'] is False
assert real['claims']['E1_proved'] is False
snaptext=SNAP.read_text(); snap=json.loads(snaptext)
assert snap['schema']==V64
assert snap['current']['unit']=='35EX-35_GOAL4AA_SECOND_CLASS_QI_CYCLIC_PRINCIPAL_DIVISOR_ADAPTER_PREFLIGHT'
assert snap['claims']['goal4aa_executed'] is True
assert snap['claims']['open_receiver_second_class_linear_hyperplane_product_route_blocked'] is True
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
        if target in OLD:
            sys.argv=['verify_stage35_ex_v64_legacy_replay.py',target]
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_v64_legacy_replay.py'),run_name='__main__')
        else:
            sys.argv=['verify_stage35_ex_35_goal4aa.py']
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_35_goal4aa.py'),run_name='__main__')
    finally: sys.argv=oldargv
finally: Path.read_text=orig
print(f'PASS V65_PERSISTED_V64_REPLAY_{target}')
