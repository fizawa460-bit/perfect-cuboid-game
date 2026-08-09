#!/usr/bin/env python3
"""Deterministic regression audit for Stage14-s5m.

The analytic statements are proved in result.md.  This script checks the exact
interfaces: fixed E-root lattices, their index and shortest-vector barrier,
finite discrepancy ledgers, and complementary-divisor switching.
"""

from __future__ import annotations

from itertools import combinations
from math import gcd, isqrt, pi, sqrt
import json

X = 72
Y = 44
Z = 6
COLUMNS = ("A", "B", "C", "D")
COEFF = {
    "A": (1, 0),
    "B": (0, 1),
    "C": (1, -1),
    "D": (1, 1),
}
WIDTHS = {
    "A": X,
    "B": Y,
    "C": X,
    "D": X + Y,
}
U_SAMPLES = (3, 5, 7, 11, 13)
V_SAMPLES = (5, 13, 17, 65, 85)
U_BLOCKS = (4, 8, 16)
V_BLOCKS = (5, 13, 32)


def value(col, m, n):
    a, b = COEFF[col]
    return a * m + b * n


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
    for p in range(2, isqrt(n) + 1):
        if n % (p * p) == 0:
            return False
    return True


def odd_squarefree(n):
    return n > 1 and n % 2 == 1 and is_squarefree(n)


def split_squarefree(n):
    return odd_squarefree(n) and all(p % 4 == 1 for p in prime_factors(n))


def roots_minus_one(v):
    return [r for r in range(v) if (r * r + 1) % v == 0]


def lam(q):
    z = 1.0
    for p in prime_factors(q):
        z /= p + 1
    return z


def lam_e(q):
    z = 1.0
    for p in prime_factors(q):
        z *= 2.0 / (p + 1)
    return z


def jacobi(a, n):
    assert n > 0 and n % 2 == 1
    a %= n
    result = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a %= n
    return result if n == 1 else 0


def divisors(n):
    out = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


def odd_squarefree_divisors(n):
    return [d for d in divisors(abs(n)) if odd_squarefree(d)]


def check_root_counts():
    checks = 0
    for v in range(5, 513, 2):
        if not split_squarefree(v):
            continue
        roots = roots_minus_one(v)
        expected = 2 ** len(prime_factors(v))
        assert len(roots) == expected, (v, len(roots), expected)
        checks += 1
    return checks


def in_lattice(col, u, v, r, m, n):
    return value(col, m, n) % u == 0 and (m - r * n) % v == 0


def check_lattice_index_and_shortest_barrier():
    index_checks = 0
    vector_checks = 0
    min_ratio = float("inf")

    for col in COLUMNS:
        for u in U_SAMPLES:
            for v in V_SAMPLES:
                if not split_squarefree(v) or gcd(u, v) != 1:
                    continue
                q = u * v
                for r in roots_minus_one(v):
                    # Index uv means exactly q residue vectors mod q in the lattice.
                    residue_count = 0
                    for m in range(q):
                        for n in range(q):
                            residue_count += in_lattice(col, u, v, r, m, n)
                    assert residue_count == q, (col, u, v, r, residue_count, q)
                    index_checks += 1

                    K = max(sqrt(v), min(u, v))
                    barrier = K / sqrt(2.0)
                    R = max(2, int(barrier) + 2)
                    for m in range(-R, R + 1):
                        for n in range(-R, R + 1):
                            if m == 0 and n == 0:
                                continue
                            if not in_lattice(col, u, v, r, m, n):
                                continue
                            norm = sqrt(m * m + n * n)
                            assert (m * m + n * n) % v == 0
                            assert norm + 1e-12 >= barrier, (
                                col,
                                u,
                                v,
                                r,
                                m,
                                n,
                                norm,
                                barrier,
                            )
                            min_ratio = min(min_ratio, norm / K)
                            vector_checks += 1

    assert index_checks > 0
    assert vector_checks > 0
    return index_checks, vector_checks, min_ratio


def block(U, split=False):
    pred = split_squarefree if split else odd_squarefree
    return [q for q in range(U, 2 * U) if pred(q)]


def signed_count(points, col, u, v, r):
    return sum(
        1
        for m, n in points
        if value(col, m, n) % u == 0 and (m - r * n) % v == 0
    )


def unsplit_count(points, col, u, v):
    return sum(
        1
        for m, n in points
        if value(col, m, n) % u == 0 and (m * m + n * n) % v == 0
    )


def discrepancy_ledgers():
    points = primitive_points()
    N = len(points)
    P = 2 * (X + Y)
    signed_max_ratio = 0.0
    unsplit_l2_max_ratio = 0.0
    signed_checks = 0
    blocks = 0

    for col in COLUMNS:
        for U in U_BLOCKS:
            us = block(U, split=False)
            for V in V_BLOCKS:
                vs = block(V, split=True)
                l2 = 0.0
                cells = 0
                K = max(sqrt(V), min(U, V))
                for u in us:
                    for v in vs:
                        if gcd(u, v) != 1:
                            continue
                        root_sum = 0
                        for r in roots_minus_one(v):
                            w = signed_count(points, col, u, v, r)
                            main_r = N * lam(u) * lam(v)
                            delta_r = abs(w - main_r)
                            envelope_r = 1.0 + P / max(1.0, max(sqrt(v), min(u, v)))
                            signed_max_ratio = max(signed_max_ratio, delta_r / envelope_r)
                            signed_checks += 1
                            root_sum += w
                        direct = unsplit_count(points, col, u, v)
                        assert root_sum == direct
                        main = N * lam(u) * lam_e(v)
                        delta = direct - main
                        l2 += delta * delta
                        cells += 1
                Q = U * V
                envelope = max(1.0, Q * (1.0 + P * P / (K * K)))
                ratio = l2 / envelope
                unsplit_l2_max_ratio = max(unsplit_l2_max_ratio, ratio)
                blocks += 1

    # Finite boxes carry substantial boundary effects; these are regression ceilings only.
    assert signed_max_ratio < 20.0, signed_max_ratio
    assert unsplit_l2_max_ratio < 20.0, unsplit_l2_max_ratio
    return {
        "primitive_points": N,
        "signed_checks": signed_checks,
        "dyadic_blocks": blocks,
        "signed_max_ratio_to_pointwise_shape": signed_max_ratio,
        "unsplit_l2_max_ratio_to_shape": unsplit_l2_max_ratio,
    }


def check_complement_switch():
    points = primitive_points()
    bijection_checks = 0
    jacobi_checks = 0
    large_states = 0

    for ci, cj in combinations(COLUMNS, 2):
        hi = WIDTHS[ci]
        for m, n in points:
            x = value(ci, m, n)
            y = value(cj, m, n)
            if x == 0 or y == 0:
                continue
            for u in odd_squarefree_divisors(x):
                if u <= hi / Z:
                    continue
                k = abs(x) // u
                assert k < Z, (ci, m, n, x, u, k, hi)
                assert u == abs(x) // k
                large_states += 1
                bijection_checks += 1

                for v in odd_squarefree_divisors(y):
                    if gcd(u, v) != 1 or gcd(abs(x), v) != 1:
                        continue
                    lhs = jacobi(u, v)
                    rhs = jacobi(abs(x), v) * jacobi(k, v)
                    assert lhs == rhs, (ci, cj, m, n, u, v, k, lhs, rhs)
                    jacobi_checks += 1

    assert large_states > 0
    assert jacobi_checks > 0
    return large_states, bijection_checks, jacobi_checks


def main():
    root_checks = check_root_counts()
    index_checks, vector_checks, min_ratio = check_lattice_index_and_shortest_barrier()
    ledgers = discrepancy_ledgers()
    large_states, bijection_checks, jacobi_checks = check_complement_switch()

    report = {
        "metadata": {
            "stage": "14-s5m",
            "box": {"X": X, "Y": Y},
            "cutoff_Z": Z,
            "classification": "DETERMINISTIC_REGRESSION_PLUS_ANALYTIC_THEOREM_INTERFACE",
        },
        "root_count_checks": root_checks,
        "fixed_root_lattice_index_checks": index_checks,
        "shortest_vector_checks": vector_checks,
        "finite_min_shortest_ratio_to_K": min_ratio,
        "discrepancy_ledgers": ledgers,
        "complement_switch": {
            "large_state_occurrences": large_states,
            "bijection_checks": bijection_checks,
            "jacobi_rewrite_checks": jacobi_checks,
        },
        "decision": {
            "STAGE14_S5M": "COMPLETE_MEDIUM_E_SIGNED_ROOT_LATTICE_DISPERSION_AND_LINEAR_BOUNDARY_SWITCH",
            "E_FIXED_ROOT_LATTICE_DETERMINANT_UV": True,
            "E_FIXED_ROOT_SHORTEST_VECTOR_BOUND_PROVED": True,
            "MEDIUM_E_LINEAR_DISPERSION_PROVED": True,
            "E_CENTRAL_MEDIUM_POWER_SAVING_PROVED": True,
            "LINEAR_LARGE_BOUNDARY_COMPLEMENT_SWITCH_EXACT": True,
            "LINEAR_BOUNDARY_REDUCED_TO_ONE_SMALL_VARIABLE": True,
            "FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED": False,
            "FAMILY_LARGE_SIEVE_THEOREM_PROVED": False,
            "SQRT_B_ASYMPTOTIC_PROVED": False,
            "NEXT": "Stage14-s5n",
        },
    }
    print(json.dumps(report, indent=2))
    print("STAGE14_S5M=COMPLETE_MEDIUM_E_SIGNED_ROOT_LATTICE_DISPERSION_AND_LINEAR_BOUNDARY_SWITCH")
    print("E_FIXED_ROOT_LATTICE_DETERMINANT_UV=true")
    print("E_FIXED_ROOT_SHORTEST_VECTOR_BOUND_PROVED=true")
    print("MEDIUM_E_LINEAR_DISPERSION_PROVED=true")
    print("E_CENTRAL_MEDIUM_POWER_SAVING_PROVED=true")
    print("LINEAR_LARGE_BOUNDARY_COMPLEMENT_SWITCH_EXACT=true")
    print("LINEAR_BOUNDARY_REDUCED_TO_ONE_SMALL_VARIABLE=true")
    print("FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED=false")
    print("FAMILY_LARGE_SIEVE_THEOREM_PROVED=false")
    print("SQRT_B_ASYMPTOTIC_PROVED=false")
    print("NEXT=Stage14-s5n")


if __name__ == "__main__":
    main()
