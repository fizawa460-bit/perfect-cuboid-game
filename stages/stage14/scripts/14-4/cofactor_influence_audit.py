#!/usr/bin/env python3
from pathlib import Path
ROOT = Path(__file__).resolve().parents[4]
locks = {
    'stages/stage14/14-4do/result.md':'ZERO_MODE_SQRT_OBSTRUCTION_REDUCED_TO_DISJOINT_PRIME_ALLOCATION_BIAS=true',
    'stages/stage14/14-s7-58/result.md':'ZERO_MODE_ORIENTATION_HECKE_EXPANSION_PROVED=true',
    'stages/stage14/14-Work-bfX18/result.md':'GLOBAL_PAIRWISE_COVARIANCE_AS_CONDITIONAL_RESPONSE_PROVED=true',
}
for rel,needle in locks.items():
    assert needle in (ROOT/rel).read_text(), (rel,needle)
res=(ROOT/'stages/stage14/14-4dp/result.md').read_text()
for needle in [
    'STAGE14_4DP=COMPLETE_ORIENTATION_VS_NONMULTIPLICATIVE_PHYSICAL_MASK_INFLUENCE_DECOMPOSITION',
    'COFACTOR_INFLUENCE_TELESCOPING_PROVED=true',
    'SQRT_ZERO_MODE_REQUIRES_EXPONENT_ZERO_ORIENTATION_OR_SINGLE_MASK_INFLUENCE=true',
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    'NEXT_H_NEEDED=false']:
    assert needle in res, needle
print({'stage':'14-4dp','current_exponent':'1/2','next':'Stage14-4dq'})
