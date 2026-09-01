#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from audit_stage32_21be_r51_endpoints import EXPECTED_TRIPLES, predicted_lo
from certify_stage32_21ba_r51_interval_census import prism_triples
from certify_stage32_21bf_r49_per_triple_projection import (
    build_21bf_solver,
    independent_integer_projection,
)
from certify_stage32_21bg_r42_per_triple_projection import audit_r49_formula, r49_hi
from certify_stage32_21bh_r54_per_triple_projection import audit_r42_formula, r42_lo
from certify_stage32_21bi_r57_per_triple_projection import (
    EXPECTED_21BH_LOCK_SHA256,
    R42_COORDINATE,
    R54_COORDINATE,
    R57_COORDINATE,
    R57_GLOBAL_BOUND,
    SCHEMA_SHARD,
    audit_r54_table_threshold,
    load_21bh_lock,
    r54_lo_from_table,
)
from direct_picard_reynolds_lattice_diagnostic import csha

SOURCE_RUN_ID = 33362677934
EXPECTED_UNKNOWN_ORDINAL = 1095
EXPECTED_UNKNOWN_TRIPLE = (75, -59, -79)
EXPECTED_SHARD_CANONICALS = {
    0: "4c0d7edcb9cf84998d8bcb8205282bd7bd31bd3667f42d19040602f053001b7a",
    1: "695886af0ab10a472404171492b14a69cc3ee2c0ed9b29298085fbcca6197b97",
}
EXPECTED_INITIAL_FAILED_AGGREGATE_CANONICAL = (
    "1c56793dbe91f93e9dc3be340c3d750d2f76957bbab38efe6d97c260be21b1a8"
)
SCHEMA = "STAGE32_21BI_TARGETED_UNKNOWN_RESCUE_AGGREGATE_V1"


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_source_shards(input_dir: Path) -> tuple[list[dict], list[dict]]:
    files = sorted(input_dir.glob("**/stage32-21bi-r57-projection-*.json"))
    if len(files) != 2:
        raise ValueError(f"expected exactly 2 source shards, got {len(files)}")
    shards = []
    sources = []
    for path in files:
        data = json.loads(path.read_text())
        claimed = data.pop("canonical_sha256_without_this_field")
        if data.get("schema") != SCHEMA_SHARD or csha(data) != claimed:
            raise ValueError(f"source shard canonical/schema regression: {path}")
        idx = int(data["partition"]["shard_index"])
        if claimed != EXPECTED_SHARD_CANONICALS[idx]:
            raise ValueError(f"unexpected source shard canonical for {idx}: {claimed}")
        data["canonical_sha256_without_this_field"] = claimed
        shards.append(data)
        sources.append({
            "shard_index": idx,
            "file": path.name,
            "raw_sha256": sha256_file(path),
            "canonical_sha256": claimed,
        })
    shards.sort(key=lambda x: x["partition"]["shard_index"])
    sources.sort(key=lambda x: x["shard_index"])
    if shards[0]["partition"]["start_ordinal"] != 0:
        raise ValueError("shard0 start regression")
    if shards[0]["partition"]["end_ordinal_exclusive"] != EXPECTED_TRIPLES // 2:
        raise ValueError("shard0 end regression")
    if shards[1]["partition"]["start_ordinal"] != EXPECTED_TRIPLES // 2:
        raise ValueError("shard1 start regression")
    if shards[1]["partition"]["end_ordinal_exclusive"] != EXPECTED_TRIPLES:
        raise ValueError("shard1 end regression")
    return shards, sources


def targeted_rescue(args) -> tuple[dict, int]:
    _, r54_table = load_21bh_lock(args.seventh_lock)
    triples = list(prism_triples())
    if len(triples) != EXPECTED_TRIPLES:
        raise ValueError("prism count regression")
    triple = tuple(map(int, triples[EXPECTED_UNKNOWN_ORDINAL]))
    if triple != EXPECTED_UNKNOWN_TRIPLE:
        raise ValueError(f"unknown target triple regression: {triple}")

    r50, r55, r27 = triple
    r51_lo, r51_hi = predicted_lo(r50, r55, r27), -132
    r49_lo, r49_upper = 132, r49_hi(r27)
    r42_lower, r42_upper = r42_lo(r50, r55, r27), 79
    r54_lower = r54_lo_from_table(r54_table, r50, r55, r27)
    r54_upper = -132

    solver, r, target = build_21bf_solver(args)
    checks = 0
    solver.push()
    try:
        solver.add(
            r[50] == r50,
            r[55] == r55,
            r[27] == r27,
            r[51] >= r51_lo,
            r[51] <= r51_hi,
        )
        r49_audit = audit_r49_formula(solver, r[49], r49_upper)
        checks += int(r49_audit["checks"])
        if r49_audit["status"] != "PASS_EXACT_R49_FORMULA_ENDPOINTS":
            raise RuntimeError(f"r49 targeted rescue failed: {r49_audit}")
        solver.add(r[49] >= r49_lo, r[49] <= r49_upper)

        r42_audit = audit_r42_formula(solver, r[R42_COORDINATE], r42_lower)
        checks += int(r42_audit["checks"])
        if r42_audit["status"] != "PASS_EXACT_R42_FORMULA_THRESHOLDS":
            raise RuntimeError(f"r42 targeted rescue failed: {r42_audit}")
        solver.add(r[R42_COORDINATE] >= r42_lower, r[R42_COORDINATE] <= r42_upper)

        r54_audit = audit_r54_table_threshold(solver, r[R54_COORDINATE], r54_lower)
        checks += int(r54_audit["checks"])
        if r54_audit["status"] != "PASS_EXACT_R54_TABLE_THRESHOLDS":
            raise RuntimeError(f"r54 targeted rescue failed: {r54_audit}")
        solver.add(r[R54_COORDINATE] >= r54_lower, r[R54_COORDINATE] <= r54_upper)

        projection = independent_integer_projection(
            solver, r[R57_COORDINATE], R57_GLOBAL_BOUND[0], R57_GLOBAL_BOUND[1]
        )
        checks += int(projection["checks"])
        if projection["status"] == "UNKNOWN":
            raise RuntimeError(f"r57 targeted rescue remained UNKNOWN: {projection}")
        if projection["status"] == "EMPTY_INTEGER_PROJECTION":
            status = "EXACT_INTEGER_PRUNED_BY_R57_INTEGRALITY"
        elif projection["status"] == "RESOLVED":
            status = "OPEN_WITH_EXACT_INTEGER_VALID_R57_INTERVAL"
        else:
            raise RuntimeError(projection["status"])

        row = {
            "ordinal": EXPECTED_UNKNOWN_ORDINAL,
            "triple": [r50, r55, r27],
            "r51_band": [r51_lo, r51_hi],
            "r49_band": [r49_lo, r49_upper],
            "r42_band": [r42_lower, r42_upper],
            "r54_band": [r54_lower, r54_upper],
            "r49_formula_audit": r49_audit,
            "r42_formula_audit": r42_audit,
            "r54_table_audit": r54_audit,
            "projection": projection,
            "status": status,
        }
        return row, checks
    finally:
        solver.pop()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input-dir", type=Path, required=True)
    ap.add_argument("--source-lock", type=Path, required=True)
    ap.add_argument("--formula-lock", type=Path, required=True)
    ap.add_argument("--pair-lock", type=Path, required=True)
    ap.add_argument("--audit-lock", type=Path, required=True)
    ap.add_argument("--fifth-lock", type=Path, required=True)
    ap.add_argument("--sixth-lock", type=Path, required=True)
    ap.add_argument("--seventh-lock", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--per-check-timeout-ms", type=int, default=20000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    shards, sources = load_source_shards(args.input_dir)
    rows = []
    source_checks = 0
    for shard in shards:
        rows.extend(shard["result"]["rows"])
        source_checks += int(shard["result"]["exact_qf_lra_checks"])
    rows.sort(key=lambda x: x["ordinal"])
    if len(rows) != EXPECTED_TRIPLES or any(r["ordinal"] != i for i, r in enumerate(rows)):
        raise ValueError("source row coverage regression")

    unknown_rows = [r for r in rows if r["status"] == "UNKNOWN"]
    if len(unknown_rows) != 1:
        raise ValueError(f"expected one source UNKNOWN, got {len(unknown_rows)}")
    old = unknown_rows[0]
    if (
        int(old["ordinal"]) != EXPECTED_UNKNOWN_ORDINAL
        or tuple(map(int, old["triple"])) != EXPECTED_UNKNOWN_TRIPLE
        or old.get("r42_formula_audit", {}).get("status") != "UNKNOWN"
        or old.get("r42_formula_audit", {}).get("phase") != "r42_upper_endpoint"
    ):
        raise ValueError(f"source UNKNOWN signature regression: {old}")

    rescued_row, rescue_checks = targeted_rescue(args)
    rows[EXPECTED_UNKNOWN_ORDINAL] = rescued_row

    final_unknown = [r for r in rows if r["status"] == "UNKNOWN"]
    mismatches = [
        r for r in rows
        if r["status"] in {"R49_FORMULA_MISMATCH", "R42_FORMULA_MISMATCH", "R54_TABLE_MISMATCH"}
    ]
    pruned = [r for r in rows if r["status"] == "EXACT_INTEGER_PRUNED_BY_R57_INTEGRALITY"]
    open_rows = [r for r in rows if r["status"] == "OPEN_WITH_EXACT_INTEGER_VALID_R57_INTERVAL"]
    if final_unknown or mismatches or len(pruned) + len(open_rows) != EXPECTED_TRIPLES:
        raise RuntimeError("repaired aggregate is not exact complete")

    total_r57_indices = sum(int(r["projection"]["domain_size"]) for r in open_rows)
    naive = EXPECTED_TRIPLES * 47
    compact_open = [
        [
            r["ordinal"], *r["triple"], *r["r51_band"], *r["r49_band"],
            *r["r42_band"], *r["r54_band"], r["projection"]["lo"], r["projection"]["hi"]
        ]
        for r in open_rows
    ]
    compact_pruned = [[r["ordinal"], *r["triple"], r["status"]] for r in pruned]

    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "leaf": "32-21bi",
        "status": "PASS_EXACT_21BI_R57_AFTER_TARGETED_UNKNOWN_RESCUE",
        "source_run_id": SOURCE_RUN_ID,
        "source_head_sha": "0ba9ebc6c1642798f32b3e98e0477dd4360c2a83",
        "source_21bh_lock_sha256": EXPECTED_21BH_LOCK_SHA256,
        "source_initial_failed_aggregate": {
            "canonical_sha256": EXPECTED_INITIAL_FAILED_AGGREGATE_CANONICAL,
            "open_triples": 3233,
            "unknown_triples": 1,
            "integer_pruned_triples": 0,
            "reason": "single QF_LRA timeout/canceled at ordinal 1095 r42 upper endpoint under 2000ms per-check timeout",
            "credit": False,
        },
        "targeted_rescue": {
            "ordinal": EXPECTED_UNKNOWN_ORDINAL,
            "triple": list(EXPECTED_UNKNOWN_TRIPLE),
            "per_check_timeout_ms": args.per_check_timeout_ms,
            "exact_qf_lra_checks": rescue_checks,
            "result_status": rescued_row["status"],
            "r42_audit": rescued_row["r42_formula_audit"],
            "r54_audit": rescued_row["r54_table_audit"],
            "r57_projection": rescued_row["projection"],
        },
        "coverage": {
            "expected_triples": EXPECTED_TRIPLES,
            "complete_partition": True,
            "r49_formula_mismatch_triples": 0,
            "r42_formula_mismatch_triples": 0,
            "r54_table_mismatch_triples": 0,
            "r57_integer_empty_triples": len(pruned),
            "exact_integer_pruned_triples": len(pruned),
            "open_triples": len(open_rows),
            "unknown_triples": 0,
            "source_qf_lra_checks": source_checks,
            "rescue_qf_lra_checks": rescue_checks,
            "total_executed_qf_lra_checks": source_checks + rescue_checks,
        },
        "compression": {
            "naive_r57_indices_before_per_triple_projection": naive,
            "r57_integer_valid_indices_after_projection": total_r57_indices,
            "removed_candidate_indices": naive - total_r57_indices,
        },
        "fixed_projection_integer_unsat": len(open_rows) == 0,
        "compact_row_encoding": (
            "[ordinal,r50,r55,r27,r51_lo,r51_hi,r49_lo,r49_hi,"
            "r42_lo,r42_hi,r54_lo,r54_hi,r57_lo,r57_hi]"
        ),
        "open_rows": compact_open,
        "pruned_row_encoding": "[ordinal,r50,r55,r27,reason]",
        "pruned_rows": compact_pruned,
        "source_shards": sources,
        "interpretation": {
            "targeted_rescue_only_replaces_the_single_source_unknown": True,
            "all_other_3233_source_rows_are_preserved_exactly": True,
            "open_rows_are_not_integer_sat_witnesses": True,
            "coordinate_interval_tightening_is_compression_not_closure": True,
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
        "open": len(open_rows),
        "pruned": len(pruned),
        "unknown": 0,
        "r57_indices": total_r57_indices,
        "rescue_ordinal": EXPECTED_UNKNOWN_ORDINAL,
        "rescue_projection": rescued_row["projection"],
    }), flush=True)


if __name__ == "__main__":
    main()
