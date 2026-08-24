#!/usr/bin/env python3
from __future__ import annotations

import argparse
import collections
import importlib.util
import itertools
import json
import pathlib
import sys
import time
from typing import Any, Iterator

import numpy as np
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


pilot = load_module("stage32_07_materialize", S32_07 / "run_d8_bounded_signature_cells.py")
coset = load_module("stage32_08_coset", HERE / "run_signature_cell_affine_coset.py")
from cap_certificate import load_and_verify

SCHEMA = "STAGE32_D8_MATERIALIZED_SIGNATURE_CELL_QTAIL_PILOT_V1"
ALGORITHM_ID = "D8_SIGNATURE_CELL_EXACT_ASSIGNMENT_MATERIALIZE_FIX52_TO_QTAIL12_FP140_V1"
EXPECTED_CAP_SHA = "75224aee543dcd4a56e814503765d1e1e69514b237fb900688243546ea6b4d03"


def bounded_compositions(length: int, total: int, cap: int) -> Iterator[tuple[int, ...]]:
    row = [0] * length

    def rec(i: int, left: int) -> Iterator[tuple[int, ...]]:
        if i == length:
            if left == 0:
                yield tuple(row)
            return
        lo = max(0, left - cap * (length - i - 1))
        hi = min(cap, left)
        for value in range(lo, hi + 1):
            row[i] = value
            yield from rec(i + 1, left - value)

    yield from rec(0, total)


def group_assignment_map(signature_matrix: np.ndarray, columns: list[int], total: int) -> dict[int, list[tuple[int, ...]]]:
    out: dict[int, list[tuple[int, ...]]] = {}
    scaled = {
        (j, v): pilot.scaled_signature(signature_matrix[:, j], v)
        for j in columns
        for v in range(pilot.EXCEPTIONAL_CAP + 1)
    }
    for values in bounded_compositions(len(columns), total, pilot.EXCEPTIONAL_CAP):
        sig = 0
        for j, value in zip(columns, values):
            sig = pilot.add_signature(sig, scaled[(j, value)])
        out.setdefault(sig, []).append(values)
    for rows in out.values():
        rows.sort()
    return out


def materialize_side(
    signature_matrix: np.ndarray,
    groups: dict[str, list[int]],
    counts: tuple[int, int, int],
    target_signature: int,
) -> list[tuple[int, ...]]:
    maps = {
        kind: group_assignment_map(signature_matrix, groups[kind], count)
        for kind, count in zip("ABC", counts)
    }
    result: list[tuple[int, ...]] = []
    for sig_a, rows_a in sorted(maps["A"].items()):
        for sig_b, rows_b in sorted(maps["B"].items()):
            partial = pilot.add_signature(sig_a, sig_b)
            needed_c = pilot.add_signature(target_signature, pilot.neg_signature(partial))
            rows_c = maps["C"].get(needed_c, [])
            for va in rows_a:
                for vb in rows_b:
                    for vc in rows_c:
                        full = [0] * 48
                        for kind, values in (("A", va), ("B", vb), ("C", vc)):
                            for j, value in zip(groups[kind], values):
                                full[j] = int(value)
                        result.append(tuple(full))
    result.sort()
    return result


def qhead_assignments(total: int) -> list[tuple[int, int, int, int]]:
    return sorted(
        tuple(int(v) for v in values)
        for values in itertools.product(range(pilot.QCAP + 1), repeat=4)
        if sum(values) == total
    )


def hform(core: dict[str, Any]) -> list[int]:
    gram = Matrix(core["basis_gram"])
    H = Matrix([core["hyperplane"]])
    return [int(v) for v in H * gram]


def build_fixed52_coset(
    core: dict[str, Any],
    exceptional: tuple[int, ...],
    qhead: tuple[int, int, int, int],
    e: int,
    a: int,
) -> tuple[Matrix, Matrix, dict[str, Any]]:
    S = coset.selected_matrix(core)
    forms = Matrix(core["raw_cross_pairings_with_basis"])
    rows: list[list[int]] = []
    rhs: list[int] = []

    for i, value in enumerate(exceptional + qhead):
        rows.append([int(S[i, j]) for j in range(64)])
        rhs.append(int(value))

    # Redundant exact parent locks are included deliberately.  The independent
    # row reducer proves whether they add rank instead of relying only on the
    # aggregate-type identities used to discover the signature cell.
    rows.append(hform(core))
    rhs.append(pilot.DEGREE)
    rows.append([sum(int(forms[i, j]) for i in range(92, 140)) for j in range(64)])
    rhs.append(e)
    rows.append([sum(int(forms[i, j]) for i in range(46)) for j in range(64)])
    rhs.append(a)
    rows.append([sum(int(forms[i, j]) for i in range(92)) for j in range(64)])
    rhs.append(19 * pilot.DEGREE - 5 * e)

    E = Matrix(rows)
    b = Matrix(rhs)
    Ered, bred, red_cert = coset.independent_equalities(E, b)
    base, kernel, hnf_cert = coset.hnf_affine_full_row(Ered, bred)
    if not hnf_cert["image_feasible"]:
        raise AssertionError("materialized signature branch unexpectedly has empty linear lattice image")
    assert E * base == b
    assert E * kernel == Matrix.zeros(E.rows, kernel.cols)
    assert kernel.rank() == kernel.cols
    return base, kernel, {
        **red_cert,
        "fixed_selected_coordinate_count": 52,
        "fixed_exceptional_coordinate_count": 48,
        "fixed_qhead_coordinate_count": 4,
        "hnf": hnf_cert,
        "kernel_dimension": kernel.cols,
        "kernel_rank": int(kernel.rank()),
        "base_sha256": coset.canonical_sha256([int(v) for v in base]),
        "kernel_sha256": coset.matrix_sha256(kernel),
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
    cells, inventory = pilot.build_signature_cells(
        quotient["K"], aggregate["types"], args.exceptional_mass, args.curve_group_mass
    )
    cell = cells[args.cell_index]
    assert cell["cell_id"] == args.expected_cell_id

    left_groups, right_groups = pilot.base.split_groups(aggregate["types"])
    left = materialize_side(
        quotient["K"], left_groups, tuple(map(int, cell["left_counts"])), int(cell["left_signature_hex"], 16)
    )
    right = materialize_side(
        quotient["K"], right_groups, tuple(map(int, cell["right_counts"])), int(cell["right_signature_hex"], 16)
    )
    assert len(left) == int(cell["left_assignment_count"])
    assert len(right) == int(cell["right_assignment_count"])
    qheads = qhead_assignments(int(cell["aggregate"][3]))
    assert qheads

    exceptional_vectors: list[tuple[int, ...]] = []
    for lrow in left:
        for rrow in right:
            combined = tuple(lrow[i] + rrow[i] for i in range(48))
            # The side column sets are disjoint, so addition is exactly a union.
            assert all(0 <= value <= pilot.EXCEPTIONAL_CAP for value in combined)
            exceptional_vectors.append(combined)
    exceptional_vectors = sorted(set(exceptional_vectors))
    assert len(exceptional_vectors) == len(left) * len(right)

    branches: list[dict[str, Any]] = []
    witness = None
    any_unknown = False
    for branch_index, (exceptional, qhead) in enumerate(itertools.product(exceptional_vectors, qheads)):
        base, kernel, linear_cert = build_fixed52_coset(
            core, exceptional, qhead, args.exceptional_mass, args.curve_group_mass
        )
        search = coset.exact_search(
            core,
            quotient["K"],
            aggregate["types"],
            base,
            kernel,
            cell,
            args.exceptional_mass,
            args.curve_group_mass,
            args.genus,
            args.node_limit_per_branch,
        )
        row = {
            "branch_index": branch_index,
            "exceptional_coordinates_sha256": coset.canonical_sha256(list(exceptional)),
            "qhead_coordinates": list(qhead),
            "linear_certificate": linear_cert,
            "search": search,
        }
        branches.append(row)
        if search["solver_result"] == "SAT_WITNESS":
            witness = search["survivors"][0]
            break
        if not search["complete_for_existence"]:
            any_unknown = True

    total_branch_count = len(exceptional_vectors) * len(qheads)
    if witness is not None:
        result = "SAT_WITNESS"
        complete = True
    elif len(branches) == total_branch_count and not any_unknown:
        result = "UNSAT"
        complete = True
    else:
        result = "UNKNOWN_NODE_BUDGET"
        complete = False

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
        "signature_cell": cell,
        "signature_cell_inventory_sha256": inventory["cell_inventory_sha256"],
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
        "branches": branches,
        "executed_branch_count": len(branches),
        "solver_result": result,
        "complete_for_existence": complete,
        "witness": witness,
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
        "elapsed_seconds": round(time.perf_counter() - started, 6),
    }
    deterministic = {k: v for k, v in report.items() if k != "elapsed_seconds"}
    report["canonical_sha256_without_elapsed"] = coset.canonical_sha256(deterministic)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "cell": cell["cell_id"],
        "e": args.exceptional_mass,
        "a": args.curve_group_mass,
        "left": len(left),
        "right": len(right),
        "qhead": len(qheads),
        "branches_total": total_branch_count,
        "branches_executed": len(branches),
        "kernel_dimensions": sorted(set(r["linear_certificate"]["kernel_dimension"] for r in branches)),
        "nodes": sum(int(r["search"]["enumeration_node_count"]) for r in branches),
        "result": result,
        "seconds": report["elapsed_seconds"],
        "canonical_sha256": report["canonical_sha256_without_elapsed"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
