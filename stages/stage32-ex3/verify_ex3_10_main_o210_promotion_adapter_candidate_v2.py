#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ART = ROOT / 'stages/stage32-ex3/ex3-10-main-o210-promotion-adapter-candidate-v2.json'
REG = ROOT / 'stages/stage32/proof/CLAIM-REGISTRY.json'
FR = ROOT / 'stages/stage32/proof/ACTIVE-FRONTIER.json'


def bsha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def csha(obj: dict) -> str:
    x = dict(obj)
    x.pop('canonical_sha256_without_this_field', None)
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


a = json.loads(ART.read_text())
assert a['schema'] == 'STAGE32EX3_EX3_10_MAIN_O210_PROMOTION_ADAPTER_V2'
assert a['status'] == 'RETAINED_PROVISIONAL_EX_TO_MAIN_PROMOTION_ADAPTER_V2_UNAUDITED'
assert a['binding']['binding_semantics'] == 'STAGE32_TARGET_CONTEXT_CORE_PLUS_EXACT_MAIN_STATE_BLOB'
assert csha(a) == a['canonical_sha256_without_this_field'] == 'ab5b734ec3ffbac2364f9762903294ae1c76c955cc4c89febd557dd92055050a'

for name, lock in a['source_locks'].items():
    p = ROOT / lock['path']
    assert bsha(p) == lock['blob_sha1'], name
    if 'canonical_sha256' in lock:
        assert csha(json.loads(p.read_text())) == lock['canonical_sha256'], name

reg = json.loads(REG.read_text())
by = {c['claim_id']: c for c in reg['claims']}
ctx = by['S32.MAIN.CURRENT_TARGET_CONTEXT.V1']
assert ctx['claim_core_sha256'] == a['binding']['stage32_target_context_core_sha256'] == 'cb3aa4b36332cda9d960103972e7235d3cf7b1bc41fcefc99f19a050a7ab2f14'
assert ctx['scope']['row_id'] == 'g1-d186' and ctx['scope']['picard_class'] == 'V6'
assert ctx['scope']['O'] == 210 and ctx['scope']['qprime'] == 4 and ctx['scope']['Q'] == 602

main = json.loads((ROOT / 'stages/stage32/MAIN-STATE.json').read_text())
assert bsha(ROOT / 'stages/stage32/MAIN-STATE.json') == a['binding']['stage32_main_state_blob_sha1'] == '05e2942b4c893044688f16926b5e9837e59d8e9d'
fixed = main['fixed_target']
assert fixed['row_id'] == 'g1-d186' and fixed['O'] == 210 and fixed['qprime'] == 4 and fixed['Q'] == 602
assert fixed['surviving_residues_decimal'] == [73, 97, 235]
assert main['firewalls']['O210_excluded'] is False
assert main['firewalls']['Q602_excluded'] is False

ex = by['S32.EX3.O210_COVER_GEOMETRY_EXCLUSION_TERMINAL.V1']
assert ex['authority_status'] == 'AUDITED'
assert ex['claim_core_sha256'] == a['binding']['from_claim_core_sha256'] == '78399b9797723b4134198b2f4b2dc3ed3024897b7ad128d1f0621e1e85cf8102'
assert ex['scope_key'] == a['binding']['from_scope_key'] == 'S32.EX3.O210_COVER'
assert ex['audit_receipt'] == a['binding']['from_audit_receipt']

fr = json.loads(FR.read_text())
goal = next(c for c in fr['claims'] if c['claim_id'] == 'S32.O210.EXCLUSION.V1')
assert goal['claim_core_sha256'] == a['binding']['to_claim_core_sha256'] == '38124e42fde826b6e3abf89b945d3633edf29cad9ccc21ad2140b99b77727d6c'
assert goal['scope_key'] == a['binding']['to_scope_key'] == 'S32.O210.COVER'
assert goal['authority_status'] == 'DECLARED_GOAL' and goal['frontier_status'] == 'OPEN_GOAL'
assert goal['scope'] == {'row_id':'g1-d186','picard_class':'V6','O':210,'qprime':4,'target':'population_wide_exclusion'}

term = json.loads((ROOT / a['source_locks']['ex3_terminal_artifact']['path']).read_text())
p = term['population_exhaustiveness']
assert p['population_preserving_from_carrier_hypothesis'] is True
assert p['finite_monodromy_search_used'] is False
assert p['monodromy_or_nielsen_case_choice_enters_argument'] is False
assert term['terminal_proposal']['outcome'] == 'O210_COVER_GEOMETRY_EXCLUDED'

ident = a['target_identity']
assert ident['population_relation'] == 'EQUAL_FOR_BOUND_STAGE32_TARGET_CONTEXT'
assert ident['q602_orbit_role'] == 'OBSTRUCTION_EVIDENCE_NOT_CARRIER_POPULATION_FILTER'
assert ident['q602_trace_gauge_invariant'] is True
assert ident['residual_monodromy_case_restriction_used'] is False
assert ident['finite_search_subpopulation_used'] is False
assert all(a['adapter_argument'].values())

fresh = a['freshness_observation']
assert fresh['observed_main_sha_at_construction'] == '42f20e47babdfdda068a605e3fec489eeace460c'
assert fresh['intervening_commit_stage'] == '35-EX'
assert fresh['stage32_main_state_blob_unchanged'] is True
assert fresh['unrelated_main_drift_is_not_semantic_binding'] is True

ceil = a['credit_ceiling']
assert ceil['promotion_adapter_retained'] is True and ceil['promotion_adapter_audited'] is False
for k in ['main_O210_claim_promoted','stage32_main_O210_excluded','stage32_main_Q602_excluded','stage32_main_credit','O212_plus_advance_allowed','stage32_closed','endpoint_credit']:
    assert ceil[k] is False, k

print('PASS Stage32EX3 EX3-10 drift-robust concrete EX3->MAIN O210 population adapter V2 candidate')
print(json.dumps({'binding':'STAGE32_TARGET_CONTEXT_CORE_PLUS_EXACT_MAIN_STATE_BLOB','from_scope':'S32.EX3.O210_COVER','to_scope':'S32.O210.COVER','population_relation':'EQUAL_FOR_BOUND_STAGE32_TARGET_CONTEXT','adapter_authority':'PROVISIONAL_PENDING_AUDIT','stage32_main_O210_excluded':False}, sort_keys=True))
