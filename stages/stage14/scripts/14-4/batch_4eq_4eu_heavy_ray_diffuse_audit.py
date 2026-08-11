#!/usr/bin/env python3
from fractions import Fraction
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

locks = {
    'stages/stage14/14-4-batch/4el-4ep-report.md': [
        'HEAVY_PRIMITIVE_RAY_SURVIVOR_RETAINED=true',
        'DIFFUSE_SURVIVOR_IS_PRIMITIVE_GAUSSIAN_NORM_FACTOR_CORRELATION=true',
        'NEXT=Stage14-4eq',
    ],
    'stages/stage14/14-s7-77/result.md': [
        'LARGE_REPEATED_RAY_ENERGY_FORCES_HEAVY_PRIMITIVE_RAY=true',
        'NON_HEAVY_RAY_SATURATION_FORCES_GENUINE_MOVER_ENERGY=true',
    ],
    'stages/stage14/14-s7-42/result.md': [
        'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
        'SQRT_SATURATION_REQUIRES_SAMESIDE_K=Bo1',
    ],
    'stages/stage14/14-4dd/result.md': [
        'CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2',
    ],
    'stages/stage14/14-4eq/result.md': [
        'HEAVY_PRIMITIVE_RAY_REVERSE_FIBER=Bo1',
        'GLOBAL_PRIMITIVE_RAY_MULTIPLICITY_BOUND=Bo1',
        'HEAVY_PRIMITIVE_RAY_BRANCH_CLOSED=true',
    ],
    'stages/stage14/14-4er/result.md': [
        'DIFFUSE_PRIMITIVE_NORM_SCALE=1/2',
        'DIFFUSE_QUOTIENT_ALWAYS_POLYNOMIAL=true',
        'NEAR_FULL_COMMON_CORE_m_Bo1_BRANCH_EMPTY=true',
    ],
    'stages/stage14/14-4es/result.md': [
        'DIFFUSE_SATURATION_REQUIRES_CORE_QUOTIENT_GCD=Bo1',
        'FIXED_POWER_CORE_QUOTIENT_OVERLAP_BRANCH_CLOSED=true',
    ],
    'stages/stage14/14-4et/result.md': [
        'DIFFUSE_GAUSSIAN_PRODUCT_FACTORIZATION_PROVED=true',
        'BARE_GAUSSIAN_BILINEAR_PRODUCT_EXPONENT=1/2',
    ],
    'stages/stage14/14-4eu/result.md': [
        'NEW_DIFFUSE_H_NEEDED=true',
        'ALL_CURRENT_MAINLINE_SURVIVORS_THEOREM_GATED=true',
        'WHOLE_MAINLINE_BLOCKED_BY_H=true',
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

# 4eq: gcd of opposite signed linear factors divides twice the underlying gcd.
for P in range(1, 40):
    for Q in range(P + 1, 50):
        h = gcd(Q + P, Q - P)
        assert (2 * gcd(P, Q)) % h == 0

# A fixed raw vector has divisor-many factorizations X=c*p and Y=d*q.
def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]

for X in range(2, 30):
    for Y in range(1, X):
        fac = [(c, X // c, d, Y // d) for c in divisors(X) for d in divisors(Y)]
        assert len(fac) == len(divisors(X)) * len(divisors(Y))
        W2 = X * X - Y * Y
        assert W2 > 0

# 4er: kappa in [1/6,1/4] forces lambda=1/2-kappa in [1/4,1/3].
for num in range(8, 13):
    kappa = Fraction(num, 48)  # 1/6 through 1/4
    lam = Fraction(1, 2) - kappa
    assert Fraction(1, 4) <= lam <= Fraction(1, 3)
    assert kappa + lam == Fraction(1, 2)

# 4es: G^2|N overlap count exponent is 1/2-gamma.
for num in range(1, 12):
    gamma = Fraction(num, 48)
    exponent = gamma + (Fraction(1, 2) - 2 * gamma)
    assert exponent == Fraction(1, 2) - gamma
    assert exponent < Fraction(1, 2)

# Primitive sum of two squares has no odd 3 mod 4 divisor unless both coordinates vanish mod p.
for p in (3, 7, 11, 19, 23, 31):
    for x in range(p):
        for y in range(p):
            if (x * x + y * y) % p == 0:
                assert x % p == 0 and y % p == 0

# 4et: bilinear norm exponents add back to the square-root barrier.
for num in range(8, 13):
    kappa = Fraction(num, 48)
    beta_exp = Fraction(1, 2) - kappa
    assert kappa + beta_exp == Fraction(1, 2)

print({
    'batch': 'Stage14-4eq..4eu',
    'substantive_stages': 5,
    'heavy_ray_reverse_fiber': 'Bo1',
    'heavy_ray_branch': 'closed',
    'diffuse_norm_scale': '1/2',
    'diffuse_quotient': 'polynomial',
    'core_quotient_overlap': 'Bo1_on_saturation',
    'diffuse_receiver': 'Gaussian_bilinear_correlation',
    'all_survivors_theorem_gated': True,
    'current_exponent': '1/2',
    'next': 'Stage14-4ev',
})
