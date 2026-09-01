#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from z3 import get_version_string, sat, unknown, unsat

from audit_stage32_21be_r51_endpoints import EXPECTED_TRIPLES, predicted_lo
from certify_stage32_21ba_r51_interval_census import prism_triples
from certify_stage32_21bc_pair_combination_projection import CANDIDATE_BOUNDS
from certify_stage32_21bf_r49_per_triple_projection import (
    build_21bf_solver,
    check_with,
    independent_integer_projection,
)
from certify_stage32_21bg_r42_per_triple_projection import audit_r49_formula, r49_hi
from certify_stage32_21bh_r54_per_triple_projection import audit_r42_formula, r42_lo
from direct_picard_reynolds_lattice_diagnostic import csha

EXPECTED_21BH_LOCK_SHA256 = "23a732fd232cf025533cb9ef17c6ab482a5a50a860d163731a346faca7a11c6d"
R42_COORDINATE = 42
R54_COORDINATE = 54
R57_COORDINATE = 57
EXPECTED_R42_GLOBAL_BOUND = (33, 79)
EXPECTED_R54_GLOBAL_BOUND = (-178, -132)
EXPECTED_R57_GLOBAL_BOUND = (0, 46)
R42_GLOBAL_BOUND = CANDIDATE_BOUNDS[R42_COORDINATE]
R54_GLOBAL_BOUND = CANDIDATE_BOUNDS[R54_COORDINATE]
R57_GLOBAL_BOUND = CANDIDATE_BOUNDS[R57_COORDINATE]
EXPECTED_INITIAL_DOMAIN_SIZE = 47
SCHEMA_SHARD = "STAGE32_21BI_EXACT_R57_PER_TRIPLE_PROJECTION_SHARD_V1"
SCHEMA_AGG = "STAGE32_21BI_EXACT_R57_PER_TRIPLE_PROJECTION_AGGREGATE_V1"


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_21bh_lock(path: Path) -> tuple[dict, dict[tuple[int, int], int]]:
    raw = json.loads(path.read_text())
    claimed = raw.pop("canonical_sha256_without_this_field")
    if claimed != EXPECTED_21BH_LOCK_SHA256 or csha(raw) != claimed:
        raise ValueError("21bh r54 lock canonical regression")
    if raw.get("status") != "PASS_EXACT_21BH_R54_PER_TRIPLE_PROJECTION":
        raise ValueError("21bh r54 lock is not exact PASS")
    if tuple(raw.get("r54_global_integer_valid_bound", [])) != EXPECTED_R54_GLOBAL_BOUND:
        raise ValueError("21bh r54 global bound regression")

    table = raw.get("lossless_r54_interval_table", {})
    if (
        table.get("upper") != -132
        or table.get("r27_start") != -96
        or table.get("r27_end") != -48
        or table.get("unique_cells") != 539
        or table.get("delta_values") != list(range(11))
        or not table.get("verified_against_all_3234_exact_21bh_rows")
        or not table.get("depends_only_on_delta_and_r27_over_21az_prism")
    ):
        raise ValueError("21bh r54 lossless table metadata regression")

    decoded: dict[tuple[int, int], int] = {}
    lower_rle = table.get("lower_rle_by_delta", {})
    for delta in range(11):
        runs = lower_rle.get(str(delta))
        if not isinstance(runs, list):
            raise ValueError(f"missing r54 RLE for delta={delta}")
        r27 = -96
        for pair in runs:
            if not isinstance(pair, list) or len(pair) != 2:
                raise ValueError(f"invalid RLE entry at delta={delta}")
            value, count = int(pair[0]), int(pair[1])
            if count <= 0:
                raise ValueError(f"nonpositive RLE count at delta={delta}")
            if not (EXPECTED_R54_GLOBAL_BOUND[0] <= value <= EXPECTED_R54_GLOBAL_BOUND[1]):
                raise ValueError(f"r54 lower outside source bound at delta={delta}: {value}")
            for _ in range(count):
                if r27 > -48:
                    raise ValueError(f"RLE overflow at delta={delta}")
                decoded[(delta, r27)] = value
                r27 += 1
        if r27 != -47:
            raise ValueError(f"RLE coverage mismatch at delta={delta}: stopped at {r27}")
    if len(decoded) != 539:
        raise ValueError(f"decoded r54 table size regression: {len(decoded)}")
    return raw, decoded


def r54_lo_from_table(table: dict[tuple[int, int], int], r50: int, r55: int, r27: int) -> int:
    delta = r50 - r55 - 129
    try:
        return table[(delta, r27)]
    except KeyError as exc:
        raise ValueError(f"missing r54 table cell delta={delta}, r27={r27}") from exc


def audit_r54_table_threshold(solver, r54, lower: int) -> dict:
    checks = 0

    lo_result, lo_reason = check_with(solver, r54 == lower)
    checks += 1
    if lo_result == unknown:
        return {
            "status": "UNKNOWN",
            "phase": "r54_lower_endpoint",
            "reason": lo_reason,
            "checks": checks,
        }

    hi_result, hi_reason = check_with(solver, r54 == -132)
    checks += 1
    if hi_result == unknown:
        return {
            "status": "UNKNOWN",
            "phase": "r54_upper_endpoint",
            "reason": hi_reason,
            "checks": checks,
        }

    if lower > EXPECTED_R54_GLOBAL_BOUND[0]:
        below_result, below_reason = check_with(solver, r54 <= lower - 1)
        checks += 1
        if below_result == unknown:
            return {
                "status": "UNKNOWN",
                "phase": "r54_lower_exclusion",
                "reason": below_reason,
                "checks": checks,
            }
    else:
        below_result, below_reason = unsat, None

    above_result, above_reason = check_with(solver, r54 >= -131)
    checks += 1
    if above_result == unknown:
        return {
            "status": "UNKNOWN",
            "phase": "r54_upper_exclusion",
            "reason": above_reason,
            "checks": checks,
        }

    valid = (
        lo_result == sat
        and hi_result == sat
        and below_result == unsat
        and above_result == unsat
    )
    return {
        "status": "PASS_EXACT_R54_TABLE_THRESHOLDS" if valid else "R54_TABLE_MISMATCH",
        "lower_endpoint": str(lo_result),
        "upper_endpoint": str(hi_result),
        "lower_exclusion": str(below_result),
        "upper_exclusion": str(above_result),
        "checks": checks,
    }


def run_shard(args) -> None:
    if args.shard_count <= 0 or not (0 <= args.shard_index < args.shard_count):
        raise ValueError("invalid shard")
    if R42_GLOBAL_BOUND != EXPECTED_R42_GLOBAL_BOUND:
        raise ValueError(f"r42 source-domain regression: {R42_GLOBAL_BOUND}")
    if R54_GLOBAL_BOUND != EXPECTED_R54_GLOBAL_BOUND:
        raise ValueError(f"r54 source-domain regression: {R54_GLOBAL_BOUND}")
    if R57_GLOBAL_BOUND != EXPECTED_R57_GLOBAL_BOUND:
        raise ValueError(f"r57 source-domain regression: {R57_GLOBAL_BOUND}")

    _, r54_table = load_21bh_lock(args.seventh_lock)
    triples = list(prism_triples())
    if len(triples) != EXPECTED_TRIPLES:
        raise ValueError("prism count regression")
    start = EXPECTED_TRIPLES * args.shard_index // args.shard_count
    end = EXPECTED_TRIPLES * (args.shard_index + 1) // args.shard_count

    solver, r, target = build_21bf_solver(args)
    rows = []
    r49_mismatch = r49_unknown = 0
    r42_mismatch = r42_unknown = 0
    r54_mismatch = r54_unknown = 0
    projection_empty = projection_unknown = resolved_nonempty = 0
    checks = total_r57_indices = 0

    for ordinal in range(start, end):
        r50, r55, r27 = triples[ordinal]
        r51_lo, r51_hi = predicted_lo(r50, r55, r27), -132
        r49_lo, r49_upper = 132, r49_hi(r27)
        r42_lower, r42_upper = r42_lo(r50, r55, r27), 79
        r54_lower, r54_upper = r54_lo_from_table(r54_table, r50, r55, r27), -132

        solver.push()
        solver.add(
            r[50] == r50,
            r[55] == r55,
            r[27] == r27,
            r[51] >= r51_lo,
            r[51] <= r51_hi,
        )
        try:
            r49_audit = audit_r49_formula(solver, r[49], r49_upper)
            checks += int(r49_audit["checks"])
            row = {
                "ordinal": ordinal,
                "triple": [r50, r55, r27],
                "r51_band": [r51_lo, r51_hi],
                "r49_band": [r49_lo, r49_upper],
                "r42_band": [r42_lower, r42_upper],
                "r54_band": [r54_lower, r54_upper],
                "r49_formula_audit": r49_audit,
            }

            if r49_audit["status"] == "UNKNOWN":
                r49_unknown += 1
                row["status"] = "UNKNOWN"
            elif r49_audit["status"] != "PASS_EXACT_R49_FORMULA_ENDPOINTS":
                r49_mismatch += 1
                row["status"] = "R49_FORMULA_MISMATCH"
            else:
                solver.add(r[49] >= r49_lo, r[49] <= r49_upper)
                r42_audit = audit_r42_formula(solver, r[R42_COORDINATE], r42_lower)
                checks += int(r42_audit["checks"])
                row["r42_formula_audit"] = r42_audit

                if r42_audit["status"] == "UNKNOWN":
                    r42_unknown += 1
                    row["status"] = "UNKNOWN"
                elif r42_audit["status"] != "PASS_EXACT_R42_FORMULA_THRESHOLDS":
                    r42_mismatch += 1
                    row["status"] = "R42_FORMULA_MISMATCH"
                else:
                    solver.add(
                        r[R42_COORDINATE] >= r42_lower,
                        r[R42_COORDINATE] <= r42_upper,
                    )
                    r54_audit = audit_r54_table_threshold(
                        solver, r[R54_COORDINATE], r54_lower
                    )
                    checks += int(r54_audit["checks"])
                    row["r54_table_audit"] = r54_audit

                    if r54_audit["status"] == "UNKNOWN":
                        r54_unknown += 1
                        row["status"] = "UNKNOWN"
                    elif r54_audit["status"] != "PASS_EXACT_R54_TABLE_THRESHOLDS":
                        r54_mismatch += 1
                        row["status"] = "R54_TABLE_MISMATCH"
                    else:
                        solver.add(
                            r[R54_COORDINATE] >= r54_lower,
                            r[R54_COORDINATE] <= r54_upper,
                        )
                        out = independent_integer_projection(
                            solver,
                            r[R57_COORDINATE],
                            R57_GLOBAL_BOUND[0],
                            R57_GLOBAL_BOUND[1],
                        )
                        checks += int(out["checks"])
                        row["projection"] = out

                        if out["status"] == "EMPTY_INTEGER_PROJECTION":
                            projection_empty += 1
                            row["status"] = "EXACT_INTEGER_PRUNED_BY_R57_INTEGRALITY"
                        elif out["status"] == "UNKNOWN":
                            projection_unknown += 1
                            row["status"] = "UNKNOWN"
                        elif out["status"] == "RESOLVED":
                            resolved_nonempty += 1
                            total_r57_indices += int(out["domain_size"])
                            row["status"] = "OPEN_WITH_EXACT_INTEGER_VALID_R57_INTERVAL"
                        else:
                            raise RuntimeError(out["status"])

            rows.append(row)
        finally:
            solver.pop()

        if (ordinal - start + 1) % 200 == 0:
            print(
                json.dumps(
                    {
                        "shard": args.shard_index,
                        "processed": ordinal - start + 1,
                        "r49_mismatch": r49_mismatch,
                        "r42_mismatch": r42_mismatch,
                        "r54_mismatch": r54_mismatch,
                        "empty": projection_empty,
                        "unknown": (
                            r49_unknown
                            + r42_unknown
                            + r54_unknown
                            + projection_unknown
                        ),
                        "open": resolved_nonempty,
                    }
                ),
                flush=True,
            )

    unknown_count = r49_unknown + r42_unknown + r54_unknown + projection_unknown
    payload = {
        "schema": SCHEMA_SHARD,
        "stage": 32,
        "leaf": "32-21bi",
        "mode": (
            "INDEPENDENT_R54_TABLE_THRESHOLD_REAUDIT_THEN_EXACT_PER_TRIPLE_"
            "R57_INTEGER_VALID_PROJECTION"
        ),
        "source_21bh_lock_sha256": EXPECTED_21BH_LOCK_SHA256,
        "r54_global_integer_valid_bound": list(R54_GLOBAL_BOUND),
        "r57_coordinate": R57_COORDINATE,
        "r57_global_integer_valid_bound": list(R57_GLOBAL_BOUND),
        "selection_basis": (
            "continue 21az tie-break after r51/r49/r42/r54; r56 and r57 tie "
            "at residual domain 47 and nonzero all140 pairing rows 76; r57 wins "
            "by larger all140 L1 coefficient activity 788 > 478"
        ),
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
            "r49_formula_mismatch_count": r49_mismatch,
            "r49_formula_unknown_count": r49_unknown,
            "r42_formula_mismatch_count": r42_mismatch,
            "r42_formula_unknown_count": r42_unknown,
            "r54_table_mismatch_count": r54_mismatch,
            "r54_table_unknown_count": r54_unknown,
            "projection_empty_count": projection_empty,
            "projection_unknown_count": projection_unknown,
            "resolved_nonempty_count": resolved_nonempty,
            "exact_qf_lra_checks": checks,
            "r57_integer_valid_index_count": total_r57_indices,
            "rows": rows,
        },
        "interpretation": {
            "r54_table_is_reaudited_against_original_all140_system_before_consumption": True,
            "r54_lower_endpoint_and_exclusion_and_upper_endpoint_and_exclusion_checked_per_triple": True,
            "r51_r49_r42_r54_bands_and_all_42_pair_bounds_preserve_every_integer_solution": True,
            "empty_r57_projection_prunes_only_this_representative_fixed_triple": True,
            "nonempty_r57_interval_is_integer_valid_necessary_data_not_integer_sat": True,
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

    print(
        json.dumps(
            {
                "status": (
                    "PASS_SHARD"
                    if (
                        r49_mismatch == 0
                        and r42_mismatch == 0
                        and r54_mismatch == 0
                        and unknown_count == 0
                    )
                    else "SHARD_NOT_PASS"
                ),
                "canonical": payload["canonical_sha256_without_this_field"],
                "processed": len(rows),
                "r49_mismatch": r49_mismatch,
                "r42_mismatch": r42_mismatch,
                "r54_mismatch": r54_mismatch,
                "integer_pruned": projection_empty,
                "open": resolved_nonempty,
                "unknown": unknown_count,
                "r57_indices": total_r57_indices,
            }
        ),
        flush=True,
    )


def run_aggregate(args) -> None:
    files = sorted(args.input_dir.glob("**/stage32-21bi-r57-projection-*.json"))
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
        sources.append(
            {
                "file": path.name,
                "raw_sha256": raw_sha,
                "canonical_sha256": claimed,
            }
        )
    shards.sort(key=lambda x: x["partition"]["shard_index"])

    expected_start = 0
    rows, total_checks = [], 0
    for idx, shard in enumerate(shards):
        p = shard["partition"]
        if (
            p["shard_index"] != idx
            or p["shard_count"] != args.shard_count
            or p["start_ordinal"] != expected_start
        ):
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

    r49_mismatch_rows = [row for row in rows if row["status"] == "R49_FORMULA_MISMATCH"]
    r42_mismatch_rows = [row for row in rows if row["status"] == "R42_FORMULA_MISMATCH"]
    r54_mismatch_rows = [row for row in rows if row["status"] == "R54_TABLE_MISMATCH"]
    unknown_rows = [row for row in rows if row["status"] == "UNKNOWN"]
    pruned_rows = [
        row for row in rows if row["status"] == "EXACT_INTEGER_PRUNED_BY_R57_INTEGRALITY"
    ]
    open_rows = [
        row for row in rows if row["status"] == "OPEN_WITH_EXACT_INTEGER_VALID_R57_INTERVAL"
    ]
    total_r57_indices = sum(int(row["projection"]["domain_size"]) for row in open_rows)
    naive_indices = EXPECTED_TRIPLES * EXPECTED_INITIAL_DOMAIN_SIZE
    pass_exact = (
        complete
        and not r49_mismatch_rows
        and not r42_mismatch_rows
        and not r54_mismatch_rows
        and not unknown_rows
        and len(pruned_rows) + len(open_rows) == EXPECTED_TRIPLES
    )
    fixed_projection_integer_unsat = pass_exact and not open_rows

    compact_open = [
        [
            row["ordinal"],
            *row["triple"],
            *row["r51_band"],
            *row["r49_band"],
            *row["r42_band"],
            *row["r54_band"],
            row["projection"]["lo"],
            row["projection"]["hi"],
        ]
        for row in open_rows
    ]
    compact_pruned = [
        [row["ordinal"], *row["triple"], row["status"]]
        for row in pruned_rows
    ]

    payload = {
        "schema": SCHEMA_AGG,
        "stage": 32,
        "leaf": "32-21bi",
        "status": (
            "PASS_EXACT_21BI_R57_PER_TRIPLE_PROJECTION"
            if pass_exact
            else "FAIL_OR_UNKNOWN_21BI_R57_PER_TRIPLE_PROJECTION"
        ),
        "source_21bh_lock_sha256": EXPECTED_21BH_LOCK_SHA256,
        "r57_coordinate": R57_COORDINATE,
        "r57_global_integer_valid_bound": list(R57_GLOBAL_BOUND),
        "coverage": {
            "expected_triples": EXPECTED_TRIPLES,
            "complete_partition": complete,
            "r49_formula_mismatch_triples": len(r49_mismatch_rows),
            "r42_formula_mismatch_triples": len(r42_mismatch_rows),
            "r54_table_mismatch_triples": len(r54_mismatch_rows),
            "r57_integer_empty_triples": len(pruned_rows),
            "exact_integer_pruned_triples": len(pruned_rows),
            "open_triples": len(open_rows),
            "unknown_triples": len(unknown_rows),
            "exact_qf_lra_checks": total_checks,
        },
        "compression": {
            "naive_r57_indices_before_per_triple_projection": naive_indices,
            "r57_integer_valid_indices_after_projection": total_r57_indices,
            "removed_candidate_indices": naive_indices - total_r57_indices,
        },
        "fixed_projection_integer_unsat": fixed_projection_integer_unsat,
        "compact_row_encoding": (
            "[ordinal,r50,r55,r27,r51_lo,r51_hi,r49_lo,r49_hi,"
            "r42_lo,r42_hi,r54_lo,r54_hi,r57_lo,r57_hi]"
        ),
        "open_rows": compact_open,
        "pruned_row_encoding": "[ordinal,r50,r55,r27,reason]",
        "pruned_rows": compact_pruned,
        "r49_formula_mismatch_rows": r49_mismatch_rows,
        "r42_formula_mismatch_rows": r42_mismatch_rows,
        "r54_table_mismatch_rows": r54_mismatch_rows,
        "unknown_rows": unknown_rows,
        "shard_sources": sources,
        "interpretation": {
            "pass_includes_independent_r54_table_threshold_reaudit_on_all_3234_triples": True,
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

    print(
        json.dumps(
            {
                "status": payload["status"],
                "canonical": payload["canonical_sha256_without_this_field"],
                "r49_mismatch": len(r49_mismatch_rows),
                "r42_mismatch": len(r42_mismatch_rows),
                "r54_mismatch": len(r54_mismatch_rows),
                "integer_pruned": len(pruned_rows),
                "open": len(open_rows),
                "unknown": len(unknown_rows),
                "r57_indices": total_r57_indices,
                "fixed_projection_integer_unsat": fixed_projection_integer_unsat,
            }
        ),
        flush=True,
    )
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
    sh.add_argument("--sixth-lock", type=Path, required=True)
    sh.add_argument("--seventh-lock", type=Path, required=True)
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
