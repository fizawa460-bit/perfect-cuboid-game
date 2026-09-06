#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent; S33=HERE.parent
STATE=S33/'MAIN-STATE.json'
AUTH=HERE/'e3-v91c1u-a2-02-known140-locator-preflight.json'
CAND=HERE/'e3-v91c1v-a2-02-actual-prime-known140-locator-bounded-result.json'
STATE_SHA='2b57eb1e4f62f1c033c70230fd3046d99d5ec60bb0183948eca31bd73054ff5b'
AUTH_SHA='7480d0d77cc70762cb80e08081f49a5895bb21a46a99dfd699fe63980a977a34'
CAND_SHA='60f41e8e324e5fb29d1b109adb860b947308b521f677e49c4965e337a0c2d2d2'
NEXT='V91C1W_SOURCE_BIND_ALL_EIGHT_STRICT_DIVISOR_SCHEMES_TO_PICARD64_CLASSES_OR_DIVISOR_RELATIONS_WITH_EXACT_DECOMPOSITION_EXHAUSTIVITY_AND_MULTIPLICITY_THEN_REDUCE_COMPLETE_SWAP23_DIFFERENCE_MOD2'
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p,h):
 o=json.loads(p.read_text()); b=dict(o); q=b.pop('canonical_sha256'); assert q==h==csha(b),p; return o
def main():
 s=load(STATE,STATE_SHA); au=load(AUTH,AUTH_SHA); ca=load(CAND,CAND_SHA)
 assert s['schema']=='STAGE33_MAIN_COMPACT_STATE_V44_V91C1V_ROUTE_NARROWING_REPAIRED_PENDING_HOSTILE_REAUDIT'
 assert s['audit_provenance']['current_authority']=='V91C1U_A2_02_KNOWN140_LOCATOR_PREFLIGHT'
 assert s['audit_provenance']['hostile_audit_review']==5124997953
 assert s['audit_provenance']['exact_audited_head']=='4f9b6643081b32256e7cef2696bfba2dc1ece1b9'
 assert s['audit_provenance']['merge_commit']=='f8522bd1a38fa551186ad370f51d17c73c7927e2'
 assert s['candidate_audit_gate']['candidate']=='V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT'
 assert s['candidate_audit_gate']['pr']==1667
 assert s['candidate_audit_gate']['hostile_audit_review']==5125492875
 assert s['candidate_audit_gate']['hostile_audit_verdict']=='FAIL'
 assert s['candidate_audit_gate']['status']=='PENDING_HOSTILE_REAUDIT'
 assert s['execution_gate']['next_expected_command']=='HOSTILE_REAUDIT_PR_1667_REPAIRED_EXACT_HEAD'
 assert s['execution_gate']['advance_allowed'] is False and s['firewalls']['merge_allowed'] is False
 assert au['canonical_sha256']==AUTH_SHA and ca['canonical_sha256']==CAND_SHA
 x=ca['exact_result']
 assert x['exceptional_locator_materialized'] is True
 assert x['unique_match_strict_prime_count']==0
 assert x['multi_match_strict_prime_count']==6
 assert x['unmatched_strict_prime_count']==2
 assert x['all_eight_strict_divisor_schemes_source_bound_to_picard64'] is False
 assert x['strict_locator_complete'] is False
 f=s['current_exact_frontier']
 assert f['a2_02_swap23_strict_divisor_scheme_unique_match_count']==0
 assert f['a2_02_swap23_strict_divisor_scheme_multi_match_count']==6
 assert f['a2_02_swap23_strict_divisor_scheme_zero_match_count']==2
 assert f['a2_02_swap23_strict_divisor_scheme_picard64_classes_materialized'] is False
 assert s['current']['next_exact_leaf']==NEXT
 assert s['stage33_progress']=='6/11'
 print(json.dumps({'success':True,'marker':'V106_V91C1V_REPAIRED_CURRENT_STARTUP','state_sha256':STATE_SHA,'authority_sha256':AUTH_SHA,'candidate_sha256':CAND_SHA,'pr':1667,'gate':'PENDING_HOSTILE_REAUDIT','unique':0,'multi_match':6,'zero_match':2},sort_keys=True))
if __name__=='__main__': main()
