#!/usr/bin/env python3
"""Stage13-7j: normalized pure-G ratio/deviation law and finite comparison."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path("stages/stage13/data")
IN_ASYM = ROOT / "13-7/individual_category_asymptotic_report.json"
IN_FINITE = ROOT / "13-7/parity_g_scaling_report.json"
OUT = ROOT / "13-7/normalized_pure_g_limit_report.json"


def build_report() -> dict:
    asym = json.loads(IN_ASYM.read_text())
    finite = json.loads(IN_FINITE.read_text())

    p = asym["normalized_limit"]["proportion"]
    ratio = asym["normalized_limit"]["bc_normalized_ratio"]
    constants = asym["individual_leading_constants"]
    k_total = float(asym["total_and_gap_checks"]["K_total"])
    k0 = float(asym["total_and_gap_checks"]["stage13_7i_K0"])

    alpha = float(p["ab"]) - 0.5
    beta = (float(p["ac"]) - float(p["bc"])) / 2.0
    delta = float(p["ac"]) - float(p["bc"])

    beta_from_gap = k0 / (2.0 * k_total)
    if abs(beta - beta_from_gap) > 2e-10:
        raise ArithmeticError("beta limit does not match Stage13-7i gap constant")

    rows = []
    checkpoints = {1_000_000, 2_000_000, 5_000_000}
    for row in finite["rows"]:
        if int(row["B"]) not in checkpoints:
            continue
        g = row["cumulative"]["G_neutral"]
        rows.append(
            {
                "B": row["B"],
                "finite_bc_normalized_ratio": {
                    "ab": g["ratio_bc"]["ab"],
                    "ac": g["ratio_bc"]["ac"],
                    "bc": 1.0,
                },
                "finite_alpha": g["alpha"],
                "finite_beta": g["beta"],
                "error_to_limit": {
                    "ab_ratio": g["ratio_bc"]["ab"] - ratio["ab"],
                    "ac_ratio": g["ratio_bc"]["ac"] - ratio["ac"],
                    "alpha": g["alpha"] - alpha,
                    "beta": g["beta"] - beta,
                },
            }
        )

    return {
        "metadata": {
            "stage": "13-7j",
            "scope": (
                "normalized law for the pure-G observable only; finite rows are diagnostics "
                "and are not used in the proof"
            ),
        },
        "asymptotic_scale": {
            "common_scale": "B(log B)^(1/3)",
            "K_ab": constants["ab"]["numeric_truncation"],
            "K_ac": constants["ac"]["numeric_truncation"],
            "K_bc": constants["bc"]["numeric_truncation"],
            "K_total": k_total,
            "K_gap_ac_minus_bc": k0,
        },
        "pure_G_limit": {
            "proportion": p,
            "bc_normalized_ratio": ratio,
            "alpha_limit": alpha,
            "beta_limit": beta,
            "delta_ac_minus_bc_limit": delta,
            "beta_from_stage13_7i_gap_constant": beta_from_gap,
            "formulas": {
                "P_q": "K_q/K_total = I_q/(I_ab+I_ac+I_bc) = 8 I_q/pi^2",
                "alpha": "P_ab-1/2",
                "beta": "(P_ac-P_bc)/2 = K0/(2 K_total)",
                "ac_over_bc": "K_ac/K_bc = I_ac/I_bc",
            },
        },
        "interpretation": {
            "stage13_3b_promotion": (
                "The Stage13-3b archimedean chamber ratio, previously only a comparison "
                "model, is the actual normalized limit of the pure-G deweighted observable."
            ),
            "finite_representation_density_flattening": (
                "The finite pure-G ratios below the chamber limit are a pre-asymptotic effect; "
                "the 7j theorem does not say that raw incidence has the same limit because raw "
                "counts restore primitive-support and shell-richness weights."
            ),
            "important_scope_guardrail": (
                "Do not transfer this limit to raw incidence or exact-one counts without new "
                "asymptotics for the reweighting layers."
            ),
        },
        "finite_scaling_comparison": rows,
        "status": {
            "pure_G_ab_ac_bc_ratio_limit": True,
            "pure_G_alpha_limit": True,
            "pure_G_beta_limit": True,
            "limit_equals_stage13_3b_geometry": True,
            "raw_ratio_limit": False,
            "exact_one_ratio_limit": False,
            "next": "Stage13-7k",
        },
    }


def main() -> None:
    report = build_report()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report["pure_G_limit"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
