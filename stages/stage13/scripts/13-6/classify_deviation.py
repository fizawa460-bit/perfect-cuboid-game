#!/usr/bin/env python3
"""Stage13-6: classify the Stage13-5 deviation coordinates by structural layer.

This script does not pretend that every audited mechanism is one additive causal
chain. It places the locked Stage13-3/4 diagnostics into the common Stage13-5
coordinates

    alpha = P_ab - 1/2,
    beta  = (P_ac - P_bc)/2,

and records which comparisons are exact transitions, model comparisons,
stratifications, stability controls, or exact null effects.

The only telescoping normalized-weight chain used here is

    G_neutral -> shell_neutral -> raw,

followed by the exact raw -> exact_one overlap sieve. Geometry is a comparison
model; OE/EE is a stratification; the outer-half comparison is a boundary
control; the Stage12 fiber factor 2 is an exact normalization-invariant null
for directional proportions.

Finite structural classification only: no convergence or directional
asymptotic claim is made.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[4]
RAW_PATH = ROOT / "stages/stage13/data/13-3/raw_incidence_report.json"
GEO_PATH = ROOT / "stages/stage13/data/13-3/geometric_chamber_report.json"
PARITY_PATH = ROOT / "stages/stage13/data/13-3/parity_2adic_report.json"
REP_PATH = ROOT / "stages/stage13/data/13-3/representation_density_report.json"
BOUNDARY_PATH = ROOT / "stages/stage13/data/13-3/boundary_stability_report.json"
SCALING_PATH = ROOT / "stages/stage13/data/13-4/ac_bc_scaling_report.json"
OUTPUT = ROOT / "stages/stage13/data/13-6/deviation_classification_report.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize(v: dict[str, float]) -> dict[str, float]:
    total = float(v["ab"] + v["ac"] + v["bc"])
    return {k: float(v[k]) / total for k in ("ab", "ac", "bc")}


def mode(p: dict[str, float]) -> dict[str, Any]:
    ab, ac, bc = float(p["ab"]), float(p["ac"]), float(p["bc"])
    alpha = ab - 0.5
    beta = (ac - bc) / 2.0
    delta = {"ab": alpha, "ac": ac - 0.25, "bc": bc - 0.25}
    if abs(sum(delta.values())) > 5e-12:
        raise ArithmeticError(("delta sum", p, delta))
    recon = {
        "ab": alpha,
        "ac": -alpha / 2.0 + beta,
        "bc": -alpha / 2.0 - beta,
    }
    if max(abs(recon[k] - delta[k]) for k in delta) > 5e-12:
        raise ArithmeticError(("mode reconstruction", p, delta, recon))
    return {
        "proportion": {"ab": ab, "ac": ac, "bc": bc},
        "alpha": alpha,
        "beta": beta,
        "delta": delta,
        "L1": sum(abs(x) for x in delta.values()),
        "Linf": max(abs(x) for x in delta.values()),
        "L2": math.sqrt(sum(x * x for x in delta.values())),
    }


def displacement(a: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
    return {
        "delta_alpha": b["alpha"] - a["alpha"],
        "delta_beta": b["beta"] - a["beta"],
        "delta_vector": {k: b["delta"][k] - a["delta"][k] for k in ("ab", "ac", "bc")},
    }


def main() -> None:
    raw = load(RAW_PATH)
    geo = load(GEO_PATH)
    parity = load(PARITY_PATH)
    rep = load(REP_PATH)
    boundary = load(BOUNDARY_PATH)
    scaling = load(SCALING_PATH)

    top_raw = raw["rows"][-1]
    top_parity = parity["rows"][-1]

    layers = {
        "archimedean_geometry": mode(geo["numerical_chamber_integrals"]["proportion"]),
        "G_neutral": mode(rep["B100000_detail"]["G_neutral_proportion"]),
        "shell_neutral": mode(rep["B100000_detail"]["shell_neutral_proportion"]),
        "raw": mode(normalize(top_raw["raw_incidence"])),
        "exact_one": mode(normalize(top_raw["exact_one"])),
        "outer_half_raw": mode(boundary["largest_cutoff_boundary_test"]["outer_half_proportion"]),
        "OE_raw": mode(top_parity["OE"]["proportion"]),
        "EE_raw": mode(top_parity["EE"]["proportion"]),
    }

    oe = top_parity["OE"]["count"]
    ee = top_parity["EE"]["count"]
    combined = {k: int(oe[k]) + int(ee[k]) for k in ("ab", "ac", "bc")}
    if combined != {k: int(top_raw["raw_incidence"][k]) for k in combined}:
        raise ArithmeticError(("OE+EE raw reconstruction", combined, top_raw["raw_incidence"]))

    transitions = {
        "geometry_to_G_neutral": {
            "type": "comparison_model_to_arithmetic_reweighting; not a causal exact factorization",
            **displacement(layers["archimedean_geometry"], layers["G_neutral"]),
        },
        "G_neutral_to_shell_neutral": {
            "type": "exact finite reweighting transition isolating primitive-support correction",
            **displacement(layers["G_neutral"], layers["shell_neutral"]),
        },
        "shell_neutral_to_raw": {
            "type": "exact finite reweighting transition restoring supported-shell richness",
            **displacement(layers["shell_neutral"], layers["raw"]),
        },
        "raw_to_exact_one": {
            "type": "exact overlap-sieve transition",
            **displacement(layers["raw"], layers["exact_one"]),
        },
        "cumulative_raw_to_outer_half_raw": {
            "type": "boundary/stability comparison; not an additive mechanism",
            **displacement(layers["raw"], layers["outer_half_raw"]),
        },
    }

    d_gs = transitions["G_neutral_to_shell_neutral"]
    d_sr = transitions["shell_neutral_to_raw"]
    d_gr = displacement(layers["G_neutral"], layers["raw"])
    if abs((d_gs["delta_alpha"] + d_sr["delta_alpha"]) - d_gr["delta_alpha"]) > 5e-12:
        raise ArithmeticError("alpha telescope")
    if abs((d_gs["delta_beta"] + d_sr["delta_beta"]) - d_gr["delta_beta"]) > 5e-12:
        raise ArithmeticError("beta telescope")

    pure_g_top = scaling["cumulative_by_bound"][-1]

    report = {
        "metadata": {
            "stage": "13-6",
            "title": "Structural classification of the Stage13 deviation modes",
            "B": 100000,
            "coordinates": "alpha=P_ab-1/2; beta=(P_ac-P_bc)/2",
            "scope": "finite structural classification; no additive attribution across incomparable diagnostics and no asymptotic claim",
            "sources": [
                str(p.relative_to(ROOT))
                for p in (RAW_PATH, GEO_PATH, PARITY_PATH, REP_PATH, BOUNDARY_PATH, SCALING_PATH)
            ],
        },
        "layers": layers,
        "transitions": transitions,
        "classification": {
            "canonical_archimedean_geometry": {
                "role": "creates a large positive leading-half mode and a positive ac/bc split in the chamber model",
                "alpha": layers["archimedean_geometry"]["alpha"],
                "beta": layers["archimedean_geometry"]["beta"],
                "status": "exact real-density/chamber model, not the full arithmetic count",
            },
            "pure_G_arithmetic_profile": {
                "role": "nearly cancels the ac/bc split mode under G-neutral weighting while leaving a large positive leading mode",
                "alpha": layers["G_neutral"]["alpha"],
                "beta": layers["G_neutral"]["beta"],
                "B100000_OE_ac_over_bc": pure_g_top["OE_G_ratio"],
                "B100000_EE_ac_over_bc": pure_g_top["EE_G_ratio"],
                "B100000_cancellation_efficiency": pure_g_top["cancellation_efficiency"],
                "status": "finite arithmetic reweighting diagnostic",
            },
            "primitive_support": {
                "role": "reintroduces a positive ac/bc split and modestly reduces the leading mode when moving G-neutral -> shell-neutral",
                **transitions["G_neutral_to_shell_neutral"],
                "late_ac_bc_relative_factor_range": scaling["late_factor_ranges_B_ge_10000"]["F_prim"],
            },
            "supported_shell_richness": {
                "role": "dominant finite flattening of the leading-half mode; changes beta only slightly at B=100000",
                **transitions["shell_neutral_to_raw"],
            },
            "parity_order_coupling": {
                "role": "OE and EE raw strata have opposite alpha signs and partially cancel in the aggregate; their raw beta signs are both positive. After pure-G deweighting their ac/bc pair gaps have opposite signs.",
                "OE_raw": {"alpha": layers["OE_raw"]["alpha"], "beta": layers["OE_raw"]["beta"]},
                "EE_raw": {"alpha": layers["EE_raw"]["alpha"], "beta": layers["EE_raw"]["beta"]},
                "OE_plus_EE_reconstructs_raw_exactly": True,
                "standalone_p2_category_bias": "zero by coordinate-permutation symmetry before canonical/order coupling",
                "pure_G_pair_signs_opposite": pure_g_top["OE_G_ratio"] < 1.0 < pure_g_top["EE_G_ratio"],
            },
            "overlap_exact_one_sieve": {
                "role": "tiny perturbation of both modes at the largest audited cutoff",
                **transitions["raw_to_exact_one"],
            },
            "cutoff_boundary": {
                "role": "largest outer-half band remains close to cumulative raw modes; no competing boundary-generated deviation is visible",
                **transitions["cumulative_raw_to_outer_half_raw"],
                "outer_half_share": boundary["largest_cutoff_boundary_test"]["outer_half_share_of_cumulative"],
            },
            "stage12_projection_fiber": {
                "role": "exact directional null for normalized proportions because every canonical raw incidence has the same projection multiplicity 2",
                "delta_alpha": 0.0,
                "delta_beta": 0.0,
                "status": "exact theorem-level finite identity from Stage13-3d",
            },
        },
        "final_exact_one": {
            "alpha": layers["exact_one"]["alpha"],
            "beta": layers["exact_one"]["beta"],
            "abs_beta_over_abs_alpha": abs(layers["exact_one"]["beta"] / layers["exact_one"]["alpha"]),
            "interpretation": "At B=100000 the final exact-one deviation is beta-dominated: the residual visible departure from 2:1:1 lies mainly in the ac/bc split, not in failure of ab to carry one half of the mass.",
        },
        "non_additivity_warning": {
            "statement": "Do not sum every named mechanism as if they were orthogonal causal contributions. Geometry is a model comparison, OE/EE is a stratification, boundary is a control, and fiber is an exact null. Only explicitly linked normalized reweighting transitions telescope.",
            "exact_telescope_used": "(G_neutral -> shell_neutral) + (shell_neutral -> raw) = (G_neutral -> raw) in Delta/alpha/beta coordinates",
        },
        "conclusion": {
            "deviation_classified_at_finite_structural_level": True,
            "alpha_main_finite_flattening_associated_with_supported_shell_richness": True,
            "beta_near_equality_associated_with_pure_G_cross_stratum_cancellation": True,
            "beta_residual_ac_excess_associated_with_primitive_support": True,
            "overlap_large_source": False,
            "boundary_large_source": False,
            "fiber_directional_source": False,
            "standalone_p2_directional_source": False,
            "additive_global_causal_decomposition_claim": False,
            "asymptotic_deviation_claim": False,
            "next": "Stage13-7: study the B-dependence of alpha(B), beta(B), and Delta(B), and decide whether any limiting or secondary asymptotic law is supported/provable.",
        },
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["final_exact_one"], indent=2))
    print(json.dumps(report["classification"], indent=2))


if __name__ == "__main__":
    main()
