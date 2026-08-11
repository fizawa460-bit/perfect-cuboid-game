from fractions import Fraction
from math import gcd, isqrt


def divisors(n: int):
    out = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


def tau(n: int) -> int:
    return len(divisors(n))


def r2_ordered_signed(n: int) -> int:
    total = 0
    lim = isqrt(n)
    for x in range(-lim, lim + 1):
        y2 = n - x * x
        if y2 < 0:
            continue
        y = isqrt(y2)
        if y * y == y2:
            total += 1 if y == 0 else 2
    return total


# 1. Exact Gaussian norm / rotated coordinate-product identities.
identity_checks = 0
for D in range(2, 180):
    for A in range(1, D):
        x = D * D + A * A
        y = D * D - A * A
        assert (D + A) * (D - A) == y
        # (1+i)conj(D+iA)=(D+A)+i(D-A)
        re_rot = D + A
        im_rot = D - A
        assert re_rot * im_rot == y
        assert x + y == 2 * D * D
        assert x - y == 2 * A * A
        identity_checks += 1

assert identity_checks > 10000

# 2. Classical representation bound r_2(n) <= 4 tau(n), checked on a finite range.
r2_checks = 0
for n in range(1, 2500):
    r2 = r2_ordered_signed(n)
    assert r2 <= 4 * tau(n)
    r2_checks += 1

# 3. Reverse real-factor reconstruction is divisor-many.
reverse_checks = 0
for n_minus in range(1, 3000):
    candidates = 0
    for lm in divisors(n_minus):
        lp = n_minus // lm
        if lp <= lm:
            continue
        if (lp + lm) % 2 != 0:
            continue
        D = (lp + lm) // 2
        A = (lp - lm) // 2
        assert D > A > 0
        assert D * D - A * A == n_minus
        candidates += 1
    assert candidates <= tau(n_minus)
    reverse_checks += 1

# 4. Exact theta-quarter exponent ledgers.
ledger_checks = 0
for k in range(0, 97):
    chi = Fraction(1, 6) + Fraction(k, 96) * (Fraction(1, 4) - Fraction(1, 6))
    phi = (chi + Fraction(1, 4)) / 2
    u = Fraction(1, 4) - chi
    s = Fraction(1, 4) - chi / 2
    r = phi
    plus = chi + s + s
    minus = u + r + r
    assert plus == Fraction(1, 2)
    assert minus == Fraction(1, 2)
    assert 2 * phi == chi + Fraction(1, 4)
    ledger_checks += 1

# 5. Elimination/resultant boundary: X,Y <-> D^2,A^2 is an invertible linear map.
# [X,Y]^T = [[1,1],[1,-1]] [D^2,A^2]^T, determinant -2.
det = 1 * (-1) - 1 * 1
assert det == -2
for d2 in range(1, 200):
    for a2 in range(0, d2):
        X = d2 + a2
        Y = d2 - a2
        assert Fraction(X + Y, 2) == d2
        assert Fraction(X - Y, 2) == a2

# 6. Synthetic finite-fiber plus/minus switch checks.
fiber_checks = 0
for D in range(5, 100):
    for A in range(1, D):
        if gcd(D, A) != 1:
            continue
        X = D * D + A * A
        Y = D * D - A * A
        # Every plus representation is bounded by 4*tau(X).
        assert r2_ordered_signed(X) <= 4 * tau(X)
        # Every minus reconstruction comes from a divisor pair of Y.
        assert (D - A) in divisors(Y)
        assert (D + A) == Y // (D - A)
        fiber_checks += 1

assert fiber_checks > 1000

print("Stage14-s7-48 Gaussian norm / coordinate-product audit: PASS")
print(f"identity checks: {identity_checks}")
print(f"r2 divisor-bound checks: {r2_checks}")
print(f"reverse divisor reconstruction checks: {reverse_checks}")
print(f"theta-quarter ledger checks: {ledger_checks}")
print(f"finite-fiber synthetic checks: {fiber_checks}")
print("linear elimination determinant: -2")
print("plus complete exponent: 1/2")
print("minus complete exponent: 1/2")
print("fresh algebraic resultant: false")
print("strict sub-sqrt whole-family saving proved: false")
print("auxiliary H needed: Stage14-sH48")
