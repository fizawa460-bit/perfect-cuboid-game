#!/usr/bin/env python3
"""Exact affine-lattice closure for the Stage32 d6/g1/e4/a32 wall.

The implementation uses only exact integer/rational arithmetic.  FLINT HNF
gives a saturated affine kernel for the ten fixed budget equalities, exact
Gram-LLL reduces that kernel, and a complete Fincke--Pohst recursion searches
the resulting shifted ellipsoid.  All 140 nonnegative intersection forms are
used as exact continuous ellipsoid bounds during the recursion.
"""

from __future__ import annotations

import hashlib
import json
import pathlib
import platform
import time
from dataclasses import dataclass
from typing import Any, Iterable

import flint
from flint import fmpq, fmpz_mat
import sympy
from sympy import Matrix


EXPECTED_CORE_SCHEMA = "STAGE32_PICARD_CORE_INDLIST_V1"
EXPECTED_SOURCE_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
CELL_SCHEMA = "STAGE32_AFFINE_LATTICE_CELL_V1"
ALGORITHM_ID = "HNF_KERNEL_EXACT_GRAM_LLL_FP140_V1"

BUDGET_KEYS = (
    "degree",
    "exceptional_mass",
    "curve_group_mass",
    "curve_quarter_mass",
    "exceptional_half_mass",
    "second_curve_quarter_mass",
    "exceptional_quarter_mass",
    "second_exceptional_quarter_mass",
    "curve_eighth_mass",
    "curve_sixteenth_mass",
)


def canonical_sha256(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def file_sha256(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def matrix_list(matrix: Matrix) -> list[list[int]]:
    return [[int(matrix[i, j]) for j in range(matrix.cols)] for i in range(matrix.rows)]


def matrix_sha256(matrix: Matrix) -> str:
    return canonical_sha256(matrix_list(matrix))


def rational_text(value: Any) -> str:
    if isinstance(value, fmpq):
        return str(value)
    value = sympy.Rational(value)
    return str(value)


def to_fmpq(value: Any) -> fmpq:
    value = sympy.Rational(value)
    return fmpq(int(value.p), int(value.q))


def atomic_json(path: pathlib.Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    temporary.replace(path)


def load_core(path: pathlib.Path) -> tuple[dict[str, Any], dict[str, str]]:
    core = json.loads(path.read_text(encoding="utf-8"))
    assert core["schema"] == EXPECTED_CORE_SCHEMA
    assert core["source"]["git_blob_sha1"] == EXPECTED_SOURCE_BLOB
    assert core["rank"] == 64 and core["known_class_count"] == 140
    assert core["h2"] == 16 and core["basis_gram_determinant"] == -268435456
    unsigned = dict(core)
    claimed = unsigned.pop("canonical_sha256_without_this_field")
    actual = canonical_sha256(unsigned)
    assert actual == claimed
    return core, {"file_sha256": file_sha256(path), "canonical_sha256": actual}


def fixed_budget_rows(core: dict[str, Any]) -> list[list[int]]:
    gram = core["basis_gram"]
    rows = core["raw_cross_pairings_with_basis"]
    hyperplane = core["hyperplane"]
    hform = [
        sum(hyperplane[i] * gram[i][j] for i in range(64)) for j in range(64)
    ]

    def row_sum(lo: int, hi: int) -> list[int]:
        return [sum(rows[k][j] for k in range(lo, hi)) for j in range(64)]

    weighted = [
        sum(rows[k][j] for k in range(92))
        + 5 * sum(rows[k][j] for k in range(92, 140))
        for j in range(64)
    ]
    assert weighted == [19 * value for value in hform]
    return [
        hform,
        row_sum(92, 140),
        row_sum(0, 46),
        row_sum(0, 23),
        row_sum(92, 116),
        row_sum(46, 69),
        row_sum(92, 104),
        row_sum(116, 128),
        row_sum(0, 11),
        row_sum(0, 5),
    ]


@dataclass
class ExactContext:
    core: dict[str, Any]
    core_hashes: dict[str, str]
    gram: Matrix
    intersections: Matrix
    fixed_map: Matrix
    hnf: Matrix
    hnf_transform: Matrix
    image_basis: Matrix
    affine_columns: Matrix
    kernel: Matrix
    reduced_kernel: Matrix
    reduced_gram: Matrix
    lll_transform: Matrix
    ldl_lower: list[list[fmpq]]
    ldl_diagonal: list[fmpq]
    intersection_reduced: Matrix
    pruning_coefficients: list[list[fmpq]]
    pruning_prefix_dual_norms: list[list[fmpq]]
    common_certificate: dict[str, Any]


def build_context(core_path: pathlib.Path) -> ExactContext:
    core, core_hashes = load_core(core_path)
    gram = Matrix(core["basis_gram"])
    intersections = Matrix(core["raw_cross_pairings_with_basis"])
    fixed_rows = fixed_budget_rows(core)
    fixed_map = Matrix(fixed_rows)
    assert fixed_map.rank() == 10

    fixed_flint = fmpz_mat(fixed_rows)
    hnf_flint, transform_flint = fixed_flint.transpose().hnf(transform=True)
    hnf = Matrix(
        [[int(hnf_flint[i, j]) for j in range(hnf_flint.ncols())] for i in range(hnf_flint.nrows())]
    )
    transform = Matrix(
        [
            [int(transform_flint[i, j]) for j in range(transform_flint.ncols())]
            for i in range(transform_flint.nrows())
        ]
    )
    assert hnf == transform * fixed_map.T
    assert abs(int(transform_flint.det())) == 1
    assert all(hnf[i, j] == 0 for i in range(10, 64) for j in range(10))

    transform_t = transform.T
    affine_columns = transform_t[:, :10]
    kernel = transform_t[:, 10:]
    image_basis = fixed_map * affine_columns
    assert image_basis == hnf[:10, :].T
    assert fixed_map * kernel == Matrix.zeros(10, 54)
    assert kernel.rank() == 54

    kernel_gram = -(kernel.T * gram * kernel)
    kernel_gram_flint = fmpz_mat(matrix_list(kernel_gram))
    reduced_gram_flint, lll_flint = kernel_gram_flint.lll(
        transform=True, rep="gram", gram="exact"
    )
    lll_transform = Matrix(
        [[int(lll_flint[i, j]) for j in range(54)] for i in range(54)]
    )
    reduced_gram = Matrix(
        [[int(reduced_gram_flint[i, j]) for j in range(54)] for i in range(54)]
    )
    assert abs(int(lll_flint.det())) == 1
    assert reduced_gram == lll_transform * kernel_gram * lll_transform.T
    reduced_kernel = kernel * lll_transform.T
    assert reduced_gram == -(reduced_kernel.T * gram * reduced_kernel)

    ldl_lower_sympy, ldl_diagonal_sympy = reduced_gram.LDLdecomposition(hermitian=False)
    assert reduced_gram == ldl_lower_sympy * ldl_diagonal_sympy * ldl_lower_sympy.T
    ldl_lower = [
        [to_fmpq(ldl_lower_sympy[i, j]) for j in range(54)] for i in range(54)
    ]
    ldl_diagonal = [to_fmpq(ldl_diagonal_sympy[i, i]) for i in range(54)]
    assert all(value > 0 for value in ldl_diagonal)

    intersection_reduced = intersections * reduced_kernel
    # If t=L^T(w-mu), then a.w = r.t with r^T L^T = a^T.
    # Solve that unit-triangular system by forward substitution.
    pruning_coefficients: list[list[fmpq]] = []
    for k in range(140):
        source = [fmpq(int(intersection_reduced[k, j])) for j in range(54)]
        result: list[fmpq] = []
        for j in range(54):
            value = source[j]
            for i in range(j):
                value -= result[i] * ldl_lower[j][i]
            result.append(value)
        pruning_coefficients.append(result)

    pruning_prefix_dual_norms: list[list[fmpq]] = []
    for row in pruning_coefficients:
        prefixes: list[fmpq] = []
        value = fmpq(0)
        for i in range(54):
            value += row[i] * row[i] / ldl_diagonal[i]
            prefixes.append(value)
        pruning_prefix_dual_norms.append(prefixes)

    hnf_diagonal = [int(image_basis[i, i]) for i in range(10)]
    common = {
        "schema": "STAGE32_AFFINE_LATTICE_COMMON_V1",
        "algorithm_id": ALGORITHM_ID,
        "core": core_hashes,
        "fixed_budget_key_order": list(BUDGET_KEYS),
        "fixed_map_rank": 10,
        "kernel_dimension": 54,
        "fixed_map_sha256": matrix_sha256(fixed_map),
        "hnf_sha256": matrix_sha256(hnf),
        "hnf_transform_sha256": matrix_sha256(transform),
        "hnf_image_diagonal": hnf_diagonal,
        "hnf_image_index": abs(sympy.prod(hnf_diagonal)),
        "kernel_sha256": matrix_sha256(kernel),
        "kernel_gram_determinant": int(kernel_gram.det()),
        "lll_transform_sha256": matrix_sha256(lll_transform),
        "reduced_kernel_sha256": matrix_sha256(reduced_kernel),
        "reduced_gram_sha256": matrix_sha256(reduced_gram),
        "reduced_gram_determinant": int(reduced_gram.det()),
        "ldl_diagonal": [str(value) for value in ldl_diagonal],
        "all_140_intersection_constraints_used": True,
        "weighted_intersection_identity_verified": True,
        "exact_arithmetic_only": True,
        "tool_versions": {
            "python": platform.python_version(),
            "python_flint": flint.__version__,
            "sympy": sympy.__version__,
        },
    }
    common["canonical_sha256_without_this_field"] = canonical_sha256(common)
    return ExactContext(
        core=core,
        core_hashes=core_hashes,
        gram=gram,
        intersections=intersections,
        fixed_map=fixed_map,
        hnf=hnf,
        hnf_transform=transform,
        image_basis=image_basis,
        affine_columns=affine_columns,
        kernel=kernel,
        reduced_kernel=reduced_kernel,
        reduced_gram=reduced_gram,
        lll_transform=lll_transform,
        ldl_lower=ldl_lower,
        ldl_diagonal=ldl_diagonal,
        intersection_reduced=intersection_reduced,
        pruning_coefficients=pruning_coefficients,
        pruning_prefix_dual_norms=pruning_prefix_dual_norms,
        common_certificate=common,
    )


def cell_target(cell: dict[str, Any]) -> Matrix:
    return Matrix([int(cell[key]) for key in BUDGET_KEYS])


def exact_pairing(left: Iterable[int], gram: Matrix, right: Iterable[int]) -> int:
    left_matrix = Matrix(list(left))
    right_matrix = Matrix(list(right))
    return int((left_matrix.T * gram * right_matrix)[0])


def verify_survivor(context: ExactContext, cell: dict[str, Any], vector: list[int]) -> None:
    x = Matrix(vector)
    assert context.fixed_map * x == cell_target(cell)
    pairings = context.intersections * x
    assert all(value >= 0 for value in pairings)
    assert sum(pairings[:92, 0]) + 5 * sum(pairings[92:, 0]) == 19 * int(cell["degree"])
    square = int((x.T * context.gram * x)[0])
    lower = -int(cell["degree"]) - 2 + 2 * int(cell["genus"])
    assert square >= lower


def _hash_event(digest: Any, *parts: object) -> None:
    digest.update("|".join(str(part) for part in parts).encode())
    digest.update(b"\n")


def solve_cell(context: ExactContext, cell: dict[str, Any]) -> dict[str, Any]:
    start = time.perf_counter()
    target = cell_target(cell)
    image_coordinates = context.image_basis.inv() * target
    image_feasible = all(value.q == 1 for value in image_coordinates)
    if not image_feasible:
        raise AssertionError("the inherited terminal target unexpectedly fails the HNF image test")
    base_point = context.affine_columns * image_coordinates
    assert all(value.q == 1 for value in base_point)
    assert context.fixed_map * base_point == target

    q0 = (base_point.T * context.gram * base_point)[0]
    cross = context.reduced_kernel.T * context.gram * base_point
    center_sympy = context.reduced_gram.inv() * cross
    lower = -int(cell["degree"]) - 2 + 2 * int(cell["genus"])
    radius_sympy = q0 - lower + (cross.T * context.reduced_gram.inv() * cross)[0]
    assert radius_sympy >= 0
    center = [to_fmpq(value) for value in center_sympy]
    radius = to_fmpq(radius_sympy)
    intersection_center = context.intersections * (
        base_point + context.reduced_kernel * center_sympy
    )
    fixed_intersections = [to_fmpq(value) for value in intersection_center]

    minimum_diagonal = min(context.ldl_diagonal)
    search_limit = 0
    while fmpq(search_limit * search_limit) < radius / minimum_diagonal:
        search_limit += 1
    # The extra unit makes the completeness independent of whether the exact
    # ellipsoid centre is itself integral.
    search_limit += 1

    coordinates = [0] * 54
    transcript = hashlib.sha256()
    node_count = 0
    interval_rejection_count = 0
    intersection_prune_count = 0
    feasible_leaf_count = 0
    survivors: list[list[int]] = []

    def viable(next_index: int, remaining: fmpq) -> bool:
        nonlocal intersection_prune_count
        for form_index in range(140):
            fixed = fixed_intersections[form_index]
            if fixed >= 0:
                continue
            impossible = next_index < 0
            if not impossible:
                dual_norm = context.pruning_prefix_dual_norms[form_index][next_index]
                impossible = fixed * fixed > remaining * dual_norm
            if impossible:
                intersection_prune_count += 1
                _hash_event(
                    transcript,
                    "P",
                    next_index,
                    form_index,
                    fixed,
                    remaining,
                )
                return False
        return True

    def recurse(index: int, remaining: fmpq) -> None:
        nonlocal node_count, interval_rejection_count, feasible_leaf_count
        node_count += 1
        _hash_event(transcript, "N", index, remaining)
        alpha = -center[index]
        for j in range(index + 1, 54):
            alpha += context.ldl_lower[j][index] * (coordinates[j] - center[j])
        exact_centre = -alpha
        base = int(exact_centre.p) // int(exact_centre.q)
        for value in range(base - search_limit, base + search_limit + 1):
            transformed = value + alpha
            cost = context.ldl_diagonal[index] * transformed * transformed
            if cost > remaining:
                interval_rejection_count += 1
                continue
            coordinates[index] = value
            for form_index in range(140):
                fixed_intersections[form_index] += (
                    context.pruning_coefficients[form_index][index] * transformed
                )
            new_remaining = remaining - cost
            if viable(index - 1, new_remaining):
                if index:
                    recurse(index - 1, new_remaining)
                else:
                    feasible_leaf_count += 1
                    vector_matrix = base_point + context.reduced_kernel * Matrix(coordinates)
                    vector = [int(value) for value in vector_matrix]
                    verify_survivor(context, cell, vector)
                    survivors.append(vector)
                    _hash_event(transcript, "S", *vector)
            for form_index in range(140):
                fixed_intersections[form_index] -= (
                    context.pruning_coefficients[form_index][index] * transformed
                )

    recurse(53, radius)
    survivors.sort()
    elapsed = time.perf_counter() - start
    result = "UNSAT" if not survivors else "SAT_EXHAUSTED"
    deterministic = {
        "schema": CELL_SCHEMA,
        "algorithm_id": ALGORITHM_ID,
        "label": cell["label"],
        "budget": {key: int(cell[key]) for key in BUDGET_KEYS},
        "genus": int(cell["genus"]),
        "core_file_sha256": context.core_hashes["file_sha256"],
        "core_canonical_sha256": context.core_hashes["canonical_sha256"],
        "common_certificate_sha256": context.common_certificate[
            "canonical_sha256_without_this_field"
        ],
        "inherited_checkpoint_file_sha256": cell.get("checkpoint_file_sha256"),
        "inherited_smt2_sha256": cell.get("smt2_sha256"),
        "hnf_image_feasible": image_feasible,
        "hnf_image_coordinates": [int(value) for value in image_coordinates],
        "base_point": [int(value) for value in base_point],
        "base_point_sha256": canonical_sha256([int(value) for value in base_point]),
        "adjunction_lower_bound": lower,
        "completed_square_radius": rational_text(radius),
        "search_limit": search_limit,
        "enumeration_node_count": node_count,
        "interval_rejection_count": interval_rejection_count,
        "intersection_prune_count": intersection_prune_count,
        "feasible_leaf_count": feasible_leaf_count,
        "enumeration_transcript_sha256": transcript.hexdigest(),
        "solver_result": result,
        "complete": True,
        "unknown_reason": None,
        "exact_survivor_count": len(survivors),
        "survivors": survivors,
        "all_140_intersection_constraints_used": True,
        "floating_point_feasibility_credit": False,
    }
    payload = dict(deterministic)
    payload["elapsed_seconds"] = round(elapsed, 6)
    payload["deterministic_result_sha256"] = canonical_sha256(deterministic)
    payload["checkpoint_sha256_without_this_field"] = canonical_sha256(payload)
    return payload


def validate_checkpoint(payload: dict[str, Any]) -> None:
    unsigned = dict(payload)
    claimed_checkpoint = unsigned.pop("checkpoint_sha256_without_this_field")
    assert canonical_sha256(unsigned) == claimed_checkpoint
    deterministic = dict(unsigned)
    claimed_result = deterministic.pop("deterministic_result_sha256")
    deterministic.pop("elapsed_seconds")
    assert canonical_sha256(deterministic) == claimed_result
    assert payload["complete"] is True and payload["unknown_reason"] is None
    assert payload["exact_survivor_count"] == len(payload["survivors"])
