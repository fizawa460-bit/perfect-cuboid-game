#!/usr/bin/env python3
"""Stage12-N1b: close the primitive correction in the shared-p convolution.

For a first right triangle x^2+y^2=p^2 let g=gcd(x,y).  Joining it to
p^2+c^2=d^2 gives a cuboid whose three-side gcd is exactly gcd(g,c).
This turns primitive compatibility into a two-variable coprimality weight.

All finite identities below are deterministic.  No asymptotic density or
improvement beyond the Stage11 lower bound is claimed.
"""
from __future__ import annotations

import argparse
import json
import math
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from audit_shared_p_convolution_stage11 import (
    MAX_D,
    THRESHOLDS,
    build_spf,
    enumerate_shared_p,
    factor_with_spf,
)

DEFAULT_REPORT = Path("data/shared_p_primitive_joint_stage12_n1b_report.json")


def mobius_sieve(limit: int) -> list[int]:
    mu = [1] * (limit + 1)
    prime = [True] * (limit + 1)
    for p in range(2, limit + 1):
        if not prime[p]:
            continue
        for n in range(p, limit + 1, p):
            prime[n] = False if n != p else prime[n]
            mu[n] *= -1
        square = p * p
        for n in range(square, limit + 1, square):
            mu[n] = 0
    mu[0] = 0
    return mu


def divisors(value: int, spf: list[int]) -> list[int]:
    result = [1]
    for p, e in factor_with_spf(value, spf):
        powers = [p**j for j in range(1, e + 1)]
        result = result + [d * power for d in result for power in powers]
    return sorted(result)


def primitive_hypotenuse_count(h: int, spf: list[int]) -> int:
    """Unordered primitive positive triples with hypotenuse h."""
    if h <= 1 or h % 2 == 0:
        return 0
    omega = 0
    for p, _ in factor_with_spf(h, spf):
        if p % 4 != 1:
            return 0
        omega += 1
    return 1 << (omega - 1) if omega else 0


def build_first_representations(triangles: list[list[tuple[int, int, int, int]]]) -> dict[int, list[tuple[int, int, int]]]:
    by_p: dict[int, list[tuple[int, int, int]]] = defaultdict(list)
    for x in range(1, len(triangles)):
        for y, p, _, _ in triangles[x]:
            if x < y:
                by_p[p].append((x, y, math.gcd(x, y)))
    return dict(by_p)


def check_scale_decomposition(
    first_by_p: dict[int, list[tuple[int, int, int]]], spf: list[int]
) -> dict[str, Any]:
    mismatches: list[dict[str, Any]] = []
    checked_groups = 0
    for p, reps in first_by_p.items():
        actual = Counter(g for _, _, g in reps)
        predicted = {
            g: primitive_hypotenuse_count(p // g, spf)
            for g in divisors(p, spf)
            if primitive_hypotenuse_count(p // g, spf)
        }
        checked_groups += len(set(actual) | set(predicted))
        if dict(sorted(actual.items())) != dict(sorted(predicted.items())):
            mismatches.append({"p": p, "actual": dict(actual), "predicted": predicted})
            if len(mismatches) >= 10:
                break
    if mismatches:
        raise ArithmeticError(f"primitive-scale decomposition mismatch: {mismatches[:3]}")
    return {
        "checked_p": len(first_by_p),
        "checked_scale_groups": checked_groups,
        "mismatches": 0,
        "formula": "#{(x,y):x<y,x^2+y^2=p^2,gcd(x,y)=g}=P(p/g)",
        "P_formula": "P(h)=2^(omega(h)-1) if h is odd and every prime divisor is 1 mod4; otherwise 0",
    }


def bound_row(
    bound: int,
    triangles: list[list[tuple[int, int, int, int]]],
    first_by_p: dict[int, list[tuple[int, int, int]]],
    stage11_records: dict[tuple[int, int, int, int], dict[str, Any]],
    spf: list[int],
    mu: list[int],
) -> dict[str, Any]:
    raw_unoriented = 0
    coprime_unoriented_direct = 0
    mobius_unoriented = 0
    repeated_primitive_unoriented = 0
    gcd_scale_contribution: Counter[int] = Counter()
    mobius_term_by_k: Counter[int] = Counter()

    for p in range(1, bound + 1):
        first = first_by_p.get(p, [])
        second = [(c, d) for c, d, _, _ in triangles[p] if d <= bound]
        raw_unoriented += len(first) * len(second)

        # Direct primitive-compatible count and equal-side correction.
        for x, y, g in first:
            for c, _ in second:
                if math.gcd(g, c) != 1:
                    continue
                coprime_unoriented_direct += 1
                gcd_scale_contribution[g] += 1
                if c == x or c == y:
                    repeated_primitive_unoriented += 1

        # Möbius factorization of 1_{gcd(g,c)=1}.
        if not first or not second:
            continue
        divisibility_first: Counter[int] = Counter()
        divisibility_second: Counter[int] = Counter()
        relevant_k: set[int] = set()
        for _, _, g in first:
            for k in divisors(g, spf):
                if mu[k]:
                    divisibility_first[k] += 1
                    relevant_k.add(k)
        for c, _ in second:
            for k in divisors(c, spf):
                if mu[k]:
                    divisibility_second[k] += 1
        for k in relevant_k:
            term = mu[k] * divisibility_first[k] * divisibility_second[k]
            mobius_unoriented += term
            mobius_term_by_k[k] += term

    if mobius_unoriented != coprime_unoriented_direct:
        raise ArithmeticError(
            f"Mobius joint identity failed at B={bound}: "
            f"{mobius_unoriented} != {coprime_unoriented_direct}"
        )

    primitive_distinct_oriented = 2 * (
        coprime_unoriented_direct - repeated_primitive_unoriented
    )
    selected = [record for key, record in stage11_records.items() if key[3] <= bound]
    stage11_primitive_oriented = sum(int(r["oriented_chain_count"]) for r in selected)
    if primitive_distinct_oriented != stage11_primitive_oriented:
        raise ArithmeticError(
            f"primitive joint identity failed at B={bound}: "
            f"{primitive_distinct_oriented} != {stage11_primitive_oriented}"
        )

    top_scales = [
        {"g": g, "primitive_compatible_unoriented_pairs": count}
        for g, count in gcd_scale_contribution.most_common(12)
    ]
    top_mobius = [
        {"k": k, "signed_term": value}
        for k, value in sorted(
            mobius_term_by_k.items(), key=lambda item: abs(item[1]), reverse=True
        )[:12]
    ]
    return {
        "B": bound,
        "raw_oriented_chains": 2 * raw_unoriented,
        "coprime_joint_oriented_before_distinctness": 2 * coprime_unoriented_direct,
        "repeated_side_oriented_correction": 2 * repeated_primitive_unoriented,
        "primitive_distinct_oriented": primitive_distinct_oriented,
        "stage11_primitive_oriented": stage11_primitive_oriented,
        "finite_raw_to_primitive_ratio": (
            primitive_distinct_oriented / (2 * raw_unoriented) if raw_unoriented else 0.0
        ),
        "top_first_triangle_scales": top_scales,
        "top_mobius_terms": top_mobius,
    }


def build_report() -> dict[str, Any]:
    triangles, _, records, _ = enumerate_shared_p(MAX_D)
    spf = build_spf(MAX_D)
    mu = mobius_sieve(MAX_D)
    first_by_p = build_first_representations(triangles)
    scale_check = check_scale_decomposition(first_by_p, spf)
    rows = [bound_row(B, triangles, first_by_p, records, spf, mu) for B in THRESHOLDS]

    return {
        "metadata": {
            "stage": "12-N1b",
            "title": "Primitive-compatible shared-p joint weight",
            "generated_by": "scripts/audit_shared_p_primitive_joint_stage12_n1b.py",
            "claim_status": (
                "The gcd reduction, primitive-scale decomposition, Mobius joint identity, "
                "and finite cross-checks are exact. No asymptotic estimate is claimed."
            ),
        },
        "exact_lemmas": {
            "gcd_reduction": "gcd(x,y,c)=gcd(gcd(x,y),c)",
            "primitive_criterion": "the joined cuboid is primitive iff gcd(g,c)=1",
            "scale_decomposition": scale_check,
            "joint_weight": (
                "J_B(p)=sum_{(x,y):x<y,x^2+y^2=p^2} "
                "sum_{(c,d):p^2+c^2=d^2,d<=B} 1_{gcd(gcd(x,y),c)=1}"
            ),
            "mobius_form": (
                "J_B(p)=sum_{k>=1}mu(k)A_k(p)B_{k,B}(p), "
                "A_k=#{first reps:k|gcd(x,y)}, B_k=#{second reps:k|c}"
            ),
            "oriented_identity": (
                "C_prim(B)=2*sum_{p<=B}J_B(p)-R_equal(B), "
                "where R_equal removes c=x or c=y"
            ),
        },
        "finite_rows": rows,
        "decision": {
            "confirmed": [
                "The primitive correction closes exactly as a coprimality joint weight.",
                "The first-triangle scale g is separated by primitive hypotenuse counts P(p/g).",
                "Mobius inversion reproduces the direct primitive-compatible count at every audited bound.",
                "After the equal-side correction, the result reproduces the Stage11 primitive oriented count exactly.",
            ],
            "not_claimed": [
                "An asymptotic formula for the primitive-compatible joint weight.",
                "A Stage11-improving lower bound for N1(B).",
                "That the finite raw-to-primitive ratio converges.",
                "Any upper bound for N2(B).",
            ],
            "next_question": (
                "Can the averages of A_k(p)B_{k,B}(p), uniformly in squarefree k, "
                "be bounded strongly enough to obtain a primitive N1 lower bound beyond B^(1/2)?"
            ),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()
    report = build_report()
    args.write_report.parent.mkdir(parents=True, exist_ok=True)
    args.write_report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["decision"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
