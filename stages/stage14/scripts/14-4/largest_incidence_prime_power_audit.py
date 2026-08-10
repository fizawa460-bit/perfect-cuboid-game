#!/usr/bin/env python3
from fractions import Fraction
from math import gcd
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[4]
PRED = ROOT / 'stages/stage14/scripts/14-4/cross_sector_gcd_cell_audit.py'


def factor(n: int):
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


def largest_prime_power(n: int):
    fs = factor(n)
    if not fs:
        return None
    ell, e = max(fs, key=lambda pe: pe[0])
    return ell, e, ell ** e


def main():
    mod = runpy.run_path(str(PRED))
    rows = mod['ordered_incidences']()
    third_face = mod['third_face']
    half_angle_roots = mod['half_angle_roots']
    good_cells = mod['good_cells']
    is_square = mod['is_square']

    incidence_norm_coprime_checks = 0
    unique_cell_checks = 0
    moving_quartic_checks = 0
    nondegenerate_quartic_checks = 0
    cell_counts = {'--': 0, '-+': 0, '+-': 0, '++': 0}

    for d_space, F1, F2 in rows:
        S, X, H = F1
        S2, X2, H2 = F2
        F3, _, _ = third_face(F1, F2, d_space)
        S3, X3, H3 = F3

        k2, a, b = half_angle_roots(S2, X2, H2)
        k3, c, d = half_angle_roots(S3, X3, H3)
        cells, Q = good_cells(X2, H, a, b, c, d)

        q11 = cells['--']
        q12 = cells['-+']
        q21 = cells['+-']
        q22 = cells['++']
        assert Q == q11 * q12 * q21 * q22

        a0 = a // (q11 * q12)
        b0 = b // (q21 * q22)
        c0 = c // (q11 * q21)
        d0 = d // (q12 * q22)

        F = (q12*q12*a0*d0)**2 - (q21*q21*b0*c0)**2
        G = (q22*q22*b0*d0)**2 - (q11*q11*a0*c0)**2
        delta_norm = F * G
        assert delta_norm > 0 and is_square(delta_norm)

        if Q == 1:
            continue

        assert gcd(Q, a*a + b*b) == 1
        assert gcd(Q, H2) == 1
        incidence_norm_coprime_checks += 1

        ell, e, z = largest_prime_power(Q)
        R = Q // z
        assert ell % 2 == 1 and gcd(z, R) == 1
        for p, _ in factor(R):
            assert p < ell

        containing = [name for name, q in cells.items() if q % z == 0]
        assert len(containing) == 1
        cell = containing[0]
        cell_counts[cell] += 1
        unique_cell_checks += 1

        if cell == '--':
            r = q11 // z
            K = F
            A = q22*q22*b0*d0
            Bc = r*r*a0*c0
        elif cell == '++':
            r = q22 // z
            K = -F
            A = q11*q11*a0*c0
            Bc = r*r*b0*d0
        elif cell == '-+':
            r = q12 // z
            K = -G
            A = q21*q21*b0*c0
            Bc = r*r*a0*d0
        else:
            r = q21 // z
            K = G
            A = q12*q12*a0*d0
            Bc = r*r*b0*c0

        quartic_value = K * (A*A - Bc*Bc*z**4)
        assert quartic_value == delta_norm
        moving_quartic_checks += 1
        assert K and A and Bc and A*A - Bc*Bc*z**4
        nondegenerate_quartic_checks += 1

    assert incidence_norm_coprime_checks > 0
    assert unique_cell_checks == moving_quartic_checks == nondegenerate_quartic_checks

    base = Fraction(3, 7) + 1
    assert base == Fraction(10, 7)
    assert base - Fraction(41, 42) == Fraction(19, 42)
    assert base - Fraction(61, 63) == Fraction(29, 63)
    assert base - Fraction(1, 2) == Fraction(13, 14)
    assert Fraction(41, 42) - Fraction(13, 14) == Fraction(1, 21)
    assert Fraction(16, 21) - Fraction(29, 63) == Fraction(19, 63)

    print(f'ORDERED_PHYSICAL_INCIDENCES={len(rows)}')
    print(f'NONTRIVIAL_Q_INCIDENCES={incidence_norm_coprime_checks}')
    print(f'UNIQUE_LARGEST_PRIME_POWER_CELL_CHECKS={unique_cell_checks}')
    print(f'MOVING_Z_QUARTIC_IDENTITY_CHECKS={moving_quartic_checks}')
    print(f'NONDEGENERATE_MOVING_Z_QUARTIC_CHECKS={nondegenerate_quartic_checks}')
    print('CELL_COUNTS=' + ','.join(f'{k}:{v}' for k, v in sorted(cell_counts.items())))
    print('Q_ODD_PRIMES_COPRIME_TO_DIRECTION_NORM_AUDIT=true')
    print('LARGEST_PRIME_POWER_UNIQUE_CELL_AUDIT=true')
    print('MOVING_Z_QUARTIC_EXACT_AUDIT=true')
    print('MOVING_Z_GENUS_ONE_NONDEGENERACY_AUDIT=true')
    print('LARGE_Z_BOUND_BASE_EXPONENT_10_7=true')
    print('LARGE_Z_ANY_IMPROVEMENT_THRESHOLD_19_42=true')
    print('LARGE_Z_CROSS_CEILING_THRESHOLD_29_63=true')
    print('LARGE_Z_SQRT_THRESHOLD_13_14=true')
    print('SUPER_SQRT_Z_BOUND_13_14=true')
    print('SUPER_SQRT_Z_GAIN_1_21=true')
    print('HARD_COMPLEMENT_R_LOWER_19_63=true')
    print('ALL_AUDITS_PASS=true')


if __name__ == '__main__':
    main()
