#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
PKG=ROOT/'stages/stage32/q602-forgetful-adapter-audit-package-20260909.json'
BUNDLE=ROOT/'stages/stage32/scratch/q602-o210-versioned-claim-bundle-20260909.json'
ACTIVE=ROOT/'stages/stage32/proof/ACTIVE-FRONTIER.json'
STATE=ROOT/'stages/stage32/MAIN-STATE.json'

def blob_sha1(data:bytes)->str:
    return hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()
def canon(o:dict)->str:
    x=dict(o); x.pop('canonical_sha256_without_this_field',None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def main():
    p=json.loads(PKG.read_text()); b=json.loads(BUNDLE.read_text()); a=json.loads(ACTIVE.read_text()); s=json.loads(STATE.read_text())
    assert p['schema']=='STAGE32_Q602_FORGETFUL_ADAPTER_RETAINED_AUDIT_PACKAGE_V1'
    assert p['status']=='PROVISIONAL_RETAINED_AUDIT_CANDIDATE_NO_AUTHORITY'
    assert p['prerequisite_o210_post_sync_audit']=={'status':'PASS','pr':1730,'review_id':5149127765,'exact_head':'f11c8c3cb402e2ec50fccf264c0fb71f56d157f9'}
    assert p['adapter_claim_core_sha256']=='ed1ea5441a3b0bb876a3a8b93f272e2a16d693f1b44f0f050c13af1625c1e028'
    assert p['q602_claim_core_sha256']=='f27890319709b9ee24a71e744990c9c5fb36d746cacb7bd8ee11a905bfc9750e'
    assert b['canonical_sha256_without_this_field']=='9ce14c2d619685ab9c22a83ccd36cc1b085bf1579132df7b0c0b2b4b1122ba07'
    assert canon(b)==b['canonical_sha256_without_this_field']
    assert b['adapter_claim']['claim_core_sha256']==p['adapter_claim_core_sha256']
    assert b['q602_exclusion_claim']['claim_core_sha256']==p['q602_claim_core_sha256']
    for lock in p['source_locks']:
        q=ROOT/lock['path']; data=q.read_bytes(); assert blob_sha1(data)==lock['blob_sha1'],lock['path']
        o=json.loads(data); assert o['canonical_sha256_without_this_field']==lock['canonical_sha256']; assert canon(o)==lock['canonical_sha256']
    claims={c['claim_id']:c for c in a.get('supporting_claims',[])+a['claims']}
    assert claims['S32.O210.EXCLUSION.V3']['authority_status']=='AUDITED'
    assert claims['S32.O210.EXCLUSION.V3']['claim_core_sha256']=='7003e228cbb0273e1ac6352bd9535a5f10ca5964bc6d4072130d20012aaec824'
    assert claims['S32.Q602.EXCLUSION.V1']['authority_status']=='DECLARED_GOAL'
    assert 'S32.Q602.EXCLUSION.V2' not in claims
    assert 'S32.ADAPTER.Q602_ADMISSIBLE_TO_O210_POPULATION.V1' not in claims
    f=s['current_exact_frontier']
    assert f['o210_excluded'] is True
    assert f['q602_excluded'] is False
    assert f['q602_survivors_audited']==[73,97,235]
    assert s['firewalls']['O212_plus_advance_allowed'] is False
    assert all(v is False for v in p['authority_firewalls'].values())
    subprocess.run(['python','stages/stage32/scratch/verify_q602_o210_forgetful_adapter_preflight_20260909.py'],cwd=ROOT,check=True)
    subprocess.run(['python','stages/stage32/scratch/verify_q602_o210_forgetful_adapter_post1500_origin_20260909.py'],cwd=ROOT,check=True)
    subprocess.run(['python','stages/stage32/scratch/verify_q602_o210_versioned_claim_bundle_20260909.py'],cwd=ROOT,check=True)
    print('PASS_STAGE32_Q602_FORGETFUL_ADAPTER_RETAINED_AUDIT_PACKAGE')
    print('authority_change=false')
if __name__=='__main__': main()
