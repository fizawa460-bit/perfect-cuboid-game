#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
ART = HERE / 'post1730-o210-v3-main-consumption-preflight.json'
ACTIVE = HERE / 'proof' / 'ACTIVE-FRONTIER.json'
STATE = HERE / 'MAIN-STATE.json'
EXPECTED_CANON = 'b28e95fbeaad0844122fb8fb62722db94cc50ea8cc3130f033a2835d6bd3acd7'
FIXED = {'row_id':'g1-d186','picard_class':'V6','O':210,'qprime':4,'target':'population_wide_exclusion'}

def csha(obj: dict) -> str:
    x=dict(obj); x.pop('canonical_sha256_without_this_field',None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def bsha(data: bytes) -> str:
    return hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()

def canonical(path: Path) -> str:
    obj=json.loads(path.read_text())
    assert csha(obj)==obj['canonical_sha256_without_this_field']
    return obj['canonical_sha256_without_this_field']

a=json.loads(ART.read_text())
assert a['schema']=='STAGE32_POST1730_O210_V3_MAIN_CONSUMPTION_PREFLIGHT_V1'
assert a['status']=='RETAINED_PROVISIONAL_MAIN_O210_V3_CONSUMPTION_PREFLIGHT_AUDIT_REQUIRED'
assert canonical(ART)==EXPECTED_CANON
assert a['upstream_remap_audit']=={
    'pr':1730,'review_id':5148423088,'exact_head':'ceeac85cb70b7765380dd31b210f0b38423fa86c','status':'PASS',
    'scope':'post-1728 V6 negative authority consumption / ACTIVE_FRONTIER_REMAP only'}
chain=a['audited_o210_chain']
assert chain['ex3_terminal']['claim_core_sha256']=='78399b9797723b4134198b2f4b2dc3ed3024897b7ad128d1f0621e1e85cf8102'
assert chain['ex3_terminal']['audit_receipt']=={'status':'PASS','pr':1714,'review_id':5141988194,'exact_head':'8da8d4cd932c5c9b82dfd0c304638e866c656069'}
assert chain['population_adapter']['claim_core_sha256']=='55505658e272ec7d60372f2d67cb93c9c007d782145f18d5ef9d2c1146582c88'
assert chain['population_adapter']['audit_receipt']=={'status':'PASS','pr':1714,'review_id':5143014619,'exact_head':'280595ed892ae2ef70e049a3f722ea024452e206'}
assert chain['main_o210']['claim_core_sha256']=='7003e228cbb0273e1ac6352bd9535a5f10ca5964bc6d4072130d20012aaec824'
assert chain['main_o210']['audit_receipt']=={'status':'PASS','pr':1714,'review_id':5147304889,'exact_head':'040dfb6c7e1dc40573866bb10f62e93419121711'}
for name,lock in a['source_locks'].items():
    p=ROOT/lock['path']; data=p.read_bytes(); assert bsha(data)==lock['blob_sha1'],name
    if 'canonical_sha256' in lock: assert canonical(p)==lock['canonical_sha256'],name
mainv3=json.loads((ROOT/a['source_locks']['main_o210_v3_artifact']['path']).read_text())
assert mainv3['claim_binding']['claim_core_sha256']==chain['main_o210']['claim_core_sha256']
assert mainv3['proof_binding']['ex3_terminal_audit_receipt']==chain['ex3_terminal']['audit_receipt']
assert mainv3['proof_binding']['promotion_adapter_audit_receipt']==chain['population_adapter']['audit_receipt']
active=json.loads(ACTIVE.read_text())
o210=[c for c in active['claims'] if c.get('scope_key')=='S32.O210.COVER']
assert len(o210)==1
assert o210[0]['claim_id']=='S32.O210.EXCLUSION.V1'
assert o210[0]['scope']==FIXED
assert o210[0]['authority_status']=='DECLARED_GOAL'
assert not any(c.get('claim_id')=='S32.O210.EXCLUSION.V3' for c in active['claims'])
state=json.loads(STATE.read_text())
assert state['current_exact_frontier']['o210_excluded'] is False
assert state['current_exact_frontier']['q602_excluded'] is False
assert state['firewalls']['O210_excluded'] is False
assert state['firewalls']['Q602_excluded'] is False
assert a['current_target']['scope_identity'] is True
assert a['current_target']['current_active_o210_scope']==a['current_target']['audited_o210_v3_scope']==FIXED
assert a['transition_contract']['before_hostile_audit']=={'active_o210_claim':'S32.O210.EXCLUSION.V1','main_state_o210_excluded':False,'q602_excluded':False}
assert a['transition_contract']['after_hostile_audit_pass_and_claim_sync_candidate']=={'replace_active_o210_with':'S32.O210.EXCLUSION.V3','main_state_o210_excluded':True,'q602_excluded':False}
assert all(v is False for k,v in a['firewalls'].items() if isinstance(v,bool))
print('PASS_STAGE32_POST1730_O210_V3_MAIN_CONSUMPTION_PREFLIGHT')
print(EXPECTED_CANON)
