#!/usr/bin/env python3
"""Finite diagnostic for the Stage14-s5g quadratic-character candidate."""

from itertools import combinations
from math import gcd, isqrt
import json

CUTS = (2000, 5000, 10000, 20000)
PRIME_LIMIT = 97
FACTORS = ("m", "n", "m-n", "m+n", "m2+n2")


def primes_upto(n):
    out = []
    for p in range(3, n + 1, 2):
        if all(p % q for q in range(3, isqrt(p) + 1, 2)):
            out.append(p)
    return out


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


def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    z = pow(a, (p - 1) // 2, p)
    return 1 if z == 1 else -1


def odd_support_separated(vs):
    for a, b in combinations(vs, 2):
        g = gcd(a, b)
        while g % 2 == 0:
            g //= 2
        if g != 1:
            return False
    return True


def local_profiles(ps):
    out = {}
    for p in ps:
        for mask in range(1, 32):
            total = 0
            nonzero = 0
            for m in range(p):
                for n in range(p):
                    if m == n == 0:
                        continue
                    z = 1
                    chars = [legendre(v, p) for v in values(m, n)]
                    for i in range(5):
                        if (mask >> i) & 1:
                            z *= chars[i]
                    if z:
                        total += z
                        nonzero += 1
            out[(p, mask)] = (total, nonzero)
    return out


def audit(B):
    rs = rows(B)
    assert rs
    assert all(odd_support_separated(values(m, n)) for m, n in rs)
    ps = primes_upto(PRIME_LIMIT)
    local = local_profiles(ps)
    records = []
    for p in ps:
        sums = [0] * 32
        nonzero = [0] * 32
        for m, n in rs:
            chars = [legendre(v, p) for v in values(m, n)]
            for mask in range(1, 32):
                z = 1
                for i in range(5):
                    if (mask >> i) & 1:
                        z *= chars[i]
                sums[mask] += z
                nonzero[mask] += z != 0
        for mask in range(1, 32):
            denom = nonzero[mask]
            lsum, lnonzero = local[(p, mask)]
            beta = lsum / lnonzero if lnonzero else 0.0
            centered = sums[mask] - beta * denom
            records.append({
                "p": p,
                "mask": mask,
                "sum": sums[mask],
                "nonzero": denom,
                "normalized_abs": abs(sums[mask]) / denom if denom else 0.0,
                "local_mean": beta,
                "centered_sum": centered,
                "centered_normalized_abs": abs(centered) / denom if denom else 0.0,
            })
    worst = max(records, key=lambda r: (r["centered_normalized_abs"], -r["p"], -r["mask"]))
    resonances = [
        {
            "p": r["p"],
            "mask": r["mask"],
            "factors": [FACTORS[i] for i in range(5) if (r["mask"] >> i) & 1],
            "sign": 1 if r["sum"] > 0 else -1,
            "nonzero": r["nonzero"],
        }
        for r in records
        if abs(r["local_mean"]) == 1
    ]
    mean_square = sum(r["sum"] ** 2 for r in records) / len(records)
    centered_mean_square = sum(r["centered_sum"] ** 2 for r in records) / len(records)
    return {
        "B": B,
        "primitive_opposite_parity_pairs": len(rs),
        "prime_count": len(ps),
        "mask_count_per_prime": 31,
        "tested_character_sums": len(records),
        "worst_centered_normalized_abs": worst["centered_normalized_abs"],
        "worst_prime": worst["p"],
        "worst_mask": worst["mask"],
        "worst_mask_factors": [FACTORS[i] for i in range(5) if (worst["mask"] >> i) & 1],
        "worst_sum": worst["sum"],
        "worst_local_mean": worst["local_mean"],
        "worst_centered_sum": worst["centered_sum"],
        "worst_nonzero_terms": worst["nonzero"],
        "mean_square_sum": mean_square,
        "mean_square_per_pair": mean_square / len(rs),
        "centered_mean_square_sum": centered_mean_square,
        "centered_mean_square_per_pair": centered_mean_square / len(rs),
        "local_exact_resonances": resonances,
    }


def main():
    profile = [audit(B) for B in CUTS]
    report = {
        "metadata": {
            "stage": "14-s5g",
            "classification": "FINITE_DIAGNOSTIC_ONLY",
            "prime_limit": PRIME_LIMIT,
            "factor_order": FACTORS,
        },
        "profile": profile,
        "decision": {
            "STAGE14_S5G": "FIRST_GLOBAL_CHARACTER_SUM_CANDIDATE_AND_FINITE_STRESS_TEST",
            "ODD_FACTOR_SUPPORT_PAIRWISE_DISJOINT_RECHECKED": True,
            "NONTRIVIAL_FACTOR_MASKS_TESTED": 31,
            "FAMILY_LARGE_SIEVE_THEOREM_PROVED": False,
            "GLOBAL_SOLUBILITY_AVERAGED": False,
            "SMALL_POINT_WINDOW_AVERAGED": False,
            "SQRT_B_ASYMPTOTIC_PROVED": False,
            "NEXT": "Stage14-s5h isolate reciprocal off-diagonal forms and prove a first dyadic bilinear bound or exhibit the obstruction",
        },
    }
    print(json.dumps(report, indent=2))
    print("STAGE14_S5G=FIRST_GLOBAL_CHARACTER_SUM_CANDIDATE_AND_FINITE_STRESS_TEST")
    print("FAMILY_LARGE_SIEVE_THEOREM_PROVED=false")
    print("SMALL_POINT_WINDOW_AVERAGED=false")
    print("SQRT_B_ASYMPTOTIC_PROVED=false")
    print("NEXT=Stage14-s5h")


if __name__ == "__main__":
    main()
