#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import multiprocessing as mp
import time
import traceback
from pathlib import Path

import islpy as isl
from sympy import Matrix

from diagnose_stage32_21ak_affine_2adic_membership import reconstruct_translation_data
from direct_picard_reynolds_lattice_diagnostic import csha, load_retained

EXPECTED_FRONTIER_SHA256 = "4b5698b9795229efd894bc4e35cb8a78d8b57fdd4560880e3fcc416b4aeabd3a"
EXPECTED_21AP_CANONICAL_SHA256 = "fc1ea72a88a6e4486bfa07a1c2489a4a38649df2cb8859781db8c83a706ac9ff"
EXPECTED_RANK = 59
EXPECTED_PAIRINGS = 140
SCHEMA = "STAGE32_21AW_ISL_EXACT_INTEGER_FIBER_V1"


def load_frontier(path: Path) -> dict:
    raw = json.loads(path.read_text())
    claimed = raw.pop("canonical_sha256_without_this_field")
    if claimed != EXPECTED_FRONTIER_SHA256 or csha(raw) != claimed:
        raise ValueError("21ap frontier canonical regression")
    if raw.get("source_canonical_sha256") != EXPECTED_21AP_CANONICAL_SHA256:
        raise ValueError("21ap source canonical regression")
    if len(raw.get("frontier", [])) != 1:
        raise ValueError("21aw expects exactly one source-locked UNKNOWN")
    return raw


def matrix_payload(m: Matrix) -> list[list[int]]:
    return [[int(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]


def affine_text(constant: int, coeffs: list[int], names: list[str]) -> str:
    parts = [str(int(constant))]
    for coeff, name in zip(coeffs, names):
        c = int(coeff)
        if c == 0:
            continue
        if c > 0:
            parts.append(f"+ {c}*{name}")
        else:
            parts.append(f"- {abs(c)}*{name}")
    return " ".join(parts)


def exact_worker(frontier_path: str, retained_path: str, marking_path: str) -> dict:
    frontier = load_frontier(Path(frontier_path))
    target = frontier["frontier"][0]
    z = tuple(int(v) for v in target["z"])
    orbit_totals_expected = tuple(int(v) for v in target["orbit_totals"])

    bundle = load_retained(Path(retained_path), "s32_21aw_picard")
    marking = load_retained(Path(marking_path), "s32_21aw_marking")
    data = reconstruct_translation_data(marking, bundle)

    M = data["M"]
    if M.shape != (EXPECTED_PAIRINGS, EXPECTED_RANK):
        raise ValueError(f"translation pairing shape regression: {M.shape}")
    y0 = data["pairing_x0_map"] * Matrix(z)
    if y0.shape != (EXPECTED_PAIRINGS, 1):
        raise ValueError("affine pairing origin shape regression")

    curve_to_orbit: dict[int, int] = {}
    orbit_totals: list[int] = []
    for oid, orbit in enumerate(data["orbits"]):
        total0 = sum(int(y0[int(i), 0]) for i in orbit)
        for j in range(EXPECTED_RANK):
            if sum(int(M[int(i), j]) for i in orbit) != 0:
                raise ValueError(f"orbit {oid} translation-sum regression")
        orbit_totals.append(total0)
        for idx in orbit:
            curve_to_orbit[int(idx)] = oid
    if len(curve_to_orbit) != EXPECTED_PAIRINGS:
        raise ValueError("orbit coverage regression")
    if tuple(orbit_totals) != orbit_totals_expected:
        raise ValueError(f"source-locked orbit totals regression: {orbit_totals}")

    names = [f"t{j}" for j in range(EXPECTED_RANK)]
    constraints: list[str] = []
    for i in range(EXPECTED_PAIRINGS):
        coeffs = [int(M[i, j]) for j in range(EXPECTED_RANK)]
        expr = affine_text(int(y0[i, 0]), coeffs, names)
        total = orbit_totals[curve_to_orbit[i]]
        constraints.append(f"({expr}) >= 0")
        constraints.append(f"({expr}) <= {total}")
    set_text = "{ [" + ", ".join(names) + "] : " + " and ".join(constraints) + " }"
    problem_sha = hashlib.sha256(set_text.encode()).hexdigest()

    ctx = isl.Context()
    start = time.perf_counter()
    integer_set = isl.Set.read_from_str(ctx, set_text)
    integer_set = integer_set.coalesce()
    empty = bool(integer_set.is_empty())
    solve_seconds = time.perf_counter() - start

    t_witness = None
    pairings = None
    if empty:
        status = "UNSAT"
    else:
        status = "SAT"
        point = integer_set.sample_point()
        t_witness = tuple(
            int(point.get_coordinate_val(isl.dim_type.set, j).to_python())
            for j in range(EXPECTED_RANK)
        )
        exact = y0 + M * Matrix(t_witness)
        pairings = tuple(int(exact[i, 0]) for i in range(EXPECTED_PAIRINGS))
        if min(pairings) < 0:
            raise ValueError("ISL sample point has negative original pairing")
        for oid, orbit in enumerate(data["orbits"]):
            if sum(pairings[int(i)] for i in orbit) != orbit_totals[oid]:
                raise ValueError("ISL sample point orbit-total regression")

    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "leaf": "32-21aw",
        "mode": "EXACT_ISL_PRESBURGER_INTEGER_SET_ON_ORIGINAL_Z59_TRANSLATION_LATTICE",
        "source_frontier_sha256": EXPECTED_FRONTIER_SHA256,
        "source_21ap_canonical_sha256": EXPECTED_21AP_CANONICAL_SHA256,
        "islpy_version": getattr(isl, "__version__", "2026.2.1"),
        "target": {
            "row_id": target["row_id"],
            "e": int(target["e"]),
            "a": int(target["a"]),
            "u": int(target["u"]),
            "v": int(target["v"]),
            "z": list(z),
        },
        "exact_problem": {
            "integer_rank": EXPECTED_RANK,
            "pairing_count": EXPECTED_PAIRINGS,
            "inequality_count": 2 * EXPECTED_PAIRINGS,
            "translation_pairing_sha256": csha(matrix_payload(M)),
            "problem_text_sha256": problem_sha,
            "orbit_totals": orbit_totals,
            "original_Z59_lattice_used_directly": True,
            "floating_point_relaxation_used": False,
        },
        "result": {
            "status": status,
            "solve_wall_seconds": solve_seconds,
            "combined_representative_sample_sat": 1 if status == "SAT" else 0,
            "combined_representative_sample_unsat": 55 + (1 if status == "UNSAT" else 0),
            "combined_representative_sample_unknown": 0,
            "translation_witness_sha256": csha(list(t_witness)) if t_witness is not None else None,
            "all140_pairings_sha256": csha(list(pairings)) if pairings is not None else None,
            "all140_pairing_minimum": min(pairings) if pairings is not None else None,
            "all140_pairing_maximum": max(pairings) if pairings is not None else None,
        },
        "interpretation": {
            "unsat_closes_the_complete_56_fixed_projection_representative_sample": status == "UNSAT",
            "sat_is_an_exact_original_t_Z59_lift_for_this_fixed_projection": status == "SAT",
            "fixed_projection_unsat_is_not_slice_unsat": True,
            "representative_sample_only": True,
            "not_full178_numerical_credit": True,
        },
        "safety": {
            "heavy_run_key_used": False,
            "full178_production_run": False,
            "legacy_prefix_dfs_run": False,
            "59d_cvp_run": False,
            "terminal_family_materialization_run": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    return payload


def child_entry(queue, frontier_path: str, retained_path: str, marking_path: str) -> None:
    try:
        queue.put(("ok", exact_worker(frontier_path, retained_path, marking_path)))
    except Exception:
        queue.put(("error", traceback.format_exc()))


def timeout_payload(frontier_path: Path, wall_timeout_seconds: int) -> dict:
    frontier = load_frontier(frontier_path)
    target = frontier["frontier"][0]
    return {
        "schema": SCHEMA,
        "stage": 32,
        "leaf": "32-21aw",
        "mode": "EXACT_ISL_PRESBURGER_INTEGER_SET_ON_ORIGINAL_Z59_TRANSLATION_LATTICE",
        "source_frontier_sha256": EXPECTED_FRONTIER_SHA256,
        "source_21ap_canonical_sha256": EXPECTED_21AP_CANONICAL_SHA256,
        "islpy_version": getattr(isl, "__version__", "2026.2.1"),
        "target": {
            "row_id": target["row_id"],
            "e": int(target["e"]),
            "a": int(target["a"]),
            "u": int(target["u"]),
            "v": int(target["v"]),
            "z": [int(v) for v in target["z"]],
        },
        "result": {
            "status": "UNKNOWN_RESOURCE_WALL",
            "wall_timeout_seconds": wall_timeout_seconds,
            "combined_representative_sample_sat": 0,
            "combined_representative_sample_unsat": 55,
            "combined_representative_sample_unknown": 1,
        },
        "interpretation": {
            "resource_wall_is_not_unsat": True,
            "fixed_projection_unsat_is_not_slice_unsat": True,
            "representative_sample_only": True,
            "not_full178_numerical_credit": True,
        },
        "safety": {
            "heavy_run_key_used": False,
            "full178_production_run": False,
            "legacy_prefix_dfs_run": False,
            "59d_cvp_run": False,
            "terminal_family_materialization_run": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--frontier", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--wall-timeout-seconds", type=int, default=300)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    ctx = mp.get_context("spawn")
    queue = ctx.Queue()
    proc = ctx.Process(
        target=child_entry,
        args=(queue, str(args.frontier), str(args.retained), str(args.marking)),
    )
    proc.start()
    proc.join(args.wall_timeout_seconds)
    if proc.is_alive():
        proc.terminate()
        proc.join(10)
        payload = timeout_payload(args.frontier, args.wall_timeout_seconds)
    else:
        if queue.empty():
            raise RuntimeError(f"21aw worker exited {proc.exitcode} without result")
        kind, value = queue.get()
        if kind != "ok":
            raise RuntimeError(f"21aw worker failed:\n{value}")
        payload = value

    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": payload["result"]["status"],
        "canonical": payload["canonical_sha256_without_this_field"],
    }))


if __name__ == "__main__":
    main()
