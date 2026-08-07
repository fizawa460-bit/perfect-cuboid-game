#!/usr/bin/env python3
"""Stage12-N1-2: exact hyperbola reparameterization of shared-p chains."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

from audit_shared_p_convolution_stage11 import (
    MAX_D,
    THRESHOLDS,
    build_spf,
    enumerate_shared_p,
    factor_with_spf,
    hypotenuse_count_formula,
)

DEFAULT_REPORT = Path("data/shared_p_hyperbola_stage12_n1_2_report.json")


def g_weight(n: int, spf: list[int]) -> int:
    value = 1
    for prime, exponent in factor_with_spf(n, spf):
        if prime % 4 == 1:
            value *= 2 * exponent + 1
    return value


def second_triangle_to_hyperbola(p: int, c: int, d: int) -> tuple[int, int, int]:
    u, v = d - c, d + c
    h = math.gcd(u, v)
    r, s = math.isqrt(u // h), math.isqrt(v // h)
    if r * r != u // h or s * s != v // h:
        raise ArithmeticError("coprime quotient pair is not a pair of squares")
    if not (r < s and math.gcd(r, s) == 1):
        raise ArithmeticError("hyperbola normalization failed")
    if p != h * r * s or 2 * c != h * (s * s - r * r):
        raise ArithmeticError("triangle recovery failed")
    if 2 * d != h * (r * r + s * s):
        raise ArithmeticError("height recovery failed")
    return h, r, s


def build_report() -> dict[str, Any]:
    triangles, hypotenuse_counts, _, _ = enumerate_shared_p(MAX_D)
    spf = build_spf(MAX_D)

    samples = violations = 0
    for a in range(1, 150):
        for b in range(1, 150):
            if a * b > MAX_D or math.gcd(a, b) != 1:
                continue
            samples += 1
            if g_weight(a * b, spf) != g_weight(a, spf) * g_weight(b, spf):
                violations += 1

    rows: list[dict[str, int]] = []
    checks = 0
    for bound in THRESHOLDS:
        direct_raw = weighted = parameter_points = max_scale = 0
        for p in range(1, bound + 1):
            h_count = hypotenuse_counts.get(p, 0)
            actual_g = g_weight(p, spf)
            if actual_g != 2 * hypotenuse_count_formula(p, spf) + 1:
                raise ArithmeticError(f"G=2H+1 mismatch at p={p}")
            for c, d, _, _ in triangles[p]:
                if d > bound:
                    continue
                h, r, s = second_triangle_to_hyperbola(p, c, d)
                if h * (r * r + s * s) > 2 * bound:
                    raise ArithmeticError("height-domain condition failed")
                if h * (r * r + s * s) & 1:
                    raise ArithmeticError("parity-domain condition failed")
                direct_raw += 2 * h_count
                weighted += actual_g - 1
                parameter_points += 1
                max_scale = max(max_scale, h)
                checks += 1
        if direct_raw != weighted:
            raise ArithmeticError(f"weighted identity failed at B={bound}")
        rows.append(
            {
                "B": bound,
                "raw_oriented_chains": direct_raw,
                "hyperbola_weighted_sum": weighted,
                "second_triangle_parameter_points": parameter_points,
                "max_scale_h": max_scale,
            }
        )

    return {
        "metadata": {
            "stage": "12-N1-2",
            "title": "Exact hyperbola coordinates for the shared-p convolution",
            "generated_by": "scripts/audit_shared_p_hyperbola_stage12_n1_2.py",
            "claim_status": "Exact finite identities only; no asymptotic formula is claimed.",
        },
        "exact_reparameterization": {
            "variables": "u=d-c=h*r^2, v=d+c=h*s^2",
            "conditions": [
                "h>=1",
                "1<=r<s",
                "gcd(r,s)=1",
                "p=h*r*s",
                "h*(r^2+s^2)<=2B",
                "h*(r^2+s^2) is even",
            ],
            "recovery": {
                "p": "h*r*s",
                "c": "h*(s^2-r^2)/2",
                "d": "h*(r^2+s^2)/2",
            },
            "weighted_identity": "C_raw(B)=sum_{D_B}(G(h*r*s)-1), G(n)=prod_{q=1 mod 4}(2*v_q(n)+1)=2H(n)+1",
        },
        "multiplicative_transform": {
            "G_is_multiplicative": violations == 0,
            "samples": samples,
            "violations": violations,
            "note": "The weight G is multiplicative, but the domain couples h,r,s through h*(r^2+s^2)<=2B and h may share primes with r*s.",
        },
        "finite_rows": rows,
        "audit_counts": {"bijection_checks": checks, "weight_checks": checks},
        "analytic_target": {
            "exact_sum": "sum_{h>=1} sum_{r<s,(r,s)=1, parity, h(r^2+s^2)<=2B} (G(h*r*s)-1)",
            "progress": [
                "The B-dependent function L_B(p) has been eliminated from the summand.",
                "The arithmetic weight is now the fixed multiplicative function G evaluated at h*r*s.",
                "All B-dependence is isolated in an explicit quadratic height domain.",
            ],
            "remaining_obstructions": [
                "Average G(h*r*s) over a coprime quadratic domain with h sharing primes with r*s.",
                "Separate or control repeated-side chains before applying the global Mobius inversion.",
                "Obtain an error term uniform enough for X=floor(B/k) across the Mobius range.",
            ],
            "classification": "A_reparameterization_progress_new_mean_value_lemma_needed",
        },
        "literature_leads": {
            "status": "candidate methods, not yet applied",
            "items": [
                {"work": "Gao-Zhao, Mean values of divisors of forms n^2+Nm^2 (2018)", "possible_use": "divisor averages on quadratic forms"},
                {"work": "Shparlinski, Modular Hyperbolas (2011)", "possible_use": "lattice-point and error estimates for hyperbolic divisor constraints"},
                {"work": "Chamizo, The additive problem for the number of representations as a sum of two squares (2020)", "possible_use": "correlation methods for representation functions"},
                {"work": "Zelator, A Non-Existence Property of Pythagorean Triangles with a 3-D Application (2009)", "possible_use": "structurally related chained triangles, not asymptotic counting"},
            ],
            "warning": "No direct theorem application or novelty claim is made from this bibliography alone.",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()
    report = build_report()
    args.write_report.parent.mkdir(parents=True, exist_ok=True)
    args.write_report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["analytic_target"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
