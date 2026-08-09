#!/usr/bin/env python3
from fractions import Fraction
from math import gcd, isqrt, log
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[4]
GRAPH = ROOT / 'stages/stage14/scripts/14-4/rank_jump_graph_audit.py'
S3 = ROOT / 'stages/stage14/scripts/14-s3/small_point_gate_audit.py'
CUT = 50_000


def prime_powers(n):
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
        p += 1 if p == 2 else 2
    if n > 1:
        out.append((n, 1))
    return out


def v_p(n, p):
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def count_faces_with_second_leg_at_most(B, Y):
    # Counts primitive oriented Pythagorean faces with H<=B and oriented X<=Y.
    count = 0
    m = 2
    while m * m + 1 <= B:
        for n in range(1, m):
            if ((m - n) & 1) == 0 or gcd(m, n) != 1:
                continue
            u = m * m - n * n
            v = 2 * m * n
            h = m * m + n * n
            if h > B:
                continue
            if v <= Y:
                count += 1  # oriented face (u,v,h)
            if u <= Y:
                count += 1  # oriented face (v,u,h)
        m += 1
    return count


def main():
    graph = runpy.run_path(str(GRAPH))
    s3 = runpy.run_path(str(S3))
    keep, _ = graph['enumerate_multi'](CUT)
    object_edges = graph['object_edges']
    physical_point = s3['physical_point']

    oriented_edges = 0
    root_sign_checks = 0
    denominator_checks = 0

    for (a, b, c, d), (mask, ds) in keep.items():
        if d > CUT or mask.bit_count() < 2:
            continue
        for f1, f2 in object_edges(a, b, c, mask, ds):
            for face, partner in ((f1, f2), (f2, f1)):
                S, X, H = face
                S2, X2, H2 = partner
                g = gcd(S, S2)
                r = g * d

                # Raw-edge norm identities BK.1--BK.4.
                assert r * r == H * H * S2 * S2 + S * S * X2 * X2
                assert r * r == H * H * H2 * H2 - X * X * X2 * X2
                assert (r - H * S2) * (r + H * S2) == S * S * X2 * X2
                assert (H * H2 - r) * (H * H2 + r) == X * X * X2 * X2

                P = physical_point(face, partner, d)
                Z = P['Z']
                assert Z > S * S

                # Simplified physical Z-coordinate BK.5--BK.7.
                T = H2 - S2
                Z_simple = Fraction(S * S * H2 + X * X * S2 + H * r, T)
                assert Z == Z_simple
                assert Z - S * S == Fraction(H * (H * S2 + r), T)
                assert Z + X * X == Fraction(H * (H * H2 + r), T)

                # Translate by T_-=(-X^2,0).
                ZQ = -X * X * (Z - S * S) / (Z + X * X)
                ZQ_exact = Fraction((r + H * S2) * (r - H * H2), X2 * X2)
                assert ZQ == ZQ_exact
                assert -X * X < ZQ < 0

                den = ZQ.denominator
                D = isqrt(den)
                assert D * D == den
                assert X2 % D == 0
                C = X2 // D
                NQ = (r + H * S2) * (H * H2 - r)
                assert C * C == gcd(X2 * X2, NQ)
                assert NQ % (C * C) == 0
                denominator_checks += 1

                # Odd good half-angle/root-sign law BK.15.
                for ell, e in prime_powers(X2):
                    if ell == 2 or H % ell == 0:
                        continue
                    mod = ell ** (2 * e)
                    minus_half = (H2 - S2) % mod == 0
                    plus_half = (H2 + S2) % mod == 0
                    assert minus_half ^ plus_half

                    delta_plus = (r - H * S2) % mod == 0
                    delta_minus = (r + H * S2) % mod == 0
                    assert delta_plus ^ delta_minus

                    expected = e if (plus_half and delta_plus) else 0
                    assert v_p(D, ell) == expected, (
                        face, partner, d, ell, e, D,
                        minus_half, plus_half, delta_plus, delta_minus,
                    )
                    root_sign_checks += 1

                oriented_edges += 1

    assert oriented_edges > 0
    assert denominator_checks == oriented_edges

    # Finite regression of the elementary O(Y log B) face-count shape.
    B0 = 20_000
    for Y in (10, 20, 50, 100, 200, 500, 1000, 2000):
        n = count_faces_with_second_leg_at_most(B0, Y)
        # Deliberately loose deterministic envelope; theorem is proved by
        # the divisor-hyperbola argument in result.md.
        assert n <= 20 * Y * max(1.0, log(2 * B0))

    from fractions import Fraction as F
    assert F(41, 42) - F(1, 2) == F(10, 21)
    assert F(10, 21) == F(40, 84)
    assert F(40, 84) + F(1, 84) == F(41, 84)
    assert F(41, 84) < F(1, 2)

    print(f'ORIENTED_PHYSICAL_EDGES_AUDITED={oriented_edges}')
    print(f'DENOMINATOR_DIVISOR_CHECKS={denominator_checks}')
    print(f'ODD_GOOD_ROOT_SIGN_CHECKS={root_sign_checks}')
    print('PHYSICAL_RAW_EDGE_R_IDENTITY_AUDIT=true')
    print('PHYSICAL_S3_Z_SIMPLIFICATION_AUDIT=true')
    print('PHYSICAL_COMPACT_TRANSLATE_AUDIT=true')
    print('PHYSICAL_DENOMINATOR_DIVIDES_X2_AUDIT=true')
    print('PHYSICAL_CANCELLATION_COFACTOR_AUDIT=true')
    print('ODD_GOOD_HALF_ANGLE_ROOT_SIGN_AUDIT=true')
    print('SMALL_PARTNER_LEG_FACE_COUNT_SHAPE_AUDIT=true')
    print('EXPONENT_LEDGER_40_84_PLUS_1_84_EQUALS_41_84=true')
    print('ALL_AUDITS_PASS=true')


if __name__ == '__main__':
    main()
