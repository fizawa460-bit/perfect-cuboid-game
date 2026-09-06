#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent; S33=HERE.parent
STATE=S33/'MAIN-STATE.json'
AUTH=HERE/'e3-v91c1u-a2-02-known140-locator-preflight.json'
CAND=HERE/'e3-v91c1v-a2-02-actual-prime-known140-locator-bounded-result.json'
STATE_SHA='bfa288ba13fc70f0e55f16139987cd67ca3865742f343b48ce3f0aac403b64bb'
AUTH_SHA='7480d0d77cc70762cb80e08081f49a5895bb21a46a99dfd699fe63980a977a34'
CAND_SHA='555c6d966ebca22536173839fda3100f2ea1fac1c10912b6a45c8833d5c0c293'
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p,h):
 o=json.loads(p.read_text()); b=dict(o); q=b.pop('canonical_sha256'); assert q==h==csha(b),p; return o
def main():
 s=load(STATE,STATE_SHA); au=load(AUTH,AUTH_SHA); ca=load(CAND,CAND_SHA)
 assert s['schema']=='STAGE33_MAIN_COMPACT_STATE_V43_V91C1V_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT_CANDIDATE_PENDING_HOSTILE_AUDIT'
 assert s['audit_provenance']['current_authority']=='V91C1U_A2_02_KNOWN140_LOCATOR_PREFLIGHT'
 assert s['audit_provenance']['hostile_audit_review']==5124997953
 assert s['audit_provenance']['exact_audited_head']=='4f9b6643081b32256e7cef2696bfba2dc1ece1b9'
 assert s['audit_provenance']['merge_commit']=='f8522bd1a38fa551186ad370f51d17c73c7927e2'
 assert s['candidate_audit_gate']['candidate']=='V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT'
 assert s['candidate_audit_gate']['pr']==1667 and s['candidate_audit_gate']['status']=='PENDING_HOSTILE_AUDIT'
 assert s['execution_gate']['next_expected_command']=='HOSTILE_AUDIT_PR_1667_EXACT_HEAD'
 assert s['execution_gate']['advance_allowed'] is False and s['firewalls']['merge_allowed'] is False
 assert au['canonical_sha256']==AUTH_SHA and ca['canonical_sha256']==CAND_SHA
 assert ca['exact_result']['exceptional_locator_materialized'] is True
 assert ca['exact_result']['matched_strict_prime_count']==6
 assert ca['exact_result']['unmatched_strict_prime_count']==2
 assert ca['exact_result']['strict_locator_complete'] is False
 assert s['current']['next_exact_leaf']=='V91C1W_SOURCE_LOCK_TWO_UNMATCHED_STRICT_PRIMES_TO_DIRECT_PICARD64_CLASS_OR_DIVISOR_RELATION_THEN_REDUCE_SWAP23_DIFFERENCE_MOD2'
 assert s['stage33_progress']=='6/11'
 print(json.dumps({'success':True,'marker':'V106_V91C1V_CURRENT_STARTUP','state_sha256':STATE_SHA,'authority_sha256':AUTH_SHA,'candidate_sha256':CAND_SHA,'pr':1667,'gate':'PENDING_HOSTILE_AUDIT'},sort_keys=True))
if __name__=='__main__': main()
