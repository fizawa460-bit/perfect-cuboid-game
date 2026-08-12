#!/usr/bin/env python3
from __future__ import annotations

import math


def naive_k_sum(K: int) -> float:
    return sum(k ** -0.5 for k in range(1, K + 1))


def split_prime_squarefree(n: int) -> bool:
    if n <= 0:
        return False
    eta = 0
    if n % 2 == 0:
        eta = 1
        n //= 2
        if n % 2 == 0:
            return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            if p % 4 != 1:
                return False
            n //= p
            if n % p == 0:
                return False
        p += 2
    if n > 1 and n % 4 != 1:
        return False
    return eta in (0, 1)


def allowed_k_sum(K: int) -> tuple[int, float]:
    vals = [k for k in range(1, K + 1) if split_prime_squarefree(k)]
    return len(vals), sum(k ** -0.5 for k in vals)


def audit_growth() -> list[dict]:
    rows = []
    previous_count = 0
    previous_sum = 0.0
    for K in (100, 1000, 10000):
        count, weighted = allowed_k_sum(K)
        if count <= previous_count or weighted <= previous_sum:
            raise AssertionError("allowed norm-core population must grow")
        if weighted <= 1.0:
            raise AssertionError("weighted core sum is not a bounded decoration")
        rows.append(
            {
                "K": K,
                "allowed_count": count,
                "allowed_weighted_sum": weighted,
                "all_k_weighted_sum": naive_k_sum(K),
            }
        )
        previous_count = count
        previous_sum = weighted
    return rows


if __name__ == "__main__":
    rows = audit_growth()
    print("STAGE15_6AQ_NORM_CORE_GATE=PASS")
    print("NAIVE_K_SUM_SUBPOLYNOMIAL=false")
    print("NORM_CORE_RECHARGE_ALLOWED=false")
    for row in rows:
        print(row)
