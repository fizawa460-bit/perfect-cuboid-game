#!/usr/bin/env python3
from pathlib import Path
import json

root = Path(__file__).resolve().parents[3]
result = (root / 'stages/stage25/25-20/result.md').read_text()
ledger = (root / 'stages/stage25/25-20/discovery-ledger.md').read_text()
ctl = json.loads((root / 'stages/stage25/25-controller.json').read_text())
matched = (root / 'stages/stage25/25-20/matched-counts.csv').read_text().strip().splitlines()

for marker in [
    'REPO_REUSE_PREFLIGHT=PASS',
    'NUM_REUSE_CHECK=PASS',
    'NUM_ASSETS_REUSED=NUM-R01,NUM-R02',
    'NUM_POPULATION_MATCH=ADAPTER_PROVED',
    'FINITE_DATA_USED_AS_PROOF=false',
    'FINITE_RATIO_MONOTONE=false',
    'MATCHED_GRID_ROWS=8',
    'NEXT_EXPECTED_COMMAND=Stage25-audit',
]:
    assert marker in result, marker

for marker in [
    '## SEARCHED_PATHS',
    '## SEARCH_TERMS',
    '## STRUCTURAL_SIGNATURES',
    '## DEPENDENCY_NEIGHBORS',
    '## CANDIDATES_FOUND',
    '## CANDIDATES_ACCEPTED',
    '## CANDIDATES_REJECTED_WITH_REASON',
    '## POPULATION_ADAPTERS_PROVED',
    'DISCOVERY_LEDGER_STATUS=COMPLETE',
]:
    assert marker in ledger, marker

assert len(matched) == 9
assert ctl['parent_class'] == 'transition'
assert ctl['checkpoint_status']['10'] == 'PROVED_AUDITED_PASS'
assert ctl['state']['CURRENT_CHECKPOINT'] == 20
cp = ctl['checkpoint20']
assert cp['matched_grid_rows'] == 8
assert cp['new_cuboid_enumeration_performed'] is False
assert cp['exact_ledger_filter_only'] is True
assert cp['stage19_cross_oracle'] == 'PASS'
assert cp['num_r01_adapter'] == 'PASS'
assert cp['finite_ratio_monotone'] is False
assert cp['finite_data_used_as_proof'] is False
assert cp['searched_paths_recorded'] is True
assert cp['candidates_found_recorded'] is True
assert cp['candidates_accepted_recorded'] is True
assert cp['candidates_rejected_with_reason_recorded'] is True
assert cp['population_adapters_proved_recorded'] is True

submission = ctl['checkpoint_status']['20'] == 'COMPUTED_SUBMITTED_FOR_FRESH_AUDIT'
audited = ctl['checkpoint_status']['20'] == 'COMPUTED_AUDITED_PASS'
assert submission or audited

if submission:
    assert ctl['state']['AUDIT_STATUS'] == 'PENDING'
    assert ctl['state']['ADVANCE_ALLOWED'] is False
    assert ctl['state']['MERGE_ALLOWED'] is False
    assert ctl['state']['NEXT_CHECKPOINT'] == 20
    assert cp['status'] == 'COMPUTED_SUBMITTED_FOR_FRESH_AUDIT'
    assert cp['audit'] == 'PENDING'
    assert cp['advance_allowed'] is False
    assert cp['merge_allowed'] is False
    assert ctl['discovery_audit']['verdict'] == 'PENDING'
    assert ctl['next_expected_command'] == 'Stage25-audit'
else:
    assert ctl['state']['AUDIT_STATUS'] == 'PASS'
    assert ctl['state']['ADVANCE_ALLOWED'] is True
    assert ctl['state']['MERGE_ALLOWED'] is True
    assert ctl['state']['NEXT_CHECKPOINT'] == 30
    assert cp['status'] == 'COMPUTED_AUDITED_PASS'
    assert cp['audit'] == 'PASS'
    assert cp['advance_allowed'] is True
    assert cp['merge_allowed'] is True
    assert ctl['discovery_audit']['verdict'] == 'PASS'
    assert ctl['last_audit']['checkpoint'] == 20
    assert ctl['last_audit']['verdict'] == 'PASS'
    assert ctl['next_expected_command'] == 'merge PR #981; then Stage25-main-batch'

print('Stage25-20 submission/audited-state contract: PASS')
