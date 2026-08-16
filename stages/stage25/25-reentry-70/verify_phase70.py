#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]

def text(rel):
    p = ROOT / rel
    assert p.exists(), rel
    return p.read_text(encoding='utf-8')

def data(rel):
    return json.loads(text(rel))

res = text('stages/stage25/25-reentry-70/result.md')
hand = data('stages/stage25/25-reentry-70/handoff-registry.json')
prop = data('stages/stage25/25-reentry-70/propagation-resolution.json')
disc = text('stages/stage25/25-reentry-70/discovery-ledger.md')
weap = text('stages/stage25/25-reentry-70/weapon-delta.md')
s26 = text('stages/stage25/25-reentry-70/stage26-handoff.md')
ctrl = data('stages/stage25/25-reentry-controller.json')
p60audit = text('stages/stage25/25-reentry-60/audit.md')
p70audit = text('stages/stage25/25-reentry-70/audit.md')
arsenal = text('docs/stage25-arsenal-promotion.md')
status = text('docs/00_CURRENT_RESEARCH_STATUS.md')
deep = text('docs/stage14-15-bound-deep-review-queue.md')

assert 'AUDIT_VERDICT=PASS' in p60audit
assert ctrl['phase60_submission']['audit_status'] == 'PASS'
assert ctrl['phase60_submission']['pr'] == 1011
assert ctrl['phase60_submission']['merge_commit'] == '119afa00919f67bea8e3ba5515c0f9663aa9f2e2'
assert ctrl['phase60_submission']['stage20_stage26_ready_interface'] is True

for phase in ('10','20','30','40','50','60'):
    assert 'AUDITED_PASS_MERGED' in ctrl['phases'][phase]['status'], (phase, ctrl['phases'][phase]['status'])
for key in ('r008a_submission','r009a_submission','r010a_submission','r011a_submission'):
    assert ctrl[key]['status'] == 'AUDITED_PASS_MERGED', key
    assert ctrl[key]['audit_status'] == 'PASS', key

assert prop['internal_queue']['active_routes'] == []
assert prop['internal_queue']['queued_routes'] == []
assert prop['internal_queue']['unresolved_internal_route'] is False
assert prop['resolution_candidate']['backflow_synchronized'] is True
assert prop['resolution_candidate']['stage26_handoff_ready'] is True

receiver_files = (
    'stages/stage19/post-stage25-50-supersession.md',
    'stages/stage23/post-stage25-r01/result.md',
    'stages/stage24/post-stage25-r01/result.md',
    'stages/stage17/post-stage25-r009a.md',
    'stages/stage23/post-stage25-r009a.md',
    'stages/stage18/post-stage25-r010a.md',
    'stages/stage20/post-stage25-r010a.md',
    'stages/stage22/post-stage25-r010a.md',
    'stages/stage21/post-stage25-r011a.md',
    'stages/stage22/post-stage25-r011a.md',
    'stages/stage18/post-stage25-phase60.md',
    'stages/stage20/post-stage25-phase60.md',
)
for rel in receiver_files:
    t = text(rel)
    assert 'BACKFLOW_AUDIT_STATUS=PASS' in t, rel
    assert 'BACKFLOW_SYNCHRONIZED=true' in t, rel
    assert 'PENDING_FRESH_AUDIT' not in t, rel

s19 = text('stages/stage19/post-stage25-50-supersession.md')
assert 'CURRENT_LOWER=N2(B)>>B^(1/4)' in s19
for token in ('N2,a(B)>>B^(1/4)', 'N2,b(B)>>B^(1/4)', 'N2,c(B)>>B^(1/4)'):
    assert token in s19
assert 'TRUE_TARGET_EXPONENT_IDENTIFIED=false' in s19
assert 'GLOBAL_N2_EXPONENT_UPGRADED=false' in s19

interfaces = hand['interfaces']
assert interfaces['N2']['lower'] == 'N2(B)>>B^(1/4)'
assert interfaces['N2']['true_exponent_identified'] is False
assert interfaces['M3']['lower'] == 'M3(B)>>B^(1/6)'
assert interfaces['M3']['true_exponent_identified'] is False
raw = interfaces['raw_pair_completion']
assert raw['directional_identity'] == 'P_j=M2,j+M3'
assert raw['global_identity'] == 'P=M2+3M3'
assert raw['literal_same_measure_probability'] is True
assert raw['directional_ratio'] == 'Theta_j/Theta_k->C_k/C_j'
r26 = hand['stage26_receiver']
for k in ('population_match','cutoff_match','multiplicity_match','measure_match','quantifier_match','ready_interface'):
    assert r26[k] is True, k
assert hand['gate_candidate']['derived_route_queue_has_unresolved_internal_route'] is False
assert hand['gate_candidate']['stage20_stage26_ready_interface'] is True
assert hand['gate_candidate']['all_reentry_phases_audited'] is False
assert hand['gate_candidate']['stage26_allowed'] is False
assert 'ALL_REENTRY_PHASES_AUDITED=false' in res
assert 'STAGE26_ALLOWED=false' in res

assert 'S25-W05' in arsenal
assert 'S25-W06' in arsenal
assert 'S25_W05_PROMOTED=true' in weap
assert 'S25_W06_PROMOTED=true' in weap
assert 'FOUR_INDEPENDENT_LOG_FACTORS_PROVED=false' in arsenal
assert 'TRUE_M3_EXPONENT_PROMOTED=false' in arsenal
assert 'PERFECT_CUBOID_EXISTENCE_PROMOTED=false' in arsenal
assert 'PERFECT_CUBOID_NONEXISTENCE_PROMOTED=false' in arsenal

for token in ('Q07', 'Q08', 'Q09', 'Q10', 'P3_EXHAUSTED_INTERNAL'):
    assert token in deep
assert 'P3_REOPEN_WITHOUT_NEW_INPUT' in disc

assert 'AUDIT_VERDICT=PASS' in p70audit
assert 'REENTRY_RESEARCH_COMPLETE=true' in p70audit
assert 'ALL_REENTRY_PHASES_AUDITED=true' in p70audit
assert 'STAGE26_ENTRY_INTERFACE_VALID=true' in p70audit
assert 'STAGE26_ALLOWED_AFTER_MERGE=true' in p70audit

assert ctrl['current_phase'] == 70
assert ctrl['status'] == 'CLOSED_AUDITED_PASS_MERGED_STAGE26_HANDOFF_READY'
assert ctrl['phases']['70']['status'] == 'AUDITED_PASS_MERGED'
p70 = ctrl['phase70_submission']
assert p70['status'] == 'AUDITED_PASS_MERGED'
assert p70['audit_status'] == 'PASS'
assert p70['advance_allowed'] is True
assert p70['merge_allowed'] is True
assert p70['reentry_research_complete'] is True
assert p70['derived_route_queue_has_unresolved_internal_route'] is False
assert p70['stage20_stage26_ready_interface'] is True
assert p70['backflow_synchronized'] is True
assert p70['stage26_allowed'] is True
assert p70['pr'] == 1012
assert p70['merge_commit'] == 'be5f7d8360b3bac2b9060cd88ede596a4fb218dc'

assert ctrl['stage26_gate']['all_reentry_phases_audited'] is True
assert ctrl['stage26_gate']['unresolved_internal_routes'] is False
assert ctrl['stage26_gate']['stage20_stage26_ready_interface'] is True
assert ctrl['stage26_gate']['backflow_synchronized'] is True
assert ctrl['stage26_gate']['stage26_allowed'] is True
assert ctrl['next_expected_command'] == 'Stage26-main-batch'

assert 'STATUS=AUDITED_PASS_MERGED_STAGE26_ENTRY_AUTHORIZED' in s26
assert 'STAGE26_ENTRY_INTERFACE_VALID=true' in s26
assert 'PHASE70_AUDIT_STATUS=PASS' in s26
assert 'PHASE70_MERGED=true' in s26
assert 'STAGE26_ALLOWED=true' in s26

# State-aware post-handoff status. Stage26-READY is the historical handoff state;
# once Stage26 starts, a Stage26-* current-state marker is the expected successor.
assert ('CURRENT_STAGE=Stage26-READY' in status) or ('CURRENT_STAGE=Stage26-' in status)
assert 'ALL_REENTRY_PHASES_AUDITED=true' in status
assert 'STAGE26_ALLOWED=true' in status
assert ('NEXT_EXPECTED_COMMAND=Stage26-main-batch' in status) or ('NEXT_EXPECTED_COMMAND=Stage26-audit' in status)

assert 'PERFECT_CUBOID_CONCLUSION=NONE' in res
assert 'PERFECT_CUBOID_CONCLUSION=NONE' in s26

print('STAGE25_REENTRY_PHASE70_PRIOR_AUDITS_MERGED=PASS')
print('STAGE25_REENTRY_PHASE70_PROPAGATION_QUEUE=RESOLVED')
print('STAGE25_REENTRY_PHASE70_BACKFLOW_SYNCHRONIZED=PASS')
print('STAGE25_REENTRY_PHASE70_STAGE19_STRONGEST_INTERFACE=PASS')
print('STAGE25_REENTRY_PHASE70_AUDIT_MERGE=PASS')
print('STAGE25_REENTRY_PHASE70_ARSENAL_PROMOTION=PASS')
print('STAGE25_REENTRY_PHASE70_P3_REOPEN_FIREWALL=PASS')
print('STAGE25_REENTRY_RESEARCH_COMPLETE=PASS')
print('STAGE26_GATE=OPEN')
