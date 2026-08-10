#!/usr/bin/env python3
"""Stage14-tH17 deterministic signed-rectangle TT*/operator audit."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
T59 = ROOT / "stages/stage14/14-t59/result.md"
T61 = ROOT / "stages/stage14/14-t61/result.md"
RESULT = ROOT / "stages/stage14/14-tH17/result.md"
SUMMARY = ROOT / "stages/stage14/data/tH17/signed_orthogonal_rectangle_kummer_large_sieve_summary.json"


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    bt = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def frob2(a):
    return sum(x * x for row in a for x in row)


def vertical_identities(v):
    """Return full pair moment, off-diagonal moment and dual-Gram mass."""
    vv_t = matmul(v, transpose(v))
    v_t_v = matmul(transpose(v), v)
    full = frob2(vv_t)
    diagonal = sum(vv_t[i][i] ** 2 for i in range(len(vv_t)))
    off = full - diagonal
    dual = frob2(v_t_v)
    assert full == dual
    return {
        "full_pair_moment": full,
        "auxiliary_diagonal": diagonal,
        "offdiagonal_pair_moment": off,
        "dual_gram_mass": dual,
    }


def main() -> None:
    t59 = T59.read_text()
    t61 = T61.read_text()
    result = RESULT.read_text()
    summary = json.loads(SUMMARY.read_text())

    # Predecessor locks.
    assert "STAGE14_T59=COMPLETE_EXACT_TWO_COMPARATOR_ORTHOGONAL_RECTANGLE_REDUCTION" in t59
    assert "BALANCED_RECTANGLE_ENERGY_PRODUCT_LE_2_R2=true" in t59
    assert "SHARED_AUXILIARY_MODULUS_PRESERVED=true" in t59
    assert "STAGE14_T61=COMPLETE_POLAR_SCHATTEN_OBSTRUCTION_AND_SIGNED_RECTANGLE_REOPENING" in t61
    assert "POLAR_ZERO_LOSS_SHORTCUT_VALID=false" in t61
    assert "TH17_REQUESTED_OBJECT=SignedOrthogonalRectangleKummerBilinearLargeSieve" in t61

    # A nontrivial signed/zero synthetic vertical Kummer matrix.  The exact
    # identity is pure TT*: ||V V^T||_HS^2 = ||V^T V||_HS^2.
    v = [
        [1, -1, 1, 0, -1, 1],
        [-1, -1, 0, 1, 1, -1],
        [1, 0, -1, -1, 1, 1],
        [0, 1, 1, -1, -1, 1],
        [1, 1, -1, 1, 0, -1],
    ]
    signed = vertical_identities(v)
    assert signed["full_pair_moment"] >= signed["offdiagonal_pair_moment"] >= 0

    # Sharp Bessel -> Schatten-4 model: a 4x4 Hadamard matrix has
    # V V^T = 4 I, so ||V||_op^2=P=4 and S4^4=P^2*R=64 exactly.
    h4 = [
        [1, 1, 1, 1],
        [1, -1, 1, -1],
        [1, 1, -1, -1],
        [1, -1, -1, 1],
    ]
    had = vertical_identities(h4)
    hh = matmul(h4, transpose(h4))
    assert hh == [[4 if i == j else 0 for j in range(4)] for i in range(4)]
    P_h, R_h = 4, 4
    assert had["full_pair_moment"] == P_h * P_h * R_h
    assert had["offdiagonal_pair_moment"] == 0

    # Coherent principal block.  A single rectangle is automatically a legal
    # pairwise-disjoint rectangle family and satisfies the t59 aspect balance,
    # yet geometry alone cannot prevent all auxiliary rows from agreeing.
    P, h = 7, 5
    coherent = [[1 for _ in range(h)] for _ in range(P)]
    coh = vertical_identities(coherent)
    assert coh["full_pair_moment"] == P * P * h * h
    assert coh["offdiagonal_pair_moment"] == P * (P - 1) * h * h
    target = P * P * h
    assert coh["offdiagonal_pair_moment"] > target
    failure_ratio = coh["offdiagonal_pair_moment"] / target
    assert failure_ratio == (P - 1) * h / P

    # One-rectangle t59 aspect balance: (sum a_j^2)(sum b_j^2)
    # <= 2(sum a_j b_j)^2.  This confirms the coherent obstruction survives
    # perfect source-side aspect bookkeeping.
    a, b = 1, h
    assert (a * a) * (b * b) <= 2 * (a * b) ** 2

    # Auxiliary diagonal is target-scale under the natural R<=P regime.
    # For unit |K|<=1, sum_p |T_pp|^2 <= P R^2 <= P^2 R.
    R = 5
    assert R <= P
    assert P * R * R <= P * P * R

    # Locked theorem/failure boundary.
    required_tokens = [
        "STAGE14_TH17=COMPLETE_SIGNED_RECTANGLE_TTSTAR_OPERATOR_LARGE_SIEVE_APPLICABILITY_AUDIT",
        "SIGNED_PHYSICAL_TO_VERTICAL_MATRIX_IDENTITY_PROVED=true",
        "POLAR_ABSOLUTE_VALUE_USED=false",
        "TTSTAR_VERTICAL_SCHATTEN4_IDENTITY_PROVED=true",
        "ORTHOGONAL_RECTANGLE_VERTICAL_KUMMER_SCHATTEN4_PROVED=false",
        "ONE_PRIME_VERTICAL_KUMMER_BESSEL_IMPLIES_SIGNED_RECTANGLE_TARGET=true",
        "ONE_PRIME_VERTICAL_KUMMER_BESSEL_PROVED=false",
        "DUALITY_ALONE_CLOSES_TARGET=false",
        "T59_GEOMETRY_ALONE_IMPLIES_VERTICAL_CANCELLATION=false",
        "PING_XI_RECTANGLE_DIRECT_IMPORT_VALID=false",
        "FKMS_RECTANGLE_DIRECT_IMPORT_VALID=false",
        "OPERATOR_VALUED_LARGE_SIEVE_TARGET_PROVED=false",
        "SIGNED_ORTHOGONAL_RECTANGLE_KUMMER_BILINEAR_LARGE_SIEVE_PROVED=false",
        "E4_COEFFICIENT_ENERGY_USED=false",
        "MINIMAL_REMAINING_OBSTRUCTION=OrthogonalRectangleVerticalKummerSchatten4",
    ]
    for token in required_tokens:
        assert token in result, token

    decision = summary["decision"]
    assert decision["STAGE14_TH17"] == "COMPLETE_SIGNED_RECTANGLE_TTSTAR_OPERATOR_LARGE_SIEVE_APPLICABILITY_AUDIT"
    assert decision["POLAR_ABSOLUTE_VALUE_USED"] is False
    assert decision["TTSTAR_VERTICAL_SCHATTEN4_IDENTITY_PROVED"] is True
    assert decision["ORTHOGONAL_RECTANGLE_VERTICAL_KUMMER_SCHATTEN4_PROVED"] is False
    assert decision["ONE_PRIME_VERTICAL_KUMMER_BESSEL_PROVED"] is False
    assert decision["SIGNED_ORTHOGONAL_RECTANGLE_KUMMER_BILINEAR_LARGE_SIEVE_PROVED"] is False
    assert decision["E4_COEFFICIENT_ENERGY_USED"] is False
    assert decision["MINIMAL_REMAINING_OBSTRUCTION"] == "OrthogonalRectangleVerticalKummerSchatten4"

    report = {
        "stage": "14-tH17",
        "synthetic_signed_ttstar": signed,
        "hadamard_bessel_sharp_model": had,
        "coherent_principal_countermodel": {
            **coh,
            "P": P,
            "coherent_states": h,
            "target": target,
            "failure_ratio": failure_ratio,
            "single_rectangle_aspect_balance": True,
        },
        "checks": {
            "merged_t59_boundary": True,
            "merged_t61_boundary": True,
            "signed_vertical_matrix_identity": True,
            "ttstar_schatten4_identity": True,
            "bessel_to_schatten4_adapter_sharp_example": True,
            "geometry_alone_countermodel": True,
            "auxiliary_diagonal_absorption_ledger": True,
            "locked_boundary": True,
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
