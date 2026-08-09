#!/usr/bin/env python3
"""Stage14-4ap: lock the reach of local character sums and transfer gates."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
Q2 = ROOT / "stages/stage14/data/14-4/q2_height_weighted_descent_summary.json"
RANK = ROOT / "stages/stage14/data/14-4/rank_smallpoint_factor_summary.json"
S3 = ROOT / "stages/stage14/data/14-s3/small_point_gate_audit.json"
S5G = ROOT / "stages/stage14/14-s5g/result.md"
OUT = ROOT / "stages/stage14/data/14-4/character_global_height_transfer_summary.json"


def main():
    q2 = json.loads(Q2.read_text())
    rank = json.loads(RANK.read_text())
    s3 = json.loads(S3.read_text())
    s5g = S5G.read_text()

    assert q2["decision"]["FULL_LOCAL_2_DESCENT_CHARACTER_SYSTEM_COMPLETE"] is True
    assert q2["decision"]["GLOBAL_SOLUBILITY_AVERAGED"] is False
    assert rank["cuts"][-1] == {
        "B": 20000, "A": 6372, "Sigma": 5209,
        "R_lower": 3784, "R_upper": 4239, "V": 54,
    }
    assert s3["decision"]["SMALL_POINT_GATE_IS_GENUINE"] is True
    assert s3["decision"]["UNIFORM_SMALL_POINT_DISTRIBUTION_PROVED"] is False
    assert "EXACT_LOCAL_MEAN_SUBTRACTION_REQUIRED=true" in s5g
    assert "FAMILY_LARGE_SIEVE_THEOREM_PROVED=false" in s5g

    # Exponent bookkeeping only: if A(B) << B and the three retainers are
    # O(B^-delta_i), then H(B;C) << B^(1-sum(delta_i)).
    threshold = 0.5
    report = {
        "stage": "14-4ap",
        "classification": "RIGOROUS_GATE_DELIMITATION_AND_CONDITIONAL_TRANSFER_ONLY",
        "gate_chain": {
            "N0": "A(B): eligible primitive opposite-parity Euclid pairs",
            "N1": "Sigma(B): bases surviving the full local 2-descent system",
            "N2": "R(B): bases with a globally soluble nontrivial class / positive rank",
            "N3": "H(B;C): bases with a globally soluble class in the s3 height window",
            "identity": "N3=N0*(N1/N0)*(N2/N1)*(N3/N2), with zero-denominator ratios interpreted as zero",
        },
        "local_character_input": {
            "source": "merged Stage14-s5g",
            "exact_local_mean_subtraction_required": True,
            "controls": "the local-admissibility retainer N1/N0 only",
            "does_not_determine": ["global solubility / Sha (N2/N1)", "first-small-point height (N3/N2)"],
        },
        "conditional_transfer": {
            "hypotheses": [
                "N0(B) << B",
                "N1/N0 << B^(-delta_local)",
                "N2/N1 << B^(-delta_global)",
                "N3/N2 << B^(-delta_height)",
            ],
            "conclusion": "H(B;C) << B^(1-delta_local-delta_global-delta_height)",
            "physical_consequence": "V(B)<=H(B;C), so the same conditional upper bound transfers to V(B)",
            "square_root_threshold": "delta_local+delta_global+delta_height >= 1/2",
            "threshold": threshold,
        },
        "finite_B20000": {
            "A": 6372,
            "Sigma": 5209,
            "R_interval": [3784, 4239],
            "V": 54,
            "Sigma_over_A": 5209 / 6372,
            "V_over_R_interval": [54 / 4239, 54 / 3784],
            "interpretation": "finite diagnostic only; no retainer is assigned an asymptotic exponent",
        },
        "decision": {
            "STAGE14_4AP": "LOCAL_CHARACTER_REACH_AND_CONDITIONAL_GLOBAL_HEIGHT_TRANSFER_BOUNDARY",
            "EXACT_LOCAL_MEAN_SUBTRACTION_REQUIRED": True,
            "LOCAL_CHARACTERS_DETERMINE_GLOBAL_SOLUBILITY": False,
            "LOCAL_CHARACTERS_DETERMINE_FIRST_SMALL_POINT_HEIGHT": False,
            "LOCAL_LARGE_SIEVE_ALONE_CONTROLS_HEIGHT_WEIGHTED_COUNT": False,
            "CONDITIONAL_THREE_RETAINER_TRANSFER_FORMULATED": True,
            "FAMILY_LARGE_SIEVE_THEOREM_PROVED": False,
            "GLOBAL_SOLUBILITY_AVERAGED": False,
            "UNIFORM_FIRST_SMALL_POINT_LOWER_TAIL_PROVED": False,
            "ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED": False,
            "NEXT": "Stage14-4aq isolate the global-solubility/Sha retainer and formulate a uniform averaging target compatible with the centered local sieve",
        },
    }
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report["decision"], indent=2))


if __name__ == "__main__":
    main()
