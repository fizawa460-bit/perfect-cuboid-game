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
    'NEXT_EXPECTED_COMMAND=Stage25-audit',
]
for marker in required_result:
    assert marker in result, marker

for marker in [
    'D25-10-1', 'D25-10-2', 'D25-10-3', 'D25-10-4', 'D25-10-5',
    'NUM_POPULATION_MATCH=ADAPTER_PROVED'
]:
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
assert ctl['transition'] == 'Stage16 -> Stage19'
assert ctl['checkpoint_status']['10'] == 'SUBMITTED_FOR_FRESH_AUDIT'
assert ctl['state']['CURRENT_CHECKPOINT'] == 10
assert ctl['state']['AUDIT_STATUS'] == 'PENDING'
assert ctl['state']['ADVANCE_ALLOWED'] is False
assert ctl['state']['MERGE_ALLOWED'] is False
assert ctl['literal_subset_transition'] is False
assert ctl['checkpoint10']['path_count_ratio_identities_exact'] is True
assert ctl['checkpoint10']['path_products_are_independence_claim'] is False
assert ctl['checkpoint10']['num_reuse_check'] == 'PASS'
assert ctl['next_expected_command'] == 'Stage25-audit'

print('Stage25-10 contract audit: PASS')
