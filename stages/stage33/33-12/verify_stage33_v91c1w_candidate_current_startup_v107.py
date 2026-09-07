#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent; S33=HERE.parent
STATE=S33/'MAIN-STATE.json'; AUTH=HERE/'e3-v91c1v-a2-02-actual-prime-known140-locator-bounded-result.json'; CAND=HERE/'e3-v91c1w-a2-02-all8-picard64-reduction.json'
STATE_SHA='5409ee6e98fa451446d5870dae6c2d7aefdc96f3a2c054d3f57b1b4c41d25f9e'; AUTH_SHA='60f41e8e324e5fb29d1b109adb860b947308b521f677e49c4965e337a0c2d2d2'; CAND_SHA='e84dcc6692849ff065b0380e760bf725f77fff6754ab5bbdc39b7e608c76a4c7'
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p,h):
 o=json.loads(p.read_text()); b=dict(o); q=b.pop('canonical_sha256'); assert q==h==csha(b),p; return o
def main():
 s=load(STATE,STATE_SHA); au=load(AUTH,AUTH_SHA); ca=load(CAND,CAND_SHA)
 assert s['schema']=='STAGE33_MAIN_COMPACT_STATE_V45_V91C1W_ALL8_PICARD64_PIC2_ZERO_CANDIDATE_PENDING_HOSTILE_AUDIT'
 assert s['audit_provenance']['current_authority']=='V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT'
 assert s['audit_provenance']['hostile_audit_review']==5126709022 and s['audit_provenance']['exact_audited_head']=='56ac6b79a4a8e13205a497af1a2cdd6d1e23aee4'
 assert s['audit_provenance']['merge_commit']=='bd1f40297f8dcf79e5bb4ef0b8cdc13fdb844177'
 cg=s['candidate_audit_gate']; assert cg['candidate']=='V91C1W_A2_02_ALL8_PICARD64_COMPLETE_SWAP23_PIC2_ZERO' and cg['pr']==1671 and cg['status']=='PENDING_HOSTILE_AUDIT'
 assert s['execution_gate']['next_expected_command']=='HOSTILE_AUDIT_PR_1671_EXACT_HEAD' and s['execution_gate']['advance_allowed'] is False and s['firewalls']['merge_allowed'] is False
 assert au['canonical_sha256']==AUTH_SHA and ca['canonical_sha256']==CAND_SHA
 assert ca['exact_result']['strict_scheme_picard64_classes_materialized'] is True and ca['exact_result']['pic2_cech_difference_class_computed'] is True and ca['exact_result']['complete_swap23_difference_zero_mod2'] is True
 assert ca['exact_consequence']['a2_02_swap23_seed_fixed_mod_pic2_promoted'] is False and ca['exact_consequence']['a2_02_marked_brauer_image_excluded_from_mask20'] is False
 assert s['stage33_progress']=='6/11'
 print(json.dumps({'success':True,'marker':'V107_V91C1W_CURRENT_STARTUP','state_sha256':STATE_SHA,'authority_sha256':AUTH_SHA,'candidate_sha256':CAND_SHA,'pr':1671,'gate':'PENDING_HOSTILE_AUDIT','complete_difference_zero_mod2':True,'seed_fixedness_promoted':False},sort_keys=True))
if __name__=='__main__': main()
