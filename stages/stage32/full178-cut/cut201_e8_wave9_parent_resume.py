#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib
import json
import subprocess
import sys
from pathlib import Path

EXECUTION_HEAD = "be6a6f8acc9942dd4973f13c630a4318b923e03d"
EXACT_WORKER_BLOB = "a8be279ebc3bca4a383d4a81e4c04de7413b17b8"
SURVIVOR_OFFSET = 2204
SHARD_COUNT = 32
DEFAULT_PRIMES = [2, 3, 5, 7, 11, 13, 17, 31, 127]
SCHEMA_PREP = "STAGE32_CUT201_G8_OFFSET2204_PARENT_MANIFEST_V1"
SCHEMA_SHARD = "STAGE32_CUT201_G8_OFFSET2204_PARENT_SHARD_V1"
SCHEMA_SINGLETON = "STAGE32_CUT201_E8_COMMON_ADAPTER_WAVE9_SHARD_V1"
MAX_MANIFEST_BYTES = 25 * 1024 * 1024


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise RuntimeError(msg)


def checked(obj: dict, schema: str) -> dict:
    q = dict(obj)
    claimed = q.pop("canonical_sha256_without_this_field", None)
    req(obj.get("schema") == schema, f"schema drift: {obj.get('schema')}")
    req(claimed == csha(q), "canonical drift")
    return obj


def load_exact(exact_root: Path):
    exact_root = exact_root.resolve()
    got = subprocess.check_output(["git", "-C", str(exact_root), "rev-parse", "HEAD"], text=True).strip()
    req(got == EXECUTION_HEAD, f"execution head drift: {got}")
    worker = exact_root / "stages/stage32/full178-cut/cut201_e8_common_adapter_wave9.py"
    raw = worker.read_bytes()
    blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    req(blob == EXACT_WORKER_BLOB, f"exact worker blob drift: {blob}")
    sys.path.insert(0, str(worker.parent))
    return importlib.import_module("cut201_e8_common_adapter_wave9")


def manifest_stream_hash(parents: list[list[int]]) -> str:
    h = hashlib.sha256()
    for ordinal, vals in enumerate(parents):
        h.update(json.dumps({"ordinal": ordinal, "selected_exceptional_pairings": vals}, sort_keys=True, separators=(",", ":")).encode() + b"\n")
    return h.hexdigest()


def prepare(args) -> None:
    core = load_exact(args.exact_root)
    primes = [int(v) for v in args.primes.split(",") if v.strip()]
    req(primes == DEFAULT_PRIMES, "generation8 prime list must remain exact")
    req(args.timeout_ms == 750, "generation8 per-check timeout must remain 750ms")
    core.preflight()
    survivors = core.e8.current_main_survivor_block_indices()
    req(len(survivors) > SURVIVOR_OFFSET, "survivor universe too small")
    block_index = int(survivors[SURVIVOR_OFFSET])
    sig = core.e8.block_signature(block_index)
    req(sig["current_main_audited_prefix_survivor"] is True, "offset2204 lost source survival")
    sums = [int(v) for v in sig["n355_known_group_sums"]]
    n356_lhs = sums[1] - sums[2]
    req(max(sums) <= 4 and n356_lhs <= 4 <= 16, "source-prefix bridge drift")

    P, blocks, g = core.load_picard_interface()
    solvers = {p: core.make_solver(P, blocks, p, args.timeout_ms) for p in primes}
    fixed_terminal = {int(k): int(v) for k, v in sig["fixed_exceptional_pairings"].items()}
    whole_attempts = []
    whole_unsat_prime = None
    for prime in primes:
        s, y, _ = solvers[prime]
        result, reason = core.check_with_fixed(s, y, fixed_terminal)
        row = {"prime": prime, "result": result}
        if reason:
            row["reason_unknown"] = reason
        whole_attempts.append(row)
        if result == "unsat":
            whole_unsat_prime = prime
            break

    parents: list[list[int]] = []
    exceptional_labels = [int(v) for v in g.exceptional_labels]
    if whole_unsat_prime is None:
        for rec in core.e8.iter_parent_population(block_index, g):
            vals = [int(v) for v in rec["selected_exceptional_pairings"]]
            req(len(vals) == len(exceptional_labels), "parent pairing width drift")
            parents.append(vals)

    body = {
        "schema": SCHEMA_PREP,
        "status": "WHOLE_BLOCK_FINITE_RING_UNSAT" if whole_unsat_prime is not None else "PARENT_POPULATION_FROZEN_FOR_RESUMABLE_SHARDS",
        "execution_head": EXECUTION_HEAD,
        "exact_worker_blob": EXACT_WORKER_BLOB,
        "survivor_offset": SURVIVOR_OFFSET,
        "block_index": block_index,
        "terminal_rank_range": [int(v) for v in sig["terminal_rank_range"]],
        "terminal_count": 113,
        "n355_group_sums": sums,
        "n356_lhs_b_minus_c": n356_lhs,
        "primes": primes,
        "per_check_timeout_ms": args.timeout_ms,
        "whole_block_attempts": whole_attempts,
        "whole_block_obstruction_prime": whole_unsat_prime,
        "exceptional_labels": exceptional_labels,
        "parent_count": len(parents),
        "parent_partition": {"kind": "ORDINAL_MOD", "shard_count": SHARD_COUNT, "rule": "ordinal % 32 == shard_id", "exact_union_required": True, "pairwise_disjoint_required": True},
        "parent_stream_sha256": manifest_stream_hash(parents),
        "parents": parents,
        "credit": {"stage32_main_pruning_credit": False, "cut201_pruning_credit": False, "merge_authorized": False},
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    raw = (json.dumps(body, sort_keys=True, indent=2) + "\n").encode()
    req(len(raw) <= MAX_MANIFEST_BYTES, f"manifest exceeds {MAX_MANIFEST_BYTES} bytes")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(raw)
    print(json.dumps({"status": body["status"], "block_index": block_index, "parent_count": len(parents), "manifest_bytes": len(raw), "canonical": body["canonical_sha256_without_this_field"]}, sort_keys=True))


def shard(args) -> None:
    core = load_exact(args.exact_root)
    manifest = checked(json.loads(args.manifest.read_text()), SCHEMA_PREP)
    req(manifest["execution_head"] == EXECUTION_HEAD, "manifest execution-head drift")
    req(manifest["exact_worker_blob"] == EXACT_WORKER_BLOB, "manifest worker drift")
    req(int(manifest["survivor_offset"]) == SURVIVOR_OFFSET, "manifest offset drift")
    req(int(args.shard_count) == SHARD_COUNT, "shard-count drift")
    sid = int(args.shard_id)
    req(0 <= sid < SHARD_COUNT, "shard id outside range")
    primes = [int(v) for v in manifest["primes"]]
    req(primes == DEFAULT_PRIMES and int(manifest["per_check_timeout_ms"]) == 750, "manifest solver semantics drift")

    outcomes = []
    if manifest["status"] != "WHOLE_BLOCK_FINITE_RING_UNSAT":
        P, blocks, _g = core.load_picard_interface()
        solvers = {p: core.make_solver(P, blocks, p, 750) for p in primes}
        labels = [int(v) for v in manifest["exceptional_labels"]]
        parents = manifest["parents"]
        for ordinal in range(sid, len(parents), SHARD_COUNT):
            vals = [int(v) for v in parents[ordinal]]
            fixed = {label: value for label, value in zip(labels, vals)}
            obstruction_prime = None
            unknown_checks = 0
            for prime in primes:
                s, y, _ = solvers[prime]
                result, _reason = core.check_with_fixed(s, y, fixed)
                if result == "unsat":
                    obstruction_prime = prime
                    break
                if result == "unknown":
                    unknown_checks += 1
            outcomes.append({"ordinal": ordinal, "obstruction_prime": obstruction_prime, "unknown_checks": unknown_checks})

    oh = hashlib.sha256()
    for row in outcomes:
        oh.update(json.dumps(row, sort_keys=True, separators=(",", ":")).encode() + b"\n")
    body = {
        "schema": SCHEMA_SHARD,
        "status": "COMPLETE",
        "execution_head": EXECUTION_HEAD,
        "exact_worker_blob": EXACT_WORKER_BLOB,
        "manifest_canonical": manifest["canonical_sha256_without_this_field"],
        "manifest_parent_stream_sha256": manifest["parent_stream_sha256"],
        "survivor_offset": SURVIVOR_OFFSET,
        "block_index": int(manifest["block_index"]),
        "shard_id": sid,
        "shard_count": SHARD_COUNT,
        "partition_rule": "ordinal % 32 == shard_id",
        "assigned_parent_count": len(outcomes),
        "outcome_stream_sha256": oh.hexdigest(),
        "outcomes": outcomes,
        "credit": {"stage32_main_pruning_credit": False, "cut201_pruning_credit": False, "merge_authorized": False},
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(body, sort_keys=True, indent=2) + "\n")
    print(json.dumps({"shard_id": sid, "assigned_parent_count": len(outcomes), "canonical": body["canonical_sha256_without_this_field"]}, sort_keys=True))


def aggregate(args) -> None:
    core = load_exact(args.exact_root)
    manifest = checked(json.loads(args.manifest.read_text()), SCHEMA_PREP)
    files = sorted(args.shards.glob("cut201-g8-parent-shard-*.json"))
    req(len(files) == SHARD_COUNT, f"expected {SHARD_COUNT} shard files, got {len(files)}")
    docs = [checked(json.loads(p.read_text()), SCHEMA_SHARD) for p in files]
    by_sid = {int(d["shard_id"]): d for d in docs}
    req(sorted(by_sid) == list(range(SHARD_COUNT)), "shard-id coverage drift")

    outcomes_by_ordinal = {}
    for sid, d in sorted(by_sid.items()):
        req(int(d["shard_count"]) == SHARD_COUNT, "shard-count certificate drift")
        req(d["manifest_canonical"] == manifest["canonical_sha256_without_this_field"], "manifest canonical mismatch")
        req(d["manifest_parent_stream_sha256"] == manifest["parent_stream_sha256"], "parent stream mismatch")
        for row in d["outcomes"]:
            ordinal = int(row["ordinal"])
            req(ordinal % SHARD_COUNT == sid, f"ordinal {ordinal} routed to wrong shard")
            req(ordinal not in outcomes_by_ordinal, f"duplicate parent ordinal {ordinal}")
            outcomes_by_ordinal[ordinal] = row

    parent_count = int(manifest["parent_count"])
    obstruction = {}
    unresolved = []
    unknown_checks = 0
    hist = {str(p): 0 for p in DEFAULT_PRIMES}
    if manifest["status"] == "WHOLE_BLOCK_FINITE_RING_UNSAT":
        req(parent_count == 0 and not outcomes_by_ordinal, "whole-block UNSAT should have no parent outcomes")
        method = "WHOLE_BLOCK_FINITE_RING_UNSAT"
        closed = True
    else:
        req(sorted(outcomes_by_ordinal) == list(range(parent_count)), "parent ordinal union has gap or overlap")
        for ordinal in range(parent_count):
            row = outcomes_by_ordinal[ordinal]
            p = row.get("obstruction_prime")
            unknown_checks += int(row.get("unknown_checks", 0))
            if p is None:
                unresolved.append(ordinal)
            else:
                p = int(p)
                req(p in DEFAULT_PRIMES, f"unexpected obstruction prime {p}")
                obstruction[ordinal] = p
                hist[str(p)] += 1
        closed = not unresolved
        method = "HNF_PARENT_POPULATION_EMPTY" if parent_count == 0 else ("ALL_HNF_PARENTS_FINITE_RING_UNSAT" if closed else "FINITE_RING_NONCLOSING_RESIDUAL_PARENTS")

    oh = hashlib.sha256()
    for ordinal in sorted(obstruction):
        oh.update(f"{ordinal}:{obstruction[ordinal]}\n".encode())
    rh = hashlib.sha256()
    for ordinal in unresolved:
        rh.update(f"{ordinal}\n".encode())

    rec = {
        "block_index": int(manifest["block_index"]),
        "terminal_rank_range": [int(v) for v in manifest["terminal_rank_range"]],
        "terminal_count": 113,
        "n355_group_sums": [int(v) for v in manifest["n355_group_sums"]],
        "n356_lhs_b_minus_c": int(manifest["n356_lhs_b_minus_c"]),
        "method": method,
        "whole_block_attempts": manifest["whole_block_attempts"],
        "modular_feasible_parent_count": None if method == "WHOLE_BLOCK_FINITE_RING_UNSAT" else parent_count,
        "closed_candidate": closed,
        "candidate_pruned_terminals": 113 if closed else 0,
    }
    if method == "WHOLE_BLOCK_FINITE_RING_UNSAT":
        rec["whole_block_obstruction_prime"] = int(manifest["whole_block_obstruction_prime"])
    elif method == "HNF_PARENT_POPULATION_EMPTY":
        rec["modular_feasible_parent_count"] = 0
    else:
        rec.update({"finite_ring_obstructed_parent_count": len(obstruction), "residual_parent_count": len(unresolved), "obstruction_prime_histogram": hist, "obstruction_assignment_sha256": oh.hexdigest(), "residual_parent_ordinal_sha256": rh.hexdigest(), "unknown_check_count": unknown_checks})

    block_index = int(manifest["block_index"])
    bh = hashlib.sha256(); bh.update(f"{block_index}\n".encode())
    ch = hashlib.sha256()
    if closed:
        ch.update(f"{block_index}\n".encode())
    body = {
        "schema": SCHEMA_SINGLETON,
        "stage": "32", "surface": "full178-cut", "node": "CUT201",
        "status": "WAVE9_SHARD_CANDIDATE_NEEDS_AGGREGATE_AND_HOSTILE_AUDIT",
        "z3_version": core.get_version_string(),
        "source": {"cut200_pr": 1805, "cut200_audited_exact_head": core.CUT200_AUDITED_HEAD, "cut200_exact_head_ci": core.CUT200_EXACT_HEAD_CI, "cut200_hostile_audit_review": core.CUT200_HOSTILE_AUDIT_REVIEW, "cut200_candidate_pruned_terminals": core.CUT200_PRUNED, "main_parent_exact_head": "6d63d798adb50dd4efc5f0d5abc553b3dfa23060", "main_parent_external_reaudit_review": 5178420739, "ex5_producer_exact_head": "fd00531181228c9f367a49eb61ddc3af6ab84ab3", "ex5_producer_ci_run": 34598945799},
        "target": {"row_id": "g1-d008", "g": 1, "d": 8, "e": 8, "survivor_offset_range": [SURVIVOR_OFFSET, SURVIVOR_OFFSET], "block_indices": [block_index], "block_index_stream_sha256": bh.hexdigest(), "block_count": 1, "terminal_count": 113, "cut191_block0_disjoint": True, "cut193_wave1_disjoint": True, "cut194_wave2_disjoint": True, "cut195_wave3_disjoint": True, "cut196_wave4_disjoint": True, "cut197_wave5_disjoint": True, "cut198_wave6_disjoint": True, "cut199_wave7_disjoint": True, "cut200_wave8_disjoint": True, "n356_preserved_all_wave_blocks": True},
        "method": {"primes": DEFAULT_PRIMES, "per_check_timeout_ms": 750, "whole_block_relaxation_first": True, "parent_level_relaxation_after_hnf": True, "necessity": "every exact integral Picard64 completion must survive the source-locked HNF parent population and every finite-ring column-image relaxation; UNSAT is monotone, SAT/UNKNOWN grants no pruning credit"},
        "result": {"candidate_closed_block_indices": [block_index] if closed else [], "candidate_closed_block_count": 1 if closed else 0, "candidate_closed_block_stream_sha256": ch.hexdigest(), "candidate_pruned_terminals": 113 if closed else 0, "method_counts": {method: 1}, "blocks": [rec]},
        "credit": {"stage32_main_pruning_credit": False, "cut201_pruning_credit": False, "full178_complete": False, "theorem_credit": False, "endpoint_credit": False, "merge_authorized": False},
        "firewalls": {"sat_or_unknown_promoted_to_unsat": False, "cut191_double_counted": False, "cut193_wave1_double_counted": False, "cut194_wave2_double_counted": False, "cut195_wave3_double_counted": False, "cut196_wave4_double_counted": False, "cut197_wave5_double_counted": False, "cut198_wave6_double_counted": False, "cut199_wave7_double_counted": False, "cut200_wave8_double_counted": False, "n356_double_counted": False, "main_authority_mutated": False, "perfect_cuboid_existence_claim": False, "perfect_cuboid_nonexistence_claim": False},
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(body, sort_keys=True, indent=2) + "\n")
    print(json.dumps({"status": body["status"], "block_index": block_index, "parent_count": parent_count, "closed": closed, "residual_parent_count": len(unresolved), "canonical": body["canonical_sha256_without_this_field"]}, sort_keys=True))


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("prepare")
    p.add_argument("--exact-root", type=Path, required=True); p.add_argument("--primes", default=",".join(map(str, DEFAULT_PRIMES))); p.add_argument("--timeout-ms", type=int, default=750); p.add_argument("--output", type=Path, required=True); p.set_defaults(fn=prepare)
    p = sub.add_parser("shard")
    p.add_argument("--exact-root", type=Path, required=True); p.add_argument("--manifest", type=Path, required=True); p.add_argument("--shard-id", type=int, required=True); p.add_argument("--shard-count", type=int, default=SHARD_COUNT); p.add_argument("--output", type=Path, required=True); p.set_defaults(fn=shard)
    p = sub.add_parser("aggregate")
    p.add_argument("--exact-root", type=Path, required=True); p.add_argument("--manifest", type=Path, required=True); p.add_argument("--shards", type=Path, required=True); p.add_argument("--output", type=Path, required=True); p.set_defaults(fn=aggregate)
    args = ap.parse_args(); args.fn(args)


if __name__ == "__main__":
    main()
