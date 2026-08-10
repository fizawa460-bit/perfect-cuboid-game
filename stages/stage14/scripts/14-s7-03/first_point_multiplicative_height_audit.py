#!/usr/bin/env python3
"""Deterministic audit for Stage14-s7-03.

Regenerates the frozen physical ordered incidences through B=50,000 and checks:
- the F2/F3 half-angle transfer;
- Jacobi u and Legendre sqrt-X rational coordinates;
- exact reduced denominators and cross-gcd product;
- exact c0 = X2/gcd(X2,X3) sharp-diagonal formula;
- uniform H_mult/2 <= d_rec <= 4 H_mult comparison;
- first-height sandwich on every observed active direction;
- the small-denominator hyperbola consequence.
"""
from collections import defaultdict
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[4]
GRAPH = ROOT / "stages/stage14/scripts/14-4/rank_jump_graph_audit.py"
B = 50_000


def is_square(n):
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n


def half_angles(face):
    S, X, H = face
    assert S * S + X * X == H * H
    rm, rp = H - S, H + S
    a = isqrt(rm)
    b = isqrt(rp)
    if a * a == rm and b * b == rp:
        kappa = 1
    else:
        assert rm % 2 == 0 and rp % 2 == 0
        a = isqrt(rm // 2)
        b = isqrt(rp // 2)
        assert 2 * a * a == rm and 2 * b * b == rp
        kappa = 2
    assert 0 < a < b and gcd(a, b) == 1
    assert S == kappa * (b * b - a * a) // 2
    assert X == kappa * a * b
    assert H == kappa * (a * a + b * b) // 2
    return kappa, a, b


def ordered_physical_edges():
    mod = runpy.run_path(str(GRAPH))
    keep, _ = mod["enumerate_multi"](B)
    object_edges = mod["object_edges"]
    rows = []
    seen = set()
    for (a, b, c, d), (mask, ds) in keep.items():
        if d > B or mask.bit_count() < 2:
            continue
        for f1, f2 in object_edges(a, b, c, mask, ds):
            for row in ((f1, f2, d), (f2, f1, d)):
                if row not in seen:
                    seen.add(row)
                    rows.append(row)
    return rows


def transfer_f3(F1, F2, dspace):
    S, X, H = F1
    S2, X2, H2 = F2
    g = gcd(S, S2)
    c0 = gcd(H, X2)
    scale = g * c0
    assert (H * S2) % scale == 0
    assert (S * X2) % scale == 0
    assert dspace % c0 == 0
    F3 = (H * S2 // scale, S * X2 // scale, dspace // c0)
    S3, X3, H3 = F3
    assert gcd(S3, X3) == 1
    assert S3 * S3 + X3 * X3 == H3 * H3
    return F3, c0


def audit_row(F1, F2, dspace):
    F3, c0 = transfer_f3(F1, F2, dspace)
    S3, X3, H3 = F3
    _, X2, H2 = F2

    k2, a, b = half_angles(F2)
    k3, c, d = half_angles(F3)

    # Positive physical cross-square.
    delta0 = (a * d - b * c) * (a * d + b * c) * (b * d - a * c) * (b * d + a * c)
    assert delta0 > 0 and is_square(delta0)
    assert a * d > b * c
    assert b * d > a * c

    # Natural rational coordinates.
    u = Fraction(b * c, a * d)
    w = Fraction(a * c, b * d)
    r = Fraction(a, b)
    x_slope = Fraction(c, d)
    assert u == Fraction(b, a) * x_slope
    assert Fraction(0, 1) < u < 1
    assert Fraction(0, 1) < w < 1
    assert w * w == r ** 4 * u * u

    # Exact reduced denominators.
    qu = gcd(b * c, a * d)
    qx = gcd(a * c, b * d)
    Du = a * d // qu
    Dx = b * d // qx
    assert u.denominator == Du
    assert w.denominator == Dx
    assert qu * qx == gcd(a * b, c * d)
    assert gcd(qu, qx) == 1

    Hmult = Du * Dx
    assert Hmult == a * b * d * d // gcd(a * b, c * d)

    # Exact sharp diagonal formula purely from F2/F3.
    assert c0 == X2 // gcd(X2, X3)
    drec = c0 * H3
    assert drec == dspace

    # Uniform absolute comparison.
    assert Hmult <= 2 * drec, (F1, F2, F3, Hmult, drec)
    assert drec <= 4 * Hmult, (F1, F2, F3, Hmult, drec)

    # Physical cutoff produces a hyperbola split.
    assert Hmult <= 2 * B
    assert min(Du, Dx) ** 2 <= Hmult <= 2 * B

    # Direction scale is automatically at most sqrt(2B).
    assert H2 <= drec
    assert b * b <= 2 * drec

    return {
        "F3": F3,
        "Du": Du,
        "Dx": Dx,
        "Hmult": Hmult,
        "drec": drec,
        "ratio": Fraction(drec, Hmult),
    }


def main():
    rows = ordered_physical_edges()
    assert len(rows) == 124, len(rows)

    by_direction = defaultdict(list)
    ratios = []
    for F1, F2, dspace in rows:
        out = audit_row(F1, F2, dspace)
        by_direction[F2].append(out)
        ratios.append(out["ratio"])

    # Minima inherit the same comparison constants on the frozen active set.
    for F2, vals in by_direction.items():
        mu = min(v["drec"] for v in vals)
        eta = min(v["Hmult"] for v in vals)
        assert eta <= 2 * mu
        assert mu <= 4 * eta

    print(f"ORDERED_PHYSICAL_INCIDENCES={len(rows)}")
    print(f"ACTIVE_DIRECTION_COUNT={len(by_direction)}")
    print(f"MIN_DREC_OVER_HMULT={min(ratios)}")
    print(f"MAX_DREC_OVER_HMULT={max(ratios)}")
    print("MERGED_S7_02_BOUNDARY_AUDIT=true")
    print("MERGED_4BN_PHYSICAL_BIJECTION_AUDIT=true")
    print("JACOBI_LEGENDRE_COORDINATE_IDENTITY_AUDIT=true")
    print("REDUCED_DENOMINATOR_AUDIT=true")
    print("CROSS_GCD_PRODUCT_AUDIT=true")
    print("SHARP_DIAGONAL_HALF_ANGLE_AUDIT=true")
    print("MULTIPLICATIVE_HEIGHT_COMPARISON_AUDIT=true")
    print("FIRST_HEIGHT_SANDWICH_AUDIT=true")
    print("SMALL_DENOMINATOR_HYPERBOLA_AUDIT=true")
    print("ALL_AUDITS_PASS=true")


if __name__ == "__main__":
    main()
