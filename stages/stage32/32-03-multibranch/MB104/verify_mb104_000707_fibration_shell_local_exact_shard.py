#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

import run_mb104_000707_fibration_shell_local_exact as engine


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--certificate", type=Path, required=True)
    ap.add_argument("--shell-index", type=int, required=True)
    ap.add_argument("--shard-residue", type=int, required=True)
    ap.add_argument("--shard-count", type=int, default=engine.SHARD_COUNT)
    args = ap.parse_args()

    d = json.loads(args.certificate.read_text(encoding="utf-8"))
    assert d["schema"] == engine.SCHEMA
    claimed = d["canonical_sha256_without_this_field"]
    body = dict(d)
    body.pop("canonical_sha256_without_this_field")
    assert claimed == engine.csha(body)
    assert d["shell_index"] == args.shell_index
    assert d["partition"]["shard_count"] == args.shard_count
    assert d["partition"]["shard_residue"] == args.shard_residue
    contract = engine.split_contract(args.shell_index, args.shard_count)
    for key in (
        "shell_index", "shard_count", "split_coordinate_0based",
        "split_coordinate_bound", "coordinate_bounds", "intervals",
        "coverage_is_exact_disjoint", "bound_method", "dual_diagonal_sha256",
        "retained_hperp_text_sha256", "retained_picard_base_canonical",
    ):
        assert d["partition"][key] == contract[key], key
    assert d["partition"]["shard_interval"] == contract["intervals"][args.shard_residue]
    assert d["source_locks"] == engine.certificate_source_locks()

    result = d["result"]
    cands = result["primitive_known140_nonnegative_candidates"]
    assert result["primitive_known140_nonnegative_candidate_count"] == len(cands)
    assert result["integral_known140_nonnegative_solution_count"] >= len(cands)
    seen_x = set()
    seen_f = set()
    split_j = contract["split_coordinate_0based"]
    lo, hi = d["partition"]["shard_interval"]
    for rec in cands:
        replay = engine.replay_solution(args.shell_index, [int(v) for v in rec["x_hperp_coordinates"]])
        assert replay == rec
        assert rec["primitive"] is True
        value = rec["x_hperp_coordinates"][split_j]
        assert lo <= value <= hi
        xkey = tuple(rec["x_hperp_coordinates"])
        fkey = tuple(rec["picard_basis_coordinates"])
        assert xkey not in seen_x
        assert fkey not in seen_f
        seen_x.add(xkey)
        seen_f.add(fkey)

    complete = result["complete"]
    assert complete == (d["status"] == "COMPLETE_EXACT_SHARD_ZERO_CREDIT")
    if complete:
        assert d["solver"]["final_solver_result"] == "unsat"
        assert d["solver"]["reason"] is None
    else:
        assert d["status"].startswith("PARTIAL_")
    assert all(v is False for v in d["credit_firewall"].values())
    print(json.dumps({
        "success": True,
        "complete": complete,
        "shell_index": args.shell_index,
        "shard_residue": args.shard_residue,
        "candidate_count": len(cands),
        "canonical": claimed,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
