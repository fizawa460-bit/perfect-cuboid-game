#!/usr/bin/env python3
"""Stage13-7jb finite diagnostics for richness restoration.

Finite data are not proof inputs.  This script places the Stage13-3e raw
incidence data and the Stage13-7d/7j pure-G data on the new asymptotic scales.
It shows explicitly that the shell-richness amplification is strongly
category-dependent at present cutoffs even though 7jb proves a common leading
amplification constant.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path("stages/stage13/data")
IN_RAW = ROOT / "13-3/representation_density_report.json"
IN_G = ROOT / "13-7/analytic_reduction_scaling_report.json"
IN_ASYM = ROOT / "13-7/supported_richness_raw_asymptotic_report.json"
OUT = ROOT / "13-7/supported_richness_finite_report.json"
CATS = ("ab", "ac", "bc")


def build_report() -> dict:
    raw = json.loads(IN_RAW.read_text())
    g = json.loads(IN_G.read_text())
    asym = json.loads(IN_ASYM.read_text())

    target_total = float(asym["frozen_stage12_total"]["numeric_total_constant_diagnostic"])
    target_ratio = asym["raw_normalized_limit"]["bc_normalized_ratio"]
    omega = float(asym["richness_amplification_relative_to_pure_G"]["numeric_Omega_using_stage12_kappa_diagnostic"])

    rows = []
    for row in raw["rows"]:
        B = int(row["B"])
        rv = {q: float(row["raw"][q]) for q in CATS}
        total = sum(rv.values())
        rows.append({
            "B": B,
            "raw_total": total,
            "raw_total_over_B_logB_cubed": total / (B * math.log(B) ** 3),
            "target_total_constant_kappa_diagnostic": target_total,
            "raw_ratio_bc": row["raw_ratio_bc"],
            "limit_ratio_bc": target_ratio,
            "ratio_error": {
                "ab": float(row["raw_ratio_bc"]["ab"]) - float(target_ratio["ab"]),
                "ac": float(row["raw_ratio_bc"]["ac"]) - float(target_ratio["ac"]),
            },
        })

    g100 = None
    for row in g["rows"]:
        if int(row["B"]) == 100000:
            g100 = {q: float(row["ALL"]["direct"][i]) for i, q in enumerate(CATS)}
            break
    if g100 is None:
        raise ArithmeticError("missing B=100000 pure-G row")

    raw100 = next(r for r in raw["rows"] if int(r["B"]) == 100000)
    richness = {}
    for q in CATS:
        amp = float(raw100["raw"][q]) / g100[q]
        richness[q] = {
            "raw_over_primitive_pure_G": amp,
            "scaled_by_log_to_minus_8_over_3": amp / math.log(100000.0) ** (8.0 / 3.0),
            "target_common_Omega": omega,
        }

    return {
        "metadata": {
            "stage": "13-7jb",
            "scope": "finite diagnostics only; the raw directional theorem is in supported_richness_raw_asymptotic_report.json",
        },
        "rows": rows,
        "B100000_richness_amplification": richness,
        "B100000_interpretation": {
            "finite_order": "raw/G amplification is smallest for ab and larger for ac,bc, which flattens the finite ab excess",
            "asymptotic_order": "7jb proves these three scaled amplifications have the same leading constant Omega",
            "warning": "the current cutoff is far from the asymptotic constant and must not be used to estimate Omega",
        },
        "status": {
            "finite_richness_direction_bias_visible": True,
            "finite_bias_is_leading_asymptotic_bias": False,
        },
    }


def main() -> None:
    report = build_report()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
