#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

import ortools
from ortools.sat.python import cp_model
from sympy import Matrix

from certify_stage32_21au_narrow_coordinate_split import build_problem
from direct_picard_reynolds_lattice_diagnostic import csha

EXPECTED_21AU_CANONICAL_SHA256 = "784ce9096441db1ba593a85731bc3094683871788cf6d075bb30682f0ddbe8c6"
EXPECTED_ORTOOLS_VERSION = "9.15.6755"
SCHEMA = "STAGE32_21AV_CP_SAT_EXACT_WITNESS_HUNT_V1"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--frontier", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--time-limit-seconds", type=float, default=300.0)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    if ortools.__version__ != EXPECTED_ORTOOLS_VERSION:
        raise ValueError(f"OR-Tools version regression: {ortools.__version__}")

    target, data, M, Mred, U, y0, curve_to_orbit, orbit_totals, bounds, split_j = build_problem(
        args.frontier, args.retained, args.marking
    )

    model = cp_model.CpModel()
    rvars = [model.new_int_var(lo, hi, f"r_{j}") for j, (lo, hi) in enumerate(bounds)]
    yexprs = []
    for i in range(Mred.rows):
        expr = int(y0[i, 0]) + sum(int(Mred[i, j]) * rvars[j] for j in range(Mred.cols))
        oid = curve_to_orbit[i]
        model.add(expr >= 0)
        model.add(expr <= orbit_totals[oid])
        yexprs.append(expr)
    for oid, orbit in enumerate(data["orbits"]):
        model.add(sum(yexprs[int(i)] for i in orbit) == orbit_totals[oid])

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = args.time_limit_seconds
    solver.parameters.num_search_workers = 4
    solver.parameters.random_seed = 32
    solver.parameters.log_search_progress = False
    status_code = solver.solve(model)

    status_name = solver.status_name(status_code)
    exact_sat = False
    reduced_witness = None
    t_witness = None
    pairings = None
    if status_code in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        reduced_witness = tuple(int(solver.value(v)) for v in rvars)
        for j, (lo, hi) in enumerate(bounds):
            if not (lo <= reduced_witness[j] <= hi):
                raise ValueError("21av CP-SAT witness violates exact reduced bound")
        tvec = U * Matrix(reduced_witness)
        t_witness = tuple(int(v) for v in tvec)
        exact = y0 + M * Matrix(t_witness)
        pairings = tuple(int(exact[i, 0]) for i in range(M.rows))
        if min(pairings) < 0:
            raise ValueError("21av candidate failed exact all140 nonnegativity")
        for oid, orbit in enumerate(data["orbits"]):
            if sum(pairings[int(i)] for i in orbit) != orbit_totals[oid]:
                raise ValueError("21av candidate failed exact orbit-total reconstruction")
        exact_red = y0 + Mred * Matrix(reduced_witness)
        if tuple(int(exact_red[i, 0]) for i in range(M.rows)) != pairings:
            raise ValueError("21av reduced/original exact reconstruction mismatch")
        exact_sat = True

    if exact_sat:
        promoted_status = "SAT_EXACTLY_RECHECKED"
        combined_sat, combined_unsat, combined_unknown = 1, 55, 0
    else:
        # CP-SAT is used only as a witness finder here. INFEASIBLE/UNKNOWN is not
        # promoted to exact UNSAT and leaves the original fixed projection unresolved.
        promoted_status = "NO_EXACT_SAT_WITNESS_FOUND"
        combined_sat, combined_unsat, combined_unknown = 0, 55, 1

    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "leaf": "32-21av",
        "mode": "SPECIALIZED_CP_SAT_WITNESS_HUNT_WITH_MANDATORY_EXACT_ORIGINAL_Z59_RECHECK",
        "source_21au_canonical_sha256": EXPECTED_21AU_CANONICAL_SHA256,
        "ortools_version": ortools.__version__,
        "settings": {
            "time_limit_seconds": args.time_limit_seconds,
            "num_search_workers": 4,
            "random_seed": 32,
            "cp_sat_unsat_credit_allowed": False,
            "only_exactly_rechecked_sat_may_be_promoted": True,
        },
        "target": {
            "row_id": target["row_id"], "e": int(target["e"]), "a": int(target["a"]),
            "u": int(target["u"]), "v": int(target["v"]), "z": list(target["z"]),
        },
        "solver_result": {
            "raw_status": status_name,
            "promoted_status": promoted_status,
            "wall_time_seconds": solver.wall_time,
            "num_conflicts": solver.num_conflicts,
            "num_branches": solver.num_branches,
            "exact_sat_witness_rechecked": exact_sat,
            "combined_representative_sample_sat": combined_sat,
            "combined_representative_sample_unsat": combined_unsat,
            "combined_representative_sample_unknown": combined_unknown,
            "reduced_coordinate_witness_sha256": csha(list(reduced_witness)) if reduced_witness is not None else None,
            "translation_witness_sha256": csha(list(t_witness)) if t_witness is not None else None,
            "all140_pairings_sha256": csha(list(pairings)) if pairings is not None else None,
            "all140_pairing_minimum": min(pairings) if pairings is not None else None,
            "all140_pairing_maximum": max(pairings) if pairings is not None else None,
        },
        "interpretation": {
            "sat_witness_is_exact_for_this_fixed_projection_only_after_recheck": True,
            "cp_sat_infeasible_is_not_exact_unsat_credit": True,
            "cp_sat_unknown_is_not_unsat": True,
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
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"raw_status": status_name, "promoted_status": promoted_status, "canonical": payload["canonical_sha256_without_this_field"]}))


if __name__ == "__main__":
    main()
