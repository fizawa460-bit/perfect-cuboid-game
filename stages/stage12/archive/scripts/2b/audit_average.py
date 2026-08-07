#!/usr/bin/env python3
"""Stage12-N1-2b: split G(h*r*s) into coprime product and overlap correction.

For G(n)=prod_{q=1 mod 4}(2*v_q(n)+1), gcd(r,s)=1 gives

  G(h*r*s)=G(h)G(r)G(s) K(h,r*s),

where K is an explicit product over primes q=1 mod 4 shared by h and r*s.
This audit verifies the identity on the Stage12-N1-2 hyperbola population and
measures, only finitely, how much of the weighted sum comes from shared primes.
No asymptotic density or mean-value theorem is claimed.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Any

from audit_shared_p_convolution_stage11 import MAX_D, THRESHOLDS, build_spf, enumerate_shared_p, factor_with_spf
from audit_shared_p_hyperbola_stage12_n1_2 import g_weight, second_triangle_to_hyperbola

DEFAULT_REPORT = Path("data/shared_p_average_stage12_n1_2b_report.json")


def exponent_map(n: int, spf: list[int]) -> dict[int, int]:
    return dict(factor_with_spf(n, spf))


def overlap_correction(h: int, t: int, spf: list[int]) -> Fraction:
    eh = exponent_map(h, spf)
    et = exponent_map(t, spf)
    value = Fraction(1, 1)
    for q in set(eh).intersection(et):
        if q % 4 != 1:
            continue
        a = eh[q]
        b = et[q]
        value *= Fraction(2 * (a + b) + 1, (2 * a + 1) * (2 * b + 1))
    return value


def build_report() -> dict[str, Any]:
    triangles, hypotenuse_counts, _, _ = enumerate_shared_p(MAX_D)
    spf = build_spf(MAX_D)
    rows: list[dict[str, Any]] = []
    identity_checks = 0

    for bound in THRESHOLDS:
        exact_sum = 0
        product_sum = 0
        correction_loss = 0
        exact_coprime_hrs = 0
        exact_shared_relevant = 0
        exact_shared_irrelevant_only = 0
        point_hist: Counter[str] = Counter()
        correction_hist: Counter[str] = Counter()

        for p in range(1, bound + 1):
            h_count = hypotenuse_counts.get(p, 0)
            if h_count == 0:
                continue
            for c, d, _, _ in triangles[p]:
                if d > bound:
                    continue
                h, r, s = second_triangle_to_hyperbola(p, c, d)
                t = r * s
                exact_g = g_weight(h * t, spf)
                separated_g = g_weight(h, spf) * g_weight(r, spf) * g_weight(s, spf)
                corr = overlap_correction(h, t, spf)
                if Fraction(separated_g, 1) * corr != exact_g:
                    raise ArithmeticError("overlap correction identity failed")
                if exact_g != 2 * h_count + 1:
                    raise ArithmeticError("G=2H+1 mismatch")
                identity_checks += 1

                exact_weight = exact_g - 1
                product_weight = separated_g - 1
                exact_sum += exact_weight
                product_sum += product_weight
                correction_loss += product_weight - exact_weight

                common = math.gcd(h, t)
                relevant_common = any(q % 4 == 1 for q in exponent_map(common, spf))
                if common == 1:
                    exact_coprime_hrs += exact_weight
                    point_hist["gcd(h,rs)=1"] += 1
                elif relevant_common:
                    exact_shared_relevant += exact_weight
                    point_hist["shared prime 1 mod 4"] += 1
                else:
                    exact_shared_irrelevant_only += exact_weight
                    point_hist["shared primes only 2 or 3 mod 4"] += 1
                correction_hist[f"{corr.numerator}/{corr.denominator}"] += 1

        if exact_sum != 2 * sum(
            hypotenuse_counts.get(p, 0)
            * sum(1 for _, d, _, _ in triangles[p] if d <= bound)
            for p in range(1, bound + 1)
        ):
            raise ArithmeticError("exact weighted sum did not reproduce Stage11")

        rows.append(
            {
                "B": bound,
                "exact_raw_weight": exact_sum,
                "naive_separated_weight": product_sum,
                "overlap_correction_loss": correction_loss,
                "naive_over_exact_ratio": product_sum / exact_sum if exact_sum else None,
                "exact_weight_by_overlap_class": {
                    "gcd_h_rs_1": exact_coprime_hrs,
                    "shared_prime_1_mod_4": exact_shared_relevant,
                    "shared_only_irrelevant_primes": exact_shared_irrelevant_only,
                },
                "point_class_histogram": dict(point_hist),
                "most_common_corrections": [
                    {"factor": key, "points": value}
                    for key, value in correction_hist.most_common(12)
                ],
            }
        )

    return {
        "metadata": {
            "stage": "12-N1-2b",
            "title": "Shared-prime correction for the multiplicative hyperbola weight",
            "generated_by": "scripts/audit_shared_p_average_stage12_n1_2b.py",
            "claim_status": "Exact factorization and finite diagnostics only; no asymptotic claim.",
        },
        "exact_factorization": {
            "formula": "G(h*r*s)=G(h)G(r)G(s)K(h,r*s), gcd(r,s)=1",
            "local_factor": "K_q=(2(a+b)+1)/((2a+1)(2b+1)) for q=1 mod4, a=v_q(h), b=v_q(rs)",
            "support": "Only primes q=1 mod4 dividing gcd(h,r*s) contribute to K.",
            "bounds": "0<K<=1, with K=1 iff no q=1 mod4 divides gcd(h,r*s).",
        },
        "finite_rows": rows,
        "audit_counts": {"exact_identity_checks": identity_checks},
        "analytic_consequence": {
            "progress": [
                "The failure of full separation is isolated in an explicit Euler-local correction K.",
                "Primes 2 and 3 mod4 shared by h and rs do not affect G and hence do not affect K.",
                "The naive product G(h)G(r)G(s) is an exact upper majorant for G(hrs).",
            ],
            "next_required_input": [
                "Average the product weight G(h)G(r)G(s) over the coprime quadratic domain.",
                "Control the aggregate loss from q=1 mod4 shared between h and rs.",
                "Retain an error term uniform under the later global Mobius inversion.",
            ],
            "classification": "A_local_correction_isolated_mean_value_still_open",
        },
        "not_claimed": [
            "That the finite overlap proportions have limits.",
            "That the correction loss is lower order.",
            "An asymptotic formula or a stronger N1 lower bound.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()
    report = build_report()
    args.write_report.parent.mkdir(parents=True, exist_ok=True)
    args.write_report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["analytic_consequence"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
