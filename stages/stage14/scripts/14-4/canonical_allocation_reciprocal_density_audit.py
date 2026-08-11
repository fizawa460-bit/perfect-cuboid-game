#!/usr/bin/env python3
from pathlib import Path
ROOT = Path(__file__).resolve().parents[4]
locks = {
    'stages/stage14/14-4dz/result.md': [
        'SQRT_OBSTRUCTION_REDUCED_TO_NESTED_PRIMITIVE_SLOPE_ACCEPTANCE_DENSITIES=true',
    ],
    'stages/stage14/14-s7-68/result.md': [
        'CANONICAL_ALLOCATION_RECIPROCAL_DENSITY_CHAIN_EXACT=true',
        'SATURATION_FORCES_CANONICAL_ALLOCATION_DENSITY_EXPONENT_ZERO=true',
        'SATURATION_FORCES_RECIPROCAL_CONDITIONAL_DENSITY_EXPONENT_ZERO=true',
    ],
    'stages/stage14/14-Work-blX24/result.md': [
        'DIRECT_GLOBAL_TO_FIXED_Q_FIBER_DENSITY_ADAPTER_NOGO=true',
        'GLOBAL_PRINCIPAL_POLYNOMIAL_SCALE_REMAINS_PRIMITIVE_SLOPE_BACKGROUND=true',
    ],
}
for rel, needles in locks.items():
    text = (ROOT / rel).read_text()
    for needle in needles:
        assert needle in text, (rel, needle)
res = (ROOT / 'stages/stage14/14-4ea/result.md').read_text()
for needle in [
    'STAGE14_4EA=COMPLETE_THREE_LEVEL_NESTED_DENSITY_TO_CANONICAL_TWO_FACTOR_RECEIVER',
    'THREE_LEVEL_CHAIN_SUPERSEDED_BY_CANONICAL_TWO_FACTOR_RECEIVER=true',
    'SQRT_OBSTRUCTION_REDUCED_TO_CANONICAL_ALLOCATION_OR_RECIPROCAL_CONDITIONAL_DENSITY=true',
    'CANONICAL_ALLOCATION_FIXED_POWER_DEFICIT_PROVED=false',
    'RECIPROCAL_CONDITIONAL_FIXED_POWER_DEFICIT_PROVED=false',
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    'NEXT_H_NEEDED=false',
]:
    assert needle in res, needle
print({'stage':'14-4ea','current_exponent':'1/2','next':'Stage14-4eb'})
