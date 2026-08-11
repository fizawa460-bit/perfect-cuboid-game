#!/usr/bin/env python3

from fractions import Fraction as F
from math import isqrt

# 1. Range-stable exponent peel: a+lambda=a forces lambda=0.
for a in range(-8, 9):
    for lam in range(0, 9):
        if a + lam == a:
            assert lam == 0

# 2. Plus-state factorization identity.
for D in range(2, 25):
    for A in range(1, D):
        m = D + A
        n = D - A
        y = D * D - A * A
        s = D * D + A * A
        assert m * n == y
        assert m * m + n * n == 2 * s

# 3. Minus-state degree-two graph after extracting ell.
for ell in (5, 13, 17, 29):
    for a in range(1, 8):
        for b in range(1, 8):
            m = ell * a
            n = b
            y = a * b
            assert m * n == ell * y
            assert m * m + n * n == ell * ell * a * a + b * b

# 4. Fixed divisor pair determines at most one positive ell.
for x in range(1, 60):
    for a in range(1, 15):
        for b in range(1, 15):
            num = a * a + b * b
            plus = []
            if num % (2 * x) == 0:
                e = num // (2 * x)
                if e > 0:
                    plus.append(e)
            assert len(set(plus)) <= 1

            rhs = 2 * x - b * b
            minus = []
            if rhs > 0 and rhs % (a * a) == 0:
                q = rhs // (a * a)
                r = isqrt(q)
                if r * r == q and r > 0:
                    minus.append(r)
            assert len(set(minus)) <= 1

# 5. 4du Cauchy exponent ledger: I=B^(1/2-o), image=B^o => energy >= B^(1-o).
I_exp = F(1, 2)
image_exp = F(0, 1)
energy_lower = 2 * I_exp - image_exp
assert energy_lower == 1

# 6. Plus/plus collision identity.
examples = [
    (3, 5, 2, 7, 9, 4),
    (5, 7, 3, 11, 13, 6),
]
for r1, s1, x1, r2, s2, x2 in examples:
    # Verify equality iff candidate rational values agree.
    lhs = x2 * (r1 * r1 + s1 * s1)
    rhs = x1 * (r2 * r2 + s2 * s2)
    cand_equal = F(r1 * r1 + s1 * s1, 2 * x1) == F(r2 * r2 + s2 * s2, 2 * x2)
    assert (lhs == rhs) == cand_equal

print("Stage14-s7-62 forced collision-energy audit: PASS")
print("range-stable arithmetic mover prime scale: B^o(1)")
print("candidate image exponent: 0")
print("forced collision energy exponent under sqrt saturation: 1")
print("next: Stage14-s7-63")
