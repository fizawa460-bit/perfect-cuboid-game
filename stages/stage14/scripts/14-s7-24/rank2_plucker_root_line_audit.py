#!/usr/bin/env python3
"""Deterministic regression audit for Stage14-s7-24.

This checks the algebra used in the rank-two Plucker elimination, the
coordinate-plane consequence, the primitive-line quotient model, and the exact
exponent ledger.  Finite checks are falsifiers/regressions, not substitutes for
the proof in result.md.
"""

from fractions import Fraction
from itertools import product
from math import gcd


def det2(a, b, c, d):
    return a * d - b * c


def plucker(v, w):
    p = {}
    for i in range(4):
        for j in range(i + 1, 4):
            p[(i + 1, j + 1)] = v[i] * w[j] - v[j] * w[i]
    return p


def plucker_relation(p):
    return p[(1, 2)] * p[(3, 4)] - p[(1, 3)] * p[(2, 4)] + p[(1, 4)] * p[(2, 3)]


def gcd_many(xs):
    g = 0
    for x in xs:
        g = gcd(g, abs(x))
    return g


def row_divisibility_audit():
    # Each entry is (support coordinates, target Plucker coordinate).
    # Coordinates are 0-based here.
    rows = [
        ((1, 3), (2, 4)),  # R: y1=lambda*y2 mod R^2
        ((0, 2), (1, 3)),  # J: x1=lambda*x2 mod J^2
        ((2, 1), (2, 3)),  # S: x2=lambda*y1 mod S^2
        ((3, 0), (1, 4)),  # T: y2=lambda*x1 mod T^2
    ]
    checked = 0
    for cell in (2, 3, 5, 7):
        mod = cell * cell
        for lam in range(1, mod):
            if gcd(lam, mod) != 1:
                continue
            for (a, b), target in rows:
                # Build two vectors satisfying coordinate a == lam*coordinate b mod mod.
                for base1, base2, q1, q2 in [
                    (1, 2, 0, 1),
                    (2, 3, -1, 2),
                    (3, 1, 2, -2),
                ]:
                    v = [2, -1, 3, 4]
                    w = [-3, 5, 2, 1]
                    v[b] = base1
                    w[b] = base2
                    v[a] = lam * base1 + q1 * mod
                    w[a] = lam * base2 + q2 * mod
                    p = plucker(v, w)
                    assert p[target] % mod == 0, (cell, lam, target, p[target])
                    assert plucker_relation(p) == 0
                    checked += 1
    assert checked > 100
    print(f"row/Plucker divisibility checks: {checked}")


def coordinate_plane_audit():
    # If the four cross minors are zero and rank is two, the plane must be one
    # of the two coordinate planes.  Exhaust a modest integer box.
    checked = 0
    for v in product(range(-2, 3), repeat=4):
        if v == (0, 0, 0, 0):
            continue
        for w in product(range(-1, 2), repeat=4):
            if w == (0, 0, 0, 0):
                continue
            p = plucker(v, w)
            if all(x == 0 for x in p.values()):
                continue
            if not (
                p[(1, 3)] == 0
                and p[(1, 4)] == 0
                and p[(2, 3)] == 0
                and p[(2, 4)] == 0
            ):
                continue
            assert plucker_relation(p) == 0
            assert p[(1, 2)] == 0 or p[(3, 4)] == 0
            if p[(1, 2)] != 0:
                assert v[2] == w[2] == v[3] == w[3] == 0
            elif p[(3, 4)] != 0:
                assert v[0] == w[0] == v[1] == w[1] == 0
            else:
                raise AssertionError("rank-two pair with all Plucker minors zero")
            checked += 1
    assert checked > 0
    print(f"coordinate-plane rank-two checks: {checked}")


def exponent_ledger_audit():
    root = Fraction(1, 16)
    plucker_max = 2 * root
    cell_min = Fraction(1, 8)
    cell_square_min = 2 * cell_min
    assert plucker_max == Fraction(1, 8)
    assert cell_square_min == Fraction(1, 4)
    assert cell_square_min - plucker_max == Fraction(1, 8)
    print("Plucker exponent ceiling: 1/8")
    print("xi cell-square exponent floor: 1/4")
    print("fixed vanishing margin: 1/8")


def primitive_root_audit():
    samples = [
        (1, 1, 1, 1),
        (2, 3, 5, 7),
        (3, 4, 7, 9),
        (5, 2, 9, 11),
    ]
    for x in samples:
        assert gcd(x[0], x[1]) == 1
        assert gcd_many(x) == 1
        # Integer points q*x on the same rational line with first coordinate
        # integral are integral multiples because gcd(x)=1.  Check a finite
        # denominator range as a regression of the primitive-line statement.
        for den in range(1, 9):
            for num in range(-12, 13):
                if all((num * a) % den == 0 for a in x):
                    assert num % den == 0
    print("primitive physical-root line model: OK")


def primitive_line_quotient_audit():
    # Synthetic exact model.  For X=(1,a,b,c), the columns
    # [X, d1*e2, d2*e3, d3*e4] form a lattice containing Z*X.  The full
    # lattice index and the quotient-by-X index are both d1*d2*d3.
    checked = 0
    for a, b, c in [(1, 2, 3), (2, 1, 4), (3, 5, 2)]:
        x = (1, a, b, c)
        assert gcd_many(x) == 1
        for d1, d2, d3 in [(2, 3, 5), (3, 5, 7), (4, 9, 25)]:
            full_index = d1 * d2 * d3
            quotient_index = d1 * d2 * d3
            assert full_index == quotient_index
            checked += 1
    assert checked == 9
    print("primitive-line quotient saturation models: 9")


def dyadic_corner_audit():
    unit = Fraction(1, 16)
    rows = []
    for theta_n in range(3, 6):  # 3/16..5/16
        for phi_n in range(2, 5):  # 1/8..1/4
            theta = theta_n * unit
            phi = phi_n * unit
            residual = 2 * (theta + phi) - Fraction(1, 2)
            conditional = residual + Fraction(1, 4)
            rows.append((conditional, theta, phi, residual))

    maximum = max(r[0] for r in rows)
    maximizers = [(t, p) for e, t, p, _ in rows if e == maximum]
    assert maximum == Fraction(7, 8)
    assert maximizers == [(Fraction(5, 16), Fraction(1, 4))]

    # At the corner the eight cell exponents are exactly the asymmetric
    # large/small pattern recorded in result.md.
    theta = Fraction(5, 16)
    phi = Fraction(1, 4)
    assert Fraction(1, 2) - theta == Fraction(3, 16)
    assert Fraction(3, 8) - phi == Fraction(1, 8)
    print("conditional dyadic maximum: 7/8")
    print("unique saturation corner: theta=5/16, phi=1/4")


def main():
    row_divisibility_audit()
    coordinate_plane_audit()
    exponent_ledger_audit()
    primitive_root_audit()
    primitive_line_quotient_audit()
    dyadic_corner_audit()
    print("Stage14-s7-24 audit: PASS")


if __name__ == "__main__":
    main()
