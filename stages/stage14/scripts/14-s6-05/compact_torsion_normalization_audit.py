#!/usr/bin/env python3
"""Deterministic regression audit for Stage14-s6-05.

The theorem-level claims are exact algebraic/real-component arguments in
result.md.  This script independently checks the key formulas on finite exact
rational samples, including compact witnesses with nontrivial denominator.
"""

from fractions import Fraction
import math


def factorint(n: int) -> dict[int, int]:
    n = abs(n)
    out: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def signed_squarefree_kernel(n: int) -> tuple[int, int]:
    assert n != 0
    r = 1
    for p, e in factorint(n).items():
        if e & 1:
            r *= p
    q = abs(n) // r
    u = math.isqrt(q)
    assert u * u == q
    return (r if n > 0 else -r), u


def admissible_tau_packets() -> list[tuple[int, int, int]]:
    vals = (-2, -1, 1, 2)
    out = []
    for t0 in vals:
        for t1 in vals:
            for t2 in vals:
                prod = t0 * t1 * t2
                if prod > 0 and math.isqrt(prod) ** 2 == prod:
                    out.append((t0, t1, t2))
    return out


TAU = admissible_tau_packets()
COMPACT_TAU = [t for t in TAU if t[0] < 0 and t[1] < 0 and t[2] > 0]


def primitive_triples(limit_m: int = 14):
    for m in range(2, limit_m + 1):
        for n in range(1, m):
            if math.gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            S = 2 * m * n
            X = m * m - n * n
            H = m * m + n * n
            assert S * S + X * X == H * H
            yield m, n, S, X, H


def curve_rhs(S: int, X: int, z: Fraction) -> Fraction:
    return z * (z - S * S) * (z + X * X)


def torsion_translate(S: int, X: int, z: Fraction, w: Fraction) -> tuple[Fraction, Fraction]:
    assert z != 0
    z2 = -Fraction(S * S * X * X, 1) / z
    w2 = Fraction(S * S * X * X, 1) * w / (z * z)
    return z2, w2


def check_s3_component_formula() -> int:
    checks = 0
    triples = list(primitive_triples(10))
    for _, _, S, X, H in triples[:12]:
        s = Fraction(S, H)
        rho = Fraction(X, H)
        assert s * s + rho * rho == 1
        A0 = 1 - 2 * rho * rho
        for _, _, S2, X2, H2 in triples[2:10:2]:
            q = Fraction(X2, H2 + S2)
            assert 0 < q < 1
            for z in (Fraction(1, 7), Fraction(3, 11), Fraction(5, 3)):
                Yq = z * (1 + q * q)
                X0 = (Yq + 1) / (q * q)
                x = (A0 + X0) / (2 * s * s)
                assert X0 > 1
                assert x > 1
                checks += 1
    return checks


def check_translation_samples() -> int:
    checks = 0

    # Universal rational 4-torsion sample on the identity component.
    for _, _, S, X, H in primitive_triples(10):
        z = Fraction(S * (S + H), 1)
        w = Fraction(S * H * (S + H), 1)
        assert curve_rhs(S, X, z) == w * w
        assert z > S * S
        z2, w2 = torsion_translate(S, X, z, w)
        assert curve_rhs(S, X, z2) == w2 * w2
        assert -X * X < z2 < 0
        z3, w3 = torsion_translate(S, X, z2, w2)
        assert z3 == z and w3 == w
        checks += 1

    # A known non-torsion algebraic sample used only for exact formula regression.
    S, X, H = 20, 21, 29
    zc = Fraction(-320, 1)
    wc = Fraction(5280, 1)
    assert curve_rhs(S, X, zc) == wc * wc
    zp, wp = torsion_translate(S, X, zc, wc)
    assert zp == Fraction(2205, 4)
    assert curve_rhs(S, X, zp) == wp * wp
    assert zp > S * S
    zback, wback = torsion_translate(S, X, zp, wp)
    assert zback == zc and wback == wc
    checks += 1

    return checks


def compact_square_witnesses(target: int = 12):
    out = []
    for m, n, S, X, H in primitive_triples(14):
        for D in range(1, 8):
            for A in range(-5000, 0):
                if math.gcd(A, D) != 1:
                    continue
                G0 = A
                G1 = A - S * S * D * D
                G2 = A + X * X * D * D
                if G2 <= 0:
                    continue
                y2 = G0 * G1 * G2
                if y2 <= 0:
                    continue
                Y = math.isqrt(y2)
                if Y * Y != y2:
                    continue
                ds = []
                us = []
                for G in (G0, G1, G2):
                    d, u = signed_squarefree_kernel(G)
                    ds.append(d)
                    us.append(u)
                out.append((m, n, S, X, H, D, A, Y, tuple(ds), tuple(us)))
                if len(out) >= target:
                    return out
    return out


def check_compact_packets() -> tuple[int, int]:
    hits = compact_square_witnesses(12)
    assert len(hits) == 12
    d_gt_1 = 0

    for rec in hits:
        m, n, S, X, H, D, A, Y, ds, us = rec
        d0, d1, d2 = ds
        u0, u1, u2 = us
        assert d0 < 0 and d1 < 0 and d2 > 0

        # Recover the odd edge packet and tau signs as in s6-01.
        odd = [abs(d) // (2 if abs(d) % 2 == 0 else 1) for d in ds]
        a = math.gcd(odd[0], odd[1])
        b = math.gcd(odd[0], odd[2])
        c = math.gcd(odd[1], odd[2])
        assert a * b == odd[0]
        assert a * c == odd[1]
        assert b * c == odd[2]
        tau = (d0 // (a * b), d1 // (a * c), d2 // (b * c))
        assert tau in COMPACT_TAU

        e0, e1, e2 = -d0, -d1, d2
        assert e1 * u1 * u1 - e0 * u0 * u0 == S * S * D * D
        assert e2 * u2 * u2 + e0 * u0 * u0 == X * X * D * D
        assert e2 * u2 * u2 + e1 * u1 * u1 == H * H * D * D

        assert e0 * u0 * u0 <= X * X * D * D
        assert e2 * u2 * u2 <= X * X * D * D
        assert e1 * u1 * u1 <= H * H * D * D
        assert max(u0, u1, u2) <= BOUND_FACTOR * H * D

        # Translate compact Z=A/D^2 back to the identity component.
        zq = Fraction(A, D * D)
        wq = Fraction(Y, D**3)
        assert curve_rhs(S, X, zq) == wq * wq
        zp, wp = torsion_translate(S, X, zq, wq)
        assert zp > S * S
        assert curve_rhs(S, X, zp) == wp * wp

        # Exact reduced-denominator involution in both directions.
        Ap = zp.numerator
        Dp2 = zp.denominator
        Dp = math.isqrt(Dp2)
        assert Dp * Dp == Dp2
        g = math.gcd(abs(Ap), S * S * X * X)
        assert abs(Ap) // g == D * D

        gq = math.gcd(abs(A), S * S * X * X)
        assert abs(A) // gq == Dp * Dp

        if D > 1:
            d_gt_1 += 1

    assert d_gt_1 >= 1
    return len(hits), d_gt_1


BOUND_FACTOR = 1  # H>=X, so the theorem-level |ui|<=B D audit uses H D here.


def check_tau_counts() -> None:
    assert len(TAU) == 16
    assert len(COMPACT_TAU) == 4
    assert set(COMPACT_TAU) == {
        (-1, -1, 1),
        (-2, -2, 1),
        (-2, -1, 2),
        (-1, -2, 2),
    }

    # The two-quadrics sign inequalities allow only +++ or --+ over R.
    feasible = []
    for s0 in (-1, 1):
        for s1 in (-1, 1):
            for s2 in (-1, 1):
                if s0 * s1 * s2 <= 0:
                    continue
                if s0 > 0:
                    if s2 <= 0:
                        continue
                    if s1 <= 0:
                        continue
                else:
                    if s1 >= 0:
                        continue
                    if s2 <= 0:
                        continue
                feasible.append((s0, s1, s2))
    assert set(feasible) == {(1, 1, 1), (-1, -1, 1)}


def main() -> None:
    check_tau_counts()
    component_checks = check_s3_component_formula()
    translation_checks = check_translation_samples()
    compact_hits, compact_d_gt_1 = check_compact_packets()

    print(f"ABSTRACT_TAU_PACKET_COUNT={len(TAU)}")
    print(f"PHYSICAL_COMPACT_TAU_PACKET_COUNT={len(COMPACT_TAU)}")
    print(f"S3_COMPONENT_FORMULA_CHECKS={component_checks}")
    print(f"TORSION_TRANSLATION_SAMPLE_CHECKS={translation_checks}")
    print(f"COMPACT_PACKET_WITNESSES={compact_hits}")
    print(f"COMPACT_PACKET_WITNESSES_D_GT_1={compact_d_gt_1}")
    print("PHYSICAL_Z_GT_S2_AUDIT=true")
    print("T0_TRANSLATION_INVOLUTION_AUDIT=true")
    print("COMPACT_SIGN_PACKET_AUDIT=true")
    print("COMPACT_POSITIVE_DEFINITE_BOUND_AUDIT=true")
    print("DENOMINATOR_INVOLUTION_AUDIT=true")
    print("ALL_AUDITS_PASS=true")


if __name__ == "__main__":
    main()
