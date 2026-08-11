#!/usr/bin/env python3
from pathlib import Path
ROOT = Path(__file__).resolve().parents[4]
locks = {
    'stages/stage14/14-4dq/result.md': 'STAGE14_4DQ=COMPLETE_RESIDUAL_ARITHMETIC_INFLUENCE_CONTRACTION',
    'stages/stage14/14-s7-60/result.md': 'SQRT_ARITHMETIC_UPLIFT_REQUIRES_EXPONENT_ZERO_SINGLE_PRIME_INFLUENCE=true',
}
for rel, needle in locks.items():
    assert needle in (ROOT / rel).read_text(), (rel, needle)
res = (ROOT / 'stages/stage14/14-4dr/result.md').read_text()
for needle in [
    'STAGE14_4DR=COMPLETE_SINGLE_PRIME_TWO_SQUARE_INFLUENCE_REDUCTION',
    'TWO_SQUARE_ADMISSIBILITY_PREDICATE_EXPLICIT=true',
    'ZERO_MODE_SQRT_OBSTRUCTION_REDUCED_TO_SINGLE_PRIME_TWO_SQUARE_INFLUENCE=true',
    'FRESH_SINGLE_PRIME_FIXED_POWER_SAVING_PROVED=false',
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    'NEXT_H_NEEDED=false',
]:
    assert needle in res, needle
print({'stage': '14-4dr', 'current_exponent': '1/2', 'next': 'Stage14-4ds'})
