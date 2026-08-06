#!/usr/bin/env python3
"""Stage12-N1-2g: audit uniform fixed-modulus lattice remainders.

This audit separates the available route into:
1. ordinary lattice counting for an anisotropic ellipse sector,
2. Möbius inversion for visibility and local coprimality,
3. weighted averaging over the three divisor moduli.

It records the strongest conclusion justified by those ingredients without
claiming a new lattice-point theorem.  The central obstruction is that the
elementary pointwise boundary budget has the same B(log B)^4 logarithmic degree
as the formal raw main term.  Fixed-domain power-saving results are not uniform
over the unbounded eccentricity family b/c required by the leading term.
"""
from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

DEFAULT_REPORT = Path("data/uniform_error_stage12_n1_2g_report.json")
THRESHOLDS = [1_000, 2_000, 5_000, 10_000, 20_000, 50_000, 100_000, 200_000]
BALANCED_LOG_WIDTH = 1.0


def main_log_simplex(L: float) -> float:
    """Integral of the Stage12-N1-2f main logarithm over the modulus simplex."""
    return L**4 / 48.0


def modulus_simplex_volume(L: float) -> float:
    """Volume of x+2*max(y,z)<L in the nonnegative octant."""
    return L**3 / 12.0


def balanced_main_integral(L: float, K: float) -> float:
    """Main-log integral restricted by |log b-log c|<=K, for L/2>=K."""
    if L / 2.0 < K:
        raise ValueError("closed formula requires L/2 >= K")
    return (
        K * L**3 / 6.0
        - K**2 * L**2 / 2.0
        + 2.0 * K**3 * L / 3.0
        - K**4 / 3.0
    )


def outer_mobius_log_degree(raw_error_degree: float) -> float:
    """Absolute summation of X(log X)^beta adds one logarithmic degree."""
    return raw_error_degree + 1.0


def build_report() -> dict[str, Any]:
    if Fraction(1, 48) * 4 != Fraction(1, 12):
        raise AssertionError("simplex coefficient relation failed")

    rows: list[dict[str, float | int]] = []
    for B in THRESHOLDS:
        L = math.log(B)
        main_volume = main_log_simplex(L)
        modulus_volume = modulus_simplex_volume(L)
        elementary_error_log_model = L * modulus_volume
        balanced = balanced_main_integral(L, BALANCED_LOG_WIDTH)
        rows.append(
            {
                "B": B,
                "log_B": L,
                "main_log_simplex_L4_over_48": main_volume,
                "modulus_simplex_L3_over_12": modulus_volume,
                "elementary_boundary_log_model_L4_over_12": elementary_error_log_model,
                "elementary_model_over_formal_main": elementary_error_log_model / main_volume,
                "balanced_width_1_main_integral": balanced,
                "balanced_fraction_of_main": balanced / main_volume,
                "balanced_asymptotic_ratio_8_over_logB": 8.0 / L,
            }
        )
    if any(abs(float(row["elementary_model_over_formal_main"]) - 4.0) > 1e-12 for row in rows):
        raise AssertionError("elementary error model must have the same degree as the main term")
    if not all(
        float(rows[i + 1]["balanced_fraction_of_main"])
        < float(rows[i]["balanced_fraction_of_main"])
        for i in range(len(rows) - 1)
    ):
        raise AssertionError("fixed-width balanced shape fraction should decrease")

    return {
        "metadata": {
            "stage": "12-N1-2g",
            "title": "Uniform lattice-remainder compatibility audit",
            "generated_by": "scripts/audit_uniform_error_stage12_n1_2g.py",
            "claim_status": (
                "Exact exponent-budget and applicability audit only; "
                "no new lattice-point or asymptotic theorem claimed."
            ),
        },
        "target": {
            "fixed_modulus_count": (
                "N_{a,b,c}(B) for h=a*u, r=b*v, s=c*w in "
                "a*u*(b^2*v^2+c^2*w^2)<=2B, b*v<c*w, "
                "gcd(v,w)=gcd(v,c)=gcd(w,b)=1, with the Stage12 parity condition"
            ),
            "weighted_raw_error": (
                "E_raw(B)=sum lambda_1(a)lambda_1(b)lambda_1(c)"
                "*(N_{a,b,c}(B)-V_{a,b,c}(B))"
            ),
            "formal_raw_main": "B*(log B)^4",
            "formal_primitive_main": "B*(log B)^3",
        },
        "geometry_of_numbers": {
            "ordinary_slice": {
                "scale": "T_u=(2B/(a*u))^(1/2)",
                "axes": "X_u=T_u/b and Y_u=T_u/c",
                "available_shape": (
                    "For one lattice or residue lattice in a semialgebraic ellipse sector, "
                    "a Lipschitz/geometry-of-numbers estimate has area/determinant main term "
                    "plus an error controlled by X_u+Y_u+1 (equivalently projection volumes "
                    "and successive minima)."
                ),
                "useful_for": "ordinary, non-visible points at fixed divisibility data",
                "missing": [
                    "visibility gcd(v,w)=1",
                    "the two local coprimality conditions involving b and c",
                    "cancellation over the three divisor moduli",
                ],
            },
            "summed_slice_boundary": (
                "Summing T_u over u<=B/(a*max(b,c)^2) gives size B/(a*max(b,c)). "
                "After the v,w step sizes are included, the best-case boundary scale is "
                "B/(a*b*c), before visibility costs."
            ),
        },
        "mobius_decomposition": {
            "identity": (
                "1_{gcd(v,w)=1}1_{gcd(v,c)=1}1_{gcd(w,b)=1}="
                "sum_{d|v,w}mu(d) sum_{e|v,c}mu(e) sum_{f|w,b}mu(f)"
            ),
            "absolute_pointwise_budget": (
                "Applying the ordinary boundary estimate term-by-term and taking absolute "
                "values introduces at least the harmonic d-sum. Even if all b,c divisor "
                "multiplicities are optimistically discarded, the fixed-(a,b,c) model is "
                "E_{a,b,c}(B) << B*log(2B)/(a*b*c)."
            ),
            "weighted_global_budget": {
                "modulus_region": "x+2*max(y,z)<L for x=log a, y=log b, z=log c, L=log B",
                "coefficient_volume": "integral 1 dx dy dz = L^3/12",
                "extra_visibility_log": "multiplication by L",
                "result": "B*L^4/12",
                "formal_main_comparison": "The Stage12-N1-2f main simplex is B*L^4/48.",
                "decision": (
                    "The elementary geometry-of-numbers plus absolute Möbius route has the "
                    "same logarithmic degree as the raw main term and therefore cannot prove "
                    "an asymptotic, even before the omitted local divisor costs."
                ),
            },
        },
        "deep_fixed_domain_results": {
            "unconditional_fixed_D": (
                "Primitive points in sqrt(x)D admit area-density asymptotics with an "
                "O(x^(1/2)*omega(x)) type remainder for a fixed smooth planar domain D, "
                "using Möbius cancellation and zero-free-region input."
            ),
            "stronger_results": (
                "Power exponents below 1/2 are available in the cited primitive planar-domain "
                "literature under RH, again for a fixed domain with constants depending on D."
            ),
            "direct_application": False,
            "failures_of_uniformity": [
                "The Stage12 domain changes with the eccentricity ratio b/c.",
                "The ratio b/c is unbounded over the leading modulus range.",
                "The domain also has an order-sector cut and congruence/local-coprimality data.",
                "The theorem constants are not supplied uniformly over a growing three-modulus family.",
                "The count is summed over u and then weighted over a,b,c.",
            ],
        },
        "eccentricity_obstruction": {
            "balanced_family": "Restrict |log b-log c|<=K with fixed K.",
            "exact_integral": (
                "I_bal(L,K)=K*L^3/6-K^2*L^2/2+2*K^3*L/3-K^4/3 "
                "for L/2>=K."
            ),
            "total_integral": "I_all(L)=L^4/48.",
            "ratio": "I_bal/I_all ~ 8K/L -> 0.",
            "consequence": (
                "Uniform estimates only for bounded eccentricity recover a lower-logarithmic-order "
                "portion of the formal main term. The leading B(log B)^4 coefficient requires "
                "uniformity through increasingly eccentric ellipses."
            ),
        },
        "average_error_results": {
            "known_template": (
                "Mean-square or first-moment lattice-rest estimates average the dilation "
                "parameter for one fixed convex domain."
            ),
            "stage12_average": (
                "A six-dyadic-parameter weighted average over h/r/s blocks and a/b/c modulus "
                "blocks, with changing eccentricity and visibility restrictions."
            ),
            "direct_application": False,
            "reason": (
                "An average in one dilation variable for fixed D does not directly control "
                "the correlated family D_{b,c}, the reciprocal sampling T_u^2=2B/(a*u), "
                "or the lambda_1 weights."
            ),
        },
        "sufficient_remainder_targets": {
            "raw_only": "E_raw(B)=o(B*(log B)^4) is enough for the raw asymptotic.",
            "primitive_by_absolute_outer_mobius": (
                "If E_raw(X)<<X*(log X)^beta, absolute outer Möbius summation gives "
                "O(B*(log B)^(beta+1)); hence beta<2 is sufficient for o(B*(log B)^3)."
            ),
            "power_saving": (
                "E_raw(X)<<X^(1-delta)*(log X)^C for fixed delta>0 is sufficient; "
                "absolute outer Möbius summation is O(B) with a delta,C-dependent constant."
            ),
            "required_new_input": (
                "A uniform or averaged visible-ellipse discrepancy over the full anisotropic "
                "three-modulus family, producing either a power saving in B or at least "
                "a raw error O(B*(log B)^(2-eta))."
            ),
        },
        "finite_exponent_diagnostics": rows,
        "literature_audit": [
            {
                "work": "Barroero-Widmer, Counting lattice points and o-minimal structures, arXiv:1210.5943",
                "usable_part": "Uniform ordinary lattice counts for definable families via projection volumes and successive minima.",
                "gap": "No primitive/Möbius cancellation or lambda_1-weighted three-modulus average.",
            },
            {
                "work": "Zhai, On primitive lattice points in planar domains, Acta Arith. 109 (2003)",
                "usable_part": "Fixed-domain primitive asymptotics and the Möbius decomposition; stronger power errors under RH.",
                "gap": "The domain is fixed, while Stage12 requires unbounded eccentricity and growing congruence moduli.",
            },
            {
                "work": "Ivic-Kratzel-Kuhleitner-Nowak, Lattice points in large regions and related arithmetic functions, arXiv:math/0410522",
                "usable_part": "Framework and average-error results for classical fixed-domain lattice remainders.",
                "gap": "No direct six-parameter weighted anisotropic estimate matching Stage12.",
            },
        ],
        "decision": {
            "classification": "B_pointwise_geometry_of_numbers_not_sufficient_averaged_anisotropic_input_required",
            "closed": [
                "The ordinary fixed-divisibility lattice error can be organized by projection lengths.",
                "The exact Möbius decomposition of all three coprimality conditions is explicit.",
                "The elementary absolute error budget has the same B(log B)^4 degree as the raw main term.",
                "Bounded-eccentricity fixed-domain theorems cover only a lower-order share of the leading logarithmic simplex.",
                "A raw power-saving remainder would now survive global Möbius inversion because the primitive main has degree 3.",
            ],
            "not_closed": [
                "A uniform fixed-modulus primitive ellipse remainder through unbounded eccentricity.",
                "Cancellation in the d/e/f Möbius variables averaged over a/b/c.",
                "A theorem delivering the required weighted six-dyadic-block discrepancy.",
            ],
            "next_stage": (
                "12-N1-2h: derive a small/large modulus and eccentricity decomposition, "
                "then test whether Poisson summation plus a hybrid large sieve can supply "
                "the missing averaged anisotropic discrepancy."
            ),
        },
        "not_claimed": [
            "That the elementary boundary model is a lower bound for the true error.",
            "That existing fixed-domain primitive results are false or cannot be extended uniformly.",
            "That RH would by itself close the Stage12 family-uniformity problem.",
            "A raw or primitive asymptotic formula.",
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
