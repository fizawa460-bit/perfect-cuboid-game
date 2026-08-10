#!/usr/bin/env python3
"""Deterministic regression audit for Stage14-s7-22.

This checks the exact finite-index / tangent algebra used by the stage.
It is not a proof by finite search of the asymptotic theorem boundary.
"""

from fractions import Fraction
from math import gcd


def gcd_many(values):
    g = 0
    for v in values:
        g = gcd(g, abs(v))
    return g


def det_matrix(mat):
    a = [[Fraction(x) for x in row] for row in mat]
    n = len(a)
    out = Fraction(1)
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            out = -out
        pv = a[col][col]
        out *= pv
        for j in range(col, n):
            a[col][j] /= pv
        for r in range(col + 1, n):
            f = a[r][col]
            if not f:
                continue
            for j in range(col, n):
                a[r][j] -= f * a[col][j]
    return out


def matrix_rank(mat):
    if not mat:
        return 0
    a = [[Fraction(x) for x in row] for row in mat]
    rows, cols = len(a), len(a[0])
    rank = 0
    col = 0
    while rank < rows and col < cols:
        pivot = next((r for r in range(rank, rows) if a[r][col]), None)
        if pivot is None:
            col += 1
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        pv = a[rank][col]
        for j in range(col, cols):
            a[rank][j] /= pv
        for r in range(rows):
            if r == rank:
                continue
            f = a[r][col]
            if not f:
                continue
            for j in range(col, cols):
                a[r][j] -= f * a[rank][j]
        rank += 1
        col += 1
    return rank


def hyperplane_basis(c):
    """Return four-dimensional integer vectors spanning c dot x = 0."""
    pivot = next(i for i, x in enumerate(c) if x)
    cp = c[pivot]
    basis = []
    for i in range(4):
        if i == pivot:
            continue
        v = [0, 0, 0, 0]
        v[i] = cp
        v[pivot] = -c[i]
        basis.append(v)
    return basis


def restriction_rank(A, B, c):
    # Symmetric matrix N with X^T N X = 2(A*x1*y1-B*x2*y2).
    N = [
        [0, A, 0, 0],
        [A, 0, 0, 0],
        [0, 0, 0, -B],
        [0, 0, -B, 0],
    ]
    basis = hyperplane_basis(c)
    # R_ij = b_i^T N b_j.
    R = []
    for u in basis:
        row = []
        for v in basis:
            Nv = [sum(N[i][j] * v[j] for j in range(4)) for i in range(4)]
            row.append(sum(u[i] * Nv[i] for i in range(4)))
        R.append(row)
    return matrix_rank(R)


def audit_tangent_criterion():
    checked = 0
    tangent = 0
    nontangent = 0
    for A in range(1, 5):
        for B in range(1, 5):
            for c1 in range(-3, 4):
                for c2 in range(-3, 4):
                    for c3 in range(-3, 4):
                        for c4 in range(-3, 4):
                            c = (c1, c2, c3, c4)
                            if c == (0, 0, 0, 0) or gcd_many(c) != 1:
                                continue
                            is_tangent = B * c1 * c2 == A * c3 * c4
                            rank = restriction_rank(A, B, c)
                            if is_tangent:
                                assert rank == 2
                                tangent += 1
                            else:
                                assert rank == 3
                                nontangent += 1
                            checked += 1
    assert tangent > 0 and nontangent > 0
    return checked, tangent, nontangent


def multiplicative_energy_bruteforce(M):
    count = 0
    for a in range(1, M + 1):
        for b in range(1, M + 1):
            for c in range(1, M + 1):
                ab = a * b
                if ab % c:
                    continue
                d = ab // c
                if 1 <= d <= M:
                    count += 1
    return count


def multiplicative_energy_param(M):
    # Exact gcd parameterization:
    # a=h*r, c=h*s, gcd(r,s)=1, b=s*t, d=r*t.
    total = 0
    for r in range(1, M + 1):
        for s in range(1, M + 1):
            if gcd(r, s) != 1:
                continue
            q = M // max(r, s)
            total += q * q
    return total


def audit_saturation_identity():
    # A sharp model for the general hyperplane formula.
    # Lambda has basis columns
    # (a,0,0,0), (0,b,0,0), (0,0,c,0), (p,q,r,d).
    # The primitive normal to the first three columns is e4.
    examples = [
        (2, 3, 5, 7, 1, 4, 2),
        (3, 4, 5, 101, 2, 1, 9),
        (5, 7, 11, 1009, 8, 3, 4),
    ]
    for a, b, c, d, p, q, r in examples:
        basis = [
            [a, 0, 0, p],
            [0, b, 0, q],
            [0, 0, c, r],
            [0, 0, 0, d],
        ]
        # Rows above are the transpose of the column-basis matrix; determinant same.
        Delta = abs(det_matrix(basis))
        assert Delta == a * b * c * d
        normal = (0, 0, 0, 1)
        dot_values = [0, 0, 0, d]
        d_H = gcd_many(dot_values)
        assert d_H == d
        covol_H = a * b * c
        # ||normal||_2=1 in this model.
        assert Fraction(Delta, d_H) == covol_H
        assert Delta % d_H == 0
        assert Delta // d_H == covol_H


def audit_exponent_ledger():
    xi = Fraction(3, 4)
    L = Fraction(1, 16)
    Delta = 2 * xi
    normal_height = 3 * L
    saturation = Delta - 3 * L
    defect = 3 * L
    cell_min = Fraction(1, 8)
    cell_square_min = 2 * cell_min
    cell_order_min = cell_square_min - defect
    tangent_normal = 6 * L
    raw_normal = 12 * L

    assert Delta == Fraction(3, 2)
    assert normal_height == Fraction(3, 16)
    assert saturation == Fraction(21, 16)
    assert defect == Fraction(3, 16)
    assert cell_order_min == Fraction(1, 16)
    assert tangent_normal == Fraction(3, 8)
    assert raw_normal == Fraction(3, 4)
    assert raw_normal - tangent_normal == Fraction(3, 8)


def main():
    audit_saturation_identity()
    checked, tangent, nontangent = audit_tangent_criterion()

    M = 18
    brute = multiplicative_energy_bruteforce(M)
    param = multiplicative_energy_param(M)
    assert brute == param

    audit_exponent_ledger()

    print("Stage14-s7-22 audit: PASS")
    print(f"tangent criterion hyperplanes checked: {checked}")
    print(f"tangent / non-tangent: {tangent} / {nontangent}")
    print(f"multiplicative energy M={M}: {brute}")
    print("rank3 normal height exponent <= 3/16")
    print("rank3 saturation exponent >= 21/16")
    print("rank3 dual defect exponent <= 3/16")
    print("each balanced cell dual component exponent >= 1/16")
    print("fixed-ratio tangent normal exponent <= 3/8")


if __name__ == "__main__":
    main()
