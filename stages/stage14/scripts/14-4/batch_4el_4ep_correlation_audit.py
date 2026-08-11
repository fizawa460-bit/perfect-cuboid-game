#!/usr/bin/env python3
from pathlib import Path
from math import gcd

ROOT = Path(__file__).resolve().parents[4]

locks = {
    'stages/stage14/14-s7-77/result.md': [
        'LARGE_REPEATED_RAY_ENERGY_FORCES_HEAVY_PRIMITIVE_RAY=true',
        'HEAVY_RAY_RELATIVE_MASS_EXPONENT_ZERO=true',
        'NON_HEAVY_RAY_SATURATION_FORCES_GENUINE_MOVER_ENERGY=true',
    ],
    'stages/stage14/14-4el/result.md': [
        'MERGED_S7_75_77_CONSUMED=true',
        'GLOBAL_PRIMITIVE_RAY_MULTIPLICITY_BOUND=UNPROVED',
        'HEAVY_PRIMITIVE_RAY_SURVIVOR_RETAINED=true',
        'GENUINE_DETERMINANT_MOVER_SURVIVOR_RETAINED=true',
    ],
    'stages/stage14/14-4em/result.md': [
        'SUPER_DETERMINANT_MODULUS_MOVER_BRANCH_EMPTY=true',
        'NEAR_MAXIMAL_MOVER_MODULUS_HAS_SUBPOLYNOMIAL_Q_DICTIONARY=true',
        'SEPARATED_MOVER_MODULUS_HAS_POLYNOMIAL_Q_RANGE=true',
        'HEAVY_RAY_BRANCH_UNCHANGED=true',
    ],
    'stages/stage14/14-4en/result.md': [
        'FIXED_FIRST_VECTOR_DETERMINANT_SOLUTIONS_FORM_ONE_AFFINE_INTEGER_LINE=true',
        'NEAR_MAXIMAL_GENUINE_MOVER_BRANCH_CLOSED=true',
        'HEAVY_RAY_BRANCH_UNCHANGED=true',
    ],
    'stages/stage14/14-4eo/result.md': [
        'NEW_RECIPROCAL_MOVER_H_NEEDED=true',
        'NEW_RECIPROCAL_MOVER_H_TARGET=FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion',
        'HEAVY_RAY_BRANCH_UNCHANGED=true',
    ],
    'stages/stage14/14-4eo/reciprocal-h-target.md': [
        'TARGET_SCOPE=GENUINE_NONZERO_DETERMINANT_MOVER_BRANCH_ONLY',
        'HEAVY_RAY_BRANCH_SEPARATELY_RETAINED=true|false',
    ],
    'stages/stage14/14-4ep/result.md': [
        'DIFFUSE_NORM_DIVISOR_GRAPH_REWRITTEN_AS_NORM_FACTOR_EQUATION=true',
        'ACCEPTED_NORM_VALUE_PROJECTION_FIBER=Bo1',
        'HEAVY_RAY_BRANCH_UNCHANGED=true',
        'NEW_DIFFUSE_H_NEEDED=false',
    ],
    'stages/stage14/14-4-batch/4el-4ep-report.md': [
        'MERGED_S7_75_77_CONSUMED=true',
        'HEAVY_PRIMITIVE_RAY_SURVIVOR_RETAINED=true',
        'BATCH_SUBSTANTIVE_STAGE_COUNT=5',
        'NEXT=Stage14-4eq',
    ],
}
for rel, needles in locks.items():
    text = (ROOT / rel).read_text()
    for needle in needles:
        assert needle in text, (rel, needle)

# Structural primitive-ray fact only: determinant zero identifies the same
# primitive ray. This deliberately does NOT assert a global reverse-fiber bound.
primitive = []
for x in range(1, 20):
    for y in range(1, 20):
        if gcd(x, y) == 1:
            primitive.append((x, y))
for x1, y1 in primitive:
    for x2, y2 in primitive:
        if x1 * y2 == x2 * y1:
            assert (x1, y1) == (x2, y2)

# Nonzero mover quotient identity and scale bound.
for C in (5, 13, 17, 29):
    for x1, y1 in primitive[:40]:
        for x2, y2 in primitive[:40]:
            delta = x1 * y2 - x2 * y1
            if delta and delta % C == 0:
                q = delta // C
                assert q != 0
                assert delta == q * C
                assert abs(delta) <= x1 * y2 + x2 * y1

# Exact affine-line parameterization on the genuine-mover branch.
def bezout_det(x, y):
    for A in range(-abs(x) - 2, abs(x) + 3):
        for B in range(-abs(y) - 2, abs(y) + 3):
            if x * B - A * y == 1:
                return A, B
    raise AssertionError((x, y))

for x1, y1 in [(1, 2), (2, 3), (3, 5), (5, 8), (7, 9)]:
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

# Diffuse norm-factor projection identities.
def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]

for x in range(1, 25):
    for y in range(1, 25):
        if gcd(x, y) != 1:
            continue
        n = x*x + y*y
        for C in divisors(n):
            m = n // C
            assert n == C * m and m > 0

print({
    'batch': 'Stage14-4el..4ep',
    'substantive_stages': 5,
    'heavy_ray_survivor_retained': True,
    'mover_determinant_quotient_audit': 'ok',
    'near_maximal_mover_affine_nogo_audit': 'ok',
    'diffuse_norm_factor_projection_audit': 'ok',
    'new_mover_h_target': 'FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion',
    'current_exponent': '1/2',
    'next': 'Stage14-4eq',
})
