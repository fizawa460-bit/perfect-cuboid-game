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

res = text('stages/stage26/26-50/result.md')
reg = data('stages/stage26/26-50/construction-registry.json')
ctl = data('stages/stage26/26-controller.json')
s20 = text('stages/stage20/final.md')
a40 = text('stages/stage26/26-40/audit.md')
a60 = text('stages/stage25/25-reentry-60/audit.md')

assert 'AUDIT_VERDICT=PASS' in a40
assert 'AUDIT_VERDICT=PASS' in a60
assert 'even integer `m>=10`' in s20
assert '31m^6' in s20
assert 'distinct primitive canonical Euler cuboid' in s20

cons = reg['construction']
assert cons['name'] == 'Saunderson_even_m_family'
assert cons['parameter'] == 'even m>=10'
assert cons['height_bound'] == 'R<31m^6'
assert cons['primitive'] is True
assert cons['canonical_ordering'] is True
assert cons['injective'] is True

# Exact count of even m in [10,N]. At B=31*N^6, the sufficient
# height condition admits exactly this parameter range.
for N in [9, 10, 11, 20, 37, 100, 1001]:
    direct = len([m for m in range(10, N + 1) if m % 2 == 0])
    formula = max(0, N // 2 - 4)
    assert direct == formula
    # F_S(31*N^6)=N/2+O(1), with a uniformly bounded floor/start error.
    assert abs(formula - N / 2) <= 4.5

for key in [
    'M3_ge_explicit_family',
    'family_asymptotic_coefficient_explicit',
    'adjacent_ratio_positive_scaled_liminf',
    'phi_positive_scaled_liminf',
    'theta_positive_scaled_liminf',
    'directional_theta_positive_scaled_liminf',
]:
    assert reg['candidate_conclusions'][key] is True, key

for key in [
    'lower_scale_matching_true_scale_proved',
    'M3_asymptotic_proved',
    'true_M3_exponent_identified',
    'finite_data_used_as_asymptotic_proof',
]:
    assert reg['firewalls'][key] is False, key
assert reg['firewalls']['perfect_cuboid_conclusion'] == 'NONE'

for marker in [
    'F_S(B):=',
    'c_S:=',
    'liminf_{B\\to\\infty}',
    'LOWER_SCALE_MATCHING_TRUE_SCALE_PROVED=false',
    'M3_ASYMPTOTIC_PROVED=false',
    'TRUE_M3_EXPONENT_IDENTIFIED=false',
    'PERFECT_CUBOID_CONCLUSION=NONE',
]:
    assert marker in res, marker

assert ctl['checkpoint_status']['40'] == 'PROVED_AUDITED_PASS_MERGED'
assert ctl['checkpoint40']['pr'] == 1017
assert ctl['checkpoint40']['merge_commit'] == '48f08c4ff7e5b9708d12e22878e16102ec6f02a0'
assert ctl['state']['CURRENT_CHECKPOINT'] == 50
assert ctl['state']['NEXT_CHECKPOINT'] == 60
c50 = ctl['checkpoint50']
assert c50['audit_status'] == 'PENDING'
assert ctl['checkpoint_status']['50'] == 'PROVED_SUBMITTED_PENDING_AUDIT'
assert ctl['state']['AUDIT_STATUS'] == 'PENDING'
assert ctl['state']['ADVANCE_ALLOWED'] is False
assert ctl['state']['MERGE_ALLOWED'] is False
assert ctl['next_expected_command'] == 'Stage26-audit'

print('STAGE26_50_SAUNDERSON_COUNT=PASS')
print('STAGE26_50_EXPLICIT_SUBFAMILY_COEFFICIENT=PASS')
print('STAGE26_50_COMPLETION_LIMINF_FLOORS=PASS')
print('STAGE26_50_TRUE_SCALE_FIREWALL=PASS')
