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

res = text('stages/stage26/26-70/result.md')
bundle = text('stages/stage26/26-70/self-contained-bundle.md')
arsenal = text('docs/stage26-arsenal-promotion.md')
reg = data('stages/stage26/26-70/closeout-registry.json')
ctl = data('stages/stage26/26-controller.json')
a60 = text('stages/stage26/26-60/audit.md')
a70 = text('stages/stage26/26-70/audit.md')
s18 = text('stages/stage18/final.md')
s20 = text('stages/stage20/final.md')

assert 'AUDIT_VERDICT=PASS' in a60
assert 'M3(B) >>_epsilon B^(1/3-epsilon)' in a60
assert reg['upstream']['checkpoint60_pr'] == 1019
assert reg['upstream']['checkpoint60_merge_commit'] == 'ade92d46148b8c7af0bd0c9165082ee8f11d0e70'
assert reg['upstream']['checkpoint60_audit'] == 'PASS'

for cp in ('10','20','30','40','50','60'):
    assert ctl['checkpoint_status'][cp] == 'PROVED_AUDITED_PASS_MERGED', (cp, ctl['checkpoint_status'][cp])

assert ctl['checkpoint60']['audit_status'] == 'PASS'
assert ctl['checkpoint60']['pr'] == 1019
assert ctl['checkpoint60']['merge_commit'] == 'ade92d46148b8c7af0bd0c9165082ee8f11d0e70'
assert ctl['checkpoint60']['M3_lower_B_one_third_minus_epsilon_accepted'] is True
assert ctl['checkpoint60']['M3_lower_B_one_third_without_epsilon_proved'] is False

assert reg['contract']['M2_M3_literal_subset'] is False
assert reg['contract']['literal_host'] == 'H_ge2=M2+M3'
assert reg['contract']['raw_incidence_host'] == 'P=M2+3M3'
assert reg['final_stack']['Phi_to_zero'] is True
assert reg['final_stack']['Theta_to_zero'] is True
assert reg['final_stack']['Theta_over_Phi_to_three'] is True

for key in [
    'epsilon_free_one_third_lower_proved',
    'true_M3_exponent_identified',
    'M3_asymptotic_proved',
    'upper_lower_match',
    'endpoint_delta_1_over_46_proved',
    'fixed_power_saving_upper_proved',
]:
    assert reg['open_frontier'][key] is False, key

assert reg['artifacts']['self_contained_bundle_required'] is True
assert reg['artifacts']['self_contained_bundle_materialized'] is True
assert reg['artifacts']['arsenal_promotion_required'] is True
assert reg['artifacts']['arsenal_promotion_materialized'] is True

for marker in [
    'M_3(B)\\gg_\\varepsilon B^{1/3-\\varepsilon}',
    'M_3(B)\\ll_\\eta B(\\log B)^{5-\\eta}',
    'SELF_CONTAINED_BUNDLE_MATERIALIZED=true',
    'ARSENAL_PROMOTION_MATERIALIZED=true',
    'TRUE_M3_EXPONENT_IDENTIFIED=false',
    'M3_ASYMPTOTIC_PROVED=false',
    'UPPER_LOWER_MATCH=false',
    'PERFECT_CUBOID_CONCLUSION=NONE',
]:
    assert marker in res, marker

for marker in [
    'M3_LOWER_B_ONE_THIRD_WITHOUT_EPSILON_PROVED=false',
    'TRUE_M3_EXPONENT_IDENTIFIED=false',
    'PERFECT_CUBOID_CONCLUSION=NONE',
]:
    assert marker in bundle, marker

for marker in [
    'S26-W01',
    'S26-W02',
    'S26-W03',
    'TRUE_M3_EXPONENT_IDENTIFIED=false',
]:
    assert marker in arsenal, marker

assert 'M_2(B)\\sim C_{M_2}B(\\log B)^5' in s18
assert 'eta<1/46' in s20
assert reg['firewalls']['finite_data_used_as_asymptotic_proof'] is False
assert reg['firewalls']['perfect_cuboid_conclusion'] == 'NONE'

# Lifecycle: the historical submission state and the later audited/merged closeout
# are both valid. Mathematics above is checked identically in either state.
if ctl['checkpoint_status']['70'] == 'SYNTHESIS_SUBMITTED_PENDING_AUDIT':
    assert ctl['state']['CURRENT_CHECKPOINT'] == 70
    assert ctl['state']['AUDIT_STATUS'] == 'PENDING'
    assert ctl['state']['ADVANCE_ALLOWED'] is False
    assert ctl['state']['MERGE_ALLOWED'] is False
    assert ctl['next_expected_command'] == 'Stage26-audit'
    lifecycle = 'PENDING_FRESH_AUDIT'
elif ctl['checkpoint_status']['70'] == 'SYNTHESIS_AUDITED_PASS_MERGED':
    assert 'AUDIT_VERDICT=PASS' in a70
    assert ctl['status'] == 'CLOSED_AUDITED_PASS_MERGED'
    assert ctl['checkpoint70']['audit_status'] == 'PASS'
    assert ctl['checkpoint70']['pr'] == 1020
    assert ctl['checkpoint70']['merge_commit'] == '8b0472db36c1113198251a7d9646b8c7bfe80331'
    assert ctl['state']['CURRENT_CHECKPOINT'] == 70
    assert ctl['state']['AUDIT_STATUS'] == 'PASS'
    assert ctl['state']['ADVANCE_ALLOWED'] is False
    assert ctl['state']['MERGE_ALLOWED'] is False
    lifecycle = 'AUDITED_PASS_MERGED_CLOSED'
else:
    raise AssertionError(ctl['checkpoint_status']['70'])

print('STAGE26_70_UPSTREAM_AUDITS=PASS')
print('STAGE26_70_FINAL_CORRIDOR=PASS')
print('STAGE26_70_ARTIFACT_DECISIONS=PASS')
print('STAGE26_70_FIREWALL=PASS')
print('STAGE26_70_CLOSEOUT_STATUS=' + lifecycle)
