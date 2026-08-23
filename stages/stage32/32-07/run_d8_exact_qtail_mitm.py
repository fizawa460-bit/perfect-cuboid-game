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

HERE = pathlib.Path(__file__).resolve().parent
STAGE32_05 = HERE.parent / "32-05"
sys.path.insert(0, str(STAGE32_05))

spec = importlib.util.spec_from_file_location(
    "lowmass", HERE / "run_d8_materialized_lowmass.py"
)
lowmass = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(lowmass)
pilot = lowmass.pilot
base = pilot.base
from cap_certificate import load_and_verify

SCHEMA = "STAGE32_D8_EXACT_QTAIL_MITM_SHARD_V1"
ALGORITHM_ID = "D8_FIXED_EXCEPTIONAL_QHEAD4_QTAIL6PLUS6_EXHAUSTIVE_V1"


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def residue_bytes(values: np.ndarray) -> bytes:
    return np.asarray(values % 8, dtype=np.uint8).tobytes()


def prepare_qtail(transform: dict[str, Any]) -> tuple[list[tuple[tuple[int, ...], np.ndarray]], dict[bytes, list[tuple[int, ...]]], dict[str, Any]]:
    inv = transform["inv"]
    left_indices = list(range(52, 58))
    right_indices = list(range(58, 64))

    left: list[tuple[tuple[int, ...], np.ndarray]] = []
    left_keys: set[bytes] = set()
    for values in itertools.product(range(pilot.QCAP + 1), repeat=6):
        vec = np.array(values, dtype=np.int64)
        residue = (inv[:, left_indices] @ vec) % 8
        key = residue_bytes(residue)
        left_keys.add(key)
        left.append((tuple(map(int, values)), residue.astype(np.int16)))

    right: dict[bytes, list[tuple[int, ...]]] = {}
    for values in itertools.product(range(pilot.QCAP + 1), repeat=6):
        vec = np.array(values, dtype=np.int64)
        key = residue_bytes(inv[:, right_indices] @ vec)
        right.setdefault(key, []).append(tuple(map(int, values)))

    cert = {
        "qtail_left_state_count": len(left),
        "qtail_right_state_count": sum(len(v) for v in right.values()),
        "qtail_left_residue_key_count": len(left_keys),
        "qtail_right_residue_key_count": len(right),
        "qtail_domain": [0, pilot.QCAP],
        "left_coordinate_indices_1based": list(range(53, 59)),
        "right_coordinate_indices_1based": list(range(59, 65)),
    }
    assert cert["qtail_left_state_count"] == 5**6
    assert cert["qtail_right_state_count"] == 5**6
    return left, right, cert


def enumerate_assignment(
    core: dict[str, Any],
    transform: dict[str, Any],
    left_tail: list[tuple[tuple[int, ...], np.ndarray]],
    right_tail: dict[bytes, list[tuple[int, ...]]],
    assignment: dict[str, Any],
    e: int,
    a: int,
    genus: int,
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    inv = transform["inv"]
    pairings = transform["pair"]
    hform = transform["h"]
    gram = transform["gram"]
    exceptional = np.array(assignment["exceptional_values"], dtype=np.int64)
    t = int(assignment["aggregate"][3])
    lower = -pilot.DEGREE - 2 + 2 * genus
    qhead_count = 0
    residue_join_count = 0
    survivors: list[dict[str, Any]] = []

    for qhead_values in itertools.product(range(pilot.QCAP + 1), repeat=4):
        if sum(qhead_values) != t:
            continue
        qhead_count += 1
        qhead = np.array(qhead_values, dtype=np.int64)
        fixed_residue = (inv[:, :48] @ exceptional + inv[:, 48:52] @ qhead) % 8
        target = (-fixed_residue) % 8

        for left_values, left_residue in left_tail:
            right_key = residue_bytes(target - left_residue)
            right_values_list = right_tail.get(right_key)
            if not right_values_list:
                continue
            for right_values in right_values_list:
                residue_join_count += 1
                selected = np.concatenate(
                    [
                        exceptional,
                        qhead,
                        np.array(left_values, dtype=np.int64),
                        np.array(right_values, dtype=np.int64),
                    ]
                )
                basis_numerator = inv @ selected
                if np.any(basis_numerator % 8):
                    raise AssertionError("qtail residue join admitted a non-Picard vector")
                basis = basis_numerator // 8

                pairing_numerator = pairings @ selected
                if np.any(pairing_numerator % 8):
                    raise AssertionError("integral Picard vector has nonintegral known pairing")
                intersections = pairing_numerator // 8
                if np.any(intersections[:92] < 0) or np.any(intersections[:92] > pilot.NORMAL_CAP):
                    continue
                if np.any(intersections[92:] < 0) or np.any(intersections[92:] > pilot.EXCEPTIONAL_CAP):
                    continue
                if int(intersections[92:].sum()) != e:
                    continue
                if int(intersections[:46].sum()) != a:
                    continue
                if int(intersections[:92].sum() + 5 * intersections[92:].sum()) != 19 * pilot.DEGREE:
                    continue
                if int(hform @ selected) != 8 * pilot.DEGREE:
                    continue
                square_numerator = int(selected @ gram @ selected)
                if square_numerator % 64:
                    raise AssertionError("integral Picard vector has nonintegral square")
                self_intersection = square_numerator // 64
                if self_intersection < lower:
                    continue

                # Independent recomputation in the original basis.
                raw = np.array(core["raw_cross_pairings_with_basis"], dtype=np.int64)
                original_gram = np.array(core["basis_gram"], dtype=np.int64)
                hyperplane = np.array(core["hyperplane"], dtype=np.int64)
                direct_intersections = raw @ basis
                if not np.array_equal(direct_intersections, intersections):
                    raise AssertionError("transformed/direct intersection mismatch")
                direct_degree = int(hyperplane @ original_gram @ basis)
                direct_square = int(basis @ original_gram @ basis)
                if direct_degree != pilot.DEGREE or direct_square != self_intersection:
                    raise AssertionError("transformed/direct degree or square mismatch")

                known = np.array(core["known_classes"], dtype=np.int64)
                known_matches = np.where(np.all(known == basis, axis=1))[0].tolist()
                survivor = {
                    "assignment_id": assignment["assignment_id"],
                    "cell_id": assignment["cell_id"],
                    "qhead_values": list(map(int, qhead_values)),
                    "qtail_left_values": list(map(int, left_values)),
                    "qtail_right_values": list(map(int, right_values)),
                    "selected_coordinates": selected.astype(int).tolist(),
                    "basis_coordinates": basis.astype(int).tolist(),
                    "basis_coordinates_sha256": canonical_sha256(basis.astype(int).tolist()),
                    "intersection_vector_sha256": canonical_sha256(intersections.astype(int).tolist()),
                    "degree": direct_degree,
                    "self_intersection": direct_square,
                    "adjunction_lower_bound": lower,
                    "known_class_matches_1based": [int(i + 1) for i in known_matches],
                }
                survivor["survivor_id"] = canonical_sha256(
                    {k: v for k, v in survivor.items() if k != "survivor_id"}
                )[:24]
                survivors.append(survivor)

    # The selected 64 coordinates form an invertible system, so selected-vector
    # equality is exactly Picard-class equality.  Dedup nevertheless and assert
    # that no two finite-enumeration paths produced the same class.
    ids = [canonical_sha256(row["selected_coordinates"]) for row in survivors]
    if len(set(ids)) != len(ids):
        raise AssertionError("duplicate numerical Picard class within one assignment")
    survivors.sort(key=lambda row: row["survivor_id"])
    row = {
        "assignment_id": assignment["assignment_id"],
        "cell_id": assignment["cell_id"],
        "qhead_sum": t,
        "qhead_assignment_count": qhead_count,
        "qtail_residue_join_count": residue_join_count,
        "survivor_count": len(survivors),
        "survivor_list_sha256": canonical_sha256(survivors),
        "complete": True,
    }
    return row, survivors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--core", type=pathlib.Path, required=True)
    parser.add_argument("--cap-certificate", type=pathlib.Path, required=True)
    parser.add_argument("--output-dir", type=pathlib.Path, required=True)
    parser.add_argument("--exceptional-mass", type=int, required=True)
    parser.add_argument("--curve-group-mass", type=int, required=True)
    parser.add_argument("--genus", type=int, choices=(0, 1), default=0)
    parser.add_argument("--max-materialized", type=int, default=10000)
    parser.add_argument("--shard-index", type=int, required=True)
    parser.add_argument("--shard-count", type=int, required=True)
    args = parser.parse_args()
    if not 0 <= args.shard_index < args.shard_count:
        raise SystemExit("invalid shard index")

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
    assignments, cell_rows = lowmass.materialize_cells(
        quotient["K"], aggregate["types"], cells, expected
    )
    shard = [row for i, row in enumerate(assignments) if i % args.shard_count == args.shard_index]
    left_tail, right_tail, tail_cert = prepare_qtail(transform)

    assignment_rows: list[dict[str, Any]] = []
    survivors: list[dict[str, Any]] = []
    for assignment in shard:
        row, found = enumerate_assignment(
            core,
            transform,
            left_tail,
            right_tail,
            assignment,
            args.exceptional_mass,
            args.curve_group_mass,
            args.genus,
        )
        assignment_rows.append(row)
        survivors.extend(found)

    selected_ids = [canonical_sha256(row["selected_coordinates"]) for row in survivors]
    if len(set(selected_ids)) != len(selected_ids):
        raise AssertionError("duplicate numerical Picard class across assignments in shard")
    survivors.sort(key=lambda row: row["survivor_id"])
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
            "shard_index": args.shard_index,
            "shard_count": args.shard_count,
        },
        "signature_inventory": inventory,
        "materialized_assignment_count_global": len(assignments),
        "materialized_cell_rows": cell_rows,
        "qtail_enumeration_certificate": tail_cert,
        "shard_assignment_count": len(shard),
        "shard_assignment_ids": [row["assignment_id"] for row in shard],
        "assignment_rows": assignment_rows,
        "assignment_rows_sha256": canonical_sha256(assignment_rows),
        "survivor_count": len(survivors),
        "survivors": survivors,
        "survivor_list_sha256": canonical_sha256(survivors),
        "complete_for_shard": len(assignment_rows) == len(shard) and all(row["complete"] for row in assignment_rows),
        "theorem_credit": False,
        "audit_status": "PENDING",
        "receiver_credit": False,
        "effectivity_credit": False,
        "orbit_census_credit": False,
        "FULL_D176_D192_NUMERICAL_ORBIT_CENSUS": False,
        "R29_LG2_NUMERICAL_COMPONENT_COMPLETE": False,
        "R29_LG2": "NOT_DISCHARGED",
        "R29_LG2_EFF": "NOT_DISCHARGED",
        "R29_LG2_MB": "NOT_DISCHARGED",
        "G10_LOWGENUS_PICARD": "AMBER",
        "elapsed_seconds": round(time.perf_counter() - started, 6),
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "manifest.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "shard": args.shard_index,
        "assignments": len(shard),
        "joins": sum(r["qtail_residue_join_count"] for r in assignment_rows),
        "survivors": len(survivors),
        "complete": report["complete_for_shard"],
        "elapsed_seconds": report["elapsed_seconds"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
