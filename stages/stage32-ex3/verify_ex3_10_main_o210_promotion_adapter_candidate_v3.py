#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ART = ROOT / 'stages/stage32-ex3/ex3-10-main-o210-promotion-adapter-candidate-v3.json'
REG = ROOT / 'stages/stage32/proof/CLAIM-REGISTRY.json'
ACTIVE = ROOT / 'stages/stage32/proof/ACTIVE-FRONTIER.json'

CID = 'S32.ADAPTER.EX3_O210_TO_MAIN_O210.V3'
CTX = 'S32.MAIN.CURRENT_TARGET_CONTEXT.V1'
EX3 = 'S32.EX3.O210_COVER_GEOMETRY_EXCLUSION_TERMINAL.V1'
CORE_KEYS = ['claim_id','kind','statement','scope_key','scope','proves','does_not_prove','requires','bridges','source_locks','replay_verifier']
FIXED_SCOPE = {'row_id':'g1-d186','picard_class':'V6','O':210,'qprime':4,'target':'population_wide_exclusion'}


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()


def canonical_file(path: Path) -> str:
    obj = json.loads(path.read_text())
    stored = obj['canonical_sha256_without_this_field']
    stripped = dict(obj)
    stripped.pop('canonical_sha256_without_this_field', None)
    assert csha(stripped) == stored
    return stored


a = json.loads(ART.read_text())
assert a['schema'] == 'STAGE32EX3_EX3_10_MAIN_O210_PROMOTION_ADAPTER_V3'
assert a['status'] == 'RETAINED_PROVISIONAL_EX_TO_MAIN_PROMOTION_ADAPTER_V3_UNAUDITED'
assert canonical_file(ART) == '63dc72b89f59709fcce13cbc4e9c777819a419f7b6213a6ccd2c7c5977fce37c'
for name, lock in a['source_locks'].items():
    p = ROOT / lock['path']
    data = p.read_bytes()
    assert git_blob_sha1(data) == lock['blob_sha1'], name
    if 'canonical_sha256' in lock:
        assert canonical_file(p) == lock['canonical_sha256'], name

reg = json.loads(REG.read_text())
by = {c['claim_id']: c for c in reg['claims']}
ctx = by[CTX]
assert ctx['claim_core_sha256'] == a['binding']['stage32_target_context_core_sha256']
assert ctx['scope']['row_id'] == 'g1-d186' and ctx['scope']['picard_class'] == 'V6'
assert ctx['scope']['O'] == 210 and ctx['scope']['qprime'] == 4 and ctx['scope']['Q'] == 602
ex = by[EX3]
assert ex['authority_status'] == 'AUDITED'
assert ex['claim_core_sha256'] == a['binding']['from_claim_core_sha256']
assert ex['audit_receipt'] == a['binding']['from_audit_receipt']

# Runtime target check: do not source-lock the mutable ACTIVE-FRONTIER blob.
active = json.loads(ACTIVE.read_text())
o210 = [c for c in active['claims'] if c.get('scope_key') == 'S32.O210.COVER' and c.get('scope') == FIXED_SCOPE]
assert len(o210) == 1
assert o210[0]['kind'] == 'mathematical_claim'
assert o210[0]['lane_links'] == [{'lane':'MAIN','role':'OWNER'},{'lane':'EX3','role':'ATTACKS'}]

if CID in by:
    claim = by[CID]
    assert claim['kind'] == 'adapter_contract'
    assert claim['scope_key'] == 'S32.ADAPTER.EX3_O210_TO_MAIN_O210'
    assert claim['bridges']['from_scope_key'] == 'S32.EX3.O210_COVER'
    assert claim['bridges']['to_scope_key'] == 'S32.O210.COVER'
    assert claim['requires'] == [CTX, EX3]
    assert claim['replay_verifier'] == 'stages/stage32-ex3/verify_ex3_10_main_o210_promotion_adapter_candidate_v3.py'
    forbidden = {'stages/stage32/MAIN-STATE.json','stages/stage32/proof/ACTIVE-FRONTIER.json'}
    assert not (forbidden & {x['path'] for x in claim['source_locks']})
    expected = csha({k:claim[k] for k in CORE_KEYS})
    assert claim['claim_core_sha256'] == expected
    assert claim['authority_status'] in {'PROVISIONAL','AUDITED'}
    if claim['authority_status'] == 'PROVISIONAL':
        assert claim['audit_receipt'] is None
    else:
        assert claim['audit_receipt']['status'] == 'PASS'

fresh = a['freshness_design']
assert fresh['repository_main_sha_is_semantic_binding'] is False
assert fresh['stage32_main_state_blob_is_direct_source_lock'] is False
assert fresh['active_frontier_blob_is_direct_source_lock'] is False
assert fresh['active_frontier_may_remap_claim_version_if_scope_and_target_context_are_preserved'] is True
assert fresh['target_context_claim_core_is_semantic_binding'] is True
assert fresh['exact_current_active_o210_scope_is_runtime_verified'] is True

ident = a['target_identity']
assert ident['population_relation'] == 'EQUAL_FOR_BOUND_STAGE32_TARGET_CONTEXT'
assert ident['q602_orbit_role'] == 'OBSTRUCTION_EVIDENCE_NOT_CARRIER_POPULATION_FILTER'
assert ident['q602_trace_gauge_invariant'] is True
assert ident['finite_search_subpopulation_used'] is False
assert ident['residual_monodromy_case_restriction_used'] is False

print('PASS Stage32EX3 EX3-10 drift-robust promotion adapter V3 candidate')
print(json.dumps({'active_o210_claim_id':o210[0]['claim_id'],'from_scope':'S32.EX3.O210_COVER','to_scope':'S32.O210.COVER','mutable_frontier_blob_locked':False,'authority':by.get(CID,{}).get('authority_status','UNREGISTERED')}, sort_keys=True))
