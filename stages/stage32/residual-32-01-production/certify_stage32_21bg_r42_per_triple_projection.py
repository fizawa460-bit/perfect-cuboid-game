#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from z3 import get_version_string, sat, unknown, unsat

from audit_stage32_21be_r51_endpoints import EXPECTED_TRIPLES, predicted_lo
from certify_stage32_21ba_r51_interval_census import prism_triples
from certify_stage32_21bf_r49_per_triple_projection import (
    EXPECTED_21BB_LOCK_SHA256,
    EXPECTED_21BE_LOCK_SHA256,
    build_21bf_solver,
    independent_integer_projection,
)
from certify_stage32_21bd_pair_cut_closure import EXPECTED_21BC_LOCK_SHA256
from direct_picard_reynolds_lattice_diagnostic import csha

EXPECTED_21BF_LOCK_SHA256 = "0eeebe9be4ed3315d3e0b078bf615681de5cad5ef261707a7e4de54f437efc7a"
SIXTH_COORDINATE = 42
SIXTH_GLOBAL_BOUND = (79, 125)
EXPECTED_INITIAL_DOMAIN_SIZE = 47
SCHEMA_SHARD = "STAGE32_21BG_EXACT_R42_PER_TRIPLE_PROJECTION_SHARD_V1"
SCHEMA_AGG = "STAGE32_21BG_EXACT_R42_PER_TRIPLE_PROJECTION_AGGREGATE_V1"


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_21bf_lock(path: Path) -> dict:
    raw = json.loads(path.read_text())
    claimed = raw.pop("canonical_sha256_without_this_field")
    if claimed != EXPECTED_21BF_LOCK_SHA256 or csha(raw) != claimed:
        raise ValueError("21bf lock canonical regression")
    if raw.get("status") != "PASS_EXACT_21BF_R49_PER_TRIPLE_PROJECTION":
        raise ValueError("21bf lock is not exact PASS")
    if raw.get("coverage", {}).get("unknown_triples") != 0:
        raise ValueError("21bf lock contains UNKNOWN")
    return raw


def r49_hi(r27: int) -> int:
    return min(178, 130 - (r27 // 2), 61 + ((-3 * r27) // 2))


def run_shard(args) -> None:
    if args.shard_count <= 0 or not (0 <= args.shard_index < args.shard_count):
        raise ValueError("invalid shard")
    lock = load_21bf_lock(args.fifth_lock)
    if lock["exact_r49_interval_formula"]["lower"] != 132:
        raise ValueError("21bf r49 lower regression")

    triples = list(prism_triples())
    if len(triples) != EXPECTED_TRIPLES:
        raise ValueError("prism count regression")
    start = EXPECTED_TRIPLES * args.shard_index // args.shard_count
    end = EXPECTED_TRIPLES * (args.shard_index + 1) // args.shard_count
    solver, r, target = build_21bf_solver(args)

    rows = []
    base_unsat = base_unknown = projection_empty = projection_unknown = resolved_nonempty = 0
    checks = total_r42_indices = 0

    for ordinal in range(start, end):
        r50, r55, r27 = triples[ordinal]
        r51_lo, r51_hi = predicted_lo(r50, r55, r27), -132
        r49_lo, r49_upper = 132, r49_hi(r27)
        solver.push()
        solver.add(
            r[50] == r50, r[55] == r55, r[27] == r27,
            r[51] >= r51_lo, r[51] <= r51_hi,
            r[49] >= r49_lo, r[49] <= r49_upper,
        )
        try:
            base = solver.check()
            checks += 1
            reason = solver.reason_unknown() if base == unknown else None
            row = {
                "ordinal": ordinal,
                "triple": [r50, r55, r27],
                "r51_band": [r51_lo, r51_hi],
                "r49_band": [r49_lo, r49_upper],
                "base_status": str(base),
            }
            if base == unsat:
                base_unsat += 1
                row["status"] = "EXACT_INTEGER_PRUNED_BY_FIVE_COORDINATE_RATIONAL_CLOSURE"
            elif base == unknown:
                base_unknown += 1
                row["status"] = "UNKNOWN"
                row["reason"] = reason
            elif base == sat:
                out = independent_integer_projection(
                    solver, r[SIXTH_COORDINATE], SIXTH_GLOBAL_BOUND[0], SIXTH_GLOBAL_BOUND[1]
                )
                checks += int(out["checks"])
                row["projection"] = out
                if out["status"] == "EMPTY_INTEGER_PROJECTION":
                    projection_empty += 1
                    row["status"] = "EXACT_INTEGER_PRUNED_BY_R42_INTEGRALITY"
                elif out["status"] == "UNKNOWN":
                    projection_unknown += 1
                    row["status"] = "UNKNOWN"
                elif out["status"] == "RESOLVED":
                    resolved_nonempty += 1
                    total_r42_indices += int(out["domain_size"])
                    row["status"] = "OPEN_WITH_EXACT_INTEGER_VALID_R42_INTERVAL"
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
        "leaf": "32-21bg",
        "mode": "EXACT_PER_TRIPLE_R42_INTEGER_VALID_PROJECTION_AFTER_R51_R49_COMPRESSION_AND_ALL_42_PAIR_CUTS",
        "source_21bb_lock_sha256": EXPECTED_21BB_LOCK_SHA256,
        "source_21bc_lock_sha256": EXPECTED_21BC_LOCK_SHA256,
        "source_21be_lock_sha256": EXPECTED_21BE_LOCK_SHA256,
        "source_21bf_lock_sha256": EXPECTED_21BF_LOCK_SHA256,
        "sixth_coordinate": SIXTH_COORDINATE,
        "sixth_global_integer_valid_bound": list(SIXTH_GLOBAL_BOUND),
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
            "r42_integer_valid_index_count": total_r42_indices,
            "rows": rows,
        },
        "interpretation": {
            "r51_r49_bands_and_all_42_pair_bounds_preserve_every_integer_solution": True,
            "independent_lower_upper_searches_allow_empty_integer_projection": True,
            "rational_unsat_or_empty_r42_integer_projection_prunes_the_fixed_triple_for_integer_solutions": True,
            "nonempty_r42_interval_is_only_integer_valid_necessary_data_not_integer_sat": True,
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
        "r42_indices": total_r42_indices,
    }), flush=True)


def run_aggregate(args) -> None:
    files = sorted(args.input_dir.glob("**/stage32-21bg-r42-projection-*.json"))
    if len(files) != args.shard_count:
        raise ValueError(f"expected {args.shard_count} shard files, got {len(files)}")
    shards, sources = [], []
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
    rows, total_checks = [], 0
    for idx, shard in enumerate(shards):
        p = shard["partition"]
        if p["shard_index"] != idx or p["shard_count"] != args.shard_count or p["start_ordinal"] != expected_start:
            raise ValueError("shard partition regression")
        expected_start = p["end_ordinal_exclusive"]
        rows.extend(shard["result"]["rows"])
        total_checks += int(shard["result"]["exact_qf_lra_checks"])
    rows.sort(key=lambda x: x["ordinal"])
    complete = expected_start == EXPECTED_TRIPLES and len(rows) == EXPECTED_TRIPLES and all(row["ordinal"] == i for i, row in enumerate(rows))

    base_unsat = sum(row["status"] == "EXACT_INTEGER_PRUNED_BY_FIVE_COORDINATE_RATIONAL_CLOSURE" for row in rows)
    empty = sum(row["status"] == "EXACT_INTEGER_PRUNED_BY_R42_INTEGRALITY" for row in rows)
    unknown_rows = [row for row in rows if row["status"] == "UNKNOWN"]
    open_rows = [row for row in rows if row["status"] == "OPEN_WITH_EXACT_INTEGER_VALID_R42_INTERVAL"]
    integer_pruned = base_unsat + empty
    total_r42_indices = sum(int(row["projection"]["domain_size"]) for row in open_rows)
    naive_indices = EXPECTED_TRIPLES * EXPECTED_INITIAL_DOMAIN_SIZE
    pass_exact = complete and not unknown_rows and integer_pruned + len(open_rows) == EXPECTED_TRIPLES
    fixed_projection_integer_unsat = pass_exact and not open_rows

    compact_open = [[row["ordinal"], *row["triple"], *row["r51_band"], *row["r49_band"], row["projection"]["lo"], row["projection"]["hi"]] for row in open_rows]
    compact_pruned = [[row["ordinal"], *row["triple"], row["status"]] for row in rows if row["status"].startswith("EXACT_INTEGER_PRUNED")]
    payload = {
        "schema": SCHEMA_AGG,
        "stage": 32,
        "leaf": "32-21bg",
        "status": "PASS_EXACT_21BG_R42_PER_TRIPLE_PROJECTION" if pass_exact else "PARTIAL_OR_UNKNOWN_21BG_R42_PER_TRIPLE_PROJECTION",
        "source_21bf_lock_sha256": EXPECTED_21BF_LOCK_SHA256,
        "sixth_coordinate": SIXTH_COORDINATE,
        "coverage": {
            "expected_triples": EXPECTED_TRIPLES,
            "complete_partition": complete,
            "base_five_coordinate_rational_unsat_triples": base_unsat,
            "r42_integer_empty_triples": empty,
            "exact_integer_pruned_triples": integer_pruned,
            "open_triples": len(open_rows),
            "unknown_triples": len(unknown_rows),
            "exact_qf_lra_checks": total_checks,
        },
        "compression": {
            "naive_r42_indices_before_per_triple_projection": naive_indices,
            "r42_integer_valid_indices_after_projection": total_r42_indices,
            "removed_candidate_indices": naive_indices - total_r42_indices,
        },
        "fixed_projection_integer_unsat": fixed_projection_integer_unsat,
        "compact_row_encoding": "[ordinal,r50,r55,r27,r51_lo,r51_hi,r49_lo,r49_hi,r42_lo,r42_hi]",
        "open_rows": compact_open,
        "pruned_row_encoding": "[ordinal,r50,r55,r27,reason]",
        "pruned_rows": compact_pruned,
        "unknown_rows": unknown_rows,
        "shard_sources": sources,
        "interpretation": {
            "pass_means_complete_exact_integer_valid_r42_projection_with_no_unknowns": True,
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
        "r42_indices": total_r42_indices,
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
    sh.add_argument("--fifth-lock", type=Path, required=True)
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
