#!/usr/bin/env python3
"""Stage14-4au: audit the full-local support/Fourier conversion boundary."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
AT = ROOT / "stages/stage14/data/14-4/dyadic_q_budget_summary.json"
S5B = ROOT / "stages/stage14/14-s5b/result.md"
S5C = ROOT / "stages/stage14/14-s5c/result.md"
S5D = ROOT / "stages/stage14/14-s5d/result.md"
S5F = ROOT / "stages/stage14/14-s5f/result.md"
OUT = ROOT / "stages/stage14/data/14-4/local_indicator_obstruction_summary.json"


def indicator_plus(chi: int) -> int:
    return (1 + chi) // 2


def unselected_x_indicator(chi_d2: int, chi_minus_one: int) -> int:
    # chi(d2)=+1 OR chi(-d2)=+1, with chi(-d2)=chi(-1)*chi(d2).
    return int(chi_d2 == 1 or chi_minus_one * chi_d2 == 1)


def main() -> None:
    at = json.loads(AT.read_text())
    s5b = S5B.read_text()
    s5c = S5C.read_text()
    s5d = S5D.read_text()
    s5f = S5F.read_text()

    assert at["decision"]["FIRST_QUANTITATIVE_GAP"] == "FULL_LOCAL_INDICATOR_CONVERSION"
    assert at["decision"]["E_LOC_IDENTIFIED_WITH_Q4"] is False
    assert "FIVE_MOVING_FACTORS_ODD_PAIRWISE_COPRIME=true" in s5b
    assert "p | S  => label 12" in s5c
    assert "p | X  => label 13" in s5c
    assert "p | H  => label 23" in s5c
    assert "p|S, p unselected  <=>  chi(d3)=+1" in s5d
    assert "p|H, p unselected  <=>  chi(d1)=+1" in s5d
    assert "p == 3 mod 4 : automatic" in s5d
    assert "Q2_COVERING_SOLUBLE_STATE_COUNT=8" in s5f
    assert "FULL_LOCAL_2_DESCENT_CHARACTER_SYSTEM_COMPLETE=true" in s5f

    # Exact Boolean identities used in the character expansion.
    for chi in (-1, 1):
        assert indicator_plus(chi) == int(chi == 1)
    for chi_d2 in (-1, 1):
        for chi_minus_one in (-1, 1):
            direct = unselected_x_indicator(chi_d2, chi_minus_one)
            reduced = 1 if chi_minus_one == -1 else indicator_plus(chi_d2)
            assert direct == reduced

    # Height scale: four linear Euclid factors are O(B^(1/2)) and the
    # quadratic factor is O(B), so their product is O(B^3).
    factor_B_exponents = [0.5, 0.5, 0.5, 0.5, 1.0]
    assert sum(factor_B_exponents) == 3.0

    report = {
        "stage": "14-4au",
        "classification": "FULL_LOCAL_INDICATOR_EXPANDED_AND_RECIPROCAL_OFF_DIAGONAL_OBSTRUCTION_ISOLATED",
        "support_count_interface": {
            "five_factors": ["m", "n", "m-n", "m+n", "m^2+n^2"],
            "odd_support_pairwise_disjoint": True,
            "selected_labels": {
                "m,n": "13",
                "m-n,m+n": "12",
                "m^2+n^2": "23",
            },
            "q2_exact_state_count": 8,
            "N_loc_F": "sum over nontrivial descent states xi of L_F(xi)",
            "base_indicator_identity": "s(F)=1_{N_loc(F)>=1}",
            "nonnegative_upper_bound": "s(F)<=N_loc(F)",
            "state_count_bound": "8*2^omega(P_F)",
            "P_F": "rad_odd(m*n*(m-n)*(m+n)*(m^2+n^2))",
            "P_F_size_on_height_B": "O(B^3)",
            "support_multiplicity_scale": "B^o(1)",
        },
        "boolean_fourier_interface": {
            "odd_row_form": "finite Boolean polynomial in quadratic-character bits",
            "fixed_support_expansion": "L_F(xi)=1_Q2 * sum_omega c_{xi,omega} X_{xi,omega}(F)",
            "coefficient_bound": "|c_{xi,omega}|<=1",
            "constant_mode": "diagonal/main contribution",
            "nonconstant_modes": "products of off-diagonal Jacobi symbols (u_i/u_j), i!=j, plus explicit mod-4 bits",
            "reciprocity_source": "Stage14-s5b/s5c/s5d",
        },
        "dyadic_nonnegative_conversion": {
            "exact_support_sum_split": "sum_F W(F)N_loc(F)=D_loc+sum_{omega!=0} B_omega",
            "rigorous_upper_bound": "S_W<=D_loc+sum_{omega!=0}|B_omega|",
            "transfer_contract": {
                "diagonal": "D_loc<=rho_diag*A_W+E_diag",
                "reciprocal": "sum|B_omega|<=E_rec",
                "local_input": "rho_loc=rho_diag; E_loc=E_diag+E_rec",
            },
            "independence_assumption": False,
        },
        "representative_obstruction": {
            "shape": "sum_{m~M,n~N} w_mn sum_{u|rad(F_i),u~U} sum_{v|rad(F_j),v~V} a_{u;mn} b_{v;mn} (u/v), i!=j",
            "correlation": "u and v divide two columns of the same polynomial tuple; coefficients retain complementary divisor pieces, remaining local rows, and Q2 state",
            "free_coefficient_quadratic_large_sieve_directly_applicable": False,
            "s5g_prime_level_second_moment_sufficient": False,
            "sufficient_target": "each nonconstant block << (MN)^(1-eta_rec+o(1)) uniformly with summable B^o(1) losses",
            "target_proved": False,
        },
        "q_budget_boundary": {
            "stage14_4at_benchmark_Q": "B^(1/4-eta)",
            "Q4_is_second_moment_cost_not_E_loc": True,
            "first_gap_refined_to": "RECIPROCAL_DIVISOR_OFF_DIAGONAL_BILINEAR_BOUND",
        },
        "decision": {
            "STAGE14_4AU": "FULL_LOCAL_INDICATOR_EXPANDED_AND_RECIPROCAL_OFF_DIAGONAL_OBSTRUCTION_ISOLATED",
            "BASE_EXISTENCE_TO_NONNEGATIVE_SUPPORT_COUNT": True,
            "SUPPORT_MULTIPLICITY_B_TO_O1": True,
            "ALL_ODD_ROWS_BOOLEAN_CHARACTER_POLYNOMIALS": True,
            "FULL_FIXED_SUPPORT_FOURIER_EXPANSION_FORMULATED": True,
            "CONSTANT_MODE_VS_RECIPROCAL_OFF_DIAGONAL_SPLIT": True,
            "LOCAL_RHO_E_TRANSFER_FROM_DIAGONAL_AND_RECIPROCAL_BOUNDS": True,
            "S5G_PRIME_LEVEL_SECOND_MOMENT_CONTROLS_FULL_INDICATOR": False,
            "RECIPROCAL_DIVISOR_BILINEAR_BOUND_PROVED": False,
            "EXPLICIT_NONTRIVIAL_RHO_LOC_PROVED": False,
            "EXPLICIT_E_LOC_PROVED": False,
            "POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED": False,
            "POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED": False,
            "ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED": False,
            "NEXT": "Stage14-4av dyadically factor the reciprocal-divisor blocks into quadratic-character bilinear forms with controlled correlated coefficients, then prove a first uniform block estimate or identify the remaining coefficient-correlation obstruction",
        },
    }

    OUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report["decision"], indent=2))


if __name__ == "__main__":
    main()
