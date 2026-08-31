#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

EXPECTED_MANIFEST_SHA256 = "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23"
EXPECTED_PREFLIGHT_SHA256 = "1654ef385558c606623f81bfbaf7c68063141a5be39d9b692d58567f011a6c65"
EXPECTED_AC_CERTIFICATE_SHA256 = "2c227d773aaf6a6543ae89419c468d85fd4ebd42422eb6f4c8ac60b2e7227c8e"
EXPECTED_COARSE_STRATA_BEFORE = 64111
EXPECTED_COARSE_STRATA_ELIMINATED = 3620
EXPECTED_COARSE_STRATA_AFTER = 60491
EXPECTED_AFFECTED_ROWS = 168
EXPECTED_SHARDS = 16
SHARD_SCHEMA = "STAGE32_POST21BL_FULL178_NODE_MASS_CENSUS_SHARD_V1"
SCHEMA = "STAGE32_POST21BL_FULL178_NODE_MASS_CENSUS_AGGREGATE_V1"


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input-dir", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    files = sorted(args.input_dir.rglob("stage32-post21bl-node-mass-shard-*.json"))
    if len(files) != EXPECTED_SHARDS:
        raise ValueError(f"expected {EXPECTED_SHARDS} shard files, got {len(files)}")

    shards: dict[int, dict] = {}
    for path in files:
        payload = json.loads(path.read_text())
        if payload.get("schema") != SHARD_SCHEMA:
            raise ValueError("shard schema mismatch")
        if payload["manifest_canonical_sha256"] != EXPECTED_MANIFEST_SHA256:
            raise ValueError("manifest hash mismatch across shards")
        if payload["node_support_preflight_canonical_sha256"] != EXPECTED_PREFLIGHT_SHA256:
            raise ValueError("node-support preflight mismatch across shards")
        if payload["audited_32_21ac_certificate_sha256"] != EXPECTED_AC_CERTIFICATE_SHA256:
            raise ValueError("audited 21ac certificate mismatch across shards")
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
    rank2_hashes = set()
    node_support_hashes = set()
    shard_certs = []
    shard_decisions = []
    shard_witnesses = []

    coarse_before = coarse_eliminated = coarse_after = affected_rows = 0
    postcut_prior = postcut_cont = postcut_pruned = postcut_survivors = 0
    zero_e = zero_rows = checked_total = 0
    checked_max = 0

    for idx in range(EXPECTED_SHARDS):
        p = shards[idx]
        rank2_hashes.add(p["rank2_model_sha256"])
        node_support_hashes.add(p["node_support_certificate_canonical_sha256"])
        shard_certs.append([idx, p["canonical_sha256_without_this_field"]])
        shard_decisions.append([idx, p["decision_stream_sha256"]])
        shard_witnesses.append([idx, p["surviving_witness_stream_sha256"]])

        coarse_before += int(p["coarse_e_strata_before_cut"])
        coarse_eliminated += int(p["coarse_e_strata_eliminated_by_node_mass_cut"])
        coarse_after += int(p["coarse_e_strata_after_cut"])
        affected_rows += int(p["rows_affected_by_node_mass_cut"])
        postcut_prior += int(p["postcut_image_and_unconstrained_quadratic_slices"])
        postcut_cont += int(p["postcut_exact_continuous_kkt_surviving_slices"])
        postcut_pruned += int(p["postcut_antifixed_coset_pruned_slices"])
        postcut_survivors += int(p["postcut_antifixed_coset_surviving_slices"])
        zero_e += int(p["postcut_zero_e_strata_from_continuous_survivor_population"])
        zero_rows += int(p["postcut_zero_rows_from_continuous_survivor_population"])
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
    if len(node_support_hashes) != 1:
        raise ValueError("node-support certificate mismatch across shards")
    if len(seen_rows) != 178:
        raise ValueError(f"FULL178 row coverage regression: {len(seen_rows)}")
    if coarse_before != EXPECTED_COARSE_STRATA_BEFORE:
        raise ValueError(f"coarse-before regression: {coarse_before}")
    if coarse_eliminated != EXPECTED_COARSE_STRATA_ELIMINATED:
        raise ValueError(f"node-mass elimination regression: {coarse_eliminated}")
    if coarse_after != EXPECTED_COARSE_STRATA_AFTER:
        raise ValueError(f"coarse-after regression: {coarse_after}")
    if affected_rows != EXPECTED_AFFECTED_ROWS:
        raise ValueError(f"affected-row regression: {affected_rows}")
    if coarse_before != coarse_eliminated + coarse_after:
        raise ValueError("coarse accounting regression")
    if postcut_pruned + postcut_survivors != postcut_cont:
        raise ValueError("postcut anti-fixed accounting regression")

    rows.sort(
        key=lambda r: (
            int(r["row_id"].split("-d")[0][1:]),
            int(r["row_id"].split("-d")[1]),
        )
    )
    combined_decision_sha = csha(shard_decisions)
    combined_witness_sha = csha(shard_witnesses)

    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "leaf": "POST_21BL_FULL178_NODE_MASS_CENSUS",
        "mode": "EXACT_16_ROW_SHARD_AGGREGATE_NODE_MASS_CUT_THEN_UNCHANGED_21AD_EVALUATORS",
        "manifest_canonical_sha256": EXPECTED_MANIFEST_SHA256,
        "node_support_preflight_canonical_sha256": EXPECTED_PREFLIGHT_SHA256,
        "node_support_certificate_canonical_sha256": next(iter(node_support_hashes)),
        "audited_32_21ac_certificate_sha256": EXPECTED_AC_CERTIFICATE_SHA256,
        "rank2_model_sha256": next(iter(rank2_hashes)),
        "shard_count": EXPECTED_SHARDS,
        "shard_canonical_sha256s": shard_certs,
        "full_population_row_count": len(seen_rows),
        "node_mass_cut": {
            "formula": "e >= ceil((d-16g+16)/4)",
            "coarse_e_strata_before_cut": coarse_before,
            "coarse_e_strata_eliminated": coarse_eliminated,
            "coarse_e_strata_after_cut": coarse_after,
            "affected_rows": affected_rows,
        },
        "postcut_image_and_unconstrained_quadratic_slices": postcut_prior,
        "postcut_exact_continuous_kkt_surviving_slices": postcut_cont,
        "postcut_antifixed_coset_pruned_slices": postcut_pruned,
        "postcut_antifixed_coset_surviving_slices": postcut_survivors,
        "postcut_zero_e_strata_from_continuous_survivor_population": zero_e,
        "postcut_zero_rows_from_continuous_survivor_population": zero_rows,
        "checked_integer_u_total": checked_total,
        "checked_integer_u_max_per_slice": checked_max,
        "decision_reason_counts": dict(sorted(reason_counts.items())),
        "quotient_coset_population_counts": dict(
            sorted(coset_counts.items(), key=lambda kv: int(kv[0]))
        ),
        "coset_penalty_population_counts": dict(sorted(penalty_counts.items())),
        "combined_shard_decision_stream_sha256": combined_decision_sha,
        "combined_shard_surviving_witness_stream_sha256": combined_witness_sha,
        "row_summaries": rows,
        "semantics": {
            "exact_partition_of_full178_rows": True,
            "node_mass_cut_exact_necessary_for_bijective_normalization_branch": True,
            "node_mass_cut_applied_before_kkt_and_antifixed": True,
            "legacy_21ad_evaluators_used_without_formula_change_after_cut": True,
            "strong_48bit_node_support_not_inferred_from_exceptional_mass": True,
            "old_679337_survivors_materialized": False,
            "terminal_family_materialization_run": False,
            "legacy_prefix_DFS_run": False,
            "anti_fixed_59d_closest_vector_search_run": False,
            "unknown_is_unsat": False,
            "numerical_row_complete": True,
            "bijective_normalization_branch_only": True,
            "multibranch_closed": False,
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
                "verdict": "PASS_STAGE32_POST21BL_FULL178_NODE_MASS_16SHARD_CENSUS",
                "rows": len(seen_rows),
                "coarse_before": coarse_before,
                "coarse_eliminated": coarse_eliminated,
                "coarse_after": coarse_after,
                "affected_rows": affected_rows,
                "postcut_prior_slices": postcut_prior,
                "postcut_continuous_kkt_survivors": postcut_cont,
                "postcut_antifixed_pruned": postcut_pruned,
                "postcut_antifixed_survivors": postcut_survivors,
                "canonical_sha256": payload["canonical_sha256_without_this_field"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
