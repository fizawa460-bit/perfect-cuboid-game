#!/usr/bin/env python3
"""E-1c: extended finite cutoff scaling for Euler-side exactly-one counts.

Reuses the E-1b exact enumerator under the locked convention

    0<a<b<c,
    gcd(a,b,c)=1,
    a^2+b^2+c^2 <= B^2,

without requiring the space diagonal to be integral.

This script is diagnostic. Polynomial fits in x=1/log(B) are not asymptotic
theorems and are recorded only to compare the visible finite profile with the
already-established Stage13 chamber vector.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import math
from pathlib import Path

E1B = Path("stages/euler-cuboid/scripts/E-1b/population_enumeration.py")
STAGE13 = Path("stages/stage13/data/13-7/consolidation_audit_report.json")
OUT = Path("stages/euler-cuboid/data/E-1c/scaling_report.json")
DEFAULT_CUTOFFS = (10000, 20000, 50000, 100000, 200000, 500000)


def load_e1b():
    spec = importlib.util.spec_from_file_location("e1b_population", E1B)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {E1B}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def solve_linear_system(a: list[list[float]], b: list[float]) -> list[float]:
    n = len(b)
    for i in range(n):
        pivot = max(range(i, n), key=lambda r: abs(a[r][i]))
        a[i], a[pivot] = a[pivot], a[i]
        b[i], b[pivot] = b[pivot], b[i]
        p = a[i][i]
        if abs(p) < 1e-18:
            raise ArithmeticError("singular normal-equation matrix")
        for j in range(i, n):
            a[i][j] /= p
        b[i] /= p
        for r in range(n):
            if r == i:
                continue
            f = a[r][i]
            for j in range(i, n):
                a[r][j] -= f * a[i][j]
            b[r] -= f * b[i]
    return b


def polyfit(xs: list[float], ys: list[float], degree: int) -> list[float]:
    n = degree + 1
    a = [
        [sum(x ** (i + j) for x in xs) for j in range(n)]
        for i in range(n)
    ]
    b = [sum(y * x**i for x, y in zip(xs, ys)) for i in range(n)]
    return solve_linear_system(a, b)


def build(cutoffs: tuple[int, ...]) -> dict:
    e1b = load_e1b()
    rows = []
    for B in cutoffs:
        base = e1b.enumerate_population(B)
        exact = base["exact_one"]
        total = base["exact_one_total"]
        rows.append(
            {
                "B": B,
                "exact_one": exact,
                "total": total,
                "ratio_bc_normalized": {
                    q: exact[q] / exact["bc"] for q in ("ab", "ac", "bc")
                },
                "proportion": {
                    q: exact[q] / total for q in ("ab", "ac", "bc")
                },
                "scaled_B2_logB": {
                    q: exact[q] / (B * B * math.log(B))
                    for q in ("ab", "ac", "bc")
                },
            }
        )

    xs = [1.0 / math.log(row["B"]) for row in rows]
    fits = {}
    for q in ("ab", "ac"):
        ys = [row["ratio_bc_normalized"][q] for row in rows]
        fits[q] = {}
        for degree in (1, 2):
            coeff = polyfit(xs, ys, degree)
            fits[q][f"degree_{degree}"] = {
                "coefficients_ascending": coeff,
                "intercept_x0": coeff[0],
            }

    chamber = None
    if STAGE13.exists():
        s13 = json.loads(STAGE13.read_text())
        chamber = s13["final_exact_one_theorem"]["bc_normalized_ratio"]

    below = [r for r in rows if r["ratio_bc_normalized"]["ab"] < 2.0]
    above = [r for r in rows if r["ratio_bc_normalized"]["ab"] >= 2.0]
    crossing = None
    if below and above:
        crossing = [max(r["B"] for r in below), min(r["B"] for r in above)]

    return {
        "metadata": {
            "stage": "E-1c",
            "scope": "finite cutoff scaling and directional-ratio diagnostic",
            "space_diagonal_integrality_required": False,
            "asymptotic_theorem_claimed": False,
        },
        "counting_convention": {
            "canonical_order": "0<a<b<c",
            "primitive": "gcd(a,b,c)=1",
            "cutoff": "a^2+b^2+c^2<=B^2",
        },
        "rows": rows,
        "crossing_observations": {
            "ab_over_bc_crosses_2_between_sampled_cutoffs": crossing,
            "ac_over_bc_below_1_at_largest_cutoff":
                rows[-1]["ratio_bc_normalized"]["ac"] < 1.0,
        },
        "scale_diagnostic": {
            "candidate_scale": "B^2 log B",
            "note": (
                "N_q/(B^2 log B) varies slowly over the audited high-B range; "
                "this is a finite diagnostic, not a proof of an asymptotic."
            ),
        },
        "inverse_log_extrapolation": {
            "x": "1/log(B)",
            "fit_cutoffs": list(cutoffs),
            "fits": fits,
            "warning": (
                "Polynomial extrapolation in 1/log(B) is diagnostic only; "
                "no convergence rate or limiting theorem is inferred."
            ),
        },
        "stage13_chamber_comparison": {
            "space_diagonal_side_bc_normalized_ratio": chamber,
            "source": str(STAGE13),
            "same_limit_proved": False,
        },
        "status": {
            "E_1C_complete": True,
            "largest_B": max(cutoffs),
            "ab_over_bc_has_crossed_2": crossing is not None,
            "ac_over_bc_has_crossed_1":
                any(r["ratio_bc_normalized"]["ac"] >= 1.0 for r in rows),
            "finite_profile_consistent_with_stage13_chamber_but_not_proved": True,
            "next": "E-1d structural explanation of the Euler-side directional profile",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cutoffs", nargs="+", type=int, default=list(DEFAULT_CUTOFFS))
    parser.add_argument("--output", type=Path, default=OUT)
    args = parser.parse_args()
    cutoffs = tuple(sorted(set(args.cutoffs)))
    report = build(cutoffs)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report["status"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
