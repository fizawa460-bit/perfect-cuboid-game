#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path

H=Path(__file__).resolve().parent
D=H/'33-12'
OUT=H/'MAIN-STATE.json'
CTL=H/'controller.json'
STATE_SHA='2b57eb1e4f62f1c033c70230fd3046d99d5ec60bb0183948eca31bd73054ff5b'
AUTH_SHA='7480d0d77cc70762cb80e08081f49a5895bb21a46a99dfd699fe63980a977a34'
CAND_SHA='60f41e8e324e5fb29d1b109adb860b947308b521f677e49c4965e337a0c2d2d2'
CTL_SHA='02cb0f964086509f8bef4ad4dc5481f9f668b7ca8127f54ebb2952831638f773'
NEXT='V91C1W_SOURCE_BIND_ALL_EIGHT_STRICT_DIVISOR_SCHEMES_TO_PICARD64_CLASSES_OR_DIVISOR_RELATIONS_WITH_EXACT_DECOMPOSITION_EXHAUSTIVITY_AND_MULTIPLICITY_THEN_REDUCE_COMPLETE_SWAP23_DIFFERENCE_MOD2'

def csha(o):
 return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def load(p,h):
 o=json.loads(p.read_text(encoding='utf-8')); b=dict(o); q=b.pop('canonical_sha256')
 assert q==h==csha(b),p
 return o

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--check',action='store_true'); ap.add_argument('--write',action='store_true'); a=ap.parse_args()
 s=load(OUT,STATE_SHA)
 au=load(D/'e3-v91c1u-a2-02-known140-locator-preflight.json',AUTH_SHA)
 ca=load(D/'e3-v91c1v-a2-02-actual-prime-known140-locator-bounded-result.json',CAND_SHA)
 ctl=json.loads(CTL.read_text(encoding='utf-8')); cb=dict(ctl); q=cb.pop('projection_canonical_sha256')
 assert q==CTL_SHA==csha(cb) and ctl['merge_allowed'] is False
 assert s['authority_sync']['frontier_authority']=='V91C1U_A2_02_KNOWN140_LOCATOR_PREFLIGHT'
 ag=s['authority_audit_gate']
 assert ag['pr']==1663 and ag['hostile_audit_review']==5124997953 and ag['hostile_audit_verdict']=='PASS'
 assert ag['exact_audited_head']=='4f9b6643081b32256e7cef2696bfba2dc1ece1b9'
 assert ag['merge_commit']=='f8522bd1a38fa551186ad370f51d17c73c7927e2'
 assert ag['merged'] is True and ag['audit_pass_credit'] is True
 cg=s['candidate_audit_gate']
 assert cg['candidate']=='V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT'
 assert cg['pr']==1667 and cg['status']=='PENDING_HOSTILE_REAUDIT'
 assert cg['hostile_audit_review']==5125492875 and cg['hostile_audit_verdict']=='FAIL'
 assert cg['audit_pass_credit'] is False and cg['merge_allowed'] is False
 assert au['canonical_sha256']==AUTH_SHA and ca['canonical_sha256']==CAND_SHA
 x=ca['exact_result']
 assert x['unique_match_strict_prime_count']==0
 assert x['multi_match_strict_prime_count']==6
 assert x['unmatched_strict_prime_count']==2
 assert x['exceptional_locator_materialized'] is True
 assert x['strict_locator_complete'] is False
 assert x['all_eight_strict_divisor_schemes_source_bound_to_picard64'] is False
 f=s['current_exact_frontier']
 assert f['a2_02_known140_picard64_recovery_materialized'] is True
 assert f['a2_02_swap23_exceptional_id_to_known140_locator_materialized'] is True
 assert f['a2_02_swap23_strict_prime_to_known140_locator_materialized'] is False
 assert f['a2_02_swap23_strict_divisor_scheme_unique_match_count']==0
 assert f['a2_02_swap23_strict_divisor_scheme_multi_match_count']==6
 assert f['a2_02_swap23_strict_divisor_scheme_zero_match_count']==2
 assert f['a2_02_swap23_strict_divisor_scheme_picard64_classes_materialized'] is False
 assert f['a2_02_swap23_actual_divisor_to_retained_picard64_adapter_materialized'] is False
 assert f['pic2_cech_difference_class_computed'] is False
 assert f['a2_02_swap23_seed_fixed_mod_pic2'] is False
 assert f['a2_02_marked_brauer_image_computed'] is False
 assert f['e3_genuine_full_surface_h2_mu2_lift_materialized'] is False
 assert s['current']['next_exact_leaf']==NEXT
 assert s['execution_gate']['next_expected_command']=='HOSTILE_REAUDIT_PR_1667_REPAIRED_EXACT_HEAD'
 assert s['stage33_progress']=='6/11' and s['execution_gate']['advance_allowed'] is False and s['firewalls']['merge_allowed'] is False
 if a.write:
  OUT.write_text(json.dumps(s,sort_keys=True,separators=(',',':'))+'\n',encoding='utf-8')
 if a.check or not a.write:
  print(json.dumps({'success':True,'marker':'V106_V91C1U_AUDITED_MERGED_V91C1V_ROUTE_NARROWING_REPAIRED_PENDING_HOSTILE_REAUDIT','state_sha256':STATE_SHA,'authority_sha256':AUTH_SHA,'candidate_sha256':CAND_SHA,'next_exact_leaf':NEXT},sort_keys=True))

if __name__=='__main__':
 main()
