#!/usr/bin/env python3
"""Stage13-12ad: exact arithmetic ledger for the j=0 quantitative closure.

This is not a numerical experiment.  It records the explicit worst-case Wiener
norm constants and the fixed logarithmic exponents used in result.md so CI can
catch accidental weakening of the proof budget.
"""
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

OUT = Path("stages/stage13/data/13-12ad/j0_quantitative_closure_audit_report.json")


def fstr(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}"


def build_report() -> dict:
    # Fix delta=1/8, sigma=5/8.  For every split prime q>=13,
    # rho=q^{-sigma}<1/4.  We use rho<=1/4 throughout.
    rho = Fraction(1, 4)

    # If a=A-1 and b=B-1, coefficient majorants give
    # ||a|| <= (8/3)rho and ||b|| <= (44/9)rho.
    a_over_rho = Fraction(8, 3)
    b_over_rho = Fraction(44, 9)

    # The genuine x-y mixed part M has norm <= (32/9)rho^2.
    mixed_over_rho2 = Fraction(32, 9)

    # D - A B_y B_z = (M_xy-a b_y)+(M_xz-a b_z)-b_y b_z-a b_y b_z.
    # In the last term use rho<=1/4 once to return to a rho^2 bound.
    e_over_rho2 = (
        2 * mixed_over_rho2
        + 2 * a_over_rho * b_over_rho
        + b_over_rho * b_over_rho
        + a_over_rho * b_over_rho * b_over_rho * rho
    )

    # Exact rational inverses satisfy the following Wiener bounds at rho<=1/4.
    inv_a = Fraction(5, 3)
    inv_b = Fraction(25, 12)
    c_over_rho2 = e_over_rho2 * inv_a * inv_b * inv_b
    c_integer_majorant = (c_over_rho2.numerator + c_over_rho2.denominator - 1) // c_over_rho2.denominator

    if c_integer_majorant != 529:
        raise ArithmeticError("unexpected Wiener constant")
    if c_over_rho2 >= 529:
        raise ArithmeticError("529 no longer majorizes the exact constant")

    # Concrete harmonic/curved-region choices.
    K = 4
    A = 48
    mesh_power = 8
    threshold_log_power = Fraction(1, 4)

    # Error exponents relative to B*(log B)^e.  The main exponent is 3.
    small_height_exp = Fraction(2, 1) + threshold_log_power            # 9/4
    small_coordinate_exp = Fraction(2, 1) + 2 * threshold_log_power    # 5/2
    boundary_exp = Fraction(3 - mesh_power, 1)                          # -5
    vaaler_exp = Fraction(3 - K, 1)                                     # -1
    harmonic_exp = Fraction(K + 2, 1) - A * threshold_log_power         # -6
    log_shift_exp = Fraction(2, 1)

    for name, exponent in {
        "small_height": small_height_exp,
        "small_coordinate": small_coordinate_exp,
        "boundary_shell": boundary_exp,
        "vaaler_excess": vaaler_exp,
        "nonzero_harmonics": harmonic_exp,
        "mixed_log_shift": log_shift_exp,
    }.items():
        if exponent >= 3:
            raise ArithmeticError(f"{name} is not lower order: exponent={exponent}")

    return {
        "metadata": {
            "stage": "13-12ad",
            "scope": "explicit j=0 Wiener constant and curved/harmonic error budget",
            "diagnostic_only": False,
        },
        "wiener_uniformity": {
            "delta": "1/8",
            "sigma": "5/8",
            "large_split_prime_range": "q>=13",
            "rho_bound": "rho=q^(-5/8)<=1/4",
            "a_norm_over_rho": fstr(a_over_rho),
            "b_norm_over_rho": fstr(b_over_rho),
            "mixed_norm_over_rho2": fstr(mixed_over_rho2),
            "E_norm_over_rho2": fstr(e_over_rho2),
            "A_inverse_norm": fstr(inv_a),
            "B_inverse_norm": fstr(inv_b),
            "exact_C_minus_1_constant": fstr(c_over_rho2),
            "integer_majorant": c_integer_majorant,
            "conclusion": "||C_{ell,q}-1||_{5/8} <= 529*q^(-5/4), uniformly in ell and phase for split q>=13; q=5 is a finite Euler factor",
            "log_moments": "weighted-l1 at exponent 5/8 implies every fixed logarithmic moment at exponent 1 is finite",
        },
        "curved_region_parameters": {
            "H0": "exp((log B)^(1/4))",
            "U": "exp((log B)^(1/4))",
            "eta": "(log B)^(-8)",
            "rectangle_power_tail": "B*(log B)^C*(H0^(-1/4+eps)+U^(-1/4+eps))",
            "boundary_shell_exponent": fstr(boundary_exp),
            "small_height_exponent": fstr(small_height_exp),
            "small_coordinate_exponent": fstr(small_coordinate_exp),
            "mixed_log_shift_exponent": fstr(log_shift_exp),
        },
        "harmonic_parameters": {
            "Vaaler_degree": "L=(log B)^4",
            "K": K,
            "finite_order_SD_A": A,
            "external_uniform_input": "Gaussian angular Hecke zero-free region with log((2+|t|)(2+|k|)) conductor dependence; no exceptional zero for nonzero angular frequency; finite-order Selberg-Delange/Tauberian consequence used with explicit A,K",
            "vaaler_excess_exponent": fstr(vaaler_exp),
            "summed_nonzero_harmonic_exponent": fstr(harmonic_exp),
            "inequality": "K+2-A/4 = -6 < 3",
        },
        "assembled_error_budget": {
            "main_scale": "B*(log B)^3",
            "small_height": f"O(B*(log B)^({fstr(small_height_exp)}))",
            "small_coordinate": f"O(B*(log B)^({fstr(small_coordinate_exp)}))",
            "mixed_log_shift": f"O(B*(log B)^({fstr(log_shift_exp)}))",
            "boundary_shell": f"O(B*(log B)^({fstr(boundary_exp)})) plus rectangle power tails",
            "Vaaler_excess": f"O(B*(log B)^({fstr(vaaler_exp)}))",
            "summed_nonzero_harmonics": f"O(B*(log B)^({fstr(harmonic_exp)})) on the core plus dominated boundary pieces",
            "all_lower_order": True,
        },
        "status": {
            "STAGE13_12AD": "COMPLETE_QUANTITATIVE_J0_ANALYTIC_CLOSURE",
            "CLAUDE_R02_WEIGHTED_L1_UNIFORMITY": "REPAIRED",
            "CLAUDE_R02_NONZERO_HARMONIC_LOWER_ORDER": "REPAIRED",
            "GROK_R02_ZERO_MODE_CURVED_TRANSFER": "REPAIRED",
            "RAW_DIRECTIONAL_ANALYTIC_CORE": "RESTORED_WITH_EXPLICIT_ERROR_BUDGET",
            "P_ADIC_POSITIVE_VALUATION_TAIL": "PENDING_13_12AE",
            "LOCAL_STATE_REFINEMENT_COMPLETENESS": "PENDING_13_12AE",
            "STAGE13_GLOBAL_REVIEW_STATUS": "OPEN",
            "NEXT": "Stage13-12ae",
        },
    }


def main() -> None:
    report = build_report()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report["status"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
