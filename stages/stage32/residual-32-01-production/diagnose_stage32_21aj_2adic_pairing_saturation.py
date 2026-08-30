#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from sympy import Matrix, ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

from direct_picard_reynolds_lattice_diagnostic import (
    EXPECTED_FIXED_RANK,
    GROUP_ORDER,
    PICARD_RANK,
    csha,
    exact_column_lattice_basis_lowrank,
    load_retained,
)
from direct_picard_reynolds_rank2_integral_projection_bound import (
    build_reynolds_numerator,
)
from direct_picard_slice_bridge import DirectPicardSliceBridge
from hperp_integral_adapter import (
    EXPECTED_PICARD_DETERMINANT,
    HperpIntegralPairingAdapter,
    RETAINED_BASIS_KNOWN_LABELS_1BASED,
)

EXPECTED_ANTI_RANK = PICARD_RANK - EXPECTED_FIXED_RANK
EXPECTED_CURVE_COUNT = 140
EXPECTED_21AI_CANONICAL_SHA256 = (
    "8f3f817e89fa938ac5bc7c425fa95a0b4ac8e971c2cb13c988540eba002f2b67"
)
EXPECTED_21AI_MOD2_RANK = 45
EXPECTED_21AI_MOD2_DEFECT = 14


def matrix_int_list(m: Matrix) -> list[list[int]]:
    return [[int(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]


def nonzero_smith_diagonal(d: Matrix) -> tuple[int, ...]:
    out = []
    for i in range(min(d.rows, d.cols)):
        v = abs(int(d[i, i]))
        if v:
            out.append(v)
    return tuple(out)


def integer_coordinate_matrix(numerator: Matrix, basis: Matrix) -> Matrix:
    row_pivots = tuple(int(i) for i in basis.T.rref()[1])
    if len(row_pivots) != EXPECTED_FIXED_RANK:
        raise ValueError("fixed-image row-pivot regression")
    square = basis[list(row_pivots), :]
    inv_square = square.inv()
    cols = []
    for j in range(numerator.cols):
        rhs = Matrix([numerator[i, j] for i in row_pivots])
        x = inv_square * rhs
        if basis * x != numerator[:, j]:
            raise ValueError(f"fixed-image coordinate reconstruction regression at {j}")
        if any(v.q != 1 for v in x):
            raise ValueError(f"nonintegral fixed-image coordinate at {j}")
        cols.append(Matrix([int(v) for v in x]))
    return Matrix.hstack(*cols)


def column_bitsets_mod2(a: Matrix) -> list[int]:
    out = []
    for j in range(a.cols):
        bits = 0
        for i in range(a.rows):
            if int(a[i, j]) & 1:
                bits |= 1 << i
        out.append(bits)
    return out


def gf2_basis_and_expressions(a: Matrix) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Return deterministic independent columns and each column's F2 expression."""
    columns = column_bitsets_mod2(a)
    echelon: dict[int, tuple[int, int]] = {}
    basis_indices: list[int] = []
    expressions: list[int] = [0] * a.cols

    for j, raw_bits in enumerate(columns):
        bits = raw_bits
        combo = 0
        while bits:
            pivot = bits.bit_length() - 1
            previous = echelon.get(pivot)
            if previous is None:
                k = len(basis_indices)
                basis_indices.append(j)
                reduced_expression = (1 << k) ^ combo
                echelon[pivot] = (bits, reduced_expression)
                expressions[j] = 1 << k
                break
            reduced_bits, reduced_expression = previous
            bits ^= reduced_bits
            combo ^= reduced_expression
        else:
            expressions[j] = combo

    for k, j in enumerate(basis_indices):
        if expressions[j] != 1 << k:
            raise ValueError("GF2 basis self-expression regression")

    return tuple(basis_indices), tuple(expressions)


def gf2_rank(a: Matrix) -> int:
    return len(gf2_basis_and_expressions(a)[0])


def two_saturate_once(a: Matrix) -> tuple[Matrix, dict]:
    """Enlarge the column lattice by exactly one layer of 2-saturation."""
    if a.cols != EXPECTED_ANTI_RANK:
        raise ValueError(f"unexpected lattice rank: {a.cols}")

    basis_indices, expressions = gf2_basis_and_expressions(a)
    basis_set = set(basis_indices)
    dependent_indices = tuple(j for j in range(a.cols) if j not in basis_set)
    defect = len(dependent_indices)

    if defect == 0:
        return a, {
            "mod2_rank": a.cols,
            "defect": 0,
            "index_log2": 0,
            "basis_indices_0based": list(basis_indices),
            "dependent_indices_0based": [],
        }

    basis_columns = [a[:, j] for j in basis_indices]
    new_columns = list(basis_columns)
    dependency_rows = []

    for j in dependent_indices:
        mask = expressions[j]
        even = a[:, j]
        selected_basis = []
        for k, bcol in enumerate(basis_columns):
            if (mask >> k) & 1:
                even = even - bcol
                selected_basis.append(k)
        if any(int(v) % 2 for v in even):
            raise ValueError(f"dependent column {j} did not become even")
        half = even.applyfunc(lambda v: int(v) // 2)
        new_columns.append(half)
        dependency_rows.append(
            {
                "dependent_column_0based": j,
                "basis_mask_hex": hex(mask),
                "basis_positions_0based": selected_basis,
            }
        )

    enlarged = Matrix.hstack(*new_columns)
    if enlarged.shape != a.shape:
        raise ValueError("2-saturated basis shape regression")

    step = {
        "mod2_rank": len(basis_indices),
        "defect": defect,
        "index_log2": defect,
        "basis_indices_0based": list(basis_indices),
        "dependent_indices_0based": list(dependent_indices),
        "dependency_description_sha256": csha(dependency_rows),
        "input_basis_sha256": csha(matrix_int_list(a)),
        "output_basis_sha256": csha(matrix_int_list(enlarged)),
    }
    return enlarged, step


def recover_smith_from_defects(
    defects_including_final_zero: list[int],
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    if not defects_including_final_zero or defects_including_final_zero[-1] != 0:
        raise ValueError("defect ladder must terminate at zero")
    if any(
        defects_including_final_zero[i + 1] > defects_including_final_zero[i]
        for i in range(len(defects_including_final_zero) - 1)
    ):
        raise ValueError(f"2-adic defects are not monotone: {defects_including_final_zero}")

    exponents: list[int] = [0] * (
        EXPECTED_ANTI_RANK - defects_including_final_zero[0]
    )
    for k in range(1, len(defects_including_final_zero)):
        count_exact = (
            defects_including_final_zero[k - 1]
            - defects_including_final_zero[k]
        )
        exponents.extend([k] * count_exact)

    if len(exponents) != EXPECTED_ANTI_RANK:
        raise ValueError(
            f"recovered Smith exponent count {len(exponents)} != {EXPECTED_ANTI_RANK}"
        )
    factors = tuple(1 << e for e in exponents)
    return tuple(exponents), factors


def build_certificate(marking: dict, bundle: dict) -> dict:
    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    bridge = DirectPicardSliceBridge.from_retained(marking, bundle)
    gram = Matrix(bundle["picard_gram_64x64"])
    if abs(int(EXPECTED_PICARD_DETERMINANT)) != 1 << 28:
        raise ValueError("Picard determinant lock is no longer 2^28")

    phi = Matrix(
        [
            list(bridge.degree_functional),
            list(bridge.exceptional_mass_functional),
            list(bridge.first_normal_half_functional),
        ]
    )
    N, _, action_hashes_sha = build_reynolds_numerator(marking, adapter, gram, phi)
    B, module_stats = exact_column_lattice_basis_lowrank(N, EXPECTED_FIXED_RANK)
    C = integer_coordinate_matrix(N, B)
    if B * C != N:
        raise ValueError("N=B*C regression")

    C_dm = DomainMatrix.from_Matrix(C).convert_to(ZZ)
    D_dm, S_dm, T_dm = smith_normal_decomp(C_dm)
    if S_dm * C_dm * T_dm != D_dm:
        raise ValueError("fixed-coordinate Smith reconstruction regression")
    D = D_dm.to_Matrix()
    T = T_dm.to_Matrix()
    cdiag = nonzero_smith_diagonal(D)
    if cdiag != (1,) * EXPECTED_FIXED_RANK:
        raise ValueError(f"fixed-coordinate map not surjective: {cdiag}")

    K = T[:, EXPECTED_FIXED_RANK:]
    if K.shape != (PICARD_RANK, EXPECTED_ANTI_RANK):
        raise ValueError(f"anti-fixed kernel shape regression: {K.shape}")
    if C * K != Matrix.zeros(EXPECTED_FIXED_RANK, EXPECTED_ANTI_RANK):
        raise ValueError("anti-fixed kernel C-regression")
    if N * K != Matrix.zeros(PICARD_RANK, EXPECTED_ANTI_RANK):
        raise ValueError("anti-fixed kernel N-regression")
    if phi * K != Matrix.zeros(3, EXPECTED_ANTI_RANK):
        raise ValueError("anti-fixed kernel slice regression")

    pairing = adapter.pairing_matrix
    coords = adapter.class_coordinates_in_retained_basis
    M = pairing * K
    retained_pairing = gram * K
    retained_indices = [
        label - 1 for label in RETAINED_BASIS_KNOWN_LABELS_1BASED
    ]
    if coords * retained_pairing != M:
        raise ValueError("all140 rows are not integral combinations of retained64 rows")
    if (
        M.extract(retained_indices, list(range(EXPECTED_ANTI_RANK)))
        != retained_pairing
    ):
        raise ValueError("retained64 generator rows are not embedded identically")

    initial_mod2_rank = gf2_rank(M)
    initial_defect = EXPECTED_ANTI_RANK - initial_mod2_rank
    if (
        initial_mod2_rank != EXPECTED_21AI_MOD2_RANK
        or initial_defect != EXPECTED_21AI_MOD2_DEFECT
    ):
        raise ValueError(
            f"21ai mod2 regression: rank={initial_mod2_rank}, defect={initial_defect}"
        )

    current = M
    steps = []
    defects = []
    for layer in range(29):
        rank2 = gf2_rank(current)
        defect = EXPECTED_ANTI_RANK - rank2
        defects.append(defect)
        if defect == 0:
            break
        enlarged, step = two_saturate_once(current)
        step["layer_1based"] = layer + 1
        steps.append(step)
        current = enlarged
    else:
        raise ValueError("2-saturation did not terminate within determinant exponent 28")

    if defects[-1] != 0:
        raise ValueError("2-saturation ladder did not reach full mod2 rank")

    exponents, smith_factors = recover_smith_from_defects(defects)
    total_log2_index = sum(defects[:-1])
    if sum(exponents) != total_log2_index:
        raise ValueError("Smith exponent sum does not match accumulated 2-index")
    if any(
        smith_factors[i] == 0
        or smith_factors[i + 1] % smith_factors[i]
        for i in range(len(smith_factors) - 1)
    ):
        raise ValueError("recovered Smith factors do not form a divisibility chain")
    if max(exponents, default=0) > 28:
        raise ValueError("recovered Smith exponent exceeds 2^28 annihilator")
    if gf2_rank(current) != EXPECTED_ANTI_RANK:
        raise ValueError("final saturated basis is not full rank mod2")

    multiplicities = []
    for e in sorted(set(exponents)):
        multiplicities.append(
            {
                "factor": 1 << e,
                "two_adic_exponent": e,
                "multiplicity": sum(1 for x in exponents if x == e),
            }
        )

    cert = {
        "schema": "STAGE32_21AJ_EXACT_2ADIC_ANTIFIXED_PAIRING_SATURATION_V1",
        "mode": "EXACT_GF2_SATURATION_LADDER_FOR_2PRIMARY_PAIRING_IMAGE_COKERNEL",
        "upstream_21ai_certificate_sha256": EXPECTED_21AI_CANONICAL_SHA256,
        "adapter_certificate_sha256": adapter.certificate[
            "canonical_sha256_without_this_field"
        ],
        "slice_bridge_certificate_sha256": bridge.certificate[
            "canonical_sha256_without_this_field"
        ],
        "reynolds_numerator_sha256": csha(matrix_int_list(N)),
        "action_hashes_sha256": action_hashes_sha,
        "fixed_image_basis_sha256": csha(matrix_int_list(B)),
        "fixed_image_column_module_stats": module_stats,
        "fixed_coordinate_smith_diagonal": list(cdiag),
        "anti_fixed_integer_kernel_sha256": csha(matrix_int_list(K)),
        "initial_pairing_translation_lattice": {
            "shape": [M.rows, M.cols],
            "sha256": csha(matrix_int_list(M)),
            "rank": EXPECTED_ANTI_RANK,
            "initial_mod2_rank": initial_mod2_rank,
            "initial_mod2_defect": initial_defect,
            "all140_row_lattice_equals_retained64_row_lattice": True,
        },
        "two_primary_proof": {
            "picard_determinant": int(EXPECTED_PICARD_DETERMINANT),
            "absolute_picard_determinant": abs(int(EXPECTED_PICARD_DETERMINANT)),
            "absolute_picard_determinant_factorization": "2^28",
            "K_transpose_surjective": True,
            "adjugate_identity_kills_cokernel_by_abs_det_gram": True,
            "pairing_saturation_quotient_is_2_primary": True,
        },
        "saturation_ladder": {
            "defects_including_terminal_zero": defects,
            "layer_count": len(steps),
            "steps": steps,
            "total_index_log2": total_log2_index,
            "total_saturation_index": str(1 << total_log2_index),
            "final_saturated_basis_sha256": csha(matrix_int_list(current)),
            "final_mod2_rank": EXPECTED_ANTI_RANK,
            "wide_hnf_run": False,
            "wide_snf_run": False,
        },
        "exact_smith_structure": {
            "nonzero_factor_count": len(smith_factors),
            "two_adic_exponents": list(exponents),
            "smith_nonzero_diagonal": list(smith_factors),
            "factor_multiplicities": multiplicities,
            "maximum_factor": max(smith_factors),
            "maximum_two_adic_exponent": max(exponents),
            "nonunit_factor_count": sum(1 for x in smith_factors if x != 1),
            "saturation_index": str(1 << total_log2_index),
            "product_matches_accumulated_index": True,
        },
        "interpretation": {
            "translation_lattice_structure_solved_exactly": True,
            "affine_projection_offset_restored": False,
            "simultaneous_nonnegative_affine_fiber_feasibility_solved": False,
            "next_leaf": (
                "32-21ak: restore the projection-residue affine offset x0 and "
                "turn the exact 2-adic quotient into a deterministic membership "
                "filter against nonnegative orbit compositions"
            ),
        },
        "safety": {
            "heavy_run_key_used": False,
            "full178_production_run": False,
            "legacy_prefix_dfs_run": False,
            "59d_cvp_run": False,
            "terminal_family_materialization_run": False,
            "unknown_is_not_unsat": True,
            "numerical_row_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    cert["canonical_sha256_without_this_field"] = csha(cert)
    return cert


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    bundle = load_retained(args.retained, "s32_21aj_picard")
    marking = load_retained(args.marking, "s32_21aj_marking")
    cert = build_certificate(marking, bundle)
    args.output.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
    smith = cert["exact_smith_structure"]
    ladder = cert["saturation_ladder"]
    print(
        json.dumps(
            {
                "verdict": "PASS_STAGE32_21AJ_EXACT_2ADIC_PAIRING_SATURATION",
                "initial_mod2_rank": cert["initial_pairing_translation_lattice"][
                    "initial_mod2_rank"
                ],
                "initial_mod2_defect": cert["initial_pairing_translation_lattice"][
                    "initial_mod2_defect"
                ],
                "defect_sequence": ladder["defects_including_terminal_zero"],
                "total_index_log2": ladder["total_index_log2"],
                "nonunit_smith_factor_count": smith["nonunit_factor_count"],
                "maximum_smith_factor": smith["maximum_factor"],
                "maximum_two_adic_exponent": smith["maximum_two_adic_exponent"],
                "canonical_sha256": cert["canonical_sha256_without_this_field"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
