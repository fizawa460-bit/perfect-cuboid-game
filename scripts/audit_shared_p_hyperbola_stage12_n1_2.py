#!/usr/bin/env python3
"""Stage12-N1-2: exact hyperbola reparameterization of the shared-p convolution.

This audit rewrites the second Pythagorean triple

    p^2 + c^2 = d^2

through the unique parameters

    u=d-c=h*r^2,  v=d+c=h*s^2,
    gcd(r,s)=1, r<s, p=h*r*s,
    d=h*(r^2+s^2)/2.

It then verifies the exact weighted identity

    C_raw(B) = sum_{(h,r,s) in D_B} (G(h*r*s)-1),

where G(n)=2H(n)+1 is multiplicative and D_B is the parity/height domain.
No asymptotic estimate is claimed.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
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
    """Return G(n)=prod_{q == 1 mod 4}(2*v_q(n)+1)=2H(n)+1."""
    value = 1
    for prime, exponent in factor_with_spf(n, spf):
        if prime % 4 == 1:
            value *= 2 * exponent + 1
    return value


def second_triangle_to_hyperbola(p: int, c: int, d: int) -> tuple[int, int, int]:
    u = d - c
    v = d + c
    h = math.gcd(u, v)
    ur = u // h
    vr = v // h
    r = math.isqrt(ur)
    s = math.isqrt(vr)
    if r * r != ur or s * s != vr:
        raise ArithmeticError("coprime quotient pair is not a pair of squares")
    if not (r < s and math.gcd(r, s) == 1):
        raise ArithmeticError("hyperbola normalization failed")
    if p != h * r * s:
        raise ArithmeticError("shared diagonal recovery failed")
    if 2 * d != h * (r * r + s * s):
        raise ArithmeticError("height recovery failed")
    if 2 * c != h * (s * s - r * r):
        raise ArithmeticError("remaining leg recovery failed")
    return h, r, s


def build_report() -> dict[str, Any]:
    triangles, hypotenuse_counts, _, _ = enumerate_shared_p(MAX_D)
    spf = build_spf(MAX_D)

    g_multiplicativity_samples = 0
    g_multiplicativity_violations = 0
    for a in range(1, 150):
        for b in range(1, 150):
            if a * b > MAX_D or math.gcd(a, b) != 1:
                continue
            g_multiplicativity_samples += 1
            if g_weight(a * b, spf) != g_weight(a, spf) * g_weight(b, spf):
                g_multiplicativity_violations += 1

    rows: list[dict[str, Any]] = []
    total_bijection_checks = 0
    total_weight_checks = 0

    for bound in THRESHOLDS:
        direct_raw = 0
        hyperbola_weighted = 0
        hyperbola_unweighted = 0
        scale_hist: Counter[int] = Counter()
        gcd_h_rs_hist: Counter[int] = Counter()
        parity_hist: Counter[str] = Counter()
        max_scale = 0

        for p in range(1, bound + 1):
            h_count = hypotenuse_counts.get(p, 0)
            expected_g = 2 * hypotenuse_count_formula(p, spf) + 1
            actual_g = g_weight(p, spf)
            if actual_g != expected_g:
                raise ArithmeticError(f"G=2H+1 mismatch at p={p}")

            for c, d, _, _ in triangles[p]:
                if d > bound:
                    continue
                h, r, s = second_triangle_to_hyperbola(p, c, d)
                total_bijection_checks += 1
                if h * (r * r + s * s) > 2 * bound:
                    raise ArithmeticError("height-domain condition failed")
                if (h * (r * r + s * s)) & 1:
                    raise ArithmeticError("parity-domain condition failed")

                direct_raw += 2 * h_count
                contribution = actual_g - 1
                hyperbola_weighted += contribution
                hyperbola_unweighted += 1
                total_weight_checks += 1

                scale_hist[h] += contribution
                gcd_h_rs_hist[math.gcd(h, r * s)] += contribution
                max_scale = max(max_scale, h)
                parity_hist[
                    "h_even" if h % 2 == 0 else "h_odd_rs_opposite_parity"
                ] += contribution

        if direct_raw != hyperbola_weighted:
            raise ArithmeticError(
                f"weighted hyperbola identity failed at B={bound}: "
                f"{direct_raw} != {hyperbola_weighted}"
            )

        top_scales = [
            {"h": h, "weighted_contribution": value}
            for h, value in scale_hist.most_common(12)
        ]
        rows.append(
            {
                "B": bound,
                "raw_oriented_chains": direct_raw,
                "hyperbola_weighted_sum": hyperbola_weighted,
                "second_triangle_parameter_points": hyperbola_unweighted,
                "max_scale_h": max_scale,
                "top_scale_contributions": top_scales,
                "gcd_h_rs_weighted_histogram": {
                    str(key): value for key, value in sorted(gcd_h_rs_hist.items())
                },
                "parity_weighted_histogram": dict(sorted(parity_hist.items())),
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
            "weighted_identity": (
                "C_raw(B)=sum_{D_B}(G(h*r*s)-1), "
                "G(n)=prod_{q=1 mod 4}(2*v_q(n)+1)=2H(n)+1"
            ),
        },
        "multiplicative_transform": {
            "G_is_multiplicative": g_multiplicativity_violations == 0,
            "samples": g_multiplicativity_samples,
            "violations": g_multiplicativity_violations,
            "note": (
                "The weight G is multiplicative, but the domain couples h,r,s through "
                "h*(r^2+s^2)<=2B and h may share primes with r*s."
            ),
        },
        "finite_rows": rows,
        "audit_counts": {
            "bijection_checks": total_bijection_checks,
            "weight_checks": total_weight_checks,
        },
        "analytic_target": {
            "exact_sum": (
                "sum_{h>=1} sum_{r<s,(r,s)=1, parity, h(r^2+s^2)<=2B} "
                "(G(h*r*s)-1)"
            ),
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
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()
    report = build_report()
    args.write_report.parent.mkdir(parents=True, exist_ok=True)
    args.write_report.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report["analytic_target"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
