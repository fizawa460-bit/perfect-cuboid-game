#!/usr/bin/env python3
from fractions import Fraction
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

locks = {
    'stages/stage14/14-s7-64/result.md': [
        'FULL_PHYSICAL_ACCEPTANCE_COLLAPSES_TO_ONE_BOOLEAN_SLOPE_PREDICATE=true',
        'PHYSICAL_ACCEPTANCE_WITNESS_MULTIPLICITY_PER_DIRECTION=Bo1',
        'NEXT=Stage14-s7-65',
    ],
    'stages/stage14/14-4dy/result.md': [
        'GLOBAL_ACCEPTANCE_PRINCIPAL_DENSITY_RECEIVER=true',
        'GLOBAL_FIXED_POWER_ACCEPTANCE_DENSITY_DEFICIT_PROVED=false',
        'NEXT_H_NEEDED=false',
    ],
    'stages/stage14/14-s7-46/result.md': [
        'MIXED_ROOT_TO_SECOND_RECIPROCAL_FIBER_MULTIPLICITY=Bo1',
        'DUAL_BALANCED_XI_COFACTOR_SPLIT_REQUIRED=true',
    ],
    'stages/stage14/14-s7-47/result.md': [
        'BALANCED_SQUAREFREE_SPLIT_ALONE_FIXED_POWER_SAVING=false',
        'SQRT_SATURATION_FOUR_NORM_BLOCKS_PAIRWISE_SEPARATED=true',
    ],
    'stages/stage14/14-s7-59/result.md': [
        'ZERO_MODE_ARITHMETIC_RECEIVER_IS_DISJOINT_ALLOCATION_PLUS_RECIPROCAL=true',
    ],
    'stages/stage14/14-s7-60/result.md': [
        'BALANCED_ALLOCATION_AND_RECIPROCAL_COMPLETION_SHARE_ONE_COORDINATE_PACKET=true',
        'RECIPROCAL_COMPLETION_INDEPENDENT_FIXED_POWER_SUPPORT=false',
    ],
    'stages/stage14/14-Work-bkX23/result.md': [
        'COMMON_FIXED_BOOLEAN_PRINCIPAL_DENSITY_TEMPLATE_PROVED=true',
        'GLOBAL_FIXED_POWER_ACCEPTANCE_DENSITY_DEFICIT_PROVED=false',
    ],
}
for rel, needles in locks.items():
    text = (ROOT / rel).read_text()
    for needle in needles:
        assert needle in text, (rel, needle)


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def roots_minus_one(p):
    return [x for x in range(1, p) if (x * x + 1) % p == 0]


identity_checks = 0
divisor_checks = 0
for a in range(1, 24):
    for b in range(a + 1, 31):
        if gcd(a, b) != 1:
            continue
        for g in (1, 2, 3, 6):
            D = Fraction(g * (a + b), 2)
            A = Fraction(g * (b - a), 2)
            assert D * D + A * A == Fraction(g * g * (a * a + b * b), 2)
            assert D * D - A * A == g * g * a * b
            identity_checks += 1

        assert gcd(a * a + b * b, a * b) == 1

        for d in divisors(a * b):
            da = gcd(d, a)
            db = gcd(d, b)
            assert d == da * db
            assert a % da == 0 and b % db == 0
            assert gcd(da, db) == 1
            divisor_checks += 1

assert identity_checks > 100
assert divisor_checks > 100

root_line_checks = 0
for ell in (5, 13, 17, 29):
    roots = roots_minus_one(ell)
    assert len(roots) == 2
    rho = roots[0]
    for b in range(1, 80):
        if b % ell == 0:
            continue
        for a in range(1, b):
            if gcd(a, b) != 1 or (a - rho * b) % ell:
                continue
            nplus = a * a + b * b
            assert nplus % ell == 0
            assert gcd(nplus // ell, a * b) == 1
            root_line_checks += 1

assert root_line_checks > 10

res = (ROOT / 'stages/stage14/14-s7-65/result.md').read_text()
for needle in [
    'STAGE14_S7_65=COMPLETE_PRIMITIVE_SLOPE_PHYSICAL_WITNESS_DECOMPOSITION_AND_COPRIME_BINARY_FORM_CONTRACTION',
    'MERGED_4DY_IMPORTED=true',
    'PRIMITIVE_BINARY_FORM_CORE_GCD_ONE=true',
    'CROSS_SIGN_PRIME_SEPARATION_AUTOMATIC_UP_TO_Bo1=true',
    'PHYSICAL_ACCEPTANCE_WITNESS_EXPANSION_EXPLICIT=true',
    'BALANCED_DIVISOR_WINDOW_ALONE_FIXED_POWER_SAVING=false',
    'CROSS_SIGN_ALLOCATION_COMPONENT_DISCHARGED=true',
    'MINUS_BALANCED_ALLOCATION_REDUCES_TO_DIVISORS_OF_COPRIME_A_AND_B=true',
    'PLUS_BALANCED_ALLOCATION_LIVES_ON_SUM_OF_TWO_SQUARES_NORM=true',
    'RECIPROCAL_COMPLETION_IS_BOOLEAN_ON_BALANCED_ALLOCATION_WITNESS=true',
    'JOINT_BALANCED_RECIPROCAL_SELECTOR_REMAINS=true',
    'FIXED_POWER_ACCEPTANCE_DENSITY_DEFICIT_PROVED=false',
    'S7_65_NEW_AUXILIARY_H_NEEDED=false',
    'NEXT=Stage14-s7-66',
]:
    assert needle in res, needle

print({
    'stage': '14-s7-65',
    'primitive_identity_checks': identity_checks,
    'minus_divisor_decomposition_checks': divisor_checks,
    'gaussian_root_line_coprimality_checks': root_line_checks,
    'current_exponent': '1/2',
    'next': 'Stage14-s7-66',
})
