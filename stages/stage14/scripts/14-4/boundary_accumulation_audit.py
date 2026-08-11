#!/usr/bin/env python3
from pathlib import Path
ROOT = Path(__file__).resolve().parents[4]
locks = {
    'stages/stage14/14-4do/result.md': 'ZERO_MODE_SQRT_OBSTRUCTION_REDUCED_TO_DISJOINT_PRIME_ALLOCATION_BIAS=true',
    'stages/stage14/14-s7-58/result.md': 'ORIENTATION_MASK_EXACT_HECKE_EXPANSION=true',
    'stages/stage14/14-t98/result.md': 'PHYSICAL_BOUNDARY_TYPES_EXPLICIT=true',
    'stages/stage14/14-Work-bgX19/result.md': 'DISJOINT_PRIME_MULTI_BOUNDARY_ACCUMULATION_PROVED=false',
}
for rel, needle in locks.items():
    text = (ROOT / rel).read_text()
    assert needle in text, (rel, needle)
res = (ROOT / 'stages/stage14/14-4dp/result.md').read_text()
for needle in [
    'STAGE14_4DP=COMPLETE_BOUNDARY_ACCUMULATION_REDUCTION_NO_GLOBAL_DEFICIT',
    'CHARGED_ONCE_TELESCOPING_IDENTITY_AVAILABLE=true',
    'ZERO_MODE_SQRT_OBSTRUCTION_REDUCED_TO_BOUNDARY_ACCUMULATION_NORM=true',
    'DISJOINT_PRIME_BOUNDARY_ACCUMULATION_FIXED_POWER_DEFICIT_PROVED=false',
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    'NEXT_H_NEEDED=false',
]:
    assert needle in res, needle
print({'stage': '14-4dp', 'current_exponent': '1/2', 'next': 'Stage14-4dq'})
