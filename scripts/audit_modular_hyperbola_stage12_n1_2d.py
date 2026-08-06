#!/usr/bin/env python3
"""Stage12-N1-2d: audit modular-hyperbola estimates against the shared-p sum.

This is a theorem-hypothesis and exponent-budget audit. It does not prove an
asymptotic formula. The central check is whether pointwise modular-hyperbola
errors remain useful after summing over h-slices, divisor moduli, and the later
global Mobius inversion.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

DEFAULT_REPORT = Path("data/modular_hyperbola_stage12_n1_2d_report.json")


def aggregate_exponent(theta: float) -> float:
    """Return the B exponent in the naive absolute h/modulus error sum.

    With R_h=(2B/h)^(1/2), model the error by

        sum_{h<=2B} sum_{m<=R_h} m^theta.

    For -1 < theta < 1 this has exponent 1 after absolute summation.
    """
    if not -1.0 < theta < 1.0:
        raise ValueError("theta must satisfy -1 < theta < 1")
    alpha = (theta + 1.0) / 2.0
    return alpha + (1.0 - alpha)


def build_report() -> dict:
    checks = [
        {
            "feature": "congruence_geometry",
            "modular_hyperbola": "x*y=a mod m",
            "stage12": "divisor expansions lead to r^2+s^2=0 mod m; after gcd(s,m)=1 this is t^2=-1 mod m",
            "status": "indirect_only",
            "reason": "The relevant quadratic roots form a thin diagonal-type restriction, not the two-dimensional hyperbola population controlled by Theorem 13.",
        },
        {
            "feature": "composite_moduli",
            "modular_hyperbola": "Theorem 13 covers arbitrary m for the product congruence; generic-curve substitution is most direct for prime moduli.",
            "stage12": "divisor variables naturally include arbitrary composite moduli",
            "status": "major_mismatch",
        },
        {
            "feature": "summation_region",
            "modular_hyperbola": "boxes have O(m^(1/2+o(1))) error; a quarter-disk consequence has O(m^(3/4+o(1))) error",
            "stage12": "ordered coprime sector inside r^2+s^2<=2B/h",
            "status": "partial_match_with_error_loss",
        },
        {
            "feature": "coprimality",
            "modular_hyperbola": "visible-point restrictions can be introduced by Mobius inversion in related problems",
            "stage12": "gcd(r,s)=1 is mandatory before the later global primitive correction",
            "status": "structurally_manageable_but_uniformity_unproved",
        },
        {
            "feature": "arithmetic_weight",
            "modular_hyperbola": "Theorem 13 is an unweighted count; the survey lists further arithmetic-function sums as a separate problem",
            "stage12": "G(h)G(r)G(s)-1",
            "status": "not_supplied",
        },
        {
            "feature": "shared_prime_correction",
            "modular_hyperbola": "no factor coupling an external h variable to prime divisors of r*s",
            "stage12": "K(h,rs) is supported on shared primes q=1 mod4",
            "status": "not_supplied",
        },
        {
            "feature": "average_over_moduli",
            "modular_hyperbola": "pointwise in m; improving the box formula on average over m is posed as Question 15",
            "stage12": "divisor decomposition and h-slicing require simultaneous summation over many moduli",
            "status": "missing_key_uniformity",
        },
        {
            "feature": "global_mobius_inversion",
            "modular_hyperbola": "no built-in error budget for a second outer Mobius sum over rescaled heights",
            "stage12": "the final error must remain summable for X=floor(B/k)",
            "status": "not_supplied",
        },
    ]
    cases = [
        {
            "input": "box discrepancy error",
            "theta": 0.5,
            "aggregate_exponent": aggregate_exponent(0.5),
        },
        {
            "input": "curved-domain discrepancy error",
            "theta": 0.75,
            "aggregate_exponent": aggregate_exponent(0.75),
        },
    ]
    if any(case["aggregate_exponent"] != 1.0 for case in cases):
        raise AssertionError("naive exponent budget must aggregate to B^1")

    return {
        "metadata": {
            "stage": "12-N1-2d",
            "title": "Modular-hyperbola uniform-error audit",
            "generated_by": "scripts/audit_modular_hyperbola_stage12_n1_2d.py",
            "source": "Shparlinski, Modular Hyperbolas, arXiv:1103.2879 (Theorem 13, (10), circle-domain consequence, Questions 15 and 31)",
            "claim_status": "Compatibility and exponent-budget audit only; no asymptotic theorem claimed.",
        },
        "target_sum": {
            "formula": "sum_{h(r^2+s^2)<=2B, r<s, gcd(r,s)=1} (G(h)G(r)G(s)K(h,rs)-1)",
            "required_output": "an h-uniform error that remains summable after divisor expansions and the later global Mobius inversion",
            "origin": "Stage12-N1-2b exact factorization and Stage12-N1-2c literature audit",
        },
        "candidate_input": {
            "object": "H_{a,m}={(x,y): x*y=a mod m}, gcd(a,m)=1",
            "interval_count": "phi(m)*X*Y/m^2 + O(m^(1/2+o(1)))",
            "curved_domain_example": "quarter-disk main term + O(m^(3/4+o(1)))",
            "scope": [
                "unweighted point counts",
                "one fixed modulus at a time",
                "invertible residue a",
                "boxes or regular planar domains via discrepancy",
            ],
        },
        "compatibility_checks": checks,
        "naive_error_budget": {
            "slice_radius": "R_h=(2B/h)^(1/2)",
            "model": "sum_{h<=2B} sum_{m<=R_h} m^theta",
            "derivation": "For -1<theta<1, the absolute sum is B^((theta+1)/2) * sum_{h<=B} h^(-(theta+1)/2) = B^(1+o(1)).",
            "cases": cases,
            "interpretation": "Naively summing pointwise modulus errors gives no power saving over B. Cancellation, a restricted modulus range, or an averaged large-sieve estimate is still required.",
            "caveat": "This is an exponent-budget obstruction, not a proved asymptotic or a lower bound for the true error.",
        },
        "decision": {
            "direct_application": False,
            "classification": "B_local_distribution_template_relevant_not_sufficient",
            "reusable_components": [
                "Kloosterman completion for unweighted inverse/product congruences",
                "discrepancy transfer from boxes to regular planar domains",
                "Mobius visible-point reduction after an independently summable error is available",
            ],
            "insufficient_components": [
                "quadratic-root counts t^2=-1 mod m on composite moduli",
                "the multiplicative weights G(h)G(r)G(s)",
                "the shared-prime correction K(h,rs)",
                "cancellation averaged over h and divisor moduli",
                "an error term stable under the later global Mobius inversion",
            ],
            "next_stage": "12-N1-2e: expand G into divisor indicators and derive the exact dyadic h/modulus ranges and error budget needed from a large-sieve or two-square-correlation theorem",
        },
        "not_claimed": [
            "That modular-hyperbola estimates yield an asymptotic for the Stage12 sum.",
            "That the B^(1+o(1)) naive accumulated error is sharp.",
            "That K is lower order.",
            "That no stronger averaged Kloosterman or large-sieve input can close the gap.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()
    report = build_report()
    args.write_report.parent.mkdir(parents=True, exist_ok=True)
    args.write_report.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report["decision"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
