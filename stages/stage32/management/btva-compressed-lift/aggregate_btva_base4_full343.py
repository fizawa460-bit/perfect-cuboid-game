#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

SHARD_COUNT = 8
BASE4_COUNT = 343
X4_VALUES = 113
TERMINAL_MASS = 1278934
AUTHORITY_BOUND = "157570677819451133507"
SHARD_SCHEMA = "STAGE32_MAIN_BTVA_BASE4_FULL343_SHARD_V1"


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def load_shard(path: Path) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    stored = obj.get("canonical_sha256_without_this_field")
    req(isinstance(stored, str), f"missing canonical {path}")
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    req(csha(body) == stored, f"canonical drift {path}")
    req(obj.get("schema") == SHARD_SCHEMA, f"schema drift {path}")
    req(obj["status"] == "EXACT_SHARD_COMPLETE_ZERO_CREDIT", f"status drift {path}")
    return obj


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input-dir", type=Path, action="append", required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    files = []
    for root in args.input_dir:
        if root.is_dir():
            files.extend(sorted(root.rglob("btva-base4-full343-shard-*.json")))
    req(files, "no shard files")

    by_shard: dict[int, tuple[Path, dict]] = {}
    source_lock = None
    solver_timeout = None
    max_flat_cuts = None

    for path in files:
        obj = load_shard(path)
        ex = obj["execution"]
        shard = int(ex["shard_index"])
        req(int(ex["shard_count"]) == SHARD_COUNT, "shard-count drift")
        req(shard not in by_shard, f"duplicate shard {shard}")
        req(0 <= shard < SHARD_COUNT, f"bad shard {shard}")
        req(ex["partition_rule"] == "sorted_base4_global_index_mod_shard_count",
            "partition-rule drift")
        if source_lock is None:
            source_lock = obj["source_locks"]
            solver_timeout = int(ex["solver_timeout_ms"])
            max_flat_cuts = int(ex["max_flat_cuts"])
        else:
            req(obj["source_locks"] == source_lock, "cross-shard source-lock drift")
            req(int(ex["solver_timeout_ms"]) == solver_timeout, "solver timeout drift")
            req(int(ex["max_flat_cuts"]) == max_flat_cuts, "flat-cut drift")

        target = obj["target"]
        req(target["row_id"] == "g0-d008", "row-id drift")
        req(int(target["base4_total_population"]) == BASE4_COUNT, "base4 count drift")
        req(int(target["x4_values_per_base4"]) == X4_VALUES, "x4 count drift")
        req(int(target["terminal_total_population"]) == TERMINAL_MASS, "terminal mass drift")
        for k, v in obj["firewalls"].items():
            req(v is False, f"shard firewall {k}")
        by_shard[shard] = (path, obj)

    req(set(by_shard) == set(range(SHARD_COUNT)),
        f"missing shards: {sorted(set(range(SHARD_COUNT)) - set(by_shard))}")

    row_map: dict[int, dict] = {}
    shard_digests = []
    for shard in range(SHARD_COUNT):
        path, obj = by_shard[shard]
        ex = obj["execution"]
        expected = list(range(shard, BASE4_COUNT, SHARD_COUNT))
        req(ex["expected_global_indices"] == expected, f"shard {shard} expected-index drift")
        rows = obj["rows"]
        req([int(r["global_base4_index"]) for r in rows] == expected,
            f"shard {shard} row-index drift")
        req(int(obj["summary"]["key_count"]) == len(rows), f"shard {shard} summary count")
        for row in rows:
            idx = int(row["global_base4_index"])
            req(idx not in row_map, f"duplicate global row {idx}")
            req(idx % SHARD_COUNT == shard, f"partition violation row {idx}")
            req(row["result"] in {
                "UNSAT_BASE4_BTVA_EFFECTIVE_PAIRING_FIBER",
                "SAT_BTVA_COMPATIBLE_BASE4_LIFT",
                "UNKNOWN",
            }, f"unexpected result row {idx}")
            m = int(row["exceptional_multiplicity_per_x4"])
            req(m > 0, f"nonpositive multiplicity row {idx}")
            req(int(row["terminal_mass_covered_if_unsat"]) == m * X4_VALUES,
                f"mass replay row {idx}")
            row_map[idx] = row
        shard_digests.append({
            "shard_index": shard,
            "canonical_sha256": obj["canonical_sha256_without_this_field"],
            "filename": path.name,
        })

    req(set(row_map) == set(range(BASE4_COUNT)), "global 343-row coverage gap/overlap")

    rows = [row_map[i] for i in range(BASE4_COUNT)]
    unsat = [r for r in rows if r["result"] == "UNSAT_BASE4_BTVA_EFFECTIVE_PAIRING_FIBER"]
    satrows = [r for r in rows if r["result"] == "SAT_BTVA_COMPATIBLE_BASE4_LIFT"]
    unknown = [r for r in rows if r["result"] == "UNKNOWN"]

    total_terminal_mass = sum(
        int(r["exceptional_multiplicity_per_x4"]) * X4_VALUES for r in rows
    )
    req(total_terminal_mass == TERMINAL_MASS, "global terminal mass conservation")

    eliminated_mass = sum(int(r["terminal_mass_covered_if_unsat"]) for r in unsat)
    survivor_mass = sum(
        int(r["exceptional_multiplicity_per_x4"]) * X4_VALUES
        for r in rows if r["result"] != "UNSAT_BASE4_BTVA_EFFECTIVE_PAIRING_FIBER"
    )
    req(eliminated_mass + survivor_mass == TERMINAL_MASS,
        "UNSAT/survivor mass partition drift")

    survivor_rows = [{
        "global_base4_index": int(r["global_base4_index"]),
        "base4": r["base4"],
        "exceptional_multiplicity_per_x4": int(r["exceptional_multiplicity_per_x4"]),
        "status": r["result"],
        "reason_unknown": r.get("reason_unknown"),
        "compatible_support": r.get("compatible_support"),
        "terminal_mass": int(r["exceptional_multiplicity_per_x4"]) * X4_VALUES,
    } for r in rows if r["result"] != "UNSAT_BASE4_BTVA_EFFECTIVE_PAIRING_FIBER"]

    payload = {
        "schema": "STAGE32_MAIN_BTVA_BASE4_FULL343_AGGREGATE_V1",
        "stage": 32,
        "route": "BTVA_COMPRESSED_PICARD_LIFT_RECEIVER_INTERSECTION",
        "status": "FULL343_EXECUTION_AGGREGATED_ZERO_CREDIT",
        "authority_snapshot": {
            "authoritative_remaining_terminals": AUTHORITY_BOUND,
            "semantics": "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET",
            "authority_changed_by_this_result": False,
        },
        "source_locks": source_lock,
        "execution": {
            "shard_count": SHARD_COUNT,
            "solver_timeout_ms": solver_timeout,
            "max_flat_cuts": max_flat_cuts,
            "shard_digests": shard_digests,
            "coverage_rule": "global_base4_indices_0_through_342_exactly_once",
            "coverage_complete": True,
        },
        "population": {
            "row_id": "g0-d008",
            "base4_key_count": BASE4_COUNT,
            "x4_values_per_base4": X4_VALUES,
            "static7_key_count": BASE4_COUNT * X4_VALUES,
            "terminal_mass": TERMINAL_MASS,
        },
        "summary": {
            "unsat_base4_fibers": len(unsat),
            "compatible_sat_base4_fibers": len(satrows),
            "unknown_base4_fibers": len(unknown),
            "static7_keys_covered_by_unsat_fibers": len(unsat) * X4_VALUES,
            "terminal_mass_covered_by_unsat_fibers": eliminated_mass,
            "survivor_terminal_mass": survivor_mass,
        },
        "survivor_rows": survivor_rows,
        "firewalls": {
            "bounded_solver_timeout_means_unknown_is_not_unsat": True,
            "known_32_plane_conics_closed": False,
            "all140_effective_pairing_semantics_promoted": False,
            "main_pruning_credit": False,
            "receiver_credit": False,
            "effectivity_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "full178_complete": False,
            "stage32_closed": False,
            "merge_authorized": False,
        },
        "next_exact_step":
            "Close the d=8 plane-conic exception and effective-pairing receiver semantics; then rescue UNKNOWN/SAT survivor fibers with longer exact runs or per-x4 fallback before any MAIN numerical promotion.",
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("BTVA_FULL343_AGGREGATE_SUMMARY=" + json.dumps(payload["summary"], sort_keys=True))
    print("BTVA_FULL343_AGGREGATE_CANONICAL=" + payload["canonical_sha256_without_this_field"])


if __name__ == "__main__":
    main()
