from pathlib import Path

base = Path('stages/stage15')
dp = (base/'15-6dp/result.md').read_text()
dq = (base/'15-6dq/result.md').read_text()
dr = (base/'15-6dr/result.md').read_text()

assert 'STAGE15_6DP_CHARACTER_OPERATOR_EXACT=true' in dp
assert 'STAGE15_6DP_DUAL_INEQUALITY_EXACT=true' in dp
assert 'STAGE15_6DP_ZERO_MODE_SUBTRACTED_BEFORE_ABSOLUTE=true' in dp
assert 'STAGE15_6DP_AR025_VALUATION_REDUCTION_ADAPTER=EXACT_RECOMBINATION_ONLY' in dp
assert 'q^2C_{q,\\omega}-X^2' in dp

assert 'STAGE15_6DQ_ARSENAL_VERSION=STAGE14-ARSENAL-20260813-R02' in dq
assert 'STAGE15_6DQ_AR025=EXACT_RECOMBINATION_ONLY' in dq
assert 'STAGE15_6DQ_AR026=DIRECT_NEGATIVE_FIREWALL' in dq
assert 'STAGE15_6DQ_AR027=DIRECT_MEASURE_FIREWALL' in dq
assert 'STAGE15_6DQ_AR033_ADAPTER=false' in dq
assert 'STAGE15_6DQ_AR035=LIVE_QUALITATIVE_ONLY' in dq
assert 'STAGE15_6DQ_AR037_ADAPTER=false' in dq
assert 'STAGE15_6DQ_SAME_MEASURE_KAPPA_LT_1_FROM_ARSENAL=false' in dq

assert 'STAGE15_6DR_CHARACTER_LARGE_SIEVE_NEGATIVE_CERTIFICATE=true' in dr
assert 'STAGE15_6DR_NEGATIVE_SCOPE=CURRENT_CERTIFIED_INPUTS_ONLY' in dr
assert 'STAGE15_6DR_KAPPA_BEST_CERTIFIED=1' in dr
assert 'STAGE15_6DR_KAPPA_LT_1_PROVED=false' in dr
assert 'STAGE15_6DR_DELTA_PROVED=false' in dr
assert 'STAGE15_6DR_SIGMA_PROVED=false' in dr
assert 'STAGE15_6DR_PARKING_ALLOWED=false' in dr
assert 'STAGE15_6DR_NEXT_PRESERVED_ROUTE=PELL_UNIT_ORBIT_SECOND_NORM_CORRELATION' in dr
assert 'CURRENT_SUBSTAGE=Stage15-6dr' in dr
assert 'AUDIT_REQUIRED=true' in dr and 'MERGE_ALLOWED=false' in dr

print('Stage15-6 main-batch dp-dr: PASS')
