#!/usr/bin/env python3
from pathlib import Path

ROOT=Path(__file__).resolve().parents[4]
locks={
    'stages/stage14/14-4du/result.md':'SQRT_OBSTRUCTION_REDUCED_TO_CANDIDATE_IMAGE_OR_COLLISION_ENERGY=true',
    'stages/stage14/14-s7-62/result.md':'DIFFUSE_IMAGE_BRANCH_REMOVED_ON_RANGE_STABLE_ARITHMETIC_RECEIVER=true',
    'stages/stage14/14-Work-biX21/result.md':'GLOBAL_COLLISION_PRIME_CAN_BE_FROZEN_ON_SATURATING_ARITHMETIC_SUBFAMILY=true',
}
for rel,needle in locks.items():
    assert needle in (ROOT/rel).read_text(), (rel,needle)

# Fixed-prime plus-state collision is algebraically tautological.
for ell in (5,13,17,29):
    for x1 in range(1,20):
        for x2 in range(1,20):
            n1=2*ell*x1
            n2=2*ell*x2
            assert x2*n1 == x1*n2

res=(ROOT/'stages/stage14/14-4dv/result.md').read_text()
for needle in [
    'STAGE14_4DV=COMPLETE_FIXED_PRIME_COLLISION_TAUTOLOGY_REDUCTION',
    'FIXED_PRIME_PLUS_PLUS_COLLISION_EQUATION_TAUTOLOGICAL=true',
    'FRESH_PAIRWISE_DETERMINANT_FROM_COLLISION=false',
    'COLLISION_ENERGY_USED_ONLY_FOR_HEAVY_FIBER_EXTRACTION=true',
    'SQRT_OBSTRUCTION_REDUCED_TO_FIXED_PRIME_DIVISOR_GRAPH_STATE_MASS=true',
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    'NEXT_H_NEEDED=false',
]:
    assert needle in res, needle
print({'stage':'14-4dv','current_exponent':'1/2','next':'Stage14-4dw'})
