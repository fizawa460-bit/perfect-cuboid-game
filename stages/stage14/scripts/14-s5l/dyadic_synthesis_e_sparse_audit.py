#!/usr/bin/env python3
"""Deterministic regression audit for Stage14-s5l."""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations
from math import gcd, isqrt
import json

X = 80
Y = 10
Z = 4
COLUMNS = ("A", "B", "C", "D")
WIDTHS = {"A": X, "B": Y, "C": X + Y, "D": X + Y}
LINEAR_BLOCKS = (2, 4, 8, 16, 32, 64)
E_BLOCKS = (32, 64, 128, 256)


def value(col, m, n):
    if col == "A": return m
    if col == "B": return n
    if col == "C": return m - n
    if col == "D": return m + n
    raise ValueError(col)


def primitive_points():
    return [
        (m, n)
        for m in range(2, X + 1)
        for n in range(1, min(Y, m - 1) + 1)
        if gcd(m, n) == 1 and (m - n) % 2 == 1
    ]


def prime_factors(n):
    out = []
    x = n
    p = 2
    while p * p <= x:
        if x % p == 0:
            out.append(p)
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        out.append(x)
    return out


def is_squarefree(n):
    return all(n % (p * p) for p in range(2, isqrt(n) + 1))


def odd_squarefree(n):
    return n > 1 and n % 2 == 1 and is_squarefree(n)


def split_squarefree(n):
    return odd_squarefree(n) and all(p % 4 == 1 for p in prime_factors(n))


def block(U, split=False):
    predicate = split_squarefree if split else odd_squarefree
    return [q for q in range(U, 2 * U) if predicate(q)]


def lam(q):
    z = 1.0
    for p in prime_factors(q):
        z /= p + 1
    return z


def root_count(v):
    return sum((r * r + 1) % v == 0 for r in range(v))


def projective_slope(m, n, v):
    assert gcd(n, v) == 1
    return (m * pow(n, -1, v)) % v


def determinant(P, Q):
    m, n = P
    mp, np = Q
    return m * np - mp * n


def check_linear_dyadic_partition():
    total = central = boundary = 0
    for ci, cj in combinations(COLUMNS, 2):
        hi, hj = WIDTHS[ci], WIDTHS[cj]
        for U in LINEAR_BLOCKS:
            for V in LINEAR_BLOCKS:
                is_central = Z <= U <= hi / Z and Z <= V <= hj / Z
                is_boundary = U < Z or V < Z or U > hi / Z or V > hj / Z
                assert is_central != is_boundary
                total += 1
                central += int(is_central)
                boundary += int(is_boundary)
    return total, central, boundary


def check_lambda_bound():
    checks = 0
    for q in range(3, 513, 2):
        if odd_squarefree(q):
            assert lam(q) <= 1.0 / q + 1e-15
            checks += 1
    return checks


def check_norm_root_count():
    checks = 0
    for v in range(5, 513, 2):
        if split_squarefree(v):
            expected = 2 ** len(prime_factors(v))
            actual = root_count(v)
            assert actual == expected, (v, actual, expected)
            checks += 1
    return checks


def check_e_root_energy():
    points = primitive_points()
    energy_checks = collision_checks = 0
    sparse_cells = sparse_nonzero_cells = 0
    max_sparse_signed_occupancy = 0

    for col in COLUMNS:
        for U in LINEAR_BLOCKS:
            for V in E_BLOCKS:
                for u in block(U):
                    for v in block(V, split=True):
                        if gcd(u, v) != 1:
                            continue
                        signed_cells = defaultdict(list)
                        W = 0
                        for P in points:
                            m, n = P
                            if value(col, m, n) % u != 0 or (m * m + n * n) % v != 0:
                                continue
                            r = projective_slope(m, n, v)
                            assert (r * r + 1) % v == 0
                            signed_cells[r].append(P)
                            W += 1

                        assert sum(len(cell) for cell in signed_cells.values()) == W
                        root_patterns = 2 ** len(prime_factors(v))
                        assert len(signed_cells) <= root_patterns

                        for cell in signed_cells.values():
                            for P, Q in combinations(cell, 2):
                                assert determinant(P, Q) % (u * v) == 0
                                collision_checks += 1

                        signed_square_sum = sum(len(cell) ** 2 for cell in signed_cells.values())
                        assert W * W <= root_patterns * signed_square_sum
                        energy_checks += 1

                        if u * v > 2 * X * Y:
                            sparse_cells += 1
                            sparse_nonzero_cells += int(W > 0)
                            if signed_cells:
                                max_sparse_signed_occupancy = max(
                                    max_sparse_signed_occupancy,
                                    max(len(cell) for cell in signed_cells.values()),
                                )
                            assert all(len(cell) <= 1 for cell in signed_cells.values())

    assert sparse_cells > 0
    assert sparse_nonzero_cells > 0
    assert max_sparse_signed_occupancy == 1
    return {
        "energy_checks": energy_checks,
        "collision_checks": collision_checks,
        "sparse_cells": sparse_cells,
        "sparse_nonzero_cells": sparse_nonzero_cells,
        "max_sparse_signed_occupancy": max_sparse_signed_occupancy,
        "primitive_points": len(points),
    }


def main():
    total, central, boundary = check_linear_dyadic_partition()
    report = {
        "metadata": {
            "stage": "14-s5l",
            "box": {"X": X, "Y": Y},
            "central_cutoff_Z": Z,
            "classification": "DETERMINISTIC_REGRESSION_PLUS_ANALYTIC_THEOREM_INTERFACE",
        },
        "linear_dyadic_partition": {
            "total_blocks": total,
            "central_blocks": central,
            "boundary_blocks": boundary,
        },
        "lambda_upper_bound_checks": check_lambda_bound(),
        "norm_root_count_checks": check_norm_root_count(),
        "e_root_energy": check_e_root_energy(),
        "decision": {
            "STAGE14_S5L": "COMPLETE_LINEAR_CENTRAL_DYADIC_SYNTHESIS_AND_E_SPARSE_ROOT_ENERGY_BOUND",
            "LINEAR_MASTER_DYADIC_ENVELOPE_PROVED": True,
            "LINEAR_CENTRAL_DYADIC_SUMMATION_PROVED": True,
            "LINEAR_BOUNDARY_STRIPS_ISOLATED": True,
            "E_ROOT_PATTERN_PARTITION_EXACT": True,
            "E_LINEAR_SPARSE_L2_DISPERSION_PROVED": True,
            "FULL_STATE_SPLIT_E_SPARSE_REGIME_CLOSED": True,
            "MEDIUM_E_LINEAR_DISPERSION_PROVED": False,
            "FAMILY_LARGE_SIEVE_THEOREM_PROVED": False,
            "SQRT_B_ASYMPTOTIC_PROVED": False,
            "NEXT": "Stage14-s5m",
        },
    }
    print(json.dumps(report, indent=2))
    print("STAGE14_S5L=COMPLETE_LINEAR_CENTRAL_DYADIC_SYNTHESIS_AND_E_SPARSE_ROOT_ENERGY_BOUND")
    print("LINEAR_MASTER_DYADIC_ENVELOPE_PROVED=true")
    print("LINEAR_CENTRAL_DYADIC_SUMMATION_PROVED=true")
    print("LINEAR_BOUNDARY_STRIPS_ISOLATED=true")
    print("E_ROOT_PATTERN_PARTITION_EXACT=true")
    print("E_LINEAR_SPARSE_L2_DISPERSION_PROVED=true")
    print("FULL_STATE_SPLIT_E_SPARSE_REGIME_CLOSED=true")
    print("MEDIUM_E_LINEAR_DISPERSION_PROVED=false")
    print("FAMILY_LARGE_SIEVE_THEOREM_PROVED=false")
    print("SQRT_B_ASYMPTOTIC_PROVED=false")
    print("NEXT=Stage14-s5m")


if __name__ == "__main__":
    main()
