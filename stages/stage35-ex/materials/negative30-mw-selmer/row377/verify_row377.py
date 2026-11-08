#!/usr/bin/env python3
"""Exact replay of the row377 identities and the rank-zero fixture."""

from fractions import Fraction
import json
from math import gcd, isqrt, prod

import sympy as sp


def verify_identities():
    U, V, W, t, s, u, w, Z = sp.symbols("U V W t s u w Z")
    relation = W**2 - U**2 - V**2

    def pythagorean_zero(expression):
        numerator = sp.cancel(expression).as_numer_denom()[0]
        assert sp.rem(numerator, relation, W) == 0

    P = V**2 * (s - 1)**2 + 4 * U**2 * s
    Q = W**2 * (s - 1)**2 + 4 * U**2 * s
    for factor, leading in ((P, V), (Q, W)):
        pythagorean_zero(
            factor.subs(s, t**2) / t**2 - leading**2 * (t - 1/t)**2 - 4 * U**2
        )
    pythagorean_zero(
        P.subs(s, t**2) / t**2 - (V**2 * (t + 1/t)**2 + 4 * (U**2 - V**2))
    )
    pythagorean_zero(Q.subs(s, t**2) / t**2 - (W**2 * (t + 1/t)**2 - 4 * V**2))

    e3_rhs = (V**2 * w**2 + 4 * U**2) * (W**2 * w**2 + 4 * U**2)
    X = 4 * U**2 / w**2
    pythagorean_zero((2 * U / w**3)**2 * e3_rhs - X * (X + V**2) * (X + W**2))

    euv_rhs = (V**2 * u**2 + 4 * (U**2 - V**2)) * (W**2 * u**2 - 4 * V**2)
    X = (V * W * u / 2)**2 - V**4
    pythagorean_zero((V**2 * W**2 * u / 8)**2 * euv_rhs - X * (X + U**4) * (X + V**4))
    pythagorean_zero(euv_rhs.subs(u, 2) - (4 * U**2)**2)
    pythagorean_zero(X.subs(u, 2) - U**2 * V**2)
    assert sp.cancel(X.subs(u, 2 * V / W)) == 0
    assert sp.cancel(euv_rhs.subs(u, 2 * V / W)) == 0

    X = W**2 + 4 * U**2 * s / (s - 1)**2
    pythagorean_zero(
        (U * (s + 1) / (s - 1)**3)**2 * P * Q - X * (X - U**2) * (X - V**2)
    )
    X = (W + U) * (W + V)
    Y = X * (U + V)
    pythagorean_zero(Y**2 - X * (X - U**2) * (X - V**2))
    slope = (3 * X**2 - 2 * W**2 * X + U**2 * V**2) / (2 * Y)
    double_x = slope**2 + W**2 - 2 * X
    pythagorean_zero(double_x - W**2)
    pythagorean_zero(slope * (X - double_x) - Y - U * V * W)
    m, n = sp.symbols("m n")
    assert sp.expand(X.subs({W: m*m + n*n, U: m*m - n*n, V: 2*m*n}) - 2 * m*m * (m+n)**2) == 0

    A, B, C, r, l, p, q, a = sp.symbols("A B C r l p q a")
    z_num = r * q - l * p
    L = p * q - r * l
    common = A**2 * B**2 - z_num**2 - 2 * r * l * L
    assert sp.expand(common).subs({p**2: A**2 + r*r, q**2: A**2 + l*l, B**2: r*r + l*l}).expand() == 0
    for sign in (-1, 1):
        lifted = A**2 * (r + sign*l)**2 - z_num**2 - 2 * r * l * (L + sign*A**2)
        assert sp.expand(lifted - common - A**2 * (r*r + l*l - B**2)) == 0
        L0 = A * C / a**2
        assert sp.cancel(L0 * (L0 + sign*A**2) - (A/a**2)**2 * C * (C + sign*A*a**2)) == 0

    R, d, z = sp.symbols("R d z")
    X = 2*d*W**2 + 2*d*(W**2 - R**2)/(z - 1)
    scale = 2*d*W*(W**2 - R**2)/(z - 1)**2
    cubic = (X - 2*d*W*R) * (X + 2*d*W*R) * (X - d*(W**2 + R**2))
    assert sp.cancel(cubic - scale**2 * d*(z**2 - 1)*(z**2 - (R/W)**2)) == 0


def prime_support(n):
    """Trial division with a complete terminating bound."""
    factors = []
    p = 2
    while p*p <= n:
        if n % p == 0:
            factors.append(p)
            while n % p == 0:
                n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        factors.append(n)
    return factors


def squarefree_divisors(primes):
    divisors = [1]
    for p in primes:
        divisors += [p*d for d in divisors]
    return sorted(divisors)


def local_classes(a2, a4, classes, levels):
    steps = []
    for p, k in levels:
        modulus = p**k
        square = {i*i % modulus for i in range(modulus)}
        second = [i*i % modulus for i in range(modulus)]
        fourth = [j*j % modulus for j in second]
        survivors = []
        for d in classes:
            assert a4 % d == 0
            c = a4 // d
            # Primitive projective charts (M,e) = (1,j), or (j,1) with p|j.
            if (any((d + a2*second[j] + c*fourth[j]) % modulus in square
                    for j in range(modulus))
                or any((d*fourth[j] + a2*second[j] + c) % modulus in square
                       for j in range(0, modulus, p))):
                survivors.append(d)
        classes = survivors
        steps.append({"p": p, "exponent": k, "survivors": classes})
    return steps


def rank_zero_fixture():
    m, n = 4096, 9
    U, V, W = m*m-n*n, 2*m*n, m*m+n*n
    assert gcd(m,n) == 1 and (m-n) % 2 == 1
    assert W > 10**7 and U*U + V*V == W*W
    assert (U, V, W) == (16777135, 73728, 16777297)
    primes = prime_support(V*W)
    primes_dual = prime_support(U)
    assert primes == [2, 3, 193, 86929]
    assert primes_dual == [5, 61, 67, 821]
    assert U == prod(primes_dual) and V == 2**13*3**2 and W == 193*86929
    ds = squarefree_divisors(primes)
    ds = sorted(ds + [-d for d in ds])
    ds_dual = squarefree_divisors(primes_dual)
    a = V*V + W*W
    steps = local_classes(a, (V*W)**2, ds, [(5,2), (61,2), (821,1)])
    steps_dual = local_classes(-2*a, U**4, ds_dual, [(2,5), (2,10), (3,2), (193,2)])
    assert [len(x["survivors"]) for x in steps] == [16, 8, 4]
    assert [len(x["survivors"]) for x in steps_dual] == [8, 4, 2, 1]
    assert steps[-1]["survivors"] == [-33554594, -1, 1, 33554594]
    assert steps_dual[-1]["survivors"] == [1]
    return {
        "m_n": [m,n],
        "U_V_W": [U,V,W],
        "positive_curve_primes": primes,
        "dual_curve_primes": primes_dual,
        "positive_curve_initial_count": len(ds),
        "dual_curve_initial_count": len(ds_dual),
        "positive_curve_local_steps": steps,
        "dual_curve_local_steps": steps_dual,
        "rank_upper_bound": 0,
    }


def double(point, a2, a4):
    if point is None or point[1] == 0:
        return None
    x, y = point
    assert y*y == x*(x*x + a2*x + a4)
    m = (3*x*x + 2*a2*x + a4) / (2*y)
    x_new = m*m - a2 - 2*x
    return x_new, m*(x-x_new) - y


def positive_rank_fixture():
    U, V, W = 21, 20, 29  # (m,n)=(5,2)
    assert U*U + V*V == W*W
    points = [
        (V, W, Fraction(-720), Fraction(5280), 2),
        (U*U, V*V, Fraction(-84707280,529), Fraction(10176974640,12167), 3),
    ]
    result = []
    for b, c, x, y, count in points:
        assert y*y == x*(x+b*b)*(x+c*c)
        point = (x,y)
        for _ in range(count):
            point = double(point, b*b+c*c, (b*c)**2)
        assert point is not None
        result.append({"point": [str(x),str(y)], "nonzero_multiple": 2**count})
    return {"m_n": [5,2], "points_on_split_models": result}


if __name__ == "__main__":
    verify_identities()
    print(json.dumps({
        "symbolic_identities": "PASS",
        "rank_zero_fixture": rank_zero_fixture(),
        "both_positive_rank_fixture": positive_rank_fixture(),
    }, indent=2))
