#!/usr/bin/env python3
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
locks = {
    'stages/stage14/14-4dv/result.md': 'SQRT_OBSTRUCTION_REDUCED_TO_FIXED_PRIME_DIVISOR_GRAPH_STATE_MASS=true',
    'stages/stage14/14-s7-62/result.md': 'RANGE_STABLE_ARITHMETIC_MOVER_PRIME_SCALE=Bo0',
    'stages/stage14/14-Work-biX21/result.md': 'GLOBAL_RANGE_STABLE_HEAVY_MOVER_PRIME_PROVED=true',
}
for rel, needle in locks.items():
    assert needle in (ROOT / rel).read_text(), (rel, needle)

# Reconstruction and gcd sanity for r=D-A, s=D+A.
for D in range(3, 40):
    for A in range(1, D):
        r, s = D-A, D+A
        assert r*s == D*D - A*A
        assert r*r + s*s == 2*(D*D + A*A)
        assert gcd(r, s) % gcd(D, A) == 0
        assert gcd(r, s) <= 2*gcd(D, A)

# Sample Gaussian split primes: exactly two roots of -1 mod ell.
for ell in (5, 13, 17, 29, 37, 41, 53, 61):
    roots = [a for a in range(ell) if (a*a + 1) % ell == 0]
    assert len(roots) == 2

res = (ROOT / 'stages/stage14/14-4dw/result.md').read_text()
for needle in [
    'STAGE14_4DW=COMPLETE_FIXED_PRIME_STATE_TO_PRIMITIVE_DIVISOR_PAIR_MASS_REDUCTION',
    'FIXED_ELL_STATE_TO_DIVISOR_PAIR_FIBER=O1',
    'FIXED_ELL_GAUSSIAN_ROOT_CONGRUENCE_EXPLICIT=true',
    'FIXED_ELL_ROOT_CONGRUENCE_FIXED_POWER_SAVING=false',
    'SQRT_OBSTRUCTION_REDUCED_TO_FIXED_PRIME_PRIMITIVE_DIVISOR_PAIR_PHYSICAL_MASK_MASS=true',
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    'NEXT_H_NEEDED=false',
]:
    assert needle in res, needle

print({'stage': '14-4dw', 'current_exponent': '1/2', 'next': 'Stage14-4dx'})
