#!/usr/bin/env python3
from pathlib import Path
from math import gcd

ROOT = Path(__file__).resolve().parents[4]

locks = {
    'stages/stage14/14-4ea/result.md': [
        'CANONICAL_ALLOCATION_RECIPROCAL_DENSITY_CHAIN_EXACT=true',
    ],
    'stages/stage14/14-4eb/result.md': [
        'FIRST_RECIPROCAL_EQUATION_IS_RECONSTRUCTION_AFTER_CANONICAL_ALLOCATION=true',
    ],
    'stages/stage14/14-4ec/result.md': [
        'SECOND_RECIPROCAL_SELECTOR_IS_GAUSSIAN_NORM_DIVISIBILITY=true',
        'PRIMITIVE_SECOND_RECIPROCAL_ROOT_PACKET_DEFINED=true',
    ],
    'stages/stage14/14-4ed/result.md': [
        'RECIPROCAL_SUBROUTE_H_NEEDED=true',
        'MAINLINE_SWITCHES_TO_CANONICAL_ALLOCATION_DENSITY=true',
        'MAINLINE_H_NEEDED=false',
    ],
    'stages/stage14/14-4ee/result.md': [
        'CANONICAL_ALLOCATION_REPRESENTED_BY_THREE_DIVISOR_INCIDENCE=true',
        'ONE_CANONICAL_ALLOCATION_TYPE_CAN_BE_FROZEN=true',
    ],
    'stages/stage14/14-4ef/result.md': [
        'MINUS_CANONICAL_DIVISOR_LEDGER_EXPONENT_NEUTRAL=true',
        'PLUS_GAUSSIAN_DIVISOR_ROOT_LEDGER_EXPONENT_NEUTRAL=true',
        'ONLY_SIMULTANEOUS_INTEGER_GAUSSIAN_DIVISOR_CORRELATION_CAN_SAVE=true',
        'MAINLINE_H_NEEDED=true',
    ],
    'stages/stage14/14-4-batch/4eb-4ef-report.md': [
        'BATCH_SUBSTANTIVE_STAGE_COUNT=5',
        'BATCH_STOP_REASON=requested_stage_limit_reached_with_theorem_gates',
        'S_ROUTE_H_STAGE=Stage14-sH71',
    ],
}
for rel, needles in locks.items():
    text = (ROOT / rel).read_text()
    for needle in needles:
        assert needle in text, (rel, needle)

# Canonical first reciprocal identity using doubled D,A.
for a, b, g in [(1, 2, 1), (2, 5, 3), (3, 8, 5), (5, 12, 7)]:
    assert gcd(a, b) == 1
    two_D = g * (a + b)
    two_A = g * (b - a)
    assert (two_D + two_A) ** 2 - (two_D - two_A) ** 2 == 4 * two_D * two_A

# Primitive odd prime divisors of X^2+Y^2 are 1 mod 4.
def prime_divisors(n):
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        out.append(n)
    return out

for x, y in [(1, 2), (2, 3), (3, 4), (4, 7), (5, 8), (7, 10)]:
    assert gcd(x, y) == 1
    for p in prime_divisors(x*x + y*y):
        if p != 2:
            assert p % 4 == 1, (x, y, p)

# Exact primitive cross-sign coprimality used by 4ee/4ef.
for a in range(1, 30):
    for b in range(a + 1, 35):
        if gcd(a, b) == 1:
            assert gcd(a*a + b*b, a*b) == 1

# Elementary dyadic ledger algebra: for D_a,D_b,D_+ <= H,
# the relaxed minus and plus sums are O(H^2) up to absolute constants.
for H in [16, 32, 64]:
    for Da in [1, 2, 4, 8, 16]:
        for Db in [1, 2, 4, 8, 16]:
            if Da <= H and Db <= H:
                relaxed_minus = H*H + H*Da + H*Db + Da*Db
                assert relaxed_minus <= 4 * H * H
    for Dp in [1, 2, 4, 8, 16, 32, 64]:
        if Dp <= H:
            relaxed_plus = H*H + Dp*H
            assert relaxed_plus <= 2 * H * H

print({
    'batch': 'Stage14-4eb..4ef',
    'substantive_stages': 5,
    'current_exponent': '1/2',
    'mainline_h_target': 'CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity',
    'reciprocal_h_target': 'CanonicalAllocationConditionalPrimitiveGaussianRootDensity',
})
