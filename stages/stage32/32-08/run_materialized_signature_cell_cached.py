#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import pathlib
import sys
import time
from typing import Any

import numpy as np
from flint import fmpq, fmpz_mat
from sympy import Matrix

HERE = pathlib.Path(__file__).resolve().parent
S32 = HERE.parent
S32_05 = S32 / "32-05"
S32_07 = S32 / "32-07"
sys.path.insert(0, str(S32_05))


def load_module(name: str, path: pathlib.Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


pilot = load_module("stage32_07_materialized_cached", S32_07 / "run_d8_bounded_signature_cells.py")
coset = load_module("stage32_08_coset_cached", HERE / "run_signature_cell_affine_coset.py")
v1 = load_module("stage32_08_materialized_v1", HERE / "run_materialized_signature_cell.py")
from cap_certificate import load_and_verify

SCHEMA = "STAGE32_D8_MATERIALIZED_SIGNATURE_CELL_QTAIL_CACHED_V2"
ALGORITHM_ID = "D8_FIX52_SHARED_HNF_LLL_QTAIL12_FP140_CACHED_V2"
EXPECTED_CAP_SHA = "75224aee543dcd4a56e814503765d1e1e69514b237fb900688243546ea6b4d03"


class NodeBudgetExhausted(Exception):
    pass


def fixed52_equation_matrix(core: dict[str, Any]) -> Matrix:
    S = coset.selected_matrix(core)
    forms = Matrix(core["raw_cross_pairings_with_basis"])
    rows: list[list[int]] = []
    for i in range(52):
        rows.append([int(S[i, j]) for j in range(64)])
    rows.append(v1.hform(core))
    rows.append([sum(int(forms[i, j]) for i in range(92, 140)) for j in range(64)])
    rows.append([sum(int(forms[i, j]) for i in range(46)) for j in range(64)])
    rows.append([sum(int(forms[i, j]) for i in range(92)) for j in range(64)])
    return Matrix(rows)


def independent_row_indices(E: Matrix) -> list[int]:
    chosen: list[int] = []
    rank = 0
    for i in range(E.rows):
        candidate = Matrix([[int(E[r, j]) for j in range(E.cols)] for r in chosen + [i]])
        new_rank = candidate.rank()
        if new_rank > rank:
            chosen.append(i)
            rank = new_rank
    return chosen


def prepare_common(core: dict[str, Any]) -> dict[str, Any]:
    started = time.perf_counter()
    E = fixed52_equation_matrix(core)
    indices = independent_row_indices(E)
    Ered = Matrix([[int(E[i, j]) for j in range(E.cols)] for i in indices])
    m = Ered.rows
    assert Ered.rank() == m
    assert m == 52

    raw = fmpz_mat(coset.matrix_list(Ered.T))
    hnf_f, transform_f = raw.hnf(transform=True)
    hnf = Matrix([[int(hnf_f[i, j]) for j in range(hnf_f.ncols())] for i in range(hnf_f.nrows())])
    transform = Matrix([[int(transform_f[i, j]) for j in range(transform_f.ncols())] for i in range(transform_f.nrows())])
    assert hnf == transform * Ered.T
    assert abs(int(transform_f.det())) == 1
    assert all(hnf[i, j] == 0 for i in range(m, 64) for j in range(m))
    U = transform.T
    affine = U[:, :m]
    kernel = U[:, m:]
    image_basis = Ered * affine
    assert image_basis == hnf[:m, :].T
    assert Ered * kernel == Matrix.zeros(m, 64 - m)
    assert kernel.rank() == 12
    image_basis_inv = image_basis.inv()

    gram = Matrix(core["basis_gram"])
    forms = Matrix(core["raw_cross_pairings_with_basis"])
    S = coset.selected_matrix(core)
    kernel_gram = -(kernel.T * gram * kernel)
    reduced_gram_f, lll_f = fmpz_mat(coset.matrix_list(kernel_gram)).lll(
        transform=True, rep="gram", gram="exact"
    )
    dim = kernel.cols
    lll = Matrix([[int(lll_f[i, j]) for j in range(dim)] for i in range(dim)])
    reduced_gram = Matrix([[int(reduced_gram_f[i, j]) for j in range(dim)] for i in range(dim)])
    assert abs(int(lll_f.det())) == 1
    reduced_kernel = kernel * lll.T
    assert reduced_gram == -(reduced_kernel.T * gram * reduced_kernel)
    Lsym, Dsym = reduced_gram.LDLdecomposition(hermitian=False)
    assert reduced_gram == Lsym * Dsym * Lsym.T
    assert all(Dsym[i, i] > 0 for i in range(dim))
    ldl_lower = [[coset.to_fmpq(Lsym[i, j]) for j in range(dim)] for i in range(dim)]
    ldl_diag = [coset.to_fmpq(Dsym[i, i]) for i in range(dim)]
    reduced_gram_inv = reduced_gram.inv()

    form_reduced = forms * reduced_kernel
    pruning_coefficients: list[list[fmpq]] = []
    for k in range(140):
        source = [fmpq(int(form_reduced[k, j])) for j in range(dim)]
        row: list[fmpq] = []
        for j in range(dim):
            value = source[j]
            for i in range(j):
                value -= row[i] * ldl_lower[j][i]
            row.append(value)
        pruning_coefficients.append(row)
    prefix_norms: list[list[fmpq]] = []
    for row in pruning_coefficients:
        accum = fmpq(0)
        values: list[fmpq] = []
        for i in range(dim):
            accum += row[i] * row[i] / ldl_diag[i]
            values.append(accum)
        prefix_norms.append(values)

    certificate = {
        "equation_row_count": E.rows,
        "independent_row_indices_0based": indices,
        "independent_row_count": m,
        "kernel_dimension": kernel.cols,
        "equation_matrix_sha256": coset.matrix_sha256(E),
        "independent_equation_matrix_sha256": coset.matrix_sha256(Ered),
        "image_basis_sha256": coset.matrix_sha256(image_basis),
        "kernel_sha256": coset.matrix_sha256(kernel),
        "kernel_gram_sha256": coset.matrix_sha256(kernel_gram),
        "lll_transform_sha256": coset.matrix_sha256(lll),
        "reduced_kernel_sha256": coset.matrix_sha256(reduced_kernel),
        "reduced_gram_sha256": coset.matrix_sha256(reduced_gram),
        "all_140_lower_and_upper_caps_preprojected": True,
        "shared_across_all_materialized_branches": True,
    }
    certificate["canonical_sha256_without_this_field"] = coset.canonical_sha256(certificate)
    return {
        "E": E,
        "indices": indices,
        "Ered": Ered,
        "affine": affine,
        "kernel": kernel,
        "image_basis": image_basis,
        "image_basis_inv": image_basis_inv,
        "gram": gram,
        "forms": forms,
        "S": S,
        "reduced_kernel": reduced_kernel,
        "reduced_gram": reduced_gram,
        "reduced_gram_inv": reduced_gram_inv,
        "ldl_lower": ldl_lower,
        "ldl_diag": ldl_diag,
        "pruning_coefficients": pruning_coefficients,
        "prefix_norms": prefix_norms,
        "certificate": certificate,
        "preparation_seconds": round(time.perf_counter() - started, 6),
    }


def branch_rhs(exceptional: tuple[int, ...], qhead: tuple[int, int, int, int], e: int, a: int) -> Matrix:
    values = list(exceptional + qhead)
    values += [pilot.DEGREE, e, a, 19 * pilot.DEGREE - 5 * e]
    assert len(values) == 56
    return Matrix(values)


def branch_base(common: dict[str, Any], rhs: Matrix) -> tuple[Matrix, dict[str, Any]]:
    bred = Matrix([int(rhs[i]) for i in common["indices"]])
    coords = common["image_basis_inv"] * bred
    feasible = all(v.q == 1 for v in coords)
    if not feasible:
        raise AssertionError("materialized branch unexpectedly fails shared HNF image test")
    base = common["affine"] * coords
    assert all(v.q == 1 for v in base)
    base = Matrix([int(v) for v in base])
    assert common["E"] * base == rhs
    return base, {
        "shared_image_feasible": True,
        "image_coordinates_sha256": coset.canonical_sha256([int(v) for v in coords]),
        "base_sha256": coset.canonical_sha256([int(v) for v in base]),
    }


def search_prepared(
    common: dict[str, Any],
    core: dict[str, Any],
    signature_matrix: np.ndarray,
    types: list[str],
    base: Matrix,
    cell: dict[str, Any],
    e: int,
    a: int,
    genus: int,
    node_limit: int,
) -> dict[str, Any]:
    started = time.perf_counter()
    gram = common["gram"]
    forms = common["forms"]
    S = common["S"]
    reduced_kernel = common["reduced_kernel"]
    reduced_gram = common["reduced_gram"]
    reduced_gram_inv = common["reduced_gram_inv"]
    ldl_lower = common["ldl_lower"]
    ldl_diag = common["ldl_diag"]
    pruning_coefficients = common["pruning_coefficients"]
    prefix_norms = common["prefix_norms"]
    dim = reduced_kernel.cols

    q0 = (base.T * gram * base)[0]
    cross = reduced_kernel.T * gram * base
    center_sym = reduced_gram_inv * cross
    lower = -pilot.DEGREE - 2 + 2 * genus
    radius_sym = q0 - lower + (cross.T * reduced_gram_inv * cross)[0]
    if radius_sym < 0:
        return {
            "solver_result": "UNSAT_RADIUS",
            "complete_for_existence": True,
            "enumeration_exhausted": True,
            "stopped_on_first_witness": False,
            "node_budget_exhausted": False,
            "node_limit": node_limit,
            "enumeration_node_count": 0,
            "interval_rejection_count": 0,
            "intersection_bound_prune_count": 0,
            "checked_leaf_count": 0,
            "exact_survivor_count": 0,
            "survivors": [],
            "final_kernel_dimension": dim,
            "completed_square_radius": str(radius_sym),
            "enumeration_transcript_sha256": hashlib.sha256(b"").hexdigest(),
            "elapsed_seconds": round(time.perf_counter() - started, 6),
        }
    center = [coset.to_fmpq(v) for v in center_sym]
    radius = coset.to_fmpq(radius_sym)
    form_center = forms * (base + reduced_kernel * center_sym)
    form_fixed = [coset.to_fmpq(v) for v in form_center]
    caps = [pilot.NORMAL_CAP] * 92 + [pilot.EXCEPTIONAL_CAP] * 48

    left_groups, right_groups = pilot.base.split_groups(types)
    side_indices = {
        "L": sorted(left_groups["A"] + left_groups["B"] + left_groups["C"]),
        "R": sorted(right_groups["A"] + right_groups["B"] + right_groups["C"]),
    }
    lsig = np.array(pilot.decode_signature(int(cell["left_signature_hex"], 16)), dtype=np.int64)
    rsig = np.array(pilot.decode_signature(int(cell["right_signature_hex"], 16)), dtype=np.int64)

    coords = [0] * dim
    node_count = interval_reject = form_prune = leaf_count = 0
    transcript = hashlib.sha256()
    survivors: list[dict[str, Any]] = []
    stopped_on_witness = False

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
        assert degree == pilot.DEGREE
        exc_mass = sum(int(raw[i]) for i in range(92, 140))
        a_mass = sum(int(raw[i]) for i in range(46))
        assert exc_mass == e and a_mass == a
        square = int((xvec.T * gram * xvec)[0])
        if square < lower:
            return None
        selected = S * xvec
        selected_np = np.array([int(v) for v in selected], dtype=np.int64)
        for side, wanted in (("L", lsig), ("R", rsig)):
            got = np.zeros(64, dtype=np.int64)
            for j in side_indices[side]:
                got = (got + int(selected_np[j]) * signature_matrix[:, j].astype(np.int64)) % 8
            assert np.array_equal(got, wanted)
        _, _, _, t = map(int, cell["aggregate"])
        xl, yl, zl = map(int, cell["left_counts"])
        xr, yr, zr = map(int, cell["right_counts"])
        for groups, counts in ((left_groups, (xl, yl, zl)), (right_groups, (xr, yr, zr))):
            for kind, target in zip("ABC", counts):
                assert sum(int(selected_np[j]) for j in groups[kind]) == int(target)
        assert sum(int(selected_np[j]) for j in range(48, 52)) == t
        return {
            "basis_coordinates": [int(v) for v in xvec],
            "basis_coordinates_sha256": coset.canonical_sha256([int(v) for v in xvec]),
            "selected_coordinates": [int(v) for v in selected],
            "selected_coordinates_sha256": coset.canonical_sha256([int(v) for v in selected]),
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
        complete = True
    elif exhausted:
        result = "UNSAT"
        complete = True
    else:
        result = "UNKNOWN_NODE_BUDGET"
        complete = False
    return {
        "solver_result": result,
        "complete_for_existence": complete,
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
        "completed_square_radius": coset.rational_text(radius),
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
    ap.add_argument("--genus", type=int, choices=(0, 1), default=0)
    ap.add_argument("--cell-index", type=int, required=True)
    ap.add_argument("--expected-cell-id", required=True)
    ap.add_argument("--node-limit-per-branch", type=int, default=100000)
    args = ap.parse_args()

    started = time.perf_counter()
    core, _, cap_summary = load_and_verify(args.core, args.cap_certificate)
    assert cap_summary["certificate_canonical_sha256"] == EXPECTED_CAP_SHA
    transform = pilot.base.build_transform(core)
    quotient = pilot.base.quotient_data(transform["inv"])
    aggregate = pilot.base.aggregate_structure(transform["pair"], transform["h"])
    cells, inventory = pilot.build_signature_cells(quotient["K"], aggregate["types"], args.exceptional_mass, args.curve_group_mass)
    cell = cells[args.cell_index]
    assert cell["cell_id"] == args.expected_cell_id

    left_groups, right_groups = pilot.base.split_groups(aggregate["types"])
    left = v1.materialize_side(quotient["K"], left_groups, tuple(map(int, cell["left_counts"])), int(cell["left_signature_hex"], 16))
    right = v1.materialize_side(quotient["K"], right_groups, tuple(map(int, cell["right_counts"])), int(cell["right_signature_hex"], 16))
    assert len(left) == int(cell["left_assignment_count"])
    assert len(right) == int(cell["right_assignment_count"])
    qheads = v1.qhead_assignments(int(cell["aggregate"][3]))

    exceptional_vectors = sorted({tuple(l[i] + r[i] for i in range(48)) for l in left for r in right})
    assert len(exceptional_vectors) == len(left) * len(right)
    total_branch_count = len(exceptional_vectors) * len(qheads)

    common = prepare_common(core)
    branches: list[dict[str, Any]] = []
    witness = None
    any_unknown = False
    for branch_index, (exceptional, qhead) in enumerate(itertools.product(exceptional_vectors, qheads)):
        rhs = branch_rhs(exceptional, qhead, args.exceptional_mass, args.curve_group_mass)
        base, base_cert = branch_base(common, rhs)
        search = search_prepared(
            common, core, quotient["K"], aggregate["types"], base, cell,
            args.exceptional_mass, args.curve_group_mass, args.genus, args.node_limit_per_branch,
        )
        branches.append({
            "branch_index": branch_index,
            "exceptional_coordinates_sha256": coset.canonical_sha256(list(exceptional)),
            "qhead_coordinates": list(qhead),
            "base_certificate": base_cert,
            "search": search,
        })
        if search["solver_result"] == "SAT_WITNESS":
            witness = search["survivors"][0]
            break
        if not search["complete_for_existence"]:
            any_unknown = True

    if witness is not None:
        result, complete = "SAT_WITNESS", True
    elif len(branches) == total_branch_count and not any_unknown:
        result, complete = "UNSAT", True
    else:
        result, complete = "UNKNOWN_NODE_BUDGET", False

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
            "node_limit_per_branch": args.node_limit_per_branch,
        },
        "signature_cell_inventory_sha256": inventory["cell_inventory_sha256"],
        "signature_cell": cell,
        "materialization": {
            "left_assignment_count": len(left),
            "right_assignment_count": len(right),
            "exceptional_vector_count": len(exceptional_vectors),
            "qhead_assignment_count": len(qheads),
            "total_branch_count": total_branch_count,
            "all_exceptional_assignments_materialized": True,
            "all_qhead_assignments_materialized": True,
            "fixed_selected_coordinate_count_per_branch": 52,
        },
        "shared_context": common["certificate"],
        "shared_context_preparation_seconds": common["preparation_seconds"],
        "branches": branches,
        "executed_branch_count": len(branches),
        "solver_result": result,
        "complete_for_existence": complete,
        "witness": witness,
        "performance_regression": True,
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
        "elapsed_seconds": round(time.perf_counter() - started, 6),
    }
    deterministic = {k: v for k, v in report.items() if k not in {"elapsed_seconds", "shared_context_preparation_seconds"}}
    deterministic["branches"] = [
        {**r, "search": {k: v for k, v in r["search"].items() if k != "elapsed_seconds"}}
        for r in report["branches"]
    ]
    report["deterministic_sha256_without_runtime"] = coset.canonical_sha256(deterministic)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "e": args.exceptional_mass,
        "a": args.curve_group_mass,
        "cell": cell["cell_id"],
        "branches_total": total_branch_count,
        "branches_executed": len(branches),
        "kernel_dimension": common["certificate"]["kernel_dimension"],
        "common_prep_seconds": common["preparation_seconds"],
        "nodes": sum(int(r["search"]["enumeration_node_count"]) for r in branches),
        "result": result,
        "witness_sha": witness["basis_coordinates_sha256"] if witness else None,
        "seconds": report["elapsed_seconds"],
        "deterministic_sha256": report["deterministic_sha256_without_runtime"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
