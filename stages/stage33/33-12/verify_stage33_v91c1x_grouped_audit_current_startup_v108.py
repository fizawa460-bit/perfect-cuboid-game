#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path
HERE=Path(__file__).resolve().parent; S33=HERE.parent
STATE=S33/'MAIN-STATE.json'; AUTH=HERE/'e3-v91c1v-a2-02-actual-prime-known140-locator-bounded-result.json'
W=HERE/'e3-v91c1w-a2-02-all8-picard64-reduction.json'; X=HERE/'e3-v91c1x-a2-02-kummer-naturality-mask20-exclusion.json'
STATE_SHA='8ce9ed3efafba1d40a057f9a1c877c7bb39d5a13d2a53845efc601b222acc2a6'; AUTH_SHA='60f41e8e324e5fb29d1b109adb860b947308b521f677e49c4965e337a0c2d2d2'
W_SHA='e84dcc6692849ff065b0380e760bf725f77fff6754ab5bbdc39b7e608c76a4c7'; X_SHA='aca4d8929f9cc04b24da6e8a7ba0ec0b89be18ac1bc2bf3e6e1f870808bdf29f'
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p,h):
 o=json.loads(p.read_text()); b=dict(o); q=b.pop('canonical_sha256'); assert q==h==csha(b),p; return o
def main():
 s=load(STATE,STATE_SHA); au=load(AUTH,AUTH_SHA); w=load(W,W_SHA); x=load(X,X_SHA)
 assert s['schema']=='STAGE33_MAIN_COMPACT_STATE_V46_V91C1W_X_GROUPED_AUDIT_CHECKPOINT'
 assert s['audit_provenance']['current_authority']=='V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT'
 assert s['audit_provenance']['hostile_audit_review']==5126709022 and s['audit_provenance']['exact_audited_head']=='56ac6b79a4a8e13205a497af1a2cdd6d1e23aee4'
 cg=s['candidate_audit_gate']; assert cg['candidate']=='V91C1X_A2_02_SWAP23_H2_SEED_FIXED_MASK20_EXCLUDED' and cg['pr']==1671 and cg['status']=='PENDING_GROUPED_HOSTILE_AUDIT'
 assert s['execution_gate']['next_expected_command']=='HOSTILE_AUDIT_PR_1671_GROUPED_V91C1W_X_EXACT_HEAD' and s['execution_gate']['advance_allowed'] is False and s['firewalls']['merge_allowed'] is False
 assert au['canonical_sha256']==AUTH_SHA and w['canonical_sha256']==W_SHA and x['canonical_sha256']==X_SHA
 assert w['exact_result']['complete_swap23_difference_zero_mod2'] is True
 assert x['exact_consequence']['a2_02_swap23_seed_fixed_mod_pic2'] is True
 assert x['exact_consequence']['a2_02_marked_brauer_image_excluded_from_mask20'] is True
 assert x['exact_consequence']['a2_02_marked_brauer_image_computed'] is False
 bp=s['continuation_provenance']['grouped_hostile_audit_policy']; assert bp['user_authorized_same_pr_noncredit_accumulation'] is True and bp['current_stop_reason']=='MATHEMATICALLY_SUBSTANTIAL_V91C1X_MASK20_EXCLUSION'
 assert s['stage33_progress']=='6/11'
 print(json.dumps({'success':True,'marker':'V108_V91C1X_GROUPED_AUDIT_CURRENT_STARTUP','state_sha256':STATE_SHA,'authority_sha256':AUTH_SHA,'w_sha256':W_SHA,'x_sha256':X_SHA,'pr':1671,'gate':'PENDING_GROUPED_HOSTILE_AUDIT','seed_fixedness_promoted':True,'mask20_excluded':True,'actual_marked_image_computed':False},sort_keys=True))
if __name__=='__main__': main()
