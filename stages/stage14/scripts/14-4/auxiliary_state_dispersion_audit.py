#!/usr/bin/env python3
"""Stage14-4aw: audit merged rank-one bulk transfer and endpoint ledger."""

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
AV = ROOT / "stages/stage14/14-4av/result.md"
S5I = ROOT / "stages/stage14/14-s5i/result.md"
OUT = ROOT / "stages/stage14/data/14-4/auxiliary_state_dispersion_summary.json"


def fstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def main() -> None:
    av = AV.read_text()
    s5i = S5I.read_text()

    assert "INTERIOR_DYADIC_POWER_SAVING_PROVED=true" in av
    assert "PURE_EUCLID_DIVISIBILITY_BULK_SEPARABLE=true" in s5i
    assert "STATE_SPLIT_MODULI_PRESERVE_BULK_FACTORIZATION=true" in s5i
    assert "MOBIUS_TRUNCATION_DISCREPANCY_DECOMPOSITION_PROVED=true" in s5i
    assert "DISCREPANCY_SECOND_MOMENT_PROVED=false" in s5i
    assert "SPARSE_LARGE_MODULUS_BLOCKS_CLOSED=false" in s5i

    exponent_audit = []
    for kappa in (Fraction(1, 10), Fraction(1, 8), Fraction(1, 6), Fraction(1, 4)):
        interior_bulk = 2 - kappa / 2
        q_threshold = 2 - 2 * kappa
        pointwise_delta = 2 - kappa
        assert interior_bulk < 2
        assert pointwise_delta < 2
        exponent_audit.append(
            {
                "kappa": fstr(kappa),
                "interior_bulk_L_exponent": fstr(interior_bulk),
                "medium_Q_threshold_L_exponent": fstr(q_threshold),
                "pointwise_Delta_L_exponent": fstr(pointwise_delta),
            }
        )

    # Dyadic microscopic bulk sum: sum U^{-1/2} over U=1,2,4,... is bounded.
    microscopic_geometric_sum_64 = sum(2.0 ** (-j / 2.0) for j in range(65))
    assert microscopic_geometric_sum_64 < 4.0

    report = {
        "stage": "14-4aw",
        "classification": "AUXILIARY_STATE_BULK_TRANSFERRED_AND_ENDPOINT_LEDGER_QUANTIFIED",
        "merged_inputs": {
            "stage14_4av_interior_bulk_saving": True,
            "stage14_s5i_rank_one_bulk": True,
            "stage14_s5i_state_split_factorization": True,
            "stage14_s5i_mobius_discrepancy": True,
        },
        "bulk_transfer": {
            "frozen_state_shape": "Gamma(frozen)*alpha(u)*beta(v)",
            "growing_auxiliary_state_coupling_in_bulk": False,
            "interior_block_bound": "L^2*(UV)^eps*sqrt(1/U+1/V)",
            "interior_condition": "L^kappa<=U,V<=L^(1-kappa)",
            "interior_dyadic_sum": "L^(2-kappa/2+o(1))",
            "interior_power_saving_summed": True,
        },
        "mobius_discrepancy": {
            "pointwise_bound": "Q^eps*((X+Y)log(2M)+sqrt(QXY)+Q)",
            "balanced_medium_condition": "X~Y~L, Q<=L^(2-2kappa)",
            "balanced_medium_pointwise": "Delta<<L^(2-kappa+o(1))",
            "pointwise_not_summable_as_L2": True,
            "sufficient_L2_contract": "sum_{u~U,v~V}|Delta(u,v)|^2 << L^(4-2eta+o(1))/(UV)",
            "second_moment_proved": False,
        },
        "endpoint_ledger": {
            "microscopic_condition": "min(U,V)<L^kappa",
            "microscopic_bulk_dyadic_sum": "L^(2+o(1))",
            "microscopic_geometric_sum_test_lt_4": True,
            "microscopic_fixed_power_saving": False,
            "microscopic_reason": "side 1 degenerates Jacobi edge to a constant/lower-dimensional mode",
            "sparse_condition": "Q>L^(2-2kappa)",
            "sparse_closed": False,
            "sparse_required_method": "divisor switching/complementary divisors or sparse-incidence estimate",
        },
        "exponent_audit": exponent_audit,
        "first_remaining_local_object": "DISCREPANCY_L2_PLUS_MICROSCOPIC_DIAGONAL_PLUS_SPARSE_SWITCHING",
        "decision": {
            "STAGE14_4AW": "AUXILIARY_STATE_BULK_TRANSFERRED_AND_ENDPOINT_LEDGER_QUANTIFIED",
            "S5I_RANK_ONE_BULK_IMPORTED": True,
            "GROWING_AUXILIARY_STATE_COUPLING_IN_BULK": False,
            "INTERIOR_AUXILIARY_BULK_POWER_SAVING_SUMMED": True,
            "MICROSCOPIC_BULK_DYADIC_SUMMED": True,
            "MICROSCOPIC_BULK_FIXED_POWER_SAVING": False,
            "MEDIUM_MODULUS_POINTWISE_DISCREPANCY_POWER_SAVING": True,
            "DISCREPANCY_L2_TARGET_EXPLICIT": True,
            "DISCREPANCY_SECOND_MOMENT_PROVED": False,
            "SPARSE_LARGE_MODULUS_BLOCKS_CLOSED": False,
            "MICROSCOPIC_DIAGONAL_CLOSED": False,
            "EXPLICIT_NONTRIVIAL_RHO_LOC_PROVED": False,
            "EXPLICIT_E_LOC_PROVED": False,
            "POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED": False,
            "POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED": False,
            "ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED": False,
            "NEXT": "Stage14-4ax attack the discrepancy L2 target on balanced/medium blocks and close either the microscopic diagonal or sparse large-modulus regime by divisor switching, exposing whichever obstruction survives first",
        },
    }

    OUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report["decision"], indent=2))


if __name__ == "__main__":
    main()
