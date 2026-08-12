from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

def text(rel):
    return (ROOT / rel).read_text(encoding='utf-8')

x = text('stages/stage14/14-Work-clX50/result.md')
m = text('docs/stage14-toolbox/work-clX50-receiver-matrix.md')
q = text('stages/stage14/14-q24/result.md')
qs = text('stages/stage14/14-q24/summary.md')
s153 = text('stages/stage14/14-s7-153/result.md')
s154 = text('stages/stage14/14-s7-154/result.md')
s155 = text('stages/stage14/14-s7-155/result.md')

for token in [
    'FIRST_REVERSE_EXACT_COMMON_GCD_CONSUMED=true',
    'PQ_COMMON_PRIME_SUPPORT_LOCALIZATION_CONSUMED=true',
    'PQ_COPRIME_SIDE_MOVERS_CONSUMED=true',
    'COMMON_CORE_SIDE_COPRIME_DECOMPOSITION_RECHARGE_FORBIDDEN=true',
    'S_COMMON_CORE_COPRIME_SIDE_THEOREM_SPECIES_COUNT=2',
    'PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false',
    'POST_MASK_REMAINS_SEPARATELY_CHARGED=true',
    'TH34_NEEDED=false',
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    'STRICT_SUBSQRT_POWER_SAVING_PROVED=false',
]:
    assert token in x, token

for token in [
    'FIRST_REVERSE_EXACT_COMMON_GCD_RECHARGED=false',
    'PQ_COMMON_PRIME_SUPPORT_LOCALIZATION_RECHARGED=false',
    'PQ_COPRIME_SIDE_MOVERS_RECHARGED=false',
    'PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false',
    'POST_MASK_REMAINS_SEPARATELY_CHARGED=true',
]:
    assert token in m, token

for token in [
    'DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0',
    'MOVING_COMMON_CORE_TWO_COPRIME_SIDE_DIRECT_THEOREM_FOUND=false',
    'COMMON_CORE_CONDITIONING_ADAPTER_PROVED=false',
    'COPRIME_SIDE_POSITIVE_DENSITY_FACTORIZATION_PROVED=false',
    'RECIPROCAL_CRT_PRESERVING_EULER_PRODUCT_ADAPTER_PROVED=false',
    'Q24_COMMON_CORE_CONDITIONING_TEST=Stage14-s7-156',
    'Q24_COPRIME_SIDE_EULER_PRODUCT_OR_SIEVE_FACTOR_TEST=Stage14-s7-157+',
]:
    assert token in q, token
    assert token in qs, token

assert 'FIRST_REVERSE_EXACT_COMMON_GCD_PROVED=true' in s153
assert 'PQ_COMMON_PRIME_SUPPORT_LOCALIZED_TO_H=true' in s154
assert 'PQ_COPRIME_SIDE_MOVERS_PROVED=true' in s154
assert 'Q24_THEOREM_TARGET_NOW_STABLE=true' in s155
assert 'Q24_NEEDED=true' in s155

print('Stage14-Work-clX50 + q24 deterministic audit: PASS')
