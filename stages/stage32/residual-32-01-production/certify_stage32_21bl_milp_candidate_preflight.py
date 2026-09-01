#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from pathlib import Path

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from z3 import sat

from certify_stage32_21ba_r51_interval_census import prism_triples
from certify_stage32_21bl_isl_current_model_preflight import (
    RANK,
    SCHEMA,
    flatten_assertion,
    make_namespace,
    relation_text,
    verify_point,
)
from certify_stage32_21bl_joint_integer_closure import (
    EXPECTED_TRIPLES,
    bands_for,
    build_joint,
)
from direct_picard_reynolds_lattice_diagnostic import csha


def candidate_worker(cfg: dict, wall_seconds: int) -> dict:
    args = make_namespace(cfg)
    triples = list(prism_triples())
    ordinal = int(cfg["ordinal"])
    if len(triples) != EXPECTED_TRIPLES or not 0 <= ordinal < EXPECTED_TRIPLES:
        raise ValueError("21bl prism/ordinal regression")
    triple = triples[ordinal]
    solver, r, ri, target, table = build_joint(args)
    bands = bands_for(triple, table)
    solver.add(r[50] == triple[0], r[55] == triple[1], r[27] == triple[2])
    for j, (lo, hi) in bands.items():
        solver.add(r[j] >= lo, r[j] <= hi)

    names = [f"ri_{j}" for j in range(RANK)]
    relations = []
    canonical_atoms = []
    for assertion in solver.assertions():
        for atom in flatten_assertion(assertion):
            text, relation = relation_text(atom, names)
            canonical_atoms.append(text)
            relations.append(relation)
    problem_text = " and ".join(canonical_atoms)
    problem_sha = hashlib.sha256(problem_text.encode()).hexdigest()

    rows = []
    lower = []
    upper = []
    max_abs_integer = 0
    for coeffs, const, relation in relations:
        row = [int(coeffs.get(name, 0)) for name in names]
        rhs = -int(const)
        max_abs_integer = max(max_abs_integer, abs(rhs), *(abs(v) for v in row))
        rows.append(row)
        if relation == "<=":
            lower.append(-np.inf); upper.append(float(rhs))
        elif relation == ">=":
            lower.append(float(rhs)); upper.append(np.inf)
        elif relation == "=":
            lower.append(float(rhs)); upper.append(float(rhs))
        else:
            raise ValueError(relation)

    A = np.asarray(rows, dtype=np.float64)
    if not np.isfinite(A).all() or not all(math.isfinite(x) for x in upper if x != np.inf) or not all(math.isfinite(x) for x in lower if x != -np.inf):
        raise ValueError("21bl numerical candidate matrix overflow")

    start = time.perf_counter()
    result = milp(
        c=np.zeros(RANK, dtype=np.float64),
        integrality=np.ones(RANK, dtype=np.int8),
        bounds=Bounds(np.full(RANK, -np.inf), np.full(RANK, np.inf)),
        constraints=LinearConstraint(A, np.asarray(lower), np.asarray(upper)),
        options={"time_limit": float(wall_seconds), "presolve": True, "mip_rel_gap": 0.0},
    )
    elapsed = time.perf_counter() - start

    witness = None
    replay_status = None
    exact_relation_replay = False
    status = "UNKNOWN_CANDIDATE_SEARCH"
    reject_reason = None
    if result.x is not None:
        proposed = [int(round(float(v))) for v in result.x]
        point_map = {name: proposed[j] for j, name in enumerate(names)}
        try:
            verify_point(relations, point_map)
            exact_relation_replay = True
        except ValueError as exc:
            reject_reason = f"exact_relation_replay_rejected: {exc}"
        if exact_relation_replay:
            solver.push()
            try:
                for j, value in enumerate(proposed):
                    solver.add(ri[j] == value)
                replay = solver.check()
                replay_status = str(replay)
                if replay == sat:
                    witness = proposed
                    status = "SAT"
                else:
                    reject_reason = f"original_z3_replay_rejected: {replay}"
            finally:
                solver.pop()

    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "leaf": "32-21bl",
        "mode": "NUMERICAL_MILP_CANDIDATE_WITH_EXACT_Z3_REPLAY_ON_CURRENT_21BL_59D_JOINT_INTEGER_MODEL",
        "ordinal": ordinal,
        "triple": list(triple),
        "target": target,
        "current_exact_bands": {str(j): list(v) for j, v in sorted(bands.items())},
        "exact_problem": {
            "integer_rank": RANK,
            "assertion_count": len(relations),
            "problem_text_sha256": problem_sha,
            "same_integerized_21bl_assertions_as_z3_solver": True,
            "fixed_triple_constraints_included": True,
            "six_lossless_coordinate_bands_included": True,
            "all_42_pair_cuts_inherited_from_21bf": True,
            "floating_point_relaxation_used": False,
            "numerical_milp_used_only_to_propose_an_integer_candidate": True,
            "numerical_backend_never_authorizes_unsat": True,
            "sat_requires_exact_relation_replay_and_original_z3_replay": True,
            "max_abs_integer_coefficient_or_rhs_before_float_conversion": max_abs_integer,
        },
        "candidate_search": {
            "backend": "scipy.optimize.milp/HiGHS",
            "solver_success": bool(result.success),
            "solver_status": int(result.status),
            "solver_message": str(result.message),
            "solve_wall_seconds": elapsed,
            "candidate_returned": result.x is not None,
            "exact_relation_replay_passed": exact_relation_replay,
            "reject_reason": reject_reason,
        },
        "result": {
            "status": status,
            "solve_wall_seconds": elapsed,
            "witness_r_reduced": witness,
            "witness_sha256": csha(witness) if witness is not None else None,
            "original_z3_replay_status": replay_status,
        },
        "interpretation": {
            "sat_is_exact_fixed_projection_integer_witness_only": status == "SAT",
            "numerical_infeasible_or_timeout_has_no_unsat_credit": True,
            "unknown_is_not_unsat": True,
            "fixed_projection_unsat_is_not_slice_unsat": True,
            "representative_sample_only": True,
            "not_full178_numerical_credit": True,
        },
        "safety": {
            "preflight_only": True,
            "full_3234_scaleout_authorized_by_this_result": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    return payload


def main() -> None:
    ap = argparse.ArgumentParser()
    for name in ("source_lock", "formula_lock", "pair_lock", "audit_lock", "seventh_lock", "eighth_lock", "ninth_lock", "tenth_lock", "retained", "marking"):
        ap.add_argument("--" + name.replace("_", "-"), type=Path, required=True)
    ap.add_argument("--ordinal", type=int, default=1617)
    ap.add_argument("--wall-seconds", type=int, default=45)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    cfg = {name: str(getattr(args, name)) for name in ("source_lock", "formula_lock", "pair_lock", "audit_lock", "seventh_lock", "eighth_lock", "ninth_lock", "tenth_lock", "retained", "marking")}
    cfg["ordinal"] = int(args.ordinal)
    payload = candidate_worker(cfg, int(args.wall_seconds))
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": payload["result"]["status"],
        "ordinal": payload["ordinal"],
        "triple": payload["triple"],
        "canonical": payload["canonical_sha256_without_this_field"],
        "solve_wall_seconds": payload["result"].get("solve_wall_seconds"),
        "candidate_search": payload["candidate_search"],
    }), flush=True)
    if payload["result"]["status"] != "SAT":
        raise SystemExit(2)


if __name__ == "__main__":
    main()
