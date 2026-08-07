#!/usr/bin/env python3
"""Stage12-N1d: audit whether the shared-p branch is ready for standard mean-value theorems.

This is a structural and finite audit. It does not claim an asymptotic formula.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

from audit_shared_p_convolution_stage11 import MAX_D, THRESHOLDS, build_spf, enumerate_shared_p, factor_with_spf
from audit_shared_p_primitive_joint_stage12_n1b import mobius_sieve

DEFAULT_REPORT = Path("data/shared_p_analytic_exit_stage12_n1d_report.json")


def prefix(values: list[int]) -> list[int]:
    out = [0] * len(values)
    total = 0
    for i, value in enumerate(values):
        total += value
        out[i] = total
    return out


def h_formula(p: int, spf: list[int]) -> int:
    if p < 2:
        return 0
    product = 1
    for q, exponent in factor_with_spf(p, spf):
        if q % 4 == 1:
            product *= 2 * exponent + 1
    return (product - 1) // 2


def build_report() -> dict[str, Any]:
    triangles, _, records, _ = enumerate_shared_p(MAX_D)
    spf = build_spf(MAX_D)
    mu = mobius_sieve(MAX_D)

    raw_distinct_exact = [0] * (MAX_D + 1)
    primitive_exact = [0] * (MAX_D + 1)
    for x in range(1, MAX_D + 1):
        for y, p, _, _ in triangles[x]:
            for c, d, _, _ in triangles[p]:
                if len({x, y, c}) == 3:
                    raw_distinct_exact[d] += 1
    for (_, _, _, d), record in records.items():
        primitive_exact[d] += int(record["oriented_chain_count"])

    raw_distinct = prefix(raw_distinct_exact)
    primitive = prefix(primitive_exact)
    h = [h_formula(p, spf) for p in range(MAX_D + 1)]

    multiplicativity_samples = 0
    h_violations = 0
    h_examples: list[dict[str, int]] = []
    for a in range(2, 120):
        for b in range(2, 120):
            if a * b > MAX_D or math.gcd(a, b) != 1:
                continue
            multiplicativity_samples += 1
            if h[a * b] != h[a] * h[b]:
                h_violations += 1
                if len(h_examples) < 8:
                    h_examples.append({"a": a, "b": b, "H_a": h[a], "H_b": h[b], "H_ab": h[a * b]})

    threshold_rows = []
    l_nonmultiplicativity = []
    f_nonmultiplicativity = []
    for B in THRESHOLDS:
        l = [0] * (B + 1)
        for p in range(1, B + 1):
            l[p] = sum(1 for _, d, _, _ in triangles[p] if d <= B)
        samples = l_violations = f_violations = 0
        l_example = f_example = None
        for a in range(2, min(100, B + 1)):
            for b in range(2, min(100, B + 1)):
                if a * b > B or math.gcd(a, b) != 1:
                    continue
                samples += 1
                if l[a * b] != l[a] * l[b]:
                    l_violations += 1
                    if l_example is None:
                        l_example = {"a": a, "b": b, "L_a": l[a], "L_b": l[b], "L_ab": l[a * b]}
                fa, fb, fab = h[a] * l[a], h[b] * l[b], h[a * b] * l[a * b]
                if fab != fa * fb:
                    f_violations += 1
                    if f_example is None:
                        f_example = {"a": a, "b": b, "F_a": fa, "F_b": fb, "F_ab": fab}
        l_nonmultiplicativity.append({"B": B, "samples": samples, "violations": l_violations, "example": l_example})
        f_nonmultiplicativity.append({"B": B, "samples": samples, "violations": f_violations, "example": f_example})

        mobius_value = sum(mu[k] * raw_distinct[B // k] for k in range(1, B + 1))
        if mobius_value != primitive[B]:
            raise ArithmeticError(f"Mobius inversion mismatch at B={B}: {mobius_value} != {primitive[B]}")
        threshold_rows.append({
            "B": B,
            "distinct_raw_oriented": raw_distinct[B],
            "primitive_oriented": primitive[B],
            "finite_retention": primitive[B] / raw_distinct[B] if raw_distinct[B] else None,
            "sum_1_over_k": sum(1.0 / k for k in range(1, B + 1)),
            "sum_1_over_sqrt_k": sum(1.0 / math.sqrt(k) for k in range(1, B + 1)),
            "mobius_reconstruction": mobius_value,
        })

    return {
        "metadata": {
            "stage": "12-N1d",
            "title": "Analytic exit audit for the shared-p branch",
            "generated_by": "scripts/audit_shared_p_analytic_exit_stage12_n1d.py",
            "claim_status": "Finite structural checks are exact; no asymptotic theorem is claimed.",
        },
        "structural_checks": {
            "H_multiplicativity": {
                "samples": multiplicativity_samples,
                "violations": h_violations,
                "examples": h_examples,
                "conclusion": "H is not multiplicative as defined; an affine multiplicative transform must be used instead.",
            },
            "L_B_multiplicativity": l_nonmultiplicativity,
            "H_times_L_B_multiplicativity": f_nonmultiplicativity,
            "height_coupling": "L_B(p) depends on p and B through d<=B; it is not a fixed one-variable coefficient sequence.",
            "global_mobius": "Exact at every audited threshold.",
        },
        "finite_rows": threshold_rows,
        "theorem_applicability": {
            "ordinary_euler_product_for_H_times_L": False,
            "direct_wirsing_delange_halasz_application": False,
            "reason": "F_B(p)=H(p)L_B(p) is B-dependent and nonmultiplicative.",
            "what_would_be_sufficient": [
                "A uniform asymptotic C_distinct_raw(X)=M(X)+R(X) for X=floor(B/k).",
                "A positive Mobius transform of the main term larger than B^(1/2).",
                "An error estimate with sum_{k<=B}|R(floor(B/k))| lower order, or signed Mobius cancellation.",
                "Separate control of repeated-side chains if their general absence is not proved.",
            ],
        },
        "decision": {
            "classification": "B_new_analytic_input_required",
            "confirmed": [
                "The algebraic primitive correction is closed by Stage12-N1c.",
                "The remaining coefficient is not an ordinary fixed multiplicative function.",
                "Wirsing, Delange, and Halasz cannot be invoked directly on H(p)L_B(p).",
                "The remaining problem is a uniform two-parameter divisor/hyperbola estimate followed by Mobius inversion.",
            ],
            "not_claimed": [
                "That no future analytic method can improve N1(B).",
                "An asymptotic formula for C_distinct_raw(B).",
                "A lower bound beyond N1(B)>>B^(1/2).",
            ],
            "branch_judgment": "Further progress requires genuinely new analytic input rather than another finite audit or direct use of standard multiplicative-function theorems.",
            "recommended_next_step": "Pause N1 after external review, then compare its cost with the N2 branches.",
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
