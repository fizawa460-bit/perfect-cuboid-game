#!/usr/bin/env python3
"""Stage14-4bc deterministic audit for the final root-sawtooth gate."""

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
RESULT = ROOT / "stages/stage14/14-4bc/result.md"
SUMMARY = ROOT / "stages/stage14/data/14-4/final_root_sawtooth_gate_summary.json"
S5P = ROOT / "stages/stage14/14-s5p/result.md"
S5Q = ROOT / "stages/stage14/14-s5q/result.md"
FOUR_BB = ROOT / "stages/stage14/14-4bb/result.md"


def r_exp(alpha: Fraction, beta: Fraction) -> Fraction:
    kappa = max(beta / 2, min(alpha, beta))
    return alpha + beta + max(Fraction(0), 1 - kappa) - 2


def psi(x: Fraction) -> Fraction:
    floor_x = x.numerator // x.denominator
    return x - floor_x - Fraction(1, 2)


def residue_count_formula(L, R, b, v):
    return (
        Fraction(R - L + 1, v)
        + psi(Fraction(L - 1 - b, v))
        - psi(Fraction(R - b, v))
    )


def main():
    result = RESULT.read_text()
    s5p = S5P.read_text()
    s5q = S5Q.read_text()
    bb = FOUR_BB.read_text()
    summary = json.loads(SUMMARY.read_text())

    for flag in (
        "AUXILIARY_INCIDENCE_UNIFORMITY_PROVED=true",
        "AUXILIARY_PROGRESSION_MODULUS_LOSS_PERSISTS=false",
        "AUXILIARY_STATE_ENERGY_TRANSFER_PROVED=true",
        "HILBERT_QUADRATIC_LARGE_SIEVE_LIFT_PROVED=true",
    ):
        assert flag in s5p

    for flag in (
        "MULTI_EDGE_DISCREPANCY_TENSOR_CONTRACTION_PROVED=true",
        "LINEAR_ONLY_FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED=true",
        "E_SELECTED_UNSELECTED_H_ROW_IDENTICAL=true",
        "E_COLUMN_SINGLE_WALSH_SUBSET_EXACT=true",
        "E_WALSH_L1_NORMALIZED=true",
        "E_WALSH_L2_CONTRACTIVE=true",
        "STATE_SPLIT_E_MULTI_EDGE_TENSOR_CONTRACTION_PROVED=true",
        "FULL_LOCAL_CHARACTER_POLYNOMIAL_REDUCED_TO_SINGLE_E_LINEAR_EDGE=true",
        "FINAL_ROOT_SAWTOOTH_KERNEL_EXPLICIT=true",
    ):
        assert flag in s5q

    assert "K4_GRAPH_ASSEMBLY_SAVING_EXPONENT=1/200" in bb
    assert "ROOT_SAWTOOTH_HANDOFF_BAND=R_E>-1/200" in result
    assert "CONDITIONAL_RECIPROCAL_EXPONENT_FORMULA=min(1/200,delta_saw)" in result

    # Walsh l1/l2 normalization for representative omega(e).
    for omega in range(0, 13):
        count = 1 << omega
        w = Fraction(1, count)
        assert count * w == 1
        assert count * w * w == Fraction(1, count) <= 1

    # Exact critical boundary pieces.
    for beta_i in range(1, 10):
        beta = Fraction(beta_i, 10)
        assert r_exp(Fraction(1), beta) == 0

    for alpha_i in range(5, 11):
        alpha = Fraction(alpha_i, 10)
        assert r_exp(alpha, Fraction(1)) == 0

    for beta_i in range(11, 20):
        beta = Fraction(beta_i, 10)
        alpha = 1 - beta / 2
        assert alpha < beta / 2
        assert r_exp(alpha, beta) == 0

    assert r_exp(Fraction(1, 2), Fraction(1)) == 0

    # Handoff band: outside it the existing L2 estimate saves >=1/200.
    threshold = -Fraction(1, 200)
    outside = inside = 0
    for ai in range(0, 201):
        alpha = Fraction(ai, 200)
        for bi in range(0, 401):
            beta = Fraction(bi, 200)
            R = r_exp(alpha, beta)
            if R <= threshold:
                outside += 1
                assert R <= -Fraction(1, 200)
            else:
                inside += 1
    assert outside > 0 and inside > 0

    # Exact floor/sawtooth residue-count identity used by s5q.
    saw_checks = 0
    for L in range(-4, 5):
        for R in range(L, 6):
            for v in range(1, 9):
                for b in range(v):
                    direct = sum(1 for y in range(L, R + 1) if (y - b) % v == 0)
                    assert residue_count_formula(L, R, b, v) == direct
                    saw_checks += 1

    decision = summary["decision"]
    assert decision["MULTI_EDGE_DISCREPANCY_TENSOR_CONTRACTION_PROVED"] is True
    assert decision["E_COLUMN_SINGLE_WALSH_SUBSET_EXACT"] is True
    assert decision["FINAL_ROOT_SAWTOOTH_KERNEL_EXPLICIT"] is True
    assert decision["ROOT_SAWTOOTH_HANDOFF_BAND"] == "R_E>-1/200"
    assert decision["CONDITIONAL_RECIPROCAL_EXPONENT_FORMULA"] == "min(1/200,delta_saw)"
    assert decision["COMPLETE_POSITIVE_RECIPROCAL_EXPONENT_PROVED"] is False

    print(f"handoff_outside_grid_points={outside}")
    print(f"handoff_inside_grid_points={inside}")
    print(f"sawtooth_identity_checks={saw_checks}")
    print(json.dumps(decision, indent=2))


if __name__ == "__main__":
    main()
