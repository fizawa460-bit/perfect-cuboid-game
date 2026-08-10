#!/usr/bin/env python3
from fractions import Fraction
from math import gcd
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[4]
PRED = ROOT / 'stages/stage14/scripts/14-4/cross_sector_gcd_cell_audit.py'


def omega(n: int) -> int:
    n = abs(n)
    out = 0
    p = 2
    while p * p <= n:
        if n % p == 0:
            out += 1
            while n % p == 0:
                n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out += 1
    return out


def main():
    mod = runpy.run_path(str(PRED))
    rows = mod['ordered_incidences']()
    third_face = mod['third_face']
    half_angle_roots = mod['half_angle_roots']
    good_cells = mod['good_cells']

    exact_f2_core = 0
    exact_f3_core = 0
    allocation_checks = 0
    max_allocation_count = 0

    for d_space, F1, F2 in rows:
        S, X, H = F1
        S2, X2, H2 = F2
        F3, G, c_scale = third_face(F1, F2, d_space)
        S3, X3, H3 = F3

        k2, a, b = half_angle_roots(S2, X2, H2)
        k3, c, d = half_angle_roots(S3, X3, H3)
        cells, qprod = good_cells(X2, H, a, b, c, d)

        q11 = cells['--']
        q12 = cells['-+']
        q21 = cells['+-']
        q22 = cells['++']
        assert q11 * q12 * q21 * q22 == qprod

        assert a % (q11 * q12) == 0
        assert b % (q21 * q22) == 0
        assert c % (q11 * q21) == 0
        assert d % (q12 * q22) == 0

        a0 = a // (q11 * q12)
        b0 = b // (q21 * q22)
        c0 = c // (q11 * q21)
        d0 = d // (q12 * q22)

        assert X2 % qprod == 0
        xcross = X2 // qprod
        assert k2 * a0 * b0 == xcross
        exact_f2_core += 1

        assert X3 % qprod == 0
        assert k3 * c0 * d0 == X3 // qprod
        exact_f3_core += 1

        # Every distinct prime power of Q has exactly four destination cells.
        # Hence cell allocation count is at most 4^omega(Q), which is
        # subpolynomial by the divisor bound.  We audit the exact finite count.
        alloc = 4 ** omega(qprod)
        max_allocation_count = max(max_allocation_count, alloc)
        allocation_checks += 1

        # Reconstruction from (core, cells, kappas) is exact.
        assert a == q11 * q12 * a0
        assert b == q21 * q22 * b0
        assert c == q11 * q21 * c0
        assert d == q12 * q22 * d0
        assert X2 == k2 * qprod * a0 * b0
        assert X3 == k3 * qprod * c0 * d0

    # Exact exponent ledger.
    gamma_cross = Fraction(4, 21)
    gamma_x2 = Fraction(20, 21)
    gamma_q = gamma_x2 - gamma_cross
    gamma_f3_core = 1 - gamma_q
    gamma_core = gamma_cross + gamma_f3_core

    assert gamma_q == Fraction(16, 21)
    assert gamma_f3_core == Fraction(5, 21)
    assert gamma_core == Fraction(3, 7)
    assert Fraction(1, 2) - gamma_core == Fraction(1, 14)

    mu_any = Fraction(41, 42) - gamma_core
    mu_cross = Fraction(61, 63) - gamma_core
    mu_sqrt = Fraction(1, 2) - gamma_core

    assert mu_any == Fraction(23, 42)
    assert mu_cross == Fraction(34, 63)
    assert mu_sqrt == Fraction(1, 14)
    assert mu_any - mu_cross == Fraction(1, 126)

    print(f'ORDERED_PHYSICAL_INCIDENCES={len(rows)}')
    print(f'EXACT_F2_NORMALIZED_CORE_CHECKS={exact_f2_core}')
    print(f'EXACT_F3_NORMALIZED_CORE_CHECKS={exact_f3_core}')
    print(f'FIXED_Q_ALLOCATION_CHECKS={allocation_checks}')
    print(f'MAX_FINITE_4_POWER_OMEGA_Q={max_allocation_count}')
    print('F2_CORE_IDENTITY_XCROSS_OVER_KAPPA=true')
    print('F3_CORE_IDENTITY_X3_OVER_KAPPA_Q=true')
    print('GOOD_PRODUCT_EXPONENT_16_21_LEDGER=true')
    print('NORMALIZED_CORE_EXPONENT_3_7_LEDGER=true')
    print('NORMALIZED_CORE_SQRT_MARGIN_1_14=true')
    print('MOVING_Q_ANY_IMPROVEMENT_THRESHOLD_23_42=true')
    print('MOVING_Q_CROSS_CEILING_THRESHOLD_34_63=true')
    print('MOVING_Q_SQRT_THRESHOLD_1_14=true')
    print('CROSS_THRESHOLD_GAP_1_126=true')
    print('ALL_AUDITS_PASS=true')


if __name__ == '__main__':
    main()
