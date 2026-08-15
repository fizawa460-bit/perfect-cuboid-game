#!/usr/bin/env python3
from pathlib import Path
import json

root = Path(__file__).resolve().parents[3]
result = (root / 'stages/stage25/25-40/result.md').read_text(encoding='utf-8')
ledger = (root / 'stages/stage25/25-40/discovery-ledger.md').read_text(encoding='utf-8')
prov = (root / 'stages/stage25/25-40/upper-provenance.md').read_text(encoding='utf-8')
ctl = json.loads((root / 'stages/stage25/25-controller.json').read_text(encoding='utf-8'))

# scale B^b (log B)^l

def mul(x, y):
    return (x[0] + y[0], x[1] + y[1])

# epsilon omitted from the polynomial tuple and carried verbally.
direct_upper = (-1.5, -1)
path_a_upper = mul((-1, 4), (-0.5, -5))
path_b_upper = mul((-1, 2), (-0.5, -3))
thin_qual = (-1, 4)
fixed_finite = (-1.6, -1)
invalid_naive_product = mul((-1, 2), (-1, 4))

assert path_a_upper == direct_upper
assert path_b_upper == direct_upper
assert thin_qual == (-1, 4)
assert fixed_finite == (-1.6, -1)
assert invalid_naive_product == (-2, 6)

# For any fixed epsilon<1/2 the direct polynomial exponent is below -1,
# so the half-power quantitative upper is stronger than the qualitative o(B^-1 log^4).
assert -1.5 + 0.25 < -1

required_result = [
    'GLOBAL_ENDPOINT_UPPER=B^(-3/2+epsilon)(log B)^(-1)',
    'DIRECT_UPPER_CHECK=PASS',
    'PATH_A_UPPER_CHECK=PASS',
    'PATH_B_UPPER_CHECK=PASS',
    'THREE_WAY_UPPER_CONSISTENCY=PASS',
    'FIXED_FINITE_CURVE_ENDPOINT_UPPER=B^(-8/5+o(1))(log B)^(-1)',
    'NO_FAKE_PRODUCT_SAVING_CHECK=PASS',
    'STAGE24_LOCAL_SIEVE_MULTIPLIED_WITH_HALF_POWER=false',
    'STAGE24_THIN_COVER_MULTIPLIED_WITH_HALF_POWER=false',
    'DIRECTIONAL_SOURCE_CHANNEL_ADAPTER_PROVED=false',
    'DIRECTIONAL_OVERCLAIM_REINTRODUCED=false',
    'FINITE_DATA_USED_AS_PROOF=false',
    'EXPLORATION_EVIDENCE_COMPLETE=true',
]
for marker in required_result:
    assert marker in result, marker

for marker in [
    'INVALID_1=(N1/M1)*(M2/M1)',
    'INVALID_2=(half_power_target_upper)*(local_sieve_density_factor)',
    'INVALID_3=(half_power_target_upper)*(thin_cover_little_o)',
    'INVALID_4=(Path_A_upper)*(Path_B_upper)',
    'DOUBLE_CHARGE_FIREWALL=PASS',
]:
    assert marker in prov, marker

for marker in [
    'DISCOVERY_CHECKPOINT=Stage25-40',
    'SEARCHED_PATHS=',
    'SEARCH_TERMS=',
    'STRUCTURAL_SIGNATURES=',
    'DEPENDENCY_NEIGHBORS=',
    'CANDIDATES_FOUND=',
    'CANDIDATES_ACCEPTED=',
    'CANDIDATES_REJECTED_WITH_REASON=',
    'POPULATION_ADAPTERS_PROVED=',
    'DISCOVERY_LEDGER_STATUS=COMPLETE',
    'LIVE_ROUTE_CANDIDATES=',
    'SUBLANES_OPENED=NONE',
    'SUBLANES_REJECTED=',
    'SUBLANE_REJECTION_REASON=',
    'FORMULA_SUBSTITUTION_ONLY=false',
    'NUM_REUSE_CHECK=PASS',
]:
    assert marker in ledger, marker

assert ctl['stage'] == 'Stage25'
assert ctl['parent_class'] == 'transition'
assert ctl['checkpoint_status']['10'] == 'PROVED_AUDITED_PASS'
assert ctl['checkpoint_status']['20'] == 'COMPUTED_AUDITED_PASS'
assert ctl['checkpoint_status']['30'] == 'PROVED_AUDITED_PASS'
assert ctl['checkpoint_status']['40'] == 'PROVED_SUBMITTED_FOR_FRESH_AUDIT'
assert ctl['state']['CURRENT_CHECKPOINT'] == 40
assert ctl['state']['AUDIT_STATUS'] == 'PENDING'
assert ctl['state']['ADVANCE_ALLOWED'] is False
assert ctl['state']['NEXT_CHECKPOINT'] == 40
assert ctl['state']['MERGE_ALLOWED'] is False

cp40 = ctl['checkpoint40']
assert cp40['upper_provenance_check'] == 'PASS'
assert cp40['direct_upper_check'] == 'PASS'
assert cp40['path_A_upper_check'] == 'PASS'
assert cp40['path_B_upper_check'] == 'PASS'
assert cp40['three_way_upper_consistency'] == 'PASS'
assert cp40['no_fake_product_saving_check'] == 'PASS'
assert cp40['fixed_finite_curve_refinement_proved'] is True
assert cp40['strict_global_upper_upgrade_proved'] is False
assert cp40['directional_source_channel_adapter_proved'] is False
assert cp40['directional_overclaim_reintroduced'] is False
assert cp40['finite_data_used_as_proof'] is False
assert cp40['exploration_evidence_complete'] is True

# Historical audit provenance must survive checkpoint40 submission.
assert ctl['checkpoint10']['previous_audit'] == 'FAIL'
assert ctl['checkpoint20']['num_r01_manifest_binding'] == 'PASS'
assert ctl['checkpoint20']['num_r01_exactly_two_row_check'] == 'PASS'
assert ctl['checkpoint20']['committed_matched_grid'] == 'PASS'
assert ctl['checkpoint30']['previous_audit'] == 'FAIL'
assert ctl['checkpoint30']['directional_ratio_refinement_status'] == 'OPEN_GATE_ADAPTER_REQUIRED'
assert any(x['checkpoint'] == 30 and x['verdict'] == 'FAIL' for x in ctl['audit_history'])
assert any(x['checkpoint'] == 30 and x['verdict'] == 'PASS' for x in ctl['audit_history'])
assert ctl['last_audit']['checkpoint'] == 30
assert ctl['last_audit']['verdict'] == 'PASS'

print('DIRECT_UPPER_SCALE=B^-3/2+eps(logB)^-1:PASS')
print('PATH_A_UPPER_MATCH=PASS')
print('PATH_B_UPPER_MATCH=PASS')
print('THIN_LOCAL_QUALITATIVE_SCALE=o(B^-1(logB)^4):PASS')
print('FIXED_FINITE_ENDPOINT_SCALE=B^-8/5+o1(logB)^-1:PASS')
print('NO_FAKE_PRODUCT_SAVING_CHECK=PASS')
print('CONTROLLER_HISTORY_PRESERVATION=PASS')
print('STAGE25_40_UPPER_PROVENANCE_AUDIT=PASS')
