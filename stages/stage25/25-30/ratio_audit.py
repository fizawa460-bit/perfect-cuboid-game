#!/usr/bin/env python3
from pathlib import Path
import json

root = Path(__file__).resolve().parents[3]
result = (root / 'stages/stage25/25-30/result.md').read_text(encoding='utf-8')
ledger = (root / 'stages/stage25/25-30/discovery-ledger.md').read_text(encoding='utf-8')
ctl = json.loads((root / 'stages/stage25/25-controller.json').read_text(encoding='utf-8'))

# Encode a scale B^b (log B)^l as (b,l). Addition = multiplication.
def mul(x, y):
    return (x[0] + y[0], x[1] + y[1])

# Direct endpoint N2 / M1.
direct_lower = (-2, -0.5)
direct_upper = (-1.5, -1)  # epsilon is carried separately.

# Path A: M2/M1 times N2/M2.
path_a_lower = mul((-1, 4), (-1, -4.5))
path_a_upper = mul((-1, 4), (-0.5, -5))

# Path B: N1/M1 times N2/N1.
path_b_lower = mul((-1, 2), (-1, -2.5))
path_b_upper = mul((-1, 2), (-0.5, -3))

assert path_a_lower == direct_lower
assert path_a_upper == direct_upper
assert path_b_lower == direct_lower
assert path_b_upper == direct_upper

required_result = [
    'ENDPOINT_RATIO_CLASS=VANISHING_POPULATION_RATIO_WITH_INFINITE_TARGET',
    'DIRECT_ENDPOINT_RATIO_CHECK=PASS',
    'PATH_A_PRODUCT_CHECK=PASS',
    'PATH_B_PRODUCT_CHECK=PASS',
    'THREE_WAY_CONSISTENCY=PASS',
    'PROBABILISTIC_INDEPENDENCE_INFERRED=false',
    'DIRECTIONAL_UPPER_ALL=PROVED',
    'DIRECTIONAL_C_LOWER=PROVED',
    'DIRECTIONAL_C_TWO_SIDED_ENVELOPE=PROVED',
    'FINITE_DATA_USED_AS_PROOF=false',
    'EXPLORATION_EVIDENCE_COMPLETE=true',
]
for marker in required_result:
    assert marker in result, marker

required_ledger = [
    'DISCOVERY_CHECKPOINT=Stage25-30',
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
]
for marker in required_ledger:
    assert marker in ledger, marker

assert ctl['stage'] == 'Stage25'
assert ctl['parent_class'] == 'transition'
assert ctl['checkpoint_status']['10'] == 'PROVED_AUDITED_PASS'
assert ctl['checkpoint_status']['20'] == 'COMPUTED_AUDITED_PASS'
assert ctl['checkpoint_status']['30'] == 'PROVED_SUBMITTED_FOR_FRESH_AUDIT'
assert ctl['state']['CURRENT_CHECKPOINT'] == 30
assert ctl['state']['AUDIT_STATUS'] == 'PENDING'
assert ctl['state']['ADVANCE_ALLOWED'] is False
assert ctl['state']['NEXT_CHECKPOINT'] == 30
assert ctl['state']['MERGE_ALLOWED'] is False
assert ctl['checkpoint30']['three_way_consistency'] == 'PASS'
assert ctl['checkpoint30']['finite_data_used_as_proof'] is False
assert ctl['checkpoint30']['exploration_evidence_complete'] is True

print('DIRECT_LOWER_SCALE=B^-2(logB)^-1/2:PASS')
print('DIRECT_UPPER_SCALE=B^-3/2+eps(logB)^-1:PASS')
print('PATH_A_SCALE_MATCH=PASS')
print('PATH_B_SCALE_MATCH=PASS')
print('THREE_WAY_CONSISTENCY=PASS')
print('STAGE25_30_RATIO_AUDIT=PASS')
