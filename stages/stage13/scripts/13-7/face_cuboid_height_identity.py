#!/usr/bin/env python3
"""Exact finite validator for the Stage13-7jd rational-height algebra.

This does not test Dujella's theorem.  It independently checks the algebraic
Yoshida inversion and the elementary projective-height majorants used to feed
that theorem.
"""
from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path

OUT = Path("stages/stage13/data/13-7/face_cuboid_height_identity_report.json")


def height(q: Fraction) -> int:
    return max(abs(q.numerator), q.denominator)


def projective_curve_height(s: Fraction) -> int:
    u, v = s.numerator, s.denominator
    coords = [
        v**6,
        v**2 * (u**4 - 6*u*u*v*v + v**4),
        -4*u*u*(u*u-v*v)**2,
        0,
    ]
    g = 0
    for z in coords:
        g = math.gcd(g, abs(z))
    coords = [z // g for z in coords]
    return max(abs(z) for z in coords)


def build_report() -> dict:
    cases = 0
    inversion_failures = 0
    alpha_height_failures = 0
    curve_height_failures = 0
    max_alpha_ratio = 0.0
    max_curve_ratio = 0.0

    for S in range(2, 31):
        for u in range(1, S + 1):
            for v in range(1, S + 1):
                if max(u, v) != S or math.gcd(u, v) != 1:
                    continue
                s = Fraction(u, v)
                if s in (Fraction(1), Fraction(-1), Fraction(0)):
                    continue
                for T in range(2, 21):
                    for m in range(1, T + 1):
                        for n in range(1, T + 1):
                            if max(m, n) != T or math.gcd(m, n) != 1:
                                continue
                            t = Fraction(m, n)
                            if t == s:
                                continue

                            alpha = 2*s*(s*s-1)*(1+s*t)/(s-t)
                            recovered = (
                                s*alpha - 2*s*(s*s-1)
                            ) / (
                                alpha + 2*s*s*(s*s-1)
                            )
                            if recovered != t:
                                inversion_failures += 1

                            alpha_bound = 4 * height(s)**4 * height(t)
                            if height(alpha) > alpha_bound:
                                alpha_height_failures += 1
                            max_alpha_ratio = max(
                                max_alpha_ratio, height(alpha) / alpha_bound
                            )

                            curve_bound = 8 * height(s)**6
                            curve_height = projective_curve_height(s)
                            if curve_height > curve_bound:
                                curve_height_failures += 1
                            max_curve_ratio = max(
                                max_curve_ratio, curve_height / curve_bound
                            )
                            cases += 1

    if inversion_failures or alpha_height_failures or curve_height_failures:
        raise ArithmeticError(
            (inversion_failures, alpha_height_failures, curve_height_failures)
        )

    return {
        "metadata": {
            "stage": "13-7jd",
            "scope": "finite exact validation of the algebraic height-transfer identities",
        },
        "ranges": {
            "H_s_max": 30,
            "H_t_max": 20,
            "coprime_positive_reduced_pairs_only": True,
            "s_equal_t_skipped_as_degenerate": True,
        },
        "checks": {
            "cases": cases,
            "yoshida_inversion_failures": inversion_failures,
            "alpha_height_bound_failures": alpha_height_failures,
            "curve_height_bound_failures": curve_height_failures,
            "max_H_alpha_over_4Hs4Ht": max_alpha_ratio,
            "max_H_curve_over_8Hs6": max_curve_ratio,
        },
        "identities": {
            "alpha": "2*s*(s^2-1)*(1+s*t)/(s-t)",
            "alpha_height": "H(alpha)<=4 H(s)^4 H(t)",
            "curve_height": "H(E_{1,s})<=8 H(s)^6",
        },
        "status": "PASS",
    }


def main() -> None:
    report = build_report()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report["checks"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
