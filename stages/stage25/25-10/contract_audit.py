from pathlib import Path
import json

root = Path(__file__).resolve().parents[3]
result = (root / 'stages/stage25/25-10/result.md').read_text()
ledger = (root / 'stages/stage25/25-10/discovery-ledger.md').read_text()
lattice = (root / 'stages/stage25/25-10/comparison-lattice.md').read_text()
ctl = json.loads((root / 'stages/stage25/25-controller.json').read_text())

required_result = [
    'LITERAL_SUBSET_TRANSITION=false',
    'RATIO_SEMANTICS=MATCHED_COMBINED_POPULATION_SIZE_RATIO',
    'M_1(B)\\sim\\frac{3}{4\\pi^2}B^2\\log B',
    'N_2(B)\\gg\\sqrt{\\log B}',
    'N_2(B)\\ll_\\varepsilon B^{1/2+\\varepsilon}',
    'PATH_A=Stage22_then_Stage24',
    'PATH_B=Stage21_then_Stage23',
    'PATH_IDENTITIES_FROZEN=true',
    'NUM_REUSE_CHECK=PASS',
    'NUM_ASSETS_REUSED=NUM-R01,NUM-R06,NUM-R07',
    'REPO_REUSE_PREFLIGHT=PASS',
    'REUSE_MATCH_STATUS=MIXED',
    'STRONGEST_KNOWN_CHECK=PASS',
    'DISCOVERY_CHECKPOINT=Stage25-10',
]
for marker in required_result:
    assert marker in result, marker

required_ledger = [
    'REPO_REUSE_PREFLIGHT=PASS',
    'REUSE_SEARCH_SCOPE=ARSENAL,NUM_INDEX,STAGES,SUPPLEMENTS,ARCHIVE,PRS',
    'REUSED_RESULTS=',
    'REUSE_MATCH_STATUS=MIXED',
    'STRONGEST_KNOWN_CHECK=PASS',
    'STRONGER_PRIOR_RESULT_FOUND=true',
    'NEW_RESEARCH_JUSTIFIED=NOT_REQUIRED_AT_CHECKPOINT10_CONTRACT_FREEZE',
    'DISCOVERY_CHECKPOINT=Stage25-10',
    'SEARCHED_PATHS=',
    'SEARCH_TERMS=',
    'STRUCTURAL_SIGNATURES=',
    'DEPENDENCY_NEIGHBORS=',
    'CANDIDATES_FOUND=',
    'CANDIDATES_ACCEPTED=',
    'CANDIDATES_REJECTED_WITH_REASON=',
    'POPULATION_ADAPTERS_PROVED=',
    'DISCOVERY_LEDGER_STATUS=COMPLETE',
    'S1415-ATTACK-0215',
    'S1415-ATTACK-0748',
    'S1415-ATTACK-0817',
    'D25-10-1', 'D25-10-2', 'D25-10-3', 'D25-10-4', 'D25-10-5',
    'NUM_POPULATION_MATCH=ADAPTER_PROVED',
]
for marker in required_ledger:
    assert marker in ledger, marker

for marker in [
    'PATH_A=Stage22_then_Stage24',
    'PATH_B=Stage21_then_Stage23',
    'PATH_PRODUCTS_EXACT=true',
    'PROBABILISTIC_INDEPENDENCE_INFERRED=false',
    'DOUBLE_CHARGE_FIREWALL=ACTIVE',
]:
    assert marker in lattice, marker

assert ctl['stage'] == 'Stage25'
assert ctl['parent_class'] == 'transition'
assert ctl['transition'] == 'Stage16 -> Stage19'
assert ctl['state']['CURRENT_CHECKPOINT'] == 10
assert ctl['literal_subset_transition'] is False
assert ctl['checkpoint10']['path_count_ratio_identities_exact'] is True
assert ctl['checkpoint10']['path_products_are_independence_claim'] is False
assert ctl['checkpoint10']['repo_reuse_preflight'] == 'PASS'
assert ctl['checkpoint10']['strongest_known_check'] == 'PASS'
assert ctl['checkpoint10']['exploration_evidence_complete'] is True
assert ctl['checkpoint10']['repo_reuse_handoff_complete'] is True
assert ctl['checkpoint10']['discovery_evidence_block_complete'] is True
assert ctl['checkpoint10']['parent_class_normalized'] is True
assert ctl['checkpoint10']['num_reuse_check'] == 'PASS'
assert ctl['repository_reuse']['REPO_REUSE_PREFLIGHT'] == 'PASS'
assert ctl['repository_reuse']['DISCOVERY_LEDGER_STATUS'] == 'COMPLETE'
assert ctl['repair']['mathematics_reopened'] is False
assert ctl['repair']['counts_recomputed'] is False

cp10_status = ctl['checkpoint_status']['10']
if cp10_status == 'REPAIR_SUBMITTED_FOR_FRESH_AUDIT':
    assert ctl['state']['AUDIT_STATUS'] == 'PENDING'
    assert ctl['state']['ADVANCE_ALLOWED'] is False
    assert ctl['state']['NEXT_CHECKPOINT'] == 10
    assert ctl['state']['MERGE_ALLOWED'] is False
    assert ctl['discovery_audit']['verdict'] == 'PENDING_REAUDIT'
    assert ctl['next_expected_command'] == 'Stage25-audit'
elif cp10_status == 'PROVED_AUDITED_PASS':
    assert ctl['state']['AUDIT_STATUS'] == 'PASS'
    assert ctl['state']['ADVANCE_ALLOWED'] is True
    assert ctl['state']['NEXT_CHECKPOINT'] == 20
    assert ctl['state']['MERGE_ALLOWED'] is True
    assert ctl['checkpoint10']['audit'] == 'PASS'
    assert ctl['checkpoint10']['advance_allowed'] is True
    assert ctl['checkpoint10']['merge_allowed'] is True
    assert ctl['discovery_audit']['verdict'] == 'PASS'
    assert ctl['last_audit']['verdict'] == 'PASS'
    assert ctl['last_audit']['merge_allowed'] is True
    assert ctl['next_expected_command'] == 'merge PR #980; then Stage25-main-batch'
else:
    raise AssertionError(f'unexpected checkpoint10 status: {cp10_status}')

print('Stage25-10 contract + reuse/discovery audit: PASS')
print(f'CONTROLLER_STATE={cp10_status}')
