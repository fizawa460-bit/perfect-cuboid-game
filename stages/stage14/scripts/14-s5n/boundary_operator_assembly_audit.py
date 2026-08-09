#!/usr/bin/env python3
"""Deterministic regression audit for Stage14-s5n.

The analytic statements are in result.md. This script checks exact Jacobi
identities, squarefree-character finite ledgers, complementary switching, the
regular-box exponent ledger, and the multi-edge product-conductor mechanism.
"""

from __future__ import annotations

from itertools import combinations
from math import gcd, isqrt, log, sqrt
import json

X = 80
Y = 48
COLUMNS = ("A", "B", "C", "D")
COEFF = {
    "A": (1, 0),
    "B": (0, 1),
    "C": (1, -1),
    "D": (1, 1),
}


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
    if n <= 0:
        return False
    p = 2
    while p * p <= n:
        if n % (p * p) == 0:
            return False
        p += 1
    return True


def odd_squarefree(n):
    return n > 1 and n % 2 == 1 and is_squarefree(n)


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


def mobius_square(n):
    return 1 if is_squarefree(n) else 0


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


def check_squarefree_character_envelope():
    moduli = (5, 13, 17, 29, 65, 85)
    lengths = (20, 40, 80, 160, 320)
    checks = 0
    max_ratio = 0.0
    weighted_max_ratio = 0.0

    for q in moduli:
        assert odd_squarefree(q)
        for T in lengths:
            total = sum(mobius_square(n) * jacobi(n, q) for n in range(1, T + 1))
            envelope = sqrt(T) * (q ** 0.25) * sqrt(log(2 * q))
            ratio = abs(total) / envelope
            max_ratio = max(max_ratio, ratio)
            assert ratio < 5.0, (q, T, total, envelope, ratio)
            checks += 1

            lo = max(2, T // 2)
            weighted = sum(
                mobius_square(n) * jacobi(n, q) / n
                for n in range(lo, T + 1)
            )
            wenv = (lo ** -0.5) * (q ** 0.25) * sqrt(log(2 * q))
            wratio = abs(weighted) / wenv
            weighted_max_ratio = max(weighted_max_ratio, wratio)
            assert wratio < 8.0, (q, T, weighted, wenv, wratio)

    return checks, max_ratio, weighted_max_ratio


def check_multi_edge_multiplicativity():
    us = (3, 7, 11, 19, 23)
    neighbor_sets = ((5,), (5, 13), (5, 13, 17))
    checks = 0
    for u in us:
        for neighbors in neighbor_sets:
            if any(gcd(u, v) != 1 for v in neighbors):
                continue
            prod = 1
            V = 1
            for v in neighbors:
                prod *= jacobi(u, v)
                V *= v
            assert prod == jacobi(u, V), (u, neighbors, prod, jacobi(u, V))
            checks += 1
    return checks


def check_complement_switch():
    points = primitive_points()
    checks = 0
    large_hits = 0
    Z = 8

    for ci, cj in combinations(COLUMNS, 2):
        hi = X + Y
        for m, n in points:
            x = value(ci, m, n)
            y = value(cj, m, n)
            if x == 0 or y == 0:
                continue
            for u in odd_squarefree_divisors(x):
                if u <= hi / Z:
                    continue
                k = abs(x) // u
                assert k < Z
                large_hits += 1
                for v in odd_squarefree_divisors(y):
                    if gcd(u, v) != 1 or gcd(abs(x), v) != 1 or gcd(k, v) != 1:
                        continue
                    lhs = jacobi(u, v)
                    rhs = jacobi(abs(x), v) * jacobi(k, v)
                    assert lhs == rhs, (ci, cj, m, n, u, v, k, lhs, rhs)
                    checks += 1

    assert large_hits > 0
    assert checks > 0
    return large_hits, checks


def small_state_ledger():
    # Finite diagnostic for the dyadic twisted-divisor shape.
    H_i = 80
    H_j = 80
    G = H_i * H_j
    ledgers = []
    max_ratio = 0.0

    for U in (3, 5, 9):
        us = [u for u in range(U, 2 * U) if odd_squarefree(u)]
        for V in (8, 16, 32):
            vs = [v for v in range(V, 2 * V) if odd_squarefree(v)]
            total = 0
            for u in us:
                for x in range(u, H_i + 1, u):
                    for v in vs:
                        if gcd(u, v) != 1:
                            continue
                        total += jacobi(u, v) * (H_j // v)
            envelope = G * (U ** 0.25) * (V ** -0.5) + H_i * V
            ratio = abs(total) / max(1.0, envelope)
            max_ratio = max(max_ratio, ratio)
            assert ratio < 8.0, (U, V, total, envelope, ratio)
            ledgers.append({"U": U, "V": V, "sum": total, "envelope": envelope, "ratio": ratio})

    return ledgers, max_ratio


def switched_ledger():
    H_i = 80
    H_j = 80
    ledgers = []
    max_ratio = 0.0

    for K in (1, 2, 4):
        ks = list(range(K, 2 * K))
        for V in (8, 16, 32):
            vs = [v for v in range(V, 2 * V) if odd_squarefree(v)]
            total = 0
            for k in ks:
                if k == 0:
                    continue
                umax = H_i // k
                for v in vs:
                    if gcd(k, v) != 1:
                        continue
                    s = sum(
                        jacobi(u, v)
                        for u in range(1, umax + 1)
                        if odd_squarefree(u) and gcd(u, v) == 1
                    )
                    total += s * (H_j // v)
            envelope = H_j * sqrt(H_i) * sqrt(max(1, K)) * (V ** 0.25) * sqrt(log(2 * max(vs or [3])))
            ratio = abs(total) / max(1.0, envelope)
            max_ratio = max(max_ratio, ratio)
            assert ratio < 10.0, (K, V, total, envelope, ratio)
            ledgers.append({"K": K, "V": V, "sum": total, "envelope": envelope, "ratio": ratio})

    return ledgers, max_ratio


def exponent_ledger():
    # Exponents in the regular scale M with Z=M^(2/5).
    z = 2.0 / 5.0
    ledger = {
        "linear_central_saving": -z / 2.0,
        "switched_large_saving": z / 2.0 - 1.0 / 4.0,
        "small_medium_saving": -z / 4.0,
        "small_large_corner_saving": 3.0 * z / 4.0 - 1.0 / 2.0,
        "E_central_Z3_minus_perimeter": 3.0 * z - 1.0,
    }
    assert ledger["linear_central_saving"] < 0
    assert ledger["switched_large_saving"] < 0
    assert ledger["small_medium_saving"] < 0
    assert ledger["small_large_corner_saving"] < 0
    assert ledger["E_central_Z3_minus_perimeter"] > 0
    worst_negative = max(
        ledger["linear_central_saving"],
        ledger["switched_large_saving"],
        ledger["small_medium_saving"],
        ledger["small_large_corner_saving"],
    )
    assert abs(worst_negative + 0.05) < 1e-12
    return ledger, worst_negative


def conductor_pileup_ledger():
    # Physical long variable T~M; each neighboring conductor ~M.
    entries = []
    for degree in (1, 2, 3):
        completion_exponent = 0.5 + 0.25 * degree
        saving_vs_trivial = completion_exponent - 1.0
        entries.append({
            "degree": degree,
            "completion_exponent": completion_exponent,
            "relative_exponent_vs_length_M": saving_vs_trivial,
        })
    assert entries[0]["relative_exponent_vs_length_M"] < 0
    assert abs(entries[1]["relative_exponent_vs_length_M"]) < 1e-12
    assert entries[2]["relative_exponent_vs_length_M"] > 0
    return entries


def main():
    sq_checks, sq_ratio, weighted_ratio = check_squarefree_character_envelope()
    mult_checks = check_multi_edge_multiplicativity()
    large_hits, switch_checks = check_complement_switch()
    small_ledgers, small_ratio = small_state_ledger()
    switched_ledgers, switched_ratio = switched_ledger()
    exponents, worst_negative = exponent_ledger()
    pileup = conductor_pileup_ledger()

    report = {
        "metadata": {
            "stage": "14-s5n",
            "classification": "DETERMINISTIC_REGRESSION_PLUS_ANALYTIC_THEOREM_INTERFACE",
        },
        "squarefree_character": {
            "checks": sq_checks,
            "max_ratio": sq_ratio,
            "weighted_max_ratio": weighted_ratio,
        },
        "multi_edge_multiplicativity_checks": mult_checks,
        "complement_switch": {
            "large_hits": large_hits,
            "jacobi_checks": switch_checks,
        },
        "small_state": {
            "max_ratio": small_ratio,
            "ledgers": small_ledgers,
        },
        "switched_boundary": {
            "max_ratio": switched_ratio,
            "ledgers": switched_ledgers,
        },
        "regular_box_exponents": exponents,
        "worst_single_edge_relative_exponent": worst_negative,
        "conductor_pileup": pileup,
        "decision": {
            "STAGE14_S5N": "COMPLETE_ONE_SMALL_VARIABLE_BOUNDARY_AVERAGING_AND_MULTI_EDGE_CONDUCTOR_OBSTRUCTION",
            "SQUAREFREE_QUADRATIC_COMPLETION_LEMMA_PROVED": True,
            "SINGLE_EDGE_SMALL_STATE_BOUNDARY_AVERAGED": True,
            "SINGLE_EDGE_SWITCHED_PHYSICAL_CHARACTER_AVERAGED": True,
            "SINGLE_EDGE_SMALL_LARGE_CORNER_AVERAGED": True,
            "MICROSCOPIC_CENTERED_PERIODIC_BOUND_PROVED": True,
            "REGULAR_BOX_COMMON_CUTOFF_Z_EQ_M_2_5_VALID": True,
            "SINGLE_LINEAR_EDGE_FULL_DYADIC_SUMMATION_PROVED": True,
            "ALL_SIX_LINEAR_EDGES_INDIVIDUALLY_CLOSED": True,
            "MULTI_EDGE_PRODUCT_CONDUCTOR_OBSTRUCTION_ISOLATED": True,
            "FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED": False,
            "FAMILY_LARGE_SIEVE_THEOREM_PROVED": False,
            "SQRT_B_ASYMPTOTIC_PROVED": False,
            "NEXT": "Stage14-s5o",
        },
    }
    print(json.dumps(report, indent=2))
    print("STAGE14_S5N=COMPLETE_ONE_SMALL_VARIABLE_BOUNDARY_AVERAGING_AND_MULTI_EDGE_CONDUCTOR_OBSTRUCTION")
    print("SQUAREFREE_QUADRATIC_COMPLETION_LEMMA_PROVED=true")
    print("SINGLE_EDGE_SMALL_STATE_BOUNDARY_AVERAGED=true")
    print("SINGLE_EDGE_SWITCHED_PHYSICAL_CHARACTER_AVERAGED=true")
    print("SINGLE_EDGE_SMALL_LARGE_CORNER_AVERAGED=true")
    print("MICROSCOPIC_CENTERED_PERIODIC_BOUND_PROVED=true")
    print("REGULAR_BOX_COMMON_CUTOFF_Z_EQ_M_2_5_VALID=true")
    print("SINGLE_LINEAR_EDGE_FULL_DYADIC_SUMMATION_PROVED=true")
    print("ALL_SIX_LINEAR_EDGES_INDIVIDUALLY_CLOSED=true")
    print("MULTI_EDGE_PRODUCT_CONDUCTOR_OBSTRUCTION_ISOLATED=true")
    print("FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED=false")
    print("FAMILY_LARGE_SIEVE_THEOREM_PROVED=false")
    print("SQRT_B_ASYMPTOTIC_PROVED=false")
    print("NEXT=Stage14-s5o")


if __name__ == "__main__":
    main()
