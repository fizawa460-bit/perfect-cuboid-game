#!/usr/bin/env python3
from pathlib import Path
from fractions import Fraction

ROOT = Path(__file__).resolve().parents[4]
locks = {
    'stages/stage14/14-4dx/result.md': 'SQRT_OBSTRUCTION_REDUCED_TO_PROJECTIVE_SLOPE_SCALE_MASK_OCCUPANCY=true',
    'stages/stage14/14-s7-64/result.md': 'FULL_PHYSICAL_ACCEPTANCE_COLLAPSES_TO_ONE_BOOLEAN_SLOPE_PREDICATE=true',
    'stages/stage14/14-Work-bkX23/result.md': 'GLOBAL_ACCEPTANCE_DENSITY_EXPONENT_ZERO_ON_SATURATING_SEQUENCE=true',
}
for rel, needle in locks.items():
    text = (ROOT / rel).read_text()
    assert needle in text, (rel, needle)

# Reduced slope uniquely determines the primitive positive pair.
for a in range(1, 20):
    for b in range(a + 1, 25):
        from math import gcd
        if gcd(a, b) == 1:
            u = Fraction(a, b)
            assert (u.numerator, u.denominator) == (a, b)

# Transport identities.
for a, b, ell in ((1, 2, 5), (2, 3, 5), (3, 5, 13), (4, 7, 17)):
    u = Fraction(a, b)
    lhs = Fraction(a*a + b*b, 2*ell*a*b)
    rhs = (u + 1/u) / (2*ell)
    assert lhs == rhs
    assert Fraction(b-a, b+a) == (1-u)/(1+u)

res = (ROOT / 'stages/stage14/14-4dy/result.md').read_text()
for needle in [
    'STAGE14_4DY=COMPLETE_PROJECTIVE_SLOPE_SCALE_OCCUPANCY_TO_FIXED_BOOLEAN_PRINCIPAL_DENSITY',
    'INDEPENDENT_POLYNOMIAL_SCALE_AFTER_PRIMITIVE_REDUCTION=false',
    'FULL_PHYSICAL_ACCEPTANCE_COLLAPSES_TO_ONE_BOOLEAN_SLOPE_PREDICATE=true',
    'GLOBAL_ACCEPTANCE_PRINCIPAL_DENSITY_RECEIVER=true',
    'GLOBAL_FIXED_POWER_ACCEPTANCE_DENSITY_DEFICIT_PROVED=false',
    'SQRT_OBSTRUCTION_REDUCED_TO_PRIMITIVE_SLOPE_PHYSICAL_ACCEPTANCE_PRINCIPAL_DENSITY=true',
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    'NEXT_H_NEEDED=false',
]:
    assert needle in res, needle
print({'stage': '14-4dy', 'current_exponent': '1/2', 'next': 'Stage14-4dz'})
