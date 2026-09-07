#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
H=Path(__file__).resolve().parent; D=H/'33-12'; OUT=H/'MAIN-STATE.json'; CTL=H/'controller.json'
STATE_SHA='9fc178d338e540ed246627385bc0a9909b73391ed3d4eb2edea43d8a10ea021e'
AUTH_SHA='60f41e8e324e5fb29d1b109adb860b947308b521f677e49c4965e337a0c2d2d2'
W_SHA='e84dcc6692849ff065b0380e760bf725f77fff6754ab5bbdc39b7e608c76a4c7'
X_SHA='aca4d8929f9cc04b24da6e8a7ba0ec0b89be18ac1bc2bf3e6e1f870808bdf29f'
AF_SHA='75e7202b3c428a5e79f18421f20e75f4f09ac243614e3e36d8109ce79b3db76a'
CTL_SHA='02cb0f964086509f8bef4ad4dc5481f9f668b7ca8127f54ebb2952831638f773'
NEXT='V91C1AG_REDUCE_THE_SOURCE_BOUND_MARKED_BRAUER_QUOTIENT_FINGERPRINT_TO_FIVE_DISCRIMINATING_BITS_AND_MATERIALIZE_THE_FIRST_GENUINE_BIT'
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p,h):
 o=json.loads(p.read_text()); b=dict(o); q=b.pop('canonical_sha256'); assert q==h==csha(b),p; return o
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--check',action='store_true'); ap.add_argument('--write',action='store_true'); a=ap.parse_args()
 s=load(OUT,STATE_SHA); au=load(D/'e3-v91c1v-a2-02-actual-prime-known140-locator-bounded-result.json',AUTH_SHA)
 w=load(D/'e3-v91c1w-a2-02-all8-picard64-reduction.json',W_SHA); x=load(D/'e3-v91c1x-a2-02-kummer-naturality-mask20-exclusion.json',X_SHA)
 af=load(D/'e3-v91c1af-a2-02-source-bound-stabilizer-fixed-subspace.json',AF_SHA)
 ctl=json.loads(CTL.read_text()); cb=dict(ctl); q=cb.pop('projection_canonical_sha256'); assert q==CTL_SHA==csha(cb) and ctl['merge_allowed'] is False
 assert s['authority_sync']['frontier_authority']=='V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT'
 assert s['authority_sync']['branch_candidate_frontier']=='V91C1AF_A2_02_SOURCE_BOUND_STABILIZER_FIXED_SUBSPACE_DIM5'
 ag=s['authority_audit_gate']; assert ag['pr']==1667 and ag['hostile_audit_review']==5126709022 and ag['hostile_audit_verdict']=='PASS'
 assert ag['exact_audited_head']=='56ac6b79a4a8e13205a497af1a2cdd6d1e23aee4' and ag['merge_commit']=='bd1f40297f8dcf79e5bb4ef0b8cdc13fdb844177' and ag['merged'] is True
 cg=s['candidate_audit_gate']; assert cg['candidate']=='V91C1AF_A2_02_SOURCE_BOUND_STABILIZER_FIXED_SUBSPACE_DIM5' and cg['candidate_certificate_sha256']==AF_SHA
 assert cg['pr']==1671 and cg['status']=='PENDING_GROUPED_HOSTILE_AUDIT' and cg['audit_pass_credit'] is False and cg['merge_allowed'] is False
 assert [r['candidate'] for r in cg['accumulated_branch_candidates']]==['V91C1W_A2_02_ALL8_PICARD64_COMPLETE_SWAP23_PIC2_ZERO','V91C1X_A2_02_SWAP23_H2_SEED_FIXED_MASK20_EXCLUDED','V91C1AF_A2_02_SOURCE_BOUND_STABILIZER_FIXED_SUBSPACE_DIM5']
 assert au['canonical_sha256']==AUTH_SHA and w['canonical_sha256']==W_SHA and x['canonical_sha256']==X_SHA and af['canonical_sha256']==AF_SHA
 p=af['proper14_reduction']; assert [p['joint_cc_ct_fixed_dimension_f2'],p['after_swap23_dimension_f2'],p['after_sign_b1_dimension_f2'],p['after_sign_a2_dimension_f2']]==[10,7,6,5]
 assert p['final_cardinality']==32 and p['minimal_coordinate_discriminator_positions_one_based']==[1,2,3,4,5]
 f=s['current_exact_frontier']; assert f['a2_02_swap23_seed_fixed_mod_pic2'] is True and f['a2_02_sign_b1_seed_fixed_mod_pic2'] is True and f['a2_02_sign_a2_seed_fixed_mod_pic2'] is True
 assert f['a2_02_unknown_brauer_image_source_bound_stabilizer_fixed_subspace_dimension_f2']==5 and f['a2_02_unknown_brauer_image_source_bound_stabilizer_fixed_subspace_cardinality']==32
 assert f['a2_02_marked_brauer_image_computed'] is False and f['source_bound_proper14_evaluation_bits_materialized']==0
 bp=s['continuation_provenance']['grouped_hostile_audit_policy']; assert bp['same_pr']==1671 and bp['user_authorized_same_pr_noncredit_accumulation'] is True
 assert bp['current_stop_reason']=='MATHEMATICALLY_SUBSTANTIAL_V91C1AF_SOURCE_BOUND_FIXED_SUBSPACE_DIM5'
 assert s['current']['next_exact_leaf']==NEXT and s['execution_gate']['next_expected_command']=='HOSTILE_AUDIT_PR_1671_GROUPED_V91C1W_X_AF_EXACT_HEAD'
 assert s['stage33_progress']=='6/11' and s['execution_gate']['advance_allowed'] is False and s['firewalls']['merge_allowed'] is False
 if a.write: OUT.write_text(json.dumps(s,sort_keys=True,separators=(',',':'))+'\n')
 if a.check or not a.write: print(json.dumps({'success':True,'marker':'V109_V91C1V_AUTHORITY_V91C1AF_DIM5_GROUPED_AUDIT_CHECKPOINT','state_sha256':STATE_SHA,'authority_sha256':AUTH_SHA,'candidate_sha256':AF_SHA,'next_exact_leaf':NEXT,'fixed_dimension_f2':5,'candidate_count':32},sort_keys=True))
if __name__=='__main__': main()
