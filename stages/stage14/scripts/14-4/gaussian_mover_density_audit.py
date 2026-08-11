#!/usr/bin/env python3
from pathlib import Path
ROOT = Path(__file__).resolve().parents[4]
locks = {
    'stages/stage14/14-4dr/result.md': 'ZERO_MODE_SQRT_OBSTRUCTION_REDUCED_TO_SINGLE_PRIME_TWO_SQUARE_INFLUENCE=true',
    'stages/stage14/14-s7-61/result.md': 'FRESH_THIN_RESIDUE_SUPPORT_PROVED=false',
    'stages/stage14/14-Work-bhX20/result.md': 'COMMON_STABILIZER_MOVER_DICHOTOMY_PROVED=true',
}
for rel, needle in locks.items():
    assert needle in (ROOT / rel).read_text(), (rel, needle)

# Gaussian split-prime sanity: x^2 == -1 mod p only on sampled p == 1 mod 4.
for p in (5,13,17,29,37,41,53,61,73,89,97):
    assert p % 4 == 1
    assert any((x*x + 1) % p == 0 for x in range(1,p))
for p in (3,7,11,19,23,31,43,47,59,67,71,79):
    assert p % 4 == 3
    assert not any((x*x + 1) % p == 0 for x in range(1,p))

res=(ROOT/'stages/stage14/14-4ds/result.md').read_text()
for needle in [
    'STAGE14_4DS=COMPLETE_GAUSSIAN_SPLIT_PRIME_MOVER_DENSITY_REDUCTION_NO_THIN_RESIDUE_SAVING',
    'FRESH_THIN_RESIDUE_SUPPORT_PROVED=false',
    'SQRT_ZERO_MODE_REQUIRES_EXPONENT_ZERO_GAUSSIAN_MOVER_DENSITY=true',
    'MAINLINE_MOVER_DENSITY_FIXED_POWER_DEFICIT_PROVED=false',
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    'NEXT_H_NEEDED=false',
]:
    assert needle in res, needle
print({'stage':'14-4ds','current_exponent':'1/2','next':'Stage14-4dt'})
