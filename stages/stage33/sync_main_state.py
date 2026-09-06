#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
H=Path(__file__).resolve().parent; D=H/'33-12'; OUT=H/'MAIN-STATE.json'; CTL=H/'controller.json'
STATE_SHA='5409ee6e98fa451446d5870dae6c2d7aefdc96f3a2c054d3f57b1b4c41d25f9e'
AUTH_SHA='60f41e8e324e5fb29d1b109adb860b947308b521f677e49c4965e337a0c2d2d2'
CAND_SHA='e84dcc6692849ff065b0380e760bf725f77fff6754ab5bbdc39b7e608c76a4c7'
CTL_SHA='02cb0f964086509f8bef4ad4dc5481f9f668b7ca8127f54ebb2952831638f773'
NEXT='V91C1X_SOURCE_LOCK_ZERO_COMPLETE_SWAP23_PICARD2_DIFFERENCE_TO_LITERAL_FULL_CECH_CARTIER_H2_MU2_SEED_FIXEDNESS_THEN_APPLY_NATURALITY_MASK20_EXCLUSION'
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p,h):
 o=json.loads(p.read_text()); b=dict(o); q=b.pop('canonical_sha256'); assert q==h==csha(b),p; return o
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--check',action='store_true'); ap.add_argument('--write',action='store_true'); a=ap.parse_args()
 s=load(OUT,STATE_SHA); au=load(D/'e3-v91c1v-a2-02-actual-prime-known140-locator-bounded-result.json',AUTH_SHA); ca=load(D/'e3-v91c1w-a2-02-all8-picard64-reduction.json',CAND_SHA)
 ctl=json.loads(CTL.read_text()); cb=dict(ctl); q=cb.pop('projection_canonical_sha256'); assert q==CTL_SHA==csha(cb) and ctl['merge_allowed'] is False
 assert s['authority_sync']['frontier_authority']=='V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT'
 ag=s['authority_audit_gate']; assert ag['pr']==1667 and ag['hostile_audit_review']==5126709022 and ag['hostile_audit_verdict']=='PASS'
 assert ag['exact_audited_head']=='56ac6b79a4a8e13205a497af1a2cdd6d1e23aee4' and ag['merge_commit']=='bd1f40297f8dcf79e5bb4ef0b8cdc13fdb844177' and ag['merged'] is True
 cg=s['candidate_audit_gate']; assert cg['candidate']=='V91C1W_A2_02_ALL8_PICARD64_COMPLETE_SWAP23_PIC2_ZERO' and cg['pr']==1671 and cg['status']=='PENDING_HOSTILE_AUDIT'
 assert cg['audit_pass_credit'] is False and cg['merge_allowed'] is False
 assert au['canonical_sha256']==AUTH_SHA and ca['canonical_sha256']==CAND_SHA
 x=ca['exact_result']; assert x['strict_scheme_count']==8 and x['strict_scheme_picard64_classes_materialized'] is True
 assert x['multi_match_exact_decomposition_count']==6 and x['zero_match_direct_relation_count']==2 and x['all_eight_exact_decomposition_or_source_bound_relation'] is True
 assert x['pic2_cech_difference_class_computed'] is True and x['complete_swap23_difference_zero_mod2'] is True and x['complete_swap23_difference_mod2_support_one_based']==[]
 f=s['current_exact_frontier']; assert f['a2_02_swap23_strict_divisor_scheme_picard64_classes_materialized'] is True and f['a2_02_swap23_actual_divisor_to_retained_picard64_adapter_materialized'] is True
 assert f['pic2_cech_difference_class_computed'] is True and f['a2_02_swap23_complete_difference_zero_in_retained_picard_mod2'] is True
 assert f['a2_02_swap23_seed_fixed_mod_pic2'] is False and f['a2_02_marked_brauer_image_computed'] is False and f['a2_02_marked_brauer_image_excluded_from_mask20'] is False
 assert s['current']['next_exact_leaf']==NEXT and s['execution_gate']['next_expected_command']=='HOSTILE_AUDIT_PR_1671_EXACT_HEAD'
 assert s['stage33_progress']=='6/11' and s['execution_gate']['advance_allowed'] is False and s['firewalls']['merge_allowed'] is False
 if a.write: OUT.write_text(json.dumps(s,sort_keys=True,separators=(',',':'))+'\n')
 if a.check or not a.write: print(json.dumps({'success':True,'marker':'V107_V91C1V_REAUDITED_MERGED_V91C1W_ALL8_PICARD64_PIC2_ZERO_PENDING_HOSTILE_AUDIT','state_sha256':STATE_SHA,'authority_sha256':AUTH_SHA,'candidate_sha256':CAND_SHA,'next_exact_leaf':NEXT},sort_keys=True))
if __name__=='__main__': main()
