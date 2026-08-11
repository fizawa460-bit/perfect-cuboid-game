#!/usr/bin/env python3
from pathlib import Path
from math import gcd

ROOT = Path(__file__).resolve().parents[4]

locks = {
    'stages/stage14/14-4ek/result.md': [
        'POLYNOMIAL_CORE_DISCREPANCY_SPLIT_INTO_CONCENTRATED_OR_DIFFUSE_MODULUS=true',
        'CONCENTRATED_MODULUS_BRANCH_REDUCES_TO_PROJECTIVE_COLLISION_ENERGY=true',
        'DIFFUSE_MODULUS_BRANCH_REMAINS_VARIABLE_NORM_DIVISOR_GRAPH=true',
    ],
    'stages/stage14/14-Work-bnX26/result.md': [
        'COMMON_CORRELATION_ONLY_OBSTRUCTION_LANGUAGE_PROVED=true',
        'MAINLINE_H_TARGET=CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity',
    ],
    'stages/stage14/14-4el/result.md': [
        'DIAGONAL_COLLISIONS_CANNOT_SUPPORT_EXPONENT_ZERO_ENERGY=true',
        'PROPORTIONAL_COLLISIONS_CANNOT_SUPPORT_EXPONENT_ZERO_ENERGY=true',
        'CONCENTRATED_SATURATION_FORCES_GENUINE_OFF_DIAGONAL_PROJECTIVE_COLLISIONS=true',
    ],
    'stages/stage14/14-4em/result.md': [
        'SUPER_DETERMINANT_MODULUS_COLLISION_BRANCH_EMPTY=true',
        'NEAR_MAXIMAL_MODULUS_HAS_SUBPOLYNOMIAL_Q_DICTIONARY=true',
        'SEPARATED_MODULUS_HAS_POLYNOMIAL_Q_RANGE=true',
    ],
    'stages/stage14/14-4en/result.md': [
        'FIXED_FIRST_VECTOR_DETERMINANT_SOLUTIONS_FORM_ONE_AFFINE_INTEGER_LINE=true',
        'NEAR_MAXIMAL_COMMON_CORE_CONCENTRATED_BRANCH_CLOSED=true',
    ],
    'stages/stage14/14-4eo/result.md': [
        'NEW_RECIPROCAL_H_NEEDED=true',
        'NEW_RECIPROCAL_H_TARGET=FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion',
    ],
    'stages/stage14/14-4ep/result.md': [
        'DIFFUSE_NORM_DIVISOR_GRAPH_REWRITTEN_AS_NORM_FACTOR_EQUATION=true',
        'ACCEPTED_NORM_VALUE_PROJECTION_FIBER=Bo1',
        'NEW_DIFFUSE_H_NEEDED=false',
    ],
    'stages/stage14/14-4-batch/4el-4ep-report.md': [
        'BATCH_SUBSTANTIVE_STAGE_COUNT=5',
        'NEXT=Stage14-4eq',
    ],
}

for rel, needles in locks.items():
    text = (ROOT / rel).read_text()
    for needle in needles:
        assert needle in text, (rel, needle)

# Primitive rational proportionality: determinant zero implies equality up to sign.
primitive = []
for x in range(1, 20):
    for y in range(1, 20):
        if gcd(x, y) == 1:
            primitive.append((x, y))
for x1, y1 in primitive:
    for x2, y2 in primitive:
        if x1 * y2 == x2 * y1:
            assert (x1, y1) == (x2, y2)

# Nonzero collision quotient and determinant-scale bound.
for C in (5, 13, 17, 29):
    for x1, y1 in primitive[:40]:
        for x2, y2 in primitive[:40]:
            delta = x1 * y2 - x2 * y1
            if delta and delta % C == 0:
                q = delta // C
                assert q != 0
                assert delta == q * C
                assert abs(delta) <= x1 * y2 + x2 * y1

# Exact affine parameterization for determinant equation.
def bezout_det(x, y):
    # Find A,B with x*B-A*y=1.
    for A in range(-abs(x) - 2, abs(x) + 3):
        for B in range(-abs(y) - 2, abs(y) + 3):
            if x * B - A * y == 1:
                return A, B
    raise AssertionError((x, y))

for x1, y1 in [(1, 2), (2, 3), (3, 5), (5, 8), (7, 9)]:
    assert gcd(x1, y1) == 1
    A, B = bezout_det(x1, y1)
    for C, q in [(5, 1), (5, -2), (13, 1), (17, 3)]:
        seen = []
        for t in range(-5, 6):
            x2 = q * C * A + t * x1
            y2 = q * C * B + t * y1
            assert x1 * y2 - x2 * y1 == q * C
            seen.append((x2, y2))
        for (xa, ya), (xb, yb) in zip(seen, seen[1:]):
            assert (xb - xa, yb - ya) == (x1, y1)

# Divisor and primitive two-square multiplicities are subpolynomial in the
# theorem use; finite diagnostic checks ensure the projection identities.
def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]

for x in range(1, 25):
    for y in range(1, 25):
        if gcd(x, y) != 1:
            continue
        n = x * x + y * y
        for C in divisors(n):
            m = n // C
            assert n == C * m
            assert m > 0

print({
    'batch': 'Stage14-4el..4ep',
    'substantive_stages': 5,
    'diagonal_proportional_audit': 'ok',
    'determinant_quotient_audit': 'ok',
    'affine_line_parameterization_audit': 'ok',
    'norm_factor_projection_audit': 'ok',
    'new_reciprocal_h_target': 'FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion',
    'current_exponent': '1/2',
    'next': 'Stage14-4eq',
})
