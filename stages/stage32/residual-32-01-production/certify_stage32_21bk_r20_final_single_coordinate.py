#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from z3 import get_version_string, unknown

from audit_stage32_21be_r51_endpoints import EXPECTED_TRIPLES, predicted_lo
from certify_stage32_21ba_r51_interval_census import prism_triples
from certify_stage32_21bc_pair_combination_projection import CANDIDATE_BOUNDS
from certify_stage32_21bf_r49_per_triple_projection import (
    build_21bf_solver,
    check_with,
    independent_integer_projection,
)
from certify_stage32_21bg_r42_per_triple_projection import r49_hi
from certify_stage32_21bh_r54_per_triple_projection import load_21bh_lock, r42_lo, r54_lo_from_table
from certify_stage32_21bj_r56_per_triple_projection import r57_hi
from direct_picard_reynolds_lattice_diagnostic import csha

EXPECTED_21BI_LOCK_SHA256 = "171de3592fec3f32a381de8a07365e3444cbfc75d5acb2e0eff053bd644bc06c"
EXPECTED_21BJ_LOCK_SHA256 = "8d803f10a52ef9b07bc1b06f2a705af068f815424296fe1cfd393d4ecdaea337"
R20, R56, R57 = 20, 56, 57
R20_BOUND, R56_BOUND, R57_BOUND = (86, 132), (14, 60), (0, 46)
SCHEMA_SHARD = "STAGE32_21BK_EXACT_R20_PER_TRIPLE_PROJECTION_SHARD_V1"
SCHEMA_AGG = "STAGE32_21BK_EXACT_R20_PER_TRIPLE_PROJECTION_AGGREGATE_V1"


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_canonical_lock(path: Path, expected: str, status: str) -> dict:
    raw = json.loads(path.read_text())
    claimed = raw.pop("canonical_sha256_without_this_field")
    if claimed != expected or csha(raw) != claimed:
        raise ValueError(f"lock canonical regression: {path}")
    if raw.get("status") != status:
        raise ValueError(f"lock status regression: {path}")
    return raw


def ceil_div2(n: int) -> int:
    return -((-n) // 2)


def r56_lo(r50: int, r55: int, r27: int) -> int:
    delta = r50 - r55 - 129
    if not 0 <= delta <= 10:
        raise ValueError(f"delta outside 21az prism: {delta}")
    return max(
        ceil_div2(r27 + 128 - (delta // 2)),
        ceil_div2(3 * r27 + 262),
    )


def audit_interval_formula(solver, expr, lo: int, hi: int, label: str) -> dict:
    checks = 0
    states = {}
    for name, constraint in (
        ("lo", expr == lo),
        ("hi", expr == hi),
        ("below", expr <= lo - 1),
        ("above", expr >= hi + 1),
    ):
        result, reason = check_with(solver, constraint)
        checks += 1
        states[name] = str(result)
        if result == unknown:
            return {"status": "UNKNOWN", "phase": name, "reason": reason, "checks": checks}
    expected = {"lo": "sat", "hi": "sat", "below": "unsat", "above": "unsat"}
    return {
        "status": f"PASS_EXACT_{label}_FORMULA_THRESHOLDS" if states == expected else f"{label}_FORMULA_MISMATCH",
        "checks": checks,
        **states,
    }


def run_shard(args) -> None:
    if CANDIDATE_BOUNDS.get(R20) != R20_BOUND:
        raise ValueError("r20 source-domain regression")
    if CANDIDATE_BOUNDS.get(R56) != R56_BOUND or CANDIDATE_BOUNDS.get(R57) != R57_BOUND:
        raise ValueError("r56/r57 source-domain regression")

    load_canonical_lock(
        args.eighth_lock,
        EXPECTED_21BI_LOCK_SHA256,
        "PASS_EXACT_21BI_R57_AFTER_TARGETED_UNKNOWN_RESCUE",
    )
    ninth = load_canonical_lock(
        args.ninth_lock,
        EXPECTED_21BJ_LOCK_SHA256,
        "PASS_EXACT_21BJ_R56_PER_TRIPLE_PROJECTION",
    )
    formula = ninth.get("lossless_r56_interval_formula", {})
    if (
        formula.get("lower_formula")
        != "max(ceil((r27+128-floor(delta/2))/2), ceil((3*r27+262)/2))"
        or formula.get("upper") != 60
        or not formula.get("verified_against_all_3234_exact_21bj_rows")
    ):
        raise ValueError("21bj r56 formula metadata regression")

    _, r54_table = load_21bh_lock(args.seventh_lock)
    triples = list(prism_triples())
    if len(triples) != EXPECTED_TRIPLES:
        raise ValueError("prism count regression")
    start = EXPECTED_TRIPLES * args.shard_index // args.shard_count
    end = EXPECTED_TRIPLES * (args.shard_index + 1) // args.shard_count
    solver, r, target = build_21bf_solver(args)

    rows = []
    checks = 0
    mismatch = audit_unknown = projection_unknown = 0
    empty = opened = total_r20_indices = 0

    for ordinal in range(start, end):
        r50, r55, r27 = triples[ordinal]
        bands = {
            51: (predicted_lo(r50, r55, r27), -132),
            49: (132, r49_hi(r27)),
            42: (r42_lo(r50, r55, r27), 79),
            54: (r54_lo_from_table(r54_table, r50, r55, r27), -132),
            57: (0, r57_hi(r27)),
            56: (r56_lo(r50, r55, r27), 60),
        }
        solver.push()
        solver.add(r[50] == r50, r[55] == r55, r[27] == r27)
        for j in (51, 49, 42, 54, 57):
            solver.add(r[j] >= bands[j][0], r[j] <= bands[j][1])
        try:
            audit = audit_interval_formula(solver, r[R56], bands[56][0], bands[56][1], "R56")
            checks += int(audit["checks"])
            row = {
                "ordinal": ordinal,
                "triple": [r50, r55, r27],
                "bands": {str(j): list(bands[j]) for j in (51, 49, 42, 54, 57, 56)},
                "r56_formula_audit": audit,
            }
            if audit["status"] == "UNKNOWN":
                audit_unknown += 1
                row["status"] = "UNKNOWN"
            elif audit["status"] != "PASS_EXACT_R56_FORMULA_THRESHOLDS":
                mismatch += 1
                row["status"] = "R56_FORMULA_MISMATCH"
            else:
                solver.add(r[R56] >= bands[56][0], r[R56] <= bands[56][1])
                out = independent_integer_projection(solver, r[R20], *R20_BOUND)
                checks += int(out["checks"])
                row["projection"] = out
                if out["status"] == "EMPTY_INTEGER_PROJECTION":
                    empty += 1
                    row["status"] = "EXACT_INTEGER_PRUNED_BY_R20_INTEGRALITY"
                elif out["status"] == "UNKNOWN":
                    projection_unknown += 1
                    row["status"] = "UNKNOWN"
                elif out["status"] == "RESOLVED":
                    opened += 1
                    total_r20_indices += int(out["domain_size"])
                    row["status"] = "OPEN_WITH_EXACT_INTEGER_VALID_R20_INTERVAL"
                else:
                    raise RuntimeError(out["status"])
            rows.append(row)
        finally:
            solver.pop()

        if (ordinal - start + 1) % 250 == 0:
            print(
                json.dumps({
                    "shard": args.shard_index,
                    "processed": ordinal - start + 1,
                    "mismatch": mismatch,
                    "empty": empty,
                    "unknown": audit_unknown + projection_unknown,
                    "open": opened,
                }),
                flush=True,
            )

    unknown_count = audit_unknown + projection_unknown
    payload = {
        "schema": SCHEMA_SHARD,
        "stage": 32,
        "leaf": "32-21bk",
        "mode": "FINAL_SINGLE_COORDINATE_R56_REAUDIT_THEN_R20_INTEGER_VALID_PROJECTION",
        "source_21bj_lock_sha256": EXPECTED_21BJ_LOCK_SHA256,
        "r20_global_integer_valid_bound": list(R20_BOUND),
        "r56_global_integer_valid_bound": list(R56_BOUND),
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
            "r56_formula_mismatch_count": mismatch,
            "r56_formula_unknown_count": audit_unknown,
            "projection_empty_count": empty,
            "projection_unknown_count": projection_unknown,
            "resolved_nonempty_count": opened,
            "exact_qf_lra_checks": checks,
            "r20_integer_valid_index_count": total_r20_indices,
            "rows": rows,
        },
        "interpretation": {
            "r56_formula_is_independently_reaudited_against_original_all140_system_before_consumption": True,
            "this_is_the_final_authorized_single_coordinate_leaf": True,
            "if_open_after_21bk_transition_to_joint_integer_closure_not_another_coordinate": True,
            "empty_r20_projection_prunes_only_this_representative_fixed_triple": True,
            "nonempty_r20_interval_is_integer_valid_necessary_data_not_integer_sat": True,
            "unknown_is_not_unsat": True,
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
        json.dumps({
            "status": "PASS_SHARD" if mismatch == 0 and unknown_count == 0 else "SHARD_NOT_PASS",
            "canonical": payload["canonical_sha256_without_this_field"],
            "processed": len(rows),
            "mismatch": mismatch,
            "integer_pruned": empty,
            "open": opened,
            "unknown": unknown_count,
            "r20_indices": total_r20_indices,
        }),
        flush=True,
    )


def run_aggregate(args) -> None:
    files = sorted(args.input_dir.glob("**/stage32-21bk-r20-projection-*.json"))
    if len(files) != args.shard_count:
        raise ValueError(f"expected {args.shard_count} shard files, got {len(files)}")
    shards, sources = [], []
    for path in files:
        data = json.loads(path.read_text())
        claimed = data.pop("canonical_sha256_without_this_field")
        if data.get("schema") != SCHEMA_SHARD or csha(data) != claimed:
            raise ValueError(f"shard canonical/schema regression {path}")
        data["canonical_sha256_without_this_field"] = claimed
        shards.append(data)
        sources.append({"file": path.name, "raw_sha256": sha256_file(path), "canonical_sha256": claimed})
    shards.sort(key=lambda x: x["partition"]["shard_index"])

    rows, expected_start, checks = [], 0, 0
    for idx, shard in enumerate(shards):
        p = shard["partition"]
        if p["shard_index"] != idx or p["shard_count"] != args.shard_count or p["start_ordinal"] != expected_start:
            raise ValueError("shard partition regression")
        expected_start = p["end_ordinal_exclusive"]
        rows.extend(shard["result"]["rows"])
        checks += int(shard["result"]["exact_qf_lra_checks"])
    rows.sort(key=lambda x: x["ordinal"])
    complete = expected_start == EXPECTED_TRIPLES and len(rows) == EXPECTED_TRIPLES and all(
        row["ordinal"] == i for i, row in enumerate(rows)
    )
    mismatch = [row for row in rows if row["status"] == "R56_FORMULA_MISMATCH"]
    unknown_rows = [row for row in rows if row["status"] == "UNKNOWN"]
    pruned = [row for row in rows if row["status"] == "EXACT_INTEGER_PRUNED_BY_R20_INTEGRALITY"]
    opened = [row for row in rows if row["status"] == "OPEN_WITH_EXACT_INTEGER_VALID_R20_INTERVAL"]
    total = sum(int(row["projection"]["domain_size"]) for row in opened)
    passed = complete and not mismatch and not unknown_rows and len(pruned) + len(opened) == EXPECTED_TRIPLES

    compact_open = [
        [
            row["ordinal"], *row["triple"],
            *row["bands"]["51"], *row["bands"]["49"], *row["bands"]["42"],
            *row["bands"]["54"], *row["bands"]["57"], *row["bands"]["56"],
            row["projection"]["lo"], row["projection"]["hi"],
        ]
        for row in opened
    ]
    payload = {
        "schema": SCHEMA_AGG,
        "stage": 32,
        "leaf": "32-21bk",
        "status": "PASS_EXACT_21BK_R20_FINAL_SINGLE_COORDINATE_PROJECTION" if passed else "FAIL_OR_UNKNOWN_21BK_R20_PROJECTION",
        "source_21bj_lock_sha256": EXPECTED_21BJ_LOCK_SHA256,
        "r20_global_integer_valid_bound": list(R20_BOUND),
        "coverage": {
            "expected_triples": EXPECTED_TRIPLES,
            "complete_partition": complete,
            "r56_formula_mismatch_triples": len(mismatch),
            "r20_integer_empty_triples": len(pruned),
            "exact_integer_pruned_triples": len(pruned),
            "open_triples": len(opened),
            "unknown_triples": len(unknown_rows),
            "exact_qf_lra_checks": checks,
        },
        "compression": {
            "naive_r20_indices_before_per_triple_projection": EXPECTED_TRIPLES * 47,
            "r20_integer_valid_indices_after_projection": total,
            "removed_candidate_indices": EXPECTED_TRIPLES * 47 - total,
        },
        "fixed_projection_integer_unsat": passed and not opened,
        "mandatory_next_mode_if_open": "32-21BL_JOINT_INTEGER_CLOSURE_CHECKPOINT",
        "single_coordinate_extension_after_this_leaf_authorized": False,
        "compact_row_encoding": "[ordinal,r50,r55,r27,r51_lo,r51_hi,r49_lo,r49_hi,r42_lo,r42_hi,r54_lo,r54_hi,r57_lo,r57_hi,r56_lo,r56_hi,r20_lo,r20_hi]",
        "open_rows": compact_open,
        "pruned_rows": [[row["ordinal"], *row["triple"], row["status"]] for row in pruned],
        "r56_formula_mismatch_rows": mismatch,
        "unknown_rows": unknown_rows,
        "shard_sources": sources,
        "interpretation": {
            "pass_includes_independent_r56_formula_threshold_reaudit_on_all_3234_triples": True,
            "this_exhausts_the_predeclared_single_coordinate_sequence": True,
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
        json.dumps({
            "status": payload["status"],
            "canonical": payload["canonical_sha256_without_this_field"],
            "mismatch": len(mismatch),
            "integer_pruned": len(pruned),
            "open": len(opened),
            "unknown": len(unknown_rows),
            "r20_indices": total,
            "fixed_projection_integer_unsat": payload["fixed_projection_integer_unsat"],
            "next_if_open": payload["mandatory_next_mode_if_open"],
        }),
        flush=True,
    )
    if not passed:
        raise SystemExit(1)


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="mode", required=True)
    shard = sub.add_parser("shard")
    for name in (
        "source-lock", "formula-lock", "pair-lock", "audit-lock", "fifth-lock",
        "sixth-lock", "seventh-lock", "eighth-lock", "ninth-lock", "retained", "marking"
    ):
        shard.add_argument("--" + name, type=Path, required=True)
    shard.add_argument("--shard-index", type=int, required=True)
    shard.add_argument("--shard-count", type=int, default=2)
    shard.add_argument("--per-check-timeout-ms", type=int, default=5000)
    shard.add_argument("--output", type=Path, required=True)
    aggregate = sub.add_parser("aggregate")
    aggregate.add_argument("--input-dir", type=Path, required=True)
    aggregate.add_argument("--shard-count", type=int, default=2)
    aggregate.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    run_shard(args) if args.mode == "shard" else run_aggregate(args)


if __name__ == "__main__":
    main()
