#!/usr/bin/env python3
from fractions import Fraction
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'stages/stage26/26-40'

def text(rel):
    p = ROOT / rel
    assert p.exists(), rel
    return p.read_text(encoding='utf-8')

def data(rel):
    return json.loads(text(rel))

res = text('stages/stage26/26-40/result.md')
ledger = text('stages/stage26/26-40/mechanism-ledger.md')
reg = data('stages/stage26/26-40/upper-registry.json')
ctl = data('stages/stage26/26-controller.json')
s18 = text('stages/stage18/final.md')
s20 = text('stages/stage20/final.md')
a30 = text('stages/stage26/26-30/audit.md')
a60 = text('stages/stage25/25-reentry-60/audit.md')

assert 'AUDIT_VERDICT=PASS' in a30
assert 'AUDIT_VERDICT=PASS' in a60
assert 'M_2(B)\\sim C_{M_2}B(\\log B)^5' in s18
assert 'eta<1/46' in s20
assert 'delta_2=2/9' in s20
assert 'delta_p=' in s20

assert reg['upstream']['checkpoint30_pr'] == 1016
assert reg['upstream']['checkpoint30_merge_commit'] == 'e5e884e37f62db78a31f09d8927be230f07b0f2f'
assert reg['candidate_conclusions']['for_every_fixed_delta_lt_1_over_46_little_o'] is True
assert reg['candidate_conclusions']['directional_theta_j_little_o'] is True
assert reg['quantifiers']['endpoint_1_over_46_included'] is False
assert reg['mechanism']['savings_multiplied'] is False
for key in [
    'endpoint_1_over_46_proved',
    'exact_log_decay_exponent_proved',
    'fixed_power_saving_in_B_proved',
    'M3_asymptotic_proved',
    'true_M3_exponent_identified',
    'K3_Manin_transfer',
    'independence_claim',
    'finite_data_used_as_proof',
]:
    assert reg['firewalls'][key] is False, key
assert reg['firewalls']['perfect_cuboid_conclusion'] == 'NONE'

# Exact completion transforms are monotone upper adapters.
for r in [Fraction(1,1000), Fraction(1,10), Fraction(1,1), Fraction(7,3)]:
    phi = r/(1+r)
    theta = 3*r/(1+3*r)
    assert 0 <= phi <= r
    assert 0 <= theta <= 3*r

# Quantifier witness: every rational delta below 1/46 admits fixed eta strictly between.
for delta in [Fraction(1,100), Fraction(1,50), Fraction(2,100), Fraction(1,47)]:
    assert delta < Fraction(1,46)
    eta = (delta + Fraction(1,46))/2
    assert delta < eta < Fraction(1,46)
    assert eta - delta > 0

for marker in [
    'ENDPOINT_FREE_LITTLE_O_CANDIDATE=true',
    'DIRECTIONAL_LITTLE_O_CANDIDATE=true',
    'LOCAL_BLOCKER_AND_THIN_COVER_SAVINGS_MULTIPLIED=false',
    'TRUE_M3_EXPONENT_IDENTIFIED=false',
    'K3_MANIN_TRANSFER=false',
    'INDEPENDENCE_CLAIM=false',
    'PERFECT_CUBOID_CONCLUSION=NONE',
    'NEXT_EXPECTED_COMMAND=Stage26-audit',
]:
    assert marker in res, marker

for marker in [
    'No uniformity in `eta` as `eta->1/46` is needed or claimed.',
    'Their savings are not multiplied.',
    'endpoint `1/46`',
]:
    assert marker in ledger, marker

assert ctl['checkpoint_status']['30'] == 'PROVED_AUDITED_PASS_MERGED'
assert ctl['checkpoint30']['merge_commit'] == 'e5e884e37f62db78a31f09d8927be230f07b0f2f'
assert ctl['state']['CURRENT_CHECKPOINT'] == 40
assert ctl['checkpoint_status']['40'] == 'PROVED_SUBMITTED_PENDING_AUDIT'
assert ctl['checkpoint40']['audit_status'] == 'PENDING'
assert ctl['checkpoint40']['advance_allowed'] is False
assert ctl['checkpoint40']['merge_allowed'] is False
assert ctl['state']['AUDIT_STATUS'] == 'PENDING'
assert ctl['state']['ADVANCE_ALLOWED'] is False
assert ctl['state']['MERGE_ALLOWED'] is False
assert ctl['state']['NEXT_CHECKPOINT'] == 50
assert ctl['next_expected_command'] == 'Stage26-audit'

print('STAGE26_40_UPPER_INPUTS=PASS')
print('STAGE26_40_ENDPOINT_FREE_LITTLE_O=PASS')
print('STAGE26_40_DIRECTIONAL_RECEIVER=PASS')
print('STAGE26_40_MECHANISM_FIREWALL=PASS')
print('STAGE26_40_AUDIT_STATUS=PENDING')
