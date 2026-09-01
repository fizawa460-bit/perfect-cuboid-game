#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from z3 import get_version_string, sat, unknown, unsat

from audit_stage32_21be_r51_endpoints import (
    EXPECTED_21BB_LOCK_SHA256,
    EXPECTED_TRIPLES,
    build_solver,
    load_formula_lock,
    predicted_lo,
)
from certify_stage32_21ba_r51_interval_census import prism_triples
from certify_stage32_21bc_pair_combination_projection import CANDIDATE_BOUNDS
from certify_stage32_21bd_pair_cut_closure import (
    EXPECTED_21BC_LOCK_SHA256,
    load_pair_lock,
)
from direct_picard_reynolds_lattice_diagnostic import csha

EXPECTED_21BE_LOCK_SHA256 = "61a1c08ab999bce28bbbf15a5286262d548b2a81960f758571e8a54414484b08"
FIFTH_COORDINATE = 49
FIFTH_GLOBAL_BOUND = (132, 178)
EXPECTED_INITIAL_DOMAIN_SIZE = 47
SCHEMA_SHARD = "STAGE32_21BF_EXACT_R49_PER_TRIPLE_PROJECTION_SHARD_V1"
SCHEMA_AGG = "STAGE32_21BF_EXACT_R49_PER_TRIPLE_PROJECTION_AGGREGATE_V1"


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_21be_lock(path: Path) -> dict:
    raw = json.loads(path.read_text())
    claimed = raw.pop("canonical_sha256_without_this_field")
    if claimed != EXPECTED_21BE_LOCK_SHA256 or csha(raw) != claimed:
        raise ValueError("21be audit-lock canonical regression")
    if raw.get("status") != "PASS_EXACT_21BB_R51_FORMULA_RESCUE":
        raise ValueError("21be audit lock is not exact PASS")
    if raw.get("source_21bb_lock_sha256") != EXPECTED_21BB_LOCK_SHA256:
        raise ValueError("21be/21bb source regression")
    if not raw.get("credit_restored", {}).get("21bc_pair_bounds"):
        raise ValueError("21be does not restore 21bc pair bounds")
    if not raw.get("credit_restored", {}).get("21bd_pair_cut_closure"):
        raise ValueError("21be does not restore 21bd pair-cut closure")
    return raw


def check_with(solver, constraint):
    solver.push()
    try:
        solver.add(constraint)
        result = solver.check()
        return result, solver.reason_unknown() if result == unknown else None
    finally:
        solver.pop()


def independent_integer_projection(solver, expr, lo: int, hi: int) -> dict:
    """Return ceil(real min), floor(real max) using independent searches.

    The upper search deliberately restarts from the original [lo, hi], not
    from the lower endpoint. This makes an integer-empty real interval appear
    as lower > upper instead of the false-singleton failure mode found in 21ba.
    """
    checks = 0

    a, b = lo, hi
    while a < b:
        mid = (a + b) // 2
        result, reason = check_with(solver, expr <= mid)
        checks += 1
        if result == unknown:
            return {"status": "UNKNOWN", "phase": "lower", "reason": reason, "checks": checks}
        if result == sat:
            b = mid
        elif result == unsat:
            a = mid + 1
        else:
            raise RuntimeError(result)
    lower = a

    a, b = lo, hi
    while a < b:
        mid = (a + b + 1) // 2
        result, reason = check_with(solver, expr >= mid)
        checks += 1
        if result == unknown:
            return {"status": "UNKNOWN", "phase": "upper", "reason": reason, "checks": checks}
        if result == sat:
            a = mid
        elif result == unsat:
            b = mid - 1
        else:
            raise RuntimeError(result)
    upper = a

    if lower > upper:
        return {
            "status": "EMPTY_INTEGER_PROJECTION",
            "checks": checks,
            "lo": lower,
            "hi": upper,
            "domain_size": 0,
        }
    return {
        "status": "RESOLVED",
        "checks": checks,
        "lo": lower,
        "hi": upper,
        "domain_size": upper - lower + 1,
    }


def build_21bf_solver(args):
    load_formula_lock(args.formula_lock)
    load_21be_lock(args.audit_lock)
    pair_lock = load_pair_lock(args.pair_lock)
    solver, r, target = build_solver(args.source_lock, args.retained, args.marking, args.per_check_timeout_ms)

    for j, (lo, hi) in CANDIDATE_BOUNDS.items():
        solver.add(r[j] >= lo, r[j] <= hi)
    for item in pair_lock["bounds"]:
        i, j, sign, lo, hi = map(int, item)
        expr = r[i] + sign * r[j]
        solver.add(expr >= lo, expr <= hi)

    if CANDIDATE_BOUNDS.get(FIFTH_COORDINATE) != FIFTH_GLOBAL_BOUND:
        raise ValueError("r49 fifth-coordinate global bound regression")
    return solver, r, target


def run_shard(args) -> None:
    if args.shard_count <= 0 or not (0 <= args.shard_index < args.shard_count):
        raise ValueError("invalid shard")
    triples = list(prism_triples())
    if len(triples) != EXPECTED_TRIPLES:
        raise ValueError("prism count regression")
    start = EXPECTED_TRIPLES * args.shard_index // args.shard_count
    end = EXPECTED_TRIPLES * (args.shard_index + 1) // args.shard_count
    solver, r, target = build_21bf_solver(args)

    rows = []
    base_unsat = 0
    base_unknown = 0
    projection_empty = 0
    projection_unknown = 0
    resolved_nonempty = 0
    checks = 0
    total_r49_indices = 0

    for ordinal in range(start, end):
        r50, r55, r27 = triples[ordinal]
        r51_lo = predicted_lo(r50, r55, r27)
        r51_hi = -132
        solver.push()
        solver.add(
            r[50] == r50,
            r[55] == r55,
            r[27] == r27,
            r[51] >= r51_lo,
            r[51] <= r51_hi,
        )
        try:
            base = solver.check()
            base_reason = solver.reason_unknown() if base == unknown else None
            checks += 1
            row = {
                "ordinal": ordinal,
                "triple": [r50, r55, r27],
                "r51_band": [r51_lo, r51_hi],
                "base_status": str(base),
            }
            if base == unsat:
                base_unsat += 1
                row["status"] = "EXACT_INTEGER_PRUNED_BY_RATIONAL_PAIR_CUT_CLOSURE"
            elif base == unknown:
                base_unknown += 1
                row["status"] = "UNKNOWN"
                row["reason"] = base_reason
            elif base == sat:
                out = independent_integer_projection(
                    solver, r[FIFTH_COORDINATE], FIFTH_GLOBAL_BOUND[0], FIFTH_GLOBAL_BOUND[1]
                )
                checks += int(out["checks"])
                row["projection"] = out
                if out["status"] == "EMPTY_INTEGER_PROJECTION":
                    projection_empty += 1
                    row["status"] = "EXACT_INTEGER_PRUNED_BY_R49_INTEGRALITY"
                elif out["status"] == "UNKNOWN":
                    projection_unknown += 1
                    row["status"] = "UNKNOWN"
                elif out["status"] == "RESOLVED":
                    resolved_nonempty += 1
                    total_r49_indices += int(out["domain_size"])
                    row["status"] = "OPEN_WITH_EXACT_INTEGER_VALID_R49_INTERVAL"
                else:
                    raise RuntimeError(out["status"])
            else:
                raise RuntimeError(base)
            rows.append(row)
        finally:
            solver.pop()

        if (ordinal - start + 1) % 200 == 0:
            print(json.dumps({
                "shard": args.shard_index,
                "processed": ordinal - start + 1,
                "base_unsat": base_unsat,
                "empty": projection_empty,
                "unknown": base_unknown + projection_unknown,
                "open": resolved_nonempty,
            }), flush=True)

    payload = {
        "schema": SCHEMA_SHARD,
        "stage": 32,
        "leaf": "32-21bf",
        "mode": "EXACT_PER_TRIPLE_R49_INTEGER_VALID_PROJECTION_AFTER_21BE_R51_RESCUE_AND_ALL_42_PAIR_CUTS",
        "source_21bb_lock_sha256": EXPECTED_21BB_LOCK_SHA256,
        "source_21bc_lock_sha256": EXPECTED_21BC_LOCK_SHA256,
        "source_21be_lock_sha256": EXPECTED_21BE_LOCK_SHA256,
        "fifth_coordinate": FIFTH_COORDINATE,
        "fifth_global_integer_valid_bound": list(FIFTH_GLOBAL_BOUND),
        "selection_basis": "21az selection order continued after excluding chosen r51: among residual-domain-47 coordinates, r49 and r42 have maximal domain reduction 58; r49 wins by nonzero all140 pairing rows 77 > 65",
        "z3_version": get_version_string(),
        "target": target,
        "partition": {
            "shard_index": args.shard_index,
            "shard_count": args.shard_count,
            "start_ordinal": start,
            "end_ordinal_exclusive": end,
            "expected_rows": end - start,
        },
        "result": {
            "processed_rows": len(rows),
            "base_unsat_count": base_unsat,
            "base_unknown_count": base_unknown,
            "projection_empty_count": projection_empty,
            "projection_unknown_count": projection_unknown,
            "resolved_nonempty_count": resolved_nonempty,
            "exact_qf_lra_checks": checks,
            "r49_integer_valid_index_count": total_r49_indices,
            "rows": rows,
        },
        "interpretation": {
            "all_42_pair_bounds_preserve_every_integer_solution": True,
            "independent_lower_upper_searches_allow_empty_integer_projection": True,
            "base_rational_unsat_or_empty_r49_integer_projection_prunes_the_fixed_triple_for_integer_solutions": True,
            "nonempty_r49_interval_is_only_integer_valid_necessary_data_not_integer_sat": True,
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
    print(json.dumps({
        "status": "PASS_SHARD" if base_unknown + projection_unknown == 0 else "SHARD_WITH_UNKNOWN",
        "canonical": payload["canonical_sha256_without_this_field"],
        "processed": len(rows),
        "integer_pruned": base_unsat + projection_empty,
        "open": resolved_nonempty,
        "unknown": base_unknown + projection_unknown,
        "r49_indices": total_r49_indices,
    }), flush=True)


def run_aggregate(args) -> None:
    files = sorted(args.input_dir.glob("**/stage32-21bf-r49-projection-*.json"))
    if len(files) != args.shard_count:
        raise ValueError(f"expected {args.shard_count} shard files, got {len(files)}")

    shards = []
    sources = []
    for path in files:
        raw_sha = sha256_file(path)
        data = json.loads(path.read_text())
        claimed = data.pop("canonical_sha256_without_this_field")
        if csha(data) != claimed or data.get("schema") != SCHEMA_SHARD:
            raise ValueError(f"shard canonical/schema regression {path}")
        data["canonical_sha256_without_this_field"] = claimed
        shards.append(data)
        sources.append({"file": path.name, "raw_sha256": raw_sha, "canonical_sha256": claimed})

    shards.sort(key=lambda x: x["partition"]["shard_index"])
    expected_start = 0
    rows = []
    total_checks = 0
    for idx, shard in enumerate(shards):
        p = shard["partition"]
        if p["shard_index"] != idx or p["shard_count"] != args.shard_count or p["start_ordinal"] != expected_start:
            raise ValueError("shard partition regression")
        expected_start = p["end_ordinal_exclusive"]
        rows.extend(shard["result"]["rows"])
        total_checks += int(shard["result"]["exact_qf_lra_checks"])

    rows.sort(key=lambda x: x["ordinal"])
    complete = (
        expected_start == EXPECTED_TRIPLES
        and len(rows) == EXPECTED_TRIPLES
        and all(row["ordinal"] == i for i, row in enumerate(rows))
    )
    base_unsat = sum(row["status"] == "EXACT_INTEGER_PRUNED_BY_RATIONAL_PAIR_CUT_CLOSURE" for row in rows)
    empty = sum(row["status"] == "EXACT_INTEGER_PRUNED_BY_R49_INTEGRALITY" for row in rows)
    unknown_rows = [row for row in rows if row["status"] == "UNKNOWN"]
    open_rows = [row for row in rows if row["status"] == "OPEN_WITH_EXACT_INTEGER_VALID_R49_INTERVAL"]
    integer_pruned = base_unsat + empty
    total_r49_indices = sum(int(row["projection"]["domain_size"]) for row in open_rows)
    naive_indices = EXPECTED_TRIPLES * EXPECTED_INITIAL_DOMAIN_SIZE
    pass_exact = complete and not unknown_rows and integer_pruned + len(open_rows) == EXPECTED_TRIPLES

    compact_open = [
        [
            row["ordinal"],
            *row["triple"],
            *row["r51_band"],
            row["projection"]["lo"],
            row["projection"]["hi"],
        ]
        for row in open_rows
    ]
    compact_pruned = [
        [row["ordinal"], *row["triple"], row["status"]]
        for row in rows
        if row["status"].startswith("EXACT_INTEGER_PRUNED")
    ]

    fixed_projection_integer_unsat = pass_exact and len(open_rows) == 0
    payload = {
        "schema": SCHEMA_AGG,
        "stage": 32,
        "leaf": "32-21bf",
        "status": "PASS_EXACT_21BF_R49_PER_TRIPLE_PROJECTION" if pass_exact else "PARTIAL_OR_UNKNOWN_21BF_R49_PER_TRIPLE_PROJECTION",
        "source_21bb_lock_sha256": EXPECTED_21BB_LOCK_SHA256,
        "source_21bc_lock_sha256": EXPECTED_21BC_LOCK_SHA256,
        "source_21be_lock_sha256": EXPECTED_21BE_LOCK_SHA256,
        "fifth_coordinate": FIFTH_COORDINATE,
        "coverage": {
            "expected_triples": EXPECTED_TRIPLES,
            "complete_partition": complete,
            "base_pair_cut_rational_unsat_triples": base_unsat,
            "r49_integer_empty_triples": empty,
            "exact_integer_pruned_triples": integer_pruned,
            "open_triples": len(open_rows),
            "unknown_triples": len(unknown_rows),
            "exact_qf_lra_checks": total_checks,
        },
        "compression": {
            "naive_r49_indices_before_per_triple_projection": naive_indices,
            "r49_integer_valid_indices_after_projection": total_r49_indices,
            "removed_candidate_indices": naive_indices - total_r49_indices,
        },
        "fixed_projection_integer_unsat": fixed_projection_integer_unsat,
        "compact_row_encoding": "[ordinal,r50,r55,r27,r51_lo,r51_hi,r49_lo,r49_hi]",
        "open_rows": compact_open,
        "pruned_row_encoding": "[ordinal,r50,r55,r27,reason]",
        "pruned_rows": compact_pruned,
        "unknown_rows": unknown_rows,
        "shard_sources": sources,
        "interpretation": {
            "pass_means_complete_exact_integer_valid_r49_projection_with_no_unknowns": True,
            "pruned_triples_have_no_integer_solution_in_this_fixed_projection": True,
            "open_rows_are_not_integer_sat_witnesses": True,
            "fixed_projection_integer_unsat_if_all_3234_triples_pruned": True,
            "fixed_projection_unsat_is_not_slice_unsat": True,
            "representative_sample_only": True,
            "not_full178_numerical_credit": True,
        },
        "safety": {
            "unknown_is_not_unsat": True,
            "rational_feasibility_is_not_integer_sat": True,
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
        "status": payload["status"],
        "canonical": payload["canonical_sha256_without_this_field"],
        "integer_pruned": integer_pruned,
        "open": len(open_rows),
        "unknown": len(unknown_rows),
        "r49_indices": total_r49_indices,
        "fixed_projection_integer_unsat": fixed_projection_integer_unsat,
    }), flush=True)
    if not pass_exact:
        raise SystemExit(1)


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="mode", required=True)
    sh = sub.add_parser("shard")
    sh.add_argument("--source-lock", type=Path, required=True)
    sh.add_argument("--formula-lock", type=Path, required=True)
    sh.add_argument("--pair-lock", type=Path, required=True)
    sh.add_argument("--audit-lock", type=Path, required=True)
    sh.add_argument("--retained", type=Path, required=True)
    sh.add_argument("--marking", type=Path, required=True)
    sh.add_argument("--shard-index", type=int, required=True)
    sh.add_argument("--shard-count", type=int, default=2)
    sh.add_argument("--per-check-timeout-ms", type=int, default=2000)
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
