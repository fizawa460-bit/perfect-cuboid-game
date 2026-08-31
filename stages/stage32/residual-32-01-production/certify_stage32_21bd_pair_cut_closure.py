#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from sympy import Matrix
from z3 import And, Or, Real, SolverFor, get_version_string, sat, unknown, unsat

from certify_stage32_21bc_pair_combination_projection import (
    CANDIDATE_BOUNDS,
    CANDIDATES,
    EXPECTED_MATRIX_SHA256,
    EXPECTED_PAIRINGS,
    EXPECTED_RANK,
    EXPECTED_U_SHA256,
    derive_initial_bounds,
    load_21bb,
    matrix_payload,
    project_integer_valid_range,
)
from diagnose_stage32_21ak_affine_2adic_membership import reconstruct_translation_data
from direct_picard_reynolds_lattice_diagnostic import csha, load_retained

EXPECTED_21BC_LOCK_SHA256 = "5b4f91a0c8cd3d3025abfeb4e169382aa79a9148f8121df5378fe1195cf54fac"
EXPECTED_21BC_SOURCE_CANONICAL = "569c3ded01f04056d5ec73b4eb48bd5b94d25533ad66b22d0caedadd8f1c1e8f"
SCHEMA = "STAGE32_21BD_EXACT_ALL_PAIR_CUT_CLOSURE_V1"
TARGET = {"row_id": "g1-d186", "e": 266, "a": 592, "u": -44, "v": 32, "z": [-15, 62, -44, 26, 32]}


def load_pair_lock(path: Path) -> dict:
    raw = json.loads(path.read_text())
    claimed = raw.pop("canonical_sha256_without_this_field")
    if claimed != EXPECTED_21BC_LOCK_SHA256 or csha(raw) != claimed:
        raise ValueError("21bc pair-bound lock canonical regression")
    if raw.get("source_canonical_sha256") != EXPECTED_21BC_SOURCE_CANONICAL:
        raise ValueError("21bc source canonical regression")
    if raw.get("resolved_combination_count") != 42 or raw.get("qflra_unknown_count") != 0:
        raise ValueError("21bc bound completeness regression")
    return raw


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--formula-lock", type=Path, required=True)
    ap.add_argument("--pair-lock", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--per-check-timeout-ms", type=int, default=3000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    load_21bb(args.formula_lock)
    pair_lock = load_pair_lock(args.pair_lock)
    z = tuple(TARGET["z"])

    bundle = load_retained(args.retained, "s32_21bd_picard")
    marking = load_retained(args.marking, "s32_21bd_marking")
    data = reconstruct_translation_data(marking, bundle)
    M = data["M"]
    pivots = tuple(int(v) for v in data["pivot_rows"])
    selected_M = M.extract(list(pivots), list(range(EXPECTED_RANK)))
    reduced_rows, Trow = selected_M.T.lll_transform()
    if reduced_rows != Trow * selected_M.T:
        raise ValueError("LLL transform reconstruction regression")
    U = Trow.T
    if abs(int(U.det())) != 1:
        raise ValueError("LLL transform not unimodular")
    Mred = M * U
    selected_red = selected_M * U
    if csha(matrix_payload(Mred)) != EXPECTED_MATRIX_SHA256 or csha(matrix_payload(U)) != EXPECTED_U_SHA256:
        raise ValueError("reduced lattice regression")

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
    r = [Real(f"r_{j}") for j in range(EXPECTED_RANK)]
    solver = SolverFor("QF_LRA")
    solver.set(timeout=args.per_check_timeout_ms)
    for row in range(EXPECTED_PAIRINGS):
        expr = int(y0[row, 0]) + sum(int(Mred[row, j]) * r[j] for j in range(EXPECTED_RANK))
        total = orbit_totals[curve_to_orbit[row]]
        solver.add(expr >= 0, expr <= total)
    for j, (lo, hi) in enumerate(bounds):
        solver.add(r[j] >= lo, r[j] <= hi)
    solver.add(r[11] >= -1426)
    solver.add(r[50] >= 69, r[50] <= 79, r[55] >= -60, r[55] <= -50, r[55] <= r[50] - 129, r[27] >= -96, r[27] <= -48)
    d = r[50] - r[55]
    solver.add(r[51] <= -132)
    solver.add(Or(
        And(d >= 129, d <= 132, r[51] >= -176, r[51] >= r[27] - 103),
        And(d >= 133, d <= 136, r[51] >= -177, r[51] >= r[27] - 103),
        And(d >= 137, d <= 139, r[51] >= -178, r[51] >= r[27] - 103),
    ))
    for j, (lo, hi) in CANDIDATE_BOUNDS.items():
        solver.add(r[j] >= lo, r[j] <= hi)

    for item in pair_lock["bounds"]:
        i, j, sign, lo, hi = map(int, item)
        expr = r[i] + sign * r[j]
        solver.add(expr >= lo, expr <= hi)

    base = solver.check()
    base_reason = solver.reason_unknown() if base == unknown else None
    if base == unknown:
        status = "BASE_QFLRA_UNKNOWN"
        projections = []
        chosen = None
    elif base == unsat:
        status = "EXACT_FIXED_PROJECTION_UNSAT_BY_INTEGER_VALID_CUT_CLOSURE"
        projections = []
        chosen = None
    elif base == sat:
        projections = []
        for j in CANDIDATES:
            lo, hi = CANDIDATE_BOUNDS[j]
            out = project_integer_valid_range(solver, r[j], lo, hi)
            item = {"coordinate": j, "initial_bound": [lo, hi], "initial_domain_size": hi - lo + 1, **out}
            if out["status"] == "RESOLVED":
                item["domain_reduction"] = item["initial_domain_size"] - out["domain_size"]
            projections.append(item)
            print(json.dumps(item), flush=True)
        resolved = [x for x in projections if x["status"] == "RESOLVED"]
        chosen = min(resolved, key=lambda x: (x["domain_size"], -x["domain_reduction"], x["coordinate"])) if resolved else None
        status = "OPEN_AFTER_ALL_42_PAIR_CUTS"
    else:
        raise RuntimeError(base)

    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "leaf": "32-21bd",
        "mode": "EXACT_SIMULTANEOUS_CLOSURE_OF_42_INTEGER_VALID_PAIR_BOUNDS_PLUS_SINGLE_COORDINATE_REPROJECTION",
        "source_21bc_lock_sha256": EXPECTED_21BC_LOCK_SHA256,
        "z3_version": get_version_string(),
        "per_check_timeout_ms": args.per_check_timeout_ms,
        "base_status": str(base),
        "base_reason_unknown": base_reason,
        "result_status": status,
        "projection_results": projections,
        "chosen": chosen,
        "interpretation": {
            "all_42_pair_bounds_added_simultaneously": True,
            "base_unsat_would_be_exact_fixed_projection_unsat": True,
            "fixed_projection_unsat_is_not_slice_unsat": True,
            "qflra_unknown_is_not_unsat": True,
            "representative_sample_only": True,
            "not_full178_numerical_credit": True
        },
        "safety": {
            "heavy_run_key_used": False,
            "full178_production_run": False,
            "integer_solver_used": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False
        }
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": status, "canonical": payload["canonical_sha256_without_this_field"], "chosen": chosen}), flush=True)


if __name__ == "__main__":
    main()
