#!/usr/bin/env python3
from __future__ import annotations

import argparse
import functools
import gzip
import hashlib
import importlib.util
import itertools
import json
import pathlib
import sys
import time
from typing import Any

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
STAGE32_05 = HERE.parent / "32-05"
sys.path.insert(0, str(STAGE32_05))
spec = importlib.util.spec_from_file_location(
    "stage32_05_exact", STAGE32_05 / "run_exact_mitm_closure.py"
)
base = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(base)
from cap_certificate import load_and_verify

SCHEMA = "STAGE32_D8_BOUNDED_MULTIPLICITY_SIGNATURE_CELL_V1"
ALGORITHM_ID = "D8_CAP2_EXCEPTIONAL_QUOTIENT_SIGNATURE_CELLS_TO_EXACT_QF_NIA_V1"
DEGREE = 8
NORMAL_CAP = 4
EXCEPTIONAL_CAP = 2
QCAP = 4
EXPECTED_CAP_SHA = "75224aee543dcd4a56e814503765d1e1e69514b237fb900688243546ea6b4d03"
NIBBLE_MASK = sum(7 << (4 * i) for i in range(64))


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def encode_signature(column: np.ndarray) -> int:
    out = 0
    for i, value in enumerate(column.tolist()):
        out |= (int(value) & 7) << (4 * i)
    return out


def decode_signature(value: int) -> list[int]:
    return [(value >> (4 * i)) & 7 for i in range(64)]


def add_signature(a: int, b: int) -> int:
    # Every nibble stores one normalized Z/8Z digit.  A digitwise sum is at
    # most 14, hence ordinary integer addition cannot carry into the next
    # nibble.  Clearing each nibble's 8-bit gives exact addition mod 8.
    return (a + b) & NIBBLE_MASK


@functools.lru_cache(maxsize=None)
def neg_signature(value: int) -> int:
    out = 0
    for i in range(64):
        digit = (value >> (4 * i)) & 7
        out |= ((-digit) & 7) << (4 * i)
    return out


def scaled_signature(column: np.ndarray, multiplier: int) -> int:
    return encode_signature((column.astype(np.int16) * int(multiplier)) % 8)


def aggregate_solutions(e: int, a: int) -> list[tuple[int, int, int, int]]:
    # x,y,z are TOTAL bounded multiplicities in the A/B/C exceptional types,
    # not counts of nonzero coordinates.  This is the essential d=8 change.
    out: list[tuple[int, int, int, int]] = []
    for x in range(32 * EXCEPTIONAL_CAP + 1):
        for y in range(8 * EXCEPTIONAL_CAP + 1):
            for z in range(8 * EXCEPTIONAL_CAP + 1):
                if x + y + z != e:
                    continue
                for t in range(4 * QCAP + 1):
                    if 8 * y + 16 * z + 16 * t != 8 * DEGREE:
                        continue
                    if -24 * x + 32 * y + 96 * z + 120 * t != 8 * a:
                        continue
                    if (
                        -40 * x + 112 * y + 264 * z + 304 * t
                        != 8 * (19 * DEGREE - 5 * e)
                    ):
                        continue
                    out.append((x, y, z, t))
    return out


def type_signature_dp(
    signature_matrix: np.ndarray, columns: tuple[int, ...]
) -> dict[int, dict[int, int]]:
    """Exact DP: multiplicity sum -> quotient signature -> assignment count."""
    dp: dict[int, dict[int, int]] = {0: {0: 1}}
    multipliers = {
        j: [scaled_signature(signature_matrix[:, j], v) for v in range(EXCEPTIONAL_CAP + 1)]
        for j in columns
    }
    for j in columns:
        nxt: dict[int, dict[int, int]] = {}
        for total, states in dp.items():
            for signature, count in states.items():
                for value in range(EXCEPTIONAL_CAP + 1):
                    ntotal = total + value
                    nsig = add_signature(signature, multipliers[j][value])
                    bucket = nxt.setdefault(ntotal, {})
                    bucket[nsig] = bucket.get(nsig, 0) + count
        dp = nxt
    assert sum(sum(states.values()) for states in dp.values()) == (EXCEPTIONAL_CAP + 1) ** len(columns)
    return dp


def convolve_signature_maps(*maps: dict[int, int]) -> dict[int, int]:
    out: dict[int, int] = {0: 1}
    for current in maps:
        nxt: dict[int, int] = {}
        for a, ca in out.items():
            for b, cb in current.items():
                sig = add_signature(a, b)
                nxt[sig] = nxt.get(sig, 0) + ca * cb
        out = nxt
    return out


def build_signature_cells(
    signature_matrix: np.ndarray, types: list[str], e: int, a: int
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    left_groups, right_groups = base.split_groups(types)
    left_groups_t = {k: tuple(v) for k, v in left_groups.items()}
    right_groups_t = {k: tuple(v) for k, v in right_groups.items()}
    type_dp: dict[str, dict[str, dict[int, dict[int, int]]]] = {"L": {}, "R": {}}
    for side, groups in (("L", left_groups_t), ("R", right_groups_t)):
        for kind in "ABC":
            type_dp[side][kind] = type_signature_dp(signature_matrix, groups[kind])

    @functools.lru_cache(maxsize=None)
    def side_map(side: str, x: int, y: int, z: int) -> dict[int, int]:
        maps = [
            type_dp[side]["A"].get(x, {}),
            type_dp[side]["B"].get(y, {}),
            type_dp[side]["C"].get(z, {}),
        ]
        if any(not m for m in maps):
            return {}
        return convolve_signature_maps(*maps)

    # For q1..q4 in 0..4, verify exactly that the quotient signature depends
    # only on t=q1+...+q4.  We never infer this from the d=6 code path.
    qhead_by_total: dict[int, set[int]] = {}
    qhead_assignment_count: dict[int, int] = {}
    qcols = [signature_matrix[:, 48 + j] for j in range(4)]
    for values in itertools.product(range(QCAP + 1), repeat=4):
        total = sum(values)
        sig = 0
        for column, value in zip(qcols, values):
            sig = add_signature(sig, scaled_signature(column, value))
        qhead_by_total.setdefault(total, set()).add(sig)
        qhead_assignment_count[total] = qhead_assignment_count.get(total, 0) + 1
    assert sum(qhead_assignment_count.values()) == (QCAP + 1) ** 4
    assert all(len(values) == 1 for values in qhead_by_total.values())

    aggregate = aggregate_solutions(e, a)
    if not aggregate:
        raise SystemExit(f"aggregate-infeasible parent e={e} a={a}")

    cells: list[dict[str, Any]] = []
    exceptional_assignment_count = 0
    split_count = 0
    max_left_signature_states = 0
    max_right_signature_states = 0

    caps = {"A": 16 * EXCEPTIONAL_CAP, "B": 4 * EXCEPTIONAL_CAP, "C": 4 * EXCEPTIONAL_CAP}
    for x, y, z, t in aggregate:
        qsig = next(iter(qhead_by_total[t]))
        target_total = neg_signature(qsig)
        for xl in range(max(0, x - caps["A"]), min(caps["A"], x) + 1):
            xr = x - xl
            for yl in range(max(0, y - caps["B"]), min(caps["B"], y) + 1):
                yr = y - yl
                for zl in range(max(0, z - caps["C"]), min(caps["C"], z) + 1):
                    zr = z - zl
                    lm = side_map("L", xl, yl, zl)
                    rm = side_map("R", xr, yr, zr)
                    if not lm or not rm:
                        continue
                    split_count += 1
                    max_left_signature_states = max(max_left_signature_states, len(lm))
                    max_right_signature_states = max(max_right_signature_states, len(rm))
                    for lsig, lcount in lm.items():
                        rsig = add_signature(target_total, neg_signature(lsig))
                        rcount = rm.get(rsig)
                        if rcount is None:
                            continue
                        exceptional_assignment_count += lcount * rcount
                        payload = {
                            "aggregate": [x, y, z, t],
                            "left_counts": [xl, yl, zl],
                            "right_counts": [xr, yr, zr],
                            "left_signature_hex": f"{lsig:064x}",
                            "right_signature_hex": f"{rsig:064x}",
                            "left_assignment_count": lcount,
                            "right_assignment_count": rcount,
                        }
                        payload["cell_id"] = canonical_sha256(payload)[:24]
                        cells.append(payload)

    cells.sort(key=lambda row: row["cell_id"])
    if len({row["cell_id"] for row in cells}) != len(cells):
        raise AssertionError("signature cell id collision")
    inventory = {
        "aggregate_solutions": [list(row) for row in aggregate],
        "signature_cell_count": len(cells),
        "exceptional_assignment_count_after_qtail_quotient": exceptional_assignment_count,
        "split_count": split_count,
        "max_left_signature_states": max_left_signature_states,
        "max_right_signature_states": max_right_signature_states,
        "qhead_signature_count_by_total": {
            str(k): len(v) for k, v in sorted(qhead_by_total.items())
        },
        "qhead_assignment_count_by_total": {
            str(k): v for k, v in sorted(qhead_assignment_count.items())
        },
        "cell_inventory_sha256": canonical_sha256(cells),
        "bounded_multiplicity_domain": {"exceptional": [0, 2], "normal": [0, 4]},
    }
    return cells, inventory


def solve_cells(
    transform: dict[str, Any],
    signature_matrix: np.ndarray,
    types: list[str],
    cells: list[dict[str, Any]],
    e: int,
    a: int,
    genus: int,
    timeout_seconds: float,
    proof_dir: pathlib.Path | None,
    stop_on_unknown: bool,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    import z3

    if proof_dir is not None:
        z3.set_param(proof=True)
        proof_dir.mkdir(parents=True, exist_ok=True)

    inv = transform["inv"]
    pairings = transform["pair"]
    hform = transform["h"]
    gram = transform["gram"]
    left_groups, right_groups = base.split_groups(types)
    side_indices = {
        "L": sorted(left_groups["A"] + left_groups["B"] + left_groups["C"]),
        "R": sorted(right_groups["A"] + right_groups["B"] + right_groups["C"]),
    }

    ev = [z3.Int(f"e{j+1}") for j in range(48)]
    qv = [z3.Int(f"q{j+1}") for j in range(16)]
    selected = ev + qv
    solver = z3.SolverFor("QF_NIA")
    solver.set(random_seed=0, threads=1)
    if timeout_seconds > 0:
        solver.set(timeout=int(timeout_seconds * 1000))

    for value in ev:
        solver.add(value >= 0, value <= EXCEPTIONAL_CAP)
    for value in qv:
        solver.add(value >= 0, value <= QCAP)

    for i in range(64):
        terms = [int(inv[i, j]) * selected[j] for j in range(64) if inv[i, j]]
        solver.add(z3.Sum(terms) % 8 == 0)

    pexpr = []
    for i in range(140):
        terms = [int(pairings[i, j]) * selected[j] for j in range(64) if pairings[i, j]]
        expr = z3.Sum(terms)
        pexpr.append(expr)
        cap = NORMAL_CAP if i < 92 else EXCEPTIONAL_CAP
        solver.add(expr >= 0, expr <= 8 * cap)

    solver.add(z3.Sum([int(hform[j]) * selected[j] for j in range(64) if hform[j]]) == 8 * DEGREE)
    solver.add(z3.Sum(pexpr[92:]) == 8 * e)
    solver.add(z3.Sum(pexpr[:46]) == 8 * a)
    solver.add(z3.Sum(pexpr[:92]) + 5 * z3.Sum(pexpr[92:]) == 8 * 19 * DEGREE)

    lower = -DEGREE - 2 + 2 * genus
    qterms = []
    for i in range(64):
        for j in range(64):
            coefficient = int(gram[i, j])
            if coefficient:
                qterms.append(coefficient * selected[i] * selected[j])
    solver.add(z3.Sum(qterms) >= 64 * lower)

    rows: list[dict[str, Any]] = []
    survivors: list[dict[str, Any]] = []
    for cell_index, cell in enumerate(cells):
        solver.push()
        x, y, z, t = map(int, cell["aggregate"])
        xl, yl, zl = map(int, cell["left_counts"])
        xr, yr, zr = map(int, cell["right_counts"])
        solver.add(z3.Sum(qv[:4]) == t)
        for groups, counts in ((left_groups, (xl, yl, zl)), (right_groups, (xr, yr, zr))):
            for kind, target in zip("ABC", counts):
                solver.add(z3.Sum([ev[j] for j in groups[kind]]) == target)

        lsig = decode_signature(int(cell["left_signature_hex"], 16))
        rsig = decode_signature(int(cell["right_signature_hex"], 16))
        for r in range(64):
            lterms = [int(signature_matrix[r, j]) * ev[j] for j in side_indices["L"] if signature_matrix[r, j]]
            rterms = [int(signature_matrix[r, j]) * ev[j] for j in side_indices["R"] if signature_matrix[r, j]]
            solver.add((z3.Sum(lterms) if lterms else 0) % 8 == lsig[r])
            solver.add((z3.Sum(rterms) if rterms else 0) % 8 == rsig[r])

        started = time.perf_counter()
        result = solver.check()
        elapsed = time.perf_counter() - started
        entry: dict[str, Any] = {
            "cell_index": cell_index,
            "cell_id": cell["cell_id"],
            "solver_result": str(result),
            "elapsed_seconds": round(elapsed, 6),
        }
        if result == z3.sat:
            model = solver.model()
            values = [model.eval(v, model_completion=True).as_long() for v in selected]
            vec = np.array(values, dtype=np.int64)
            assert np.all((inv @ vec) % 8 == 0)
            numerator = pairings @ vec
            assert np.all(numerator % 8 == 0)
            ints = numerator // 8
            assert np.all((ints[:92] >= 0) & (ints[:92] <= NORMAL_CAP))
            assert np.all((ints[92:] >= 0) & (ints[92:] <= EXCEPTIONAL_CAP))
            assert int(ints[92:].sum()) == e
            assert int(ints[:46].sum()) == a
            assert int(hform @ vec) == 8 * DEGREE
            assert int(vec @ gram @ vec) >= 64 * lower
            entry["selected_coordinates"] = values
            entry["intersection_vector_sha256"] = canonical_sha256(ints.astype(int).tolist())
            survivors.append(dict(entry))
        elif result == z3.unsat and proof_dir is not None:
            proof_raw = (solver.proof().sexpr() + "\n").encode()
            name = f"cell-{cell_index:05d}-{cell['cell_id']}.sexpr.gz"
            with gzip.open(proof_dir / name, "wb", compresslevel=9) as handle:
                handle.write(proof_raw)
            entry["proof_sha256"] = hashlib.sha256(proof_raw).hexdigest()
            entry["proof_gzip_name"] = name
        elif result != z3.unsat:
            entry["unknown_reason"] = solver.reason_unknown()
        rows.append(entry)
        solver.pop()
        if result == z3.unknown and stop_on_unknown:
            break

    return rows, survivors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--core", type=pathlib.Path, required=True)
    parser.add_argument("--cap-certificate", type=pathlib.Path, required=True)
    parser.add_argument("--output-dir", type=pathlib.Path, required=True)
    parser.add_argument("--exceptional-mass", type=int, required=True)
    parser.add_argument("--curve-group-mass", type=int, required=True)
    parser.add_argument("--genus", type=int, choices=(0, 1), default=0)
    parser.add_argument("--cell-timeout", type=float, default=5.0)
    parser.add_argument("--count-only", action="store_true")
    parser.add_argument("--proof", action="store_true")
    parser.add_argument("--continue-after-unknown", action="store_true")
    args = parser.parse_args()

    started = time.perf_counter()
    core, _, cap_summary = load_and_verify(args.core, args.cap_certificate)
    assert cap_summary["certificate_canonical_sha256"] == EXPECTED_CAP_SHA
    transform = base.build_transform(core)
    quotient = base.quotient_data(transform["inv"])
    aggregate = base.aggregate_structure(transform["pair"], transform["h"])
    # The d=8 q-tail domain 0..4 reaches exactly the same residue subgroup as
    # 0..3 because every locked q-tail generator has order dividing 4 mod 8;
    # the extra value 4 contributes residue zero.  This is exact, not a relaxed
    # d=4-style quotient.
    qorders = quotient["certificate"]["qtail_column_orders_mod8"]
    assert all(4 % int(order) == 0 for order in qorders)
    qtail_domain_certificate = {
        "domain": [0, QCAP],
        "column_orders_mod8": qorders,
        "extra_value_4_is_zero_residue_for_every_generator": True,
        "reachable_residue_count": quotient["certificate"]["qtail_reachable_residue_count"],
        "subgroup_size_from_hnf_index": quotient["certificate"]["qtail_subgroup_size_from_hnf_index"],
        "quotient_role": "EXACT_FOR_LATTICE_RESIDUE_COMPLETION_ONLY",
    }
    assert qtail_domain_certificate["reachable_residue_count"] == qtail_domain_certificate["subgroup_size_from_hnf_index"]

    cells, inventory = build_signature_cells(
        quotient["K"], aggregate["types"], args.exceptional_mass, args.curve_group_mass
    )
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "signature-cells.json").write_text(json.dumps(cells, indent=2, sort_keys=True) + "\n")

    if args.count_only:
        rows: list[dict[str, Any]] = []
        survivors: list[dict[str, Any]] = []
    else:
        rows, survivors = solve_cells(
            transform,
            quotient["K"],
            aggregate["types"],
            cells,
            args.exceptional_mass,
            args.curve_group_mass,
            args.genus,
            args.cell_timeout,
            args.output_dir / "proofs" if args.proof else None,
            stop_on_unknown=not args.continue_after_unknown,
        )

    solved_all = (not args.count_only) and len(rows) == len(cells)
    exact_closed = bool(
        solved_all
        and not survivors
        and all(row["solver_result"] == "unsat" for row in rows)
    )
    report = {
        "schema": SCHEMA,
        "algorithm_id": ALGORITHM_ID,
        "parameters": {
            "degree": DEGREE,
            "genus": args.genus,
            "exceptional_mass": args.exceptional_mass,
            "curve_group_mass": args.curve_group_mass,
            "normal_cap": NORMAL_CAP,
            "exceptional_cap": EXCEPTIONAL_CAP,
            "normal_selected_coordinate_domain": [0, QCAP],
            "exceptional_selected_coordinate_domain": [0, EXCEPTIONAL_CAP],
            "cell_timeout_seconds": args.cell_timeout,
            "count_only": args.count_only,
        },
        "cap_verification": cap_summary,
        "transform_certificate": transform["certificate"],
        "qtail_subgroup_certificate": quotient["certificate"],
        "d8_qtail_domain_certificate": qtail_domain_certificate,
        "aggregate_certificate": aggregate["certificate"],
        "signature_inventory": inventory,
        "solver_rows": rows,
        "solver_row_count": len(rows),
        "survivor_count": len(survivors),
        "survivors": survivors,
        "parent_exactly_closed": exact_closed,
        "count_only_benchmark": args.count_only,
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
        "signature_cells": inventory["signature_cell_count"],
        "exceptional_assignments_after_quotient": inventory["exceptional_assignment_count_after_qtail_quotient"],
        "solver_rows": len(rows),
        "survivors": len(survivors),
        "closed": exact_closed,
        "count_only": args.count_only,
        "elapsed_seconds": report["elapsed_seconds"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
