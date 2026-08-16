#!/usr/bin/env python3
from fractions import Fraction
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'stages/stage26/26-30'

def text(rel):
    p = ROOT / rel
    assert p.exists(), rel
    return p.read_text(encoding='utf-8')

def data(rel):
    return json.loads(text(rel))

res = text('stages/stage26/26-30/result.md')
reg = data('stages/stage26/26-30/ratio-registry.json')
ctl = data('stages/stage26/26-controller.json')
s18 = text('stages/stage18/final.md')
s20 = text('stages/stage20/final.md')
a20 = text('stages/stage26/26-20/audit.md')

assert 'AUDIT_VERDICT=PASS' in a20
assert 'M_2(B)\\sim C_{M_2}B(\\log B)^5' in s18
assert 'B^{1/6}\\ll M_3(B)' in s20
assert 'eta<1/46' in s20

assert reg['population']['same_cutoff'] is True
assert reg['population']['same_physical_object_convention'] is True
assert reg['population']['exact_strata_disjoint'] is True
assert reg['inputs']['finite_panel_used_as_proof'] is False
assert reg['candidate_conclusions']['r_to_zero'] is True
assert reg['candidate_conclusions']['phi_to_zero'] is True
assert reg['candidate_conclusions']['theta_to_zero'] is True
assert reg['candidate_conclusions']['theta_over_phi_to_3'] is True
assert reg['firewalls']['true_M3_exponent_identified'] is False
assert reg['firewalls']['M3_asymptotic_claimed'] is False
assert reg['firewalls']['independence_claim'] is False
assert reg['firewalls']['K3_Manin_transfer'] is False
assert reg['firewalls']['perfect_cuboid_conclusion'] == 'NONE'

for r in [Fraction(1,1000), Fraction(1,10), Fraction(1,1), Fraction(7,3)]:
    phi = r/(1+r)
    theta = 3*r/(1+3*r)
    assert phi/(1-phi) == r
    assert theta/(1-theta) == 3*r
    assert theta == 3*phi/(1+2*phi)
    assert phi == theta/(3-2*theta)

for n in [10, 100, 1000, 10000]:
    r = Fraction(1,n)
    phi = r/(1+r)
    theta = 3*r/(1+3*r)
    assert abs(float(phi/r)-1.0) <= 1.0/n
    assert abs(float(theta/r)-3.0) <= 9.0/n

for marker in [
    'OBJECT_COMPLETION_RATE=Phi_EQUALS_M3_OVER_M2_PLUS_M3',
    'RAW_INCIDENCE_RATE=Theta_EQUALS_3M3_OVER_M2_PLUS_3M3',
    'EXACT_ODDS_BRIDGE=true',
    'PHI_TO_ZERO_PROVED_CANDIDATE=true',
    'THETA_TO_ZERO_PROVED_CANDIDATE=true',
    'THETA_OVER_PHI_TO_3_PROVED_CANDIDATE=true',
    'TRUE_M3_EXPONENT_IDENTIFIED=false',
    'FINITE_PANEL_USED_AS_ASYMPTOTIC_PROOF=false',
    'PERFECT_CUBOID_CONCLUSION=NONE',
]:
    assert marker in res, marker

assert ctl['checkpoint_status']['20'] == 'PROVED_AUDITED_PASS_MERGED'
c30 = ctl['checkpoint30']
if c30['audit_status'] == 'PENDING':
    assert ctl['state']['CURRENT_CHECKPOINT'] == 30
    assert ctl['checkpoint_status']['30'] == 'PROVED_SUBMITTED_PENDING_AUDIT'
    assert c30['advance_allowed'] is False
    assert c30['merge_allowed'] is False
    assert ctl['state']['AUDIT_STATUS'] == 'PENDING'
    assert ctl['next_expected_command'] == 'Stage26-audit'
elif c30['audit_status'] == 'PASS' and c30.get('merge_commit') is None:
    assert ctl['state']['CURRENT_CHECKPOINT'] == 30
    assert ctl['checkpoint_status']['30'] == 'PROVED_AUDITED_PASS_AWAITING_MERGE'
    assert c30['advance_allowed'] is True
    assert c30['merge_allowed'] is True
    assert (BASE / 'audit.md').exists()
    assert 'AUDIT_VERDICT=PASS' in (BASE / 'audit.md').read_text(encoding='utf-8')
    assert ctl['state']['NEXT_CHECKPOINT'] == 40
    assert ctl['next_expected_command'] == 'merge PR #1016; then Stage26-main-batch'
elif c30['audit_status'] == 'PASS' and c30.get('merge_commit'):
    assert ctl['checkpoint_status']['30'] == 'PROVED_AUDITED_PASS_MERGED'
    assert c30['pr'] == 1016
    assert c30['merge_commit'] == 'e5e884e37f62db78a31f09d8927be230f07b0f2f'
    assert ctl['state']['CURRENT_CHECKPOINT'] >= 40
    assert (BASE / 'audit.md').exists()
    assert 'AUDIT_VERDICT=PASS' in (BASE / 'audit.md').read_text(encoding='utf-8')
else:
    raise AssertionError(c30['audit_status'])

print('STAGE26_30_RATIO_INPUTS=PASS')
print('STAGE26_30_EXACT_MEASURE_ALGEBRA=PASS')
print('STAGE26_30_LITERAL_COMPLETION_CORRIDOR=PASS')
print('STAGE26_30_FIREWALL=PASS')
print(f"STAGE26_30_AUDIT_STATUS={c30['audit_status']}")
