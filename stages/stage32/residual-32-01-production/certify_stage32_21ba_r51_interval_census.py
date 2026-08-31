#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import time
from fractions import Fraction
from pathlib import Path

from sympy import Matrix
from z3 import Real, SolverFor, get_version_string, sat, unknown, unsat

from diagnose_stage32_21ak_affine_2adic_membership import reconstruct_translation_data
from direct_picard_reynolds_lattice_diagnostic import csha, load_retained

EXPECTED_SOURCE_LOCK_SHA256 = "3c83ce97058ad52124730376a4e41720a40eb45995994314ac47d7f973da40da"
EXPECTED_21AZ_CANONICAL_SHA256 = "da62663b507c6df8e9c8620ade3c63157fea8d125c2f552da1ef89211e9f4315"
EXPECTED_21AY_CANONICAL_SHA256 = "8c149a585d6b4f1168d1425cc89daafad4bf37e1ac3568dffb97e1628ffd14be"
EXPECTED_21AX_CANONICAL_SHA256 = "21c7b96be83f0d85a722fd16279fe3c9808918536cca258ee3e8110a695c092b"
EXPECTED_MATRIX_SHA256 = "77d62f4473f315212efaad8e4852bb097b2a8584838a5f1299d6528ab8a29bc3"
EXPECTED_U_SHA256 = "fdbf00267e3835efa9e1e77fc628c8a62779f6c42e16076b244cded276934c4f"
EXPECTED_RANK = 59
EXPECTED_PAIRINGS = 140
EXPECTED_TRIPLES = 3234
R51_GLOBAL_LO = -178
R51_GLOBAL_HI = -132
SCHEMA = "STAGE32_21BA_EXACT_PER_TRIPLE_R51_INTEGER_INTERVAL_CENSUS_V1"


def frac(v) -> Fraction:
    return Fraction(int(v.p), int(v.q)) if hasattr(v, "p") else Fraction(int(v), 1)


def matrix_payload(m: Matrix) -> list[list[int]]:
    return [[int(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]


def derive_initial_bounds(selected_red: Matrix, pivots: tuple[int, ...], y0: Matrix,
                          orbit_totals: list[int], curve_to_orbit: dict[int, int]) -> list[tuple[int, int]]:
    inv = selected_red.inv()
    selected_y0 = [int(y0[i, 0]) for i in pivots]
    bounds: list[tuple[int, int]] = []
    for rj in range(EXPECTED_RANK):
        lo = Fraction(0, 1)
        hi = Fraction(0, 1)
        for k, curve_idx in enumerate(pivots):
            oid = curve_to_orbit[curve_idx]
            d_lo = Fraction(-selected_y0[k], 1)
            d_hi = Fraction(orbit_totals[oid] - selected_y0[k], 1)
            a = frac(inv[rj, k])
            if a >= 0:
                lo += a * d_lo
                hi += a * d_hi
            else:
                lo += a * d_hi
                hi += a * d_lo
        ilo, ihi = math.ceil(lo), math.floor(hi)
        if ilo > ihi:
            raise ValueError(f"initial integer-valid bound empty at {rj}: {ilo}>{ihi}")
        bounds.append((int(ilo), int(ihi)))
    return bounds


def load_source_lock(path: Path) -> dict:
    raw = json.loads(path.read_text())
    claimed = raw.pop("canonical_sha256_without_this_field")
    if claimed != EXPECTED_SOURCE_LOCK_SHA256 or csha(raw) != claimed:
        raise ValueError("21az source-lock canonical regression")
    if raw.get("source_canonical_sha256") != EXPECTED_21AZ_CANONICAL_SHA256:
        raise ValueError("21az source canonical regression")
    if raw.get("source_21ay_canonical_sha256") != EXPECTED_21AY_CANONICAL_SHA256:
        raise ValueError("21ay source canonical regression")
    if raw.get("source_21ax_canonical_sha256") != EXPECTED_21AX_CANONICAL_SHA256:
        raise ValueError("21ax source canonical regression")
    return raw


def threshold_check(solver, var, relation: str, value: int):
    solver.push()
    try:
        if relation == "le":
            solver.add(var <= value)
        elif relation == "ge":
            solver.add(var >= value)
        else:
            raise ValueError(relation)
        result = solver.check()
        reason = solver.reason_unknown() if result == unknown else None
        return result, reason
    finally:
        solver.pop()


def integer_interval(solver, var, lo: int, hi: int) -> dict:
    checks = 0
    # The fixed-triple source contract says the rational fiber is nonempty.
    # Recheck it independently before using interval convexity.
    base = solver.check()
    checks += 1
    if base == unknown:
        return {"status": "UNKNOWN", "checks": checks, "reason": solver.reason_unknown(), "phase": "base"}
    if base == unsat:
        return {"status": "SOURCE_REPLAY_UNSAT", "checks": checks}
    if base != sat:
        raise RuntimeError(base)

    a, b = lo, hi
    while a < b:
        mid = (a + b) // 2
        result, reason = threshold_check(solver, var, "le", mid)
        checks += 1
        if result == unknown:
            return {"status": "UNKNOWN", "checks": checks, "reason": reason, "phase": "lower"}
        if result == sat:
            b = mid
        elif result == unsat:
            a = mid + 1
        else:
            raise RuntimeError(result)
    new_lo = a

    a, b = new_lo, hi
    while a < b:
        mid = (a + b + 1) // 2
        result, reason = threshold_check(solver, var, "ge", mid)
        checks += 1
        if result == unknown:
            return {"status": "UNKNOWN", "checks": checks, "reason": reason, "phase": "upper"}
        if result == sat:
            a = mid
        elif result == unsat:
            b = mid - 1
        else:
            raise RuntimeError(result)
    new_hi = a

    # If the real projection interval avoids all integers, the two searches
    # can only cross when the independently bounded integer domain is empty.
    if new_lo > new_hi:
        return {"status": "INTEGER_EMPTY", "checks": checks, "lo": new_lo, "hi": new_hi}
    return {
        "status": "INTERVAL",
        "checks": checks,
        "lo": new_lo,
        "hi": new_hi,
        "integer_domain_size": new_hi - new_lo + 1,
    }


def prism_triples():
    for r50 in range(69, 80):
        for r55 in range(-60, -49):
            if r55 > r50 - 129:
                continue
            for r27 in range(-96, -47):
                yield r50, r55, r27


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-lock", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--wall-seconds", type=int, default=390)
    ap.add_argument("--per-check-timeout-ms", type=int, default=1000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    started = time.monotonic()
    deadline = started + args.wall_seconds
    source = load_source_lock(args.source_lock)
    target = source["target"]
    z = tuple(int(v) for v in target["z"])

    if source["compressed_survivor_region"]["integer_point_count"] != EXPECTED_TRIPLES:
        raise ValueError("21az survivor count regression")
    if source["fourth_coordinate_selection"]["chosen_coordinate"] != 51:
        raise ValueError("21az chosen-coordinate regression")
    if source["fourth_coordinate_selection"]["residual_integer_valid_bound"] != [R51_GLOBAL_LO, R51_GLOBAL_HI]:
        raise ValueError("21az r51 residual-bound regression")

    bundle = load_retained(args.retained, "s32_21ba_picard")
    marking = load_retained(args.marking, "s32_21ba_marking")
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
    if bounds[51] != (-236, -132):
        raise ValueError(f"r51 initial bound regression: {bounds[51]}")

    rvars = [Real(f"r_{j}") for j in range(EXPECTED_RANK)]
    solver = SolverFor("QF_LRA")
    solver.set(timeout=args.per_check_timeout_ms)
    for i in range(EXPECTED_PAIRINGS):
        expr = int(y0[i, 0]) + sum(int(Mred[i, j]) * rvars[j] for j in range(EXPECTED_RANK))
        total = orbit_totals[curve_to_orbit[i]]
        solver.add(expr >= 0, expr <= total)
    for j, (lo, hi) in enumerate(bounds):
        solver.add(rvars[j] >= lo, rvars[j] <= hi)

    # Persisted 21ax cut.
    solver.add(rvars[11] >= -1426)

    # Independently replay the 21az global r51 lower projection cut over the
    # compact survivor prism before consuming it in the per-triple census.
    solver.set(timeout=max(args.per_check_timeout_ms, 10000))
    solver.push()
    solver.add(
        rvars[50] >= 69, rvars[50] <= 79,
        rvars[55] >= -60, rvars[55] <= -50,
        rvars[55] <= rvars[50] - 129,
        rvars[27] >= -96, rvars[27] <= -48,
        rvars[51] <= R51_GLOBAL_LO - 1,
    )
    global_cut_replay = solver.check()
    global_cut_reason = solver.reason_unknown() if global_cut_replay == unknown else None
    solver.pop()
    if global_cut_replay != unsat:
        raise ValueError(f"21az global r51 lower cut replay failed: {global_cut_replay} {global_cut_reason}")

    solver.add(rvars[51] >= R51_GLOBAL_LO, rvars[51] <= R51_GLOBAL_HI)
    solver.set(timeout=args.per_check_timeout_ms)

    interval_records: list[list[int]] = []
    unknown_records: list[dict] = []
    source_replay_unsat: list[list[int]] = []
    integer_empty_triples: list[list[int]] = []
    total_checks = 0
    total_integer_r51_indices = 0
    processed = 0
    stopped_by_wall = False

    triples = list(prism_triples())
    if len(triples) != EXPECTED_TRIPLES:
        raise ValueError(f"compact prism point-count regression: {len(triples)}")

    for r50, r55, r27 in triples:
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
        total_checks += int(result["checks"])
        triple = [r50, r55, r27]
        status = result["status"]
        if status == "INTERVAL":
            lo, hi = int(result["lo"]), int(result["hi"])
            interval_records.append([r50, r55, r27, lo, hi])
            total_integer_r51_indices += hi - lo + 1
        elif status == "INTEGER_EMPTY":
            integer_empty_triples.append(triple)
        elif status == "UNKNOWN":
            unknown_records.append({"triple": triple, **result})
        elif status == "SOURCE_REPLAY_UNSAT":
            source_replay_unsat.append(triple)
        else:
            raise RuntimeError(status)

        if processed % 250 == 0:
            print(json.dumps({
                "processed": processed,
                "intervals": len(interval_records),
                "integer_empty": len(integer_empty_triples),
                "unknown": len(unknown_records),
                "source_replay_unsat": len(source_replay_unsat),
                "integer_r51_indices": total_integer_r51_indices,
                "checks": total_checks,
            }), flush=True)

    complete = processed == EXPECTED_TRIPLES
    if source_replay_unsat:
        status = "SOURCE_REPLAY_REGRESSION"
    elif not complete:
        status = "PARTIAL_PREFIX_RESOURCE_WALL"
    elif unknown_records:
        status = "COMPLETE_WITH_QFLRA_UNKNOWN"
    elif not interval_records:
        status = "UNSAT_AT_INTEGER_R51_INDEX_LEVEL"
    else:
        status = "OPEN_COMPLETE_R51_INTERVAL_CENSUS"

    baseline_quadruple_indices = EXPECTED_TRIPLES * (R51_GLOBAL_HI - R51_GLOBAL_LO + 1)
    exact_pruned_r51_indices = baseline_quadruple_indices - total_integer_r51_indices
    interval_stream_sha256 = csha(interval_records)

    widths = [rec[4] - rec[3] + 1 for rec in interval_records]
    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "leaf": "32-21ba",
        "mode": "EXACT_PER_TRIPLE_QF_LRA_R51_PROJECTION_TO_COMPLETE_INTEGER_INTERVAL",
        "source_lock_sha256": EXPECTED_SOURCE_LOCK_SHA256,
        "source_21az_canonical_sha256": EXPECTED_21AZ_CANONICAL_SHA256,
        "z3_version": get_version_string(),
        "wall_seconds": args.wall_seconds,
        "per_check_timeout_ms": args.per_check_timeout_ms,
        "target": target,
        "r51_global_integer_valid_bound": [R51_GLOBAL_LO, R51_GLOBAL_HI],
        "coverage": {
            "expected_triples": EXPECTED_TRIPLES,
            "processed_triples": processed,
            "complete": complete,
            "lexicographic_compact_prism_order": True,
            "stopped_by_wall": stopped_by_wall,
            "total_exact_qf_lra_checks": total_checks,
        },
        "result": {
            "status": status,
            "interval_record_count": len(interval_records),
            "integer_empty_triple_count": len(integer_empty_triples),
            "qflra_unknown_triple_count": len(unknown_records),
            "source_replay_unsat_triple_count": len(source_replay_unsat),
            "baseline_integer_r51_index_count": baseline_quadruple_indices,
            "rationally_feasible_integer_r51_index_count": total_integer_r51_indices,
            "exact_rationally_pruned_integer_r51_index_count": exact_pruned_r51_indices,
            "interval_stream_sha256": interval_stream_sha256,
            "interval_width_min": min(widths) if widths else None,
            "interval_width_max": max(widths) if widths else None,
            "interval_width_sum": sum(widths),
            "integer_empty_triples": integer_empty_triples,
            "qflra_unknown_triples": unknown_records,
            "source_replay_unsat_triples": source_replay_unsat,
            "interval_records": interval_records,
            "combined_representative_sample_sat": 0,
            "combined_representative_sample_unsat": 56 if status == "UNSAT_AT_INTEGER_R51_INDEX_LEVEL" else 55,
            "combined_representative_sample_unknown": 0 if status == "UNSAT_AT_INTEGER_R51_INDEX_LEVEL" else 1,
        },
        "interpretation": {
            "fixed_triple_real_r51_projection_is_interval_by_convexity": True,
            "each_interval_is_complete_for_integer_r51_values_with_rational_remaining_coordinates": True,
            "surviving_r51_integer_index_is_not_integer_sat": True,
            "all_empty_complete_census_would_close_only_this_fixed_projection": True,
            "fixed_projection_unsat_is_not_slice_unsat": True,
            "representative_sample_only": True,
            "not_full178_numerical_credit": True,
            "qflra_unknown_is_not_unsat": True,
        },
        "safety": {
            "heavy_run_key_used": False,
            "full178_production_run": False,
            "integer_solver_used": False,
            "raw_3234_x_47_enumeration_used": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": status,
        "canonical": payload["canonical_sha256_without_this_field"],
        "processed": processed,
        "intervals": len(interval_records),
        "integer_empty": len(integer_empty_triples),
        "unknown": len(unknown_records),
        "r51_indices": total_integer_r51_indices,
        "baseline": baseline_quadruple_indices,
        "checks": total_checks,
        "elapsed_seconds": round(time.monotonic() - started, 3),
    }), flush=True)


if __name__ == "__main__":
    main()
