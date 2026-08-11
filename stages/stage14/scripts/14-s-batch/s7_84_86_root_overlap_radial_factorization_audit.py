from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def factorint(n: int) -> dict[int, int]:
    n = abs(n)
    out: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def squarefree_part(n: int) -> int:
    out = 1
    for p, e in factorint(n).items():
        if e % 2:
            out *= p
    return out


def rational_squareclass_rep(q: Fraction) -> int:
    assert q > 0
    parity: dict[int, int] = {}
    for p, e in factorint(q.numerator).items():
        parity[p] = (parity.get(p, 0) + e) % 2
    for p, e in factorint(q.denominator).items():
        # negative exponent has the same parity modulo 2
        parity[p] = (parity.get(p, 0) + e) % 2
    out = 1
    for p, e in parity.items():
        if e:
            out *= p
    return out


def is_rational_square(q: Fraction) -> bool:
    if q < 0:
        return False
    a = isqrt(q.numerator)
    b = isqrt(q.denominator)
    return a * a == q.numerator and b * b == q.denominator


# Rational squareclass representatives are integral squarefree and peel a square.
for q in [Fraction(1, 2), Fraction(18, 25), Fraction(75, 8), Fraction(98, 45)]:
    k = rational_squareclass_rep(q)
    assert squarefree_part(k) == k
    assert is_rational_square(q / k), (q, k, q / k)

# If two squarefree root kernels have fixed product squareclass K_Z, their
# noncommon parts multiply exactly to K_Z.
for kx, ky in [(6, 15), (10, 14), (21, 35), (30, 42)]:
    assert squarefree_part(kx) == kx
    assert squarefree_part(ky) == ky
    j = gcd(kx, ky)
    a = kx // j
    b = ky // j
    assert gcd(a, b) == 1
    assert gcd(j, a * b) == 1
    assert squarefree_part(kx * ky) == a * b

# Exact normal form: X=J*A*a^2, Y=J*B*b^2 with A*B=K_Z gives
# X*Y=K_Z*(J*a*b)^2.  With h=J*a*b this is the radial square identity.
examples = [
    (5, 3, 7, 2, 4),
    (11, 1, 13, 3, 5),
    (17, 5, 19, 2, 3),
]
for j, A, B, a, b in examples:
    assert gcd(A, B) == 1
    assert gcd(j, A * B) == 1
    X = j * A * a * a
    Y = j * B * b * b
    K = A * B
    h = j * a * b
    assert X * Y == K * h * h
    assert squarefree_part(X * Y) == K

checks = {
    'stages/stage14/14-s7-84/result.md': [
        'AGREEMENT_PAIR_TOTAL_VALUE_SUPPORT=Bo1',
        'POLYNOMIAL_FACTOR_MOBILITY_MUST_BE_ROOT_SIDE=true',
        'COMMON_CORE_ROOT_LINE_RECHARGED=false',
        'NEXT=Stage14-s7-85',
    ],
    'stages/stage14/14-s7-85/result.md': [
        'ROOT_KERNEL_NONCOMMON_SPLIT_COST=Bo1',
        'ROOT_KERNEL_DIFFUSION_ONLY_THROUGH_SHARED_OVERLAP_J=true',
        'GENERIC_SQUAREFREE_J_SAVING_CLAIMED=false',
        'NEXT=Stage14-s7-86',
    ],
    'stages/stage14/14-s7-86/result.md': [
        'ROOT_OVERLAP_SQUAREPART_RADIAL_EQUATION=d0_J_a_b_equals_c0_h',
        'FIXED_H_ROOT_OVERLAP_SQUAREPART_FIBER=Bo1',
        'S_ROUTE_HEAVY_RAY_SUPPORT_CAPACITY_EXPONENT_MAX=1/24',
        'UNIFORM_REQUIRED_HEAVY_RAY_MASS_EXPONENT_GT_1_24_PROVED=false',
        'RECEIVER_MATERIALLY_CHANGED=true',
        'NEXT=Stage14-s7-87',
    ],
}
for rel, needles in checks.items():
    text = (ROOT / rel).read_text()
    for needle in needles:
        assert needle in text, (rel, needle)

print('STAGE14_S_BATCH_S7_84_86_AUDIT=PASS')
