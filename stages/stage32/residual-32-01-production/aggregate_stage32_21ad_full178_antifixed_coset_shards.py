#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

EXPECTED_MANIFEST_SHA256 = "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23"
EXPECTED_AC_CERTIFICATE_SHA256 = "2c227d773aaf6a6543ae89419c468d85fd4ebd42422eb6f4c8ac60b2e7227c8e"
EXPECTED_PRIOR_SLICES = 2018569
EXPECTED_CONTINUOUS_KKT_SURVIVORS = 679337
EXPECTED_SHARDS = 16
SCHEMA = "STAGE32_21AD_FULL178_ANTIFIXED_COSET_PARALLEL_AGGREGATE_V1"


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input-dir", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    files = sorted(args.input_dir.rglob("stage32-21ad-shard-*.json"))
    if len(files) != EXPECTED_SHARDS:
        raise ValueError(f"expected {EXPECTED_SHARDS} shard files, got {len(files)}")

    shards: dict[int, dict] = {}
    for path in files:
        payload = json.loads(path.read_text())
        if payload["manifest_canonical_sha256"] != EXPECTED_MANIFEST_SHA256:
            raise ValueError("manifest hash mismatch across shards")
        if payload["audited_32_21ac_certificate_sha256"] != EXPECTED_AC_CERTIFICATE_SHA256:
            raise ValueError("audited ac certificate mismatch across shards")
        if payload["row_shards"] != EXPECTED_SHARDS or payload["full_run"] is not False:
            raise ValueError("invalid shard geometry")
        idx = int(payload["shard_index"])
        if idx in shards:
            raise ValueError(f"duplicate shard index {idx}")
        shards[idx] = payload
    if set(shards) != set(range(EXPECTED_SHARDS)):
        raise ValueError("shard index coverage regression")

    rows: list[dict] = []
    seen_rows: set[str] = set()
    reason_counts: Counter[str] = Counter()
    coset_counts: Counter[str] = Counter()
    penalty_counts: Counter[str] = Counter()
    prior = cont = pruned = survivors = zero_e = zero_rows = checked_total = 0
    checked_max = 0
    rank2_hashes = set()
    shard_certs = []
    shard_decisions = []
    shard_witnesses = []

    for idx in range(EXPECTED_SHARDS):
        p = shards[idx]
        rank2_hashes.add(p["rank2_model_sha256"])
        shard_certs.append([idx, p["canonical_sha256_without_this_field"]])
        shard_decisions.append([idx, p["decision_stream_sha256"]])
        shard_witnesses.append([idx, p["surviving_witness_stream_sha256"]])
        prior += int(p["prior_image_and_unconstrained_quadratic_slices"])
        cont += int(p["exact_continuous_kkt_surviving_slices"])
        pruned += int(p["antifixed_coset_pruned_slices"])
        survivors += int(p["antifixed_coset_surviving_slices"])
        zero_e += int(p["zero_e_strata_from_continuous_survivor_population"])
        zero_rows += int(p["zero_rows_from_continuous_survivor_population"])
        checked_total += int(p["checked_integer_u_total"])
        checked_max = max(checked_max, int(p["checked_integer_u_max_per_slice"]))
        reason_counts.update({k: int(v) for k, v in p["decision_reason_counts"].items()})
        coset_counts.update({k: int(v) for k, v in p["quotient_coset_population_counts"].items()})
        penalty_counts.update({k: int(v) for k, v in p["coset_penalty_population_counts"].items()})
        for row in p["row_summaries"]:
            row_id = row["row_id"]
            if row_id in seen_rows:
                raise ValueError(f"duplicate row {row_id}")
            seen_rows.add(row_id)
            rows.append(row)

    if len(rank2_hashes) != 1:
        raise ValueError("rank2 model hash mismatch across shards")
    if len(seen_rows) != 178:
        raise ValueError(f"FULL178 row coverage regression: {len(seen_rows)}")
    if prior != EXPECTED_PRIOR_SLICES:
        raise ValueError(f"prior slice regression: {prior}")
    if cont != EXPECTED_CONTINUOUS_KKT_SURVIVORS:
        raise ValueError(f"continuous KKT survivor regression: {cont}")
    if pruned + survivors != cont:
        raise ValueError("anti-fixed census accounting regression")

    rows.sort(key=lambda r: (int(r["row_id"].split("-d")[0][1:]), int(r["row_id"].split("-d")[1])))
    combined_decision_sha = csha(shard_decisions)
    combined_witness_sha = csha(shard_witnesses)

    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "leaf": "32-21ad",
        "mode": "EXACT_16_ROW_SHARD_AGGREGATE_OF_AUDITED_32_21AC_ANTIFIXED_COSET_BOUND",
        "manifest_canonical_sha256": EXPECTED_MANIFEST_SHA256,
        "audited_32_21ac_certificate_sha256": EXPECTED_AC_CERTIFICATE_SHA256,
        "rank2_model_sha256": next(iter(rank2_hashes)),
        "shard_count": EXPECTED_SHARDS,
        "shard_canonical_sha256s": shard_certs,
        "full_population_row_count": len(seen_rows),
        "prior_image_and_unconstrained_quadratic_slices": prior,
        "exact_continuous_kkt_surviving_slices": cont,
        "antifixed_coset_pruned_slices": pruned,
        "antifixed_coset_surviving_slices": survivors,
        "zero_e_strata_from_continuous_survivor_population": zero_e,
        "zero_rows_from_continuous_survivor_population": zero_rows,
        "checked_integer_u_total": checked_total,
        "checked_integer_u_max_per_slice": checked_max,
        "decision_reason_counts": dict(sorted(reason_counts.items())),
        "quotient_coset_population_counts": dict(sorted(coset_counts.items(), key=lambda kv: int(kv[0]))),
        "coset_penalty_population_counts": dict(sorted(penalty_counts.items())),
        "combined_shard_decision_stream_sha256": combined_decision_sha,
        "combined_shard_surviving_witness_stream_sha256": combined_witness_sha,
        "row_summaries": rows,
        "semantics": {
            "exact_partition_of_full178_rows": True,
            "continuous_kkt_problem_exact_under_stabilizer_averaging": True,
            "audited_32_21ac_evaluator_used_without_formula_change": True,
            "antifixed_coset_false_decision_safe_for_original_integral_picard_slice": True,
            "antifixed_coset_true_decision_only_necessary_condition": True,
            "terminal_family_materialization_run": False,
            "legacy_prefix_DFS_run": False,
            "anti_fixed_59d_closest_vector_search_run": False,
            "unknown_is_unsat": False,
            "numerical_row_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False
        }
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": "PASS_STAGE32_21AD_FULL178_16SHARD_ANTIFIXED_COSET_NUMERICAL_CENSUS",
        "prior_slices": prior,
        "continuous_kkt_survivors": cont,
        "antifixed_pruned": pruned,
        "antifixed_survivors": survivors,
        "zero_e_strata": zero_e,
        "zero_rows": zero_rows,
        "checked_u_total": checked_total,
        "checked_u_max": checked_max,
        "canonical_sha256": payload["canonical_sha256_without_this_field"]
    }, sort_keys=True))


if __name__ == "__main__":
    main()
