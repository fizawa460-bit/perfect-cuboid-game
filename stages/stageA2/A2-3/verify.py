#!/usr/bin/env python3
from itertools import product
from math import isqrt


# Published equation-(6) direct evaluator.  The only coefficient parameterized
# here is the disputed c^4 d^4 coefficient in the a0 anchor factor; the
# published source is coeff=-18.  The remaining a1,a2,a3 factors are transcribed
# independently from equation (6), arXiv:2604.05459v1, PDF p.13.
def equation6(c, d, G, H, coeff=-18):
    anchor = (
        -4 * c**2 * d**4 * (c**2 - d**2) * G**4
        + (c**8 + coeff * c**4 * d**4 + d**8) * G**3 * H
        + 8 * c**2 * d**2 * (c**2 - d**2) * (2 * c**2 + d**2) * G**2 * H**2
        - (c**8 + coeff * c**4 * d**4 + d**8) * G * H**3
        - 4 * c**2 * d**4 * (c**2 - d**2) * H**4
    )
    a0 = (c**2 + d**2) ** 2 * anchor**2

    a1 = (
        8 * c**2 * d**2 * (c**4 - d**4) ** 2 * (G**2 + H**2) ** 2
        * (2 * c**2 * d**2 * G**2 - (c**4 - d**4) * G * H - 2 * c**2 * d**2 * H**2)
        * ((c**4 - d**4) * G**2 + 8 * c**2 * d**2 * G * H - (c**4 - d**4) * H**2)
    )

    a2_factors = [
        d * (c + d) * G - c * (c - d) * H,
        d * (c - d) * G + c * (c + d) * H,
        (c**2 - 2 * c * d - d**2) * G + (c**2 + d**2) * H,
        (c**2 + 2 * c * d - d**2) * G + (c**2 + d**2) * H,
        (c**2 + d**2) * G - (c**2 + 2 * c * d - d**2) * H,
        c * (c + d) * G - d * (c - d) * H,
        c * (c - d) * G + d * (c + d) * H,
        (c**2 + d**2) * G - (c**2 - 2 * c * d - d**2) * H,
    ]
    a2 = (c**2 - d**2) ** 2
    for f in a2_factors:
        a2 *= f

    a3_factors = [
        (c**4 - d**4) * G + 4 * c**2 * d**2 * H,
        4 * c**2 * d**2 * G - (c**4 - d**4) * H,
        (c**4 - 4 * c**2 * d**2 - d**4) * G + (c**4 + 4 * c**2 * d**2 - d**4) * H,
        (c**4 + 4 * c**2 * d**2 - d**4) * G - (c**4 - 4 * c**2 * d**2 - d**4) * H,
    ]
    a3 = 4 * c**2 * d**2 * G * H * (G**2 - H**2)
    for f in a3_factors:
        a3 *= f

    return (a0, a1, a2, a3), anchor


def square_root(n):
    assert n >= 0
    r = isqrt(n)
    return r if r * r == n else None


# 1. Exact nondegenerate source sanity point.
PARAM = (3, 1, 7, 1)
vals18, F18_at_point = equation6(*PARAM, coeff=-18)
assert F18_at_point == 1559424
assert vals18 == (
    243180321177600,
    1521303552000000,
    1362949057806336,
    403778845016064,
)

expected_roots = {
    (0, 0, 0): 15594240,
    (0, 0, 1): 25435392,
    (0, 1, 0): 40076544,
    (0, 1, 1): 44832000,
    (1, 0, 0): 42005760,
    (1, 0, 1): 46564608,
    (1, 1, 0): 55923456,
    (1, 1, 1): 59424000,
}
for bits in product((0, 1), repeat=3):
    s = vals18[0] + sum(bits[i] * vals18[i + 1] for i in range(3))
    assert square_root(s) == expected_roots[bits]

# Nondegenerate walls checked at the chosen point.
c, d, G, H = PARAM
assert c * d * G * H * (c*c - d*d) * (G*G - H*H) != 0
assert all(x != 0 for x in vals18[1:])

# 2. Negative control: changing only -18 -> -8 destroys 7 of 8 square sums.
vals8, F8_at_point = equation6(*PARAM, coeff=-8)
assert F8_at_point == 1831584
assert vals8[1:] == vals18[1:]
count8 = 0
for bits in product((0, 1), repeat=3):
    s = vals8[0] + sum(bits[i] * vals8[i + 1] for i in range(3))
    if square_root(s) is not None:
        count8 += 1
assert count8 == 1


# Small integer-polynomial helpers; coefficients are low-to-high.
def poly_add(a, b):
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        out[i] = (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_scale(a, c):
    return [c * x for x in a]


def poly_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_deriv(a):
    return [i * a[i] for i in range(1, len(a))] or [0]


def det_bareiss(M):
    A = [row[:] for row in M]
    n = len(A)
    if n == 0:
        return 1
    sign = 1
    prev = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            swap = next((i for i in range(k + 1, n) if A[i][k] != 0), None)
            if swap is None:
                return 0
            A[k], A[swap] = A[swap], A[k]
            sign *= -1
        pivot = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * pivot - A[i][k] * A[k][j]) // prev
        prev = pivot
        for i in range(k + 1, n):
            A[i][k] = 0
    return sign * A[-1][-1]


def resultant(a, b):
    m = len(a) - 1
    n = len(b) - 1
    ah = list(reversed(a))
    bh = list(reversed(b))
    N = m + n
    M = []
    for i in range(n):
        row = [0] * N
        row[i:i + m + 1] = ah
        M.append(row)
    for i in range(m):
        row = [0] * N
        row[i:i + n + 1] = bh
        M.append(row)
    return det_bareiss(M)


def discriminant(a):
    n = len(a) - 1
    return ((-1) ** (n * (n - 1) // 2)) * resultant(a, poly_deriv(a)) // a[-1]


# 3. A2.3.1 discriminant expansion.
# A18(k)=k^4-18k^2+1.
A18 = [1, 0, -18, 0, 1]
# 256 k^3 (k-1)^2 = 256(k^5-2k^4+k^3).
correction = [0, 0, 0, 256, -512, 256]
D18 = poly_add(poly_mul(A18, A18), correction)
EXPECTED_D18 = [1, 0, -36, 256, -186, 256, -36, 0, 1]
assert D18 == EXPECTED_D18
assert discriminant(D18) == -(2**80) * (3**3) * (5**2)

# 4. Reciprocal quotient identity.
# D18/k^4 = (k^4+k^-4)-36(k^2+k^-2)+256(k+k^-1)-186.
# With z=k+k^-1 this becomes
# (z^4-4z^2+2)-36(z^2-2)+256z-186.
Q18 = [-112, 256, -40, 0, 1]
constructed_Q18 = poly_add(
    poly_add([2, 0, -4, 0, 1], poly_scale([-2, 0, 1], -36)),
    [(-186), 256],
)
assert constructed_Q18 == Q18
assert discriminant(Q18) == -(2**32) * 3 * 5

# Excluded k=1 wall gives z=2 and Y=+-16.
def eval_poly(a, x):
    out = 0
    for c in reversed(a):
        out = out * x + c
    return out

assert eval_poly(D18, 1) == 256
assert eval_poly(Q18, 2) == 256

print("A2-3 source sanity point: PASS")
print("A2-3 published -18: 8/8 subset sums square")
print("A2-3 negative-control -8: 1/8 subset sums square")
print("A2-3 D18 discriminant: PASS")
print("A2-3 E18 quartic: Y^2=z^4-40z^2+256z-112")
print("A2-3 E18 discriminant: PASS")
print("A2-3 published-minus18 restart verifier: PASS")
