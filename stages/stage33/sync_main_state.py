#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path

H=Path(__file__).resolve().parent
D=H/'33-12'
OUT=H/'MAIN-STATE.json'
CTL=H/'controller.json'
STATE_SHA='bfa288ba13fc70f0e55f16139987cd67ca3865742f343b48ce3f0aac403b64bb'
AUTH_SHA='7480d0d77cc70762cb80e08081f49a5895bb21a46a99dfd699fe63980a977a34'
CAND_SHA='555c6d966ebca22536173839fda3100f2ea1fac1c10912b6a45c8833d5c0c293'
CTL_SHA='02cb0f964086509f8bef4ad4dc5481f9f668b7ca8127f54ebb2952831638f773'

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
 assert cg['pr']==1667 and cg['status']=='PENDING_HOSTILE_AUDIT'
 assert cg['audit_pass_credit'] is False and cg['merge_allowed'] is False
 assert au['canonical_sha256']==AUTH_SHA and ca['canonical_sha256']==CAND_SHA
 assert ca['exact_result']['matched_strict_prime_count']==6
 assert ca['exact_result']['unmatched_strict_prime_count']==2
 assert ca['exact_result']['exceptional_locator_materialized'] is True
 assert ca['exact_result']['strict_locator_complete'] is False
 f=s['current_exact_frontier']
 assert f['a2_02_known140_picard64_recovery_materialized'] is True
 assert f['a2_02_swap23_exceptional_id_to_known140_locator_materialized'] is True
 assert f['a2_02_swap23_strict_prime_to_known140_locator_materialized'] is False
 assert f['a2_02_swap23_strict_prime_partial_locator_matched_count']==6
 assert f['a2_02_swap23_strict_prime_unmatched_count_among_pinned_92_known_curves']==2
 assert f['a2_02_swap23_actual_divisor_to_retained_picard64_adapter_materialized'] is False
 assert f['pic2_cech_difference_class_computed'] is False
 assert f['a2_02_swap23_seed_fixed_mod_pic2'] is False
 assert f['a2_02_marked_brauer_image_computed'] is False
 assert f['e3_genuine_full_surface_h2_mu2_lift_materialized'] is False
 assert s['stage33_progress']=='6/11' and s['execution_gate']['advance_allowed'] is False and s['firewalls']['merge_allowed'] is False
 if a.write:
  OUT.write_text(json.dumps(s,sort_keys=True,separators=(',',':'))+'\n',encoding='utf-8')
 if a.check or not a.write:
  print(json.dumps({'success':True,'marker':'V106_V91C1U_AUDITED_MERGED_V91C1V_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT_PENDING_HOSTILE_AUDIT','state_sha256':STATE_SHA,'authority_sha256':AUTH_SHA,'candidate_sha256':CAND_SHA,'next_exact_leaf':s['current']['next_exact_leaf']},sort_keys=True))

if __name__=='__main__':
 main()
