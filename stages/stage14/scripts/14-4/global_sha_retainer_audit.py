#!/usr/bin/env python3
"""Stage14-4aq: isolate the global-solubility/Sha retainer."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
RANK = ROOT / "stages/stage14/data/14-4/rank_smallpoint_factor_summary.json"
Q2 = ROOT / "stages/stage14/data/14-4/q2_height_weighted_descent_summary.json"
S5G = ROOT / "stages/stage14/14-s5g/result.md"
OUT = ROOT / "stages/stage14/data/14-4/global_sha_retainer_summary.json"


def main():
    rank = json.loads(RANK.read_text())
    q2 = json.loads(Q2.read_text())
    s5g = S5G.read_text()

    assert q2["decision"]["FULL_LOCAL_2_DESCENT_CHARACTER_SYSTEM_COMPLETE"] is True
    assert q2["decision"]["GLOBAL_SOLUBILITY_AVERAGED"] is False
    assert "EXACT_LOCAL_MEAN_SUBTRACTION_REQUIRED=true" in s5g
    assert "FAMILY_LARGE_SIEVE_THEOREM_PROVED=false" in s5g

    finite = []
    for row in rank["cuts"]:
        sigma = row["Sigma"]
        r_lo = row["R_lower"]
        r_hi = row["R_upper"]
        assert 0 <= r_lo <= r_hi <= sigma <= row["A"]
        trap_lo = sigma - r_hi
        trap_hi = sigma - r_lo
        finite.append({
            "B": row["B"],
            "A": row["A"],
            "Sigma": sigma,
            "R_interval": [r_lo, r_hi],
            "Sha_trap_base_interval": [trap_lo, trap_hi],
            "R_over_Sigma_interval": [r_lo / sigma, r_hi / sigma],
            "Sha_trap_over_Sigma_interval": [trap_lo / sigma, trap_hi / sigma],
            "V": row["V"],
        })
        assert r_lo + trap_hi == sigma
        assert r_hi + trap_lo == sigma

    report = {
        "stage": "14-4aq",
        "classification": "GLOBAL_SHA_RETAINER_ISOLATED_AND_WEIGHTED_TARGET_FORMULATED",
        "exact_sequence": {
            "sequence": "0 -> E(Q)/2E(Q) -> Sel_2(E) -> Sha(E)[2] -> 0",
            "full_rational_2_torsion_dimension": 2,
            "dimension_identity": "dim Sel_2(E)=2+rank(E(Q))+dim Sha(E)[2]",
            "base_indicators": {
                "s(F)": "1_{dim Sel_2(E_F)>2}",
                "r(F)": "1_{rank E_F(Q)>0}",
                "tau(F)": "s(F)-r(F)=1 exactly for rank-zero Selmer-excess / Sha[2] trap bases",
            },
            "aggregate_identity": "R(B)=Sigma(B)-T_Sha(B)",
            "retainer_identity": "R/Sigma=1-T_Sha/Sigma when Sigma>0",
        },
        "centered_local_compatible_target": {
            "weight": "any nonnegative W_Q(F) built from the full centered local 2-descent sieve",
            "weighted_counts": {
                "S_Q": "sum_F W_Q(F) s(F)",
                "G_Q": "sum_F W_Q(F) r(F)",
                "T_Q": "sum_F W_Q(F) tau(F)",
            },
            "exact_weighted_identity": "G_Q=S_Q-T_Q",
            "uniform_target": "G_Q <= rho_glob(B,Q) S_Q + E_glob(B,Q), uniformly in dyadic Euclid boxes and centered-local weights",
            "equivalent_sha_target": "T_Q >= (1-rho_glob(B,Q)) S_Q - E_glob(B,Q)",
            "transfer_if_power_saving": "rho_glob << B^(-delta_global) with negligible error contributes delta_global to the 4ap exponent budget",
            "constant_density_boundary": "rho_glob=O(1) contributes no B-power saving",
        },
        "finite_census": finite,
        "finite_interpretation": "Sha-trap population is substantial at all audited cutoffs; no positive global saving exponent is inferred",
        "decision": {
            "STAGE14_4AQ": "GLOBAL_SHA_RETAINER_ISOLATED_AND_WEIGHTED_TARGET_FORMULATED",
            "SEL2_EXACT_SEQUENCE_IMPORTED": True,
            "SHA_TRAP_INDICATOR_EXACT": True,
            "GLOBAL_RETAINER_IDENTITY_R_EQ_SIGMA_MINUS_SHA_TRAP": True,
            "CENTERED_LOCAL_WEIGHTED_GLOBAL_IDENTITY": True,
            "GLOBAL_RETAINER_UNIFORM_AVERAGING_TARGET_FORMULATED": True,
            "GLOBAL_SOLUBILITY_DENSITY_PROVED": False,
            "POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED": False,
            "FAMILY_LARGE_SIEVE_THEOREM_PROVED": False,
            "UNIFORM_FIRST_SMALL_POINT_LOWER_TAIL_PROVED": False,
            "ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED": False,
            "NEXT": "Stage14-4ar isolate the positive-rank-to-first-small-point retainer and formulate a uniform weighted lower-tail target using the s3 height window",
        },
    }
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report["decision"], indent=2))


if __name__ == "__main__":
    main()
