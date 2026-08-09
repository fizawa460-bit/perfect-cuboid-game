#!/usr/bin/env python3
"""Deterministic audit for Stage14-s6-08.

Checks on actual physical ordered incidences through the frozen s6-07 audit:
- exact half-angle four-bilinear factorization of the F2/F3 cross square;
- extraction of the full odd-good gcd-matrix product as an automatic square;
- normalized cross-square remains a square;
- normalized two difference-of-squares have the same squarefree kernel;
- the two raw factors satisfy the coupled linear identities;
- dual physical selector product Q*K=X2/kappa and its good-cell split;
- merged 4bl exponent/boundary regression.
"""
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[4]
S7 = ROOT / 'stages/stage14/scripts/14-s6-07/dual_half_angle_gcd_matrix_audit.py'
BL = ROOT / 'stages/stage14/14-4bl/result.md'


def is_square(n):
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n


def squarefree_kernel(n):
    """Product of primes occurring to odd valuation in |n|."""
    n = abs(n)
    assert n > 0
    out = 1
    e = 0
    while n % 2 == 0:
        n //= 2
        e ^= 1
    if e:
        out *= 2
    p = 3
    while p * p <= n:
        odd = 0
        while n % p == 0:
            n //= p
            odd ^= 1
        if odd:
            out *= p
        p += 2
    if n > 1:
        out *= n
    return out


def audit_row(mod, F1, F2, physical_d):
    prev = mod['audit_row'](F1, F2, physical_d)
    half_angles = mod['half_angles']
    F3 = prev['F3']
    S2, X2, H2 = F2
    S3, X3, H3 = F3

    k2, a, b = half_angles(F2)
    k3, c, d = half_angles(F3)
    assert gcd(a, b) == 1
    assert gcd(c, d) == 1

    # Half-angle reconstruction.
    assert 2 * S2 == k2 * (b * b - a * a)
    assert X2 == k2 * a * b
    assert 2 * S3 == k3 * (d * d - c * c)
    assert X3 == k3 * c * d

    # Raw cross-square and exact four-bilinear factorization.
    A0 = a * b * (d * d - c * c)
    C0 = c * d * (b * b - a * a)
    raw = A0 * A0 - C0 * C0
    L1 = a * d - b * c
    L2 = a * d + b * c
    L3 = b * d - a * c
    L4 = b * d + a * c
    assert raw == L1 * L2 * L3 * L4
    assert raw > 0 and is_square(raw)

    geom = (S3 * X2) ** 2 - (X3 * S2) ** 2
    assert geom > 0 and is_square(geom)
    assert 4 * geom == (k2 * k3) ** 2 * raw

    # Full odd-good gcd matrix from s6-07.
    q11, q12, q21, q22 = prev['cells']
    qprod = q11 * q12 * q21 * q22
    assert qprod == prev['xgood']
    for q in (q11, q12):
        assert a % q == 0
    for q in (q21, q22):
        assert b % q == 0
    for q in (q11, q21):
        assert c % q == 0
    for q in (q12, q22):
        assert d % q == 0

    a0 = a // (q11 * q12)
    b0 = b // (q21 * q22)
    c0 = c // (q11 * q21)
    d0 = d // (q12 * q22)

    M1 = q12 * q12 * a0 * d0
    M2 = q21 * q21 * b0 * c0
    M3 = q22 * q22 * b0 * d0
    M4 = q11 * q11 * a0 * c0

    nL1 = M1 - M2
    nL2 = M1 + M2
    nL3 = M3 - M4
    nL4 = M3 + M4
    norm = nL1 * nL2 * nL3 * nL4

    assert L1 == q11 * q22 * nL1
    assert L2 == q11 * q22 * nL2
    assert L3 == q12 * q21 * nL3
    assert L4 == q12 * q21 * nL4
    assert raw == qprod * qprod * norm
    assert norm > 0 and is_square(norm)

    # Exact normalized two-factor kernel collision.
    F = M1 * M1 - M2 * M2
    G = M3 * M3 - M4 * M4
    assert F == nL1 * nL2
    assert G == nL3 * nL4
    assert F != 0 and G != 0 and F * G == norm and F * G > 0
    assert squarefree_kernel(F) == squarefree_kernel(G)

    # Raw coupled identities: independent tensorization loses this relation.
    Fraw = a * a * d * d - b * b * c * c
    Graw = b * b * d * d - a * a * c * c
    assert raw == Fraw * Graw
    assert a * a * Fraw - b * b * Graw == d * d * (a ** 4 - b ** 4)
    assert b * b * Fraw - a * a * Graw == c * c * (a ** 4 - b ** 4)

    # Merged 4bl exact dual selector product, reconstructed from s6-07 selectors.
    Dm = prev['D0']
    Dp = prev['D1']
    assert a % Dm == 0 and b % Dp == 0
    km = a // Dm
    kp = b // Dp
    Q = Dp * Dm
    K = kp * km
    assert Q * K == a * b == X2 // k2
    assert gcd(Q, prev['xgood']) == q12 * q21
    assert gcd(K, prev['xgood']) == q11 * q22

    return {
        'qprod': qprod,
        'max_cell': max(q11, q12, q21, q22),
        'kernel': squarefree_kernel(F),
        'Q': Q,
        'K': K,
        'X2': X2,
    }


def main():
    mod = runpy.run_path(str(S7))
    rows = mod['ordered_physical_edges']()
    assert rows

    nontrivial_matrix = 0
    max_qprod = 1
    max_cell = 1
    nontrivial_kernel = 0
    for F1, F2, physical_d in rows:
        out = audit_row(mod, F1, F2, physical_d)
        if out['qprod'] > 1:
            nontrivial_matrix += 1
        if out['kernel'] > 1:
            nontrivial_kernel += 1
        max_qprod = max(max_qprod, out['qprod'])
        max_cell = max(max_cell, out['max_cell'])

    # Exact exponent ledger imported from merged 4bl.
    assert Fraction(41, 42) - Fraction(20, 21) == Fraction(1, 42)
    assert 2 * Fraction(10, 21) == Fraction(20, 21)
    assert Fraction(20, 21) < Fraction(41, 42)

    text = BL.read_text()
    required = [
        'STAGE14_4BL=DUAL_COMPACT_HALF_ANGLE_CRITICAL_SQUARE_REDUCTION',
        'DUAL_PRODUCT_IDENTITY=Q*K=X2/kappa',
        'OPTIMAL_PARTNER_LEG_SPLIT_EXPONENT=20/21',
        'SMALL_PARTNER_LEG_EDGE_BOUND=B^(20/21+o(1))',
        'SMALL_PARTNER_LEG_SECTOR_SAVING_VS_41_42=1/42',
        'CRITICAL_DUAL_DENOMINATOR_OR_CANCELLATION_SCALE=10/21',
        'FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false',
    ]
    for token in required:
        assert token in text, token

    print(f'ordered physical incidences audited={len(rows)}')
    print(f'nontrivial good gcd matrices={nontrivial_matrix}')
    print(f'nontrivial normalized kernels={nontrivial_kernel}')
    print(f'max audited gcd-matrix product={max_qprod}')
    print(f'max audited individual gcd cell={max_cell}')
    print('HALF_ANGLE_FOUR_BILINEAR_FACTORIZATION_AUDIT=true')
    print('GOOD_GCD_MATRIX_AUTOMATIC_SQUARE_FACTOR_AUDIT=true')
    print('NORMALIZED_CROSS_SQUARE_AUDIT=true')
    print('NORMALIZED_KERNEL_COLLISION_AUDIT=true')
    print('RAW_TWO_FACTOR_COUPLING_IDENTITY_AUDIT=true')
    print('DUAL_QK_PRODUCT_AND_GOOD_CELL_SPLIT_AUDIT=true')
    print('MERGED_4BL_EXPONENT_LEDGER_AUDIT=true')
    print('ALL_AUDITS_PASS=true')


if __name__ == '__main__':
    main()
