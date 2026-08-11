#!/usr/bin/env python3
from pathlib import Path
ROOT = Path(__file__).resolve().parents[4]
locks = {
 'stages/stage14/14-4dn/result.md':'ZERO_MODE_POSITIVE_OBSTRUCTION_EQUALS_POSITIVE_CONDITIONAL_UPLIFT=true',
 'stages/stage14/14-s7-57/result.md':'PAIRWISE_NEAR_DETERMINISM_PROMOTION_LEGAL=false',
 'stages/stage14/14-Work-bfX18/result.md':'GLOBAL_PAIRWISE_COVARIANCE_AS_CONDITIONAL_RESPONSE_PROVED=true',
 'stages/stage14/14-4df/result.md':'SIX_ATOMIC_NORM_BLOCKS_PAIRWISE_SEPARATED=true',
}
for rel,needle in locks.items():
    assert needle in (ROOT/rel).read_text(), (rel,needle)
res=(ROOT/'stages/stage14/14-4do/result.md').read_text()
for needle in [
 'STAGE14_4DO=COMPLETE_ZERO_MODE_UPLIFT_DISJOINT_PRIME_ALLOCATION_REDUCTION',
 'FIXED_POWER_COMMON_PRIME_UPLIFT_REMOVED=true',
 'ZERO_MODE_SQRT_OBSTRUCTION_REDUCED_TO_DISJOINT_PRIME_ALLOCATION_BIAS=true',
 'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
 'NEXT_H_NEEDED=false']:
    assert needle in res, needle
print({'stage':'14-4do','current_exponent':'1/2','next':'Stage14-4dp'})
