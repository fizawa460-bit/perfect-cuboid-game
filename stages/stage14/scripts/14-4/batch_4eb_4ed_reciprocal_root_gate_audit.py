#!/usr/bin/env python3
from pathlib import Path
from math import gcd

ROOT = Path(__file__).resolve().parents[4]

locks = {
    'stages/stage14/14-4ea/result.md': [
        'CANONICAL_ALLOCATION_RECIPROCAL_DENSITY_CHAIN_EXACT=true',
        'SQRT_OBSTRUCTION_REDUCED_TO_CANONICAL_ALLOCATION_OR_RECIPROCAL_CONDITIONAL_DENSITY=true',
    ],
    'stages/stage14/14-4eb/result.md': [
        'FIRST_RECIPROCAL_EQUATION_IS_RECONSTRUCTION_AFTER_CANONICAL_ALLOCATION=true',
        'RECIPROCAL_CONDITIONAL_REDUCED_TO_SECOND_RECIPROCAL_AND_POST_COLUMN_FILTER=true',
    ],
    'stages/stage14/14-4ec/result.md': [
        'SECOND_RECIPROCAL_SELECTOR_IS_GAUSSIAN_NORM_DIVISIBILITY=true',
        'PRIMITIVE_SECOND_RECIPROCAL_ROOT_PACKET_DEFINED=true',
        'RECIPROCAL_CONDITIONAL_DENSITY_REDUCED_TO_ROOT_SELECTOR=true',
    ],
    'stages/stage14/14-4ed/result.md': [
        'INDEPENDENT_SECOND_GROWING_MODULUS_PRODUCED=false',
        'PRIMITIVE_GAUSSIAN_ROOT_CONDITIONAL_DENSITY_THEOREM_PROVED=false',
        'MAINLINE_H_NEEDED=true',
        'BATCH_STOP_REASON=new_external_lemma_needed',
    ],
    'stages/stage14/14-4-batch/4eb-4ed-report.md': [
        'BATCH_SUBSTANTIVE_STAGE_COUNT=3',
        'BATCH_STOP_REASON=new_external_lemma_needed',
        'AUXILIARY_STAGE=Stage14-sH71',
    ],
}

for rel, needles in locks.items():
    text = (ROOT / rel).read_text()
    for needle in needles:
        assert needle in text, (rel, needle)

# Canonical first-reciprocal identity.
for a, b, g in [(1, 2, 1), (2, 5, 3), (3, 8, 5), (5, 12, 7)]:
    assert gcd(a, b) == 1
    # Use doubled D,A to avoid parity restrictions in the deterministic identity check.
    two_D = g * (a + b)
    two_A = g * (b - a)
    # 4*((D+A)^2-(D-A)^2) = (2D+2A)^2-(2D-2A)^2 = 16DA.
    lhs4 = (two_D + two_A) ** 2 - (two_D - two_A) ** 2
    rhs4 = 4 * two_D * two_A
    assert lhs4 == rhs4

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

print({
    'batch': 'Stage14-4eb..4ed',
    'substantive_stages': 3,
    'stop_reason': 'new_external_lemma_needed',
    'current_exponent': '1/2',
    'next': 'Stage14-sH71',
})
