#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REG = ROOT / 'stages/stage32/proof/CLAIM-REGISTRY.json'
ACTIVE = ROOT / 'stages/stage32/proof/ACTIVE-FRONTIER.json'
STATE = ROOT / 'stages/stage32-ex3/MAIN-STATE.json'
CID = 'S32.O210.EXCLUSION.V3'
OLD = 'S32.O210.EXCLUSION.V2'
CTX = 'S32.MAIN.CURRENT_TARGET_CONTEXT.V1'
EX3 = 'S32.EX3.O210_COVER_GEOMETRY_EXCLUSION_TERMINAL.V1'
AD = 'S32.ADAPTER.EX3_O210_TO_MAIN_O210.V3'
CORE = '7003e228cbb0273e1ac6352bd9535a5f10ca5964bc6d4072130d20012aaec824'
AUDIT = {
    'status': 'PASS',
    'pr': 1714,
    'review_id': 5147304889,
    'exact_head': '040dfb6c7e1dc40573866bb10f62e93419121711',
}
EXPECTED_BLOCKER = 'Hostile audit of the explicit MAIN O210 V3 claim has not yet been performed.'

def dump_compact(path: Path, obj: dict) -> None:
    path.write_text(json.dumps(obj, sort_keys=False, separators=(',', ':')) + '\n', encoding='utf-8')

def dump_pretty(path: Path, obj: dict) -> None:
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

# V3 is intentionally an ACTIVE-FRONTIER claim, not a base CLAIM-REGISTRY record.
# Registry remains read-only and supplies the immutable audited dependencies plus V2 history.
reg = json.loads(REG.read_text(encoding='utf-8'))
by = {c['claim_id']: c for c in reg['claims']}
assert CID not in by
assert by[CTX]['authority_status'] == 'AUDITED'
assert by[EX3]['authority_status'] == 'AUDITED' and by[EX3]['audit_receipt']['status'] == 'PASS'
assert by[AD]['authority_status'] == 'AUDITED' and by[AD]['audit_receipt']['status'] == 'PASS'
assert by[OLD]['authority_status'] == 'SUPERSEDED'
assert by[OLD]['audit_receipt'] is None
assert by[OLD]['claim_core_sha256'] == '178c0a8a381abacbfb5662f44f2faab2f2f6076f4be653172f7e586f77476746'

active = json.loads(ACTIVE.read_text(encoding='utf-8'))
matches = [x for x in active['claims'] if x['claim_id'] == CID]
assert len(matches) == 1
ac = matches[0]
assert ac['claim_core_sha256'] == CORE
assert ac['scope_key'] == 'S32.O210.COVER'
assert ac['scope'] == {'row_id':'g1-d186','picard_class':'V6','O':210,'qprime':4,'target':'population_wide_exclusion'}
assert ac['requires'] == [CTX, EX3, AD]
assert ac['lane_links'] == [{'lane':'MAIN','role':'OWNER'},{'lane':'EX3','role':'ATTACKS'}]
assert ac['authority_status'] == 'PROVISIONAL'
assert ac['audit_receipt'] is None
assert ac['frontier_status'] == 'ACTIVE_INCOMPLETE'
assert ac['blockers'] == [EXPECTED_BLOCKER]
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
# Authority receipt synchronization is deliberately not the MAIN routing-credit transition.
assert state['authority']['stage32_main_authority_unchanged'] is True
assert state['credit']['O210_excluded'] is False
assert state['credit']['stage32_main_credit'] is False
assert state['firewalls']['O210_excluded'] is False
assert state['firewalls']['O212_plus_advance_allowed'] is False
dump_pretty(STATE, state)

print('PASS applied S32.O210.EXCLUSION.V3 audit receipt sync on ACTIVE-FRONTIER')
print(json.dumps({'claim_id': CID, 'core': CORE, 'review_id': AUDIT['review_id'], 'exact_head': AUDIT['exact_head']}, sort_keys=True))
