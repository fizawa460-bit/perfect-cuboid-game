#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import time
from pathlib import Path

import numpy as np
import sympy
from scipy.optimize import Bounds, LinearConstraint, milp
from sympy import Matrix
from z3 import And, Int, Or, SolverFor, get_version_string, sat

import diagnose_stage32_post1473_integral_picard_support_reduced_lia_preflight as v5
from diagnose_stage32_post1473_integral_picard_support_preflight import (
    EXPECTED_21AK_CONSTRAINT_ROWS_SHA256,
    EXPECTED_ALL140_COUNT,
    EXPECTED_EXCEPTIONAL_COUNT,
    EXPECTED_NODE_SUPPORT_AUDIT_CANONICAL,
    EXPECTED_PICARD_ADAPTER_CANONICAL,
    EXPECTED_REQUIRED_EXCEPTIONAL_SUPPORT,
    EXPECTED_TARGET,
    load_canonical,
)

EXPECTED_V5_CANONICAL = "ceb88e2d9386293909689ac24a7573a8e1e6992d2467ec1e251dff4bd321f49a"
RANK = 59
CATEGORY_COUNT = 3


def add_row(rows, lower, upper, nvars: int, coeffs: dict[int, int]) -> None:
    row = np.zeros(nvars, dtype=np.float64)
    for idx, value in coeffs.items():
        row[idx] = float(value)
    rows.append((row, float(lower), float(upper)))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--node-preflight", type=Path, required=True)
    ap.add_argument("--picard-adapter", type=Path, required=True)
    ap.add_argument("--node-support-audit", type=Path, required=True)
    ap.add_argument("--source-lock", type=Path, required=True)
    ap.add_argument("--formula-lock", type=Path, required=True)
    ap.add_argument("--audit-lock", type=Path, required=True)
    ap.add_argument("--pair-lock", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--wall-seconds", type=int, default=60)
    ap.add_argument("--exact-replay-timeout-ms", type=int, default=30000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if args.wall_seconds <= 0 or args.exact_replay_timeout_ms <= 0:
        raise ValueError("timeouts must be positive")

    manifest = json.loads(args.manifest.read_text())
    claimed_manifest = manifest.pop("canonical_sha256_without_this_field")
    if v5.csha(manifest) != claimed_manifest or claimed_manifest != v5.EXPECTED_MANIFEST_SHA256:
        raise ValueError("FULL178 manifest canonical regression")
    node_preflight = v5.load_preflight(args.node_preflight)
    if node_preflight["canonical_sha256_without_this_field"] != v5.EXPECTED_PREFLIGHT_SHA256:
        raise ValueError("node-support preflight regression")
    adapter_evidence = load_canonical(
        args.picard_adapter, EXPECTED_PICARD_ADAPTER_CANONICAL, "post-21bl Picard adapter"
    )
    node_audit = load_canonical(
        args.node_support_audit, EXPECTED_NODE_SUPPORT_AUDIT_CANONICAL, "node-support fresh audit"
    )
    if node_audit["verdict"]["bijective_normalization_genus1_curve_in_representative_class"] is not False:
        raise ValueError("representative node-support exclusion audit regression")

    target = adapter_evidence["target"]
    for key, expected in EXPECTED_TARGET.items():
        if target.get(key) != expected:
            raise ValueError(f"representative target regression at {key}: {target.get(key)} != {expected}")
    required_support = v5.ceil_div(int(target["degree"]) - 16 * int(target["genus"]) + 16, 4)
    if required_support != EXPECTED_REQUIRED_EXCEPTIONAL_SUPPORT:
        raise ValueError("required exceptional support regression")

    source = v5.load_source_lock(args.source_lock)
    if source["compressed_survivor_region"]["integer_point_count"] != 3234:
        raise ValueError("21az prism population regression")
    if source["fourth_coordinate_selection"]["residual_integer_valid_bound"] != [v5.R51_GLOBAL_LO, v5.R51_GLOBAL_HI]:
        raise ValueError("21az r51 bound regression")
    v5.load_21be_lock(args.audit_lock)
    pair_lock = v5.load_pair_lock(args.pair_lock)
    formula_raw = json.loads(args.formula_lock.read_text())
    if formula_raw.get("canonical_sha256_without_this_field") != "370bc29433006c5a5ac0b8ee977212f0a274449ab85c736e62b3f5cbf7e51405":
        raise ValueError("21bb formula lock canonical regression")

    bundle = v5.load_module_payload(args.retained, "stage32_post1473_support_picard")
    marking = v5.load_module_payload(args.marking, "stage32_post1473_support_marking")
    picard_model = v5.ReynoldsRank2AntiFixedCosetBound.from_retained(marking, bundle)
    if picard_model.certificate["canonical_sha256_without_this_field"] != v5.EXPECTED_AC_CERTIFICATE_SHA256:
        raise ValueError("audited 32-21ac evaluator certificate regression")
    data = v5.reconstruct_translation_data(marking, bundle)
    if v5.csha(list(tuple(data["constraint_rows"]))) != EXPECTED_21AK_CONSTRAINT_ROWS_SHA256:
        raise ValueError("21ak affine constraint-row regression")

    z = tuple(int(v) for v in target["z"])
    Mred, U, y0, curve_to_orbit, orbit_totals, initial_bounds = v5.reduced_model(data, z)

    known_picard = Matrix([int(v) for v in adapter_evidence["reconstruction"]["picard_coordinates"]])
    x0 = data["x0_map"] * Matrix(z)
    known_t, params = data["K"].gauss_jordan_solve(known_picard - x0)
    if params.rows != 0 or any(sympy.denom(v) != 1 for v in known_t):
        raise ValueError("known Picard class lacks integral translation")
    known_t = Matrix([int(v) for v in known_t])
    known_r = U.inv() * known_t
    if any(sympy.denom(v) != 1 for v in known_r):
        raise ValueError("known reduced lift became nonintegral")
    known_r = Matrix([int(v) for v in known_r])
    known_pairings = tuple(int(v) for v in (y0 + Mred * known_r))
    if known_pairings != tuple(int(v) for v in adapter_evidence["all140"]["pairings"]):
        raise ValueError("known Picard reduced-coordinate replay regression")
    known_support = sum(1 for value in known_pairings[-EXPECTED_EXCEPTIONAL_COUNT:] if value > 0)
    if known_support != v5.EXPECTED_KNOWN_EXCEPTIONAL_SUPPORT:
        raise ValueError("known support regression")

    # Exact Z3 replay model. Numerical MILP below is never allowed to authorize UNSAT.
    r = [Int(f"r_{j}") for j in range(RANK)]
    exact = SolverFor("QF_LIA")
    exact.set(timeout=args.exact_replay_timeout_ms)
    pairing_exprs = []
    for row in range(EXPECTED_ALL140_COUNT):
        expr = int(y0[row, 0]) + sum(int(Mred[row, j]) * r[j] for j in range(RANK))
        pairing_exprs.append(expr)
        total = orbit_totals[curve_to_orbit[row]]
        exact.add(expr >= 0, expr <= total)
    for j, (lo, hi) in enumerate(initial_bounds):
        exact.add(r[j] >= lo, r[j] <= hi)
    exact.add(r[11] >= -1426)
    exact.add(
        r[50] >= 69,
        r[50] <= 79,
        r[55] >= -60,
        r[55] <= -50,
        r[55] <= r[50] - 129,
        r[27] >= -96,
        r[27] <= -48,
    )
    d = r[50] - r[55]
    exact.add(r[51] <= -132)
    exact.add(
        Or(
            And(d >= 129, d <= 132, r[51] >= -176, r[51] >= r[27] - 103),
            And(d >= 133, d <= 136, r[51] >= -177, r[51] >= r[27] - 103),
            And(d >= 137, d <= 139, r[51] >= -178, r[51] >= r[27] - 103),
        )
    )
    for j, (lo, hi) in v5.CANDIDATE_BOUNDS.items():
        exact.add(r[j] >= lo, r[j] <= hi)
    for item in pair_lock["bounds"]:
        i, j, sign, lo, hi = map(int, item)
        expr = r[i] + sign * r[j]
        exact.add(expr >= lo, expr <= hi)

    # MILP variables: 59 exact reduced integers, 48 support selector binaries,
    # 3 piecewise-r51 category binaries. All numerical output is only a candidate.
    b0 = RANK
    c0 = RANK + EXPECTED_EXCEPTIONAL_COUNT
    nvars = RANK + EXPECTED_EXCEPTIONAL_COUNT + CATEGORY_COUNT
    lower = np.full(nvars, -np.inf, dtype=np.float64)
    upper = np.full(nvars, np.inf, dtype=np.float64)
    integrality = np.ones(nvars, dtype=np.int8)
    for j, (lo, hi) in enumerate(initial_bounds):
        lower[j] = max(lower[j], float(lo))
        upper[j] = min(upper[j], float(hi))
    lower[11] = max(lower[11], -1426.0)
    for j, (lo, hi) in v5.CANDIDATE_BOUNDS.items():
        lower[j] = max(lower[j], float(lo))
        upper[j] = min(upper[j], float(hi))
    lower[50], upper[50] = max(lower[50], 69.0), min(upper[50], 79.0)
    lower[55], upper[55] = max(lower[55], -60.0), min(upper[55], -50.0)
    lower[27], upper[27] = max(lower[27], -96.0), min(upper[27], -48.0)
    upper[51] = min(upper[51], -132.0)
    for idx in range(b0, c0 + CATEGORY_COUNT):
        lower[idx], upper[idx] = 0.0, 1.0

    rows: list[tuple[np.ndarray, float, float]] = []
    for row in range(EXPECTED_ALL140_COUNT):
        coeffs = {j: int(Mred[row, j]) for j in range(RANK) if int(Mred[row, j]) != 0}
        total = orbit_totals[curve_to_orbit[row]]
        add_row(rows, -int(y0[row, 0]), total - int(y0[row, 0]), nvars, coeffs)

    # Exact prism linear constraints.
    add_row(rows, -np.inf, -129, nvars, {55: 1, 50: -1})
    add_row(rows, -103, np.inf, nvars, {51: 1, 27: -1})

    # Exact 3-way r51 boundary encoded with binary categories and safe small M.
    add_row(rows, 1, 1, nvars, {c0: 1, c0 + 1: 1, c0 + 2: 1})
    for k, (dlo, dhi, r51lo) in enumerate(((129, 132, -176), (133, 136, -177), (137, 139, -178))):
        ck = c0 + k
        # d >= dlo - 20(1-c); d <= dhi + 20(1-c)
        add_row(rows, dlo - 20, np.inf, nvars, {50: 1, 55: -1, ck: -20})
        add_row(rows, -np.inf, dhi + 20, nvars, {50: 1, 55: -1, ck: 20})
        # r51 >= r51lo - 50(1-c)
        add_row(rows, r51lo - 50, np.inf, nvars, {51: 1, ck: -50})

    for item in pair_lock["bounds"]:
        i, j, sign, lo, hi = map(int, item)
        add_row(rows, lo, hi, nvars, {i: 1, j: sign})

    exceptional_start = EXPECTED_ALL140_COUNT - EXPECTED_EXCEPTIONAL_COUNT
    for i in range(EXPECTED_EXCEPTIONAL_COUNT):
        row = exceptional_start + i
        coeffs = {j: int(Mred[row, j]) for j in range(RANK) if int(Mred[row, j]) != 0}
        coeffs[b0 + i] = -1
        add_row(rows, -int(y0[row, 0]), np.inf, nvars, coeffs)
    add_row(rows, required_support, np.inf, nvars, {b0 + i: 1 for i in range(EXPECTED_EXCEPTIONAL_COUNT)})

    A = np.vstack([x[0] for x in rows])
    lba = np.asarray([x[1] for x in rows], dtype=np.float64)
    uba = np.asarray([x[2] for x in rows], dtype=np.float64)
    if not np.isfinite(A).all():
        raise ValueError("MILP coefficient overflow")
    max_abs = int(np.max(np.abs(A))) if A.size else 0

    start = time.perf_counter()
    result = milp(
        c=np.zeros(nvars, dtype=np.float64),
        integrality=integrality,
        bounds=Bounds(lower, upper),
        constraints=LinearConstraint(A, lba, uba),
        options={"time_limit": float(args.wall_seconds), "presolve": True, "mip_rel_gap": 0.0},
    )
    elapsed = time.perf_counter() - start

    status = "UNKNOWN_CANDIDATE_SEARCH"
    witness = None
    exact_replay_status = None
    reject_reason = None
    proposed_r = None
    if result.x is not None:
        proposed = [int(round(float(value))) for value in result.x]
        proposed_r = proposed[:RANK]
        exact.push()
        try:
            for j, value in enumerate(proposed_r):
                exact.add(r[j] == value)
            replay = exact.check()
            exact_replay_status = str(replay)
            if replay == sat:
                witness = v5.reconstruct_witness(
                    data=data,
                    z=z,
                    Mred=Mred,
                    U=U,
                    y0=y0,
                    rvars=r,
                    model=exact.model(),
                    required_support=required_support,
                )
                status = "SAT"
            else:
                reject_reason = f"exact_z3_replay_rejected: {replay}"
        finally:
            exact.pop()

    payload = {
        "schema": "STAGE32_POST1473_INTEGRAL_PICARD_SUPPORT_MILP_CANDIDATE_PREFLIGHT_V6",
        "stage": 32,
        "leaf": "POST1473_FIXED_Z_SUPPORT_MILP_CANDIDATE_EXACT_REPLAY",
        "mode": "NUMERICAL_HIGHS_INTEGER_CANDIDATE_ON_EXACT_V5_LINEAR_MODEL_WITH_BINARY_SUPPORT_AND_PIECEWISE_R51_PLUS_EXACT_Z3_PICARD_REPLAY",
        "source_locks": {
            "v5_evidence_canonical_sha256": EXPECTED_V5_CANONICAL,
            "manifest_canonical_sha256": v5.EXPECTED_MANIFEST_SHA256,
            "node_support_preflight_canonical_sha256": v5.EXPECTED_PREFLIGHT_SHA256,
            "picard_adapter_canonical_sha256": EXPECTED_PICARD_ADAPTER_CANONICAL,
            "node_support_audit_canonical_sha256": EXPECTED_NODE_SUPPORT_AUDIT_CANONICAL,
            "affine_21ak_constraint_rows_sha256": EXPECTED_21AK_CONSTRAINT_ROWS_SHA256,
            "reduced_pairing_matrix_sha256": v5.EXPECTED_MATRIX_SHA256,
            "unimodular_transform_sha256": v5.EXPECTED_U_SHA256,
            "source_21az_lock_sha256": v5.EXPECTED_SOURCE_LOCK_SHA256,
        },
        "locked_projection": {
            **EXPECTED_TARGET,
            "required_positive_exceptional_support": required_support,
            "known_exact_picard_positive_exceptional_support": known_support,
            "known_exact_picard_class_excluded_by_refined_support_bound": True,
        },
        "candidate_problem": {
            "reduced_integer_rank": RANK,
            "support_binary_count": EXPECTED_EXCEPTIONAL_COUNT,
            "piecewise_category_binary_count": CATEGORY_COUNT,
            "total_milp_variable_count": nvars,
            "linear_constraint_row_count": len(rows),
            "all140_nonnegative_and_orbit_upper_bounds_included": True,
            "all_initial_coordinate_bounds_included": True,
            "compressed_21az_prism_included": True,
            "exact_piecewise_r51_boundary_included": True,
            "candidate_coordinate_bounds_included": True,
            "all_42_pair_cuts_included": True,
            "support_ge_47_encoded_by_binary_selectors": True,
            "max_abs_float_converted_integer_coefficient": max_abs,
            "numerical_backend_never_authorizes_unsat": True,
        },
        "candidate_search": {
            "backend": "scipy.optimize.milp/HiGHS",
            "wall_limit_seconds": args.wall_seconds,
            "solve_wall_seconds": elapsed,
            "solver_success": bool(result.success),
            "solver_status": int(result.status),
            "solver_message": str(result.message),
            "candidate_returned": result.x is not None,
            "candidate_reduced_translation_sha256": v5.csha(proposed_r) if proposed_r is not None else None,
            "reject_reason": reject_reason,
        },
        "exact_replay": {
            "status": status,
            "z3_version": get_version_string(),
            "z3_replay_status": exact_replay_status,
            "witness": witness,
            "sat_requires_exact_original_linear_model_replay": True,
            "sat_requires_exact_picard_reconstruction_and_all140_replay": True,
            "numerical_infeasible_or_timeout_is_unknown_not_unsat": True,
        },
        "firewalls": {
            "fixed_z_affine_fiber_closed": False,
            "full178_integral_picard_closed": False,
            "full178_geometric_closed": False,
            "multibranch_closed": False,
            "receiver_credit": False,
            "route_credit": False,
            "theorem_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
            "unknown_is_not_unsat": True,
        },
    }
    payload["canonical_sha256_without_this_field"] = v5.csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": "PASS_STAGE32_POST1473_SUPPORT_MILP_CANDIDATE_PREFLIGHT",
        "status": status,
        "candidate_returned": result.x is not None,
        "solver_status": int(result.status),
        "solve_wall_seconds": elapsed,
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
        "witness_support": witness.get("positive_exceptional_support") if witness else None,
    }, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
