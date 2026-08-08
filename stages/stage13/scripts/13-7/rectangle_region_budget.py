#!/usr/bin/env python3
"""Stage13-7h: exponent/core-wing budget after the uniform rectangle repair.

This companion report does not claim the final curved-wedge asymptotic.  It
checks that the 7h rectangle lemma has enough room for the same kind of
core/wing transfer used in frozen Stage12 and records the singularity hierarchy
which Stage13-7i must turn into an actual leading constant.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

OUT = Path("stages/stage13/data/13-7/rectangle_region_budget_report.json")


def t_of_lambda(lam: float) -> float:
    return (lam * lam - 1.0) / (2.0 * lam)


def k0_of_t(t: float) -> float:
    invsqrt2 = 1.0 / math.sqrt(2.0)
    if t < invsqrt2:
        return 8.0 * math.asin(t) / math.pi - 1.0
    if t < 1.0:
        return 4.0 * math.acos(t) / math.pi
    return 0.0


def simpson(f, a: float, b: float, n: int = 200000) -> float:
    if n % 2:
        n += 1
    h = (b - a) / n
    acc = f(a) + f(b)
    for i in range(1, n):
        acc += (4.0 if i % 2 else 2.0) * f(a + i * h)
    return acc * h / 3.0


def build_report() -> dict:
    lam0 = (math.sqrt(6.0) + math.sqrt(2.0)) / 2.0
    lam1 = 1.0 + math.sqrt(2.0)

    # In polar coordinates r=rho cos(phi), s=rho sin(phi), r<s.
    # t=-cot(2phi), and support t<1 is phi in (pi/4,3pi/8).
    phi_a = math.pi / 4.0
    phi_b = 3.0 * math.pi / 8.0

    def angular(phi: float) -> float:
        r, s = math.cos(phi), math.sin(phi)
        t = (s * s - r * r) / (2.0 * r * s)
        return k0_of_t(t)

    angular_integral = simpson(angular, phi_a, phi_b)

    ledger = []
    for j in range(1, 9):
        alpha = 3.0 ** (-j)
        beta0 = (1.0 + 3.0 ** (1 - j)) / 2.0
        beta1 = (1.0 + alpha) / 2.0
        bulk0 = alpha + 2.0 * beta0 - 2.0
        boundary0 = 2.0 * beta0 - 2.0
        boundary_h = 2.0 * beta1 - 2.0
        ledger.append({
            "j": j,
            "alpha_scale_zero": alpha,
            "beta_base_zero": beta0,
            "beta_base_harmonic": beta1,
            "bulk_zero_log_exponent": bulk0,
            "minimal_scale_zero_log_exponent": boundary0,
            "minimal_scale_harmonic_log_exponent": boundary_h,
            "bulk_minus_boundary_zero": bulk0 - boundary0,
        })

    return {
        "metadata": {
            "stage": "13-7h",
            "scope": "core/wing and singularity budget; no final curved-wedge constant theorem",
        },
        "fixed_wedge": {
            "lambda_break_t_1_over_sqrt2": lam0,
            "lambda_support_end_t_1": lam1,
            "k0_sup_norm": 1.0,
            "k0_total_variation": 3.0,
            "reason": "k0 rises monotonically from -1 to +1, then falls monotonically from +1 to 0.",
            "consequence": "The fixed directional wedge multiplier has bounded variation, so it costs only a fixed factor in boxwise partial summation; the square-root derivative at t=1 does not create infinite total variation.",
        },
        "stage12_style_cutoffs": {
            "choice": "U=H0=exp(c*(log B)^(1/4)) with fixed c>0",
            "small_height": "O(B log H0)=O(B(log B)^(1/4)) from the exact shellwise |G-neutral gap|<=1 bound",
            "small_coordinate_fixed_channel": "O(B log U)=O(B(log B)^(1/4)) from the positive j=1 zero-mode scale majorant; all fixed channels are pointwise dominated by it",
            "core_power_tail": "On H,R,S>=U, the 3/4+eps rectangle tails acquire U^(-1/4+eps), hence beat every fixed log power after summing polynomially many dyadic boxes.",
            "core_sd_tail": "Arbitrary finite-order Selberg-Delange saving gives (log U)^(-A)=O((log B)^(-A/4)); choose A after the fixed box/variation losses.",
            "margin_against_candidate_j1_bulk": "1/3-1/4=1/12 in the logarithmic exponent.",
        },
        "homogeneity_ledger": ledger,
        "hierarchy": {
            "largest_fixed_channel_candidate": "j=1 zero bulk with B(log B)^(1/3)",
            "j2_zero_bulk": "B(log B)^(-5/9)",
            "j1_minimal_scale_zero": "O(B)",
            "j1_minimal_scale_harmonic": "O(B(log B)^(-2/3)) at the rectangle-singularity level",
            "nonzero_bulk_harmonics": "The pure h factor has Selberg-Delange z=0 and arbitrary fixed log-power cancellation on the retained h-core; no competing positive zeta singularity is present.",
            "interpretation": "The exponent ledger isolates j=1 zero bulk as the only fixed channel with a positive log exponent. Turning this hierarchy into a theorem for the curved wedge is Stage13-7i, not asserted here.",
        },
        "archimedean_diagnostic_for_7i": {
            "integral": "int_{pi/4}^{3pi/8} k0((s^2-r^2)/(2rs)) dphi",
            "numeric_value": angular_integral,
            "sign": "positive" if angular_integral > 0 else "nonpositive",
            "status": "diagnostic only in 7h; the arithmetic local-density constant and full radial beta integral are not multiplied out here",
        },
        "status": {
            "core_wing_error_budget": "CLOSED_AT_FIXED_CHANNEL_LEVEL",
            "fixed_wedge_bv_compatibility": "PROVED",
            "j1_zero_bulk_unique_positive_log_exponent": True,
            "j1_zero_bulk_curved_region_asymptotic": False,
            "next": "Stage13-7i",
        },
    }


def main() -> None:
    report = build_report()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
