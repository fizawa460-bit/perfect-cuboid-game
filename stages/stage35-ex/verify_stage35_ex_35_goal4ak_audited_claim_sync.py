#!/usr/bin/env python3
"""Verify the post-audit V74 synchronization for Goal4AK."""
from __future__ import annotations
import json,runpy,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
SYNC=ROOT/'stages/stage35-ex/35ex-35/goal4ak-audited-claim-sync.json'
V74='STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED'

oldargv=sys.argv[:]
try:
    sys.argv=['verify_stage35_ex_v74_legacy_replay.py','35g4ak']
    runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_v74_legacy_replay.py'),run_name='__main__')
finally:
    sys.argv=oldargv

s=json.loads(STATE.read_text())
r=json.loads(SYNC.read_text())
assert s['schema']==V74
assert r['schema']=='STAGE35_EX_GOAL4AK_AUDITED_CLAIM_SYNC_V1'
assert r['source_pr']==1720
assert r['hostile_audit']['result']=='PASS'
assert r['hostile_audit']['review_id']==5142248509
assert r['hostile_audit']['audited_exact_head_sha']=='2d6ec7c836857386b3e5553cc3117295775ca8d4'
assert r['merge_sha']=='42f20e47babdfdda068a605e3fec489eeace460c'
assert r['exact_head_evidence']['aggregate_run']==34229590114
assert r['exact_head_evidence']['goal4ak_run']==34229590249
assert r['exact_head_evidence']['goal4ak_job']==102072085126
assert r['explicit_F_B']['representative']=='A31/B31'
assert r['explicit_F_B']['symbol_mod_Br0']=='(-1,F_B)'
assert r['explicit_F_B']['homogeneous_degree']==31
assert r['explicit_F_B']['numerator_sha256']=='358ee320a7d28b790ee9267aad3f95e8ff35af15d002976720622bd2b6e8decb'
assert r['explicit_F_B']['denominator_sha256']=='28d738a7a23df1ace371cabe3a476c270a54c6b7798e8172bd7111b14e25fc29'
assert r['explicit_F_B']['assembly_canonical_sha256']=='105060a54ae5c64ba4d3d978fce5a7b76e890ee1516268b09ac96c4722d982d9'
assert r['explicit_F_B']['audited_materialized'] is True
assert s['last_audited_authority']['hostile_review_id']==5142248509
assert s['last_audited_authority']['merge_sha']=='42f20e47babdfdda068a605e3fec489eeace460c'
assert s['claims']['open_receiver_second_class_explicit_F_B_computed'] is True
assert s['claims']['open_receiver_second_class_explicit_F_B_hostile_audited'] is True
assert s['claims']['open_receiver_second_class_local_evaluation_released'] is True
assert s['claims']['open_receiver_local_evaluations_computed'] is False
assert s['claims']['brauer_manin_obstruction_obtained'] is False
assert s['claims']['E1_proved'] is False
assert s['claims']['stage35_closed'] is False
assert s['claims']['perfect_cuboid_existence_claim'] is False
assert s['claims']['perfect_cuboid_nonexistence_claim'] is False
print('STAGE35_EX_GOAL4AK_AUDITED_CLAIM_SYNC=PASS')
