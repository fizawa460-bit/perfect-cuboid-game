#!/usr/bin/env python3
"""Stage13-7jg: final consistency audit for the Stage13-7 theorem chain.

This script does not introduce a new analytic theorem.  It cross-checks the
already proved Stage13-7j/ja/jb/jc/jd/je/jf reports and records the exact
logical status of superseded intermediate claims.

The final theorem is the exactly-one category asymptotic

    N_q(B) ~ [kappa I_q/(3 pi^3)] B(log B)^3,

with normalized limit 8 I_q/pi^2.  The pair/triple overlap correction is lower
order by the fixed-prime sieve of 7jf, so the Stage13-7 asymptotic-deviation
question is resolved at the same standard-theorem-application level as the
frozen Stage12 input.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path("stages/stage13/data/13-7")
PURE = ROOT / "individual_category_asymptotic_report.json"
SUPPORT = ROOT / "primitive_support_scale_report.json"
RAW = ROOT / "supported_richness_raw_asymptotic_report.json"
OVERLAP = ROOT / "overlap_face_cuboid_reduction_report.json"
HEIGHT = ROOT / "face_cuboid_uniform_height_report.json"
KUMMER = ROOT / "face_cuboid_coupled_kummer_report.json"
EXACT = ROOT / "exact_one_fixed_prime_sieve_report.json"
OUT = ROOT / "consolidation_audit_report.json"

TOL = 5e-13


def close(a: float, b: float, tol: float = TOL) -> bool:
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


def vector_close(a: dict, b: dict, tol: float = TOL) -> bool:
    return all(close(float(a[q]), float(b[q]), tol) for q in ("ab", "ac", "bc"))


def build_report() -> dict:
    pure = json.loads(PURE.read_text())
    support = json.loads(SUPPORT.read_text())
    raw = json.loads(RAW.read_text())
    overlap = json.loads(OVERLAP.read_text())
    height = json.loads(HEIGHT.read_text())
    kummer = json.loads(KUMMER.read_text())
    exact = json.loads(EXACT.read_text())

    I = pure["stage13_3b_bridge"]["I_stage13_3b"]
    I_sum = sum(float(I[q]) for q in ("ab", "ac", "bc"))
    assert close(I_sum, math.pi**2 / 8.0)

    P_expected = {q: 8.0 * float(I[q]) / math.pi**2 for q in ("ab", "ac", "bc")}
    P_pure = pure["normalized_limit"]["proportion"]
    P_raw = raw["raw_normalized_limit"]["proportion"]
    P_exact = exact["exact_one_asymptotics"]["normalized_proportion"]
    assert vector_close(P_pure, P_expected)
    assert vector_close(P_raw, P_expected)
    assert vector_close(P_exact, P_expected)
    assert close(sum(P_expected.values()), 1.0)

    K = {
        q: float(pure["individual_leading_constants"][q]["numeric_truncation"])
        for q in ("ab", "ac", "bc")
    }
    C = {q: 8.0 * float(I[q]) / math.pi**3 for q in ("ab", "ac", "bc")}
    lambdas = {q: K[q] / C[q] for q in ("ab", "ac", "bc")}
    assert max(lambdas.values()) - min(lambdas.values()) < 5e-15
    assert close(sum(C.values()), 1.0 / math.pi)
    assert close(lambdas["ab"], math.pi * sum(K.values()))

    # Use the support report as an independent cross-check of the common scale factor.
    support_lambda = float(support["primitive_support_transition"]["Lambda_numeric"])
    assert close(lambdas["ab"], support_lambda)

    kappa_diag = float(raw["frozen_stage12_total"]["kappa_prime_product_diagnostic"])
    D = {
        q: float(raw["individual_raw_asymptotics"][q]["numeric_prime_product_diagnostic"])
        for q in ("ab", "ac", "bc")
    }
    D_formula = {q: kappa_diag * float(I[q]) / (3.0 * math.pi**3) for q in ("ab", "ac", "bc")}
    assert vector_close(D, D_formula)
    assert close(sum(D.values()), kappa_diag / (24.0 * math.pi))

    omega = {q: D[q] / K[q] for q in ("ab", "ac", "bc")}
    assert max(omega.values()) - min(omega.values()) < 5e-18

    alpha = P_expected["ab"] - 0.5
    beta = (P_expected["ac"] - P_expected["bc"]) / 2.0
    delta = {
        "ab": P_expected["ab"] - 0.5,
        "ac": P_expected["ac"] - 0.25,
        "bc": P_expected["bc"] - 0.25,
    }
    assert close(alpha, float(exact["exact_one_asymptotics"]["alpha_limit"]))
    assert close(beta, float(exact["exact_one_asymptotics"]["beta_limit"]))
    assert close(sum(delta.values()), 0.0)

    # Logical dependency / supersession checks.
    assert overlap["status"]["pair_overlap_lower_order_proved"] is False
    assert height["status"]["pair_overlap_lower_order_proved"] is False
    assert kummer["status"]["pair_overlap_lower_order_proved"] is False
    assert exact["status"]["pair_overlap_lower_order_proved"] is True
    assert exact["status"]["triple_overlap_lower_order_proved"] is True
    assert exact["status"]["exact_one_directional_limit_identified"] is True
    assert exact["status"]["perfect_cuboid_nonexistence_assumed"] is False

    # The 7jf squeeze must use fixed k before B->infinity.
    order = exact["fixed_congruence_refinement"]["important_order_of_limits"]
    assert "hold them fixed" in order and "B->infinity" in order and "k->infinity" in order

    # The tagged orientation must be one universal copy, not a factor-two main term.
    tagged = exact["tagged_pair_overlap_bridge"]
    assert "exactly one tagged orientation" in tagged["statement"]
    assert "No variable multiplicity" in tagged["orientation_factor"]

    ratio = {q: P_expected[q] / P_expected["bc"] for q in ("ab", "ac", "bc")}

    finite_alpha = 131.0 / 168030.0
    finite_beta = 619.0 / 84015.0

    return {
        "metadata": {
            "stage": "13-7jg",
            "scope": "final theorem-chain consistency audit and supersession ledger; no new analytic input",
            "classification": "PASS_AT_EXISTING_STAGE12_STANDARD_THEOREM_APPLICATION_LEVEL",
        },
        "final_exact_one_theorem": {
            "category_scale": "B(log B)^3",
            "category_constants": {
                "ab": "kappa I_ab/(3 pi^3)",
                "ac": "kappa I_ac/(3 pi^3)",
                "bc": "kappa I_bc/(3 pi^3)",
            },
            "total": "N1(B) ~ [kappa/(24 pi)] B(log B)^3",
            "normalized_proportion": P_expected,
            "bc_normalized_ratio": ratio,
            "alpha_limit": alpha,
            "beta_limit": beta,
            "delta_limit": delta,
            "delta_l1": sum(abs(v) for v in delta.values()),
            "limit_is_2_1_1": False,
            "perfect_cuboid_nonexistence_assumed": False,
        },
        "scale_ladder": {
            "preprimitive_m1": {
                "scale": "B log B",
                "constants": C,
                "total_constant": 1.0 / math.pi,
                "normalized_limit": P_expected,
            },
            "primitive_pure_G": {
                "scale": "B(log B)^(1/3)",
                "constants_numeric_prime_product_diagnostic": K,
                "primitive_support_survival_constant": lambdas["ab"],
                "normalized_limit": P_expected,
            },
            "primitive_raw_incidence": {
                "scale": "B(log B)^3",
                "constants_numeric_using_stage12_kappa_diagnostic": D,
                "pure_G_to_raw_common_scaled_amplification": omega["ab"],
                "normalized_limit": P_expected,
            },
            "primitive_exact_one": {
                "scale": "B(log B)^3",
                "leading_constants_equal_raw": True,
                "normalized_limit": P_expected,
            },
        },
        "supersession_ledger": {
            "13-7j": "pure-G-only guardrails are historical; raw and exact-one limits are now identified",
            "13-7ja": "its statement that primitive support changes scale but not normalized vector remains active",
            "13-7jb": "raw directional theorem remains active and supplies the exact-one main term",
            "13-7jc": "its conditional requirement F(B)=o(B(log B)^3) is discharged by 13-7jf",
            "13-7jd": "its B*exp(C log B/loglog B) face-cuboid upper bound remains valid but is superseded in strength by 13-7jf",
            "13-7je": "its Kummer/coupled-height reduction remains valid structural information but is not needed in the shortest final proof",
            "13-7jf": "fixed-prime sieve is the active overlap theorem; fixed modulus first, B limit second, number of primes last",
        },
        "finite_vs_asymptotic_interpretation": {
            "B100000_exact_one_alpha": finite_alpha,
            "B100000_exact_one_beta": finite_beta,
            "limit_alpha": alpha,
            "limit_beta": beta,
            "finite_beta_over_alpha": finite_beta / finite_alpha,
            "limit_alpha_over_beta": alpha / beta,
            "conclusion": (
                "The near-2:1:1 vector at accessible cutoffs is pre-asymptotically flattened. "
                "The proved limiting deviation is nonzero and alpha-dominated relative to the B=100000 regime."
            ),
            "rate_claimed": "only o(1) after normalization; no monotonicity or explicit secondary convergence rate is claimed",
        },
        "audit_checks": {
            "I_sum_equals_pi2_over_8": True,
            "all_four_normalized_layers_share_chamber_limit": True,
            "primitive_support_constant_category_independent": True,
            "raw_amplification_constant_category_independent": True,
            "raw_constants_sum_to_stage12_half_projection_total": True,
            "tagged_orientation_factor_audited": True,
            "fixed_prime_order_of_limits_audited": True,
            "conditional_overlap_requirement_discharged": True,
        },
        "status": {
            "stage13_7_complete": True,
            "asymptotic_deviation_resolved": True,
            "alpha_limit_identified": True,
            "beta_limit_identified": True,
            "delta_limit_identified": True,
            "exact_one_directional_limit_unconditional": True,
            "independent_publication_review_completed": False,
            "next": "Stage13-8",
        },
    }


def main() -> None:
    report = build_report()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report["status"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
