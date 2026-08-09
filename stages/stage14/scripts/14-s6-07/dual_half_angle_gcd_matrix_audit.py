#!/usr/bin/env python3
"""Deterministic audit for Stage14-s6-07.

Audits actual physical edges through B=50,000 and checks:
- exact third primitive Pythagorean face transfer;
- injective recovery data `(F2,F3) -> F1,d` on the physical image;
- exact cross-product square compatibility;
- the two compact torsion denominator formulas;
- the 2x2 good-odd half-angle gcd matrix;
- the five-factor decomposition of X2.
"""
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[4]
GRAPH = ROOT / 'stages/stage14/scripts/14-4/rank_jump_graph_audit.py'
B = 50_000


def is_square(n):
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n


def prime_factorization(n):
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            out.append((p, e))
        p += 1 if p == 2 else 2
    if n > 1:
        out.append((n, 1))
    return out


def x_good_part(x2, H):
    out = 1
    for p, e in prime_factorization(x2):
        if p != 2 and H % p != 0:
            out *= p ** e
    return out


def half_angles(face):
    S, X, H = face
    assert S * S + X * X == H * H
    rm, rp = H - S, H + S
    a = isqrt(rm)
    b = isqrt(rp)
    if a * a == rm and b * b == rp:
        return 1, a, b
    assert rm % 2 == 0 and rp % 2 == 0
    a = isqrt(rm // 2)
    b = isqrt(rp // 2)
    assert 2 * a * a == rm and 2 * b * b == rp
    return 2, a, b


def square_den(fr):
    q = fr.denominator
    r = isqrt(q)
    assert r * r == q, (fr, q)
    return r


def ordered_physical_edges():
    mod = runpy.run_path(str(GRAPH))
    keep, _ = mod['enumerate_multi'](B)
    object_edges = mod['object_edges']
    rows = []
    seen = set()
    for (a, b, c, d), (mask, ds) in keep.items():
        if d > B or mask.bit_count() < 2:
            continue
        for f1, f2 in object_edges(a, b, c, mask, ds):
            edge = (f1, f2, d)
            rev = (f2, f1, d)
            for row in (edge, rev):
                if row not in seen:
                    seen.add(row)
                    rows.append(row)
    return rows


def audit_row(F1, F2, d):
    S, X, H = F1
    S2, X2, H2 = F2
    assert gcd(S, X) == gcd(S2, X2) == 1
    g = gcd(S, S2)
    G = g * d

    # s6-06 gluing identity.
    assert G * G == H * H * S2 * S2 + S * S * X2 * X2
    assert G * G == S * S * H2 * H2 + X * X * S2 * S2

    # Third primitive face.
    c = gcd(H, X2)
    h3scale = g * c
    assert gcd(g, c) == 1
    assert (H * S2) % h3scale == 0
    assert (S * X2) % h3scale == 0
    assert G % h3scale == 0
    assert d % c == 0
    F3 = (H * S2 // h3scale, S * X2 // h3scale, G // h3scale)
    S3, X3, H3 = F3
    assert gcd(S3, X3) == 1
    assert S3 * S3 + X3 * X3 == H3 * H3
    assert H3 == d // c <= B

    # Recovery / compatibility.
    assert Fraction(X3 * S2, S3 * X2) == Fraction(S, H)
    assert d == c * H3
    A = S3 * X2
    C = X3 * S2
    delta = A * A - C * C
    assert delta > 0 and is_square(delta)
    assert isqrt(delta) == X * S2 * X2 // h3scale

    # Half angles for F2,F3.
    _, t2m, t2p = half_angles(F2)
    _, t3m, t3p = half_angles(F3)
    assert gcd(t2m, t2p) == 1
    assert gcd(t3m, t3p) == 1

    # Dual compact selector exact formulas.
    N0 = H * G - S * S * H2 - X * X * S2
    Rm = H2 - S2
    z0 = Fraction(-N0, Rm)
    D0 = square_den(z0)
    assert t2m % D0 == 0

    N1 = H * G - S * S * H2 + X * X * S2
    Rp = H2 + S2
    # Independent factorization of the T_- numerator.
    nq = (G + H * S2) * (H * H2 - G)
    assert nq == Rm * N1
    z1a = Fraction(-nq, X2 * X2)
    z1b = Fraction(-N1, Rp)
    assert z1a == z1b
    D1 = square_den(z1b)
    assert t2p % D1 == 0

    # Good odd gcd matrix.
    xgood = x_good_part(X2, H)
    qmm = gcd(gcd(t2m, t3m), xgood)
    qmp = gcd(gcd(t2m, t3p), xgood)
    qpm = gcd(gcd(t2p, t3m), xgood)
    qpp = gcd(gcd(t2p, t3p), xgood)
    cells = (qmm, qmp, qpm, qpp)
    prod = 1
    for q in cells:
        prod *= q
    assert prod == xgood, (F1, F2, F3, xgood, cells)
    for i in range(4):
        for j in range(i + 1, 4):
            assert gcd(cells[i], cells[j]) == 1

    assert gcd(D0, xgood) == qmp
    assert gcd(t2m // D0, xgood) == qmm
    assert gcd(D1, xgood) == qpm
    assert gcd(t2p // D1, xgood) == qpp

    xcross = X2 // xgood
    assert xcross * prod == X2
    assert max(xcross, *cells) ** 5 >= X2

    # Prime-power root-sign -> third half-angle column.
    for p, e in prime_factorization(X2):
        if p == 2 or H % p == 0:
            continue
        pe = p ** e
        p2e = p ** (2 * e)
        assert (G * G - H * H * S2 * S2) % p2e == 0
        plus = (G - H * S2) % p2e == 0
        minus = (G + H * S2) % p2e == 0
        assert plus ^ minus
        if plus:
            assert t3m % pe == 0
            assert t3p % pe != 0
        else:
            assert t3p % pe == 0
            assert t3m % pe != 0

    return {
        'F3': F3,
        'D0': D0,
        'D1': D1,
        'xgood': xgood,
        'cells': cells,
    }


def main():
    rows = ordered_physical_edges()
    assert rows
    pair_keys = set()
    nontrivial_good = 0
    nontrivial_dual = 0
    max_cell = 1
    for F1, F2, d in rows:
        out = audit_row(F1, F2, d)
        key = (F2, out['F3'])
        assert key not in pair_keys, ('noninjective physical transfer', key)
        pair_keys.add(key)
        if out['xgood'] > 1:
            nontrivial_good += 1
        if out['D0'] > 1 or out['D1'] > 1:
            nontrivial_dual += 1
        max_cell = max(max_cell, *out['cells'])

    print(f'ordered physical incidences audited={len(rows)}')
    print(f'injective F2,F3 keys={len(pair_keys)}')
    print(f'nontrivial X2_good incidences={nontrivial_good}')
    print(f'nontrivial compact denominators={nontrivial_dual}')
    print(f'max audited gcd cell={max_cell}')
    print('THIRD_FACE_TRANSFER_AUDIT=true')
    print('PHYSICAL_EDGE_TO_F2_F3_INJECTIVE_AUDIT=true')
    print('F2_F3_CROSS_PRODUCT_SQUARE_AUDIT=true')
    print('DUAL_COMPACT_SELECTOR_AUDIT=true')
    print('GOOD_ODD_GCD_MATRIX_PRODUCT_AUDIT=true')
    print('DUAL_SELECTOR_GCD_CELL_IDENTIFICATION_AUDIT=true')
    print('FIVE_FACTOR_DICHOTOMY_AUDIT=true')
    print('ALL_AUDITS_PASS=true')


if __name__ == '__main__':
    main()
