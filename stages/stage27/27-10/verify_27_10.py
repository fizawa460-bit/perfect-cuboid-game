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

res = text('stages/stage27/27-10/result.md')
road = text('docs/stage27-roadmap.md')
reg = data('stages/stage27/27-10/route-registry.json')
ctl = data('stages/stage27/27-controller.json')
s26ctl = data('stages/stage26/26-controller.json')
s26audit = text('stages/stage26/26-70/audit.md')
s26close = text('stages/stage26/postmerge-closeout.md')
s19 = text('stages/stage19/post-stage25-50-supersession.md')
s24 = text('stages/stage24/post-stage25-r01/result.md')
s25 = text('stages/stage25/25-reentry-20/result.md')
a10 = text('stages/stage27/27-10/audit.md')

assert 'AUDIT_VERDICT=PASS' in s26audit
assert 'SOURCE_MERGE_COMMIT=8b0472db36c1113198251a7d9646b8c7bfe80331' in s26close
assert s26ctl['status'] == 'CLOSED_AUDITED_PASS_MERGED'
assert s26ctl['checkpoint_status']['70'] == 'SYNTHESIS_AUDITED_PASS_MERGED'

for marker in ['N_2(B)\\gg B^{1/4}','N_2(B)\\ll_\\varepsilon B^{1/2+\\varepsilon}','TRUE_TARGET_EXPONENT_IDENTIFIED=false']:
    assert marker in s19, marker
for marker in ['B^{-3/4}(\\log B)^{-5}','ALL_DIRECTIONAL_SURVIVAL_LOWER_SYNCED=true','STRICT_SUB_SQRT_WHOLE_FAMILY_UPPER_PROVED=false']:
    assert marker in s24, marker
for marker in ['GLOBAL_N2_EXPONENT_UPGRADED=false','MOVING_FAMILY_UNIFORMITY_PROVED=false','GROWING_MODULUS_SIEVE_UNIFORMITY_PROVED=false']:
    assert marker in s25, marker

assert reg['contract']['literal_subset'] is True
assert reg['current_surface']['N2_lower'] == 'B^(1/4)'
assert reg['current_surface']['N2_upper'] == 'B^(1/2+epsilon)'
assert reg['current_surface']['directional_lower_all_three'] == 'B^(1/4)'
assert reg['routes']['L27_LOWER_FAMILY']['direct_stage26_M3_transfer_allowed'] is False
assert reg['routes']['U27_SUBHALF_UPPER']['fixed_prime_zero_density_is_power_saving'] is False
assert reg['routes']['D27_FINITE_DIAGNOSTIC']['asymptotic_proof_allowed'] is False

for key in ['finite_data_used_as_asymptotic_proof','M3_population_used_as_N2_lower','fixed_prime_sieve_promoted_to_power_saving','independence_product_claimed','true_N2_exponent_identified']:
    assert reg['firewalls'][key] is False, key
assert reg['firewalls']['perfect_cuboid_conclusion'] == 'NONE'

assert 'AUDIT_VERDICT=PASS' in a10
assert ctl['checkpoint_status']['10'] in ('CONTRACT_AUDITED_PASS_AWAITING_MERGE','CONTRACT_AUDITED_PASS_MERGED')
assert ctl['checkpoint10']['audit_status'] == 'PASS'
assert ctl['checkpoint10']['pr'] == 1021
if ctl['checkpoint_status']['10'] == 'CONTRACT_AUDITED_PASS_MERGED':
    assert ctl['checkpoint10']['merge_commit'] == 'f509bba40197262051aad2f22775583b1571a6f5'
    assert ctl['state']['CURRENT_CHECKPOINT'] >= 20
    assert ctl['next_expected_command'].startswith('Stage27')
    assert ctl['next_expected_command'].endswith('-audit')
else:
    assert ctl['state']['CURRENT_CHECKPOINT'] == 10

for marker in ['CURRENT_N2_LOWER=N2(B)>>B^(1/4)','CURRENT_N2_UPPER=N2(B)<<_epsilon B^(1/2+epsilon)','STAGE26_M3_LOWER_TRANSFERRED_TO_N2=false','FINITE_DATA_USED_AS_ASYMPTOTIC_PROOF=false','TRUE_N2_EXPONENT_IDENTIFIED=false','PERFECT_CUBOID_CONCLUSION=NONE']:
    assert marker in res, marker
for marker in ['PROGRAM=TRUE_N2_EXPONENT_ATTACK','Stage26\'s `w^3` divisor-fiber argument is a methodological template only','FIXED_PRIME_ZERO_DENSITY_AS_POWER_SAVING=false','Stage28 boundary']:
    assert marker in road, marker

print('STAGE27_10_STAGE26_ENTRY_GATE=PASS')
print('STAGE27_10_N2_CONTRACT=PASS')
print('STAGE27_10_CURRENT_CORRIDOR=PASS')
print('STAGE27_10_ROUTE_PREFLIGHT=PASS')
print('STAGE27_10_LIFECYCLE=PASS')
