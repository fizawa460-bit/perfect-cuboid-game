#!/usr/bin/env python3
"""Stage13-7i: uniform harmonic truncation and normalization-tail budget.

Stage13-7h proves strong cancellation for each fixed nonzero Gaussian angular
Hecke mode.  The missing 7i issue is whether infinitely many angular modes can
be discarded after the curved-region transfer.  This report records the
finite-degree Selberg/Vaaler truncation used to make that passage rigorous.

Key points:
  * interval indicators admit degree-L pointwise majorants/minorants whose
    zeroth coefficient error is O(1/L) and whose l-th coefficient is O(1/l);
  * the outer t-dependent harmonic coefficient has total variation O(1)
    uniformly in l;
  * the Gaussian Hecke zero-free region is uniform for 1<=l<=log(B)^K because
    the angular character xi_{8l} is nontrivial, so the exceptional-zero case
    k=0 is absent;
  * the normalization remainder j>=2 is pointwise dominated by the positive
    j=2 zero channel, avoiding any infinite (j,l) interchange there.

The analytic Hecke input is external theorem-level material, just as in 7h.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

OUT = Path("stages/stage13/data/13-7/harmonic_uniformity_budget_report.json")


def a_l_of_t(t: float, ell: int) -> float:
    invsqrt2 = 1.0 / math.sqrt(2.0)
    if t < invsqrt2:
        return 4.0 * math.sin(4.0 * ell * math.asin(t)) / (math.pi * ell)
    if t < 1.0:
        return 2.0 * math.sin(4.0 * ell * math.acos(t)) / (math.pi * ell)
    return 0.0


def t_of_phi(phi: float) -> float:
    r, s = math.cos(phi), math.sin(phi)
    return (s * s - r * r) / (2.0 * r * s)


def sampled_variation(ell: int, n: int = 200000) -> tuple[float, float]:
    a = math.pi / 4.0
    b = 3.0 * math.pi / 8.0
    prev = a_l_of_t(t_of_phi(a), ell)
    sup = abs(prev)
    var = 0.0
    for i in range(1, n + 1):
        phi = a + (b - a) * i / n
        cur = a_l_of_t(t_of_phi(phi), ell)
        sup = max(sup, abs(cur))
        var += abs(cur - prev)
        prev = cur
    return sup, var


def build_report() -> dict:
    harmonic_rows = []
    max_sup_scaled = 0.0
    max_var = 0.0
    for ell in [1, 2, 3, 5, 10, 25, 50]:
        sup, var = sampled_variation(ell, n=40000)
        max_sup_scaled = max(max_sup_scaled, ell * sup)
        max_var = max(max_var, var)
        harmonic_rows.append({
            "ell": ell,
            "sampled_sup": sup,
            "ell_times_sampled_sup": ell * sup,
            "sampled_total_variation": var,
        })

    return {
        "metadata": {
            "stage": "13-7i",
            "scope": "uniform nonzero-harmonic closure and all-j normalization tail",
        },
        "finite_fourier_majorant": {
            "tool": "standard Selberg/Vaaler trigonometric majorant/minorant for interval indicators",
            "degree": "L=(log B)^K with any fixed K>1/12; K=4 is a convenient choice",
            "pointwise_feature": (
                "The interval indicator is bracketed pointwise, so no uniform Fejer convergence "
                "at moving jump locations is assumed."
            ),
            "constant_term_error": "O(1/L) times the positive j=1 zero-channel mass",
            "harmonic_coefficients": "for 1<=ell<=L, coefficient size O(1/ell)",
            "truncation_error": (
                "Since the positive j=1 mass on the retained wedge is O(B(log B)^(1/3)), "
                "the majorant/minorant excess is O(B(log B)^(1/3)/L)=o(B(log B)^(1/3))."
            ),
        },
        "outer_coefficient_bv": {
            "exact_bounds": {
                "sup": "|a_ell(t)| <= 4/(pi ell)",
                "variation_first_piece": "<=8/pi",
                "variation_second_piece": "<=4/pi",
                "total_variation": "<=12/pi, uniformly in ell",
            },
            "consequence": (
                "Boxwise partial summation costs a constant independent of ell; the growth of "
                "the oscillation count is cancelled by the 1/ell Fourier amplitude."
            ),
            "sampled_checks": harmonic_rows,
            "max_ell_times_sup_sampled": max_sup_scaled,
            "max_total_variation_sampled": max_var,
            "theoretical_12_over_pi": 12.0 / math.pi,
        },
        "uniform_hecke_input": {
            "characters": "xi_{8ell}, 1<=ell<=L=(log B)^K",
            "zero_free_region": (
                "Use the standard Hecke zero-free region with analytic-conductor dependence "
                "log((2+|t|)(2+|k|)); the possible exceptional real zero occurs only for k=0, "
                "so it is absent for xi_{8ell}, ell>=1."
            ),
            "reference_boundary": (
                "For example Merikoski, On Gaussian primes in sparse sets, Sec. 2.7, "
                "Lemma 2.13 (classical Landau-Page zero-free region, citing Iwaniec-Kowalski Ch.5)."
            ),
            "polylog_uniformity": (
                "For ell<=log(B)^K, conductor dependence is only polylogarithmic.  Together "
                "with uniform local majorants from 7h and polynomial vertical growth, the "
                "z=0 scale contour/finite-order Selberg-Delange argument gives, for every fixed "
                "A,K, a bound O_{A,K}(X(log X)^(-A)) uniformly in this ell range."
            ),
            "curved_core": (
                "After the 7h rectangle and bounded-variation transfer, each retained harmonic "
                "is O_{A,K}(B(log B)^(-A)); summing at most L=log(B)^K modes remains lower order "
                "after choosing A>K+10."
            ),
        },
        "normalization_remainder": {
            "identity": (
                "After extracting j=1, the exact denominator remainder is "
                "1/(G-1)-1/G = 1/(G(G-1))."
            ),
            "pointwise_majorant": (
                "If N is the signed primitive face-gap numerator and T_G is the positive "
                "primitive face-count numerator, |N|<=T_G.  Since G>=3, "
                "|N|/(G(G-1)) <= (3/2) T_G/G^2."
            ),
            "consequence": (
                "All j>=2 zero and nonzero angular content is dominated at once by 3/2 times "
                "the positive j=2 zero channel; no uniform summation over j or ell is needed."
            ),
            "j2_bulk": "Stage13-7h exponent: B(log B)^(-5/9) on the core",
            "boundary_and_wings": (
                "The separated minimal-scale and small-height/coordinate regions are at most "
                "O(B(log B)^(1/4)), hence o(B(log B)^(1/3))."
            ),
        },
        "assembled_remainder": {
            "small_height_or_coordinate": "O(B(log B)^(1/4))",
            "j1_nonzero_harmonics_core": "o(B(log B)^(1/3)) by finite Vaaler truncation plus polylog-uniform Hecke cancellation",
            "all_j_ge_2": "o(B(log B)^(1/3)) by the positive j=2 zero-channel majorant",
            "minimal_scale": "O(B)=o(B(log B)^(1/3)) for the largest j=1 zero boundary",
            "result": "Every term other than the j=1 zero bulk is o(B(log B)^(1/3)).",
        },
        "final_stage13_7i_conclusion": {
            "pure_G_ac_minus_bc": (
                "Delta_G(B) ~ K0 B(log B)^(1/3), with K0>0 as evaluated in "
                "curved_wedge_asymptotic_report.json."
            ),
            "finite_positive_drift_promoted_to_secondary_asymptotic": True,
            "exact_directional_ratio_limit_from_this_step": False,
            "reason_ratio_not_claimed": (
                "7i proves the secondary ac-bc gap for the pure-G observable; a separate "
                "asymptotic for the individual G-neutral category masses is required before "
                "turning this into an ac/bc ratio limit statement."
            ),
        },
        "status": {
            "STAGE13_7I": "COMPLETE_AT_PURE_G_SECONDARY_GAP_ASYMPTOTIC_LEVEL",
            "J1_ZERO_CURVED_WEDGE_CONSTANT": "EVALUATED_POSITIVE",
            "NONZERO_HARMONIC_FAMILY": "CLOSED_BY_FINITE_VAALER_TRUNCATION_AND_POLYLOG_UNIFORM_HECKE_INPUT",
            "NORMALIZATION_TAIL": "CLOSED_BY_J2_ZERO_POSITIVE_MAJORANT",
            "PURE_G_SECONDARY_ASYMPTOTIC": True,
            "DIRECTIONAL_RATIO_LIMIT_IDENTIFIED": False,
            "next": "Stage13-7j",
        },
    }


def main() -> None:
    report = build_report()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
