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
s14 = text('stages/stage14/final.md')
s15_5 = text('stages/stage15/15-5/result.md')
s15_6 = text('stages/stage15/15-6-final.md')
queue = text('docs/stage14-15-bound-deep-review-queue.md')
status = text('docs/00_CURRENT_RESEARCH_STATUS.md')

# Checkpoint30 authorization and merge synchronization.
assert 'AUDIT_VERDICT=PASS' in a30
assert 'NEXT_CHECKPOINT=40' in a30
assert ctl['checkpoint_status']['30'] == 'DERIVED_RECEIVER_CALCULUS_AUDITED_PASS_MERGED'
assert ctl['checkpoint30']['audit_status'] == 'PASS'
assert ctl['checkpoint30']['pr'] == 1024
assert ctl['checkpoint30']['merge_commit'] == 'cf0f2a378ca6a3338670063821efb513e0aaeb73'

# Current theorem surface must remain unchanged.
assert 'N_2(B)\\ll B^{1/2+o(1)}' in s14
assert 'N_2(B)\\ll B^{1/2+o(1)}' in s15_5
assert ctl['current_theorem_surface']['N2_global_upper'] == 'N2(B)<<_epsilon B^(1/2+epsilon)'
assert ctl['current_theorem_surface']['strict_sub_sqrt_upper_proved'] is False

# Exact half-power bottleneck: horizontal active-vertex host, with vertical fibers only subpolynomial.
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
assert reg['half_power_bottleneck']['subpolynomial_fiber_improvement_changes_mu'] is False

# Latest exact same-measure local squareclass law and its mechanism-specific logarithmic boundary.
for marker in [
    'rho_p=',
    '1-\\rho_p=',
    '(\\log z)^{-2+o(1)}',
    'STAGE15_6_INTERNAL_FIXED_DELTA_PROVED=false',
    'STAGE15_6_INTERNAL_ROUTE_REMAINS=false',
]:
    assert marker in s15_6, marker
assert reg['local_squareclass']['same_measure'] is True
assert reg['local_squareclass']['polynomial_z_gives_fixed_power'] is False
assert reg['local_squareclass']['qualitative_zero_density_proved'] is True

# Q05/Q06/Q11 boundaries are read from the historical discovery queue, not reinvented.
for marker in [
    'Q05 — moving genus-one small-support receiver',
    'Q06 — admissible physical-diagonal Kummer support',
    'Q11 — fixed-prime local overlap sieve',
    'no effective growing-modulus uniformity',
]:
    assert marker in queue, marker

# Reopen contracts must demand true same-measure fixed-power progress.
assert reg['routes']['U40_A_SATURATION_HOST']['delta_required'] is True
assert reg['routes']['U40_B_LOCAL_SIEVE']['strict_subhalf_by_itself'] is False
assert '1/2-delta+epsilon' in reg['routes']['U40_C_KUMMER_SUPPORT']['sufficient_input']
assert reg['routes']['U40_D_MOVING_GENUS_ONE']['required_global_measure_adapter'] is True
assert reg['routes']['U40_D_MOVING_GENUS_ONE']['required_fixed_power_deficit'] is True
assert reg['routes']['U40_E_MAIN_T_S']['independence_product_allowed'] is False

# No theorem inflation.
for marker in [
    'STRICT_SUB_SQRT_UPPER_PROVED=false',
    'NEW_MU_LT_HALF_PROVED=false',
    'FINITE_ALPHA_USED_AS_PROOF=false',
    'TRUE_N2_EXPONENT_IDENTIFIED=false',
    'PERFECT_CUBOID_CONCLUSION=NONE',
]:
    assert marker in res, marker
assert reg['verdict']['new_mu_lt_half_proved'] is False
assert reg['verdict']['finite_alpha_used_as_proof'] is False
assert reg['verdict']['perfect_cuboid_conclusion'] == 'NONE'

# Historical checkpoint40 may be in its original submission state or in the
# audited/merged state while an authorized checkpoint40 child route is active.
assert ctl['checkpoint_status']['40'] in (
    'UPPER_ATTACK_SUBMITTED_PENDING_FRESH_AUDIT',
    'UPPER_ATTACK_AUDITED_PASS_MERGED_WITH_R401A_PENDING_AUDIT',
)
assert ctl['checkpoint40']['new_mu_lt_half_proved'] is False
assert ctl['state']['CURRENT_CHECKPOINT'] == 40
assert ctl['state']['AUDIT_STATUS'] == 'PENDING'
assert ctl['state']['ADVANCE_ALLOWED'] is False
assert ctl['state']['MERGE_ALLOWED'] is False
assert ctl['next_expected_command'] == 'Stage27-audit'
if ctl['checkpoint40']['audit_status'] == 'PASS':
    assert ctl['checkpoint40']['pr'] == 1025
    assert ctl['checkpoint40']['merge_commit'] == 'b76ebce08c5a90ed23bbd92762960ce719d3c718'
    assert ctl['state']['NEXT_CHECKPOINT'] == 40
    assert ctl['derived_routes']['Stage27-r401a']['audit_status'] == 'PENDING'
    assert 'CURRENT_STAGE=Stage27-r401a-SUBMITTED-PENDING-FRESH-AUDIT' in status
else:
    assert ctl['state']['NEXT_CHECKPOINT'] == 50
    assert 'CURRENT_STAGE=Stage27-40-SUBMITTED-PENDING-FRESH-AUDIT' in status
assert 'STAGE27_CHECKPOINT30_STATUS=DERIVED_RECEIVER_CALCULUS_AUDITED_PASS_MERGED_PR1024' in status
assert 'STAGE27_STRICT_SUB_SQRT_UPPER_PROVED=false' in status

print('STAGE27_40_AUTHORIZATION=PASS')
print('STAGE27_40_HALF_POWER_BOTTLENECK=PASS')
print('STAGE27_40_LOCAL_SIEVE_BOUNDARY=PASS')
print('STAGE27_40_REOPEN_CONTRACTS=PASS')
print('STAGE27_40_FIREWALL=PASS')
