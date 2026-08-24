#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import pathlib
import platform
import sys
import time
from typing import Any

import flint
from flint import fmpq, fmpz_mat
import numpy as np
import sympy
from sympy import Matrix

HERE = pathlib.Path(__file__).resolve().parent
S32 = HERE.parent
S32_07 = S32 / "32-07"
S32_05 = S32 / "32-05"
sys.path.insert(0, str(S32_05))


def load_module(name: str, path: pathlib.Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


pilot = load_module("stage32_07_pilot_coset", S32_07 / "run_d8_bounded_signature_cells.py")
from cap_certificate import load_and_verify

SCHEMA = "STAGE32_D8_SIGNATURE_CELL_AFFINE_COSET_PILOT_V2"
ALGORITHM_ID = "D8_SIGNATURE_CELL_PICARD_BASIS_MOD8_HNF_COSET_GRAM_LLL_FP140_V1"
EXPECTED_CAP_SHA = "75224aee543dcd4a56e814503765d1e1e69514b237fb900688243546ea6b4d03"
DEN = 8


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def matrix_list(matrix: Matrix) -> list[list[int]]:
    return [[int(matrix[i, j]) for j in range(matrix.cols)] for i in range(matrix.rows)]


def matrix_sha256(matrix: Matrix) -> str:
    return canonical_sha256(matrix_list(matrix))


def to_fmpq(value: Any) -> fmpq:
    value = sympy.Rational(value)
    return fmpq(int(value.p), int(value.q))


def rational_text(value: Any) -> str:
    return str(value if isinstance(value, fmpq) else sympy.Rational(value))


def hnf_affine_full_row(A: Matrix, b: Matrix) -> tuple[Matrix, Matrix, dict[str, Any]]:
    """Exact Z-preimage for a full-row-rank integer map A."""
    m, n = A.shape
    assert b.shape == (m, 1) and 0 < m <= n and A.rank() == m
    raw = fmpz_mat(matrix_list(A.T))
    hnf_f, transform_f = raw.hnf(transform=True)
    hnf = Matrix([[int(hnf_f[i, j]) for j in range(hnf_f.ncols())] for i in range(hnf_f.nrows())])
    transform = Matrix([[int(transform_f[i, j]) for j in range(transform_f.ncols())] for i in range(transform_f.nrows())])
    assert hnf == transform * A.T
    assert abs(int(transform_f.det())) == 1
    assert all(hnf[i, j] == 0 for i in range(m, n) for j in range(m))
    U = transform.T
    affine = U[:, :m]
    kernel = U[:, m:]
    image_basis = A * affine
    assert image_basis == hnf[:m, :].T
    coordinates = image_basis.inv() * b
    feasible = all(sympy.denom(v) == 1 for v in coordinates)
    cert = {
        "rows": m,
        "columns": n,
        "rank": m,
        "image_basis_sha256": matrix_sha256(image_basis),
        "hnf_sha256": matrix_sha256(hnf),
        "hnf_transform_sha256": matrix_sha256(transform),
        "image_feasible": feasible,
    }
    if not feasible:
        return Matrix.zeros(n, 1), Matrix.zeros(n, n - m), cert
    point = affine * coordinates
    assert all(sympy.denom(v) == 1 for v in point)
    point = Matrix([int(v) for v in point])
    assert A * point == b
    assert A * kernel == Matrix.zeros(m, n - m)
    cert["point_sha256"] = canonical_sha256([int(v) for v in point])
    cert["kernel_sha256"] = matrix_sha256(kernel)
    return point, kernel, cert


def dedup_congruences(rows: list[list[int]], rhs: list[int]) -> tuple[Matrix, Matrix, dict[str, Any]]:
    assert len(rows) == len(rhs)
    seen: dict[tuple[int, ...], int] = {}
    kept_rows: list[list[int]] = []
    kept_rhs: list[int] = []
    zero_rows = duplicate_rows = 0
    for raw_row, raw_rhs in zip(rows, rhs):
        row = tuple(int(v) % DEN for v in raw_row)
        value = int(raw_rhs) % DEN
        if not any(row):
            zero_rows += 1
            if value:
                raise ValueError("infeasible zero congruence")
            continue
        if row in seen:
            duplicate_rows += 1
            if seen[row] != value:
                raise ValueError("inconsistent duplicate congruence")
            continue
        seen[row] = value
        kept_rows.append(list(row))
        kept_rhs.append(value)
    return Matrix(kept_rows), Matrix(kept_rhs), {
        "raw_congruence_row_count": len(rows),
        "deduplicated_congruence_row_count": len(kept_rows),
        "zero_congruence_row_count": zero_rows,
        "duplicate_congruence_row_count": duplicate_rows,
    }


def independent_equalities(F: Matrix, target: Matrix) -> tuple[Matrix, Matrix, dict[str, Any]]:
    rows: list[list[int]] = []
    rhs: list[int] = []
    rank = aug_rank = 0
    for i in range(F.rows):
        row = [int(F[i, j]) for j in range(F.cols)]
        value = int(target[i])
        candidate = Matrix(rows + [row])
        candidate_aug = Matrix([r + [v] for r, v in zip(rows + [row], rhs + [value])])
        new_rank = candidate.rank()
        new_aug_rank = candidate_aug.rank()
        if new_rank > rank:
            rows.append(row)
            rhs.append(value)
            rank = new_rank
            aug_rank = new_aug_rank
        elif new_aug_rank > aug_rank:
            raise ValueError("inconsistent dependent equality")
    return Matrix(rows), Matrix(rhs), {
        "raw_equality_row_count": F.rows,
        "independent_equality_row_count": len(rows),
    }


def selected_matrix(core: dict[str, Any]) -> Matrix:
    rows = core["raw_cross_pairings_with_basis"]
    S = Matrix([rows[i] for i in pilot.base.SELECTED_ROWS])
    assert abs(int(S.det())) == pilot.base.EXPECTED_DET
    return S


def build_cell_coset(
    core: dict[str, Any],
    signature_matrix: np.ndarray,
    types: list[str],
    cell: dict[str, Any],
    e: int,
    a: int,
) -> tuple[Matrix, Matrix, dict[str, Any]]:
    """Return exact affine Picard-basis coset x = base + kernel*z."""
    S = selected_matrix(core)
    raw = Matrix(core["raw_cross_pairings_with_basis"])
    gram = Matrix(core["basis_gram"])
    H = Matrix([core["hyperplane"]])
    hrow = H * gram
    left_groups, right_groups = pilot.base.split_groups(types)
    side_indices = {
        "L": sorted(left_groups["A"] + left_groups["B"] + left_groups["C"]),
        "R": sorted(right_groups["A"] + right_groups["B"] + right_groups["C"]),
    }

    # Work directly in the primitive Picard basis x.  The selected-coordinate
    # lattice membership y in S*Z^64 is therefore automatic and the old 64
    # membership congruences disappear.  Only signature congruences remain.
    congruence_rows: list[list[int]] = []
    congruence_rhs: list[int] = []
    lsig = pilot.decode_signature(int(cell["left_signature_hex"], 16))
    rsig = pilot.decode_signature(int(cell["right_signature_hex"], 16))
    for side, sig in (("L", lsig), ("R", rsig)):
        for r in range(64):
            yrow = [0] * 64
            for j in side_indices[side]:
                yrow[j] = int(signature_matrix[r, j])
            xrow = Matrix([yrow]) * S
            congruence_rows.append([int(xrow[0, j]) for j in range(64)])
            congruence_rhs.append(int(sig[r]))

    C, rvec, congruence_cert = dedup_congruences(congruence_rows, congruence_rhs)
    m = C.rows
    Aaug = C.row_join(-DEN * Matrix.eye(m))
    aug_point, aug_kernel, aug_cert = hnf_affine_full_row(Aaug, rvec)
    if not aug_cert["image_feasible"]:
        raise ValueError("signature congruence coset is empty")
    x0 = aug_point[:64, :]
    L = aug_kernel[:64, :]
    assert L.shape == (64, 64) and L.rank() == 64
    assert all(int(v) % DEN == 0 for v in C * x0 - rvec)
    assert all(int(v) % DEN == 0 for v in C * L)

    eq_rows: list[list[int]] = []
    eq_rhs: list[int] = []

    def add(row: Matrix | list[int], value: int) -> None:
        if isinstance(row, Matrix):
            assert row.rows == 1 and row.cols == 64
            eq_rows.append([int(row[0, j]) for j in range(64)])
        else:
            eq_rows.append([int(v) for v in row])
        eq_rhs.append(int(value))

    add(hrow, pilot.DEGREE)
    add(Matrix([[sum(int(raw[k, j]) for k in range(92, 140)) for j in range(64)]]), e)
    add(Matrix([[sum(int(raw[k, j]) for k in range(46)) for j in range(64)]]), a)
    add(Matrix([[sum(int(raw[k, j]) for k in range(92)) for j in range(64)]]), 19 * pilot.DEGREE - 5 * e)

    xmass, ymass, zmass, t = map(int, cell["aggregate"])
    xl, yl, zl = map(int, cell["left_counts"])
    xr, yr, zr = map(int, cell["right_counts"])
    assert (xl + xr, yl + yr, zl + zr) == (xmass, ymass, zmass)
    for groups, counts in ((left_groups, (xl, yl, zl)), (right_groups, (xr, yr, zr))):
        for kind, target in zip("ABC", counts):
            yrow = Matrix([[1 if j in groups[kind] else 0 for j in range(64)]])
            add(yrow * S, int(target))
    qhead_row = Matrix([[1 if 48 <= j < 52 else 0 for j in range(64)]])
    add(qhead_row * S, t)

    E = Matrix(eq_rows)
    b = Matrix(eq_rhs)
    F = E * L
    target = b - E * x0
    Fred, bred, equality_cert = independent_equalities(F, target)
    point_t, kernel_t, eq_hnf_cert = hnf_affine_full_row(Fred, bred)
    if not eq_hnf_cert["image_feasible"]:
        raise ValueError("signature equality coset is empty")
    base = x0 + L * point_t
    kernel = L * kernel_t
    assert E * base == b
    assert E * kernel == Matrix.zeros(E.rows, kernel.cols)
    assert all(int(v) % DEN == 0 for v in C * base - rvec)
    assert all(int(v) % DEN == 0 for v in C * kernel)
    assert kernel.rank() == kernel.cols

    cert = {
        **congruence_cert,
        "coordinate_system": "primitive_picard_basis_x",
        "selected_membership_congruences_eliminated_by_basis_choice": True,
        "congruence_augmented_hnf": aug_cert,
        "projected_congruence_kernel_rank": int(L.rank()),
        "projected_congruence_kernel_determinant_abs": abs(int(L.det())),
        "projected_congruence_kernel_sha256": matrix_sha256(L),
        **equality_cert,
        "equality_hnf": eq_hnf_cert,
        "final_kernel_dimension": kernel.cols,
        "final_kernel_rank": int(kernel.rank()),
        "final_base_sha256": canonical_sha256([int(v) for v in base]),
        "final_kernel_sha256": matrix_sha256(kernel),
        "selected_matrix_sha256": matrix_sha256(S),
    }
    return base, kernel, cert


class NodeBudgetExhausted(Exception):
    pass


def exact_search(
    core: dict[str, Any],
    signature_matrix: np.ndarray,
    types: list[str],
    base: Matrix,
    kernel: Matrix,
    cell: dict[str, Any],
    e: int,
    a: int,
    genus: int,
    node_limit: int,
) -> dict[str, Any]:
    started = time.perf_counter()
    gram = Matrix(core["basis_gram"])
    forms = Matrix(core["raw_cross_pairings_with_basis"])
    S = selected_matrix(core)
    dim = kernel.cols
    kernel_gram = -(kernel.T * gram * kernel)
    kernel_gram_f = fmpz_mat(matrix_list(kernel_gram))
    reduced_gram_f, lll_f = kernel_gram_f.lll(transform=True, rep="gram", gram="exact")
    lll = Matrix([[int(lll_f[i, j]) for j in range(dim)] for i in range(dim)])
    reduced_gram = Matrix([[int(reduced_gram_f[i, j]) for j in range(dim)] for i in range(dim)])
    assert abs(int(lll_f.det())) == 1
    reduced_kernel = kernel * lll.T
    assert reduced_gram == -(reduced_kernel.T * gram * reduced_kernel)
    Lsym, Dsym = reduced_gram.LDLdecomposition(hermitian=False)
    assert reduced_gram == Lsym * Dsym * Lsym.T
    assert all(Dsym[i, i] > 0 for i in range(dim))
    ldl_lower = [[to_fmpq(Lsym[i, j]) for j in range(dim)] for i in range(dim)]
    ldl_diag = [to_fmpq(Dsym[i, i]) for i in range(dim)]

    form_reduced = forms * reduced_kernel
    pruning_coefficients: list[list[fmpq]] = []
    for k in range(140):
        source = [fmpq(int(form_reduced[k, j])) for j in range(dim)]
        result: list[fmpq] = []
        for j in range(dim):
            value = source[j]
            for i in range(j):
                value -= result[i] * ldl_lower[j][i]
            result.append(value)
        pruning_coefficients.append(result)
    prefix_norms: list[list[fmpq]] = []
    for row in pruning_coefficients:
        accum = fmpq(0)
        values: list[fmpq] = []
        for i in range(dim):
            accum += row[i] * row[i] / ldl_diag[i]
            values.append(accum)
        prefix_norms.append(values)

    q0 = (base.T * gram * base)[0]
    cross = reduced_kernel.T * gram * base
    center_sym = reduced_gram.inv() * cross
    lower = -pilot.DEGREE - 2 + 2 * genus
    radius_sym = q0 - lower + (cross.T * reduced_gram.inv() * cross)[0]
    if radius_sym < 0:
        return {
            "solver_result": "UNSAT_RADIUS",
            "complete_for_existence": True,
            "enumeration_exhausted": True,
            "stopped_on_first_witness": False,
            "node_budget_exhausted": False,
            "node_limit": node_limit,
            "enumeration_node_count": 0,
            "checked_leaf_count": 0,
            "exact_survivor_count": 0,
            "survivors": [],
            "completed_square_radius": str(radius_sym),
            "final_kernel_dimension": dim,
            "elapsed_seconds": round(time.perf_counter() - started, 6),
        }
    center = [to_fmpq(v) for v in center_sym]
    radius = to_fmpq(radius_sym)
    form_center = forms * (base + reduced_kernel * center_sym)
    form_fixed = [to_fmpq(v) for v in form_center]
    caps = [pilot.NORMAL_CAP] * 92 + [pilot.EXCEPTIONAL_CAP] * 48

    coords = [0] * dim
    node_count = interval_reject = form_prune = leaf_count = 0
    transcript = hashlib.sha256()
    survivors: list[dict[str, Any]] = []
    stopped_on_witness = False
    left_groups, right_groups = pilot.base.split_groups(types)
    side_indices = {
        "L": sorted(left_groups["A"] + left_groups["B"] + left_groups["C"]),
        "R": sorted(right_groups["A"] + right_groups["B"] + right_groups["C"]),
    }
    lsig = np.array(pilot.decode_signature(int(cell["left_signature_hex"], 16)), dtype=np.int64)
    rsig = np.array(pilot.decode_signature(int(cell["right_signature_hex"], 16)), dtype=np.int64)

    def event(*parts: object) -> None:
        transcript.update("|".join(str(x) for x in parts).encode())
        transcript.update(b"\n")

    def viable(next_index: int, remaining: fmpq) -> bool:
        nonlocal form_prune
        for k in range(140):
            value = form_fixed[k]
            lo, hi = fmpq(0), fmpq(caps[k])
            if lo <= value <= hi:
                continue
            impossible = next_index < 0
            if not impossible:
                gap = lo - value if value < lo else value - hi
                impossible = gap * gap > remaining * prefix_norms[k][next_index]
            if impossible:
                form_prune += 1
                event("P", next_index, k, value, remaining)
                return False
        return True

    def verify_leaf(xvec: Matrix) -> dict[str, Any] | None:
        nonlocal leaf_count
        leaf_count += 1
        raw = forms * xvec
        if any(int(raw[i]) < 0 or int(raw[i]) > caps[i] for i in range(140)):
            return None
        H = Matrix([core["hyperplane"]])
        degree = int((H * gram * xvec)[0])
        if degree != pilot.DEGREE:
            raise AssertionError("degree mismatch")
        exc_mass = sum(int(raw[i]) for i in range(92, 140))
        a_mass = sum(int(raw[i]) for i in range(46))
        if exc_mass != e or a_mass != a:
            raise AssertionError("parent mass mismatch")
        square = int((xvec.T * gram * xvec)[0])
        if square < lower:
            return None
        selected = S * xvec
        selected_np = np.array([int(v) for v in selected], dtype=np.int64)
        for side, wanted in (("L", lsig), ("R", rsig)):
            got = np.zeros(64, dtype=np.int64)
            for j in side_indices[side]:
                got = (got + int(selected_np[j]) * signature_matrix[:, j].astype(np.int64)) % DEN
            if not np.array_equal(got, wanted):
                raise AssertionError("signature mismatch")
        xmass, ymass, zmass, t = map(int, cell["aggregate"])
        xl, yl, zl = map(int, cell["left_counts"])
        xr, yr, zr = map(int, cell["right_counts"])
        for groups, counts in ((left_groups, (xl, yl, zl)), (right_groups, (xr, yr, zr))):
            for kind, target in zip("ABC", counts):
                if sum(int(selected_np[j]) for j in groups[kind]) != int(target):
                    raise AssertionError("side count mismatch")
        if sum(int(selected_np[j]) for j in range(48, 52)) != t:
            raise AssertionError("qhead total mismatch")
        return {
            "basis_coordinates": [int(v) for v in xvec],
            "basis_coordinates_sha256": canonical_sha256([int(v) for v in xvec]),
            "selected_coordinates": [int(v) for v in selected],
            "selected_coordinates_sha256": canonical_sha256([int(v) for v in selected]),
            "self_intersection": square,
            "degree": degree,
            "exceptional_mass": exc_mass,
            "curve_group_mass": a_mass,
        }

    def local_limit(remaining: fmpq, diagonal: fmpq) -> int:
        bound = remaining / diagonal
        k = 0
        while fmpq(k * k) < bound:
            k += 1
        return k + 1

    def recurse(index: int, remaining: fmpq) -> None:
        nonlocal node_count, interval_reject, stopped_on_witness
        node_count += 1
        if node_limit > 0 and node_count > node_limit:
            raise NodeBudgetExhausted
        event("N", index, remaining)
        alpha = -center[index]
        for j in range(index + 1, dim):
            alpha += ldl_lower[j][index] * (coords[j] - center[j])
        exact_centre = -alpha
        base_int = int(exact_centre.p) // int(exact_centre.q)
        limit = local_limit(remaining, ldl_diag[index])
        for value in range(base_int - limit, base_int + limit + 1):
            transformed = fmpq(value) + alpha
            cost = ldl_diag[index] * transformed * transformed
            if cost > remaining:
                interval_reject += 1
                continue
            coords[index] = value
            for k in range(140):
                form_fixed[k] += pruning_coefficients[k][index] * transformed
            rem = remaining - cost
            if viable(index - 1, rem):
                if index:
                    recurse(index - 1, rem)
                else:
                    witness = verify_leaf(base + reduced_kernel * Matrix(coords))
                    if witness is not None:
                        survivors.append(witness)
                        event("S", witness["basis_coordinates_sha256"])
                        stopped_on_witness = True
            for k in range(140):
                form_fixed[k] -= pruning_coefficients[k][index] * transformed
            if stopped_on_witness:
                return

    exhausted = True
    budget_exhausted = False
    try:
        recurse(dim - 1, radius)
    except NodeBudgetExhausted:
        exhausted = False
        budget_exhausted = True

    if survivors:
        result = "SAT_WITNESS"
        complete_for_existence = True
    elif exhausted:
        result = "UNSAT"
        complete_for_existence = True
    else:
        result = "UNKNOWN_NODE_BUDGET"
        complete_for_existence = False

    return {
        "solver_result": result,
        "complete_for_existence": complete_for_existence,
        "enumeration_exhausted": exhausted and not stopped_on_witness,
        "stopped_on_first_witness": stopped_on_witness,
        "node_budget_exhausted": budget_exhausted,
        "node_limit": node_limit,
        "enumeration_node_count": min(node_count, node_limit + 1 if node_limit > 0 else node_count),
        "interval_rejection_count": interval_reject,
        "intersection_bound_prune_count": form_prune,
        "checked_leaf_count": leaf_count,
        "exact_survivor_count": len(survivors),
        "survivors": survivors,
        "final_kernel_dimension": dim,
        "kernel_gram_sha256": matrix_sha256(kernel_gram),
        "reduced_gram_sha256": matrix_sha256(reduced_gram),
        "lll_transform_sha256": matrix_sha256(lll),
        "completed_square_radius": rational_text(radius),
        "enumeration_transcript_sha256": transcript.hexdigest(),
        "elapsed_seconds": round(time.perf_counter() - started, 6),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--core", type=pathlib.Path, required=True)
    ap.add_argument("--cap-certificate", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    ap.add_argument("--exceptional-mass", type=int, required=True)
    ap.add_argument("--curve-group-mass", type=int, required=True)
    ap.add_argument("--genus", type=int, default=0, choices=(0, 1))
    ap.add_argument("--cell-index", type=int, required=True)
    ap.add_argument("--expected-cell-id", type=str, required=True)
    ap.add_argument("--node-limit", type=int, default=250000)
    args = ap.parse_args()

    started = time.perf_counter()
    core, _, cap_summary = load_and_verify(args.core, args.cap_certificate)
    assert cap_summary["certificate_canonical_sha256"] == EXPECTED_CAP_SHA
    transform = pilot.base.build_transform(core)
    quotient = pilot.base.quotient_data(transform["inv"])
    aggregate = pilot.base.aggregate_structure(transform["pair"], transform["h"])
    cells, inventory = pilot.build_signature_cells(quotient["K"], aggregate["types"], args.exceptional_mass, args.curve_group_mass)
    if not 0 <= args.cell_index < len(cells):
        raise SystemExit("cell index out of range")
    cell = cells[args.cell_index]
    if cell["cell_id"] != args.expected_cell_id:
        raise AssertionError(f"immutable cell mismatch {cell['cell_id']} != {args.expected_cell_id}")

    base, kernel, coset_cert = build_cell_coset(core, quotient["K"], aggregate["types"], cell, args.exceptional_mass, args.curve_group_mass)
    search = exact_search(core, quotient["K"], aggregate["types"], base, kernel, cell, args.exceptional_mass, args.curve_group_mass, args.genus, args.node_limit)
    report = {
        "schema": SCHEMA,
        "algorithm_id": ALGORITHM_ID,
        "parameters": {
            "degree": 8,
            "genus": args.genus,
            "exceptional_mass": args.exceptional_mass,
            "curve_group_mass": args.curve_group_mass,
            "cell_index": args.cell_index,
            "cell_id": cell["cell_id"],
            "node_limit": args.node_limit,
        },
        "signature_inventory": inventory,
        "signature_cell": cell,
        "transform_certificate": transform["certificate"],
        "qtail_certificate": quotient["certificate"],
        "coset_certificate": coset_cert,
        "search": search,
        "performance_pilot": True,
        "parent_exactly_closed": False,
        "theorem_credit": False,
        "audit_status": "PENDING",
        "receiver_credit": False,
        "FULL_D8_G0_ROW_COMPLETE": False,
        "FULL_D176_D192_NUMERICAL_ORBIT_CENSUS": False,
        "R29_LG2_NUMERICAL_COMPONENT_COMPLETE": False,
        "R29_LG2": "NOT_DISCHARGED",
        "R29_LG2_EFF": "NOT_DISCHARGED",
        "R29_LG2_MB": "NOT_DISCHARGED",
        "G10_LOWGENUS_PICARD": "AMBER",
        "tool_versions": {
            "python": platform.python_version(),
            "python_flint": flint.__version__,
            "sympy": sympy.__version__,
            "numpy": np.__version__,
        },
        "elapsed_seconds": round(time.perf_counter() - started, 6),
    }
    deterministic = {k: v for k, v in report.items() if k not in {"elapsed_seconds", "tool_versions"}}
    deterministic["search"] = {k: v for k, v in report["search"].items() if k != "elapsed_seconds"}
    report["deterministic_sha256_without_runtime"] = canonical_sha256(deterministic)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "e": args.exceptional_mass,
        "a": args.curve_group_mass,
        "cell": cell["cell_id"],
        "congruence_rows": coset_cert["deduplicated_congruence_row_count"],
        "equality_rank": coset_cert["independent_equality_row_count"],
        "kernel_dimension": coset_cert["final_kernel_dimension"],
        "result": search["solver_result"],
        "nodes": search["enumeration_node_count"],
        "leaves": search["checked_leaf_count"],
        "seconds": search["elapsed_seconds"],
        "canonical_sha256": report["deterministic_sha256_without_runtime"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
