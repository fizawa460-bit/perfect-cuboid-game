#!/usr/bin/env python3
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[4]
GRAPH = ROOT / 'stages/stage14/scripts/14-4/rank_jump_graph_audit.py'
MAX_B = 50_000


def is_square(n):
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n


def factor(n):
    n = abs(n)
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            out.append((p, e))
        p = 3 if p == 2 else p + 2
    if n > 1:
        out.append((n, 1))
    return out


def v2part(n):
    q = 1
    while n % 2 == 0:
        q *= 2
        n //= 2
    return q


def half_angle_roots(A, B, C):
    hm = C - A
    hp = C + A
    if is_square(hm) and is_square(hp):
        kappa = 1
        u = isqrt(hm)
        v = isqrt(hp)
    else:
        assert hm % 2 == 0 and hp % 2 == 0
        assert is_square(hm // 2) and is_square(hp // 2)
        kappa = 2
        u = isqrt(hm // 2)
        v = isqrt(hp // 2)
    assert gcd(u, v) == 1
    assert A == kappa * (v * v - u * u) // 2
    assert B == kappa * u * v
    assert C == kappa * (v * v + u * u) // 2
    return kappa, u, v


def ordered_incidences():
    mod = runpy.run_path(str(GRAPH))
    keep, _ = mod['enumerate_multi'](MAX_B)
    object_edges = mod['object_edges']
    rows = []
    undirected = 0
    for (a, b, c, d), (mask, ds) in keep.items():
        if d > MAX_B or mask.bit_count() < 2:
            continue
        for f1, f2 in object_edges(a, b, c, mask, ds):
            undirected += 1
            rows.append((d, f1, f2))
            rows.append((d, f2, f1))
    assert undirected == 62, undirected
    assert len(rows) == 124
    return rows


def third_face(F1, F2, d):
    S, X, H = F1
    S2, X2, H2 = F2
    g = gcd(S, S2)
    G = g * d
    c = gcd(H, X2)
    assert G * G == H * H * S2 * S2 + S * S * X2 * X2
    scale = g * c
    assert (H * S2) % scale == 0
    assert (S * X2) % scale == 0
    assert G % scale == 0
    S3 = H * S2 // scale
    X3 = S * X2 // scale
    H3 = G // scale
    assert S3 * S3 + X3 * X3 == H3 * H3
    assert gcd(S3, X3) == 1
    assert H3 == d // c
    return (S3, X3, H3), G, c


def good_cells(X2, H, u, v, r, s):
    cells = {'--': 1, '-+': 1, '+-': 1, '++': 1}
    xgood = 1
    for p, e in factor(X2):
        if p == 2 or H % p == 0:
            continue
        pe = p ** e
        row = '-' if u % pe == 0 else '+'
        assert (u % pe == 0) ^ (v % pe == 0)
        col = '-' if r % pe == 0 else '+'
        assert (r % pe == 0) ^ (s % pe == 0)
        cells[row + col] *= pe
        xgood *= pe
    prod = 1
    for z in cells.values():
        prod *= z
    assert prod == xgood
    return cells, xgood


def cross_squarefull_receiver(X2, H, xcross):
    two = v2part(X2)
    codd = gcd(H, X2)
    while codd % 2 == 0:
        codd //= 2
    assert xcross % (two * codd) == 0
    residual = xcross // (two * codd)
    h = 1
    for p, e in factor(residual):
        assert p != 2
        h *= p ** ((e + 1) // 2)
    assert (h * h) % residual == 0
    assert X2 % (h * h) == 0
    assert xcross <= two * codd * h * h
    return two, codd, h, residual


def main():
    rows = ordered_incidences()
    four_linear_checks = 0
    square_neutral_checks = 0
    cross_receiver_checks = 0
    nontrivial_cells = 0
    qminusminus_formula_checks = 0

    for d, F1, F2 in rows:
        S, X, H = F1
        S2, X2, H2 = F2
        F3, G, c = third_face(F1, F2, d)
        S3, X3, H3 = F3

        k2, u, v = half_angle_roots(S2, X2, H2)
        k3, r, s = half_angle_roots(S3, X3, H3)

        A = S3 * X2
        C = X3 * S2
        diff = A * A - C * C
        assert diff > 0 and is_square(diff)

        FF = (r * u - s * v) * (r * u + s * v) * (r * v - s * u) * (r * v + s * u)
        assert FF > 0
        assert 4 * diff == (k2 * k3) ** 2 * FF
        assert is_square(FF)
        four_linear_checks += 1

        cells, xgood = good_cells(X2, H, u, v, r, s)
        assert X2 % xgood == 0
        xcross = X2 // xgood
        cross_squarefull_receiver(X2, H, xcross)
        cross_receiver_checks += 1

        for name, q in cells.items():
            assert FF % (q * q) == 0
            assert is_square(FF // (q * q))
            square_neutral_checks += 1
            if q > 1:
                nontrivial_cells += 1

        q = cells['--']
        if q > 1:
            assert u % q == 0 and r % q == 0
            a = u // q
            b = r // q
            reduced = (
                (q * q * a * b - s * v)
                * (q * q * a * b + s * v)
                * (b * v - s * a)
                * (b * v + s * a)
            )
            assert reduced == FF // (q * q)
            assert is_square(reduced)
            qminusminus_formula_checks += 1

    # Exact exponent ledger used by the theorem statement.
    gamma = Fraction(4, 21)
    assert Fraction(20, 21) / 5 == gamma
    assert 1 - gamma / 6 == Fraction(61, 63)
    assert Fraction(41, 42) - Fraction(61, 63) == Fraction(1, 126)
    assert Fraction(61, 63) < Fraction(41, 42)

    print(f'ORDERED_PHYSICAL_INCIDENCES={len(rows)}')
    print(f'FOUR_LINEAR_COMPATIBILITY_CHECKS={four_linear_checks}')
    print(f'SQUARE_NEUTRAL_CELL_CHECKS={square_neutral_checks}')
    print(f'NONTRIVIAL_GOOD_CELLS={nontrivial_cells}')
    print(f'QMINUSMINUS_REDUCED_FORMULA_CHECKS={qminusminus_formula_checks}')
    print(f'CROSS_RECEIVER_DECOMPOSITION_CHECKS={cross_receiver_checks}')
    print('HALF_ANGLE_FOUR_LINEAR_SQUARE_FACTORIZATION_AUDIT=true')
    print('GOOD_GCD_CELL_AUTOMATIC_SQUARE_FACTOR_AUDIT=true')
    print('CROSS_FACTOR_2_C_H2_DECOMPOSITION_AUDIT=true')
    print('CROSS_BOUND_61_63_LEDGER_AUDIT=true')
    print('CROSS_SAVING_1_126_LEDGER_AUDIT=true')
    print('ALL_AUDITS_PASS=true')


if __name__ == '__main__':
    main()
