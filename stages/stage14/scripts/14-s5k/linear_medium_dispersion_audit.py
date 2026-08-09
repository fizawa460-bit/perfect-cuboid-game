#!/usr/bin/env python3
"""Deterministic regression audit for Stage14-s5k.

The theorem in result.md is analytic. This script checks the exact algebraic
interfaces used by that proof and records finite discrepancy ledgers.
"""

from __future__ import annotations

from itertools import combinations
from math import gcd, pi
import json

X = 80
Y = 50
PRIMES = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43)
COLUMNS = ("A", "B", "C", "D")
MATRICES = {
    "A": (1, 0),
    "B": (0, 1),
    "C": (1, -1),
    "D": (1, 1),
}
WIDTHS = {
    "A": X,
    "B": Y,
    "C": X + Y,
    "D": X + Y,
}
DYADIC_BASES = (4, 8, 16)


def det2(a, b):
    return a[0] * b[1] - a[1] * b[0]


def value(col, m, n):
    a, b = MATRICES[col]
    return a * m + b * n


def opposite_parity(m, n):
    return (m - n) & 1


def primitive_points():
    return [
        (m, n)
        for m in range(1, X + 1)
        for n in range(1, Y + 1)
        if opposite_parity(m, n) and gcd(m, n) == 1
    ]


def all_opposite_points():
    return [
        (m, n)
        for m in range(1, X + 1)
        for n in range(1, Y + 1)
        if opposite_parity(m, n)
    ]


def mobius(n):
    if n == 1:
        return 1
    x = n
    mu = 1
    p = 2
    while p * p <= x:
        if x % p == 0:
            x //= p
            mu = -mu
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        mu = -mu
    return mu


def is_squarefree(n):
    p = 2
    x = n
    while p * p <= x:
        if x % (p * p) == 0:
            return False
        p += 1
    return True


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


def lam(q):
    z = 1.0
    for p in prime_factors(q):
        z /= p + 1
    return z


def odd_squarefree_in_block(U):
    return [
        q for q in range(U, 2 * U)
        if q > 1 and q % 2 == 1 and is_squarefree(q)
    ]


def direct_count(points, ci, cj, u, v):
    return sum(
        1
        for m, n in points
        if value(ci, m, n) % u == 0 and value(cj, m, n) % v == 0
    )


def finite_mobius_count(points, ci, cj, u, v):
    max_d = 2 * (X + Y)
    total = 0
    for d in range(1, max_d + 1, 2):
        mu = mobius(d)
        if mu == 0:
            continue
        cnt = 0
        for m, n in points:
            xi = value(ci, m, n)
            xj = value(cj, m, n)
            if xi % u == 0 and xj % v == 0 and xi % d == 0 and xj % d == 0:
                cnt += 1
        total += mu * cnt
    return total


def check_coordinate_algebra():
    dets = {}
    gcd_checks = 0
    for ci, cj in combinations(COLUMNS, 2):
        delta = det2(MATRICES[ci], MATRICES[cj])
        assert abs(delta) in (1, 2)
        dets[f"{ci}{cj}"] = delta
        for m in range(1, 45):
            for n in range(1, 35):
                if not opposite_parity(m, n):
                    continue
                g0 = gcd(m, n)
                g1 = gcd(abs(value(ci, m, n)), abs(value(cj, m, n)))
                assert g0 == g1, (ci, cj, m, n, g0, g1)
                gcd_checks += 1
    return dets, gcd_checks


def check_local_factors():
    checks = 0
    pair_exclusions = 0
    for p in PRIMES:
        nonzero = p * p - 1
        for c in COLUMNS:
            roots = 0
            for m in range(p):
                for n in range(p):
                    if m == 0 and n == 0:
                        continue
                    roots += value(c, m, n) % p == 0
            assert roots == p - 1, (p, c, roots)
            assert abs(roots / nonzero - 1 / (p + 1)) < 1e-15
            checks += 1
        for ci, cj in combinations(COLUMNS, 2):
            both = 0
            for m in range(p):
                for n in range(p):
                    if m == 0 and n == 0:
                        continue
                    both += value(ci, m, n) % p == 0 and value(cj, m, n) % p == 0
            assert both == 0, (p, ci, cj, both)
            pair_exclusions += 1
    return checks, pair_exclusions


def check_mobius_identity():
    prim = primitive_points()
    opp = all_opposite_points()
    samples = ((3, 5), (3, 7), (5, 7), (3, 11), (7, 13))
    checks = 0
    for ci, cj in combinations(COLUMNS, 2):
        for u, v in samples:
            if gcd(u, v) != 1:
                continue
            direct = direct_count(prim, ci, cj, u, v)
            inverted = finite_mobius_count(opp, ci, cj, u, v)
            assert direct == inverted, (ci, cj, u, v, direct, inverted)
            checks += 1
    return checks


def discrepancy_ledgers():
    prim = primitive_points()
    area = X * Y
    ledgers = []
    max_ratio = 0.0
    for ci, cj in combinations(COLUMNS, 2):
        hi = WIDTHS[ci]
        hj = WIDTHS[cj]
        for U in DYADIC_BASES:
            for V in DYADIC_BASES:
                us = odd_squarefree_in_block(U)
                vs = odd_squarefree_in_block(V)
                l2 = 0.0
                cells = 0
                for u in us:
                    for v in vs:
                        if gcd(u, v) != 1:
                            continue
                        w = direct_count(prim, ci, cj, u, v)
                        main = (4.0 / (pi * pi)) * area * lam(u) * lam(v)
                        delta = w - main
                        l2 += delta * delta
                        cells += 1
                envelope = U * V + hi * hi * V / U + hj * hj * U / V
                ratio = l2 / envelope if envelope else 0.0
                max_ratio = max(max_ratio, ratio)
                ledgers.append({
                    "edge": ci + cj,
                    "U": U,
                    "V": V,
                    "cells": cells,
                    "l2": l2,
                    "envelope": envelope,
                    "ratio": ratio,
                })
    assert max_ratio < 20.0, max_ratio
    return ledgers, max_ratio, len(prim)


def main():
    dets, gcd_checks = check_coordinate_algebra()
    local_checks, pair_exclusions = check_local_factors()
    mobius_checks = check_mobius_identity()
    ledgers, max_ratio, primitive_count = discrepancy_ledgers()
    report = {
        "metadata": {
            "stage": "14-s5k",
            "box": {"X": X, "Y": Y},
            "classification": "DETERMINISTIC_REGRESSION_PLUS_ANALYTIC_THEOREM_INTERFACE",
        },
        "coordinate_determinants": dets,
        "odd_gcd_preservation_checks": gcd_checks,
        "local_factor_checks": local_checks,
        "distinct_root_exclusion_checks": pair_exclusions,
        "exact_mobius_identity_checks": mobius_checks,
        "primitive_opposite_parity_points": primitive_count,
        "finite_l2_max_ratio_to_theorem_envelope": max_ratio,
        "finite_l2_ledgers": ledgers,
        "decision": {
            "STAGE14_S5K": "COMPLETE_SIX_LINEAR_MEDIUM_DISPERSION_THEOREM",
            "LINEAR_SIX_POINTWISE_DISCREPANCY_PROVED": True,
            "MEDIUM_LINEAR_L2_DISPERSION_PROVED": True,
            "STATE_SPLIT_E_MIXED_SIGN_OBSTRUCTION_PERSISTS": True,
            "FAMILY_LARGE_SIEVE_THEOREM_PROVED": False,
            "SQRT_B_ASYMPTOTIC_PROVED": False,
            "NEXT": "Stage14-s5l",
        },
    }
    print(json.dumps(report, indent=2))
    print("STAGE14_S5K=COMPLETE_SIX_LINEAR_MEDIUM_DISPERSION_THEOREM")
    print("LINEAR_SIX_POINTWISE_DISCREPANCY_PROVED=true")
    print("MEDIUM_LINEAR_L2_DISPERSION_PROVED=true")
    print("STATE_SPLIT_E_MIXED_SIGN_OBSTRUCTION_PERSISTS=true")
    print("FAMILY_LARGE_SIEVE_THEOREM_PROVED=false")
    print("SQRT_B_ASYMPTOTIC_PROVED=false")
    print("NEXT=Stage14-s5l")


if __name__ == "__main__":
    main()
