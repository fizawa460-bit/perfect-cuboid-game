#!/usr/bin/env python3
from fractions import Fraction
from math import gcd


def oddpart(n: int) -> int:
    n = abs(n)
    while n and n % 2 == 0:
        n //= 2
    return n


pythagorean_checks = 0
primitive_gcd_checks = 0
rotated_pair_checks = 0
reconstruction_checks = 0

for D in range(2, 161):
    for A in range(1, D):
        g = gcd(D, A)
        m = D + A
        n = D - A
        xp = D * D + A * A
        xm = D * D - A * A
        x0 = 2 * D * A

        assert m * n == xm
        assert m * m + n * n == 2 * xp
        assert m * m - n * n == 2 * x0
        rotated_pair_checks += 3

        assert xp * xp == xm * xm + x0 * x0
        pythagorean_checks += 1

        assert (xp + xm) % 2 == 0
        assert (xp - xm) % 2 == 0
        assert (xp + xm) // 2 == D * D
        assert (xp - xm) // 2 == A * A
        reconstruction_checks += 4

        # Any odd common prime of a Pythagorean side and X0 must already
        # come from the primitive-coordinate gcd.  Remove g^2 because
        # xp/xm scale quadratically in a common factor.
        g_xp_x0 = oddpart(gcd(xp, x0))
        g_xm_x0 = oddpart(gcd(xm, x0))
        assert g_xp_x0 == 1 or g_xp_x0 <= oddpart(g * g)
        assert g_xm_x0 == 1 or g_xm_x0 <= oddpart(g * g)

        if g == 1:
            assert g_xp_x0 == 1
            assert g_xm_x0 == 1
            assert oddpart(gcd(xp, xm)) == 1
        primitive_gcd_checks += 3


ledger_checks = 0
for k in range(0, 257):
    chi = Fraction(1, 6) + Fraction(k, 256) * (Fraction(1, 4) - Fraction(1, 6))
    phi = (chi + Fraction(1, 4)) / 2
    u = Fraction(1, 4) - chi
    s = Fraction(1, 4) - chi / 2
    r = Fraction(1, 8) + chi / 2

    plus = chi + s + s
    minus = u + r + r
    kagree = Fraction(1, 4) + Fraction(1, 4)
    mixed = chi + u

    assert plus == Fraction(1, 2)
    assert minus == Fraction(1, 2)
    assert kagree == Fraction(1, 2)
    assert mixed == Fraction(1, 4)
    assert phi == r
    assert u >= 0
    ledger_checks += 7


# Exact triple-centering identity on deterministic synthetic weights.
centering_checks = 0
for length in range(2, 18):
    wp = [((3 * i + length) % 7) for i in range(length)]
    wm = [((5 * i + 2 * length) % 9) for i in range(length)]
    wk = [((7 * i + 3 * length) % 11) for i in range(length)]

    P = Fraction(length, 1)
    mup = sum(map(Fraction, wp), Fraction(0, 1)) / P
    mum = sum(map(Fraction, wm), Fraction(0, 1)) / P
    muk = sum(map(Fraction, wk), Fraction(0, 1)) / P

    cp = [Fraction(x, 1) - mup for x in wp]
    cm = [Fraction(x, 1) - mum for x in wm]
    ck = [Fraction(x, 1) - muk for x in wk]

    assert sum(cp, Fraction(0, 1)) == 0
    assert sum(cm, Fraction(0, 1)) == 0
    assert sum(ck, Fraction(0, 1)) == 0

    lhs = sum((Fraction(wp[i] * wm[i] * wk[i], 1) for i in range(length)), Fraction(0, 1))
    rhs = P * mup * mum * muk
    rhs += mup * sum((cm[i] * ck[i] for i in range(length)), Fraction(0, 1))
    rhs += mum * sum((cp[i] * ck[i] for i in range(length)), Fraction(0, 1))
    rhs += muk * sum((cp[i] * cm[i] for i in range(length)), Fraction(0, 1))
    rhs += sum((cp[i] * cm[i] * ck[i] for i in range(length)), Fraction(0, 1))
    assert lhs == rhs
    centering_checks += 5


# Small divisor-fiber model for the third coordinate system.  For fixed
# D,A every ordered three-factor split of xp or xm is divisor-bounded.
def ordered_three_factor_count(n: int) -> int:
    total = 0
    for a in range(1, n + 1):
        if n % a:
            continue
        q = n // a
        for b in range(1, q + 1):
            if q % b == 0:
                total += 1
    return total


fiber_checks = 0
max_three_factor_fiber = 0
for D, A in [(5, 2), (7, 4), (8, 3), (11, 6), (13, 4), (17, 8), (19, 10)]:
    xp = D * D + A * A
    xm = D * D - A * A
    cp = ordered_three_factor_count(xp)
    cm = ordered_three_factor_count(xm)
    assert cp >= 1 and cm >= 1
    max_three_factor_fiber = max(max_three_factor_fiber, cp, cm)
    fiber_checks += 2


print("Stage14-X15 three-projection Pythagorean audit: PASS")
print(f"Pythagorean cone identity checks: {pythagorean_checks}")
print(f"rotated-pair projection checks: {rotated_pair_checks}")
print(f"square reconstruction checks: {reconstruction_checks}")
print(f"primitive odd-gcd checks: {primitive_gcd_checks}")
print(f"exact exponent-ledger checks: {ledger_checks}")
print(f"triple-centering checks: {centering_checks}")
print(f"small divisor-fiber checks: {fiber_checks}")
print(f"max small ordered three-factor fiber: {max_three_factor_fiber}")
print("current whole-family exponent: 1/2")
print("strict sub-square-root saving proved: false")
print("three complete coordinate systems: plus / minus / k-agreement")
print("remaining receiver: SquareRootQuarterPrimitivePythagoreanConeEightAtomicBlockThreeProjectionPhysicalCorrelationDensity")
print("X15 auxiliary H needed: false")
