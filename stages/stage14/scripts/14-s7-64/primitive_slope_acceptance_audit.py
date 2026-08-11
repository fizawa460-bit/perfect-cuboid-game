#!/usr/bin/env python3
from pathlib import Path
from math import gcd, log
from fractions import Fraction

ROOT = Path(__file__).resolve().parents[4]

locks = {
    'stages/stage14/14-s7-63/result.md': [
        'PROPORTIONAL_COLLISION_CLASS_SIZE=Bo1',
        'COMPLEMENTARY_FACTOR_GCD=Bo1',
    ],
    'stages/stage14/14-Work-bjX22/result.md': [
        'GLOBAL_FIXED_GAUSSIAN_ROOT_ORIENTATION_PROVED=true',
        'GLOBAL_FIXED_ROOT_ORIENTATION_DIRECTION_COUNT_EXPONENT=1/2',
        'COMMON_FINITE_LABEL_FREEZING_PRINCIPLE_PROVED=true',
    ],
    'stages/stage14/14-4dx/result.md': [
        'PHYSICAL_MASK_TRANSPORT_TO_SLOPE_SCALE_COMPLETED=true',
        'BALANCED_INTERIOR_MASKS_ARE_O1_SLOPE_WINDOWS=true',
        'SQRT_OBSTRUCTION_REDUCED_TO_PROJECTIVE_SLOPE_SCALE_MASK_OCCUPANCY=true',
    ],
    'stages/stage14/14-s7-46/result.md': [
        'MIXED_ROOT_TO_SECOND_RECIPROCAL_FIBER_MULTIPLICITY=Bo1',
        'MIXED_FOURTH_ROOT_TUPLE_PHYSICAL_PACKET_FINITE_FIBER_EQUIVALENCE=true',
    ],
    'stages/stage14/14-s7-47/result.md': [
        'BALANCED_XI_CELL_SPLIT_MULTIPLICITY_GIVEN_COFACTORS=Bo1',
        'BALANCED_SQUAREFREE_SPLIT_ALONE_FIXED_POWER_SAVING=false',
    ],
}
for rel, needles in locks.items():
    text = (ROOT / rel).read_text()
    for needle in needles:
        assert needle in text, (rel, needle)


def roots_minus_one(p):
    return [x for x in range(1, p) if (x*x + 1) % p == 0]

# Exact primitive-slope transport identities on Gaussian root-line examples.
checked = 0
for ell in (5, 13, 17, 29, 37, 41):
    roots = roots_minus_one(ell)
    assert len(roots) == 2
    rho = roots[0]
    for b in range(3, 100, 2):
        for a in range(1, b, 2):
            if gcd(a, b) != 1 or (a-rho*b) % ell:
                continue
            assert (a*a+b*b) % ell == 0
            D = Fraction(a+b, 2)
            A = Fraction(b-a, 2)
            x = Fraction(a*a+b*b, 2*ell)
            y = a*b
            u = Fraction(a, b)
            assert x/Fraction(y, 1) == (u + 1/u)/(2*ell)
            assert A/D == (1-u)/(1+u)
            checked += 1
            break
        if checked:
            break
assert checked >= 1

# Reduced slope uniquely recovers its primitive positive pair.
for a, b in ((1, 3), (3, 5), (5, 11), (7, 19), (11, 23)):
    assert gcd(a, b) == 1
    u = Fraction(a, b)
    assert (u.numerator, u.denominator) == (a, b)

# One active cross-sign atomic mover chart has at most 3x3 core labels.
plus_blocks = ('C_*', 'S', 'T')
minus_blocks = ('u_*', 'R', 'J')
charts = {(p, m) for p in plus_blocks for m in minus_blocks}
assert len(charts) == 9

# Ambient compatibility: fixed positive-width slope interval + one fixed
# Gaussian root line modulo a fixed small prime retains quadratic pair count
# up to logarithmic/subpolynomial losses.
ell = 5
rho = roots_minus_one(ell)[0]
H = 800
lo, hi = Fraction(1, 4), Fraction(3, 4)
count = 0
for b in range(H//2, H+1):
    amin = (lo.numerator*b)//lo.denominator + 1
    amax = (hi.numerator*b + hi.denominator - 1)//hi.denominator
    for a in range(amin, amax):
        if a >= b:
            continue
        if (a-rho*b) % ell == 0 and gcd(a, b) == 1:
            count += 1
assert count > H*H/(100*ell*log(H))

res = (ROOT / 'stages/stage14/14-s7-64/result.md').read_text()
for needle in [
    'STAGE14_S7_64=COMPLETE_PRIMITIVE_RATIONAL_SLOPE_CONTRACTION_AND_PHYSICAL_ACCEPTANCE_PREDICATE',
    'MERGED_4DX_IMPORTED=true',
    'INDEPENDENT_POLYNOMIAL_SCALE_AFTER_PRIMITIVE_REDUCTION=false',
    'FIXED_WIDTH_SLOPE_ROOT_LINE_AMBIENT_EXPONENT=1/2',
    'ATOMIC_MOVER_CORE_CHART_LABEL_COUNT_LE_9=true',
    'ONE_ATOMIC_MOVER_CHART_CAN_BE_FROZEN=true',
    'FULL_PHYSICAL_ACCEPTANCE_COLLAPSES_TO_ONE_BOOLEAN_SLOPE_PREDICATE=true',
    'TRANSPORTED_PHYSICAL_ACCEPTANCE_FIXED_POWER_DEFICIT_PROVED=false',
    'MERGED_Q12_COLLISION_LITERATURE_CROSS_PROMOTED_TO_S7_64=false',
    'MERGED_T104_FIXED_U_BOUNDARY_CROSS_PROMOTED_TO_S7_64=false',
    'S7_64_NEW_AUXILIARY_H_NEEDED=false',
    'NEXT=Stage14-s7-65',
]:
    assert needle in res, needle

print({
    'stage': '14-s7-64',
    'transport_examples_checked': checked,
    'atomic_core_chart_labels': len(charts),
    'ambient_root_line_primitive_pairs': count,
    'current_exponent': '1/2',
    'next': 'Stage14-s7-65',
})
