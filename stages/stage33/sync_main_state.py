#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
H=Path(__file__).resolve().parent; D=H/'33-12'; OUT=H/'MAIN-STATE.json'; CTL=H/'controller.json'
STATE_SHA='8ce9ed3efafba1d40a057f9a1c877c7bb39d5a13d2a53845efc601b222acc2a6'
AUTH_SHA='60f41e8e324e5fb29d1b109adb860b947308b521f677e49c4965e337a0c2d2d2'
W_SHA='e84dcc6692849ff065b0380e760bf725f77fff6754ab5bbdc39b7e608c76a4c7'
X_SHA='aca4d8929f9cc04b24da6e8a7ba0ec0b89be18ac1bc2bf3e6e1f870808bdf29f'
CTL_SHA='02cb0f964086509f8bef4ad4dc5481f9f668b7ca8127f54ebb2952831638f773'
NEXT='V91C1Y_CONSTRAIN_OR_COMPUTE_THE_REMAINING_SWAP23_FIXED_MARKED_BRAUER_IMAGE_WITH_A_SOURCE_BOUND_QUOTIENT_FINGERPRINT_WITHOUT_REINTRODUCING_MASK20'
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p,h):
 o=json.loads(p.read_text()); b=dict(o); q=b.pop('canonical_sha256'); assert q==h==csha(b),p; return o
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--check',action='store_true'); ap.add_argument('--write',action='store_true'); a=ap.parse_args()
 s=load(OUT,STATE_SHA)
 au=load(D/'e3-v91c1v-a2-02-actual-prime-known140-locator-bounded-result.json',AUTH_SHA)
 w=load(D/'e3-v91c1w-a2-02-all8-picard64-reduction.json',W_SHA)
 x=load(D/'e3-v91c1x-a2-02-kummer-naturality-mask20-exclusion.json',X_SHA)
 ctl=json.loads(CTL.read_text()); cb=dict(ctl); q=cb.pop('projection_canonical_sha256'); assert q==CTL_SHA==csha(cb) and ctl['merge_allowed'] is False
 assert s['authority_sync']['frontier_authority']=='V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT'
 assert s['authority_sync']['branch_candidate_frontier']=='V91C1X_A2_02_SWAP23_H2_SEED_FIXED_MASK20_EXCLUDED'
 assert s['authority_sync']['operational_routing_authority']=='V58_ARSENAL_FIRST_REPEATABLE_BOUNDED_SEARCH_NO_FIXED_CAP'
 ag=s['authority_audit_gate']; assert ag['pr']==1667 and ag['hostile_audit_review']==5126709022 and ag['hostile_audit_verdict']=='PASS'
 assert ag['exact_audited_head']=='56ac6b79a4a8e13205a497af1a2cdd6d1e23aee4' and ag['merge_commit']=='bd1f40297f8dcf79e5bb4ef0b8cdc13fdb844177' and ag['merged'] is True
 cg=s['candidate_audit_gate']; assert cg['candidate']=='V91C1X_A2_02_SWAP23_H2_SEED_FIXED_MASK20_EXCLUDED' and cg['pr']==1671 and cg['status']=='PENDING_GROUPED_HOSTILE_AUDIT'
 assert cg['audit_pass_credit'] is False and cg['merge_allowed'] is False
 assert [r['candidate'] for r in cg['accumulated_branch_candidates']]==['V91C1W_A2_02_ALL8_PICARD64_COMPLETE_SWAP23_PIC2_ZERO','V91C1X_A2_02_SWAP23_H2_SEED_FIXED_MASK20_EXCLUDED']
 assert au['canonical_sha256']==AUTH_SHA and w['canonical_sha256']==W_SHA and x['canonical_sha256']==X_SHA
 assert w['exact_result']['pic2_cech_difference_class_computed'] is True and w['exact_result']['complete_swap23_difference_zero_mod2'] is True
 xe=x['exact_consequence']; assert xe['a2_02_swap23_seed_fixed_mod_pic2'] is True and xe['a2_02_marked_brauer_image_excluded_from_mask20'] is True
 assert xe['a2_02_marked_brauer_image_computed'] is False and xe['e3_genuine_full_surface_h2_mu2_lift_materialized'] is False and xe['e3_kummer_column_materialized'] is False
 f=s['current_exact_frontier']; assert f['pic2_cech_difference_class_computed'] is True and f['a2_02_swap23_complete_difference_zero_in_retained_picard_mod2'] is True
 assert f['a2_02_swap23_seed_fixed_mod_pic2'] is True and f['a2_02_marked_brauer_image_excluded_from_mask20'] is True and f['a2_02_marked_brauer_image_computed'] is False
 bp=s['continuation_provenance']['grouped_hostile_audit_policy']; assert bp['same_pr']==1671 and bp['user_authorized_same_pr_noncredit_accumulation'] is True
 assert bp['current_stop_reason']=='MATHEMATICALLY_SUBSTANTIAL_V91C1X_MASK20_EXCLUSION'
 assert s['current']['next_exact_leaf']==NEXT and s['execution_gate']['next_expected_command']=='HOSTILE_AUDIT_PR_1671_GROUPED_V91C1W_X_EXACT_HEAD'
 assert s['stage33_progress']=='6/11' and s['execution_gate']['advance_allowed'] is False and s['firewalls']['merge_allowed'] is False
 if a.write: OUT.write_text(json.dumps(s,sort_keys=True,separators=(',',':'))+'\n')
 if a.check or not a.write: print(json.dumps({'success':True,'marker':'V108_V91C1V_AUTHORITY_V91C1W_X_GROUPED_AUDIT_CHECKPOINT','state_sha256':STATE_SHA,'authority_sha256':AUTH_SHA,'w_sha256':W_SHA,'x_sha256':X_SHA,'next_exact_leaf':NEXT,'mask20_excluded':True},sort_keys=True))
if __name__=='__main__': main()
