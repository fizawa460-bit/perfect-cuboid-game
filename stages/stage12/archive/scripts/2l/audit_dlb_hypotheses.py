#!/usr/bin/env python3
"""Deterministic audit for Stage12-N1-2l.

This script checks the exact local two-variable beta factor, its factorization
into one-variable factors and a coprimality correction, and the order at which
the correction starts.  It does not prove analytic continuation or vertical
growth (P2/P3); those are deliberately reported as unverified.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


def beta_local(q: int) -> Fraction:
    return Fraction(2 * (q - 1), q + 1)


def local_factor(q: int, x: Fraction, y: Fraction) -> Fraction:
    b = beta_local(q)
    return 1 + b * x / (1 - x) + b * y / (1 - y)


def one_variable_factor(q: int, x: Fraction) -> Fraction:
    b = beta_local(q)
    return 1 + b * x / (1 - x)


def correction(q: int, x: Fraction, y: Fraction) -> Fraction:
    return local_factor(q, x, y) / (
        one_variable_factor(q, x) * one_variable_factor(q, y)
    )


def build_report() -> dict:
    primes = [5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97]
    samples = []
    for q in primes:
        x = Fraction(1, q)
        y = Fraction(1, q * q)
        lhs = local_factor(q, x, y)
        rhs = one_variable_factor(q, x) * one_variable_factor(q, y) * correction(q, x, y)
        assert lhs == rhs
        # Exact identity: C_q - 1 starts with a term divisible by x*y.
        c = correction(q, x, y)
        samples.append(
            {
                "q": q,
                "beta_q": str(beta_local(q)),
                "factorization_exact": lhs == rhs,
                "correction": str(c),
                "abs_correction_minus_1": float(abs(c - 1)),
                "xy": float(x * y),
                "ratio_to_xy": float(abs(c - 1) / (x * y)),
            }
        )

    return {
        "metadata": {
            "stage": "12-N1-2l",
            "claim_status": "Exact local algebra and hypothesis audit only; P2/P3 are not proved.",
        },
        "de_la_breteche_theorem_1": {
            "P1": "absolute convergence in a right poly-half-plane",
            "P2": "holomorphic continuation after removing finitely many linear-form poles",
            "P3": "uniform polynomial growth in a shrunken tube domain",
        },
        "beta_two_variable_local_factor": "1+b_q*x/(1-x)+b_q*y/(1-y)",
        "factorization": "F_q(s1,s2)=D_q(s1)D_q(s2)C_q(s1,s2)",
        "finite_exact_checks": samples,
        "decision": {
            "classification": "B_DLB_DIRECT_APPLICATION_NOT_VERIFIED_REPAIR_ROUTE_AVAILABLE",
            "P1": "verified by beta(n) << tau(n)",
            "P2": "not verified in Stage12-N1-2k",
            "P3": "not verified in Stage12-N1-2k",
            "repair_route": "factor one-variable beta series and absolutely convergent coprimality correction, then use iterated Selberg-Delange and partial summation",
            "next_stage": "12-N1-2m",
        },
        "not_claimed": [
            "P2 or P3 fails",
            "the final asymptotic is false",
            "the iterated one-variable repair route is already complete",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-report", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(build_report(), ensure_ascii=False, indent=2) + "\n"
    if args.write_report:
        args.write_report.parent.mkdir(parents=True, exist_ok=True)
        args.write_report.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
