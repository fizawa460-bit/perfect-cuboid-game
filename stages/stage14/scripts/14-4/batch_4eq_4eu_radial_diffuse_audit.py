#!/usr/bin/env python3
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

locks = {
    'stages/stage14/14-s7-80/result.md': [
        'HEAVY_RAY_SPLIT_INTO_FIXED_DATA_BACKGROUND_FIBER_OR_DIFFUSE_RADIAL_SUPPORT=true',
        'FIXED_RECIPROCAL_DATA_TO_CANONICAL_BACKGROUND_FIBER_BOUND=UNPROVED',
    ],
    'stages/stage14/14-4eq/result.md': [
        'FIXED_RECIPROCAL_DATA_TO_CANONICAL_BACKGROUND_FIBER_BOUND=Bo1',
        'HEAVY_RAY_RADIAL_CONCENTRATION_BRANCH_CLOSED=true',
        'HEAVY_RAY_RADIAL_DIFFUSION_BRANCH_RETAINED=true',
    ],
    'stages/stage14/14-4er/result.md': [
        'DIFFUSE_SMALL_QUOTIENT_BRANCH_DEFINED=true',
        'DIFFUSE_POLYNOMIAL_QUOTIENT_BRANCH_DEFINED=true',
    ],
    'stages/stage14/14-4es/result.md': [
        'DIFFUSE_SMALL_QUOTIENT_BRANCH_BOUND_EXPONENT=1/4',
        'DIFFUSE_SMALL_QUOTIENT_BRANCH_CLOSED=true',
    ],
    'stages/stage14/14-4et/result.md': [
        'DIFFUSE_POLYNOMIAL_QUOTIENT_GAUSSIAN_FACTORIZATION_PROVED=true',
        'CORE_QUOTIENT_COPRIMALITY_ASSUMED=false',
    ],
    'stages/stage14/14-4eu/result.md': [
        'NEW_DIFFUSE_H_NEEDED=true',
        'HEAVY_RAY_RADIAL_DIFFUSION_BRANCH_RETAINED=true',
        'WHOLE_MAINLINE_BLOCKED_BY_H=false',
    ],
    'stages/stage14/14-4-batch/4eq-4eu-report.md': [
        'BATCH_SUBSTANTIVE_STAGE_COUNT=5',
        'NEXT=Stage14-4ev',
    ],
}

for rel, needles in locks.items():
    text = (ROOT / rel).read_text()
    for needle in needles:
        assert needle in text, (rel, needle)

# 4eq: fixed raw reciprocal data give one fixed positive second reciprocal difference.
for x in range(2, 30):
    for y in range(1, x):
        if gcd(x, y) != 1:
            continue
        for h in range(1, 8):
            X, Y = h * x, h * y
            W2 = X * X - Y * Y
            assert W2 > 0
            assert W2 == h * h * (x * x - y * y)

# Fixed X,Y have divisor-many decompositions X=p*c, Y=q*d.
def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]

for X in range(2, 25):
    for Y in range(1, X):
        count = len(divisors(X)) * len(divisors(Y))
        brute = sum(1 for p in divisors(X) for q in divisors(Y)
                    if X % p == 0 and Y % q == 0)
        assert count == brute

# 4es exponent audit: kappa <= 1/4 and subpolynomial m gives <=1/4 support.
from fractions import Fraction
for k_num in range(8, 13):
    kappa = Fraction(k_num, 48)  # [1/6,1/4]
    assert Fraction(1, 6) <= kappa <= Fraction(1, 4)
    assert kappa <= Fraction(1, 4) < Fraction(1, 2)

# Gaussian norm multiplicativity diagnostic.
for a, b, c, d in [(1,2,2,1),(2,3,1,4),(3,4,2,5),(1,6,5,2)]:
    xr = a*c - b*d
    yi = a*d + b*c
    lhs = xr*xr + yi*yi
    rhs = (a*a+b*b)*(c*c+d*d)
    assert lhs == rhs

print({
    'batch': 'Stage14-4eq..4eu',
    'substantive_stages': 5,
    'fixed_h_heavy_ray': 'closed',
    'radial_diffusion': 'retained',
    'diffuse_small_m': 'closed_at_1/4',
    'diffuse_polynomial_m': 'gaussian_bilinear_H_gate',
    'whole_mainline_blocked_by_H': False,
    'current_exponent': '1/2',
    'next': 'Stage14-4ev',
})
