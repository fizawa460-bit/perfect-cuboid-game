#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

EXPECTED_SHARD_COUNT = 16
EXPECTED_WORKER_BLOB = "546335d44c068a565e715973c886e9980cf85587"
EXPECTED_TARGET_BLOB = "beb6fb487a41f16d783f8762220a175d46ff2620"
EXPECTED_PREFIX_PRODUCER_BLOB = "173ea0c029dbdfc511baecc9138a9613693afa70"
EXPECTED_N356_REVIEW = 5176607630
EXPECTED_N356_HEAD = "0cd222d4824e65ea122bc90ac0d48686ddae38f2"
EXPECTED_N356_STRATA = 17128
EXPECTED_N356_TERMINALS = 65396964990500233636214


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--shard-dir", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    paths = sorted(args.shard_dir.glob("n357-shard-*.json"))
    if len(paths) != EXPECTED_SHARD_COUNT:
        raise ValueError(f"expected {EXPECTED_SHARD_COUNT} shard files, got {len(paths)}")

    shards = [json.loads(p.read_text()) for p in paths]
    indexes = sorted(int(s["shard_index"]) for s in shards)
    if indexes != list(range(EXPECTED_SHARD_COUNT)):
        raise ValueError(f"shard index coverage regression: {indexes}")

    total_groups = None
    total_records_expected = None
    prefix_cache_sha256 = None
    records = []
    for shard in shards:
        if shard.get("schema") != "STAGE32_32_01_178_N357_ALL178_SHARD_V1":
            raise ValueError("N357 shard schema regression")
        if shard.get("status") != "RESEARCH_SHARD_NO_MAIN_CREDIT":
            raise ValueError("N357 shard status regression")
        if shard.get("shard_count") != EXPECTED_SHARD_COUNT:
            raise ValueError("N357 shard-count regression")
        if shard.get("worker_blob_sha1") != EXPECTED_WORKER_BLOB:
            raise ValueError("N357 shard worker source-lock regression")
        if shard.get("target_blob_sha1") != EXPECTED_TARGET_BLOB:
            raise ValueError("N357 target source-lock regression")
        if shard.get("prefix_producer_blob_sha1") != EXPECTED_PREFIX_PRODUCER_BLOB:
            raise ValueError("N357 prefix producer source-lock regression")
        if shard.get("main_pruning_credit") is not False:
            raise ValueError("N357 shard must not self-promote MAIN credit")
        if prefix_cache_sha256 is None:
            prefix_cache_sha256 = shard.get("prefix_cache_sha256")
        elif prefix_cache_sha256 != shard.get("prefix_cache_sha256"):
            raise ValueError("N357 shard prefix-cache disagreement")
        if total_groups is None:
            total_groups = int(shard["structural_group_count_total"])
            total_records_expected = int(shard["structural_record_count_total"])
        elif total_groups != int(shard["structural_group_count_total"]) or total_records_expected != int(shard["structural_record_count_total"]):
            raise ValueError("N357 shard structural-total disagreement")
        records.extend(shard["records"])

    if not prefix_cache_sha256:
        raise ValueError("N357 prefix cache digest missing")
    if sum(int(s["shard_group_count"]) for s in shards) != total_groups:
        raise ValueError("N357 shard group partition regression")
    if len(records) != total_records_expected:
        raise ValueError("N357 shard record partition regression")

    ids = [(r["row_id"], int(r["g"]), int(r["d"]), int(r["e"])) for r in records]
    if len(ids) != len(set(ids)):
        raise ValueError("N357 duplicate stratum record across shards")

    source_terminals = sum(int(r["n356_transport_remaining_terminals"]) for r in records)
    source_strata = sum(int(r["n356_transport_remaining_terminals"]) > 0 for r in records)
    rejected = sum(int(r["n357_support_capacity_rejected_terminals"]) for r in records)
    remaining = sum(int(r["n357_support_capacity_remaining_terminals"]) for r in records)
    remaining_strata = sum(int(r["n357_support_capacity_remaining_terminals"]) > 0 for r in records)
    affected_strata = sum(int(r["n357_support_capacity_rejected_terminals"]) > 0 for r in records)

    if source_strata != EXPECTED_N356_STRATA:
        raise ValueError(f"N356 source-strata replay regression {source_strata}")
    if source_terminals != EXPECTED_N356_TERMINALS:
        raise ValueError(f"N356 source-terminal replay regression {source_terminals}")
    if rejected <= 0:
        raise ValueError("N357 all178 support-capacity cut is not incrementally strict")
    if source_terminals - rejected != remaining:
        raise ValueError("N357 partition identity regression")

    stream = hashlib.sha256()
    for rec in sorted(records, key=lambda r: (r["g"], r["d"], r["e"], r["row_id"])):
        stream.update(json.dumps(rec, sort_keys=True, separators=(",", ":")).encode() + b"\n")

    result = {
        "schema": "STAGE32_32_01_178_N357_ALL178_SUPPORT_SUFFIX_CAPACITY_CENSUS_V1",
        "node_id": "N357",
        "status": "RESEARCH_CANDIDATE_ALL178_N357_NO_MAIN_CREDIT",
        "audited_input": {
            "node": "N356",
            "review_id": EXPECTED_N356_REVIEW,
            "audited_exact_head": EXPECTED_N356_HEAD,
            "remaining_strata": EXPECTED_N356_STRATA,
            "remaining_terminals": EXPECTED_N356_TERMINALS,
        },
        "necessary_condition": "s + min(e-M,Srem) >= K",
        "aggregate": {
            "source_strata_replayed": source_strata,
            "source_terminals_replayed": source_terminals,
            "affected_strata": affected_strata,
            "candidate_incremental_rejected_terminals": rejected,
            "candidate_remaining_strata": remaining_strata,
            "candidate_remaining_terminals": remaining,
            "per_stratum_stream_sha256": stream.hexdigest(),
        },
        "verification": {
            "full178_rows": 178,
            "structural_strata_replayed": len(records),
            "structural_group_count": total_groups,
            "n356_authority_replayed_exactly": True,
            "partition_identity": True,
            "shard_count": EXPECTED_SHARD_COUNT,
            "worker_blob_sha1": EXPECTED_WORKER_BLOB,
            "target_blob_sha1": EXPECTED_TARGET_BLOB,
            "prefix_producer_blob_sha1": EXPECTED_PREFIX_PRODUCER_BLOB,
            "prefix_cache_sha256": prefix_cache_sha256,
        },
        "semantics": {
            "main_pruning_credit": False,
            "external_hostile_audit_required_before_credit": True,
            "full178_complete": False,
            "n350_producer_registered": False,
            "production_complete": False,
            "n104_release": False,
            "receiver_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "stage32_closed": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
            "heavy_compute_authorized": False,
            "merge_authorized": False,
        },
    }
    result["canonical_sha256_without_this_field"] = csha(result)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": "PASS_N357_ALL178_SUPPORT_SUFFIX_CAPACITY_CANDIDATE",
        "source_strata": source_strata,
        "source_terminals": source_terminals,
        "affected_strata": affected_strata,
        "incremental_rejected_terminals": rejected,
        "remaining_strata": remaining_strata,
        "remaining_terminals": remaining,
        "prefix_cache_sha256": prefix_cache_sha256,
        "stream": stream.hexdigest(),
        "canonical": result["canonical_sha256_without_this_field"],
        "main_credit": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
