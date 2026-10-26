#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

import run_mb104_000707_fibration_shell_local_exact as engine

HERE = Path(__file__).resolve().parent
SHARD_VERIFIER = HERE / "verify_mb104_000707_fibration_shell_local_exact_shard.py"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input-dir", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--shell-index", type=int, default=0)
    ap.add_argument("--shard-count", type=int, default=engine.SHARD_COUNT)
    args = ap.parse_args()

    files = sorted(args.input_dir.glob("mb-fib-shell0-shard-*.json"))
    rows = []
    shard_hashes = {}
    expected_source_locks = engine.certificate_source_locks()
    for path in files:
        d = json.loads(path.read_text(encoding="utf-8"))
        if d.get("schema") != engine.SCHEMA:
            raise ValueError(f"schema mismatch: {path}")
        claimed = d.get("canonical_sha256_without_this_field")
        body = dict(d)
        body.pop("canonical_sha256_without_this_field", None)
        if claimed != engine.csha(body):
            raise ValueError(f"canonical mismatch: {path}")
        residue = int(d.get("partition", {}).get("shard_residue", -1))
        if not 0 <= residue < args.shard_count:
            raise ValueError(f"shard residue drift: {path}")
        subprocess.run([
            sys.executable,
            str(SHARD_VERIFIER),
            "--certificate", str(path),
            "--shell-index", str(args.shell_index),
            "--shard-count", str(args.shard_count),
            "--shard-residue", str(residue),
        ], check=True)
        if d.get("status") != "COMPLETE_EXACT_SHARD_ZERO_CREDIT":
            raise ValueError(f"incomplete shard status: {path}")
        if d.get("result", {}).get("complete") is not True:
            raise ValueError(f"incomplete shard result: {path}")
        if d.get("solver", {}).get("final_solver_result") != "unsat":
            raise ValueError(f"non-UNSAT shard completion: {path}")
        if d.get("source_locks") != expected_source_locks:
            raise ValueError(f"stale/mismatched shard source locks: {path}")
        shard_hashes[residue] = claimed
        rows.append(d)

    contract = engine.split_contract(args.shell_index, args.shard_count)
    by_residue = {}
    for d in rows:
        if d["shell_index"] != args.shell_index:
            raise ValueError("shell index drift")
        r = int(d["partition"]["shard_residue"])
        if r in by_residue:
            raise ValueError("duplicate shard")
        by_residue[r] = d

    expected = set(range(args.shard_count))
    discovered = set(by_residue)
    complete_residues = sorted(r for r, d in by_residue.items() if d["result"]["complete"])
    coverage_complete = discovered == expected and len(complete_residues) == args.shard_count

    candidates = []
    seen_x = set()
    total_models = 0
    if coverage_complete:
        for r in range(args.shard_count):
            d = by_residue[r]
            assert d["partition"]["intervals"] == contract["intervals"]
            assert d["partition"]["split_coordinate_0based"] == contract["split_coordinate_0based"]
            assert d["partition"]["shard_interval"] == contract["intervals"][r]
            total_models += int(d["result"]["integral_known140_nonnegative_solution_count"])
            for rec in d["result"]["primitive_known140_nonnegative_candidates"]:
                xkey = tuple(rec["x_hperp_coordinates"])
                if xkey in seen_x:
                    raise ValueError("cross-shard duplicate H-perp solution")
                seen_x.add(xkey)
                candidates.append(rec)
    candidates.sort(key=lambda rec: tuple(rec["picard_basis_coordinates"]))

    out = {
        "schema": "STAGE32_MB104_000707_FIBRATION_SHELL0_LOCAL_EXACT_AGGREGATE_V1",
        "status": "COMPLETE_EXACT_SHELL0_ZERO_CREDIT" if coverage_complete else "INCOMPLETE_SHARD_COVERAGE_NO_CREDIT",
        "shell_index": args.shell_index,
        "partition": contract,
        "discovered_shard_residues": sorted(discovered),
        "complete_shard_residues": complete_residues,
        "coverage_complete": coverage_complete,
        "source_locks": expected_source_locks,
        "input_shard_canonical_sha256": [
            {"shard_residue": r, "canonical_sha256": shard_hashes[r]}
            for r in sorted(shard_hashes)
        ],
        "result": {
            "integral_known140_nonnegative_solution_count": total_models if coverage_complete else None,
            "primitive_known140_nonnegative_candidate_count": len(candidates) if coverage_complete else None,
            "primitive_known140_nonnegative_candidates": candidates if coverage_complete else [],
        },
        "credit_firewall": {
            "numerical_fibration_shell_credit": False,
            "effectivity_credit": False,
            "semiampleness_credit": False,
            "global_fibration_optimum_credit": False,
            "MB104_complete": False,
            "receiver_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "merge_authorized": False,
        },
    }
    out["canonical_sha256_without_this_field"] = engine.csha(out)
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": out["status"],
        "discovered": len(discovered),
        "complete": len(complete_residues),
        "candidate_count": out["result"]["primitive_known140_nonnegative_candidate_count"],
        "canonical": out["canonical_sha256_without_this_field"],
    }, sort_keys=True))
    raise SystemExit(0 if coverage_complete else 2)


if __name__ == "__main__":
    main()
