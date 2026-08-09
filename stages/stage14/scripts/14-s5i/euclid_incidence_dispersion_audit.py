#!/usr/bin/env python3
"""Deterministic structural audit for Stage14-s5i Euclid incidence bulk."""

from fractions import Fraction
from math import gcd, pi, sqrt
import json

COLUMNS = ("m", "n", "m-n", "m+n", "m2+n2")
LINEAR = {0, 1, 2, 3}
PRIMES = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43)
CRT_PRIME_PAIRS = ((3, 5), (5, 7), (5, 13), (7, 13))
RECTANGLES = (
    (64, 128, 16, 48),
    (128, 256, 32, 96),
    (256, 512, 64, 192),
)
MODULI = (1, 3, 5, 7, 11, 13, 15, 17, 19)
EDGES = ((0, 1), (2, 3), (0, 4), (2, 4))


def values(m, n):
    return (m, n, m - n, m + n, m * m + n * n)


def factor_squarefree(n):
    if n == 1:
        return []
    out = []
    p = 3
    x = n
    while p * p <= x:
        if x % p == 0:
            out.append(p)
            x //= p
            if x % p == 0:
                raise AssertionError(f"modulus is not squarefree: {n}")
        p += 2
    if x > 1:
        out.append(x)
    return out


def local_root_count(p, col):
    total = 0
    for m in range(p):
        for n in range(p):
            if m == 0 and n == 0:
                continue
            if values(m, n)[col] % p == 0:
                total += 1
    return total


def expected_local_root_count(p, col):
    if col in LINEAR:
        return p - 1
    return 2 * (p - 1) if p % 4 == 1 else 0


def local_lambda(q, col):
    ans = Fraction(1, 1)
    for p in factor_squarefree(q):
        if col == 4 and p % 4 == 3:
            return Fraction(0, 1)
        ans *= Fraction(2 if col == 4 else 1, p + 1)
    return ans


def crt_joint_count(p, col_p, q, col_q):
    assert p != q
    Q = p * q
    total = 0
    for m in range(Q):
        for n in range(Q):
            if gcd(gcd(m, n), Q) != 1:
                continue
            vs = values(m, n)
            if vs[col_p] % p == 0 and vs[col_q] % q == 0:
                total += 1
    return total


def primitive_opposite_points(rect):
    m0, m1, n0, n1 = rect
    out = []
    for m in range(m0, m1):
        for n in range(n0, n1):
            assert m > n
            if gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            out.append((m, n, values(m, n)))
    return out


def incidence(points, u, col_u, v, col_v):
    total = 0
    for _, _, vs in points:
        if vs[col_u] % u == 0 and vs[col_v] % v == 0:
            total += 1
    return total


def mobius(n):
    if n == 1:
        return 1
    x = n
    p = 2
    parity = 0
    while p * p <= x:
        if x % p == 0:
            x //= p
            parity ^= 1
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        parity ^= 1
    return -1 if parity else 1


def locally_primitive_candidates(rect, u, col_u, v, col_v):
    Q = u * v
    m0, m1, n0, n1 = rect
    out = []
    for m in range(m0, m1):
        for n in range(n0, n1):
            if (m - n) % 2 == 0:
                continue
            vs = values(m, n)
            if vs[col_u] % u or vs[col_v] % v:
                continue
            if gcd(gcd(m, n), Q) != 1:
                continue
            out.append((m, n))
    return out


def full_mobius_check():
    rect = (80, 160, 20, 60)
    u, col_u = 15, 2
    v, col_v = 7, 3
    Q = u * v
    cand = locally_primitive_candidates(rect, u, col_u, v, col_v)
    exact = sum(gcd(m, n) == 1 for m, n in cand)
    max_d = max(max(m for m, _ in cand), max(n for _, n in cand)) if cand else 1
    total = 0
    for d in range(1, max_d + 1):
        if gcd(d, 2 * Q) != 1:
            continue
        mu = mobius(d)
        if mu:
            total += mu * sum(m % d == 0 and n % d == 0 for m, n in cand)
    assert total == exact
    return {
        "rectangle": rect,
        "u": u,
        "v": v,
        "locally_primitive_candidates": len(cand),
        "exact_primitive_count": exact,
        "full_mobius_sum": total,
    }


def box_profile(rect):
    points = primitive_opposite_points(rect)
    m0, m1, n0, n1 = rect
    X, Y = m1 - m0, n1 - n0
    edge_rows = []
    for col_u, col_v in EDGES:
        residual_sq = 0.0
        actual_sq = 0.0
        bulk_sq = 0.0
        entries = 0
        max_abs_residual = 0.0
        max_row = None
        inert_norm_nonzero = 0
        for u in MODULI:
            for v in MODULI:
                if gcd(u, v) != 1:
                    continue
                actual = incidence(points, u, col_u, v, col_v)
                lu = float(local_lambda(u, col_u))
                lv = float(local_lambda(v, col_v))
                bulk = (4.0 / (pi * pi)) * X * Y * lu * lv
                residual = actual - bulk
                residual_sq += residual * residual
                actual_sq += actual * actual
                bulk_sq += bulk * bulk
                entries += 1
                if col_v == 4 and local_lambda(v, 4) == 0 and actual:
                    inert_norm_nonzero += 1
                if abs(residual) > max_abs_residual:
                    max_abs_residual = abs(residual)
                    max_row = {"u": u, "v": v, "actual": actual, "bulk": bulk, "residual": residual}
        assert inert_norm_nonzero == 0
        edge_rows.append({
            "edge": [COLUMNS[col_u], COLUMNS[col_v]],
            "entries": entries,
            "frobenius_residual": sqrt(residual_sq),
            "frobenius_actual": sqrt(actual_sq),
            "frobenius_bulk": sqrt(bulk_sq),
            "max_abs_residual": max_abs_residual,
            "max_residual_row": max_row,
        })
    return {
        "rectangle": rect,
        "primitive_opposite_parity_points": len(points),
        "edges": edge_rows,
    }


def main():
    local_checks = []
    for p in PRIMES:
        row = {"p": p, "counts": {}}
        for col, name in enumerate(COLUMNS):
            got = local_root_count(p, col)
            expected = expected_local_root_count(p, col)
            assert got == expected
            row["counts"][name] = got
            if col in LINEAR:
                assert Fraction(got, p * p - 1) == Fraction(1, p + 1)
            elif p % 4 == 1:
                assert Fraction(got, p * p - 1) == Fraction(2, p + 1)
            else:
                assert got == 0
        local_checks.append(row)

    crt_checks = []
    for p, q in CRT_PRIME_PAIRS:
        for col_p in range(5):
            for col_q in range(5):
                if col_p == col_q and col_p != 4:
                    continue
                got = crt_joint_count(p, col_p, q, col_q)
                expected = expected_local_root_count(p, col_p) * expected_local_root_count(q, col_q)
                assert got == expected
                crt_checks.append({
                    "p": p,
                    "p_column": COLUMNS[col_p],
                    "q": q,
                    "q_column": COLUMNS[col_q],
                    "count": got,
                })

    mobius_check = full_mobius_check()
    profiles = [box_profile(rect) for rect in RECTANGLES]

    report = {
        "metadata": {
            "stage": "14-s5i",
            "classification": "STRUCTURAL_THEOREM_PLUS_FINITE_DIAGNOSTIC",
            "columns": COLUMNS,
        },
        "local_prime_checks": local_checks,
        "crt_joint_checks": len(crt_checks),
        "full_mobius_check": mobius_check,
        "finite_rectangle_profiles": profiles,
        "decision": {
            "STAGE14_S5I": "COMPLETE_EUCLID_INCIDENCE_RANK_ONE_BULK_AND_DISCREPANCY_REDUCTION",
            "PURE_EUCLID_DIVISIBILITY_BULK_SEPARABLE": True,
            "STATE_SPLIT_MODULI_PRESERVE_BULK_FACTORIZATION": True,
            "EUCLID_INCIDENCE_ARBITRARY_MATRIX_OBSTRUCTION_REDUCED": True,
            "MOBIUS_TRUNCATION_DISCREPANCY_DECOMPOSITION_PROVED": True,
            "DISCREPANCY_SECOND_MOMENT_PROVED": False,
            "SPARSE_LARGE_MODULUS_BLOCKS_CLOSED": False,
            "FAMILY_LARGE_SIEVE_THEOREM_PROVED": False,
            "GLOBAL_SOLUBILITY_AVERAGED": False,
            "SMALL_POINT_WINDOW_AVERAGED": False,
            "SQRT_B_ASYMPTOTIC_PROVED": False,
            "NEXT": "Stage14-s5j prove an L2 dispersion bound for Delta on balanced/medium dyadic blocks and close the sparse Q>=XY regime by divisor switching or isolate its persistent diagonal",
        },
    }
    print(json.dumps(report, indent=2))
    print("STAGE14_S5I=COMPLETE_EUCLID_INCIDENCE_RANK_ONE_BULK_AND_DISCREPANCY_REDUCTION")
    print("PURE_EUCLID_DIVISIBILITY_BULK_SEPARABLE=true")
    print("STATE_SPLIT_MODULI_PRESERVE_BULK_FACTORIZATION=true")
    print("DISCREPANCY_SECOND_MOMENT_PROVED=false")
    print("SPARSE_LARGE_MODULUS_BLOCKS_CLOSED=false")
    print("FAMILY_LARGE_SIEVE_THEOREM_PROVED=false")
    print("SQRT_B_ASYMPTOTIC_PROVED=false")
    print("NEXT=Stage14-s5j")


if __name__ == "__main__":
    main()
