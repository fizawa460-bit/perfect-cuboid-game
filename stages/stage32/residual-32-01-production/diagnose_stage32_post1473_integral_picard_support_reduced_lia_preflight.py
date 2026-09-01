#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy
from sympy import Matrix
from z3 import And, Int, Or, SolverFor, get_version_string, sat, unknown, unsat

from build_stage32_post21bl_full178_node_mass_census import (
    EXPECTED_AC_CERTIFICATE_SHA256,
    EXPECTED_MANIFEST_SHA256,
    EXPECTED_PREFLIGHT_SHA256,
    ceil_div,
    load_module_payload,
    load_preflight,
)
from certify_stage32_21ba_r51_interval_census import (
    EXPECTED_MATRIX_SHA256,
    EXPECTED_SOURCE_LOCK_SHA256,
    EXPECTED_U_SHA256,
    R51_GLOBAL_HI,
    R51_GLOBAL_LO,
    derive_initial_bounds,
    load_source_lock,
    matrix_payload,
)
from certify_stage32_21bc_pair_combination_projection import CANDIDATE_BOUNDS
from certify_stage32_21bd_pair_cut_closure import load_pair_lock
from certify_stage32_21bf_r49_per_triple_projection import load_21be_lock
from diagnose_stage32_21ak_affine_2adic_membership import reconstruct_translation_data
from diagnose_stage32_post1473_integral_picard_support_preflight import (
    EXPECTED_21AK_CONSTRAINT_ROWS_SHA256,
    EXPECTED_ALL140_COUNT,
    EXPECTED_EXCEPTIONAL_COUNT,
    EXPECTED_KNOWN_EXCEPTIONAL_SUPPORT,
    EXPECTED_NODE_SUPPORT_AUDIT_CANONICAL,
    EXPECTED_PICARD_ADAPTER_CANONICAL,
    EXPECTED_REQUIRED_EXCEPTIONAL_SUPPORT,
    EXPECTED_TARGET,
    load_canonical,
)
from direct_picard_reynolds_lattice_diagnostic import csha
from direct_picard_reynolds_rank2_antifixed_coset_bound import ReynoldsRank2AntiFixedCosetBound

V4_CANONICAL_SHA256 = "521bc9291bb6ab9b738528b23c04b46e24f83d89a326a6b95f787970a96a57c5"
EXPECTED_ORBIT_TOTALS = [72, 76, 64, 168, 124, 88, 88, 176, 1080, 268, 10, 100, 104, 52]
EXPECTED_RANK = 59


def reduced_model(data: dict, z: tuple[int, ...]):
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
        raise ValueError("reduced pairing matrix regression")
    if csha(matrix_payload(U)) != EXPECTED_U_SHA256:
        raise ValueError("unimodular transform regression")

    y0 = data["pairing_x0_map"] * Matrix(z)
    curve_to_orbit: dict[int, int] = {}
    orbit_totals: list[int] = []
    for oid, orbit in enumerate(data["orbits"]):
        total = sum(int(y0[int(i), 0]) for i in orbit)
        orbit_totals.append(total)
        for idx in orbit:
            curve_to_orbit[int(idx)] = oid
    if orbit_totals != EXPECTED_ORBIT_TOTALS:
        raise ValueError(f"fixed orbit total regression: {orbit_totals}")

    bounds = derive_initial_bounds(selected_red, pivots, y0, orbit_totals, curve_to_orbit)
    return Mred, U, y0, curve_to_orbit, orbit_totals, bounds


def reconstruct_witness(
    *,
    data: dict,
    z: tuple[int, ...],
    Mred: Matrix,
    U: Matrix,
    y0: Matrix,
    rvars,
    model,
    required_support: int,
) -> dict:
    rv = Matrix([int(model.eval(v, model_completion=True).as_long()) for v in rvars])
    original_t = U * rv
    pairings = y0 + Mred * rv
    pairings_t = tuple(int(pairings[i, 0]) for i in range(EXPECTED_ALL140_COUNT))
    exceptional = pairings_t[-EXPECTED_EXCEPTIONAL_COUNT:]
    support = sum(1 for value in exceptional if value > 0)
    if min(pairings_t) < 0 or support < required_support:
        raise ValueError("SAT witness violates support/nonnegativity")
    if data["M"] * original_t != Mred * rv:
        raise ValueError("reduced/original translation reconstruction regression")
    picard = data["x0_map"] * Matrix(z) + data["K"] * original_t
    if tuple(int(v) for v in data["C"] * picard) != z:
        raise ValueError("SAT Picard witness left locked projection")
    exact_pairings = data["adapter"].pairing_matrix * picard
    if tuple(int(exact_pairings[i, 0]) for i in range(EXPECTED_ALL140_COUNT)) != pairings_t:
        raise ValueError("SAT Picard witness pairing replay regression")
    return {
        "reduced_translation_sha256": csha([int(v) for v in rv]),
        "original_translation_sha256": csha([int(v) for v in original_t]),
        "picard_coordinates_sha256": csha([int(v) for v in picard]),
        "all140_pairings_sha256": csha(list(pairings_t)),
        "minimum_pairing": min(pairings_t),
        "maximum_pairing": max(pairings_t),
        "positive_exceptional_support": support,
        "zero_exceptional_indices": [i for i, value in enumerate(exceptional) if value == 0],
    }


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
    ap.add_argument("--branch-timeout-ms", type=int, default=5000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if args.branch_timeout_ms <= 0:
        raise ValueError("branch timeout must be positive")

    manifest = json.loads(args.manifest.read_text())
    claimed_manifest = manifest.pop("canonical_sha256_without_this_field")
    if csha(manifest) != claimed_manifest or claimed_manifest != EXPECTED_MANIFEST_SHA256:
        raise ValueError("FULL178 manifest canonical regression")
    node_preflight = load_preflight(args.node_preflight)
    if node_preflight["canonical_sha256_without_this_field"] != EXPECTED_PREFLIGHT_SHA256:
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
    required_support = ceil_div(int(target["degree"]) - 16 * int(target["genus"]) + 16, 4)
    if required_support != EXPECTED_REQUIRED_EXCEPTIONAL_SUPPORT:
        raise ValueError("required exceptional support regression")

    source = load_source_lock(args.source_lock)
    for key in ("row_id", "e", "a", "u", "v", "z"):
        if source["target"].get(key) != EXPECTED_TARGET[key]:
            raise ValueError(f"21az target regression at {key}")
    if source["compressed_survivor_region"]["integer_point_count"] != 3234:
        raise ValueError("21az prism population regression")
    if source["fourth_coordinate_selection"]["residual_integer_valid_bound"] != [R51_GLOBAL_LO, R51_GLOBAL_HI]:
        raise ValueError("21az r51 bound regression")
    # These loaders enforce the audited 21bb/21be/21bc lock chain.
    load_21be_lock(args.audit_lock)
    pair_lock = load_pair_lock(args.pair_lock)
    formula_raw = json.loads(args.formula_lock.read_text())
    if formula_raw.get("canonical_sha256_without_this_field") != "370bc29433006c5a5ac0b8ee977212f0a274449ab85c736e62b3f5cbf7e51405":
        raise ValueError("21bb formula lock canonical regression")

    bundle = load_module_payload(args.retained, "stage32_post1473_support_picard")
    marking = load_module_payload(args.marking, "stage32_post1473_support_marking")
    picard_model = ReynoldsRank2AntiFixedCosetBound.from_retained(marking, bundle)
    if picard_model.certificate["canonical_sha256_without_this_field"] != EXPECTED_AC_CERTIFICATE_SHA256:
        raise ValueError("audited 32-21ac evaluator certificate regression")
    data = reconstruct_translation_data(marking, bundle)
    if csha(list(tuple(data["constraint_rows"]))) != EXPECTED_21AK_CONSTRAINT_ROWS_SHA256:
        raise ValueError("21ak affine constraint-row regression")

    z = tuple(int(v) for v in target["z"])
    Mred, U, y0, curve_to_orbit, orbit_totals, bounds = reduced_model(data, z)

    # Replay the persisted support-44 Picard class through the same unimodular coordinates.
    known_picard = Matrix([int(v) for v in adapter_evidence["reconstruction"]["picard_coordinates"]])
    x0 = data["x0_map"] * Matrix(z)
    known_t, params = data["K"].gauss_jordan_solve(known_picard - x0)
    if params.rows != 0 or any(sympy.denom(v) != 1 for v in known_t):
        raise ValueError("known Picard class lacks integral translation")
    known_t = Matrix([int(v) for v in known_t])
    known_r = U.inv() * known_t
    if any(sympy.denom(v) != 1 for v in known_r):
        raise ValueError("unimodular reduced coordinate lift became nonintegral")
    known_r = Matrix([int(v) for v in known_r])
    known_pairings = tuple(int(v) for v in (y0 + Mred * known_r))
    persisted_pairings = tuple(int(v) for v in adapter_evidence["all140"]["pairings"])
    if known_pairings != persisted_pairings:
        raise ValueError("known Picard reduced-coordinate replay regression")
    known_support = sum(1 for v in known_pairings[-EXPECTED_EXCEPTIONAL_COUNT:] if v > 0)
    known_zero_indices = [i for i, v in enumerate(known_pairings[-EXPECTED_EXCEPTIONAL_COUNT:]) if v == 0]
    if known_support != EXPECTED_KNOWN_EXCEPTIONAL_SUPPORT:
        raise ValueError("known support regression")

    r = [Int(f"r_{j}") for j in range(EXPECTED_RANK)]
    solver = SolverFor("QF_LIA")
    solver.set(timeout=args.branch_timeout_ms)
    pairing_exprs = []
    for row in range(EXPECTED_ALL140_COUNT):
        expr = int(y0[row, 0]) + sum(int(Mred[row, j]) * r[j] for j in range(EXPECTED_RANK))
        pairing_exprs.append(expr)
        total = orbit_totals[curve_to_orbit[row]]
        solver.add(expr >= 0, expr <= total)
    for j, (lo, hi) in enumerate(bounds):
        solver.add(r[j] >= lo, r[j] <= hi)
    solver.add(r[11] >= -1426)

    # Exact 21az integer projection prism for every integer point in this fixed-z fiber.
    solver.add(
        r[50] >= 69,
        r[50] <= 79,
        r[55] >= -60,
        r[55] <= -50,
        r[55] <= r[50] - 129,
        r[27] >= -96,
        r[27] <= -48,
    )
    d = r[50] - r[55]
    solver.add(r[51] <= -132)
    solver.add(
        Or(
            And(d >= 129, d <= 132, r[51] >= -176, r[51] >= r[27] - 103),
            And(d >= 133, d <= 136, r[51] >= -177, r[51] >= r[27] - 103),
            And(d >= 137, d <= 139, r[51] >= -178, r[51] >= r[27] - 103),
        )
    )
    for j, (lo, hi) in CANDIDATE_BOUNDS.items():
        solver.add(r[j] >= lo, r[j] <= hi)
    for item in pair_lock["bounds"]:
        i, j, sign, lo, hi = map(int, item)
        expr = r[i] + sign * r[j]
        solver.add(expr >= lo, expr <= hi)

    exceptional_exprs = pairing_exprs[-EXPECTED_EXCEPTIONAL_COUNT:]
    exceptional_rank = int(Mred[-EXPECTED_EXCEPTIONAL_COUNT:, :].rank())
    branch_order = known_zero_indices + [i for i in range(EXPECTED_EXCEPTIONAL_COUNT) if i not in known_zero_indices]
    branch_results = []
    aggregate_status = "UNSAT"
    aggregate_witness = None
    sat_branch = None
    for omitted in branch_order:
        solver.push()
        for i, expr in enumerate(exceptional_exprs):
            if i != omitted:
                solver.add(expr >= 1)
        result = solver.check()
        record = {"omitted_exceptional_index": omitted}
        if result == sat:
            aggregate_status = "SAT"
            sat_branch = omitted
            record["status"] = "SAT"
            aggregate_witness = reconstruct_witness(
                data=data,
                z=z,
                Mred=Mred,
                U=U,
                y0=y0,
                rvars=r,
                model=solver.model(),
                required_support=required_support,
            )
            branch_results.append(record)
            solver.pop()
            break
        if result == unsat:
            record["status"] = "UNSAT"
        elif result == unknown:
            record["status"] = "UNKNOWN"
            record["reason"] = solver.reason_unknown()
            aggregate_status = "UNKNOWN"
        else:
            solver.pop()
            raise ValueError(f"unexpected solver status: {result}")
        branch_results.append(record)
        solver.pop()

    tested = len(branch_results)
    sat_count = sum(x["status"] == "SAT" for x in branch_results)
    unsat_count = sum(x["status"] == "UNSAT" for x in branch_results)
    unknown_count = sum(x["status"] == "UNKNOWN" for x in branch_results)
    if aggregate_status == "UNSAT" and (tested != EXPECTED_EXCEPTIONAL_COUNT or unsat_count != EXPECTED_EXCEPTIONAL_COUNT):
        raise ValueError("UNSAT aggregate requires all 48 branches UNSAT")
    if aggregate_status == "SAT" and sat_count != 1:
        raise ValueError("SAT aggregate requires one recorded SAT branch")
    if aggregate_status == "UNKNOWN" and (sat_count != 0 or unknown_count == 0):
        raise ValueError("UNKNOWN aggregate accounting regression")

    payload = {
        "schema": "STAGE32_POST1473_INTEGRAL_PICARD_SUPPORT_REDUCED_LIA_PREFLIGHT_V5",
        "stage": 32,
        "leaf": "POST1473_FIXED_Z_EXACT_REDUCED_SUPPORT_FEASIBILITY",
        "mode": "ONE_LOCKED_PROJECTION_EXACT_UNIMODULAR_LLL_REDUCED_QF_LIA_PLUS_21AZ_PRISM_PLUS_21BD_PAIR_CUTS_PLUS_48_SUPPORT_BRANCHES",
        "source_locks": {
            "main_merge_base": "4a08b3636b342b682d2a257aa157e146e86ba302",
            "v4_unknown_canonical_sha256": V4_CANONICAL_SHA256,
            "manifest_canonical_sha256": EXPECTED_MANIFEST_SHA256,
            "node_support_preflight_canonical_sha256": EXPECTED_PREFLIGHT_SHA256,
            "picard_adapter_canonical_sha256": EXPECTED_PICARD_ADAPTER_CANONICAL,
            "node_support_audit_canonical_sha256": EXPECTED_NODE_SUPPORT_AUDIT_CANONICAL,
            "affine_21ak_constraint_rows_sha256": EXPECTED_21AK_CONSTRAINT_ROWS_SHA256,
            "reduced_pairing_matrix_sha256": EXPECTED_MATRIX_SHA256,
            "unimodular_transform_sha256": EXPECTED_U_SHA256,
            "source_21az_lock_sha256": EXPECTED_SOURCE_LOCK_SHA256,
        },
        "locked_projection": {
            **EXPECTED_TARGET,
            "required_positive_exceptional_support": required_support,
            "known_exact_picard_positive_exceptional_support": known_support,
            "known_exact_picard_zero_exceptional_indices": known_zero_indices,
            "known_exact_picard_class_excluded_by_refined_support_bound": True,
            "known_exact_picard_reduced_translation_sha256": csha([int(v) for v in known_r]),
        },
        "reduced_integer_model": {
            "integer_rank": EXPECTED_RANK,
            "unimodular_change_of_coordinates": True,
            "exceptional_translation_rational_rank": exceptional_rank,
            "all140_nonnegative_enforced": True,
            "fixed_orbit_upper_bounds_enforced": True,
            "initial_integer_valid_coordinate_bounds_enforced": True,
            "compressed_21az_prism_enforced": True,
            "compressed_21az_prism_integer_point_count": 3234,
            "audited_r51_piecewise_lower_boundary_enforced": True,
            "candidate_coordinate_bound_count": len(CANDIDATE_BOUNDS),
            "pair_cut_count": len(pair_lock["bounds"]),
            "all_cuts_are_necessary_only_and_preserve_every_integer_solution": True,
        },
        "exact_48_branch_linearization": {
            "equivalence": "support>=47_of_48 iff union_j(all_exceptional_i_except_j>=1, exceptional_j>=0)",
            "branch_count": EXPECTED_EXCEPTIONAL_COUNT,
            "branch_timeout_ms": args.branch_timeout_ms,
            "tested_branch_count": tested,
            "sat_count": sat_count,
            "unsat_count": unsat_count,
            "unknown_count": unknown_count,
            "sat_branch": sat_branch,
            "branch_results": branch_results,
        },
        "affine_fiber_support_preflight": {
            "status": aggregate_status,
            "z3_version": get_version_string(),
            "witness": aggregate_witness,
            "sat_is_only_necessary_condition_survival": True,
            "unsat_would_reject_only_this_fixed_z_for_bijective_normalization_branch": True,
            "unknown_is_not_unsat": True,
            "self_intersection_threshold_enforced": False,
        },
        "firewalls": {
            "fixed_z_affine_fiber_closed": aggregate_status == "UNSAT",
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
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": "PASS_STAGE32_POST1473_INTEGRAL_PICARD_SUPPORT_REDUCED_LIA_PREFLIGHT",
        "fixed_z_affine_fiber_status": aggregate_status,
        "tested": tested,
        "sat": sat_count,
        "unsat": unsat_count,
        "unknown": unknown_count,
        "exceptional_rank": exceptional_rank,
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
