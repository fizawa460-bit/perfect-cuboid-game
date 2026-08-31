#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from sympy import Matrix
from z3 import Real, SolverFor, get_version_string, sat, unknown, unsat

from certify_stage32_21ba_r51_interval_census import (
    EXPECTED_MATRIX_SHA256,
    EXPECTED_PAIRINGS,
    EXPECTED_RANK,
    EXPECTED_U_SHA256,
    R51_GLOBAL_HI,
    R51_GLOBAL_LO,
    derive_initial_bounds,
    load_source_lock,
    matrix_payload,
    prism_triples,
)
from diagnose_stage32_21ak_affine_2adic_membership import reconstruct_translation_data
from direct_picard_reynolds_lattice_diagnostic import csha, load_retained

EXPECTED_21AZ_LOCK_SHA256 = "3c83ce97058ad52124730376a4e41720a40eb45995994314ac47d7f973da40da"
EXPECTED_21BB_LOCK_SHA256 = "370bc29433006c5a5ac0b8ee977212f0a274449ab85c736e62b3f5cbf7e51405"
EXPECTED_TRIPLES = 3234
EXPECTED_FEASIBLE_INDICES = 124856
SCHEMA_SHARD = "STAGE32_21BE_R51_ENDPOINT_AUDIT_SHARD_V1"
SCHEMA_AGG = "STAGE32_21BE_R51_ENDPOINT_AUDIT_AGGREGATE_V1"


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_formula_lock(path: Path) -> dict:
    raw = json.loads(path.read_text())
    claimed = raw.pop("canonical_sha256_without_this_field")
    if claimed != EXPECTED_21BB_LOCK_SHA256 or csha(raw) != claimed:
        raise ValueError("21bb formula lock canonical regression")
    return raw


def predicted_lo(r50: int, r55: int, r27: int) -> int:
    return max(r27 - 103, -176 - ((r50 - r55 - 129) // 4))


def check_with(solver, constraint):
    solver.push()
    try:
        solver.add(constraint)
        result = solver.check()
        return result, solver.reason_unknown() if result == unknown else None
    finally:
        solver.pop()


def build_solver(source_lock: Path, retained: Path, marking: Path, timeout_ms: int):
    source = load_source_lock(source_lock)
    target = source["target"]
    z = tuple(int(v) for v in target["z"])
    bundle = load_retained(retained, "s32_21be_picard")
    mark = load_retained(marking, "s32_21be_marking")
    data = reconstruct_translation_data(mark, bundle)
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
    r = [Real(f"r_{j}") for j in range(EXPECTED_RANK)]
    solver = SolverFor("QF_LRA")
    solver.set(timeout=timeout_ms)
    for row in range(EXPECTED_PAIRINGS):
        expr = int(y0[row, 0]) + sum(int(Mred[row, j]) * r[j] for j in range(EXPECTED_RANK))
        total = orbit_totals[curve_to_orbit[row]]
        solver.add(expr >= 0, expr <= total)
    for j, (lo, hi) in enumerate(bounds):
        solver.add(r[j] >= lo, r[j] <= hi)
    solver.add(r[11] >= -1426)
    solver.add(r[51] >= R51_GLOBAL_LO, r[51] <= R51_GLOBAL_HI)
    return solver, r, target


def run_shard(args) -> None:
    if args.shard_count <= 0 or not (0 <= args.shard_index < args.shard_count):
        raise ValueError("invalid shard")
    load_formula_lock(args.formula_lock)
    if EXPECTED_21AZ_LOCK_SHA256 != "3c83ce97058ad52124730376a4e41720a40eb45995994314ac47d7f973da40da":
        raise AssertionError
    triples = list(prism_triples())
    if len(triples) != EXPECTED_TRIPLES:
        raise ValueError("prism count regression")
    start = EXPECTED_TRIPLES * args.shard_index // args.shard_count
    end = EXPECTED_TRIPLES * (args.shard_index + 1) // args.shard_count
    solver, r, target = build_solver(args.source_lock, args.retained, args.marking, args.per_check_timeout_ms)

    failures = []
    unknowns = []
    passed = 0
    checks = 0
    feasible_indices = 0
    for ordinal in range(start, end):
        r50, r55, r27 = triples[ordinal]
        lo = predicted_lo(r50, r55, r27)
        hi = -132
        solver.push()
        solver.add(r[50] == r50, r[55] == r55, r[27] == r27)
        try:
            eq_lo, reason_lo = check_with(solver, r[51] == lo)
            checks += 1
            eq_hi, reason_hi = check_with(solver, r[51] == hi)
            checks += 1
            below = unsat
            reason_below = None
            if lo > R51_GLOBAL_LO:
                below, reason_below = check_with(solver, r[51] <= lo - 1)
                checks += 1
        finally:
            solver.pop()
        row = {"ordinal": ordinal, "triple": [r50, r55, r27], "lo": lo, "hi": hi}
        if unknown in (eq_lo, eq_hi, below):
            row.update({"eq_lo": str(eq_lo), "eq_hi": str(eq_hi), "below": str(below), "reasons": [reason_lo, reason_hi, reason_below]})
            unknowns.append(row)
        elif eq_lo != sat or eq_hi != sat or below != unsat:
            row.update({"eq_lo": str(eq_lo), "eq_hi": str(eq_hi), "below": str(below)})
            failures.append(row)
        else:
            passed += 1
            feasible_indices += hi - lo + 1
        if (ordinal - start + 1) % 250 == 0:
            print(json.dumps({"shard": args.shard_index, "processed": ordinal - start + 1, "passed": passed, "failures": len(failures), "unknowns": len(unknowns)}), flush=True)

    payload = {
        "schema": SCHEMA_SHARD,
        "stage": 32,
        "leaf": "32-21be",
        "mode": "INDEPENDENT_EXACT_INTEGER_ENDPOINT_AND_LOWER_EXCLUSION_AUDIT_OF_21BB_R51_FORMULA",
        "source_21az_lock_sha256": EXPECTED_21AZ_LOCK_SHA256,
        "source_21bb_lock_sha256": EXPECTED_21BB_LOCK_SHA256,
        "z3_version": get_version_string(),
        "target": target,
        "partition": {"shard_index": args.shard_index, "shard_count": args.shard_count, "start_ordinal": start, "end_ordinal_exclusive": end, "expected_rows": end - start},
        "result": {"passed_rows": passed, "failure_count": len(failures), "unknown_count": len(unknowns), "exact_qf_lra_checks": checks, "formula_feasible_integer_r51_indices": feasible_indices, "failures": failures, "unknowns": unknowns},
        "interpretation": {
            "eq_lo_sat_plus_below_unsat_proves_exact_integer_lower_endpoint": True,
            "eq_hi_sat_plus_global_r51_upper_bound_proves_exact_integer_upper_endpoint": True,
            "fixed_triple_rational_projection_is_convex_interval": True,
            "therefore_all_integers_between_endpoints_are_rationally_feasible": True,
            "this_audit_does_not_establish_integer_sat_in_full_59d_lattice": True,
            "fixed_projection_unsat_is_not_slice_unsat": True,
            "representative_sample_only": True,
            "not_full178_numerical_credit": True
        }
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS_SHARD" if not failures and not unknowns else "SHARD_NOT_PASS", "canonical": payload["canonical_sha256_without_this_field"], "passed": passed, "failures": len(failures), "unknowns": len(unknowns), "feasible_indices": feasible_indices}), flush=True)


def run_aggregate(args) -> None:
    files = sorted(args.input_dir.glob("**/stage32-21be-r51-endpoint-audit-*.json"))
    if len(files) != args.shard_count:
        raise ValueError(f"expected {args.shard_count} shard files, got {len(files)}")
    rows = []
    source_shas = []
    for path in files:
        raw_sha = sha256_file(path)
        data = json.loads(path.read_text())
        claimed = data.pop("canonical_sha256_without_this_field")
        if csha(data) != claimed or data.get("schema") != SCHEMA_SHARD:
            raise ValueError(f"shard canonical/schema regression {path}")
        data["canonical_sha256_without_this_field"] = claimed
        rows.append(data)
        source_shas.append({"file": path.name, "raw_sha256": raw_sha, "canonical_sha256": claimed})
    rows.sort(key=lambda x: x["partition"]["shard_index"])
    expected_start = 0
    total_pass = total_fail = total_unknown = total_checks = total_feasible = 0
    for idx, row in enumerate(rows):
        p = row["partition"]
        if p["shard_index"] != idx or p["shard_count"] != args.shard_count or p["start_ordinal"] != expected_start:
            raise ValueError("shard partition regression")
        expected_start = p["end_ordinal_exclusive"]
        r = row["result"]
        total_pass += r["passed_rows"]
        total_fail += r["failure_count"]
        total_unknown += r["unknown_count"]
        total_checks += r["exact_qf_lra_checks"]
        total_feasible += r["formula_feasible_integer_r51_indices"]
    complete = expected_start == EXPECTED_TRIPLES and total_pass + total_fail + total_unknown == EXPECTED_TRIPLES
    pass_exact = complete and total_fail == 0 and total_unknown == 0 and total_pass == EXPECTED_TRIPLES and total_feasible == EXPECTED_FEASIBLE_INDICES
    payload = {
        "schema": SCHEMA_AGG,
        "stage": 32,
        "leaf": "32-21be",
        "status": "PASS_EXACT_21BB_R51_FORMULA_RESCUE" if pass_exact else "FAIL_OR_UNKNOWN_21BB_R51_FORMULA_AUDIT",
        "source_21az_lock_sha256": EXPECTED_21AZ_LOCK_SHA256,
        "source_21bb_lock_sha256": EXPECTED_21BB_LOCK_SHA256,
        "coverage": {"expected_triples": EXPECTED_TRIPLES, "complete_partition": complete, "passed_rows": total_pass, "failure_count": total_fail, "unknown_count": total_unknown, "exact_qf_lra_checks": total_checks},
        "result": {"formula_rationally_feasible_integer_r51_indices": total_feasible, "expected_formula_indices": EXPECTED_FEASIBLE_INDICES, "formula_rescued": pass_exact},
        "shard_sources": source_shas,
        "bug_context": {
            "21ba_integer_interval_upper_search_can_false_positive_when_real_interval_contains_no_integer": True,
            "21be_uses_direct_endpoint_equality_and_lower_exclusion_checks_instead": True,
            "21bb_21bc_21bd_remain_provisional_unless_this_aggregate_passes": True
        },
        "safety": {"unknown_is_not_unsat": True, "rational_feasibility_is_not_integer_sat": True, "fixed_projection_unsat_is_not_slice_unsat": True, "representative_sample_only": True, "not_full178_numerical_credit": True, "theorem_credit": False, "receiver_credit": False, "route_credit": False, "perfect_cuboid_existence_claim": False, "perfect_cuboid_nonexistence_claim": False}
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": payload["status"], "canonical": payload["canonical_sha256_without_this_field"], "passed": total_pass, "failures": total_fail, "unknowns": total_unknown, "feasible_indices": total_feasible}), flush=True)
    if not pass_exact:
        raise SystemExit(1)


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="mode", required=True)
    sh = sub.add_parser("shard")
    sh.add_argument("--source-lock", type=Path, required=True)
    sh.add_argument("--formula-lock", type=Path, required=True)
    sh.add_argument("--retained", type=Path, required=True)
    sh.add_argument("--marking", type=Path, required=True)
    sh.add_argument("--shard-index", type=int, required=True)
    sh.add_argument("--shard-count", type=int, default=2)
    sh.add_argument("--per-check-timeout-ms", type=int, default=1500)
    sh.add_argument("--output", type=Path, required=True)
    ag = sub.add_parser("aggregate")
    ag.add_argument("--input-dir", type=Path, required=True)
    ag.add_argument("--shard-count", type=int, default=2)
    ag.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if args.mode == "shard":
        run_shard(args)
    else:
        run_aggregate(args)


if __name__ == "__main__":
    main()
