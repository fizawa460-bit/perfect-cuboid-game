#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

from z3 import get_version_string

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))

import cut195_e8_common_adapter_wave3 as prev

core = prev.core

SCHEMA = "STAGE32_CUT196_E8_COMMON_ADAPTER_WAVE4_SHARD_V1"
PREFLIGHT = HERE / "CUT196-e8-common-adapter-wave4-preflight.json"
CUT195_WORKER = HERE / "cut195_e8_common_adapter_wave3.py"
CUT195_RESULT = HERE / "CUT195-e8-common-adapter-wave3-result.json"
CUT195_HANDOFF = HERE / "CUT195-e8-common-adapter-wave3-audit-handoff.json"
CUT195_VERIFY = HERE / "verify_cut195_e8_common_adapter_wave3.py"

PREFLIGHT_CANONICAL = "c0d5e240ec1c665c143826e8f1eaca6a3f25a6278d1e41cd8b7f5c911aebb5e1"
LOCKS = {
    CUT195_WORKER: "9f42f23272e1fc52097a0eb372cfc4dfa7d534c9",
    CUT195_RESULT: "d9fe913dccd41446780dbdde9f0200970ee9129e",
    CUT195_HANDOFF: "e449c1ef0b6180694f02fc4ae6ab083e2a934b26",
    CUT195_VERIFY: "022a8733eae7763926848b5e8bcf7f54f69bee66",
}
CUT195_AUDITED_HEAD = "2618f4dcd546d569b212753ac7abc10e07ee5828"
CUT195_EXACT_HEAD_CI = 34664320955
CUT195_HOSTILE_AUDIT_REVIEW = 5184909672
CUT195_PRUNED = 26216


def csha(v: object) -> str:
    return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise RuntimeError(msg)


def preflight() -> None:
    for path, expected in LOCKS.items():
        req(core.blob(path) == expected, f"predecessor source-lock drift: {path.relative_to(ROOT)}")
    pf = json.loads(PREFLIGHT.read_text())
    q = dict(pf)
    claimed = q.pop("canonical_sha256_without_this_field", None)
    req(
        pf.get("schema") == "STAGE32_CUT196_E8_COMMON_ADAPTER_WAVE4_PREFLIGHT_V1"
        and claimed == PREFLIGHT_CANONICAL
        and csha(q) == PREFLIGHT_CANONICAL,
        "CUT196 preflight canonical/schema drift",
    )
    prev.preflight()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--survivor-offset-start", type=int, required=True)
    ap.add_argument("--survivor-offset-count", type=int, required=True)
    ap.add_argument("--primes", default=",".join(map(str, core.DEFAULT_PRIMES)))
    ap.add_argument("--timeout-ms", type=int, default=750)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    start = args.survivor_offset_start
    end = start + args.survivor_offset_count
    req(start >= 766 and end <= 1021 and args.survivor_offset_count > 0,
        "CUT196 wave4 shards must stay inside survivor offsets 766..1020")
    primes = [int(v) for v in args.primes.split(",") if v.strip()]
    req(primes and all(p >= 2 for p in primes), "prime list empty")

    preflight()
    survivors = core.e8.current_main_survivor_block_indices()
    req(len(survivors) > 1020, "common e8 survivor universe too small for CUT196 wave4")
    prior = set(survivors[0:766])
    block_indices = survivors[start:end]
    req(len(block_indices) == args.survivor_offset_count, "wave4 block count drift")
    req(prior.isdisjoint(block_indices),
        "CUT196 overlaps CUT191/CUT193/CUT194/CUT195 prior offsets")

    P, blocks, g = core.load_picard_interface()
    solvers = {p: core.make_solver(P, blocks, p, args.timeout_ms) for p in primes}
    recs = [core.classify_block(i, P, blocks, g, solvers, primes) for i in block_indices]
    closed = [int(r["block_index"]) for r in recs if r["closed_candidate"]]
    methods: dict[str, int] = {}
    for r in recs:
        methods[r["method"]] = methods.get(r["method"], 0) + 1

    bh = hashlib.sha256()
    ch = hashlib.sha256()
    for i in block_indices:
        bh.update(f"{i}\n".encode())
    for i in closed:
        ch.update(f"{i}\n".encode())

    body = {
        "schema": SCHEMA,
        "stage": "32",
        "surface": "full178-cut",
        "node": "CUT196",
        "status": "WAVE4_SHARD_CANDIDATE_NEEDS_AGGREGATE_AND_HOSTILE_AUDIT",
        "z3_version": get_version_string(),
        "source": {
            "cut195_pr": 1792,
            "cut195_audited_exact_head": CUT195_AUDITED_HEAD,
            "cut195_exact_head_ci": CUT195_EXACT_HEAD_CI,
            "cut195_hostile_audit_review": CUT195_HOSTILE_AUDIT_REVIEW,
            "cut195_candidate_pruned_terminals": CUT195_PRUNED,
            "main_parent_exact_head": "6d63d798adb50dd4efc5f0d5abc553b3dfa23060",
            "main_parent_external_reaudit_review": 5178420739,
            "ex5_producer_exact_head": "fd00531181228c9f367a49eb61ddc3af6ab84ab3",
            "ex5_producer_ci_run": 34598945799,
        },
        "target": {
            "row_id": "g1-d008",
            "g": 1,
            "d": 8,
            "e": 8,
            "survivor_offset_range": [start, end - 1],
            "block_indices": block_indices,
            "block_index_stream_sha256": bh.hexdigest(),
            "block_count": len(block_indices),
            "terminal_count": 113 * len(block_indices),
            "cut191_block0_disjoint": True,
            "cut193_wave1_disjoint": True,
            "cut194_wave2_disjoint": True,
            "cut195_wave3_disjoint": True,
            "n356_preserved_all_wave_blocks": True,
        },
        "method": {
            "primes": primes,
            "per_check_timeout_ms": args.timeout_ms,
            "whole_block_relaxation_first": True,
            "parent_level_relaxation_after_hnf": True,
            "necessity": "every exact integral Picard64 completion must survive the source-locked HNF parent population and every finite-ring column-image relaxation; UNSAT is monotone, SAT/UNKNOWN grants no pruning credit",
        },
        "result": {
            "candidate_closed_block_indices": closed,
            "candidate_closed_block_count": len(closed),
            "candidate_closed_block_stream_sha256": ch.hexdigest(),
            "candidate_pruned_terminals": 113 * len(closed),
            "method_counts": methods,
            "blocks": recs,
        },
        "credit": {
            "stage32_main_pruning_credit": False,
            "cut196_pruning_credit": False,
            "full178_complete": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "merge_authorized": False,
        },
        "firewalls": {
            "sat_or_unknown_promoted_to_unsat": False,
            "cut191_double_counted": False,
            "cut193_wave1_double_counted": False,
            "cut194_wave2_double_counted": False,
            "cut195_wave3_double_counted": False,
            "n356_double_counted": False,
            "main_authority_mutated": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(body, sort_keys=True, indent=2) + "\n")
    print(json.dumps({"status": body["status"], "offsets": [start, end - 1], "blocks": len(block_indices), "closed": len(closed), "candidate_pruned_terminals": 113 * len(closed), "canonical": body["canonical_sha256_without_this_field"]}, sort_keys=True))


if __name__ == "__main__":
    main()
