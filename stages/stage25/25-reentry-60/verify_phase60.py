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

res = text('stages/stage25/25-reentry-60/result.md')
proof = text('stages/stage25/25-reentry-60/completion-proof.md')
reg = data('stages/stage25/25-reentry-60/completion-registry.json')
back = data('stages/stage25/25-reentry-60/backflow-proposals.json')
s18 = text('stages/stage18/final.md')
s20 = text('stages/stage20/final.md')
r010 = text('stages/stage25/25-reentry-r010a/result.md')
r011audit = text('stages/stage25/25-reentry-r011a/audit.md')
ctrl = data('stages/stage25/25-reentry-controller.json')

assert 'AUDIT_VERDICT=PASS' in r011audit
assert ctrl['r011a_submission']['status'] == 'AUDITED_PASS_MERGED'
assert ctrl['r011a_submission']['audit_status'] == 'PASS'
assert ctrl['r011a_submission']['merge_commit'] == 'e64f21621bb1b7062dfd21f186e6ed1bcc191272'

assert 'M_2(B)\\sim C_{M_2}B(\\log B)^5' in s18
assert 'B^{1/6}\\ll M_3(B)' in s20
assert 'eta<1/46' in s20
assert ('P_j=M_{2,j}+M_3' in r010 or 'P_j=M2,j+M3' in r010)

assert reg['population']['raw_directional'] == 'P_j=M2,j+M3'
assert reg['population']['raw_total'] == 'P=M2+3M3'
assert reg['completion_rates']['literal_incidence_probability'] is True
assert reg['completion_rates']['object_ratio_M3_over_M2_is_probability'] is False
assert 'Theta_j=M3/P_j' in reg['completion_rates']['directional']
assert 'Theta=3M3/(M2+3M3)' in reg['completion_rates']['total']

cc = reg['candidate_conclusions']
assert 'B^(-5/6)(log B)^(-5)' in cc['directional_corridor']
assert '(log B)^(-eta)' in cc['directional_corridor']
assert cc['directional_ratio'] == 'Theta_j/Theta_k->C_k/C_j'
assert cc['true_M3_exponent_identified'] is False
assert 'Theta_j(B)}{\\Theta_k(B)' in res
assert 'C_k}{C_j' in res
assert 'B^{-5/6}(\\log B)^{-5}' in proof

for k in ('population_match','cutoff_match','multiplicity_match','measure_match','quantifier_match'):
    assert reg['compatibility'][k] is True
assert reg['compatibility']['finite_data_promoted'] is False
assert 'The K3 cover is not assigned a fake `(a,b)` difference' in proof
assert 'PERFECT_CUBOID_CONCLUSION=NONE' in res

assert back['derived_routes_opened'] == []
assert back['phase70_after_audit_pass_and_merge'] is True
assert back['stage26_allowed'] is False
assert reg['stage26_receiver']['candidate_ready'] is True
assert reg['stage26_receiver']['accepted_ready'] is False

assert ctrl['current_phase'] == 60
assert ctrl['status'] == 'PHASE60_SUBMITTED_PENDING_FRESH_AUDIT'
p60 = ctrl['phase60_submission']
assert p60['task_id'] == 'Stage25-u20-r006a'
assert p60['audit_status'] == 'PENDING'
assert p60['advance_allowed'] is False
assert p60['merge_allowed'] is False
assert ctrl['phases']['60']['status'] == 'SUBMITTED_PENDING_FRESH_AUDIT'
assert ctrl['phases']['70']['status'] == 'BLOCKED_UNTIL_PHASE60_AUDIT_PASS_MERGE'
assert ctrl['stage26_gate']['stage20_stage26_ready_interface'] is False
assert ctrl['stage26_gate']['stage26_allowed'] is False
assert ctrl['next_expected_command'] == 'Stage25-reentry-audit'

print('STAGE25_REENTRY_PHASE60_AUTHORIZATION=PASS')
print('STAGE25_REENTRY_PHASE60_RAW_PAIR_MEASURE=PASS')
print('STAGE25_REENTRY_PHASE60_COMPLETION_CORRIDOR=PASS')
print('STAGE25_REENTRY_PHASE60_DIRECTIONAL_RATIO=PASS')
print('STAGE25_REENTRY_PHASE60_STAGE26_RECEIVER_CANDIDATE=PASS')
print('STAGE26_GATE=BLOCKED_VALID')
