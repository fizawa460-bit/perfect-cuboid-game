#!/usr/bin/env python3
"""Deterministic audit for Stage14-s7-04.

Checks on the frozen physical ordered incidences:
- the four cross-gcd cell factorization and exact D_u/D_x formulas;
- fixed-u and fixed-w genus-one quartic identities;
- the exact joint reduced-coordinate receiver;
- same-squarefree-kernel collision of the two difference-of-squares;
- Farey projection-space O(L^2) counting;
- exact hyperbola-split exponent ceiling 1;
- merged 4bq 61/63 baseline is present and strictly below that ceiling.
"""
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[4]
S703 = ROOT / "stages/stage14/scripts/14-s7-03/first_point_multiplicative_height_audit.py"
R4BQ = ROOT / "stages/stage14/14-4bq/result.md"


def is_square_int(n):
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n


def is_square_fraction(x):
    x = Fraction(x)
    return x >= 0 and is_square_int(x.numerator) and is_square_int(x.denominator)


def squarefree_kernel(n):
    assert n > 0
    out = 1
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e ^= 1
        if e:
            out *= p
        p += 1 if p == 2 else 2
    if n > 1:
        out *= n
    return out


def cross_cells(a, b, c, d):
    qac = gcd(a, c)
    qad = gcd(a, d)
    qbc = gcd(b, c)
    qbd = gcd(b, d)
    qs = (qac, qad, qbc, qbd)
    for i in range(4):
        for j in range(i + 1, 4):
            assert gcd(qs[i], qs[j]) == 1
    assert a % (qac * qad) == 0
    assert b % (qbc * qbd) == 0
    assert c % (qac * qbc) == 0
    assert d % (qad * qbd) == 0
    a0 = a // (qac * qad)
    b0 = b // (qbc * qbd)
    c0 = c // (qac * qbc)
    d0 = d // (qad * qbd)
    return qac, qad, qbc, qbd, a0, b0, c0, d0


def audit_physical_rows():
    mod = runpy.run_path(str(S703))
    rows = mod["ordered_physical_edges"]()
    audit_row = mod["audit_row"]
    half_angles = mod["half_angles"]
    assert len(rows) == 124

    fixed_u_checks = 0
    fixed_w_checks = 0
    joint_checks = 0
    kernel_checks = 0
    cell_checks = 0

    for F1, F2, dspace in rows:
        out = audit_row(F1, F2, dspace)
        F3 = out["F3"]
        _, a, b = half_angles(F2)
        _, c, d = half_angles(F3)

        u = Fraction(b * c, a * d)
        w = Fraction(a * c, b * d)
        P, Q = u.numerator, u.denominator
        R, S = w.numerator, w.denominator

        assert Q == out["Du"]
        assert S == out["Dx"]
        assert 0 < w < u < 1
        assert Q * S == out["Hmult"]

        # Cross-gcd cell decomposition and exact denominator formulas.
        qac, qad, qbc, qbd, a0, b0, c0, d0 = cross_cells(a, b, c, d)
        assert gcd(b * c, a * d) == qac * qbd
        assert gcd(a * c, b * d) == qad * qbc
        assert Q == qad * qad * a0 * d0
        assert S == qbd * qbd * b0 * d0
        cell_checks += 1

        # Fixed-u genus-one quartic identity.
        fixed_u_rhs = (Q * Q - P * P) * (Q * Q * b**4 - P * P * a**4)
        assert fixed_u_rhs > 0 and is_square_int(fixed_u_rhs)
        fixed_u_checks += 1

        # Fixed-w symmetric genus-one quartic identity.
        fixed_w_rhs = (S * S - R * R) * (S * S * a**4 - R * R * b**4)
        assert fixed_w_rhs > 0 and is_square_int(fixed_w_rhs)
        fixed_w_checks += 1

        # Joint receiver: one rational-square condition recovers both slopes.
        uw = Fraction(P * R, Q * S)
        w_over_u = Fraction(R * Q, S * P)
        assert is_square_fraction(uw)
        assert is_square_fraction(w_over_u)
        assert w_over_u / uw == Fraction(Q * Q, P * P)
        assert uw == Fraction(c * c, d * d)
        assert w_over_u == Fraction(a * a, b * b)

        # Remaining Jacobi condition is a same-kernel difference-of-squares collision.
        A = Q * Q - P * P
        C = S * S - R * R
        assert A > 0 and C > 0
        assert is_square_int(A * C)
        assert squarefree_kernel(A) == squarefree_kernel(C)
        joint_checks += 1
        kernel_checks += 1

    return {
        "rows": len(rows),
        "cell": cell_checks,
        "fixed_u": fixed_u_checks,
        "fixed_w": fixed_w_checks,
        "joint": joint_checks,
        "kernel": kernel_checks,
    }


def farey_projection_audit(L=128):
    # Number of reduced p/q in (0,1) with q<=L is sum phi(q), and is < L^2.
    count = 0
    for q in range(2, L + 1):
        for p in range(1, q):
            if gcd(p, q) == 1:
                count += 1
    assert count < L * L
    return count


def exponent_ledger_audit():
    # For L=B^alpha, the separate projection route gives
    # max(2alpha, 2-2alpha), minimized exactly at alpha=1/2 with value 1.
    half = Fraction(1, 2)
    at_half = max(2 * half, 2 - 2 * half)
    assert at_half == 1

    # Exact rational grid check of the minimum.
    best = None
    best_alpha = None
    for k in range(0, 127):
        alpha = Fraction(k, 126)
        val = max(2 * alpha, 2 - 2 * alpha)
        if best is None or val < best:
            best = val
            best_alpha = alpha
    assert best == 1 and best_alpha == half

    baseline = Fraction(61, 63)
    assert baseline < 1
    return best_alpha, best, baseline


def merged_4bq_boundary_audit():
    text = R4BQ.read_text()
    assert "STAGE14_4BQ=DIAGONAL_PAIR_GENUS_ONE_CLOSURE_AND_FIRST_FULL_POST_LOCAL_SAVING" in text
    assert "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=61/63" in text
    assert "FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=true" in text
    return True


def main():
    stats = audit_physical_rows()
    farey_count = farey_projection_audit()
    alpha, exponent, baseline = exponent_ledger_audit()
    assert merged_4bq_boundary_audit()

    print(f"ORDERED_PHYSICAL_INCIDENCES={stats['rows']}")
    print(f"CROSS_CELL_DENOMINATOR_IDENTITY_CHECKS={stats['cell']}")
    print(f"FIXED_U_QUARTIC_CHECKS={stats['fixed_u']}")
    print(f"FIXED_W_QUARTIC_CHECKS={stats['fixed_w']}")
    print(f"JOINT_RECEIVER_CHECKS={stats['joint']}")
    print(f"SAME_KERNEL_CHECKS={stats['kernel']}")
    print(f"FAREY_REDUCED_COORDINATES_DENOM_LE_128={farey_count}")
    print(f"SEPARATE_PROJECTION_OPTIMAL_ALPHA={alpha}")
    print(f"SEPARATE_PROJECTION_OPTIMAL_EXPONENT={exponent}")
    print(f"MERGED_4BQ_BASELINE={baseline}")
    print("S7_03_PREDECESSOR_AUDIT=true")
    print("CROSS_GCD_DENOMINATOR_FACTORIZATION_AUDIT=true")
    print("FIXED_U_GENUS_ONE_IDENTITY_AUDIT=true")
    print("FIXED_W_GENUS_ONE_IDENTITY_AUDIT=true")
    print("FAREY_L2_PROJECTION_SPACE_AUDIT=true")
    print("SEPARATE_PROJECTION_HYPERBOLA_CEILING_AUDIT=true")
    print("JOINT_REDUCED_COORDINATE_RECEIVER_AUDIT=true")
    print("JOINT_SAME_SQUAREFREE_KERNEL_AUDIT=true")
    print("MERGED_4BQ_BOUNDARY_AUDIT=true")
    print("ALL_AUDITS_PASS=true")


if __name__ == "__main__":
    main()
