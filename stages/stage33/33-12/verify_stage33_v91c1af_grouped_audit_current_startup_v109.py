#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path

D=Path(__file__).resolve().parent; S33=D.parent
STATE=S33/'MAIN-STATE.json'; C=D/'e3-v91c1af-a2-02-source-bound-stabilizer-fixed-subspace.json'
AUTH=D/'e3-v91c1v-a2-02-actual-prime-known140-locator-bounded-result.json'; CTL=S33/'controller.json'
AF=D/'diagnose_e3_v91c1af_sign_a2_seed_fixed_subspace.py'; NOTE=D/'e3-v91c1af-kummer-sign-a2-source-lock.md'
STATE_SHA='9fc178d338e540ed246627385bc0a9909b73391ed3d4eb2edea43d8a10ea021e'
C_SHA='75e7202b3c428a5e79f18421f20e75f4f09ac243614e3e36d8109ce79b3db76a'
AUTH_SHA='60f41e8e324e5fb29d1b109adb860b947308b521f677e49c4965e337a0c2d2d2'
CTL_SHA='02cb0f964086509f8bef4ad4dc5481f9f668b7ca8127f54ebb2952831638f773'
AF_BLOB='6bc01ca7c0ff8dda25bc8e01f5258df340c2d1ab'; NOTE_BLOB='dde3a20cc91021cc8d2a504e1d2f9d1c577cffb8'
NEXT='V91C1AG_REDUCE_THE_SOURCE_BOUND_MARKED_BRAUER_QUOTIENT_FINGERPRINT_TO_FIVE_DISCRIMINATING_BITS_AND_MATERIALIZE_THE_FIRST_GENUINE_BIT'

def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def gitblob(data): return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
def load(p,h):
 o=json.loads(p.read_text()); b=dict(o); q=b.pop('canonical_sha256'); assert q==h==csha(b),p; return o

s=load(STATE,STATE_SHA); c=load(C,C_SHA); au=load(AUTH,AUTH_SHA)
ctl=json.loads(CTL.read_text()); cb=dict(ctl); q=cb.pop('projection_canonical_sha256'); assert q==CTL_SHA==csha(cb)
assert gitblob(AF.read_bytes())==AF_BLOB and gitblob(NOTE.read_bytes())==NOTE_BLOB
assert s['authority_sync']['frontier_authority']=='V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT'
assert s['authority_sync']['branch_candidate_frontier']=='V91C1AF_A2_02_SOURCE_BOUND_STABILIZER_FIXED_SUBSPACE_DIM5'
assert s['branch_exact_frontier_candidate']==str(C.relative_to(Path.cwd()))
cg=s['candidate_audit_gate']; assert cg['candidate']=='V91C1AF_A2_02_SOURCE_BOUND_STABILIZER_FIXED_SUBSPACE_DIM5'
assert cg['candidate_certificate_sha256']==C_SHA and cg['pr']==1671 and cg['status']=='PENDING_GROUPED_HOSTILE_AUDIT'
assert cg['audit_pass_credit'] is False and cg['merge_allowed'] is False
assert [r['candidate'] for r in cg['accumulated_branch_candidates']]==[
 'V91C1W_A2_02_ALL8_PICARD64_COMPLETE_SWAP23_PIC2_ZERO',
 'V91C1X_A2_02_SWAP23_H2_SEED_FIXED_MASK20_EXCLUDED',
 'V91C1AF_A2_02_SOURCE_BOUND_STABILIZER_FIXED_SUBSPACE_DIM5']
p=c['proper14_reduction']; assert p['joint_cc_ct_fixed_dimension_f2']==10 and p['after_swap23_dimension_f2']==7
assert p['after_sign_b1_dimension_f2']==6 and p['after_sign_a2_dimension_f2']==5 and p['final_cardinality']==32
assert p['minimal_coordinate_discriminator_positions_one_based']==[1,2,3,4,5]
e=c['exact_consequence']; assert e['a2_02_marked_brauer_image_computed'] is False
assert e['a2_02_marked_brauer_image_constrained_to_source_bound_fixed_subspace_dimension_f2']==5
assert e['next_exact_leaf']==NEXT
f=s['current_exact_frontier']; assert f['a2_02_sign_b1_seed_fixed_mod_pic2'] is True and f['a2_02_sign_a2_seed_fixed_mod_pic2'] is True
assert f['a2_02_unknown_brauer_image_source_bound_stabilizer_fixed_subspace_dimension_f2']==5
assert f['a2_02_unknown_brauer_image_source_bound_stabilizer_fixed_subspace_cardinality']==32
assert f['a2_02_marked_brauer_image_computed'] is False and f['source_bound_proper14_evaluation_bits_materialized']==0
assert s['current']['next_exact_leaf']==NEXT
assert s['execution_gate']['next_expected_command']=='HOSTILE_AUDIT_PR_1671_GROUPED_V91C1W_X_AF_EXACT_HEAD'
assert s['stage33_progress']=='6/11' and s['firewalls']['merge_allowed'] is False
assert au['canonical_sha256']==AUTH_SHA and ctl['merge_allowed'] is False
print(json.dumps({'success':True,'marker':'V109_V91C1V_AUTHORITY_V91C1AF_DIM5_GROUPED_AUDIT_CHECKPOINT','state_sha256':STATE_SHA,'candidate_sha256':C_SHA,'next_exact_leaf':NEXT,'fixed_dimension_f2':5,'candidate_count':32,'credit':False},sort_keys=True))
