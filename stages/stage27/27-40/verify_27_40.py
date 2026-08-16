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

res = text('stages/stage27/27-40/result.md')
reg = data('stages/stage27/27-40/upper-attack-registry.json')
ctl = data('stages/stage27/27-controller.json')
a30 = text('stages/stage27/27-30/audit.md')
a40 = text('stages/stage27/27-40/audit.md')
s14 = text('stages/stage14/final.md')
s15_5 = text('stages/stage15/15-5/result.md')
s15_6 = text('stages/stage15/15-6-final.md')
queue = text('docs/stage14-15-bound-deep-review-queue.md')
status = text('docs/00_CURRENT_RESEARCH_STATUS.md')

assert 'AUDIT_VERDICT=PASS' in a30
assert ctl['checkpoint_status']['30'] == 'DERIVED_RECEIVER_CALCULUS_AUDITED_PASS_MERGED'
assert ctl['checkpoint30']['merge_commit'] == 'cf0f2a378ca6a3338670063821efb513e0aaeb73'

assert 'N_2(B)\\ll B^{1/2+o(1)}' in s14
assert 'N_2(B)\\ll B^{1/2+o(1)}' in s15_5
assert ctl['current_theorem_surface']['N2_global_upper'] == 'N2(B)<<_epsilon B^(1/2+epsilon)'
assert ctl['current_theorem_surface']['strict_sub_sqrt_upper_proved'] is False

for marker in [
    'E(B)\\ll V(B)B^{o(1)}',
    'V(B)\\ll B^{1/2+o(1)}',
    'Proposition 3.6 — active-face square-root bound',
    'proportional branch: `E<=7/16<1/2`',
    'nonproportional and `theta<=1/4`',
    'nonproportional and `theta>=1/4`',
]:
    assert marker in s14, marker
assert reg['half_power_bottleneck']['fixed_exponent_source'] == 'horizontal active-vertex complete-host saturation'
assert reg['half_power_bottleneck']['vertical_elliptic_fiber_fixed_power'] is False

for marker in ['rho_p=', '1-\\rho_p=', '(\\log z)^{-2+o(1)}', 'STAGE15_6_INTERNAL_FIXED_DELTA_PROVED=false']:
    assert marker in s15_6, marker
assert reg['local_squareclass']['same_measure'] is True
assert reg['local_squareclass']['polynomial_z_gives_fixed_power'] is False

for marker in [
    'Q05 — moving genus-one small-support receiver',
    'Q06 — admissible physical-diagonal Kummer support',
    'Q11 — fixed-prime local overlap sieve',
]:
    assert marker in queue, marker

assert reg['routes']['U40_A_SATURATION_HOST']['delta_required'] is True
assert reg['routes']['U40_B_LOCAL_SIEVE']['strict_subhalf_by_itself'] is False
assert '1/2-delta+epsilon' in reg['routes']['U40_C_KUMMER_SUPPORT']['sufficient_input']
assert reg['routes']['U40_D_MOVING_GENUS_ONE']['required_global_measure_adapter'] is True
assert reg['routes']['U40_E_MAIN_T_S']['independence_product_allowed'] is False

for marker in [
    'STRICT_SUB_SQRT_UPPER_PROVED=false',
    'NEW_MU_LT_HALF_PROVED=false',
    'FINITE_ALPHA_USED_AS_PROOF=false',
    'TRUE_N2_EXPONENT_IDENTIFIED=false',
    'PERFECT_CUBOID_CONCLUSION=NONE',
]:
    assert marker in res, marker

# Checkpoint40 itself is frozen PASS+merged. Any authorized checkpoint40 child
# route may update the lifecycle suffix without changing the theorem surface.
assert 'AUDIT_VERDICT=PASS' in a40
assert ctl['checkpoint40']['audit_status'] == 'PASS'
assert ctl['checkpoint40']['pr'] == 1025
assert ctl['checkpoint40']['merge_commit'] == 'b76ebce08c5a90ed23bbd92762960ce719d3c718'
assert ctl['checkpoint_status']['40'].startswith('UPPER_ATTACK_AUDITED_PASS_MERGED')
assert ctl['state']['CURRENT_CHECKPOINT'] == 40
assert ctl['state']['NEXT_CHECKPOINT'] == 40
assert ctl['state']['AUDIT_STATUS'] == 'PENDING'
assert ctl['state']['ADVANCE_ALLOWED'] is False
assert ctl['state']['MERGE_ALLOWED'] is False
assert ctl['next_expected_command'] == 'Stage27-audit'
assert 'STAGE27_CHECKPOINT40_STATUS=UPPER_ATTACK_AUDITED_PASS_MERGED_PR1025' in status
assert 'STAGE27_STRICT_SUB_SQRT_UPPER_PROVED=false' in status

print('STAGE27_40_AUTHORIZATION=PASS')
print('STAGE27_40_HALF_POWER_BOTTLENECK=PASS')
print('STAGE27_40_LOCAL_SIEVE_BOUNDARY=PASS')
print('STAGE27_40_REOPEN_CONTRACTS=PASS')
print('STAGE27_40_CHILD_ROUTE_LIFECYCLE=PASS')
print('STAGE27_40_FIREWALL=PASS')
