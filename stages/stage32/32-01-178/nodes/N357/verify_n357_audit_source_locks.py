#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]

LOCKS = {
    "main_routed_contract": (
        ROOT / "stages/stage32/32-01-178/nodes/N357/TRANSPORT_SUPPORT_CAPACITY_CONTRACT.md",
        "8a2a0048d216de9d177dc581dc208b51c6436442",
    ),
    "audit_contract": (
        ROOT / "stages/stage32/32-01-178/nodes/N357/AUDIT-CONTRACT.md",
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
    "n357_engine_direct": (
        ROOT / "stages/stage32/32-01-178/nodes/N357-engine/verify_n357_transport_support_capacity.py",
        "479c783cb42d0952cc310708106787147b499240",
    ),
    "n355_full_census_direct": (
        ROOT / "stages/stage32/32-01-178/nodes/N355/verify_n355_full_prefix_block_sum_census.py",
        "ccc00d1536cdf5e27965465dd5e40163e2fcb91c",
    ),
    "n220_base_import_direct": (
        ROOT / "stages/stage32/32-01-178/nodes/N220/verify_n220_exact_symbolic_count.py",
        "5855ae0835a828ab56b7a6e93a42f6788b6f676a",
    ),
    "n220_fast_import_direct": (
        ROOT / "stages/stage32/32-01-178/nodes/N220/verify_n220_exact_symbolic_count_fast.py",
        "1510533965c475baab577e30e4eb26ad58dc4ac8",
    ),
    "full178_manifest_direct": (
        ROOT / "stages/stage32/residual-32-01-production/full178-manifest.json",
        "0a46b34e278688240656b4977e9cb7f589e90e06",
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
    "n356_active_audited_workflow": (
        ROOT / ".github/workflows/stage32-01-178-n356-optimistic-exceptional-transport.yml",
        "ce7047ecc57dc2001856cf5382707c37adeefd08",
    ),
    "n357_generation_workflow_archive": (
        ROOT / "stages/stage32/32-01-178/nodes/N357-engine/FROZEN-GENERATION-WORKFLOW-ae6425.yml",
        "4d705356e95436b089743ede593ec24f8f2a59a7",
    ),
    "exact_head_ci_gate": (
        ROOT / ".github/workflows/stage32-claim-frontier-integrity.yml",
        "e4636477ba0e6696fea3def0f0c503f04720e0b6",
    ),
}

PRIOR_HOSTILE_AUDIT_FAIL_REVIEW = 5180168777
PRIOR_HOSTILE_AUDIT_FAIL_HEAD = "0bd9d452259fbbebb79bbb7ca91c155d2aaa34f6"
EXPECTED_GENERATION_HEAD = "ae6425fc0acc393d7554185af38a9525627ec180"
EXPECTED_GENERATION_RUN = 34602587402
EXPECTED_ARTIFACT_ID = 10265472692
EXPECTED_ARTIFACT_DIGEST = "da3b65180c19143800d1ddcc1cab0a3080ecd310e1d2b88b24c81314a7bc6b3f"
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

    result = json.loads((ROOT / "stages/stage32/32-01-178/nodes/N357/RESULT.json").read_text())
    if canonical_sha256_without_field(result) != EXPECTED_CANONICAL:
        raise ValueError("N357 RESULT canonical regression")
    if result.get("canonical_sha256_without_this_field") != EXPECTED_CANONICAL:
        raise ValueError("N357 RESULT self-canonical regression")

    agg = result["aggregate"]
    expected = {
        "source_strata_replayed": EXPECTED_SOURCE_STRATA,
        "source_terminals_replayed": EXPECTED_SOURCE_TERMINALS,
        "candidate_incremental_rejected_terminals": EXPECTED_REJECTED,
        "candidate_remaining_strata": EXPECTED_REMAINING_STRATA,
        "candidate_remaining_terminals": EXPECTED_REMAINING,
    }
    for key, value in expected.items():
        if int(agg[key]) != value:
            raise ValueError(f"N357 aggregate regression: {key}")
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
        "verdict": "PASS_N357_FROZEN_AUDIT_BOUNDARY_TRANSITIVE_SOURCE_LOCKS",
        "prior_hostile_audit_fail_review": PRIOR_HOSTILE_AUDIT_FAIL_REVIEW,
        "prior_hostile_audit_fail_head": PRIOR_HOSTILE_AUDIT_FAIL_HEAD,
        "generation_exact_head": EXPECTED_GENERATION_HEAD,
        "generation_workflow_run": EXPECTED_GENERATION_RUN,
        "generation_artifact_id": EXPECTED_ARTIFACT_ID,
        "generation_artifact_digest_sha256": EXPECTED_ARTIFACT_DIGEST,
        "result_canonical_sha256": EXPECTED_CANONICAL,
        "per_stratum_stream_sha256": EXPECTED_STREAM,
        "source_terminals": EXPECTED_SOURCE_TERMINALS,
        "incremental_rejected_terminals": EXPECTED_REJECTED,
        "candidate_remaining_terminals": EXPECTED_REMAINING,
        "direct_runtime_dependency_locks": [
            "n357_engine_direct",
            "n355_full_census_direct",
            "n220_base_import_direct",
            "n220_fast_import_direct",
            "full178_manifest_direct",
        ],
        "exact_head_ci_gate_locked": True,
        "main_credit": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
