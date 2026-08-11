#!/usr/bin/env python3
"""Deterministic audit for Stage14-4fn..4fp outer-support compression."""

from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def divisors(n: int):
    return [d for d in range(1, n + 1) if n % d == 0]


def unitary_divisors(n: int):
    return [d for d in divisors(n) if gcd(d, n // d) == 1]


def tau(n: int) -> int:
    return len(divisors(n))


def check_fixed_outer_sandwich() -> None:
    # Use a deterministic physical-like Boolean depending genuinely on the inner divisor.
    for m in range(1, 161):
        cand = unitary_divisors(m)
        assert len(cand) <= tau(m)
        accepted = [u for u in cand if (u + m // u + m) % 5 in (0, 1)]
        a = int(bool(accepted))
        weighted = len(accepted)
        assert a <= weighted
        assert weighted <= max(1, len(cand)) * a


def check_polynomial_outer_pair_sandwich() -> None:
    total_weighted = 0
    total_support = 0
    max_fiber = 1
    for e in range(2, 18):
        for m in range(1, 91):
            cand = unitary_divisors(m)
            max_fiber = max(max_fiber, len(cand))
            accepted = [u for u in cand if (e * m + u * u + m // u) % 7 in (0, 2)]
            total_weighted += len(accepted)
            total_support += int(bool(accepted))
    assert total_support <= total_weighted
    assert total_weighted <= max_fiber * total_support


def check_stage_locks() -> None:
    locks = {
        "stages/stage14/14-4fn/result.md": [
            "FIXED_E_WEIGHTED_INCIDENCE_OUTER_SUPPORT_EXPONENT_EQUIVALENT=true",
            "INNER_WEIGHT_POINTWISE_FACTORIZATION_PROVED=false",
        ],
        "stages/stage14/14-4fo/result.md": [
            "POLYNOMIAL_E_WEIGHTED_INCIDENCE_OUTER_PAIR_SUPPORT_EXPONENT_EQUIVALENT=true",
            "OUTER_PAIR_E_M_REMAINS_GENUINE=true",
        ],
        "stages/stage14/14-4fp/result.md": [
            "PHYSICAL_WEIGHT_OUTERIZED_AT_SUPPORT_LEVEL=true",
            "POINTWISE_WEIGHT_FACTORIZATION_PROVED=false",
            "RECEIVER_MATERIALLY_CHANGED=true",
            "NEXT=Stage14-4fq",
        ],
    }
    for rel, needles in locks.items():
        text = (ROOT / rel).read_text()
        for needle in needles:
            assert needle in text, (rel, needle)


def main() -> None:
    check_fixed_outer_sandwich()
    check_polynomial_outer_pair_sandwich()
    check_stage_locks()
    print("Stage14-4fn..4fp outer physical support audit: OK")


if __name__ == "__main__":
    main()
