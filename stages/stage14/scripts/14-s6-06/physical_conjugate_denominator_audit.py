#!/usr/bin/env python3
"""Deterministic audit for Stage14-s6-06.

The audit uses actual physical raw-pair edges through d<=50,000 and checks:
- exact physical gluing / third Pythagorean identity;
- direct simplification of the Stage14-s3 physical point;
- conjugate numerator and gap factorizations;
- the compact T0 denominator formulas;
- Euclid half-angle divisibility D_T|t and exact cofactor square;
- compact packet square-kernel identities;
- the good odd partner-leg prime root-sign law.

No PARI/GP or external package is required.
"""

from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[4]
GRAPH = ROOT / "stages/stage14/scripts/14-4/rank_jump_graph_audit.py"
S3 = ROOT / "stages/stage14/scripts/14-s3/small_point_gate_audit.py"
RESULT = ROOT / "stages/stage14/14-s6-06/result.md"
MAX_B = 50_000


def factor_small(n):
    n = abs(n)
    out = {}
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            out[p] = e
        p = 3 if p == 2 else p + 2
    if n > 1:
        out[n] = 1
    return out


def vp(n, p):
    n = abs(n)
    e = 0
    while n and n % p == 0:
        n //= p
        e += 1
    return e


def support_squarefree_kernel_and_root(n, support):
    """Return (squarefree kernel, square root after division).

    We only need to factor the small support integer.  If an odd-valuation
    prime outside support occurs, the final square test fails.
    """
    assert n > 0
    ker = 1
    for p in factor_small(support):
        if vp(n, p) & 1:
            ker *= p
    q, r = divmod(n, ker)
    assert r == 0
    u = isqrt(q)
    assert u * u == q, (n, support, ker, q)
    return ker, u


def partner_euclid(S2, X2, H2):
    assert gcd(S2, X2) == 1
    assert S2 * S2 + X2 * X2 == H2 * H2
    if S2 & 1:
        odd = S2
        even = X2
        role = "odd"
    else:
        odd = X2
        even = S2
        role = "even"
    m2sq = (H2 + odd) // 2
    n2sq = (H2 - odd) // 2
    m = isqrt(m2sq)
    n = isqrt(n2sq)
    assert m * m == m2sq and n * n == n2sq
    assert 2 * m * n == even
    assert m > n > 0 and gcd(m, n) == 1 and ((m - n) & 1)
    if role == "even":
        # S2=2mn, so H2-S2=(m-n)^2.
        kappa = 1
        t = m - n
        assert S2 == 2 * m * n
    else:
        # S2=m^2-n^2, so H2-S2=2n^2.
        kappa = 2
        t = n
        assert S2 == m * m - n * n
    assert H2 - S2 == kappa * t * t
    return m, n, role, kappa, t


def main():
    graph = runpy.run_path(str(GRAPH))
    s3 = runpy.run_path(str(S3))
    keep, _ = graph["enumerate_multi"](MAX_B)
    object_edges = graph["object_edges"]
    physical_point = s3["physical_point"]

    undirected = 0
    ordered = 0
    compact_d_gt_1 = 0
    root_checks = 0
    plus_checks = 0
    minus_positive_checks = 0
    minus_negative_checks = 0

    for (a, b, c, d), (mask, ds) in keep.items():
        if d > MAX_B or mask.bit_count() < 2:
            continue
        edges = object_edges(a, b, c, mask, ds)
        undirected += len(edges)
        for f1, f2 in edges:
            for face, partner in ((f1, f2), (f2, f1)):
                ordered += 1
                S, X, H = face
                S2, X2, H2 = partner
                g = gcd(S, S2)
                G = g * d
                R = H2 - S2
                assert R > 0 and X2 > 0

                # Exact physical gluing / third Pythagorean triple.
                assert G * G == S * S * H2 * H2 + X * X * S2 * S2
                assert G * G == H * H * S2 * S2 + S * S * X2 * X2
                assert (S * H2) ** 2 + (X * S2) ** 2 == G * G

                Np = H * G + S * S * H2 + X * X * S2
                Nm = H * G - S * S * H2 - X * X * S2
                assert Np > 0 and Nm > 0
                assert Np * Nm == S * S * X * X * R * R

                # Direct comparison with the already-merged Stage14-s3 map.
                P = physical_point(face, partner, d)
                Zp = P["Z"]
                assert Zp == Fraction(Np, R)
                assert Zp > S * S

                # Compact T0 translate and gap product.
                U = G - H * S2
                V = H * H2 - G
                assert U > 0 and V > 0
                assert U * (G + H * S2) == S * S * X2 * X2
                assert V * (H * H2 + G) == X * X * X2 * X2
                assert U * V == (H2 + S2) * Nm
                assert X2 * X2 == R * (H2 + S2)

                Zt = -Fraction(S * S * X * X, 1) / Zp
                assert Zt == -Fraction(Nm, R)
                assert Zt == -Fraction(U * V, X2 * X2)
                assert -X * X < Zt < 0

                DT2 = Zt.denominator
                DT = isqrt(DT2)
                assert DT * DT == DT2
                if DT > 1:
                    compact_d_gt_1 += 1
                assert DT2 == R // gcd(Nm, R)
                assert X2 * X2 // gcd(X2 * X2, U * V) == DT2
                assert X2 % DT == 0

                # Partner Euclid half-angle divisor and exact cofactor square.
                m2, n2, role, kappa, t = partner_euclid(S2, X2, H2)
                assert t % DT == 0
                k = t // DT
                cancel = gcd(Nm, R)
                assert cancel == kappa * k * k

                # Reduced compact packet and physical gap square-kernel identities.
                AT = Zt.numerator
                assert AT < 0
                G0 = AT
                G1 = AT - S * S * DT2
                G2 = AT + X * X * DT2
                assert G1 < 0 < G2

                e0, u0 = support_squarefree_kernel_and_root(-G0, 2 * S * X)
                e1, u1 = support_squarefree_kernel_and_root(-G1, 2 * S * H)
                e2, u2 = support_squarefree_kernel_and_root(G2, 2 * X * H)
                common = kappa * k * k
                assert Nm == common * e0 * u0 * u0
                assert H * U == common * e1 * u1 * u1
                assert H * V == common * e2 * u2 * u2
                assert e2 * u2 * u2 + e1 * u1 * u1 == H * H * DT2
                assert e2 * u2 * u2 + e0 * u0 * u0 == X * X * DT2

                # Good odd partner-leg prime root-sign law.
                for ell, e in factor_small(X2).items():
                    if ell == 2 or (H * S * X) % ell == 0:
                        continue
                    mod = ell ** (2 * e)
                    in_plus = (H2 + S2) % mod == 0
                    in_minus = (H2 - S2) % mod == 0
                    assert in_plus ^ in_minus
                    root_pos = (G - H * S2) % mod == 0
                    root_neg = (G + H * S2) % mod == 0
                    assert root_pos ^ root_neg
                    actual = vp(DT, ell)
                    if in_plus:
                        plus_checks += 1
                        expected = 0
                    elif root_neg:
                        minus_negative_checks += 1
                        expected = e
                    else:
                        minus_positive_checks += 1
                        expected = 0
                    assert actual == expected, (face, partner, d, ell, e, actual, expected)
                    root_checks += 1

    # At B=50,000 the frozen rank-jump graph has 62 raw pair edges and no triples.
    assert undirected == 62, undirected
    assert ordered == 124, ordered
    assert compact_d_gt_1 > 0
    assert root_checks > 0 and plus_checks > 0 and minus_negative_checks > 0 and minus_positive_checks > 0

    # Exact exponent ledger.
    assert Fraction(1, 2) - Fraction(10, 21) == Fraction(1, 42)
    assert Fraction(1, 2) + Fraction(10, 21) == Fraction(41, 42)

    text = RESULT.read_text()
    required = [
        "STAGE14_S6_06=COMPLETE_PHYSICAL_CONJUGATE_GAP_AND_HALF_ANGLE_DENOMINATOR_REDUCTION",
        "PHYSICAL_GLUE_THIRD_PYTHAGOREAN_IDENTITY=true",
        "TORSION_DENOMINATOR_SQUARE_DIVIDES_H2_MINUS_S2=true",
        "PARTNER_HALF_ANGLE_DIVISOR_D_T=true",
        "HALF_ANGLE_CANCELLATION_COFACTOR_EXACT=true",
        "COMPACT_GAP_SQUARE_KERNEL_FACTORIZATION=true",
        "GOOD_ODD_T0_ROOT_SIGN_LAW=true",
        "HALF_ANGLE_SIZE_ONLY_BEATS_CURRENT_BOUND=false",
        "FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false",
        "NEXT=Stage14-s6-07",
    ]
    for needle in required:
        assert needle in text, needle

    print("Stage14-s6-06 audit: success")
    print(f"undirected physical edges: {undirected}")
    print(f"ordered physical incidences: {ordered}")
    print(f"compact denominators >1: {compact_d_gt_1}")
    print(f"good odd root-sign checks: {root_checks}")
    print(f"  plus-factor automatic cancellation: {plus_checks}")
    print(f"  minus-factor positive-root cancellation: {minus_positive_checks}")
    print(f"  minus-factor negative-root denominator: {minus_negative_checks}")


if __name__ == "__main__":
    main()
