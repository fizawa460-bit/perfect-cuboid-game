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
from flint import fmpq
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


pilot = load_module("stage32_07_exhaustive", S32_07 / "run_d8_bounded_signature_cells.py")
v1 = load_module("stage32_08_materialized_v1_exhaustive", HERE / "run_materialized_signature_cell.py")
cached = load_module("stage32_08_cached_exhaustive", HERE / "run_materialized_signature_cell_cached.py")
coset = load_module("stage32_08_coset_exhaustive", HERE / "run_signature_cell_affine_coset.py")
from cap_certificate import load_and_verify

SCHEMA = "STAGE32_D8_MATERIALIZED_CELL_EXHAUSTIVE_NUMERICAL_V1"
ALGORITHM_ID = "D8_FIX52_SHARED_QTAIL12_FP140_EXHAUSTIVE_SURVIVORS_V1"
EXPECTED_CAP_SHA = "75224aee543dcd4a56e814503765d1e1e69514b237fb900688243546ea6b4d03"


class NodeBudgetExhausted(Exception):
    pass


def search_exhaustive(
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
    """Exhaust the exact 12D branch; never stop after the first numerical survivor."""
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
    assert dim == 12

    q0 = (base.T * gram * base)[0]
    cross = reduced_kernel.T * gram * base
    center_sym = reduced_gram_inv * cross
    lower = -pilot.DEGREE - 2 + 2 * genus
    radius_sym = q0 - lower + (cross.T * reduced_gram_inv * cross)[0]
    if radius_sym < 0:
        return {
            "solver_result": "UNSAT_RADIUS",
            "complete_numerical_enumeration": True,
            "enumeration_exhausted": True,
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
                got = (
                    got
                    + int(selected_np[j]) * signature_matrix[:, j].astype(np.int64)
                ) % 8
            assert np.array_equal(got, wanted)

        _, _, _, t = map(int, cell["aggregate"])
        xl, yl, zl = map(int, cell["left_counts"])
        xr, yr, zr = map(int, cell["right_counts"])
        for groups, counts in (
            (left_groups, (xl, yl, zl)),
            (right_groups, (xr, yr, zr)),
        ):
            for kind, target in zip("ABC", counts):
                assert sum(int(selected_np[j]) for j in groups[kind]) == int(target)
        assert sum(int(selected_np[j]) for j in range(48, 52)) == t

        basis = [int(v) for v in xvec]
        selected_list = [int(v) for v in selected]
        return {
            "basis_coordinates": basis,
            "basis_coordinates_sha256": coset.canonical_sha256(basis),
            "selected_coordinates": selected_list,
            "selected_coordinates_sha256": coset.canonical_sha256(selected_list),
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
        nonlocal node_count, interval_reject
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
                    survivor = verify_leaf(base + reduced_kernel * Matrix(coords))
                    if survivor is not None:
                        survivors.append(survivor)
                        event("S", survivor["basis_coordinates_sha256"])
            for k in range(140):
                form_fixed[k] -= pruning_coefficients[k][index] * transformed

    exhausted = True
    budget_exhausted = False
    try:
        recurse(dim - 1, radius)
    except NodeBudgetExhausted:
        exhausted = False
        budget_exhausted = True

    survivors.sort(key=lambda row: tuple(row["basis_coordinates"]))
    survivor_keys = [tuple(row["basis_coordinates"]) for row in survivors]
    assert len(survivor_keys) == len(set(survivor_keys))

    if not exhausted:
        result = "UNKNOWN_NODE_BUDGET"
        complete = False
    elif survivors:
        result = "SAT_EXHAUSTED"
        complete = True
    else:
        result = "UNSAT"
        complete = True

    return {
        "solver_result": result,
        "complete_numerical_enumeration": complete,
        "enumeration_exhausted": exhausted,
        "node_budget_exhausted": budget_exhausted,
        "node_limit": node_limit,
        "enumeration_node_count": min(
            node_count, node_limit + 1 if node_limit > 0 else node_count
        ),
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
    ap.add_argument("--node-limit-per-branch", type=int, default=1000000)
    args = ap.parse_args()

    started = time.perf_counter()
    core, _, cap_summary = load_and_verify(args.core, args.cap_certificate)
    assert cap_summary["certificate_canonical_sha256"] == EXPECTED_CAP_SHA
    transform = pilot.base.build_transform(core)
    quotient = pilot.base.quotient_data(transform["inv"])
    aggregate = pilot.base.aggregate_structure(transform["pair"], transform["h"])
    cells, inventory = pilot.build_signature_cells(
        quotient["K"],
        aggregate["types"],
        args.exceptional_mass,
        args.curve_group_mass,
    )
    assert 0 <= args.cell_index < len(cells)
    cell = cells[args.cell_index]
    assert cell["cell_id"] == args.expected_cell_id

    left_groups, right_groups = pilot.base.split_groups(aggregate["types"])
    left = v1.materialize_side(
        quotient["K"],
        left_groups,
        tuple(map(int, cell["left_counts"])),
        int(cell["left_signature_hex"], 16),
    )
    right = v1.materialize_side(
        quotient["K"],
        right_groups,
        tuple(map(int, cell["right_counts"])),
        int(cell["right_signature_hex"], 16),
    )
    assert len(left) == int(cell["left_assignment_count"])
    assert len(right) == int(cell["right_assignment_count"])
    qheads = v1.qhead_assignments(int(cell["aggregate"][3]))

    exceptional_vectors = sorted(
        {
            tuple(l[i] + r[i] for i in range(48))
            for l in left
            for r in right
        }
    )
    assert len(exceptional_vectors) == len(left) * len(right)
    total_branch_count = len(exceptional_vectors) * len(qheads)

    common = cached.prepare_common(core)
    branches: list[dict[str, Any]] = []
    all_survivors: list[dict[str, Any]] = []
    any_unknown = False

    for branch_index, (exceptional, qhead) in enumerate(
        itertools.product(exceptional_vectors, qheads)
    ):
        rhs = cached.branch_rhs(
            exceptional, qhead, args.exceptional_mass, args.curve_group_mass
        )
        base, base_cert = cached.branch_base(common, rhs)
        search = search_exhaustive(
            common,
            core,
            quotient["K"],
            aggregate["types"],
            base,
            cell,
            args.exceptional_mass,
            args.curve_group_mass,
            args.genus,
            args.node_limit_per_branch,
        )
        branches.append(
            {
                "branch_index": branch_index,
                "exceptional_coordinates_sha256": coset.canonical_sha256(
                    list(exceptional)
                ),
                "qhead_coordinates": list(qhead),
                "base_certificate": base_cert,
                "search": search,
            }
        )
        all_survivors.extend(search["survivors"])
        if not search["complete_numerical_enumeration"]:
            any_unknown = True

    all_survivors.sort(key=lambda row: tuple(row["basis_coordinates"]))
    all_keys = [tuple(row["basis_coordinates"]) for row in all_survivors]
    assert len(all_keys) == len(set(all_keys))

    complete = len(branches) == total_branch_count and not any_unknown
    if not complete:
        result = "UNKNOWN_NODE_BUDGET"
    elif all_survivors:
        result = "SAT_EXHAUSTED"
    else:
        result = "UNSAT"

    report = {
        "schema": SCHEMA,
        "algorithm_id": ALGORITHM_ID,
        "parameters": {
            "degree": pilot.DEGREE,
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
        "complete_numerical_enumeration": complete,
        "exact_numerical_survivor_count": len(all_survivors),
        "numerical_survivors": all_survivors,
        "numerical_census_scope": "ONE_SIGNATURE_CELL_ONLY",
        "effectivity_classification_complete": False,
        "actual_curve_existence_claim": False,
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

    deterministic = {
        k: v
        for k, v in report.items()
        if k not in {"elapsed_seconds", "shared_context_preparation_seconds"}
    }
    deterministic["branches"] = [
        {
            **row,
            "search": {
                k: v
                for k, v in row["search"].items()
                if k != "elapsed_seconds"
            },
        }
        for row in report["branches"]
    ]
    report["deterministic_sha256_without_runtime"] = coset.canonical_sha256(
        deterministic
    )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "e": args.exceptional_mass,
                "a": args.curve_group_mass,
                "cell": cell["cell_id"],
                "branches": total_branch_count,
                "kernel_dimension": common["certificate"]["kernel_dimension"],
                "nodes": sum(
                    int(row["search"]["enumeration_node_count"])
                    for row in branches
                ),
                "leaves": sum(
                    int(row["search"]["checked_leaf_count"])
                    for row in branches
                ),
                "survivors": len(all_survivors),
                "result": result,
                "complete": complete,
                "seconds": report["elapsed_seconds"],
                "deterministic_sha256": report[
                    "deterministic_sha256_without_runtime"
                ],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
