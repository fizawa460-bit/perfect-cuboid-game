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

res = text('stages/stage27/27-30/result.md')
reg = data('stages/stage27/27-30/receiver-registry.json')
ctl = data('stages/stage27/27-controller.json')
a20 = text('stages/stage27/27-20/audit.md')
a30 = text('stages/stage27/27-30/audit.md')
s19 = text('stages/stage19/post-stage25-50-supersession.md')
s23 = text('stages/stage23/post-stage25-r01/result.md')
s24 = text('stages/stage24/post-stage25-r01/result.md')

# Upstream checkpoint20 remains audited and merged.
assert 'AUDIT_VERDICT=PASS' in a20
assert reg['upstream']['checkpoint20_pr'] == 1023
assert reg['upstream']['checkpoint20_merge_commit'] == 'ecbd182f25dcb010319789855c82477eee7077c7'
assert reg['upstream']['checkpoint20_audit'] == 'PASS'
assert ctl['checkpoint_status']['20'] == 'DERIVED_EXACT_FINITE_AUDITED_PASS_MERGED'
assert ctl['checkpoint20']['audit_status'] == 'PASS'
assert ctl['checkpoint20']['pr'] == 1023
assert ctl['checkpoint20']['merge_commit'] == 'ecbd182f25dcb010319789855c82477eee7077c7'

# Current theorem surface is unchanged.
for marker in [
    'N_2(B)\\gg B^{1/4}',
    'N_2(B)\\ll_\\varepsilon B^{1/2+\\varepsilon}',
]:
    assert marker in s19, marker
assert 'RATIO_LOWER=N2/N1>>B^(-3/4)(log B)^(-3)' in s23
assert 'RATIO_UPPER=N2/N1<<_epsilon B^(-1/2+epsilon)(log B)^(-3)' in s23
assert 'CURRENT_SURVIVOR_RATIO_LOWER=N2/M2>>B^(-3/4)(log B)^(-5)' in s24

beta = 1/4
mu = 1/2
assert beta - 1 == -3/4
assert mu - 1 == -1/2
assert reg['current']['beta_lower'] == '1/4'
assert reg['current']['mu_upper'] == '1/2'
assert reg['generic_lower']['progress_gate'] == 'beta>1/4'
assert reg['generic_upper']['progress_gate'] == 'mu<1/2'

assert reg['population']['literal_subset'] is True
assert reg['directional']['lower_requires_directional_hypothesis'] is True
assert reg['directional']['global_lower_implies_all_directional_lower'] is False
assert reg['directional']['global_upper_implies_all_directional_upper'] is True
assert reg['directional']['shared_edge_map'] == {
    'a':'A_ab,ac', 'b':'A_ab,bc', 'c':'A_ac,bc'
}

ident = reg['exponent_identification']
assert ident['matched_epsilon_bounds_required'] is True
assert ident['implies_log_slope_limit'] is True
assert ident['implies_asymptotic_constant'] is False
assert ident['implies_log_secondary_factor'] is False

for key in [
    'finite_effective_exponent_as_theorem',
    'fixed_prime_zero_density_as_power_saving',
    'global_lower_promoted_to_all_named_directions',
    'new_N2_exponent_proved',
    'true_N2_exponent_identified',
]:
    assert reg['firewalls'][key] is False, key
assert reg['firewalls']['perfect_cuboid_conclusion'] == 'NONE'

for marker in [
    'GLOBAL_LOWER_PROGRESS_GATE=beta>1/4',
    'GLOBAL_UPPER_PROGRESS_GATE=mu<1/2',
    'GLOBAL_LOWER_IMPLIES_ALL_DIRECTIONAL_LOWER=false',
    'GLOBAL_UPPER_IMPLIES_ALL_DIRECTIONAL_UPPER=true',
    'FINITE_EFFECTIVE_EXPONENT_AS_THEOREM=false',
    'NEW_N2_EXPONENT_PROVED=false',
    'TRUE_N2_EXPONENT_IDENTIFIED=false',
    'PERFECT_CUBOID_CONCLUSION=NONE',
]:
    assert marker in res, marker

# Historical checkpoint30 mathematics is preserved; lifecycle may be its own
# submission state or any later state after hostile audit PASS + merge.
assert 'AUDIT_VERDICT=PASS' in a30
assert ctl['checkpoint_status']['30'] in (
    'DERIVED_RECEIVER_CALCULUS_AUDITED_PASS_AWAITING_MERGE',
    'DERIVED_RECEIVER_CALCULUS_AUDITED_PASS_MERGED',
)
assert ctl['checkpoint30']['audit_status'] == 'PASS'
assert ctl['checkpoint30']['pr'] == 1024
if ctl['checkpoint_status']['30'] == 'DERIVED_RECEIVER_CALCULUS_AUDITED_PASS_MERGED':
    assert ctl['checkpoint30']['merge_commit'] == 'cf0f2a378ca6a3338670063821efb513e0aaeb73'
    assert ctl['state']['CURRENT_CHECKPOINT'] >= 40
else:
    assert ctl['state']['CURRENT_CHECKPOINT'] == 30

assert ctl['checkpoint30']['new_N2_exponent_proved'] is False
assert ctl['next_expected_command'] == 'Stage27-audit'

print('STAGE27_30_UPSTREAM_AUDIT_MERGE=PASS')
print('STAGE27_30_CURRENT_CORRIDOR_RECOVERY=PASS')
print('STAGE27_30_GENERIC_RECEIVER_CALCULUS=PASS')
print('STAGE27_30_DIRECTIONAL_PROPAGATION_FIREWALL=PASS')
print('STAGE27_30_EXPONENT_IDENTIFICATION_CONTRACT=PASS')
print('STAGE27_30_LIFECYCLE=PASS')
