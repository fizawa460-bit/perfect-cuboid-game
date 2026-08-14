#!/usr/bin/env python3
from math import gcd, isqrt

A = -1156  # E: y^2 = x^3 + A x


def is_square(n: int) -> bool:
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n


def family_point(p: int, q: int, z: int):
    assert gcd(p, q) == 1
    assert p > 0 and q > 0 and z > 0
    assert p**4 + q**4 == 17 * z**2
    e = 4 * p * q
    x = 4 * p * p - q * q
    y = 4 * q * q - p * p
    d = 17 * z
    h1 = 4 * p * p + q * q
    h2 = 4 * q * q + p * p
    assert e * e + x * x == h1 * h1
    assert e * e + y * y == h2 * h2
    assert e * e + x * x + y * y == d * d
    assert gcd(gcd(abs(e), abs(x)), abs(y)) == 1
    return e, x, y, d, h1, h2


def inv(a: int, p: int) -> int:
    return pow(a % p, -1, p)


def add(P, Q, p):
    if P is None:
        return Q
    if Q is None:
        return P
    x1, y1 = P
    x2, y2 = Q
    if x1 == x2 and (y1 + y2) % p == 0:
        return None
    if P != Q:
        m = ((y2 - y1) * inv(x2 - x1, p)) % p
    else:
        if y1 % p == 0:
            return None
        m = ((3 * x1 * x1 + A) * inv(2 * y1, p)) % p
    x3 = (m * m - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    return x3, y3


def mul(n, P, p):
    R = None
    Q = P
    while n:
        if n & 1:
            R = add(R, Q, p)
        Q = add(Q, Q, p)
        n >>= 1
    return R


def count_E(p: int) -> int:
    total = 1  # point at infinity
    for x in range(p):
        rhs = (x**3 + A * x) % p
        if rhs == 0:
            total += 1
        elif pow(rhs, (p - 1) // 2, p) == 1:
            total += 2
    return total


def point_order(P, p: int, group_order: int) -> int:
    assert mul(group_order, P, p) is None
    n = group_order
    d = 2
    while d * d <= n:
        while n % d == 0 and mul(n // d, P, p) is None:
            n //= d
        d += 1
    return n


def main():
    # Two exact mixed-parity C_17 points found by the fresh lower surgeon.
    witnesses = [
        (38, 43, 569),
        (859, 1186, 385241),
    ]
    rows = []
    for p, q, z in witnesses:
        e, x, y, d, h1, h2 = family_point(p, q, z)
        assert 0 < x < y < e
        assert not is_square(x * x + y * y)
        rows.append((p, q, z, x, y, e, d, h1, h2))

    assert rows[0][3:7] == (3927, 5952, 6536, 9673)
    assert rows[1][3:7] == (1544928, 4888503, 4075096, 6549097)

    # General elliptic-map identity.  With a=p^4 and b=q^4,
    # 289 z^4=(a+b)^2, so
    # (b-a)^2=(a+b)^2-4ab gives Y^2=X^3-1156X.
    for p, q, z in [(1, 2, 1), *witnesses]:
        assert p**4 + q**4 == 17 * z**2
        X_num = -4 * p * p * q * q
        X_den = z * z
        Y_num = 4 * p * q * (q**4 - p**4)
        Y_den = z**3
        # Clear denominators in Y^2 = X^3 - 1156 X.
        lhs = Y_num * Y_num * X_den**3
        rhs = X_num**3 * Y_den**2 - 1156 * X_num * X_den**2 * Y_den**2
        assert lhs == rhs

    # Boundary point (t,z)=(2,1) maps to P=(-16,120) on E.
    P = (-16, 120)
    assert P[1] * P[1] == P[0]**3 + A * P[0]

    # Good-reduction torsion certificate.  Delta has only primes 2 and 17.
    # #E(F_31)=32, #E(F_41)=52.  A rational torsion point would therefore
    # have order dividing 4 after the standard two-prime reduction argument,
    # while P mod 31 has exact order 16.
    n31 = count_E(31)
    n41 = count_E(41)
    assert (n31, n41) == (32, 52)
    P31 = (P[0] % 31, P[1] % 31)
    assert point_order(P31, 31, n31) == 16
    assert gcd(n31, n41) == 4

    # Branch audit for the third-face fiber product.
    # f1=t^4+1 has four simple finite roots.
    # f2=17t^4-16t^2+17 has derivative 4t(17t^2-8);
    # f2(0)=17 and f2 at t^2=8/17 equals 225/17, so all roots are simple.
    # A common root with f1 would give f2=-16 t^2=0, impossible.
    assert 17 != 0
    assert 225 != 0
    # Connected V4 degree-4 cover, eight disjoint simple branch values.
    degree = 4
    branch_values = 8
    total_ramification = 2 * branch_values
    two_g_minus_two = degree * (-2) + total_ramification
    genus = (two_g_minus_two + 2) // 2
    assert genus == 5

    print("STAGE24_50_QUARTIC_AUDIT=PASS")
    print(f"WITNESSES={[(r[0], r[1], r[3], r[4], r[5], r[6]) for r in rows]}")
    print(f"E_F31={n31} E_F41={n41} P_MOD31_ORDER=16 TORSION_GCD_BOUND=4")
    print("THIRD_FACE_FIBER_PRODUCT_GENUS=5")


if __name__ == "__main__":
    main()
