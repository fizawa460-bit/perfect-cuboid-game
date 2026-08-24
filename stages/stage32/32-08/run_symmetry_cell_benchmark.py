#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import pathlib
import sys
import time
from typing import Any

import numpy as np

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


pilot = load_module("stage32_07_pilot", S32_07 / "run_d8_bounded_signature_cells.py")
orbit = load_module("stage32_07_orbit", S32_07 / "orbit_dedup_e2a54.py")
from cap_certificate import load_and_verify

SCHEMA = "STAGE32_D8_A_STABILIZER_SYMMETRY_BENCHMARK_V1"
ALGORITHM_ID = "D8_SIGNATURE_CELL_QF_NIA_WITH_EXACT_A_STABILIZER_LEX_V1"
EXPECTED_GROUP_ORDER = 1536
EXPECTED_A_STABILIZER_ORDER = 64
EXPECTED_CAP_SHA = "75224aee543dcd4a56e814503765d1e1e69514b237fb900688243546ea6b4d03"


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def inverse_exceptional_image(p: tuple[int, ...]) -> tuple[int, ...]:
    inv = orbit.invert_perm(p)
    out = tuple(inv[92 + j] - 92 for j in range(48))
    if sorted(out) != list(range(48)):
        raise AssertionError("Aut element does not preserve exceptional divisors")
    return out


def a_stabilizer(group: list[tuple[int, ...]]) -> list[tuple[int, ...]]:
    target = set(range(46))
    subgroup = [p for p in group if {p[i] for i in range(46)} == target]
    if len(subgroup) != EXPECTED_A_STABILIZER_ORDER:
        raise AssertionError(f"unexpected a-stabilizer order {len(subgroup)}")
    return subgroup


def lex_leq(z3, left, right):
    assert len(left) == len(right) and left
    expr = left[-1] <= right[-1]
    for i in range(len(left) - 2, -1, -1):
        expr = z3.Or(left[i] < right[i], z3.And(left[i] == right[i], expr))
    return expr


def build_solver(
    transform: dict[str, Any],
    signature_matrix: np.ndarray,
    types: list[str],
    e: int,
    a: int,
    genus: int,
    timeout_seconds: float,
    exceptional_image_maps: list[tuple[int, ...]],
):
    import z3

    inv = transform["inv"]
    pairings = transform["pair"]
    hform = transform["h"]
    gram = transform["gram"]
    left_groups, right_groups = pilot.base.split_groups(types)
    side_indices = {
        "L": sorted(left_groups["A"] + left_groups["B"] + left_groups["C"]),
        "R": sorted(right_groups["A"] + right_groups["B"] + right_groups["C"]),
    }

    # The first 48 selected coordinates are exactly intersections with the 48
    # exceptional divisors.  Reverify this rather than assuming the old order.
    expected = np.zeros((48, 64), dtype=np.int64)
    expected[:, :48] = 8 * np.eye(48, dtype=np.int64)
    if not np.array_equal(pairings[92:140, :], expected):
        raise AssertionError("selected exceptional coordinates are not the locked 48 exceptional intersections")

    ev = [z3.Int(f"e{j+1}") for j in range(48)]
    qv = [z3.Int(f"q{j+1}") for j in range(16)]
    selected = ev + qv
    solver = z3.SolverFor("QF_NIA")
    solver.set(random_seed=0, threads=1)
    if timeout_seconds > 0:
        solver.set(timeout=int(timeout_seconds * 1000))

    for value in ev:
        solver.add(value >= 0, value <= pilot.EXCEPTIONAL_CAP)
    for value in qv:
        solver.add(value >= 0, value <= pilot.QCAP)

    for i in range(64):
        terms = [int(inv[i, j]) * selected[j] for j in range(64) if inv[i, j]]
        solver.add(z3.Sum(terms) % 8 == 0)

    pexpr = []
    for i in range(140):
        terms = [int(pairings[i, j]) * selected[j] for j in range(64) if pairings[i, j]]
        expr = z3.Sum(terms)
        pexpr.append(expr)
        cap = pilot.NORMAL_CAP if i < 92 else pilot.EXCEPTIONAL_CAP
        solver.add(expr >= 0, expr <= 8 * cap)

    solver.add(z3.Sum([int(hform[j]) * selected[j] for j in range(64) if hform[j]]) == 8 * pilot.DEGREE)
    solver.add(z3.Sum(pexpr[92:]) == 8 * e)
    solver.add(z3.Sum(pexpr[:46]) == 8 * a)
    solver.add(z3.Sum(pexpr[:92]) + 5 * z3.Sum(pexpr[92:]) == 8 * 19 * pilot.DEGREE)

    lower = -pilot.DEGREE - 2 + 2 * genus
    qterms = []
    for i in range(64):
        for j in range(64):
            coefficient = int(gram[i, j])
            if coefficient:
                qterms.append(coefficient * selected[i] * selected[j])
    solver.add(z3.Sum(qterms) >= 64 * lower)

    # Exact parent-level symmetry breaking.  These constraints are deliberately
    # NOT interpreted cell-by-cell: an H_a element can move a class to another
    # signature cell, but it stays in the same (d,g,e,a) parent.  Searching all
    # cells with the same global canonicality condition therefore preserves one
    # representative of every parent orbit.
    for image_map in exceptional_image_maps:
        image = [ev[image_map[j]] for j in range(48)]
        solver.add(lex_leq(z3, ev, image))

    return solver, ev, qv, pexpr, left_groups, right_groups, side_indices


def benchmark_cells(
    transform: dict[str, Any],
    signature_matrix: np.ndarray,
    types: list[str],
    cells: list[dict[str, Any]],
    e: int,
    a: int,
    genus: int,
    timeout_seconds: float,
    cell_limit: int,
    exceptional_image_maps: list[tuple[int, ...]],
) -> list[dict[str, Any]]:
    import z3

    solver, ev, qv, _, left_groups, right_groups, side_indices = build_solver(
        transform,
        signature_matrix,
        types,
        e,
        a,
        genus,
        timeout_seconds,
        exceptional_image_maps,
    )

    rows: list[dict[str, Any]] = []
    selected_cells = cells[: min(len(cells), cell_limit)] if cell_limit > 0 else cells
    for cell_index, cell in enumerate(selected_cells):
        solver.push()
        x, y, z, t = map(int, cell["aggregate"])
        xl, yl, zl = map(int, cell["left_counts"])
        xr, yr, zr = map(int, cell["right_counts"])
        solver.add(z3.Sum(qv[:4]) == t)
        for groups, counts in ((left_groups, (xl, yl, zl)), (right_groups, (xr, yr, zr))):
            for kind, target in zip("ABC", counts):
                solver.add(z3.Sum([ev[j] for j in groups[kind]]) == target)

        lsig = pilot.decode_signature(int(cell["left_signature_hex"], 16))
        rsig = pilot.decode_signature(int(cell["right_signature_hex"], 16))
        for r in range(64):
            lterms = [
                int(signature_matrix[r, j]) * ev[j]
                for j in side_indices["L"]
                if signature_matrix[r, j]
            ]
            rterms = [
                int(signature_matrix[r, j]) * ev[j]
                for j in side_indices["R"]
                if signature_matrix[r, j]
            ]
            solver.add((z3.Sum(lterms) if lterms else 0) % 8 == lsig[r])
            solver.add((z3.Sum(rterms) if rterms else 0) % 8 == rsig[r])

        started = time.perf_counter()
        result = solver.check()
        elapsed = time.perf_counter() - started
        reason = solver.reason_unknown() if result == z3.unknown else ""
        rows.append(
            {
                "cell_index": cell_index,
                "cell_id": cell["cell_id"],
                "solver_result": str(result),
                "reason_unknown": reason,
                "elapsed_seconds": round(elapsed, 6),
            }
        )
        solver.pop()
    return rows


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--core", type=pathlib.Path, required=True)
    ap.add_argument("--cap-certificate", type=pathlib.Path, required=True)
    ap.add_argument("--action", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    ap.add_argument("--exceptional-mass", type=int, required=True)
    ap.add_argument("--curve-group-mass", type=int, required=True)
    ap.add_argument("--genus", type=int, default=0, choices=(0, 1))
    ap.add_argument("--cell-timeout", type=float, default=3.0)
    ap.add_argument("--cell-limit", type=int, default=16)
    ap.add_argument("--symmetry", choices=("none", "a-stabilizer"), required=True)
    args = ap.parse_args()

    started = time.perf_counter()
    core, _, cap_summary = load_and_verify(args.core, args.cap_certificate)
    assert cap_summary["certificate_canonical_sha256"] == EXPECTED_CAP_SHA
    action = json.loads(args.action.read_text())
    group, action_certificate = orbit.verify_permutations(core, action)
    assert len(group) == EXPECTED_GROUP_ORDER
    subgroup = a_stabilizer(group)

    # H_a must preserve all parent-level quantities used for this benchmark.
    assert all({p[i] for i in range(46)} == set(range(46)) for p in subgroup)
    assert all({p[i] for i in range(92, 140)} == set(range(92, 140)) for p in subgroup)

    identity = tuple(range(140))
    if args.symmetry == "a-stabilizer":
        maps = [inverse_exceptional_image(p) for p in subgroup if p != identity]
    else:
        maps = []

    transform = pilot.base.build_transform(core)
    quotient = pilot.base.quotient_data(transform["inv"])
    aggregate = pilot.base.aggregate_structure(transform["pair"], transform["h"])
    cells, inventory = pilot.build_signature_cells(
        quotient["K"], aggregate["types"], args.exceptional_mass, args.curve_group_mass
    )
    rows = benchmark_cells(
        transform,
        quotient["K"],
        aggregate["types"],
        cells,
        args.exceptional_mass,
        args.curve_group_mass,
        args.genus,
        args.cell_timeout,
        args.cell_limit,
        maps,
    )

    counts: dict[str, int] = {}
    for row in rows:
        counts[row["solver_result"]] = counts.get(row["solver_result"], 0) + 1
    report = {
        "schema": SCHEMA,
        "algorithm_id": ALGORITHM_ID,
        "parameters": {
            "degree": 8,
            "genus": args.genus,
            "exceptional_mass": args.exceptional_mass,
            "curve_group_mass": args.curve_group_mass,
            "cell_timeout_seconds": args.cell_timeout,
            "cell_limit": args.cell_limit,
            "symmetry": args.symmetry,
        },
        "aut_action": action_certificate,
        "full_aut_order": len(group),
        "a_stabilizer_order": len(subgroup),
        "a_stabilizer_nonidentity_lex_constraints": len(maps),
        "signature_cell_inventory": inventory,
        "benchmarked_cell_count": len(rows),
        "solver_result_counts": counts,
        "solver_rows": rows,
        "total_solver_seconds": round(sum(r["elapsed_seconds"] for r in rows), 6),
        "performance_only": True,
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
    report["canonical_sha256_without_runtime"] = canonical_sha256(
        {k: v for k, v in report.items() if k not in {"solver_rows", "elapsed_seconds", "total_solver_seconds", "canonical_sha256_without_runtime"}}
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "e": args.exceptional_mass,
                "a": args.curve_group_mass,
                "symmetry": args.symmetry,
                "cells_total": inventory["signature_cell_count"],
                "cells_benchmarked": len(rows),
                "results": counts,
                "solver_seconds": report["total_solver_seconds"],
                "a_stabilizer_order": len(subgroup),
                "canonical_sha256": report["canonical_sha256_without_runtime"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
