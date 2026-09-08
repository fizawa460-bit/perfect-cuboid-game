#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REG = ROOT / 'stages/stage32/proof/CLAIM-REGISTRY.json'
ACTIVE = ROOT / 'stages/stage32/proof/ACTIVE-FRONTIER.json'
STATE = ROOT / 'stages/stage32-ex3/MAIN-STATE.json'
CID = 'S32.O210.EXCLUSION.V3'
CORE = '7003e228cbb0273e1ac6352bd9535a5f10ca5964bc6d4072130d20012aaec824'
AUDIT = {
    'status': 'PASS',
    'pr': 1714,
    'review_id': 5147304889,
    'exact_head': '040dfb6c7e1dc40573866bb10f62e93419121711',
}

def dump_compact(path: Path, obj: dict) -> None:
    path.write_text(json.dumps(obj, sort_keys=False, separators=(',', ':')) + '\n', encoding='utf-8')

def dump_pretty(path: Path, obj: dict) -> None:
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

def walk(obj):
    if isinstance(obj, dict):
        yield obj
        for value in obj.values():
            yield from walk(value)
    elif isinstance(obj, list):
        for value in obj:
            yield from walk(value)

def registry_claims(reg: dict) -> dict[str, dict]:
    records = [
        d for d in walk(reg)
        if isinstance(d.get('claim_id'), str)
        and 'claim_core_sha256' in d
        and 'authority_status' in d
        and 'scope_key' in d
    ]
    by: dict[str, dict] = {}
    for rec in records:
        claim_id = rec['claim_id']
        assert claim_id not in by, f'duplicate actual claim record: {claim_id}'
        by[claim_id] = rec
    return by

reg = json.loads(REG.read_text(encoding='utf-8'))
by = registry_claims(reg)
assert CID in by, f'missing actual claim record: {CID}; available={sorted(by)}'
c = by[CID]
assert c['claim_core_sha256'] == CORE
assert c['authority_status'] == 'PROVISIONAL'
assert c['audit_receipt'] is None
assert c['requires'] == [
    'S32.MAIN.CURRENT_TARGET_CONTEXT.V1',
    'S32.EX3.O210_COVER_GEOMETRY_EXCLUSION_TERMINAL.V1',
    'S32.ADAPTER.EX3_O210_TO_MAIN_O210.V3',
]
for dep in c['requires'][1:]:
    assert by[dep]['authority_status'] == 'AUDITED', (dep, by[dep]['authority_status'])
c['authority_status'] = 'AUDITED'
c['audit_receipt'] = dict(AUDIT)
dump_compact(REG, reg)

active = json.loads(ACTIVE.read_text(encoding='utf-8'))
active_matches = [x for x in active['claims'] if x['claim_id'] == CID]
assert len(active_matches) == 1
ac = active_matches[0]
assert ac['claim_core_sha256'] == CORE
assert ac['authority_status'] == 'PROVISIONAL'
assert ac['audit_receipt'] is None
assert ac['frontier_status'] == 'ACTIVE_INCOMPLETE'
ac['authority_status'] = 'AUDITED'
ac['audit_receipt'] = dict(AUDIT)
ac['frontier_status'] = 'AUDITED_TRUE'
ac['blockers'] = []
dump_compact(ACTIVE, active)

state = json.loads(STATE.read_text(encoding='utf-8'))
assert state['candidate_frontier']['main_o210_active_claim_id'] == CID
assert state['candidate_frontier']['main_o210_v3_core_sha256'] == CORE
assert state['candidate_frontier']['main_o210_v3_hostile_audited'] is False
assert state['credit']['O210_excluded'] is False
assert state['credit']['stage32_main_credit'] is False
assert state['firewalls']['O210_excluded'] is False
assert state['firewalls']['O212_plus_advance_allowed'] is False
state['schema'] = 'STAGE32EX3_MAIN_COMPACT_STATE_V1_MAIN_O210_V3_AUDITED_RECEIPT_SYNCED_MAIN_CREDIT_PENDING'
state['current'].update({
    'status': 'MAIN_O210_V3_AUDITED_RECEIPT_SYNCED_MAIN_CREDIT_PENDING',
    'subroute': 'MAIN_O210_V3_AUDITED_AUTHORITY_SYNC',
    'objective': 'Hostile-audit PASS receipt for S32.O210.EXCLUSION.V3 is synchronized; Stage32 MAIN O210 routing credit remains a separate explicit transition.',
    'next_route_on_success': 'STAGE32_MAIN_O210_CREDIT_TRANSITION',
    'next_route_on_block': 'REPAIR_ONLY_IF_POST_SYNC_VERIFIER_FAILS',
    'stop_semantics': 'V3_AUDITED_MAIN_O210_CREDIT_NOT_YET_ROUTED_NO_O212_ADVANCE_NO_MERGE',
})
state['candidate_frontier'].update({
    'main_o210_v3_hostile_audited': True,
    'main_o210_v3_audit_review_id': AUDIT['review_id'],
    'main_o210_v3_audited_exact_head': AUDIT['exact_head'],
    'main_o210_v3_claim_sync_complete': True,
})
state['management'].update({
    'claim_sync_trigger': 'AUTHORITY_OR_AUDIT_TRANSITION',
    'claim_sync_status': 'COMPLETE_MAIN_O210_V3_AUDITED_PASS_RECEIPT_SYNCED_MAIN_CREDIT_PENDING',
    'active_frontier_remap_authority': 'AUDITED',
    'main_o210_v3_hostile_audit_required': False,
    'main_o210_v3_hostile_audit_result': 'PASS',
    'main_o210_v3_hostile_audit_review_id': AUDIT['review_id'],
    'main_o210_v3_hostile_audited_exact_head': AUDIT['exact_head'],
    'ex_to_main_promotion_complete': False,
})
state['main_o210_v3'].update({
    'status': 'HOSTILE_AUDIT_PASS_RECEIPT_SYNCED_AUDITED_MAIN_CREDIT_PENDING',
    'hostile_audit_required': False,
    'hostile_audit_result': 'PASS',
    'main_O210_promotion_complete': False,
    'credit_ceiling': 'AUDITED_MAIN_O210_EXCLUSION_CLAIM_CONSUMABLE_ROUTING_CREDIT_PENDING',
    'hostile_audit_review_id': AUDIT['review_id'],
    'hostile_audited_exact_head': AUDIT['exact_head'],
})
# This checkpoint synchronizes authority only. MAIN routing credit is deliberately separate.
assert state['authority']['stage32_main_authority_unchanged'] is True
assert state['credit']['O210_excluded'] is False
assert state['credit']['stage32_main_credit'] is False
assert state['firewalls']['O210_excluded'] is False
assert state['firewalls']['O212_plus_advance_allowed'] is False
dump_pretty(STATE, state)

print('PASS applied S32.O210.EXCLUSION.V3 audit receipt sync')
print(json.dumps({'claim_id': CID, 'core': CORE, 'review_id': AUDIT['review_id'], 'exact_head': AUDIT['exact_head']}, sort_keys=True))
