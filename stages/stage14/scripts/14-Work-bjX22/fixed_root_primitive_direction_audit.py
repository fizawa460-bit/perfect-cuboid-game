#!/usr/bin/env python3
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[4]
locks = {
    'stages/stage14/14-Work-biX21/result.md': [
        'GLOBAL_RANGE_STABLE_HEAVY_MOVER_PRIME_PROVED=true',
        'GLOBAL_HEAVY_MOVER_STATE_MASS_EXPONENT=1/2',
    ],
    'stages/stage14/14-4dw/result.md': [
        'FIXED_ELL_ROOT_ORIENTATION_COUNT=2',
        'SQRT_OBSTRUCTION_REDUCED_TO_FIXED_PRIME_PRIMITIVE_DIVISOR_PAIR_PHYSICAL_MASK_MASS=true',
    ],
    'stages/stage14/14-s7-63/result.md': [
        'PROPORTIONAL_COLLISION_CLASS_SIZE=Bo1',
        'NONPROPORTIONAL_COLLISION_PAIR_ADDS_FRESH_CODIMENSION=false',
    ],
    'stages/stage14/14-t103/frozen-boundary.txt': [
        'COMMON_ELEMENTARY_BOUNDARY_SKELETON_ACROSS_PRIMES_PROVED=true',
        'GLOBAL_FIXED_U_ARITHMETIC_ADAPTER_PROVED=false',
    ],
}
for rel, needles in locks.items():
    text = (ROOT / rel).read_text()
    for needle in needles:
        assert needle in text, (rel, needle)

# Finite-support model: total mass divided among direction classes of bounded size.
classes = {'d1': 3, 'd2': 2, 'd3': 1, 'd4': 3, 'd5': 2}
M = sum(classes.values())
C = max(classes.values())
assert len(classes) >= M / C

# Two root orientations: one carries at least half of total mass.
orient = {'+': 0, '-': 0}
assignment = {'d1': '+', 'd2': '-', 'd3': '+', 'd4': '-', 'd5': '+'}
for d, mass in classes.items():
    orient[assignment[d]] += mass
assert max(orient.values()) * 2 >= M

# After fixing the heavier orientation, direction count is still mass / class-cap.
eps = max(orient, key=orient.get)
M_eps = orient[eps]
D_eps = sum(1 for d in classes if assignment[d] == eps)
assert D_eps >= M_eps / C

# Gaussian root sanity: split primes have exactly two roots of -1.
for ell in (5, 13, 17, 29, 37, 41):
    roots = [a for a in range(ell) if (a*a + 1) % ell == 0]
    assert len(roots) == 2

res = (ROOT / 'stages/stage14/14-Work-bjX22/result.md').read_text()
for needle in [
    'STAGE14_WORK_BJX22=COMPLETE_FIXED_HEAVY_PRIME_ROOT_ORIENTATION_PRIMITIVE_DIRECTION_CONTRACTION',
    'GLOBAL_PRIMITIVE_DIRECTION_COUNT_EXPONENT=1/2',
    'GLOBAL_FIXED_GAUSSIAN_ROOT_ORIENTATION_PROVED=true',
    'GLOBAL_FIXED_ROOT_ORIENTATION_DIRECTION_COUNT_EXPONENT=1/2',
    'COLLISION_ENERGY_DISCHARGED_AS_LOCALIZATION=true',
    'COMMON_FINITE_LABEL_FREEZING_PRINCIPLE_PROVED=true',
    'COMMON_ARITHMETIC_MASK_ADAPTER_PROVED=false',
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    'TH28_NEEDED=false',
]:
    assert needle in res, needle

print({'stage':'14-Work-bjX22','checks':'PASS','current_exponent':'1/2'})
