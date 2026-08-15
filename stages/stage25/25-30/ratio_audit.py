#!/usr/bin/env python3
from pathlib import Path
import json

root = Path(__file__).resolve().parents[3]
result = (root / 'stages/stage25/25-30/result.md').read_text(encoding='utf-8')
ledger = (root / 'stages/stage25/25-30/discovery-ledger.md').read_text(encoding='utf-8')
ctl = json.loads((root / 'stages/stage25/25-controller.json').read_text(encoding='utf-8'))

# Encode B^b (log B)^l as (b,l); multiplication adds exponents.
def mul(x, y):
    return (x[0] + y[0], x[1] + y[1])

direct_lower = (-2, -0.5)
direct_upper = (-1.5, -1)
path_a_lower = mul((-1, 4), (-1, -4.5))
path_a_upper = mul((-1, 4), (-0.5, -5))
path_b_lower = mul((-1, 2), (-1, -2.5))
path_b_upper = mul((-1, 2), (-0.5, -3))

assert path_a_lower == direct_lower
assert path_a_upper == direct_upper
assert path_b_lower == direct_lower
assert path_b_upper == direct_upper

for marker in [
    'ENDPOINT_RATIO_CLASS=VANISHING_POPULATION_RATIO_WITH_INFINITE_TARGET',
    'DIRECT_ENDPOINT_RATIO_CHECK=PASS',
    'PATH_A_PRODUCT_CHECK=PASS',
    'PATH_B_PRODUCT_CHECK=PASS',
    'THREE_WAY_CONSISTENCY=PASS',
    'PROBABILISTIC_INDEPENDENCE_INFERRED=false',
    'DIRECTIONAL_STAGE23_C_LOWER=PROVED_TARGET_ONLY',
    'DIRECTIONAL_SOURCE_CHANNEL_ADAPTER_PROVED=false',
    'DIRECTIONAL_UPPER_ALL=NOT_PROVED',
    'DIRECTIONAL_C_TWO_SIDED_ENVELOPE=NOT_PROVED',
    'DIRECTIONAL_RATIO_REFINEMENT_STATUS=OPEN_GATE_ADAPTER_REQUIRED',
    'DIRECTIONAL_OVERCLAIM_REPAIRED=true',
    'CONTROLLER_HISTORY_RESTORE_STATUS=COMPLETE_IN_CONTROLLER',
    'FINITE_DATA_USED_AS_PROOF=false',
    'EXPLORATION_EVIDENCE_COMPLETE=true',
]:
    assert marker in result, marker

for marker in [
    'DISCOVERY_CHECKPOINT=Stage25-30',
    'SEARCHED_PATHS=',
    'SEARCH_TERMS=',
    'STRUCTURAL_SIGNATURES=',
    'DEPENDENCY_NEIGHBORS=',
    'CANDIDATES_FOUND=',
    'CANDIDATES_ACCEPTED=',
    'CANDIDATES_REJECTED_WITH_REASON=',
    'POPULATION_ADAPTERS_PROVED=',
    'NO_DIRECTIONAL_CHAMBER_TO_SHARED_EDGE_ADAPTER_PROVED',
    'DIRECTIONAL_REFINEMENT_CHECK=OPEN_GATE_ADAPTER_REQUIRED',
    'DIRECTIONAL_OVERCLAIM_REPAIRED=true',
    'DISCOVERY_LEDGER_STATUS=COMPLETE_REPAIRED_AFTER_DIRECTIONAL_AUDIT_FAIL',
    'LIVE_ROUTE_CANDIDATES=',
    'SUBLANES_OPENED=NONE',
    'SUBLANES_REJECTED=',
    'SUBLANE_REJECTION_REASON=',
    'FORMULA_SUBSTITUTION_ONLY=false',
]:
    assert marker in ledger, marker

assert ctl['stage'] == 'Stage25'
assert ctl['parent_class'] == 'transition'
assert ctl['checkpoint_status']['10'] == 'PROVED_AUDITED_PASS'
assert ctl['checkpoint_status']['20'] == 'COMPUTED_AUDITED_PASS'
status30 = ctl['checkpoint_status']['30']
assert status30 in ('REPAIR_SUBMITTED_FOR_FRESH_AUDIT', 'PROVED_AUDITED_PASS')
current = int(ctl['state']['CURRENT_CHECKPOINT'])
assert current >= 30

# Historical audited controller provenance must survive checkpoint30 append.
cp10 = ctl['checkpoint10']
assert cp10['previous_audit'] == 'FAIL'
assert cp10['population_contract_frozen'] is True
assert cp10['ratio_semantics_frozen'] is True
assert cp10['repair_status'] == 'COMPLETE_AUDITED_PASS'

cp20 = ctl['checkpoint20']
for key in ['replay','workflow','source_counts','target_object_ledger','target_manifest','target_cross_oracle']:
    assert cp20[key]
assert cp20['num_r01_manifest_binding'] == 'PASS'
assert cp20['num_r01_exactly_two_row_check'] == 'PASS'
assert cp20['committed_matched_grid'] == 'PASS'
assert cp20['audit'] == 'PASS'

cp30 = ctl['checkpoint30']
assert cp30['previous_audit'] == 'FAIL'
assert cp30['three_way_consistency'] == 'PASS'
assert cp30['directional_stage23_c_lower'] == 'PROVED_TARGET_ONLY'
assert cp30['directional_source_channel_adapter_proved'] is False
assert cp30['directional_upper_all'] == 'NOT_PROVED'
assert cp30['directional_c_two_sided_envelope'] == 'NOT_PROVED'
assert cp30['directional_ratio_refinement_status'] == 'OPEN_GATE_ADAPTER_REQUIRED'
assert cp30['directional_overclaim_repaired'] is True
assert cp30['controller_history_restore_status'] == 'COMPLETE'
assert cp30['exploration_evidence_complete'] is True
assert cp30['finite_data_used_as_proof'] is False
assert len(ctl['audit_history']) >= 3
assert ctl['repair']['directional_ratio_claims_downgraded'] is True
assert ctl['repair']['controller_checkpoint10_history_restored'] is True
assert ctl['repair']['controller_checkpoint20_history_restored'] is True

if status30 == 'REPAIR_SUBMITTED_FOR_FRESH_AUDIT':
    assert current == 30
    assert ctl['state']['AUDIT_STATUS'] == 'PENDING'
    assert ctl['state']['ADVANCE_ALLOWED'] is False
    assert ctl['state']['MERGE_ALLOWED'] is False
    assert ctl['state']['NEXT_CHECKPOINT'] == 30
    assert cp30['audit'] == 'PENDING_REAUDIT'
    assert cp30['repair_status'] == 'SUBMITTED_FOR_FRESH_AUDIT'
    assert cp30['advance_allowed'] is False
    assert cp30['merge_allowed'] is False
    assert ctl['discovery_audit']['verdict'] == 'PENDING_REAUDIT'
    assert ctl['last_audit']['verdict'] == 'FAIL'
    assert ctl['repair']['status'] == 'SUBMITTED_FOR_FRESH_AUDIT'
else:
    assert cp30['audit'] == 'PASS'
    assert cp30['repair_status'] == 'COMPLETE_AUDITED_PASS'
    assert cp30['advance_allowed'] is True
    assert cp30['merge_allowed'] is True
    assert ctl['repair']['status'] == 'COMPLETE_AUDITED_PASS'
    assert any(x['checkpoint'] == 30 and x['verdict'] == 'PASS' for x in ctl['audit_history'])
    if current == 30:
        assert ctl['state']['AUDIT_STATUS'] == 'PASS'
        assert ctl['state']['ADVANCE_ALLOWED'] is True
        assert ctl['state']['MERGE_ALLOWED'] is True
        assert ctl['state']['NEXT_CHECKPOINT'] == 40
        assert ctl['discovery_audit']['verdict'] == 'PASS'
        assert ctl['last_audit']['checkpoint'] == 30
        assert ctl['last_audit']['verdict'] == 'PASS'
        assert ctl['next_expected_command'] == 'merge PR #982; then Stage25-main-batch'
    else:
        # Once Stage25 advances, current state/discovery_audit belong to the later
        # checkpoint.  Checkpoint30 stays immutable as a historical audited PASS.
        assert current > 30
        assert ctl['last_audit']['checkpoint'] >= 30
        assert ctl['last_audit']['verdict'] == 'PASS'

print('DIRECT_LOWER_SCALE=B^-2(logB)^-1/2:PASS')
print('DIRECT_UPPER_SCALE=B^-3/2+eps(logB)^-1:PASS')
print('PATH_A_SCALE_MATCH=PASS')
print('PATH_B_SCALE_MATCH=PASS')
print('THREE_WAY_CONSISTENCY=PASS')
print('DIRECTIONAL_OVERCLAIM_DOWNGRADE=PASS')
print('CONTROLLER_HISTORY_RESTORE=PASS')
print(f'CURRENT_CHECKPOINT={current}')
print('STAGE25_30_RATIO_AUDIT=PASS')
