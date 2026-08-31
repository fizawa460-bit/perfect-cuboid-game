#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

from sympy import Matrix
from z3 import Real, SolverFor, unknown, unsat

from certify_stage32_21ba_r51_interval_census import (
    EXPECTED_MATRIX_SHA256,
    EXPECTED_PAIRINGS,
    EXPECTED_RANK,
    EXPECTED_SOURCE_LOCK_SHA256,
    EXPECTED_TRIPLES,
    EXPECTED_U_SHA256,
    R51_GLOBAL_HI,
    R51_GLOBAL_LO,
    derive_initial_bounds,
    integer_interval,
    load_source_lock,
    matrix_payload,
    prism_triples,
)
from diagnose_stage32_21ak_affine_2adic_membership import reconstruct_translation_data
from direct_picard_reynolds_lattice_diagnostic import csha, load_retained

EXPECTED_PREFIX_LOCK_SHA256 = "43a102214f3830652b95e749da20ff0418b5534973d70749401e360898ece56b"
EXPECTED_PREFIX_CANONICAL_SHA256 = "cc17cb1405095d7f9d855a21043388f4830ba611d69dc22af15b88c75287ef0c"
PREFIX_COUNT = 2709
PREFIX_FEASIBLE_R51_INDICES = 104607
SCHEMA = "STAGE32_21BA_R51_INTERVAL_SUFFIX_RESUME_V1"


def load_prefix(path: Path) -> dict:
    raw = json.loads(path.read_text())
    claimed = raw.pop("canonical_sha256_without_this_field")
    if claimed != EXPECTED_PREFIX_LOCK_SHA256 or csha(raw) != claimed:
        raise ValueError("21ba prefix source-lock canonical regression")
    if raw.get("source_canonical_sha256") != EXPECTED_PREFIX_CANONICAL_SHA256:
        raise ValueError("21ba prefix source canonical regression")
    if int(raw.get("processed_prefix_triples", -1)) != PREFIX_COUNT:
        raise ValueError("21ba prefix coverage regression")
    return raw


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-lock", type=Path, required=True)
    ap.add_argument("--prefix-lock", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--wall-seconds", type=int, default=390)
    ap.add_argument("--per-check-timeout-ms", type=int, default=1000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    started = time.monotonic()
    deadline = started + args.wall_seconds
    source = load_source_lock(args.source_lock)
    prefix = load_prefix(args.prefix_lock)
    target = source["target"]
    z = tuple(int(v) for v in target["z"])

    bundle = load_retained(args.retained, "s32_21ba_resume_picard")
    marking = load_retained(args.marking, "s32_21ba_resume_marking")
    data = reconstruct_translation_data(marking, bundle)
    M = data["M"]
    pivots = tuple(int(v) for v in data["pivot_rows"])
    selected_M = M.extract(list(pivots), list(range(EXPECTED_RANK)))
    reduced_rows, Trow = selected_M.T.lll_transform()
    if reduced_rows != Trow * selected_M.T:
        raise ValueError("LLL transform reconstruction regression")
    U = Trow.T
    if abs(int(U.det())) != 1:
        raise ValueError("LLL transform is not unimodular")
    Mred = M * U
    selected_red = selected_M * U
    if csha(matrix_payload(Mred)) != EXPECTED_MATRIX_SHA256:
        raise ValueError("reduced matrix regression")
    if csha(matrix_payload(U)) != EXPECTED_U_SHA256:
        raise ValueError("unimodular transform regression")

    y0 = data["pairing_x0_map"] * Matrix(z)
    curve_to_orbit: dict[int, int] = {}
    orbit_totals: list[int] = []
    for oid, orbit in enumerate(data["orbits"]):
        total0 = sum(int(y0[int(i), 0]) for i in orbit)
        orbit_totals.append(total0)
        for idx in orbit:
            curve_to_orbit[int(idx)] = oid
    if orbit_totals != [72, 76, 64, 168, 124, 88, 88, 176, 1080, 268, 10, 100, 104, 52]:
        raise ValueError("orbit totals regression")

    bounds = derive_initial_bounds(selected_red, pivots, y0, orbit_totals, curve_to_orbit)
    rvars = [Real(f"r_{j}") for j in range(EXPECTED_RANK)]
    solver = SolverFor("QF_LRA")
    solver.set(timeout=args.per_check_timeout_ms)
    for i in range(EXPECTED_PAIRINGS):
        expr = int(y0[i, 0]) + sum(int(Mred[i, j]) * rvars[j] for j in range(EXPECTED_RANK))
        total = orbit_totals[curve_to_orbit[i]]
        solver.add(expr >= 0, expr <= total)
    for j, (lo, hi) in enumerate(bounds):
        solver.add(rvars[j] >= lo, rvars[j] <= hi)
    solver.add(rvars[11] >= -1426)
    solver.add(rvars[51] >= R51_GLOBAL_LO, rvars[51] <= R51_GLOBAL_HI)

    triples = list(prism_triples())
    if len(triples) != EXPECTED_TRIPLES:
        raise ValueError("prism coverage regression")
    if list(triples[PREFIX_COUNT - 1]) != prefix["last_processed_triple"]:
        raise ValueError("prefix last-triple partition regression")
    if list(triples[PREFIX_COUNT]) != prefix["next_unprocessed_triple"]:
        raise ValueError("suffix first-triple partition regression")
    suffix = triples[PREFIX_COUNT:]
    if len(suffix) != int(prefix["remaining_triples"]):
        raise ValueError("suffix count regression")

    interval_records: list[list[int]] = []
    integer_empty: list[list[int]] = []
    unknown_records: list[dict] = []
    replay_unsat: list[list[int]] = []
    processed = 0
    checks = 0
    feasible_indices = 0
    stopped_by_wall = False

    for r50, r55, r27 in suffix:
        if time.monotonic() >= deadline:
            stopped_by_wall = True
            break
        solver.push()
        solver.add(rvars[50] == r50, rvars[55] == r55, rvars[27] == r27)
        try:
            result = integer_interval(solver, rvars[51], R51_GLOBAL_LO, R51_GLOBAL_HI)
        finally:
            solver.pop()
        processed += 1
        checks += int(result["checks"])
        triple = [r50, r55, r27]
        status = result["status"]
        if status == "INTERVAL":
            lo, hi = int(result["lo"]), int(result["hi"])
            interval_records.append([r50, r55, r27, lo, hi])
            feasible_indices += hi - lo + 1
        elif status == "INTEGER_EMPTY":
            integer_empty.append(triple)
        elif status == "UNKNOWN":
            unknown_records.append({"triple": triple, **result})
        elif status == "SOURCE_REPLAY_UNSAT":
            replay_unsat.append(triple)
        else:
            raise RuntimeError(status)
        if processed % 100 == 0:
            print(json.dumps({"suffix_processed": processed, "intervals": len(interval_records), "empty": len(integer_empty), "unknown": len(unknown_records), "checks": checks}), flush=True)

    suffix_expected = len(suffix)
    complete_suffix = processed == suffix_expected
    if replay_unsat:
        status = "SOURCE_REPLAY_REGRESSION"
    elif not complete_suffix:
        status = "PARTIAL_SUFFIX_RESOURCE_WALL"
    elif unknown_records:
        status = "COMPLETE_SUFFIX_WITH_QFLRA_UNKNOWN"
    else:
        status = "COMPLETE_COMBINED_R51_INTERVAL_CENSUS"

    suffix_baseline = processed * (R51_GLOBAL_HI - R51_GLOBAL_LO + 1)
    suffix_pruned = suffix_baseline - feasible_indices
    combined_processed = PREFIX_COUNT + processed
    combined_feasible = PREFIX_FEASIBLE_R51_INDICES + feasible_indices
    combined_baseline = combined_processed * (R51_GLOBAL_HI - R51_GLOBAL_LO + 1)
    combined_pruned = combined_baseline - combined_feasible
    suffix_stream_sha = csha(interval_records)
    combined_manifest_sha = csha([prefix["interval_stream_sha256"], suffix_stream_sha])

    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "leaf": "32-21ba-resume",
        "mode": "EXACT_SUFFIX_RESUME_FOR_PER_TRIPLE_QF_LRA_R51_INTEGER_INTERVALS",
        "source_21az_lock_sha256": EXPECTED_SOURCE_LOCK_SHA256,
        "source_21ba_prefix_lock_sha256": EXPECTED_PREFIX_LOCK_SHA256,
        "target": target,
        "partition": {
            "full_expected_triples": EXPECTED_TRIPLES,
            "prefix_triples": PREFIX_COUNT,
            "suffix_expected_triples": suffix_expected,
            "suffix_processed_triples": processed,
            "combined_processed_triples": combined_processed,
            "complete_suffix": complete_suffix,
            "complete_full_partition": combined_processed == EXPECTED_TRIPLES,
            "suffix_first_triple": list(suffix[0]),
            "suffix_last_triple": list(suffix[-1]),
            "stopped_by_wall": stopped_by_wall,
        },
        "result": {
            "status": status,
            "suffix_interval_record_count": len(interval_records),
            "suffix_integer_empty_triple_count": len(integer_empty),
            "suffix_qflra_unknown_triple_count": len(unknown_records),
            "suffix_source_replay_unsat_count": len(replay_unsat),
            "suffix_exact_qf_lra_checks": checks,
            "suffix_baseline_integer_r51_indices_for_processed": suffix_baseline,
            "suffix_rationally_feasible_integer_r51_indices": feasible_indices,
            "suffix_exact_rationally_pruned_integer_r51_indices": suffix_pruned,
            "combined_baseline_integer_r51_indices_for_processed": combined_baseline,
            "combined_rationally_feasible_integer_r51_indices": combined_feasible,
            "combined_exact_rationally_pruned_integer_r51_indices": combined_pruned,
            "prefix_interval_stream_sha256": prefix["interval_stream_sha256"],
            "suffix_interval_stream_sha256": suffix_stream_sha,
            "combined_two_stream_manifest_sha256": combined_manifest_sha,
            "suffix_interval_records": interval_records,
            "suffix_integer_empty_triples": integer_empty,
            "suffix_qflra_unknown_triples": unknown_records,
            "suffix_source_replay_unsat_triples": replay_unsat,
        },
        "interpretation": {
            "partition_is_disjoint_and_complete_if_suffix_complete": True,
            "surviving_r51_integer_index_is_not_integer_sat": True,
            "qflra_unknown_is_not_unsat": True,
            "fixed_projection_unsat_is_not_slice_unsat": True,
            "representative_sample_only": True,
            "not_full178_numerical_credit": True,
        },
        "safety": {
            "heavy_run_key_used": False,
            "full178_production_run": False,
            "integer_solver_used": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": status, "canonical": payload["canonical_sha256_without_this_field"], "suffix_processed": processed, "suffix_feasible_indices": feasible_indices, "combined_feasible_indices": combined_feasible, "combined_pruned_indices": combined_pruned, "elapsed_seconds": round(time.monotonic() - started, 3)}), flush=True)


if __name__ == "__main__":
    main()
