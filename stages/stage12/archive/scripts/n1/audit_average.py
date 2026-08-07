#!/usr/bin/env python3
"""Stage12-N1: audit average structure of the shared-p convolution.

This stage tests the Meta-AI proposal to strengthen the N1 lower bound through

    C_raw(B) = 2 * sum_{p<=B} H(p) L_B(p).

The script separates three logically different objects:

1. exact raw oriented chains;
2. primitive oriented chains / unique primitive cuboids where feasible;
3. explicit scaling families which make the raw convolution large but collapse
   after primitive normalization.

No asymptotic formula is inferred from finite ratios. In particular, a lower
bound for C_raw is not reported as a lower bound for N1.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from pathlib import Path
from typing import Any

RAW_THRESHOLDS = [1_000, 2_000, 5_000, 10_000, 20_000, 50_000, 100_000, 200_000]
PRIMITIVE_THRESHOLDS = [1_000, 2_000, 5_000, 10_000, 20_000]
DEFAULT_REPORT = Path("data/shared_p_average_stage12_n1_report.json")


def build_spf(limit: int) -> list[int]:
    spf = list(range(limit + 1))
    if limit >= 1:
        spf[1] = 1
    for prime in range(2, math.isqrt(limit) + 1):
        if spf[prime] != prime:
            continue
        for multiple in range(prime * prime, limit + 1, prime):
            if spf[multiple] == multiple:
                spf[multiple] = prime
    return spf


def factor(value: int, spf: list[int]) -> list[tuple[int, int]]:
    result: list[tuple[int, int]] = []
    while value > 1:
        prime = spf[value]
        exponent = 0
        while value % prime == 0:
            value //= prime
            exponent += 1
        result.append((prime, exponent))
    return result


def square_divisors(factors: list[tuple[int, int]]) -> list[int]:
    divisors = [1]
    for prime, exponent in factors:
        previous = list(divisors)
        powers = [prime**power for power in range(1, 2 * exponent + 1)]
        divisors = previous + [divisor * power for divisor in previous for power in powers]
    return sorted(divisors)


def hypotenuse_count(factors: list[tuple[int, int]]) -> int:
    product = 1
    for prime, exponent in factors:
        if prime % 4 == 1:
            product *= 2 * exponent + 1
    return (product - 1) // 2


def leg_count(p: int, bound: int, factors: list[tuple[int, int]]) -> int:
    square = p * p
    count = 0
    for small in square_divisors(factors):
        if small >= p:
            break
        large = square // small
        if (small - large) & 1:
            continue
        if small + large <= 2 * bound:
            count += 1
    return count


def largest_prime_factor(factors: list[tuple[int, int]]) -> int:
    return factors[-1][0] if factors else 1


def raw_rows(max_bound: int, spf: list[int]) -> list[dict[str, Any]]:
    thresholds = set(RAW_THRESHOLDS)
    rows: list[dict[str, Any]] = []
    sum_h = 0
    sum_l = 0
    sum_hl = 0
    support_h = 0
    support_l = 0
    support_hl = 0
    quintile_contribution = [0, 0, 0, 0, 0]
    smooth_contribution = [0, 0, 0, 0]

    for p in range(1, max_bound + 1):
        factors = factor(p, spf)
        h_value = hypotenuse_count(factors)
        # L_B depends on B, so values must be recomputed at each requested bound.
        if p not in thresholds:
            continue

        # Recompute the complete prefix for determinism and a simple audit trail.
        sum_h = sum_l = sum_hl = 0
        support_h = support_l = support_hl = 0
        quintile_contribution = [0, 0, 0, 0, 0]
        smooth_contribution = [0, 0, 0, 0]
        top_contributors: list[tuple[int, int, int, int, int]] = []
        for q in range(1, p + 1):
            q_factors = factor(q, spf)
            h_q = hypotenuse_count(q_factors)
            l_q = leg_count(q, p, q_factors)
            product = h_q * l_q
            sum_h += h_q
            sum_l += l_q
            sum_hl += product
            support_h += int(h_q > 0)
            support_l += int(l_q > 0)
            support_hl += int(product > 0)
            if product:
                quintile = min(4, (5 * q - 1) // p)
                quintile_contribution[quintile] += product
                largest = largest_prime_factor(q_factors)
                ratio = largest / q
                smooth_bin = 0 if ratio <= 0.10 else 1 if ratio <= 0.25 else 2 if ratio <= 0.50 else 3
                smooth_contribution[smooth_bin] += product
                top_contributors.append((product, q, h_q, l_q, largest))
        top_contributors.sort(reverse=True)
        raw = 2 * sum_hl
        rows.append(
            {
                "B": p,
                "sum_H": sum_h,
                "sum_LB": sum_l,
                "sum_H_times_LB": sum_hl,
                "C_raw": raw,
                "C_raw_over_B": raw / p,
                "C_raw_over_B_log_B": raw / (p * math.log(p)),
                "support_H": support_h,
                "support_LB": support_l,
                "support_product": support_hl,
                "product_contribution_by_p_quintile": quintile_contribution,
                "product_contribution_by_largest_prime_factor_ratio": {
                    "lpf_over_p_le_0.10": smooth_contribution[0],
                    "0.10_to_0.25": smooth_contribution[1],
                    "0.25_to_0.50": smooth_contribution[2],
                    "above_0.50": smooth_contribution[3],
                },
                "top_product_contributors": [
                    {
                        "p": q,
                        "H": h_q,
                        "L_B": l_q,
                        "product": product,
                        "largest_prime_factor": largest,
                    }
                    for product, q, h_q, l_q, largest in top_contributors[:10]
                ],
            }
        )
    return rows


def triangles_by_leg(limit: int, spf: list[int]) -> list[list[tuple[int, int]]]:
    table: list[list[tuple[int, int]]] = [[] for _ in range(limit + 1)]
    for leg in range(1, limit + 1):
        square = leg * leg
        for small in square_divisors(factor(leg, spf)):
            if small >= leg:
                break
            large = square // small
            if (small - large) & 1:
                continue
            other = (large - small) // 2
            hypotenuse = (large + small) // 2
            if other > 0 and hypotenuse <= limit:
                table[leg].append((other, hypotenuse))
    return table


def primitive_rows(limit: int, spf: list[int]) -> list[dict[str, Any]]:
    triangles = triangles_by_leg(limit, spf)
    records: dict[tuple[int, int, int, int], int] = {}
    raw_by_bound = Counter()
    rejected_nonprimitive_by_bound = Counter()

    chains: list[tuple[int, bool, tuple[int, int, int, int]]] = []
    for first_leg in range(1, limit + 1):
        for second_leg, p in triangles[first_leg]:
            for remaining_leg, d in triangles[p]:
                sides = sorted((first_leg, second_leg, remaining_leg))
                key = (sides[0], sides[1], sides[2], d)
                primitive = (
                    sides[0] < sides[1] < sides[2]
                    and math.gcd(math.gcd(sides[0], sides[1]), sides[2]) == 1
                )
                chains.append((d, primitive, key))
                if primitive:
                    records[key] = records.get(key, 0) + 1

    rows = []
    for bound in PRIMITIVE_THRESHOLDS:
        selected = [(d, primitive, key) for d, primitive, key in chains if d <= bound]
        raw_count = len(selected)
        primitive_count = sum(int(primitive) for _, primitive, _ in selected)
        unique = {key for _, primitive, key in selected if primitive}
        rows.append(
            {
                "B": bound,
                "C_raw_direct": raw_count,
                "primitive_oriented_chains": primitive_count,
                "primitive_retention_ratio": primitive_count / raw_count,
                "unique_primitive_cuboids": len(unique),
            }
        )
    return rows


def scaling_trap_rows() -> list[dict[str, Any]]:
    rows = []
    for bound in RAW_THRESHOLDS:
        count = bound // 13
        rows.append(
            {
                "B": bound,
                "parameters_t": count,
                "oriented_raw_chains": 2 * count,
                "primitive_parameters": int(count >= 1),
                "family": "(a,b,c,d,p)=(3t,4t,12t,13t,5t)",
                "gcd": "t",
            }
        )
    return rows


def build_report() -> dict[str, Any]:
    max_bound = max(RAW_THRESHOLDS)
    spf = build_spf(max_bound)
    raw = raw_rows(max_bound, spf)
    primitive = primitive_rows(max(PRIMITIVE_THRESHOLDS), spf)

    return {
        "metadata": {
            "stage": "12-N1",
            "title": "Average structure of the shared-p convolution",
            "generated_by": "scripts/audit_shared_p_average_stage12_n1.py",
            "claim_status": (
                "All identities and finite counts are deterministic. The finite ratios are not "
                "asymptotic claims. A raw-chain lower bound is not an N1 lower bound."
            ),
        },
        "exact_formulas": {
            "H": "H(p)=(prod_{q|p,q=1 mod4}(2*v_q(p)+1)-1)/2",
            "L": (
                "L_B(p)=#{u|p^2: u<p, u and p^2/u same parity, "
                "u+p^2/u<=2B}"
            ),
            "raw_convolution": "C_raw(B)=2*sum_{p<=B}H(p)L_B(p)",
        },
        "finite_raw_average": {
            "rows": raw,
            "interpretation": [
                "C_raw(B)/(B log B) grows on the tested range; no limiting value is claimed.",
                "Most finite product mass comes from p with a small largest prime factor.",
                "These observations motivate average-value analysis but do not establish it.",
            ],
        },
        "primitive_retention": {
            "rows": primitive,
            "warning": (
                "The retention ratio is finite-range only. It shows that primitive correction is "
                "a main-order issue, not a cosmetic constant that may be ignored."
            ),
        },
        "scaling_trap": {
            "proof": [
                "For every t>=1, (3t)^2+(4t)^2=(5t)^2.",
                "Also (5t)^2+(12t)^2=(13t)^2.",
                "Hence p=5t contributes two oriented raw chains whenever 13t<=B.",
                "The resulting cuboid has gcd(3t,4t,12t)=t, so only t=1 is primitive.",
            ],
            "linear_raw_lower_bound": "C_raw(B)>=2*floor(B/13)",
            "rows": scaling_trap_rows(),
            "consequence": (
                "A linear or stronger lower bound for C_raw can be caused entirely by scaled "
                "copies and does not improve the primitive N1 lower bound."
            ),
        },
        "meta_ai_route_audit": {
            "confirmed": [
                "The shared-p convolution is a natural analytic-number-theory object.",
                "Smooth / highly composite p dominate a large part of the tested raw mass.",
                "A strong raw lower bound is easy: the 3-4-5 / 5-12-13 scaling family is linear.",
            ],
            "refuted_or_not_established": [
                "A raw lower bound such as B/sqrt(log B) does not by itself improve N1(B).",
                "Möbius inversion has not yet converted the raw average into a primitive average.",
                "Finite C_raw/(B log B) values do not prove a B log B asymptotic.",
            ],
            "next_required_object": (
                "Replace H(p) and L_B(p) by a primitive-compatible joint weight, or prove an "
                "average bound for the gcd of the two joined Pythagorean triples."
            ),
            "decision": (
                "The first Meta-AI task reaches a genuine wall: raw-average growth is visible and "
                "even has a trivial linear subfamily, but primitive normalization can erase the "
                "entire gain. Continue this branch only through a primitive-compatible convolution."
            ),
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-report", type=Path, default=DEFAULT_REPORT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report = build_report()
    args.write_report.parent.mkdir(parents=True, exist_ok=True)
    args.write_report.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "status": "ok",
                "max_raw_B": RAW_THRESHOLDS[-1],
                "max_raw": report["finite_raw_average"]["rows"][-1]["C_raw"],
                "linear_scaling_lower_bound": report["scaling_trap"]["linear_raw_lower_bound"],
                "decision": "primitive-compatible convolution required",
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
