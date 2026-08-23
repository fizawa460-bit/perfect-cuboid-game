#!/usr/bin/env python3
from __future__ import annotations

import argparse
import gzip
import hashlib
import importlib.util
import itertools
import json
import pathlib
import sys
import time
from typing import Iterator, Any

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
STAGE32_05 = HERE.parent / "32-05"
sys.path.insert(0, str(STAGE32_05))

spec = importlib.util.spec_from_file_location(
    "d8pilot", HERE / "run_d8_bounded_signature_cells.py"
)
pilot = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(pilot)
base = pilot.base
from cap_certificate import load_and_verify

SCHEMA = "STAGE32_D8_LOWMASS_MATERIALIZED_CLOSURE_V1"
ALGORITHM_ID = "D8_SIGNATURE_CELL_EXACT_MATERIALIZE_TO_16Q_QF_NIA_V1"


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def bounded_vectors(length: int, total: int, cap: int = 2) -> Iterator[tuple[int, ...]]:
    """Every vector in [0,cap]^length with the requested sum, exactly once."""
    if total < 0 or total > cap * length:
        return
    row = [0] * length

    def rec(pos: int, remaining: int) -> Iterator[tuple[int, ...]]:
        if pos == length:
            if remaining == 0:
                yield tuple(row)
            return
        slots = length - pos - 1
        lo = max(0, remaining - cap * slots)
        hi = min(cap, remaining)
        for value in range(lo, hi + 1):
            row[pos] = value
            yield from rec(pos + 1, remaining - value)
        row[pos] = 0

    yield from rec(0, total)


def side_assignments(
    signature_matrix: np.ndarray,
    groups: dict[str, list[int]],
    counts: tuple[int, int, int],
    target_signature: int,
) -> list[tuple[int, ...]]:
    """Materialize the exact bounded assignments represented by one side-state."""
    pieces: list[list[tuple[int, ...]]] = []
    for kind, total in zip("ABC", counts):
        cols = groups[kind]
        vectors: list[tuple[int, ...]] = []
        for values in bounded_vectors(len(cols), int(total), pilot.EXCEPTIONAL_CAP):
            sig = 0
            for col, value in zip(cols, values):
                if value:
                    sig = pilot.add_signature(
                        sig, pilot.scaled_signature(signature_matrix[:, col], value)
                    )
            # Keep the local vector and filter the combined A/B/C signature below.
            vectors.append(values)
        pieces.append(vectors)

    out: list[tuple[int, ...]] = []
    for avec, bvec, cvec in itertools.product(*pieces):
        full = [0] * 48
        sig = 0
        for kind, values in zip("ABC", (avec, bvec, cvec)):
            for col, value in zip(groups[kind], values):
                full[col] = int(value)
                if value:
                    sig = pilot.add_signature(
                        sig, pilot.scaled_signature(signature_matrix[:, col], value)
                    )
        if sig == target_signature:
            out.append(tuple(full))
    return out


def materialize_cells(
    signature_matrix: np.ndarray,
    types: list[str],
    cells: list[dict[str, Any]],
    expected_total: int,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    left_groups, right_groups = base.split_groups(types)
    assignments: list[dict[str, Any]] = []
    cell_rows: list[dict[str, Any]] = []

    for cell in cells:
        left = side_assignments(
            signature_matrix,
            left_groups,
            tuple(map(int, cell["left_counts"])),
            int(cell["left_signature_hex"], 16),
        )
        right = side_assignments(
            signature_matrix,
            right_groups,
            tuple(map(int, cell["right_counts"])),
            int(cell["right_signature_hex"], 16),
        )
        if len(left) != int(cell["left_assignment_count"]):
            raise AssertionError((cell["cell_id"], "left", len(left), cell["left_assignment_count"]))
        if len(right) != int(cell["right_assignment_count"]):
            raise AssertionError((cell["cell_id"], "right", len(right), cell["right_assignment_count"]))

        expected_cell = len(left) * len(right)
        produced = 0
        for lv in left:
            for rv in right:
                vec = tuple(int(lv[j] + rv[j]) for j in range(48))
                # The sides are disjoint, so no selected exceptional coordinate can exceed 2.
                assert all(0 <= value <= pilot.EXCEPTIONAL_CAP for value in vec)
                payload = {
                    "cell_id": cell["cell_id"],
                    "aggregate": list(map(int, cell["aggregate"])),
                    "exceptional_values": list(vec),
                }
                payload["assignment_id"] = canonical_sha256(payload)[:24]
                assignments.append(payload)
                produced += 1
        if produced != expected_cell:
            raise AssertionError((cell["cell_id"], produced, expected_cell))
        cell_rows.append({
            "cell_id": cell["cell_id"],
            "left_materialized": len(left),
            "right_materialized": len(right),
            "materialized_assignment_count": produced,
        })

    if len(assignments) != expected_total:
        raise AssertionError((len(assignments), expected_total))
    ids = [row["assignment_id"] for row in assignments]
    if len(set(ids)) != len(ids):
        raise AssertionError("materialized exceptional assignment duplication/collision")
    assignments.sort(key=lambda row: row["assignment_id"])
    return assignments, cell_rows


def solve_fixed_exceptional(
    transform: dict[str, Any],
    assignment: dict[str, Any],
    e: int,
    a: int,
    genus: int,
    timeout_seconds: float,
    proof_dir: pathlib.Path | None,
) -> tuple[dict[str, Any], dict[str, Any] | None]:
    import z3

    if proof_dir is not None:
        z3.set_param(proof=True)
        proof_dir.mkdir(parents=True, exist_ok=True)

    exceptional = np.array(assignment["exceptional_values"], dtype=np.int64)
    inv = transform["inv"]
    pairings = transform["pair"]
    hform = transform["h"]
    gram = transform["gram"]
    qvars = [z3.Int(f"q{j+1}") for j in range(16)]
    solver = z3.SolverFor("QF_NIA")
    solver.set(random_seed=0, threads=1)
    if timeout_seconds > 0:
        solver.set(timeout=int(timeout_seconds * 1000))
    for q in qvars:
        solver.add(q >= 0, q <= pilot.QCAP)

    for i in range(64):
        constant = int(inv[i, :48] @ exceptional)
        terms = [int(inv[i, 48+j]) * qvars[j] for j in range(16) if inv[i, 48+j]]
        solver.add((constant + (z3.Sum(terms) if terms else 0)) % 8 == 0)

    pexpr = []
    for i in range(140):
        constant = int(pairings[i, :48] @ exceptional)
        terms = [int(pairings[i, 48+j]) * qvars[j] for j in range(16) if pairings[i, 48+j]]
        expr = constant + (z3.Sum(terms) if terms else 0)
        pexpr.append(expr)
        cap = pilot.NORMAL_CAP if i < 92 else pilot.EXCEPTIONAL_CAP
        solver.add(expr >= 0, expr <= 8 * cap)

    constant_h = int(hform[:48] @ exceptional)
    hterms = [int(hform[48+j]) * qvars[j] for j in range(16) if hform[48+j]]
    solver.add(constant_h + (z3.Sum(hterms) if hterms else 0) == 8 * pilot.DEGREE)
    solver.add(z3.Sum(pexpr[92:]) == 8 * e)
    solver.add(z3.Sum(pexpr[:46]) == 8 * a)
    solver.add(z3.Sum(pexpr[:92]) + 5 * z3.Sum(pexpr[92:]) == 8 * 19 * pilot.DEGREE)
    solver.add(z3.Sum(qvars[:4]) == int(assignment["aggregate"][3]))

    constant_square = int(exceptional @ gram[:48, :48] @ exceptional)
    linear_terms = []
    for j in range(16):
        coefficient = int(2 * (exceptional @ gram[:48, 48+j]))
        if coefficient:
            linear_terms.append(coefficient * qvars[j])
    quadratic_terms = []
    for i in range(16):
        for j in range(16):
            coefficient = int(gram[48+i, 48+j])
            if coefficient:
                quadratic_terms.append(coefficient * qvars[i] * qvars[j])
    lower = -pilot.DEGREE - 2 + 2 * genus
    solver.add(
        constant_square
        + (z3.Sum(linear_terms) if linear_terms else 0)
        + (z3.Sum(quadratic_terms) if quadratic_terms else 0)
        >= 64 * lower
    )

    started = time.perf_counter()
    result = solver.check()
    elapsed = time.perf_counter() - started
    row: dict[str, Any] = {
        "assignment_id": assignment["assignment_id"],
        "cell_id": assignment["cell_id"],
        "solver_result": str(result),
        "elapsed_seconds": round(elapsed, 6),
    }
    survivor = None
    if result == z3.sat:
        model = solver.model()
        qvalues = [model.eval(q, model_completion=True).as_long() for q in qvars]
        selected = np.array(list(exceptional) + qvalues, dtype=np.int64)
        assert np.all((inv @ selected) % 8 == 0)
        numerator = pairings @ selected
        assert np.all(numerator % 8 == 0)
        ints = numerator // 8
        assert np.all((ints[:92] >= 0) & (ints[:92] <= pilot.NORMAL_CAP))
        assert np.all((ints[92:] >= 0) & (ints[92:] <= pilot.EXCEPTIONAL_CAP))
        assert int(ints[92:].sum()) == e
        assert int(ints[:46].sum()) == a
        assert int(hform @ selected) == 8 * pilot.DEGREE
        assert int(selected @ gram @ selected) >= 64 * lower
        row["q_values"] = qvalues
        row["intersection_vector_sha256"] = canonical_sha256(ints.astype(int).tolist())
        survivor = dict(row)
    elif result == z3.unsat and proof_dir is not None:
        proof_raw = (solver.proof().sexpr() + "\n").encode()
        name = f"assignment-{assignment['assignment_id']}.sexpr.gz"
        with gzip.open(proof_dir / name, "wb", compresslevel=9) as handle:
            handle.write(proof_raw)
        row["proof_sha256"] = hashlib.sha256(proof_raw).hexdigest()
        row["proof_gzip_name"] = name
    elif result != z3.unsat:
        row["unknown_reason"] = solver.reason_unknown()
    return row, survivor


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--core", type=pathlib.Path, required=True)
    parser.add_argument("--cap-certificate", type=pathlib.Path, required=True)
    parser.add_argument("--output-dir", type=pathlib.Path, required=True)
    parser.add_argument("--exceptional-mass", type=int, required=True)
    parser.add_argument("--curve-group-mass", type=int, required=True)
    parser.add_argument("--genus", type=int, choices=(0, 1), default=0)
    parser.add_argument("--assignment-timeout", type=float, default=5.0)
    parser.add_argument("--max-materialized", type=int, default=10000)
    parser.add_argument("--proof", action="store_true")
    args = parser.parse_args()

    started = time.perf_counter()
    core, _, cap_summary = load_and_verify(args.core, args.cap_certificate)
    assert cap_summary["certificate_canonical_sha256"] == pilot.EXPECTED_CAP_SHA
    transform = base.build_transform(core)
    quotient = base.quotient_data(transform["inv"])
    aggregate = base.aggregate_structure(transform["pair"], transform["h"])
    cells, inventory = pilot.build_signature_cells(
        quotient["K"], aggregate["types"], args.exceptional_mass, args.curve_group_mass
    )
    expected = int(inventory["exceptional_assignment_count_after_qtail_quotient"])
    if expected > args.max_materialized:
        raise SystemExit(f"materialization budget exceeded: {expected}>{args.max_materialized}")

    assignments, cell_rows = materialize_cells(
        quotient["K"], aggregate["types"], cells, expected
    )
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "materialized-assignments.json").write_text(
        json.dumps(assignments, indent=2, sort_keys=True) + "\n"
    )

    solver_rows: list[dict[str, Any]] = []
    survivors: list[dict[str, Any]] = []
    proof_dir = args.output_dir / "proofs" if args.proof else None
    for assignment in assignments:
        row, survivor = solve_fixed_exceptional(
            transform,
            assignment,
            args.exceptional_mass,
            args.curve_group_mass,
            args.genus,
            args.assignment_timeout,
            proof_dir,
        )
        solver_rows.append(row)
        if survivor is not None:
            survivors.append(survivor)
        if row["solver_result"] == "unknown":
            break

    closed = bool(
        len(solver_rows) == len(assignments)
        and not survivors
        and all(row["solver_result"] == "unsat" for row in solver_rows)
    )
    report = {
        "schema": SCHEMA,
        "algorithm_id": ALGORITHM_ID,
        "parameters": {
            "degree": pilot.DEGREE,
            "genus": args.genus,
            "exceptional_mass": args.exceptional_mass,
            "curve_group_mass": args.curve_group_mass,
            "exceptional_cap": pilot.EXCEPTIONAL_CAP,
            "normal_cap": pilot.NORMAL_CAP,
            "assignment_timeout_seconds": args.assignment_timeout,
            "max_materialized": args.max_materialized,
        },
        "signature_inventory": inventory,
        "signature_cells_sha256": canonical_sha256(cells),
        "materialization": {
            "cell_rows": cell_rows,
            "materialized_assignment_count": len(assignments),
            "materialized_assignments_sha256": canonical_sha256(assignments),
            "complete_against_signature_inventory": len(assignments) == expected,
            "duplicate_assignment_count": len(assignments) - len({row['assignment_id'] for row in assignments}),
        },
        "solver_rows": solver_rows,
        "solver_row_count": len(solver_rows),
        "survivor_count": len(survivors),
        "survivors": survivors,
        "parent_exactly_closed": closed,
        "theorem_credit": False,
        "audit_status": "PENDING",
        "receiver_credit": False,
        "FULL_D176_D192_NUMERICAL_ORBIT_CENSUS": False,
        "R29_LG2_NUMERICAL_COMPONENT_COMPLETE": False,
        "R29_LG2": "NOT_DISCHARGED",
        "R29_LG2_EFF": "NOT_DISCHARGED",
        "R29_LG2_MB": "NOT_DISCHARGED",
        "G10_LOWGENUS_PICARD": "AMBER",
        "elapsed_seconds": round(time.perf_counter() - started, 6),
    }
    report["deterministic_manifest_sha256"] = canonical_sha256(
        {k: v for k, v in report.items() if k not in {"elapsed_seconds", "solver_rows", "deterministic_manifest_sha256"}}
    )
    (args.output_dir / "manifest.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "e": args.exceptional_mass,
        "a": args.curve_group_mass,
        "cells": len(cells),
        "materialized": len(assignments),
        "solver_rows": len(solver_rows),
        "survivors": len(survivors),
        "closed": closed,
        "first_nonunsat": next((r for r in solver_rows if r['solver_result'] != 'unsat'), None),
        "elapsed_seconds": report["elapsed_seconds"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
