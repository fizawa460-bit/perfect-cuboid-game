#!/usr/bin/env python3
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
locks = {
    'stages/stage14/14-4dw/result.md': 'SQRT_OBSTRUCTION_REDUCED_TO_FIXED_PRIME_PRIMITIVE_DIVISOR_PAIR_PHYSICAL_MASK_MASS=true',
    'stages/stage14/14-Work-bjX22/result.md': 'GLOBAL_FIXED_GAUSSIAN_ROOT_ORIENTATION_PROVED=true',
    'stages/stage14/14-s7-63/result.md': 'PROPORTIONAL_COLLISION_CLASS_SIZE=Bo1',
}
for rel, needle in locks.items():
    assert needle in (ROOT / rel).read_text(), (rel, needle)

# Exact slope transport identities for positive integer primitive pairs.
for r, s in ((1,2),(2,3),(3,5),(4,7),(5,8)):
    t=F(r,s)
    # x/y ratio with ell suppressed as a symbolic factor: 2 ell x/y = t + 1/t
    lhs=F(r*r+s*s, r*s)
    rhs=t+1/t
    assert lhs == rhs
    D=F(r+s,2)
    A=F(s-r,2)
    assert A/D == (1-t)/(1+t)

res=(ROOT/'stages/stage14/14-4dx/result.md').read_text()
for needle in [
    'STAGE14_4DX=COMPLETE_PROJECTIVE_SLOPE_MASK_TRANSPORT_NO_FIXED_POWER_DEFICIT',
    'PROJECTIVE_SLOPE_COORDINATE_DEFINED=true',
    'BALANCED_INTERIOR_MASKS_ARE_O1_SLOPE_WINDOWS=true',
    'SQRT_OBSTRUCTION_REDUCED_TO_PROJECTIVE_SLOPE_SCALE_MASK_OCCUPANCY=true',
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    'NEXT_H_NEEDED=false',
]:
    assert needle in res, needle
print({'stage':'14-4dx','current_exponent':'1/2','next':'Stage14-4dy'})
