#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
WORKER = HERE / "run_row_shard.py"
WORKER_BLOB = "380c191b7dd3bcc6c1e290495c776203d4a92b63"
PRODUCER_BLOB = "837d647cfcbc96bbe384e564f449cd7042a46d48"
SCHEMA = "STAGE32EX5_HPADJ20_PARALLEL_UNION_V1"
Q_BENCHMARK = 195603649074545538415
HPADJ15_BENCHMARK = 426398981823116026011


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def load_worker():
    req(WORKER.is_file() and git_blob(WORKER) == WORKER_BLOB, "HPADJ20 row-shard worker blob drift")
    spec = importlib.util.spec_from_file_location("hpadj20_row_shard_locked_for_union", WORKER)
    req(spec is not None and spec.loader is not None, "cannot load HPADJ20 row-shard worker")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    req(mod.PRODUCER_BLOB == PRODUCER_BLOB, "worker producer lock drift")
    return mod


def frac(totals: dict, prefix: str) -> Fraction:
    return Fraction(
        int(totals[prefix + "_numerator"]),
        int(totals[prefix + "_denominator"]),
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cert-dir", type=Path, required=True)
    ap.add_argument("--shard-count", type=int, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    req(args.shard_count > 0, "shard_count must be positive")

    worker = load_worker()
    certs = []
    for shard_index in range(args.shard_count):
        candidates = sorted(args.cert_dir.glob(f"**/hpadj20-shard-{shard_index}.json"))
        req(len(candidates) == 1, f"expected exactly one certificate for shard {shard_index}, got {len(candidates)}")
        certs.append(worker.cheap_validate_certificate(candidates[0], shard_index, args.shard_count))

    # Reconstruct the exact current partition from the source-locked mathematical context.
    (
        p20, _h19, h18, _h17, _h16, _cells, p14, _counter, rows, _BC, _profiles, profile_meta
    ) = worker.load_context()
    buckets, loads = worker.deterministic_partition(rows, args.shard_count)
    expected_row_indices = set(range(len(rows)))
    seen_row_indices = set()
    seen_assignment_digests = set()
    profile_ref = None

    total_obj = Fraction(0, 1)
    parent_total_obj = Fraction(0, 1)
    cell_floor_sum = 0
    parent_cell_floor_sum = 0
    total_pre_terms = 0
    total_pre_blocks = 0
    positive_q_capacity = 0
    parent_positive_q_capacity = 0
    nonzero_post_cells = 0
    strict_survivor_tiers = 0
    strict_cell_count = 0
    diagnostic_rows = []
    shard_canonicals = []

    for shard_index, data in enumerate(certs):
        expected_rows = [list(x) for x in buckets[shard_index]]
        req(data["assignment"]["rows"] == expected_rows, f"shard {shard_index} assignment differs from deterministic current partition")
        req(int(data["assignment"]["estimated_weight"]) == int(loads[shard_index]), f"shard {shard_index} weight drift")
        req(data["assignment"]["sha256"] not in seen_assignment_digests, "duplicate shard assignment digest")
        seen_assignment_digests.add(data["assignment"]["sha256"])
        for row in expected_rows:
            row_index = int(row[0])
            req(row_index not in seen_row_indices, f"duplicate FULL178 row index {row_index}")
            seen_row_indices.add(row_index)

        locks = data["source_locks"]
        req(locks["hpadj20_producer_git_blob"] == PRODUCER_BLOB, "producer source lock drift")
        req(locks["full178_manifest_blob_sha1"] == p14.LOCKS["manifest_blob"], "FULL178 manifest lock drift")
        req(locks["hpadj10_counter_blob_sha1"] == p14.LOCKS["hpadj10_counter_blob"], "counter lock drift")
        if profile_ref is None:
            profile_ref = data["profile"]
        req(data["profile"] == profile_ref, "global qA profile metadata drift across shards")

        totals = data["totals"]
        parent_total_obj += frac(totals, "hpadj19_replay_rational_objective")
        total_obj += frac(totals, "hpadj20_rational_objective")
        parent_cell_floor_sum += int(totals["hpadj19_replay_cellwise_integer_floor_sum"])
        cell_floor_sum += int(totals["hpadj20_cellwise_integer_floor_sum"])
        total_pre_terms += int(totals["pre_hpadj08_exact_terminal_mass"])
        total_pre_blocks += int(totals["pre_hpadj08_exact_block_mass"])
        parent_positive_q_capacity += int(totals["hpadj19_replay_positive_q_terminal_capacity"])
        positive_q_capacity += int(totals["hpadj20_positive_q_terminal_capacity"])
        nonzero_post_cells += int(totals["nonzero_post_mass_cells"])
        strict_survivor_tiers += int(totals["strict_survivor_tier_instances"])
        strict_cell_count += int(totals["strict_lp_cell_count"])
        diagnostic_rows.extend(data["diagnostic_records"])
        shard_canonicals.append(data["canonical_sha256_without_this_field"])

    req(seen_row_indices == expected_row_indices, "FULL178 union has row gaps or extras")
    req(len(seen_assignment_digests) == args.shard_count, "assignment digest cardinality drift")
    req(total_pre_terms == p14.EXPECTED_PRE_TERMS, "parallel union exact pre terminal aggregate drift")
    req(total_pre_blocks == p14.EXPECTED_PRE_BLOCKS, "parallel union exact pre block aggregate drift")
    req(cell_floor_sum <= parent_cell_floor_sum, "parallel union weakened HPADJ19 replay")
    req(cell_floor_sum <= Q_BENCHMARK, "parallel union weakened MAIN q benchmark")
    req(cell_floor_sum <= HPADJ15_BENCHMARK, "parallel union weakened HPADJ15 benchmark")
    req(strict_survivor_tiers > 0 and strict_cell_count > 0, "parallel union has no strict refinement")

    diagnostic_rows.sort(key=lambda x: (int(x["row_index"]), int(x["interval_position"])))
    req(len(diagnostic_rows) == len(rows) * len(h18.PLANNED), "diagnostic cell coverage drift")
    diag = hashlib.sha256()
    seen_diag = set()
    for item in diagnostic_rows:
        key = (int(item["row_index"]), int(item["interval_position"]))
        req(key not in seen_diag, f"duplicate diagnostic cell {key}")
        seen_diag.add(key)
        diag.update(json.dumps(item["record"], sort_keys=True, separators=(",", ":")).encode() + b"\n")

    global_floor = total_obj.numerator // total_obj.denominator
    parent_global_floor = parent_total_obj.numerator // parent_total_obj.denominator
    req(cell_floor_sum <= global_floor, "parallel HPADJ20 cellwise floor direction drift")
    req(parent_cell_floor_sum <= parent_global_floor, "parallel HPADJ19 cellwise floor direction drift")

    hist_classes, strict_profile_classes, nonminimum_tuples = profile_meta
    req(profile_ref == {
        "exact_histogram_class_count": hist_classes,
        "strict_two_tier_class_count": strict_profile_classes,
        "nonminimum_tuple_count_in_full_H96_profile": nonminimum_tuples,
    }, "profile metadata differs from source-locked recomputation")

    out = {
        "schema": SCHEMA,
        "route_id": "HPADJ-20_ex5",
        "status": "Q_QUADRATIC_QA_TWO_TIER_PARALLEL_EXACT_UNION_CANDIDATE_HOSTILE_AUDIT_REQUIRED",
        "source_locks": {
            "hpadj20_producer_git_blob": PRODUCER_BLOB,
            "row_shard_worker_git_blob": WORKER_BLOB,
            "union_aggregator_git_blob": git_blob(Path(__file__)),
            "hpadj19_parent_blob_sha1": p20.PARENT_BLOB,
            "full178_manifest_blob_sha1": p14.LOCKS["manifest_blob"],
            "hpadj10_counter_blob_sha1": p14.LOCKS["hpadj10_counter_blob"],
        },
        "partition": {
            "shard_count": args.shard_count,
            "full178_rows": len(rows),
            "strategy": "DETERMINISTIC_GREEDY_FULL178_ROW_WEIGHT_HPLUS1_CUBED",
            "exact_disjoint_union_verified": True,
            "row_gap_count": 0,
            "row_overlap_count": 0,
            "shard_canonical_sha256": shard_canonicals,
        },
        "qA_refinement": {
            **profile_ref,
            "strict_survivor_tier_instances": strict_survivor_tiers,
            "strict_lp_cell_count": strict_cell_count,
        },
        "exact_population_adapter": {
            "full178_rows": len(rows),
            "historical_b_shards": len(h18.PLANNED),
            "row_shard_cells": len(rows) * len(h18.PLANNED),
            "nonzero_post_mass_cells": nonzero_post_cells,
            "pre_hpadj08_exact_terminal_mass": total_pre_terms,
            "pre_hpadj08_exact_block_mass": total_pre_blocks,
            "post_hpadj08_x4_complete_survivor_mass": p14.EXPECTED_SURVIVOR_ENVELOPE,
            "A_ordered_triple_population_preserved_exactly": True,
        },
        "optimization": {
            "hpadj19_replay_positive_q_terminal_capacity": parent_positive_q_capacity,
            "hpadj20_positive_q_terminal_capacity": positive_q_capacity,
            "hpadj19_replay_rational_objective_numerator": parent_total_obj.numerator,
            "hpadj19_replay_rational_objective_denominator": parent_total_obj.denominator,
            "hpadj20_rational_objective_numerator": total_obj.numerator,
            "hpadj20_rational_objective_denominator": total_obj.denominator,
            "hpadj19_replay_aggregate_rational_floor": parent_global_floor,
            "hpadj20_aggregate_rational_floor": global_floor,
            "hpadj19_replay_cellwise_integer_floor_sum": parent_cell_floor_sum,
            "hpadj20_cellwise_integer_floor_sum": cell_floor_sum,
            "diagnostic_stream_sha256": diag.hexdigest(),
        },
        "candidate_bound": {
            "main_q_quadratic_global_candidate_upper_bound": Q_BENCHMARK,
            "hpadj15_candidate_upper_bound": HPADJ15_BENCHMARK,
            "replayed_hpadj19_candidate_upper_bound": parent_cell_floor_sum,
            "hpadj20_candidate_upper_bound": cell_floor_sum,
            "improvement_vs_hpadj19_replay": parent_cell_floor_sum - cell_floor_sum,
            "improvement_vs_main_q_quadratic_global": Q_BENCHMARK - cell_floor_sum,
            "improvement_vs_hpadj15": HPADJ15_BENCHMARK - cell_floor_sum,
            "strict_improvement_vs_hpadj19_replay": cell_floor_sum < parent_cell_floor_sum,
            "structurally_no_weaker_than_hpadj19": True,
            "composition_if_consumed": "DIRECT_REFINEMENT_OF_SAME_POPULATION_LP__NO_ADDITIVE_SUBTRACTION",
        },
        "resume_evidence": {
            "completed_shards_are_individually_source_locked_and_canonical": True,
            "carry_over_requires_same_worker_producer_partition_and_shard_count": True,
            "recompute_only_missing_or_rejected_shards": True,
        },
        "semantics": {
            "same_hpadj08_td01_x4_complete_population": True,
            "row_partition_changes_mathematical_population": False,
            "statistical_independence_assumed": False,
            "additive_subtraction_used": False,
            "main_consumption_performed": False,
            "hostile_audit_required_before_main_handoff_or_consumption": True,
        },
        "firewalls": {
            "stage32_main_pruning_credit": False,
            "current_main_incremental_credit": False,
            "full178_complete": False,
            "effectivity_credit": False,
            "receiver_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_credit": False,
            "merge_authorized": False,
        },
    }
    out["canonical_sha256_without_this_field"] = canonical(out)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n")
    print("HPADJ20_PARALLEL_UNION_CANONICAL=" + out["canonical_sha256_without_this_field"])
    print("HPADJ20_HPADJ19_REPLAY_UPPER=" + str(parent_cell_floor_sum))
    print("HPADJ20_UPPER=" + str(cell_floor_sum))
    print("HPADJ20_IMPROVEMENT_VS_HPADJ19=" + str(parent_cell_floor_sum - cell_floor_sum))
    print("HPADJ20_IMPROVEMENT_VS_MAIN_Q=" + str(Q_BENCHMARK - cell_floor_sum))
    print("HPADJ20_DIAGNOSTIC_STREAM_SHA256=" + diag.hexdigest())


if __name__ == "__main__":
    main()
