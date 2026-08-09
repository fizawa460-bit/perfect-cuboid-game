#!/usr/bin/env python3
"""Stage14-4ar: isolate the positive-rank to first-small-point retainer."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
RANK = ROOT / "stages/stage14/data/14-4/rank_smallpoint_factor_summary.json"
S3 = ROOT / "stages/stage14/data/14-s3/small_point_gate_audit.json"
AQ = ROOT / "stages/stage14/14-4aq/result.md"
OUT = ROOT / "stages/stage14/data/14-4/small_point_retainer_summary.json"


def main():
    rank = json.loads(RANK.read_text())
    s3 = json.loads(S3.read_text())
    aq = AQ.read_text()

    assert rank["decision"]["ACTIVATION_DENSITY_THREE_GATE_FACTORIZATION_LOCKED"] is True
    assert s3["decision"]["PHYSICAL_HIT_IMPLIES_LOGARITHMIC_CANONICAL_HEIGHT_WINDOW"] is True
    assert s3["decision"]["SMALL_POINT_GATE_IS_GENUINE"] is True
    assert s3["decision"]["UNIFORM_SMALL_POINT_DISTRIBUTION_PROVED"] is False
    assert "STAGE14_4AQ=GLOBAL_SHA_RETAINER_ISOLATED_AND_WEIGHTED_TARGET_FORMULATED" in aq

    finite = []
    for row in rank["cuts"]:
        B = row["B"]
        lo = row["R_lower"]
        hi = row["R_upper"]
        V = row["V"]
        finite.append({
            "B": B,
            "R_interval": [lo, hi],
            "V": V,
            "physical_V_over_R_interval": [V / hi, V / lo],
            "height_retainer_information": "V<=H_C<=R, so complete data give only V/R <= H_C/R <= 1",
        })

    diag = s3["finite_diagnostic"]
    report = {
        "stage": "14-4ar",
        "classification": "FIRST_SMALL_POINT_RETAINER_ISOLATED_AND_WEIGHTED_LOWER_TAIL_TARGET_FORMULATED",
        "minimum_height_interface": {
            "lambda_F": "minimum canonical height among non-torsion points on E_F(Q), with +infinity at rank zero",
            "h_BC_F": "1_{lambda(F) <= C(log B + log H(F))}",
            "u_BC_F": "r(F)-h_BC(F)",
            "aggregate_identity": "H_C(B)=R(B)-U_C(B)",
            "physical_inclusion": "for any fixed admissible s3 comparison constant C, V(B)<=H_C(B)",
            "converse_claimed": False,
        },
        "centered_local_compatible_weighted_target": {
            "weight": "any nonnegative W_Q(F) compatible with the centered full-local sieve; no independence assumption",
            "R_Q": "sum_F W_Q(F) r(F)",
            "H_Q_C": "sum_F W_Q(F) h_BC(F)",
            "U_Q_C": "sum_F W_Q(F) u_BC(F)",
            "exact_identity": "H_Q_C=R_Q-U_Q_C",
            "uniform_lower_tail_target": "H_Q_C <= rho_ht(B,Q,C) R_Q + E_ht(B,Q,C), uniformly in dyadic Euclid boxes and allowed weights",
            "equivalent_large_minimum_target": "U_Q_C >= (1-rho_ht(B,Q,C)) R_Q - E_ht(B,Q,C)",
            "power_saving_transfer": "rho_ht << B^(-delta_ht) with negligible error contributes delta_ht to the 4ap exponent budget",
            "constant_density_boundary": "rho_ht=O(1) contributes no B-power saving",
        },
        "finite_complete_census": finite,
        "s3_sample_diagnostic": {
            "active_actual_first_hit_canonical_height": diag["active_actual_first_hit_canonical_height"],
            "active_canonical_height_over_log_mu": diag["active_canonical_height_over_log_mu"],
            "inactive_positive_rank_controls_with_witness": diag["inactive_controls_with_certified_positive_rank_and_pari_witness"],
            "inactive_found_witness_canonical_height": diag["inactive_found_witness_canonical_height"],
            "boundary": "inactive witnesses are not certified minima; sample diagnostics do not estimate H_C/R",
        },
        "decision": {
            "STAGE14_4AR": "FIRST_SMALL_POINT_RETAINER_ISOLATED_AND_WEIGHTED_LOWER_TAIL_TARGET_FORMULATED",
            "MINIMUM_NON_TORSION_CANONICAL_HEIGHT_INTERFACE_LOCKED": True,
            "PHYSICAL_HIT_IMPLIES_HEIGHT_RETAINER": True,
            "HEIGHT_RETAINER_EXACT_COMPLEMENT_IDENTITY": True,
            "CENTERED_LOCAL_WEIGHTED_HEIGHT_IDENTITY": True,
            "UNIFORM_WEIGHTED_SMALL_POINT_LOWER_TAIL_TARGET_FORMULATED": True,
            "HEIGHT_RETAINER_FINITE_COMPLETE_CENSUS_MEASURED": False,
            "UNIFORM_FIRST_SMALL_POINT_LOWER_TAIL_PROVED": False,
            "POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED": False,
            "FAMILY_LARGE_SIEVE_THEOREM_PROVED": False,
            "ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED": False,
            "NEXT": "Stage14-4as synthesize the local, global/Sha, and first-small-point weighted retainers into one end-to-end theorem target without assuming independence",
        },
    }
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report["decision"], indent=2))


if __name__ == "__main__":
    main()
