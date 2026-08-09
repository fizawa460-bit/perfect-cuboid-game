#!/usr/bin/env python3
"""Deterministic algebra audit for Stage14-s5h."""

from fractions import Fraction
from itertools import combinations, product
from math import gcd, isqrt, sqrt
import json

CUTS = (2000, 5000, 10000, 20000)
FACTORS = ("m", "n", "m-n", "m+n", "m2+n2")
EDGES = tuple(combinations(range(5), 2))


def rows(B):
    out = []
    for m in range(2, isqrt(B) + 1):
        for n in range(1, m):
            if gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            if m * m + n * n <= B:
                out.append((m, n))
    return out


def values(m, n):
    return (m, n, m - n, m + n, m * m + n * n)


def odd_squarefree_kernel(x):
    while x % 2 == 0:
        x //= 2
    out = 1
    p = 3
    while p * p <= x:
        parity = 0
        while x % p == 0:
            x //= p
            parity ^= 1
        if parity:
            out *= p
        p += 2
    if x > 1:
        out *= x
    return out


def jacobi(a, n):
    assert n > 0 and n % 2 == 1
    a %= n
    sign = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                sign = -sign
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            sign = -sign
        a %= n
    return sign if n == 1 else 0


def odd_prime_factors(x):
    out = []
    p = 3
    while p * p <= x:
        if x % p == 0:
            out.append(p)
            while x % p == 0:
                x //= p
        p += 2
    if x > 1:
        out.append(x)
    return out


def local_row_truth_table():
    records = []
    for x, s in product((-1, 1), repeat=2):
        formulas = {
            "selected_S_or_H": Fraction(1 + x, 2),
            "selected_X": Fraction((1 + s) * (1 + x), 4),
            "unselected_S_or_H": Fraction(1 + x, 2),
            "unselected_X": Fraction(3 + x - s + s * x, 4),
        }
        expected = {
            "selected_S_or_H": int(x == 1),
            "selected_X": int(s == 1 and x == 1),
            "unselected_S_or_H": int(x == 1),
            "unselected_X": int(s == -1 or x == 1),
        }
        for key in formulas:
            assert formulas[key].denominator == 1
            assert int(formulas[key]) == expected[key]
        records.append({
            "x": x,
            "minus_one_character": s,
            "values": {k: int(v) for k, v in formulas.items()},
        })
    return records


def audit(B):
    rs = rows(B)
    reciprocity_checks = 0
    e_column_checks = 0
    nontrivial_edge_samples = {f"{FACTORS[i]}|{FACTORS[j]}": 0 for i, j in EDGES}
    negative_edge_samples = {f"{FACTORS[i]}|{FACTORS[j]}": 0 for i, j in EDGES}

    for m, n in rs:
        kernels = tuple(odd_squarefree_kernel(v) for v in values(m, n))
        a, b, c, d, e = kernels

        for p in odd_prime_factors(e):
            assert p % 4 == 1

        for i, j in EDGES:
            u, v = kernels[i], kernels[j]
            assert gcd(u, v) == 1
            uv = jacobi(u, v)
            vu = jacobi(v, u)
            reciprocity_sign = -1 if u % 4 == 3 and v % 4 == 3 else 1
            assert uv * vu == reciprocity_sign
            reciprocity_checks += 1

            key = f"{FACTORS[i]}|{FACTORS[j]}"
            if u > 1 and v > 1:
                nontrivial_edge_samples[key] += 1
                if uv == -1:
                    negative_edge_samples[key] += 1

        # Exact whole-kernel collapse for the m^2+n^2 column.
        assert jacobi(a, e) == 1
        assert jacobi(b, e) == 1
        assert jacobi(c, e) == jacobi(2, c)
        assert jacobi(d, e) == jacobi(2, d)
        e_column_checks += 4

    return {
        "B": B,
        "primitive_opposite_parity_pairs": len(rs),
        "reciprocity_checks": reciprocity_checks,
        "e_column_identity_checks": e_column_checks,
        "nontrivial_edge_samples": nontrivial_edge_samples,
        "negative_edge_samples": negative_edge_samples,
    }


def bilinear_ratio(U, V):
    # For |alpha|,|beta|<=1, the separable large-sieve bound is
    # sqrt(U*V*(U+V)) up to (UV)^epsilon, versus the trivial U*V.
    return sqrt(1 / U + 1 / V)


def main():
    truth = local_row_truth_table()
    profile = [audit(B) for B in CUTS]
    dyadic_examples = [
        {"U": U, "V": V, "bound_to_trivial_ratio_without_epsilon": bilinear_ratio(U, V)}
        for U, V in ((16, 16), (16, 256), (256, 256), (256, 4096))
    ]
    report = {
        "metadata": {
            "stage": "14-s5h",
            "classification": "ALGEBRAIC_REDUCTION_PLUS_IMPORTED_QUADRATIC_LARGE_SIEVE",
            "factor_order": FACTORS,
            "raw_whole_kernel_edge_count": len(EDGES),
        },
        "local_row_truth_table": truth,
        "profile": profile,
        "dyadic_examples": dyadic_examples,
        "decision": {
            "STAGE14_S5H": "COMPLETE_RECIPROCAL_OFFDIAGONAL_REDUCTION_AND_FIRST_DYADIC_BILINEAR_BOUND",
            "LOCAL_ROWS_FINITE_CHARACTER_POLYNOMIAL": True,
            "WHOLE_KERNEL_E_COLUMN_COLLAPSES": True,
            "WHOLE_KERNEL_GENUINE_RECIPROCAL_EDGE_COUNT": 6,
            "STATE_SPLIT_E_PIECES_CAN_REINTRODUCE_BILINEARITY": True,
            "FIRST_SEPARABLE_DYADIC_BILINEAR_BOUND_PROVED": True,
            "EUCLID_INCIDENCE_SEPARABILITY_PROVED": False,
            "FAMILY_LARGE_SIEVE_THEOREM_PROVED": False,
            "GLOBAL_SOLUBILITY_AVERAGED": False,
            "SMALL_POINT_WINDOW_AVERAGED": False,
            "SQRT_B_ASYMPTOTIC_PROVED": False,
            "NEXT": "Stage14-s5i derive a dyadic Euclid-incidence dispersion/low-rank decomposition that converts the two-variable divisor weight into large-sieve-admissible coefficients, or isolate a persistent diagonal obstruction",
        },
    }
    print(json.dumps(report, indent=2))
    print("STAGE14_S5H=COMPLETE_RECIPROCAL_OFFDIAGONAL_REDUCTION_AND_FIRST_DYADIC_BILINEAR_BOUND")
    print("WHOLE_KERNEL_GENUINE_RECIPROCAL_EDGE_COUNT=6")
    print("FIRST_SEPARABLE_DYADIC_BILINEAR_BOUND_PROVED=true")
    print("EUCLID_INCIDENCE_SEPARABILITY_PROVED=false")
    print("FAMILY_LARGE_SIEVE_THEOREM_PROVED=false")
    print("SMALL_POINT_WINDOW_AVERAGED=false")
    print("SQRT_B_ASYMPTOTIC_PROVED=false")
    print("NEXT=Stage14-s5i")


if __name__ == "__main__":
    main()
