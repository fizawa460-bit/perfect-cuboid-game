#!/usr/bin/env python3
from pathlib import Path
from math import gcd, pi
import cmath

ROOT = Path(__file__).resolve().parents[4]

locks = {
    'stages/stage14/14-4ef/result.md': [
        'ONLY_SIMULTANEOUS_INTEGER_GAUSSIAN_DIVISOR_CORRELATION_CAN_SAVE=true',
        'MAINLINE_H_TARGET=CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity',
    ],
    'stages/stage14/14-sH71/BOUNDARY.txt': [
        'C0_FIXED_POWER_LOWER_BOUND_PROVED=false',
        'ROOT_LINE_PRINCIPAL_DENSITY_UNIFORMLY_POWER_SPARSE=false',
        'PREFERRED_NEXT_INTERNAL_REDUCTION=CommonCoreScaleStratifiedCanonicalAllocationRootLinePrincipalDensityPlusCenteredDiscrepancy',
        'NEXT_H_NEEDED=false',
    ],
    'stages/stage14/14-s7-74/result.md': [
        'POLYNOMIAL_C0_SATURATION_FORCES_CENTERED_DISCREPANCY_EXPONENT_ZERO=true',
        'SMALL_C0_REVERTS_TO_CANONICAL_ALLOCATION_DENSITY_OBSTRUCTION=true',
        'CURRENT_S_RECEIVER=SmallCommonCoreCanonicalBalancedIntegerGaussianAllocationDensity_OR_PolynomialCommonCoreCanonicalAllocationCenteredGaussianRootDiscrepancy',
    ],
    'stages/stage14/14-4eg/result.md': [
        'ROOT_INDICATOR_PRINCIPAL_PLUS_CENTERED_DECOMPOSITION_EXACT=true',
        'POLYNOMIAL_COMMON_CORE_SATURATION_REQUIRES_CENTERED_DISCREPANCY=true',
    ],
    'stages/stage14/14-4eh/result.md': [
        'CENTERED_ROOT_DISCREPANCY_EXPONENT_ZERO_ON_SATURATING_BLOCK=true',
        'RECIPROCAL_POLYNOMIAL_CORE_RECEIVER_IS_CENTERED_DISCREPANCY=true',
    ],
    'stages/stage14/14-4ei/result.md': [
        'SQRT_OBSTRUCTION_SPLIT_INTO_LOW_CORE_ALLOCATION_OR_POLYNOMIAL_CORE_DISCREPANCY=true',
    ],
    'stages/stage14/14-4ej/result.md': [
        'CENTERED_ROOT_LINE_HAS_EXACT_MULTIPLICATIVE_CHARACTER_EXPANSION=true',
        'ROOT_SET_CHARACTER_COEFFICIENT_L2_IDENTITY_EXACT=true',
    ],
    'stages/stage14/14-4ek/result.md': [
        'FIXED_C_CHARACTER_ENERGY_PROJECTIVE_COLLISION_IDENTITY_EXACT=true',
        'POLYNOMIAL_CORE_DISCREPANCY_SPLIT_INTO_CONCENTRATED_OR_DIFFUSE_MODULUS=true',
        'DIFFUSE_MODULUS_BRANCH_REMAINS_VARIABLE_NORM_DIVISOR_GRAPH=true',
    ],
    'stages/stage14/14-4-batch/4eg-4ek-report.md': [
        'BATCH_PUBLICATION_MAIN_SHA=7bcb1b56d11c92249c826e7c6cbe9b86f2f9b3a4',
        'MERGED_S7_72_74_CONSUMED=true',
        'BATCH_SUBSTANTIVE_STAGE_COUNT=5',
        'NEXT=Stage14-4el',
    ],
}

for rel, needles in locks.items():
    text = (ROOT / rel).read_text()
    for needle in needles:
        assert needle in text, (rel, needle)


def factor(n):
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            out.append((p, e))
        p += 1 if p == 2 else 2
    if n > 1:
        out.append((n, 1))
    return out


def phi(n):
    ans = n
    for p, _ in factor(n):
        ans = ans // p * (p - 1)
    return ans


def roots_minus_one(n):
    return [r for r in range(n) if gcd(r, n) == 1 and (r*r + 1) % n == 0]


# Root-count / principal-density identities on representative split squarefree moduli.
for c in (5, 13, 17, 29, 37, 65, 85, 145):
    fs = factor(c)
    if all(e == 1 and p % 4 == 1 for p, e in fs):
        roots = roots_minus_one(c)
        assert len(roots) == 2 ** len(fs), (c, roots)
        unit_pairs = phi(c) ** 2
        hits = 0
        for x in range(c):
            if gcd(x, c) != 1:
                continue
            for y in range(c):
                if gcd(y, c) != 1:
                    continue
                if (x*x + y*y) % c == 0:
                    hits += 1
        assert hits == len(roots) * phi(c)
        assert abs(hits / unit_pairs - len(roots) / phi(c)) < 1e-12


# Exact multiplicative-character expansion for prime split moduli.
def primitive_root(p):
    ph = p - 1
    prime_divs = [q for q, _ in factor(ph)]
    for g in range(2, p):
        if all(pow(g, ph // q, p) != 1 for q in prime_divs):
            return g
    raise AssertionError(p)


def check_prime_character_expansion(p):
    g = primitive_root(p)
    order = p - 1
    log = {}
    x = 1
    for k in range(order):
        log[x] = k
        x = (x * g) % p
    roots = roots_minus_one(p)

    def chi(j, t):
        return cmath.exp(2j * pi * j * log[t] / order)

    hat = []
    for j in range(order):
        hat.append(sum(chi(j, r).conjugate() for r in roots))

    # Parseval for the root-set indicator.
    assert abs(sum(abs(v) ** 2 for v in hat) - order * len(roots)) < 1e-8

    for t in range(1, p):
        inv = sum(hat[j] * chi(j, t) for j in range(order)) / order
        expected = 1.0 if t in roots else 0.0
        assert abs(inv.real - expected) < 1e-8
        assert abs(inv.imag) < 1e-8

    # Weighted projective-collision energy identity.
    candidates = [(1, 1, 1.0), (2, 1, 2.0), (3, 2, 1.5), (4, 3, 0.5)]
    A = []
    for j in range(order):
        A.append(sum(w * chi(j, X) * chi(j, Y).conjugate() for X, Y, w in candidates))
    lhs = sum(abs(A[j]) ** 2 for j in range(1, order)) / order
    total_w = sum(w for _, _, w in candidates)
    collision = 0.0
    for X1, Y1, w1 in candidates:
        for X2, Y2, w2 in candidates:
            if (X1 * Y2 - X2 * Y1) % p == 0:
                collision += w1 * w2
    rhs = collision - total_w * total_w / order
    assert abs(lhs - rhs) < 1e-8, (p, lhs, rhs)


for p in (5, 13):
    check_prime_character_expansion(p)

print({
    'batch': 'Stage14-4eg..4ek',
    'substantive_stages': 5,
    'merged_s7_72_74_regression': 'locked',
    'root_principal_density_checks': 'ok',
    'character_expansion_checks': 'ok',
    'projective_collision_energy_checks': 'ok',
    'current_exponent': '1/2',
    'next': 'Stage14-4el',
})
