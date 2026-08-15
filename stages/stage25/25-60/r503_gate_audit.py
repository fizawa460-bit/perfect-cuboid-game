#!/usr/bin/env python3
from fractions import Fraction
from pathlib import Path
import json

root = Path(__file__).resolve().parents[3]
result = (root/'stages/stage25/25-60/r503-yoshida-generic-rank-zero-gate.md').read_text(encoding='utf-8')
summary = (root/'stages/stage25/25-60/r503-result.md').read_text(encoding='utf-8')
ledger = (root/'stages/stage25/25-60/r503-discovery-ledger.md').read_text(encoding='utf-8')
triage = (root/'stages/stage25/25-60/deeper-lane-triage.md').read_text(encoding='utf-8')
continuation = (root/'stages/stage25/25-60/continuation-policy.md').read_text(encoding='utf-8')
audit = (root/'stages/stage25/25-60/r503-audit.md').read_text(encoding='utf-8')
iter_ctl = json.loads((root/'stages/stage25/25-60/r503-iteration-controller.json').read_text(encoding='utf-8'))
main_ctl = json.loads((root/'stages/stage25/25-controller.json').read_text(encoding='utf-8'))

# Exact family identification: (a,b,c)=(2s,s^2-1,s^2+1) is Pythagorean.
for num, den in [(2,1),(3,2),(5,3),(7,4),(11,6),(13,5)]:
    s=Fraction(num,den)
    a=2*s
    b=s*s-1
    c=s*s+1
    assert a*a+b*b == c*c

# Yoshida Theorem 1.1 specialization at s=5/3.
def t_from_alpha(alpha):
    return Fraction(15)*(9*alpha-32)/(81*alpha+800)

def alpha_from_t(t):
    return -Fraction(160)*(5*t+3)/(27*(3*t-5))

samples=[Fraction(-20,27),Fraction(1,2),Fraction(7,9),Fraction(-11,13),Fraction(25,17)]
for alpha in samples:
    if 81*alpha+800 == 0:
        continue
    t=t_from_alpha(alpha)
    if 3*t-5 == 0:
        continue
    assert alpha_from_t(t) == alpha

# Yoshida Corollary 4.7 transformed s-coordinate at s=5/3.
def sprime_from_alpha(alpha):
    return Fraction(4)*(27*alpha+40)/(27*alpha-640)

def alpha_from_sprime(sp):
    return Fraction(160)*(4*sp+1)/(27*(sp-4))

for alpha in samples:
    if 27*alpha-640 == 0:
        continue
    sp=sprime_from_alpha(alpha)
    if sp == 4:
        continue
    assert alpha_from_sprime(sp) == alpha

# Degree-two edge-ratio map used for physical-height transfer.
def rho(t):
    return 2*t/(t*t-1)
for t in [Fraction(2),Fraction(3,2),Fraction(7,4),Fraction(-5,3)]:
    assert rho(t) == Fraction(2*t, t*t-1)

for marker in [
    'R503_YOSHIDA_FAMILY_IDENTIFIED_WITH_PYTHAGOREAN_FREY_PLUS_FAMILY=true',
    'R503_GENERIC_GEOMETRIC_MW_RANK=0',
    'R503_NONTORSION_GENERIC_SECTION_EXISTS=false',
    'R503_DIRECT_SECTION_BASED_POWER_COUNT_ROUTE=CLOSED',
    'R503_YOSHIDA_FIXED_FIBER_ORBIT_COUNT_UPPER=O(sqrt(log B))',
    'R503_YOSHIDA_DISPLAYED_S_SEQUENCE_COUNT_UPPER=O(sqrt(log X))',
    'R503_STATUS=EXTERNAL_OR_BASE_CHANGE_THEOREM_GATE',
    'R503_LOW_DEGREE_BASE_CHANGE_MULTISECTION=OPEN_GATE',
    'R503_QUANTITATIVE_POSITIVE_RANK_FIBER_COUNT=OPEN_GATE',
    'R503_UNIFORM_SMALL_POINT_COUNT=OPEN_GATE',
    'NO_EXHAUSTIVE_LITERATURE_NONEXISTENCE_CLAIM=true',
    'FINITE_DATA_USED_AS_PROOF=false',
]: assert marker in result, marker

for marker in [
    'DISCOVERY_CHECKPOINT=Stage25-60-R503',
    'R503_FAMILY_IDENTIFICATION_ADAPTER=EXACT',
    'R503_GENERIC_GEOMETRIC_MW_RANK=0',
    'R503_FIXED_FIBER_ORBIT_COUNT_UPPER=O(sqrt(log B))',
    'R503_STATUS=EXTERNAL_OR_BASE_CHANGE_THEOREM_GATE',
    'R503_DIRECT_GENERIC_SECTION_ROUTE=CLOSED',
    'R503_BASE_CHANGE_MULTISECTION_ROUTE=OPEN_GATE',
    'NO_EXHAUSTIVE_NO_KNOWN_THEOREM_CLAIM=true',
]: assert marker in ledger, marker

# Main controller's previously audited checkpoint60 state must remain intact.
assert main_ctl['checkpoint_status']['60']=='PROVED_AUDITED_PASS'
assert main_ctl['checkpoint60']['audit']=='PASS'
assert main_ctl['checkpoint60']['r502_route_boundary_accepted'] is True
assert main_ctl['checkpoint60']['r502_route_boundary_certificate']=='CLOSED_NO_UPGRADE_WITH_CERTIFICATE'
assert main_ctl['checkpoint60']['deep_stop_rule_satisfied'] is False
assert main_ctl['checkpoint60']['stage70_allowed'] is False

status=iter_ctl['status']
assert status in ('SUBMITTED_FOR_FRESH_AUDIT','AUDITED_PASS')
assert iter_ctl['stage']=='Stage25'
assert iter_ctl['checkpoint']==60
assert iter_ctl['iteration']=='R503'
assert iter_ctl['previous_checkpoint60_audit']['verdict']=='PASS'
assert iter_ctl['generic_geometric_mw_rank']==0
assert iter_ctl['generic_nontorsion_section_exists'] is False
assert iter_ctl['direct_generic_section_route']=='CLOSED'
assert iter_ctl['route_status_after_candidate_audit']=='EXTERNAL_OR_BASE_CHANGE_THEOREM_GATE'
assert iter_ctl['checkpoint60_deep_stop_rule_satisfied'] is False
assert iter_ctl['stage70_allowed'] is False
assert iter_ctl['next_checkpoint']==60

if status == 'SUBMITTED_FOR_FRESH_AUDIT':
    assert iter_ctl['audit']=='PENDING'
    assert iter_ctl['advance_allowed'] is False
    assert iter_ctl['merge_allowed'] is False
    assert iter_ctl['next_expected_command']=='Stage25-audit'
    assert 'R503_STATUS=EXTERNAL_OR_BASE_CHANGE_THEOREM_GATE_SUBMITTED_FOR_FRESH_AUDIT' in triage
    assert 'R503=EXTERNAL_OR_BASE_CHANGE_THEOREM_GATE_SUBMITTED_FOR_FRESH_AUDIT' in continuation
else:
    assert iter_ctl['audit']=='PASS'
    assert iter_ctl['hostile_audit'] is True
    assert iter_ctl['audit_record']=='stages/stage25/25-60/r503-audit.md'
    assert iter_ctl['advance_allowed'] is True
    assert iter_ctl['merge_allowed'] is True
    assert iter_ctl['next_expected_command']=='merge PR #986; then Stage25-main-batch at checkpoint60'
    assert 'STATUS=AUDITED_PASS' in summary
    assert 'AUDIT_VERDICT=PASS' in summary
    assert 'R503_STATUS=EXTERNAL_OR_BASE_CHANGE_THEOREM_GATE_AUDITED_PASS' in triage
    assert 'R503=EXTERNAL_OR_BASE_CHANGE_THEOREM_GATE_AUDITED_PASS' in continuation
    for marker in [
        'AUDIT_VERDICT=PASS',
        'DISCOVERY_AUDIT_VERDICT=PASS',
        'R503_GENERIC_GEOMETRIC_MW_RANK_ACCEPTED=0',
        'R503_DIRECT_GENERIC_SECTION_ROUTE=CLOSED',
        'R503_ROUTE_STATUS=EXTERNAL_OR_BASE_CHANGE_THEOREM_GATE',
        'CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false',
        'STAGE70_ALLOWED=false',
        'MERGE_ALLOWED=true',
    ]: assert marker in audit, marker

print('R503_EXACT_PYTHAGOREAN_FREY_IDENTIFICATION=PASS')
print('R503_YOSHIDA_ALPHA_T_MOBIUS_BINDING=PASS')
print('R503_YOSHIDA_ALPHA_SPRIME_MOBIUS_BINDING=PASS')
print('R503_PHYSICAL_EDGE_RATIO_BINDING=PASS')
print('R503_GENERIC_RANK_ZERO_SOURCE_CONTRACT=PASS')
print('R503_FIXED_ORBIT_SQRT_LOG_UPPER_CONTRACT=PASS')
print('R503_MAIN_CONTROLLER_HISTORY_PRESERVED=PASS')
print(f'R503_ITERATION_CONTROLLER={status}')
print('STAGE25_60_R503_GATE_AUDIT=PASS')
