#!/usr/bin/env python3
from pathlib import Path
from fractions import Fraction

ROOT = Path(__file__).resolve().parents[4]
locks = {
    'stages/stage14/14-4dt/result.md': 'SQRT_OBSTRUCTION_REDUCED_TO_WEIGHTED_MOVER_CANDIDATE_CONCENTRATION=true',
    'stages/stage14/14-4ds/result.md': 'SQRT_ZERO_MODE_REQUIRES_EXPONENT_ZERO_GAUSSIAN_MOVER_DENSITY=true',
    'stages/stage14/14-Work-bhX20/result.md': 'NEXT_INTERNAL_TARGET=PrimeMoverDensityOrEnergyLemma',
}
for rel, needle in locks.items():
    assert needle in (ROOT / rel).read_text(), (rel, needle)

# Verify plus-state candidate formula from y=rs.
for x, r, s in ((5,3,7),(13,5,9),(17,7,11),(29,9,13)):
    D=Fraction(r+s,2)
    A=Fraction(s-r,2)
    ell=(D*D+A*A)/x
    assert ell == Fraction(r*r+s*s,2*x)

# First/second moment inequality on finite incidence examples.
examples = [
    {5:1,13:1,17:1,29:1},
    {5:3,13:1,17:2},
    {5:4,13:4},
]
for mult in examples:
    I=sum(mult.values())
    image=len(mult)
    energy=sum(v*v for v in mult.values())
    assert I*I <= image*energy

res=(ROOT/'stages/stage14/14-4du/result.md').read_text()
for needle in [
    'STAGE14_4DU=COMPLETE_MOVER_CANDIDATE_IMAGE_ENERGY_DICHOTOMY_NO_FORCED_COLLISION',
    'CANDIDATE_FIRST_SECOND_MOMENT_DICHOTOMY_PROVED=true',
    'SATURATION_FORCES_COLLISION_ENERGY_ALONE=false',
    'DIFFUSE_CANDIDATE_IMAGE_BRANCH_RETAINED=true',
    'COLLISION_ENERGY_BRANCH_RETAINED=true',
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    'NEXT_H_NEEDED=false',
]:
    assert needle in res, needle
print({'stage':'14-4du','current_exponent':'1/2','next':'Stage14-4dv'})
