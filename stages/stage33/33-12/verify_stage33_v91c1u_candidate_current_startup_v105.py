#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent; S33=HERE.parent
STATE=S33/'MAIN-STATE.json'; AUTH=HERE/'e3-v91c1t-a2-02-swap23-pic2-adapter-preflight.json'; CAND=HERE/'e3-v91c1u-a2-02-known140-locator-preflight.json'
STATE_SHA='a1102c55582f9ce09bd19384a881eda2824dad4a2912f2d69bbd0d2dcc6b4713'
AUTH_SHA='6c064cf02fb7a0908242317bf7ac1b20b0586751b78e07b26d6c7889060ffdfa'
CAND_SHA='7480d0d77cc70762cb80e08081f49a5895bb21a46a99dfd699fe63980a977a34'
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p,h):
 o=json.loads(p.read_text()); b=dict(o); q=b.pop('canonical_sha256'); assert q==h==csha(b),p; return o
def main():
 s=load(STATE,STATE_SHA); au=load(AUTH,AUTH_SHA); ca=load(CAND,CAND_SHA)
 assert s['schema']=='STAGE33_MAIN_COMPACT_STATE_V42_V91C1U_KNOWN140_LOCATOR_PREFLIGHT_CANDIDATE_PENDING_HOSTILE_AUDIT'
 assert s['audit_provenance']['current_authority']=='V91C1T_A2_02_SWAP23_PIC2_ADAPTER_PREFLIGHT'
 assert s['audit_provenance']['hostile_audit_review']==5124888078
 assert s['audit_provenance']['exact_audited_head']=='da521c5091f42f4e9f40d71a81f484f232b6a5d5'
 assert s['audit_provenance']['merge_commit']=='f6b1d047dfd238de80ed8f5c267609d01ea1a3bb'
 assert s['candidate_audit_gate']['candidate']=='V91C1U_A2_02_KNOWN140_LOCATOR_PREFLIGHT'
 assert s['candidate_audit_gate']['pr']==1663 and s['candidate_audit_gate']['status']=='PENDING_HOSTILE_AUDIT'
 assert s['execution_gate']['next_expected_command']=='HOSTILE_AUDIT_PR_1663_EXACT_HEAD'
 assert s['execution_gate']['advance_allowed'] is False and s['firewalls']['merge_allowed'] is False
 assert au['canonical_sha256']==AUTH_SHA and ca['canonical_sha256']==CAND_SHA
 assert ca['exact_consequence']['picard64_lattice_reconstruction_is_not_the_current_blocker'] is True
 assert ca['locator_audit']['strict_actual_prime_to_known140_class_index_materialized'] is False
 assert ca['locator_audit']['exceptional_id_to_known140_class_index_materialized'] is False
 assert s['current']['next_exact_leaf']=='V91C1V_SOURCE_LOCK_ACTUAL_PRIME_AND_EXCEPTIONAL_ID_TO_KNOWN140_CLASS_LOCATOR_THEN_APPLY_EXISTING_PICARD64_BRIDGE'
 assert s['stage33_progress']=='6/11'
 print(json.dumps({'success':True,'marker':'V105_V91C1U_CURRENT_STARTUP','state_sha256':STATE_SHA,'authority_sha256':AUTH_SHA,'candidate_sha256':CAND_SHA,'pr':1663,'gate':'PENDING_HOSTILE_AUDIT'},sort_keys=True))
if __name__=='__main__': main()
