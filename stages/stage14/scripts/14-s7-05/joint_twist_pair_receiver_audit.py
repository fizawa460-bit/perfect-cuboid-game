#!/usr/bin/env python3
"""Deterministic audit for Stage14-s7-05.

Checks:
- merged s7-04 physical reduced-coordinate receiver on the frozen B=50,000 graph;
- canonical squareclass labels xi=ker(PQ), k=ker(Q^2-P^2);
- exact representation u=xi*z^2 and 1-u^2=k*y^2;
- equality of (k,xi) for both physical coordinates;
- inverse reconstruction r=z2/z1 and x=xi*z1*z2;
- binary-quartic invariants and exact j=1728 Jacobian coefficient;
- finite rational-grid collision atlas for the same-twist label;
- exact current exponent thresholds 1/21 and 2/21.
"""
from collections import defaultdict
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[4]
S703 = ROOT / "stages/stage14/scripts/14-s7-03/first_point_multiplicative_height_audit.py"
B = 50_000
GRID_DEN = 120


def is_square(n):
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n


def squarefree_kernel(n):
    assert n > 0
    out = 1
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e & 1:
            out *= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out *= n
    return out


def canonical_label(fr):
    assert 0 < fr < 1
    P, Q = fr.numerator, fr.denominator
    assert gcd(P, Q) == 1

    xi = squarefree_kernel(P * Q)
    h2 = P * Q // xi
    assert is_square(h2)
    h = isqrt(h2)
    z = Fraction(h, Q)
    assert xi * z * z == fr

    gap = Q * Q - P * P
    k = squarefree_kernel(gap)
    a2 = gap // k
    assert is_square(a2)
    A = isqrt(a2)
    y = Fraction(A, Q)
    assert 1 - fr * fr == k * y * y
    assert k * y * y == 1 - xi * xi * z ** 4

    return {
        "P": P,
        "Q": Q,
        "xi": xi,
        "k": k,
        "z": z,
        "y": y,
    }


def binary_quartic_jacobian_audit(k, xi):
    # F(Z,T) = a4 Z^4 + a0 T^4 = -k xi^2 Z^4 + k T^4.
    a4 = -k * xi * xi
    a3 = a2 = a1 = 0
    a0 = k
    I = 12 * a4 * a0 - 3 * a3 * a1 + a2 * a2
    J = (
        72 * a4 * a2 * a0
        + 9 * a3 * a2 * a1
        - 27 * a0 * a3 * a3
        - 27 * a4 * a1 * a1
        - 2 * a2 * a2 * a2
    )
    assert I == -12 * k * k * xi * xi
    assert J == 0
    A = -I // 3
    Bc = -J // 27
    n = k * xi
    assert A == 4 * n * n
    assert Bc == 0
    # j=1728 follows because J=0 and I != 0 for this nonsingular quartic.
    assert I != 0
    return n, A


def physical_rows():
    mod = runpy.run_path(str(S703))
    rows = mod["ordered_physical_edges"]()
    assert len(rows) == 124, len(rows)
    return mod, rows


def audit_physical_receiver():
    mod, rows = physical_rows()
    half_angles = mod["half_angles"]
    transfer_f3 = mod["transfer_f3"]

    labels = defaultdict(int)
    jacobian_products = defaultdict(set)
    for F1, F2, dspace in rows:
        F3, _ = transfer_f3(F1, F2, dspace)
        _, a, b = half_angles(F2)
        _, c, d = half_angles(F3)

        u = Fraction(b * c, a * d)
        w = Fraction(a * c, b * d)
        assert 0 < w < u < 1

        lu = canonical_label(u)
        lw = canonical_label(w)
        assert lu["xi"] == lw["xi"]
        assert lu["k"] == lw["k"]
        xi, k = lu["xi"], lu["k"]

        # Product-square and same-difference-kernel conditions.
        assert squarefree_kernel(lu["P"] * lu["Q"]) == squarefree_kernel(lw["P"] * lw["Q"])
        assert squarefree_kernel(lu["Q"] ** 2 - lu["P"] ** 2) == squarefree_kernel(lw["Q"] ** 2 - lw["P"] ** 2)
        ratio = w / u
        prod = w * u
        assert is_square(ratio.numerator) and is_square(ratio.denominator)
        assert is_square(prod.numerator) and is_square(prod.denominator)

        # Exact inverse from the two same-twist points.
        r = lw["z"] / lu["z"]
        x = xi * lu["z"] * lw["z"]
        assert r == Fraction(a, b)
        assert x == Fraction(c, d)

        # The Jacobi cross-square is automatic from the shared k label.
        cross = (1 - u * u) * (1 - w * w)
        assert is_square(cross.numerator) and is_square(cross.denominator)
        assert cross == (k * lu["y"] * lw["y"]) ** 2

        # s7-03 height receiver remains exact.
        Hmult = lu["Q"] * lw["Q"]
        assert Hmult <= 2 * B
        assert Hmult <= 2 * dspace
        assert dspace <= 4 * Hmult

        n, jacA = binary_quartic_jacobian_audit(k, xi)
        assert jacA == 4 * n * n
        labels[(k, xi)] += 1
        jacobian_products[n].add((k, xi))

    return rows, labels, jacobian_products


def audit_grid_collisions():
    groups = defaultdict(list)
    total = 0
    for Q in range(2, GRID_DEN + 1):
        for P in range(1, Q):
            if gcd(P, Q) != 1:
                continue
            fr = Fraction(P, Q)
            lab = canonical_label(fr)
            binary_quartic_jacobian_audit(lab["k"], lab["xi"])
            groups[(lab["k"], lab["xi"])].append(fr)
            total += 1

    offdiag = 0
    collision_labels = 0
    max_mult = 0
    for (k, xi), vals in groups.items():
        vals = sorted(set(vals))
        max_mult = max(max_mult, len(vals))
        if len(vals) >= 2:
            collision_labels += 1
        for i in range(len(vals)):
            for j in range(i):
                u, w = vals[i], vals[j]
                if w > u:
                    u, w = w, u
                lu, lw = canonical_label(u), canonical_label(w)
                assert (lu["k"], lu["xi"]) == (k, xi)
                assert (lw["k"], lw["xi"]) == (k, xi)
                # Same label implies both original joint receiver conditions.
                assert is_square((u * w).numerator) and is_square((u * w).denominator)
                cross = (1 - u * u) * (1 - w * w)
                assert is_square(cross.numerator) and is_square(cross.denominator)
                # Exact rational inverse.
                r = lw["z"] / lu["z"]
                x = xi * lu["z"] * lw["z"]
                assert r > 0 and x > 0
                assert r * r == w / u
                assert x * x == w * u
                offdiag += 2

    assert collision_labels > 0
    assert offdiag > 0
    return total, len(groups), collision_labels, max_mult, offdiag


def exponent_ledger():
    current = Fraction(20, 21)
    direct_required = Fraction(1, 1) - current
    squared_required = 2 * direct_required
    assert direct_required == Fraction(1, 21)
    assert squared_required == Fraction(2, 21)
    return current, direct_required, squared_required


def main():
    rows, labels, jac_products = audit_physical_receiver()
    total, classes, collision_labels, max_mult, offdiag = audit_grid_collisions()
    current, direct_required, squared_required = exponent_ledger()

    print(f"ORDERED_PHYSICAL_INCIDENCES={len(rows)}")
    print(f"PHYSICAL_TWIST_LABEL_COUNT={len(labels)}")
    print(f"PHYSICAL_JACOBIAN_N_COUNT={len(jac_products)}")
    print(f"GRID_REDUCED_COORDINATES={total}")
    print(f"GRID_TWIST_LABELS={classes}")
    print(f"GRID_COLLISION_LABELS={collision_labels}")
    print(f"GRID_MAX_TWIST_MULTIPLICITY={max_mult}")
    print(f"GRID_ORDERED_OFFDIAGONAL_COLLISIONS={offdiag}")
    print(f"CURRENT_WHOLE_FAMILY_EXPONENT={current}")
    print(f"DIRECT_TWIST_SAVING_REQUIRED={direct_required}")
    print(f"SQUARED_ENERGY_SAVING_REQUIRED={squared_required}")
    print("CANONICAL_XI_K_LABEL_AUDIT=true")
    print("SAME_TWIST_TWO_POINT_RECEIVER_AUDIT=true")
    print("TWIST_INVERSE_R_X_RECONSTRUCTION_AUDIT=true")
    print("PHYSICAL_OFFDIAGONAL_AUDIT=true")
    print("BINARY_QUARTIC_J_ZERO_AUDIT=true")
    print("J1728_JACOBIAN_COEFFICIENT_AUDIT=true")
    print("JACOBIAN_DEPENDS_ON_K_TIMES_XI_AUDIT=true")
    print("FINITE_TWIST_COLLISION_ATLAS_AUDIT=true")
    print("MERGED_4BR_EXPONENT_LEDGER_AUDIT=true")
    print("ALL_AUDITS_PASS=true")


if __name__ == "__main__":
    main()
