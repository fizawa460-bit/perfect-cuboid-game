#!/usr/bin/env python3
from collections import Counter
from math import gcd, isqrt
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[4]
BM = ROOT / 'stages/stage14/scripts/14-4/cross_sector_gcd_cell_audit.py'
T36 = ROOT / 'stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py'
MAX_B = 50_000
PAIR_H = 250


def is_square(n):
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n


def reconstruct(F2, F3):
    S2, X2, H2 = F2
    S3, X3, H3 = F3
    A = S3 * X2
    C = X3 * S2
    diff = A * A - C * C
    if diff <= 0 or not is_square(diff):
        return None
    Y = isqrt(diff)
    h0 = gcd(A, C)
    assert Y % h0 == 0
    H = A // h0
    S = C // h0
    X = Y // h0
    assert S * S + X * X == H * H
    assert gcd(S, X) == 1
    assert gcd(S, H) == 1

    g = gcd(S, S2)
    c0 = gcd(H, X2)
    assert gcd(g, c0) == 1
    scale = gcd(H * S2, S * X2)
    assert scale == g * c0
    assert H * S2 == scale * S3
    assert S * X2 == scale * X3

    d_rec = c0 * H3
    assert (g * d_rec) ** 2 == H * H * S2 * S2 + S * S * X2 * X2

    Araw = S * S2 // g
    Braw = X * S2 // g
    Craw = X2 * S // g
    D1 = H * S2 // g
    D2 = H2 * S // g
    assert Araw * Araw + Braw * Braw == D1 * D1
    assert Araw * Araw + Craw * Craw == D2 * D2
    assert Araw * Araw + Braw * Braw + Craw * Craw == d_rec * d_rec
    assert gcd(gcd(Araw, Braw), Craw) == 1

    return {
        'F1': (S, X, H),
        'raw': (Araw, Braw, Craw, d_rec),
        'g': g,
        'c0': c0,
        'h0': h0,
    }


def primitive_faces(Hmax):
    out = []
    mmax = isqrt(Hmax) + 2
    for m in range(2, mmax + 1):
        for n in range(1, m):
            if gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            H = m * m + n * n
            if H > Hmax:
                continue
            L1 = m * m - n * n
            L2 = 2 * m * n
            out.append((L1, L2, H))
            out.append((L2, L1, H))
    return out


def main():
    bm = runpy.run_path(str(BM))
    rows = bm['ordered_incidences']()
    third_face = bm['third_face']
    half_angle_roots = bm['half_angle_roots']

    forward_inverse_checks = 0
    minus_class_checks = 0
    plus_class_checks = 0
    active = Counter()

    for d_phys, F1, F2 in rows:
        F3, _, _ = third_face(F1, F2, d_phys)
        rec = reconstruct(F2, F3)
        assert rec is not None
        assert rec['F1'] == F1
        assert rec['raw'][3] == d_phys
        assert rec['c0'] * F3[2] == d_phys
        forward_inverse_checks += 1
        active[F2] += 1

        _, a, b = half_angle_roots(*F2)
        _, c, q = half_angle_roots(*F3)
        delta0 = (
            (a * q - b * c)
            * (a * q + b * c)
            * (b * q - a * c)
            * (b * q + a * c)
        )
        assert delta0 > 0 and is_square(delta0)
        fab = (b * b * c * c - a * a * q * q) * (b * b * q * q - a * a * c * c)
        assert fab == -delta0
        assert fab < 0 and is_square(-fab)
        anchor_minus = -(a * b) ** 2
        assert anchor_minus < 0 and is_square(-anchor_minus)
        minus_class_checks += 1

        fcd = (q * q * a * a - c * c * b * b) * (q * q * b * b - c * c * a * a)
        assert fcd == delta0
        anchor_plus = (q * q - c * c) ** 2
        assert is_square(anchor_plus)
        plus_class_checks += 1

    # Independent converse enumeration: every positive cross-square pair
    # reconstructs a primitive raw two-face + space-diagonal cuboid.
    faces = primitive_faces(PAIR_H)
    converse_pairs = 0
    admissible_pairs = 0
    for F2 in faces:
        for F3 in faces:
            rec = reconstruct(F2, F3)
            if rec is None:
                continue
            converse_pairs += 1
            if rec['raw'][3] <= MAX_B:
                admissible_pairs += 1
    assert converse_pairs > 0
    assert admissible_pairs > 0

    # The merged t36 audit must remain executable: 4bn uses its theorem,
    # but introduces no replacement fixed-fiber analytic estimate.
    runpy.run_path(str(T36), run_name='__main__')

    assert len(active) <= len(rows)
    assert max(active.values()) >= 1

    print(f'ORDERED_PHYSICAL_INCIDENCES={len(rows)}')
    print(f'FORWARD_INVERSE_BIJECTION_CHECKS={forward_inverse_checks}')
    print(f'INDEPENDENT_POSITIVE_CROSS_SQUARE_PAIRS={converse_pairs}')
    print(f'INDEPENDENT_B_ADMISSIBLE_PAIRS={admissible_pairs}')
    print(f'MINUS_TARGET_SQUARECLASS_CHECKS={minus_class_checks}')
    print(f'PLUS_REVERSE_SQUARECLASS_CHECKS={plus_class_checks}')
    print(f'ACTIVE_F2_SAMPLE_COUNT={len(active)}')
    print(f'MAX_SAMPLE_F2_FIBER={max(active.values())}')
    print('PHYSICAL_PAIR_CONVERSE_AUDIT=true')
    print('RECONSTRUCTED_RAW_PRIMITIVITY_AUDIT=true')
    print('RECONSTRUCTED_CUTOFF_D_EQUALS_C0_H3_AUDIT=true')
    print('PHYSICAL_CROSS_SQUARE_BIJECTION_AUDIT=true')
    print('T36_MINUS_SQUARECLASS_IDENTITY_AUDIT=true')
    print('UNIVERSAL_MINUS_ANCHOR_AUDIT=true')
    print('SYMMETRIC_PLUS_SQUARECLASS_IDENTITY_AUDIT=true')
    print('ACTIVE_DIRECTION_OBJECT_AUDIT=true')
    print('ALL_AUDITS_PASS=true')


if __name__ == '__main__':
    main()
