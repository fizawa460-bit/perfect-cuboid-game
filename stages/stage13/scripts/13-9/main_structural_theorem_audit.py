#!/usr/bin/env python3
"""Stage13-9 main structural theorem consistency audit.

This script introduces no new analytic input. It checks that the theorem statement
assembled in Stage13-9 is numerically and algebraically consistent with the locked
Stage13-3b chamber integrals, Stage13-7 asymptotic theorem, and Stage13-8 bridge.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

I = {
    "ab": 0.659705248705705,
    "ac": 0.3026997526726076,
    "bc": 0.2712955487578571,
}

FINITE_RAW = {"ab": 84212, "ac": 43236, "bc": 40760}
FINITE_PROJECTED = {"ab": 168424, "ac": 86472, "bc": 81520}
FINITE_OVERLAP = {"ab_ac": 33, "ab_bc": 33, "ac_bc": 23}
FINITE_TRIPLE = 0
FINITE_EXACT_ONE = {"ab": 84146, "ac": 43180, "bc": 40704}
FINITE_C_PRIM = 336416


def close(a: float, b: float, tol: float = 2e-15) -> bool:
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


def main() -> None:
    i_sum = sum(I.values())
    p = {q: 8.0 * I[q] / math.pi**2 for q in I}
    p_sum = sum(p.values())
    ratio = {q: I[q] / I["bc"] for q in I}

    delta = {
        "ab": p["ab"] - 0.5,
        "ac": p["ac"] - 0.25,
        "bc": p["bc"] - 0.25,
    }
    alpha = delta["ab"]
    beta = (p["ac"] - p["bc"]) / 2.0

    directional_projection_ok = all(
        FINITE_PROJECTED[q] == 2 * FINITE_RAW[q] for q in FINITE_RAW
    )
    raw_total = sum(FINITE_RAW.values())
    projected_total = sum(FINITE_PROJECTED.values())
    overlap_sum = sum(FINITE_OVERLAP.values())
    exact_one_total = sum(FINITE_EXACT_ONE.values())

    exact_directional_ok = (
        FINITE_EXACT_ONE["ab"]
        == FINITE_RAW["ab"]
        - FINITE_OVERLAP["ab_ac"]
        - FINITE_OVERLAP["ab_bc"]
        + FINITE_TRIPLE
        and FINITE_EXACT_ONE["ac"]
        == FINITE_RAW["ac"]
        - FINITE_OVERLAP["ab_ac"]
        - FINITE_OVERLAP["ac_bc"]
        + FINITE_TRIPLE
        and FINITE_EXACT_ONE["bc"]
        == FINITE_RAW["bc"]
        - FINITE_OVERLAP["ab_bc"]
        - FINITE_OVERLAP["ac_bc"]
        + FINITE_TRIPLE
    )
    exact_total_ok = (
        exact_one_total
        == FINITE_C_PRIM // 2 - 2 * overlap_sum + 3 * FINITE_TRIPLE
    )

    checks = {
        "I_sum_equals_pi2_over_8": close(i_sum, math.pi**2 / 8.0),
        "P_sum_equals_1": close(p_sum, 1.0),
        "delta_sum_equals_0": close(sum(delta.values()), 0.0),
        "directional_projection_factor_2": directional_projection_ok,
        "projected_total_equals_C_prim": projected_total == FINITE_C_PRIM,
        "C_prim_equals_2_raw_total": FINITE_C_PRIM == 2 * raw_total,
        "directional_inclusion_exclusion": exact_directional_ok,
        "total_inclusion_exclusion": exact_total_ok,
        "limit_is_not_2_1_1": not close(p["ab"], 0.5, 1e-12),
    }

    report = {
        "metadata": {
            "stage": "13-9",
            "scope": "main structural theorem consistency audit; no new analytic theorem",
            "classification": "PASS" if all(checks.values()) else "FAIL",
        },
        "theorem": {
            "vector": "N(B) = [kappa/(3 pi^3)] (I_ab,I_ac,I_bc) B(log B)^3 + o(B(log B)^3)",
            "categorywise": "N_q(B) ~ [kappa I_q/(3 pi^3)] B(log B)^3",
            "total": "N1(B) ~ [kappa/(24 pi)] B(log B)^3",
            "normalized": "P_q(B) -> 8 I_q/pi^2",
            "stage12_bridge": "N_q(B)=(1/2)C_prim,q^proj(B)+o(B(log B)^3); N1(B)=(1/2)C_prim(B)+o(B(log B)^3)",
        },
        "archimedean": {
            "I": I,
            "I_sum": i_sum,
            "pi2_over_8": math.pi**2 / 8.0,
            "P_inf": p,
            "bc_normalized_ratio": ratio,
        },
        "deviation": {
            "baseline": {"ab": 0.5, "ac": 0.25, "bc": 0.25},
            "Delta_inf": delta,
            "alpha_inf": alpha,
            "beta_inf": beta,
        },
        "finite_B100000": {
            "C_prim": FINITE_C_PRIM,
            "projected": FINITE_PROJECTED,
            "raw": FINITE_RAW,
            "pair_overlaps": FINITE_OVERLAP,
            "triple": FINITE_TRIPLE,
            "exact_one": FINITE_EXACT_ONE,
        },
        "scope": {
            "perfect_cuboid_nonexistence_assumed": False,
            "explicit_convergence_rate_proved": False,
            "monotonicity_proved": False,
            "independent_publication_review_completed": False,
            "new_analytic_theorem_introduced_in_13_9": False,
        },
        "checks": checks,
        "status": {
            "stage13_9_complete": all(checks.values()),
            "next": "Stage13-10 final explanation" if all(checks.values()) else "repair Stage13-9",
        },
    }

    out = Path("stages/stage13/data/13-9/main_structural_theorem_audit_report.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, sort_keys=False) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=False))


if __name__ == "__main__":
    main()
