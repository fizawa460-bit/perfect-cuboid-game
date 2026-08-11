#!/usr/bin/env python3
from pathlib import Path
ROOT = Path(__file__).resolve().parents[4]
locks = {
    'stages/stage14/14-4dp/result.md': 'SQRT_ZERO_MODE_REQUIRES_EXPONENT_ZERO_ORIENTATION_OR_SINGLE_MASK_INFLUENCE=true',
    'stages/stage14/14-s7-59/result.md': 'ZERO_MODE_ARITHMETIC_RECEIVER_IS_DISJOINT_ALLOCATION_PLUS_RECIPROCAL=true',
    'stages/stage14/14-4do/result.md': 'FIXED_POWER_COMMON_PRIME_UPLIFT_REMOVED=true',
    'stages/stage14/14-t99/boundary.md': 'SATURATION_LOCALIZES_TO_ONE_BOUNDARY_CLASS=true',
}
for rel, needle in locks.items():
    assert needle in (ROOT / rel).read_text(), (rel, needle)
res = (ROOT / 'stages/stage14/14-4dq/result.md').read_text()
for needle in [
    'STAGE14_4DQ=COMPLETE_SINGLE_MASK_TO_BALANCED_RECIPROCAL_ARITHMETIC_CORE_REDUCTION',
    'MAINLINE_RESIDUAL_ARITHMETIC_MASK_COUNT=2',
    'BALANCED_RECIPROCAL_DOUBLE_CHARGE_FORBIDDEN=true',
    'MAINLINE_ZERO_MODE_ARITHMETIC_RECEIVER_CONTRACTED=true',
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    'NEXT_H_NEEDED=false',
]:
    assert needle in res, needle
print({'stage':'14-4dq','residual_arithmetic_masks':2,'current_exponent':'1/2','next':'Stage14-4dr'})
