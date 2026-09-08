#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ART = ROOT / 'stages/stage32-ex3/ex3-10-main-o210-promotion-adapter-candidate.json'
REG = ROOT / 'stages/stage32/proof/CLAIM-REGISTRY.json'
FR = ROOT / 'stages/stage32/proof/ACTIVE-FRONTIER.json'
EX3_STATE = ROOT / 'stages/stage32-ex3/MAIN-STATE.json'


def bsha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def csha(obj: dict) -> str:
    x = dict(obj)
    x.pop('canonical_sha256_without_this_field', None)
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


a = json.loads(ART.read_text())
assert a['schema'] == 'STAGE32EX3_EX3_10_MAIN_O210_PROMOTION_ADAPTER_V1'
assert a['status'] == 'RETAINED_PROVISIONAL_EX_TO_MAIN_PROMOTION_ADAPTER_UNAUDITED'
assert csha(a) == a['canonical_sha256_without_this_field'] == 'a779f99606c28bbc5b4c5a6a0da72762afc142ab5ccf755b5b22ebeaa6853e05'

for name, lock in a['source_locks'].items():
    p = ROOT / lock['path']
    assert bsha(p) == lock['blob_sha1'], name
    if 'canonical_sha256' in lock:
        assert csha(json.loads(p.read_text())) == lock['canonical_sha256'], name

reg = json.loads(REG.read_text())
by = {c['claim_id']: c for c in reg['claims']}
ex = by['S32.EX3.O210_COVER_GEOMETRY_EXCLUSION_TERMINAL.V1']
assert ex['authority_status'] == 'AUDITED'
assert ex['claim_core_sha256'] == a['binding']['from_claim_core_sha256']
assert ex['scope_key'] == a['binding']['from_scope_key'] == 'S32.EX3.O210_COVER'
assert ex['audit_receipt'] == a['binding']['from_audit_receipt']

ctx = by['S32.MAIN.CURRENT_TARGET_CONTEXT.V1']
assert ctx['claim_core_sha256'] == 'cb3aa4b36332cda9d960103972e7235d3cf7b1bc41fcefc99f19a050a7ab2f14'
assert ctx['scope']['row_id'] == 'g1-d186' and ctx['scope']['picard_class'] == 'V6'
assert ctx['scope']['O'] == 210 and ctx['scope']['qprime'] == 4 and ctx['scope']['Q'] == 602

fr = json.loads(FR.read_text())
goal = next(c for c in fr['claims'] if c['claim_id'] == 'S32.O210.EXCLUSION.V1')
assert goal['claim_core_sha256'] == a['binding']['to_claim_core_sha256']
assert goal['authority_status'] == 'DECLARED_GOAL' and goal['frontier_status'] == 'OPEN_GOAL'
assert goal['scope_key'] == a['binding']['to_scope_key'] == 'S32.O210.COVER'
assert goal['scope'] == {'row_id':'g1-d186','picard_class':'V6','O':210,'qprime':4,'target':'population_wide_exclusion'}

main = json.loads((ROOT / 'stages/stage32/MAIN-STATE.json').read_text())
fixed = main['fixed_target']
assert fixed['row_id'] == 'g1-d186' and fixed['O'] == 210 and fixed['qprime'] == 4 and fixed['Q'] == 602
assert fixed['surviving_residues_decimal'] == [73,97,235]
assert main['firewalls']['O210_excluded'] is False and main['firewalls']['Q602_excluded'] is False

ex3 = json.loads(EX3_STATE.read_text())
assert ex3['fixed_target']['row_id'] == 'g1-d186' and ex3['fixed_target']['picard_class'] == 'V6'
assert ex3['fixed_target']['context_O'] == 210 and ex3['fixed_target']['context_qprime'] == 4 and ex3['fixed_target']['context_Q'] == 602
assert ex3['fixed_target']['context_surviving_residues'] == [73,97,235]
assert ex3['audit']['result'] == 'PASS' and ex3['audit']['review_id'] == 5141988194
assert ex3['frontier']['full_target_closure'] is True and ex3['frontier']['terminal_outcome'] == 'O210_COVER_GEOMETRY_EXCLUDED'
assert ex3['credit']['stage32_main_credit'] is False and ex3['credit']['O210_excluded'] is False and ex3['credit']['Q602_excluded'] is False

term = json.loads((ROOT / a['source_locks']['ex3_terminal_artifact']['path']).read_text())
p = term['population_exhaustiveness']
assert p['population_preserving_from_carrier_hypothesis'] is True
assert p['finite_monodromy_search_used'] is False
assert p['monodromy_or_nielsen_case_choice_enters_argument'] is False
assert term['terminal_proposal']['outcome'] == 'O210_COVER_GEOMETRY_EXCLUDED'

ident = a['target_identity']
assert ident['population_relation'] == 'EQUAL_FOR_CURRENT_TARGET'
assert ident['q602_orbit_role'] == 'OBSTRUCTION_EVIDENCE_NOT_CARRIER_POPULATION_FILTER'
assert ident['q602_trace_gauge_invariant'] is True
assert ident['residual_monodromy_case_restriction_used'] is False
assert ident['finite_search_subpopulation_used'] is False
assert all(a['adapter_argument'].values())

ceil = a['credit_ceiling']
assert ceil['promotion_adapter_retained'] is True and ceil['promotion_adapter_audited'] is False
for k in ['main_O210_claim_promoted','stage32_main_O210_excluded','stage32_main_Q602_excluded','stage32_main_credit','O212_plus_advance_allowed','stage32_closed','endpoint_credit']:
    assert ceil[k] is False, k

print('PASS Stage32EX3 EX3-10 concrete EX3->MAIN O210 population adapter candidate')
print(json.dumps({'from_scope':'S32.EX3.O210_COVER','to_scope':'S32.O210.COVER','population_relation':'EQUAL_FOR_CURRENT_TARGET','adapter_authority':'PROVISIONAL_PENDING_AUDIT','stage32_main_O210_excluded':False}, sort_keys=True))
