#!/usr/bin/env python3
"""Stage14-4ao: import the exact Q2 image and lock the height-weighted count.

This is a consistency/boundary audit.  It does not prove a family large-sieve
estimate or a small-point lower-tail theorem.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
ODD = ROOT / "stages/stage14/data/14-4/character_gate_matrix_summary.json"
RANK = ROOT / "stages/stage14/data/14-4/rank_smallpoint_factor_summary.json"
S3 = ROOT / "stages/stage14/data/14-s3/small_point_gate_audit.json"
OUT = ROOT / "stages/stage14/data/14-4/q2_height_weighted_descent_summary.json"

Q2_IMAGE = [
    [1, 1, 1], [3, 7, 5], [5, 1, 5], [7, 7, 1],
    [2, 1, 2], [6, 7, 10], [10, 1, 10], [14, 7, 2],
]


def main():
    odd = json.loads(ODD.read_text())
    rank = json.loads(RANK.read_text())
    s3 = json.loads(S3.read_text())

    assert len(Q2_IMAGE) == 8 and len({tuple(x) for x in Q2_IMAGE}) == 8
    assert odd["decision"]["ALL_ODD_BAD_PRIME_ROWS_EXPLICIT"] is True
    assert rank["cuts"][-1] == {
        "B": 20000, "A": 6372, "Sigma": 5209,
        "R_lower": 3784, "R_upper": 4239, "V": 54,
    }
    assert s3["decision"]["PHYSICAL_HIT_IMPLIES_LOGARITHMIC_CANONICAL_HEIGHT_WINDOW"] is True

    report = {
        "stage": "14-4ao",
        "q2": {
            "product_square_state_count": 64,
            "covering_soluble_state_count": 8,
            "covering_soluble_states": Q2_IMAGE,
        },
        "full_local_system": {
            "odd_rows_source": "merged Stage14-4an / s5c / s5d",
            "prime_2_source": "merged Stage14-s5f",
            "all_local_rows_explicit": True,
            "finite_B20000_A_to_Sigma": {
                "A": 6372,
                "Sigma": 5209,
                "Sigma_over_A": 5209 / 6372,
            },
        },
        "height_weighted_count": {
            "notation": "H_loc,glob(B;C)=sum_{F in A(B)} 1{there exists a nontrivial locally soluble 2-cover class xi, a rational point P on C_{F,xi}, and hhat(phi_xi(P)) <= C(log B+log H(F))}",
            "physical_implication": "V(B) <= H_loc,glob(B;C) for the constant C supplied by the s3 height comparison; extra physical coordinate conditions may make the inclusion strict.",
            "gate_separation": [
                "local admissibility A->Sigma",
                "global solubility / Sha Sigma->R",
                "least physical small point R->V",
            ],
            "multiplicity_rule": "count each base F once by existence, not once per Selmer class or rational point",
        },
        "finite_B20000": rank["B20000"],
        "s3_height_diagnostic": s3["finite_diagnostic"],
        "decision": {
            "STAGE14_4AO": "COMPLETE_FULL_LOCAL_MATRIX_AND_HEIGHT_WEIGHTED_COUNTING_INTERFACE",
            "Q2_COVERING_SPECIFIC_64_STATE_SOLUBILITY_CLASSIFIED": True,
            "FULL_LOCAL_2_DESCENT_CHARACTER_SYSTEM_COMPLETE": True,
            "FINITE_A_TO_SIGMA_SIEVE_QUANTIFIED": True,
            "HEIGHT_WEIGHTED_DESCENT_COUNT_FORMULATED": True,
            "GLOBAL_SOLUBILITY_AVERAGED": False,
            "FAMILY_LARGE_SIEVE_THEOREM_PROVED": False,
            "UNIFORM_FIRST_SMALL_POINT_LOWER_TAIL_PROVED": False,
            "ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED": False,
            "NEXT": "Stage14-4ap prove or sharply delimit a family character-sum estimate coupled to global solubility and the s3 height window",
        },
    }
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report["decision"], indent=2))


if __name__ == "__main__":
    main()
