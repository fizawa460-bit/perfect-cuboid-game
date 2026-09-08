#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ART = ROOT / 'stages/stage32-ex3/main-o210-exclusion-v2-candidate.json'
REG = ROOT / 'stages/stage32/proof/CLAIM-REGISTRY.json'
ACTIVE = ROOT / 'stages/stage32/proof/ACTIVE-FRONTIER.json'
STATE = ROOT / 'stages/stage32-ex3/MAIN-STATE.json'

CID='S32.O210.EXCLUSION.V2'
OLD='S32.O210.EXCLUSION.V1'
CTX='S32.MAIN.CURRENT_TARGET_CONTEXT.V1'
EX3='S32.EX3.O210_COVER_GEOMETRY_EXCLUSION_TERMINAL.V1'
V3='S32.ADAPTER.EX3_O210_TO_MAIN_O210.V3'
CORE='178c0a8a381abacbfb5662f44f2faab2f2f6076f4be653172f7e586f77476746'
CORE_KEYS=['claim_id','kind','statement','scope_key','scope','proves','does_not_prove','requires','source_locks','replay_verifier']
FIXED={'row_id':'g1-d186','picard_class':'V6','O':210,'qprime':4,'target':'population_wide_exclusion'}

def csha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def bsha(data:bytes):
    return hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()

def canonical(path:Path):
    obj=json.loads(path.read_text())
    stored=obj['canonical_sha256_without_this_field']
    stripped=dict(obj); stripped.pop('canonical_sha256_without_this_field',None)
    assert csha(stripped)==stored
    return stored

a=json.loads(ART.read_text())
assert a['schema']=='STAGE32_MAIN_O210_EXCLUSION_V2_CANDIDATE_V1'
assert a['status']=='RETAINED_PROVISIONAL_MAIN_O210_EXCLUSION_V2_AUDIT_PENDING'
assert canonical(ART)=='82dc2bd52765d28d82f0ddf5d3105af64ee571878bd708b901b97899eb5d558a'
for name,lock in a['source_locks'].items():
    p=ROOT/lock['path']; data=p.read_bytes()
    assert bsha(data)==lock['blob_sha1'], name
    if 'canonical_sha256' in lock:
        assert canonical(p)==lock['canonical_sha256'], name

reg=json.loads(REG.read_text())
by={c['claim_id']:c for c in reg['claims']}
assert by[CTX]['claim_core_sha256']==a['proof_binding']['target_context_core_sha256']
assert by[EX3]['authority_status']=='AUDITED'
assert by[EX3]['claim_core_sha256']==a['proof_binding']['ex3_terminal_core_sha256']
assert by[EX3]['audit_receipt']==a['proof_binding']['ex3_terminal_audit_receipt']
assert by[V3]['authority_status']=='AUDITED'
assert by[V3]['claim_core_sha256']==a['proof_binding']['promotion_adapter_core_sha256']
assert by[V3]['audit_receipt']==a['proof_binding']['promotion_adapter_audit_receipt']
assert by[OLD]['authority_status']=='SUPERSEDED'
assert by[OLD]['claim_core_sha256']=='38124e42fde826b6e3abf89b945d3633edf29cad9ccc21ad2140b99b77727d6c'

active=json.loads(ACTIVE.read_text())
claims={c['claim_id']:c for c in active['claims']}
assert OLD not in claims
assert CID in claims
c=claims[CID]
assert c['kind']=='mathematical_claim'
assert c['scope_key']=='S32.O210.COVER' and c['scope']==FIXED
assert c['requires']==[CTX,EX3,V3]
assert c['lane_links']==[{'lane':'MAIN','role':'OWNER'},{'lane':'EX3','role':'ATTACKS'}]
assert c['replay_verifier']=='stages/stage32-ex3/verify_main_o210_exclusion_v2_candidate.py'
assert c['claim_core_sha256']==CORE==csha({k:c[k] for k in CORE_KEYS})
assert c['authority_status'] in {'PROVISIONAL','AUDITED'}
if c['authority_status']=='PROVISIONAL':
    assert c['audit_receipt'] is None
    assert c['frontier_status']=='ACTIVE_INCOMPLETE'
    assert c['blockers']==['Hostile audit of the explicit MAIN O210 V2 claim has not yet been performed.']
else:
    assert c['audit_receipt']['status']=='PASS'
    assert c['frontier_status']=='AUDITED_TRUE'
    assert c['blockers']==[]
for lock in c['source_locks']:
    assert lock['path'] not in {'stages/stage32/MAIN-STATE.json','stages/stage32/proof/ACTIVE-FRONTIER.json','stages/stage32-ex3/MAIN-STATE.json'}

state=json.loads(STATE.read_text())
for key in ['stage32_main_credit','Q602_excluded','O210_excluded','receiver_credit','theorem_credit','endpoint_credit']:
    assert state['credit'][key] is False
for key in ['stage32_main_credit','Q602_excluded','O210_excluded','O212_plus_advance_allowed','stage32_closed']:
    assert state['firewalls'][key] is False

print('PASS Stage32 MAIN O210 exclusion V2 candidate')
print(json.dumps({'claim_id':CID,'claim_core_sha256':CORE,'authority':c['authority_status'],'frontier_status':c['frontier_status'],'main_O210_credit':False},sort_keys=True))
