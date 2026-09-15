#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

RESULT_PATH = Path("stages/stage32-ex5/hpadj-08_ex5/FULL178-RESULT.json")
ADAPTER_PATH = Path("stages/stage32-ex5/hpadj-08_ex5/CURRENT-MAIN-NO-DOUBLE-CHARGE-ADAPTER.json")
ADAPTER_VERIFIER = Path("stages/stage32-ex5/hpadj-08_ex5/verify_hpadj08_current_main_adapter.py")
PLANNED = ((0,11),(12,23),(24,35),(36,47),(48,59),(60,71),(72,83),(84,96))
EXPECTED_SHARD_CANONICALS = (
    "185504dcbc7f77b8c4682934a83a0fa2e8f4f36bd7cf6b5b3089b8b483ebeb64",
    "e35491cf9bff7d75834ae3729bad6697b5887d182e9752237b616307ebb9d019",
    "717a508a60650239fe4669360dd9c055da111ca2e31d2363ee617274fb5a9375",
    "e30bc9172233ffe41718cf590a574fe5b48f183e36201ed5544ff530e90945ea",
    "8e41ae8dbaae894a34e959ff31d27db5ac8a425118332ec8e0a20f9bbeaa2a84",
    "e1c934f7a2ce6c8f9fc10962ac909a6b184239ad1d4e435c602cd883e674025c",
    "2afbce5bc957819deea1e95d89b7b754da7bb64388f0c2515b508327254b46dd",
    "1d36974b8f67a3082fd3e37cf1d048deefbffa2527bc70d2b88d93be6a919898",
)
EXPECTED_AGGREGATE_CANONICAL = "9b6df7b5959d7afa996332bbdd2b3c0f661dfb2dc186767db8f29635fb0e028e"
EXPECTED_RESULT_CANONICAL = "625e289a1a9f086b5e02f247665a7f9ac4b7fe72eaacd3011fe73a0e96041953"
EXPECTED_ROW_STREAM = "d5d8ab364d122c4b3138d577442b383290ab7878e11629b3673058073690e5a1"
EXPECTED_OLD = 20713268924714183714810
EXPECTED_EXACT = 40886299509963924857401
EXPECTED_INCREMENTAL = 20173030585249741142591


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def canon(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def verify_result(result: dict) -> None:
    req(result.get("schema") == "STAGE32EX5_HPADJ08_FULL178_RESULT_V1", "result schema")
    req(result.get("route_id") == "HPADJ-08_ex5", "route id")
    req(result.get("source_run_id") == 34935380596, "source run")
    req(result.get("source_exact_head") == "b11a9820af4a02148112a6ae235bc3a51d134ef2", "source exact head")
    cov = result.get("coverage", {})
    req(cov.get("rows") == 178, "coverage rows")
    req(tuple(map(tuple, cov.get("b_partition", []))) == PLANNED, "coverage partition")
    req(cov.get("all_shards_success") is True, "all shards success")
    req(result.get("old_group_cauchy_candidate_rejected_terminals") == EXPECTED_OLD, "old total")
    req(result.get("stored_exact_square_candidate_rejected_terminals") == EXPECTED_EXACT, "exact total")
    req(result.get("incremental_candidate_over_group_cauchy") == EXPECTED_INCREMENTAL, "incremental total")
    req(EXPECTED_EXACT - EXPECTED_OLD == EXPECTED_INCREMENTAL, "expected arithmetic")
    req(result.get("stored_exact_square_candidate_rejected_terminals") - result.get("old_group_cauchy_candidate_rejected_terminals") == result.get("incremental_candidate_over_group_cauchy"), "result arithmetic")
    req(result.get("row_stream_sha256") == EXPECTED_ROW_STREAM, "row stream")
    req(result.get("aggregate_candidate_canonical") == EXPECTED_AGGREGATE_CANONICAL, "aggregate canonical")
    shards = result.get("shards", [])
    req(len(shards) == len(PLANNED), "shard count")
    req(tuple(tuple(x.get("b_interval", [])) for x in shards) == PLANNED, "shard order/coverage")
    req(tuple(x.get("canonical") for x in shards) == EXPECTED_SHARD_CANONICALS, "shard canonicals")
    fw = result.get("firewalls", {})
    req(fw.get("stage32_main_pruning_credit") is False, "MAIN pruning firewall")
    req(fw.get("current_main_incremental_credit") is False, "MAIN incremental firewall")
    req(fw.get("full178_candidate_only") is True, "candidate-only firewall")
    req(fw.get("full178_complete") is False, "FULL178 completion firewall")
    req(fw.get("theorem_credit") is False, "theorem firewall")
    req(fw.get("effectivity_credit") is False, "effectivity firewall")
    req(fw.get("receiver_credit") is False, "receiver firewall")
    req(fw.get("endpoint_credit") is False, "endpoint firewall")
    req(fw.get("perfect_cuboid_existence_claim") is False, "existence firewall")
    req(fw.get("perfect_cuboid_nonexistence_claim") is False, "nonexistence firewall")
    req(fw.get("merge_authorized") is False, "merge firewall")
    req(result.get("canonical_sha256_without_this_field") == canon(result), "result self canonical")
    req(result.get("canonical_sha256_without_this_field") == EXPECTED_RESULT_CANONICAL, "retained result canonical")


def verify_aggregate(result: dict, aggregate: dict) -> None:
    req(aggregate.get("schema") == "STAGE32EX5_HPADJ08_FULL178_AGGREGATE_CANDIDATE_V1", "aggregate schema")
    req(aggregate.get("route_id") == "HPADJ-08_ex5", "aggregate route")
    req(aggregate.get("canonical_sha256_without_this_field") == canon(aggregate), "aggregate self canonical")
    req(aggregate.get("canonical_sha256_without_this_field") == result.get("aggregate_candidate_canonical"), "result/aggregate canonical binding")
    req(aggregate.get("row_stream_sha256") == result.get("row_stream_sha256"), "result/aggregate row stream")
    req(aggregate.get("old_group_cauchy_candidate_rejected_terminals") == result.get("old_group_cauchy_candidate_rejected_terminals"), "result/aggregate old total")
    req(aggregate.get("stored_exact_square_candidate_rejected_terminals") == result.get("stored_exact_square_candidate_rejected_terminals"), "result/aggregate exact total")
    req(aggregate.get("incremental_candidate_over_group_cauchy") == result.get("incremental_candidate_over_group_cauchy"), "result/aggregate incremental")
    req(tuple(aggregate.get("shard_canonicals", [])) == EXPECTED_SHARD_CANONICALS, "aggregate shard canonicals")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--result", default=str(RESULT_PATH))
    ap.add_argument("--aggregate")
    ns = ap.parse_args()
    result = json.loads(Path(ns.result).read_text(encoding="utf-8"))
    verify_result(result)
    if ns.aggregate:
        aggregate = json.loads(Path(ns.aggregate).read_text(encoding="utf-8"))
        verify_aggregate(result, aggregate)
    if ADAPTER_PATH.is_file():
        req(ADAPTER_VERIFIER.is_file(), "current-MAIN adapter present without verifier")
        subprocess.check_call([sys.executable, str(ADAPTER_VERIFIER)])
    print("HPADJ08_EX5_FULL178_RESULT_OK", result["canonical_sha256_without_this_field"], result["aggregate_candidate_canonical"])


if __name__ == "__main__":
    main()
