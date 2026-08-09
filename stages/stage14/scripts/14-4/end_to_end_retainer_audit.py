#!/usr/bin/env python3
"""Stage14-4as: audit the exact end-to-end weighted-retainer recursion."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
AP = ROOT / "stages/stage14/data/14-4/character_global_height_transfer_summary.json"
AQ = ROOT / "stages/stage14/data/14-4/global_sha_retainer_summary.json"
AR = ROOT / "stages/stage14/data/14-4/small_point_retainer_summary.json"
OUT = ROOT / "stages/stage14/data/14-4/end_to_end_retainer_summary.json"


def main():
    ap = json.loads(AP.read_text())
    aq = json.loads(AQ.read_text())
    ar = json.loads(AR.read_text())

    assert ap["decision"]["CONDITIONAL_THREE_RETAINER_TRANSFER_FORMULATED"] is True
    assert ap["decision"]["EXACT_LOCAL_MEAN_SUBTRACTION_REQUIRED"] is True
    assert aq["decision"]["CENTERED_LOCAL_WEIGHTED_GLOBAL_IDENTITY"] is True
    assert aq["decision"]["POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED"] is False
    assert ar["decision"]["CENTERED_LOCAL_WEIGHTED_HEIGHT_IDENTITY"] is True
    assert ar["decision"]["HEIGHT_RETAINER_FINITE_COMPLETE_CENSUS_MEASURED"] is False

    finite = ap["finite_B20000"]
    assert finite["A"] == 6372
    assert finite["Sigma"] == 5209
    assert finite["R_interval"] == [3784, 4239]
    assert finite["V"] == 54

    # Algebraic regression check for the recursive transfer.  No probability
    # or independence assumption is used: substitute the three one-step upper
    # bounds in order.
    rho_loc, rho_glob, rho_ht = 0.8, 0.7, 0.1
    A, e_loc, e_glob, e_ht = 1000.0, 9.0, 7.0, 5.0
    recursive = (
        rho_ht * rho_glob * rho_loc * A
        + rho_ht * rho_glob * e_loc
        + rho_ht * e_glob
        + e_ht
    )
    S_bound = rho_loc * A + e_loc
    R_bound = rho_glob * S_bound + e_glob
    sequential = rho_ht * R_bound + e_ht
    assert abs(recursive - sequential) < 1e-12

    report = {
        "stage": "14-4as",
        "classification": "END_TO_END_WEIGHTED_RETAINER_THEOREM_TARGET_SYNTHESIZED",
        "weighted_chain": {
            "A_Q": "sum_F W_Q(F)",
            "S_Q": "sum_F W_Q(F) s(F)",
            "R_Q": "sum_F W_Q(F) r(F)",
            "H_Q_C": "sum_F W_Q(F) h_BC(F)",
            "nesting": "0 <= H_Q_C <= R_Q <= S_Q <= A_Q",
            "factorization": "H_Q_C/A_Q=(S_Q/A_Q)(R_Q/S_Q)(H_Q_C/R_Q), with zero-denominator ratios interpreted as zero",
            "independence_required": False,
        },
        "three_targets": {
            "local": "S_Q <= rho_loc A_Q + E_loc",
            "global_sha": "R_Q <= rho_glob S_Q + E_glob",
            "height": "H_Q_C <= rho_ht R_Q + E_ht",
        },
        "recursive_transfer": {
            "bound": "H_Q_C <= rho_ht rho_glob rho_loc A_Q + rho_ht rho_glob E_loc + rho_ht E_glob + E_ht",
            "main_exponent": "if A_Q<<B^(1+o(1)) and rho_i<<B^(-delta_i+o(1)), main exponent is 1-delta_loc-delta_glob-delta_ht+o(1)",
            "sqrt_main_threshold": "delta_loc+delta_glob+delta_ht >= 1/2",
            "sqrt_error_requirements": [
                "rho_ht rho_glob E_loc = O(B^(1/2+o(1)))",
                "rho_ht E_glob = O(B^(1/2+o(1)))",
                "E_ht = O(B^(1/2+o(1)))",
            ],
        },
        "physical_transfer": {
            "unweighted_specialization": "W_Q(F)=1 recovers H_C=A*(Sigma/A)*(R/Sigma)*(H_C/R)",
            "inclusion": "V(B)<=H_C(B)",
            "warning": "a signed centered-trace cancellation estimate alone is not automatically an upper bound for V(B)",
        },
        "finite_B20000": {
            "A": 6372,
            "Sigma": 5209,
            "R_interval": [3784, 4239],
            "V": 54,
            "H_C_complete_census_measured": False,
            "interpretation": "no asymptotic delta_i is inferred and V/R is not identified with H_C/R",
        },
        "decision": {
            "STAGE14_4AS": "END_TO_END_WEIGHTED_RETAINER_THEOREM_TARGET_SYNTHESIZED",
            "COMMON_NONNEGATIVE_WEIGHTED_FAMILY_LOCKED": True,
            "WEIGHTED_THREE_GATE_FACTORIZATION_EXACT": True,
            "INDEPENDENCE_ASSUMPTION_REQUIRED": False,
            "RECURSIVE_THREE_RETAINER_TRANSFER_EXACT": True,
            "PROPAGATED_ERROR_BUDGET_EXPLICIT": True,
            "PHYSICAL_TRANSFER_REQUIRES_UNWEIGHTED_OR_DOMINATING_INSTANTIATION": True,
            "FAMILY_LARGE_SIEVE_THEOREM_PROVED": False,
            "POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED": False,
            "UNIFORM_FIRST_SMALL_POINT_LOWER_TAIL_PROVED": False,
            "POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED": False,
            "ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED": False,
            "NEXT": "Stage14-4at instantiate the end-to-end target on the dyadic Euclid decomposition, choose Q(B), and expose the first quantitatively insufficient retainer or propagated error",
        },
    }

    committed = json.loads(OUT.read_text())
    assert committed == report
    print(json.dumps(report["decision"], indent=2))


if __name__ == "__main__":
    main()
