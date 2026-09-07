#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, subprocess, sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
S33=HERE.parent
STATE_SHA='3c53225c087415a62deae70eadcf2287252b41cb872022cc26360e9d194f4b1c'
R4_SHA='cead57f641b02e8defb8cb614ee1b1acdca1ee6d1e9f7c04514ccfffef5577e0'
NEXT='V91C1X_R5_FIND_OR_CONSTRUCT_SOURCE_BOUND_A2_02_FINITE_COVER_LOCAL_EQUATION_UNIFORMIZER_OVERLAP_GLUE_PACKAGE'
MISSING='NEW_SOURCE_BOUND_A2_02_FINITE_COVER_WITH_LITERAL_LOCAL_EQUATIONS_UNIFORMIZERS_OVERLAP_TRANSITIONS_AND_SWAP23_COMMON_REFINEMENT_SUFFICIENT_TO_MATERIALIZE_Z_IJK_ELL_IJ_R_IJ_AND_TRIPLE_OVERLAP_IDENTITY'

def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p,h):
    o=json.loads(p.read_text(encoding='utf-8')); b=dict(o); q=b.pop('canonical_sha256'); assert q==h==csha(b),p; return o

s=load(S33/'MAIN-STATE.json',STATE_SHA)
r4=load(HERE/'e3-v91c1x-r4-retained-boundary-resolution-insufficient-for-cover-indexed-h2.json',R4_SHA)
assert s['schema']=='STAGE33_MAIN_COMPACT_STATE_V54_V91C1X_R4_HOSTILE_PASS_R5_ACTIVE'
assert s['authority_sync']['frontier_authority']=='V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT'
assert s['authority_sync']['status']=='V91C1V_AUTHORITY_R4_HOSTILE_PASS_R5_CONSTRUCTION_ACTIVE'
cg=s['candidate_audit_gate']
assert cg['pr']==1682 and cg['hostile_audit_verdict']=='PASS' and cg['hostile_audit_review']==5128292956
assert cg['hostile_audit_review_node']=='PRR_kwDOTr52Y88AAAABMauKXA'
assert cg['exact_audited_head']=='4dd839ec21ece8ef08c25cb385e28050720dda77'
assert cg['merge_commit']=='726198a3d8ca4834e45c2ef275a75266b0f752b4' and cg['merged'] is True
assert cg['mathematical_authority_promoted'] is False and cg['merge_allowed'] is False
r4a=s['continuation_provenance']['x_r4_grouped_hostile_audit']
assert r4a['verdict']=='PASS' and r4a['checkpoint_credit']=='NONCREDIT_CONSTRUCTION_BLOCKER_ONLY' and r4a['authority_unchanged'] is True
assert r4['credit']=='NONCREDIT_CONSTRUCTION_BLOCKER' and r4['next_missing_object']==MISSING and r4['next_exact_leaf_after_audit']==NEXT
assert s['current']['active_missing_interface']==MISSING and s['current']['next_exact_leaf']==NEXT
assert s['execution_gate']['advance_allowed'] is True
assert s['execution_gate']['advance_scope']=='V91C1X_R5_SOURCE_BOUND_COVER_LOCAL_EQUATION_UNIFORMIZER_OVERLAP_GLUE_PACKAGE_ONLY'
assert s['execution_gate']['next_expected_command']=='STAGE33_MAIN_BATCH_V91C1X_R5_COVER_GLUE_PACKAGE'
for k in ['stage33_12_closed_exact','stage33_13_released','receiver_credit','theorem_credit','endpoint_credit','merge_allowed']:
    assert s['firewalls'][k] is False,k
assert s['stage33_progress']=='6/11'
subprocess.run([sys.executable,str(S33/'sync_main_state.py'),'--check'],check=True)
print(json.dumps({'success':True,'marker':'V115_V91C1X_R5_ACTIVE_CURRENT_STARTUP','state_sha256':STATE_SHA,'r4_sha256':R4_SHA,'next_exact_leaf':NEXT,'stage33_progress':'6/11'},sort_keys=True))
