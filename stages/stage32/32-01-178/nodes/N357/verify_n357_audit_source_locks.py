#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]

LOCKS = {
    "contract": (
        ROOT / "stages/stage32/32-01-178/nodes/N357/TRANSPORT_SUPPORT_CAPACITY_CONTRACT.md",
        "be35e28b0e0f21ea0e3e0135d3515acaaa06f3bd",
    ),
    "result": (
        ROOT / "stages/stage32/32-01-178/nodes/N357/RESULT.json",
        "50014d453266ad79101910a943d14388bd3ef6ec",
    ),
    "prefix_producer": (
        ROOT / "stages/stage32/32-01-178/nodes/N357/prepare_n357_all178_prefix_cache.py",
        "2b04166a863383bdd5e6eeccc01998dd173e40d3",
    ),
    "deterministic_worker": (
        ROOT / "stages/stage32/32-01-178/nodes/N357/verify_n357_all178_support_capacity_shard_deterministic.py",
        "cf6cf60d557f05268ea063f6d8bc7bc24fad1f8c",
    ),
    "canonical_worker": (
        ROOT / "stages/stage32/32-01-178/nodes/N357/verify_n357_all178_support_capacity_shard_canonical.py",
        "81bcbab9bb49d4ac1f8be28c038f25ae3a469ab8",
    ),
    "all178_target": (
        ROOT / "stages/stage32/32-01-178/nodes/N357/verify_n357_all178_support_capacity_census.py",
        "beb6fb487a41f16d783f8762220a175d46ff2620",
    ),
    "aggregate_base": (
        ROOT / "stages/stage32/32-01-178/nodes/N357/aggregate_n357_all178_support_capacity_shards.py",
        "f9bbfc2739629c302d00a4d8d3974be3a30b52b7",
    ),
    "aggregate_wrapper": (
        ROOT / "stages/stage32/32-01-178/nodes/N357/aggregate_n357_all178_support_capacity_canonical_shards.py",
        "3b20ea11af78e210f9bb615bd164082c56d9239c",
    ),
    "n356_audit_receipt": (
        ROOT / "stages/stage32/32-01-178/nodes/N356/HOSTILE-AUDIT-PASS.json",
        "4966d57f61624c1cfd313ae5d1fe5e33bb25e569",
    ),
    "workflow": (
        ROOT / ".github/workflows/stage32-01-178-n356-optimistic-exceptional-transport.yml",
        "c616cad5d0ed8d6d9e2ca5bdcd57db0b89d31c84",
    ),
}

EXPECTED_CANONICAL = "0718c1f8f92a6d18e99e82b4adcbe1efe66a0daa47347284cbc6f42e6f0dac53"
EXPECTED_STREAM = "62c863cdbf3b18f34dbd0d95ea0c1980f361992b8ecec54a70f22efc33ff6d7b"
EXPECTED_SOURCE_STRATA = 17128
EXPECTED_SOURCE_TERMINALS = 65396964990500233636214
EXPECTED_REJECTED = 17797986705435299826016
EXPECTED_REMAINING_STRATA = 17128
EXPECTED_REMAINING = 47598978285064933810198
EXPECTED_PREFIX_CACHE = "5e6704bebc5118957bfbc42fbd30a9dc539f773231e6d22efc6f30a44e39acc5"


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical_sha256_without_field(obj: dict) -> str:
    payload = dict(obj)
    payload.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def main() -> None:
    for name, (path, expected) in LOCKS.items():
        actual = git_blob_sha1(path)
        if actual != expected:
            raise ValueError(f"{name} source-lock regression: {actual} != {expected}")

    result_path = ROOT / "stages/stage32/32-01-178/nodes/N357/RESULT.json"
    result = json.loads(result_path.read_text())
    if canonical_sha256_without_field(result) != EXPECTED_CANONICAL:
        raise ValueError("N357 RESULT canonical regression")
    if result.get("canonical_sha256_without_this_field") != EXPECTED_CANONICAL:
        raise ValueError("N357 RESULT self-canonical regression")
    agg = result["aggregate"]
    if int(agg["source_strata_replayed"]) != EXPECTED_SOURCE_STRATA:
        raise ValueError("N357 source strata regression")
    if int(agg["source_terminals_replayed"]) != EXPECTED_SOURCE_TERMINALS:
        raise ValueError("N357 source terminals regression")
    if int(agg["candidate_incremental_rejected_terminals"]) != EXPECTED_REJECTED:
        raise ValueError("N357 rejected-terminals regression")
    if int(agg["candidate_remaining_strata"]) != EXPECTED_REMAINING_STRATA:
        raise ValueError("N357 remaining-strata regression")
    if int(agg["candidate_remaining_terminals"]) != EXPECTED_REMAINING:
        raise ValueError("N357 remaining-terminals regression")
    if agg["per_stratum_stream_sha256"] != EXPECTED_STREAM:
        raise ValueError("N357 per-stratum stream regression")
    if EXPECTED_SOURCE_TERMINALS - EXPECTED_REJECTED != EXPECTED_REMAINING:
        raise ValueError("N357 frozen partition identity regression")
    ver = result["verification"]
    if ver.get("prefix_cache_sha256") != EXPECTED_PREFIX_CACHE:
        raise ValueError("N357 deterministic prefix-cache regression")
    if ver.get("n356_authority_replayed_exactly") is not True:
        raise ValueError("N357 N356 authority replay flag regression")
    if ver.get("partition_identity") is not True:
        raise ValueError("N357 partition identity flag regression")
    sem = result["semantics"]
    if sem.get("main_pruning_credit") is not False:
        raise ValueError("N357 must not self-promote MAIN pruning credit")
    if sem.get("external_hostile_audit_required_before_credit") is not True:
        raise ValueError("N357 hostile-audit firewall regression")
    for key in (
        "full178_complete", "production_complete", "n104_release",
        "receiver_credit", "theorem_credit", "endpoint_credit",
        "stage32_closed", "merge_authorized",
        "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim",
    ):
        if sem.get(key) is not False:
            raise ValueError(f"N357 firewall regression: {key}")

    print(json.dumps({
        "verdict": "PASS_N357_FROZEN_AUDIT_BOUNDARY_SOURCE_LOCKS",
        "result_canonical_sha256": EXPECTED_CANONICAL,
        "per_stratum_stream_sha256": EXPECTED_STREAM,
        "source_terminals": EXPECTED_SOURCE_TERMINALS,
        "incremental_rejected_terminals": EXPECTED_REJECTED,
        "candidate_remaining_terminals": EXPECTED_REMAINING,
        "main_credit": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
