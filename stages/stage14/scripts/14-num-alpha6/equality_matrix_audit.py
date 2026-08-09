#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
A5_PATH = ROOT / "stages/stage14/scripts/14-num-alpha5/safe_primitive_sieve_audit.py"
NUM3_PATH = ROOT / "stages/stage14/scripts/14-num3/extended_exact_census.py"
NUM1_MANIFEST = ROOT / "stages/stage14/data/14-num1/baseline_manifest.json"
NUM3_MANIFEST = ROOT / "stages/stage14/data/14-num3/census_manifest.json"

SMALL_DIRECT_CUTS = (1_000, 5_000, 20_000, 100_000, 200_000, 500_000)
LARGE_MATRIX_CUTS = (2_000_000, 5_000_000, 10_000_000)
MAX_LARGE_BOUND = max(LARGE_MATRIX_CUTS)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


A5 = load_module("stage14_num_alpha5", A5_PATH)
NUM3 = load_module("stage14_num3_independent", NUM3_PATH)


def compare_small_direct():
    rows = []
    previous_alpha = set()
    previous_bound = 0
    for B in SMALL_DIRECT_CUTS:
        t0 = time.perf_counter()
        alpha, ap = A5.stream_pruned(B)
        ordinary, index_profile, kernel_profile = NUM3.enumerate_chunk(B, 0, 1)
        if alpha != ordinary:
            raise ArithmeticError(
                f"alpha5/ordinary-num3 raw-set mismatch B={B}; "
                f"missing={sorted(ordinary-alpha)[:10]} extra={sorted(alpha-ordinary)[:10]}"
            )
        if previous_alpha and not previous_alpha <= alpha:
            raise ArithmeticError(f"alpha census is not nested from B={previous_bound} to B={B}")
        alpha_summary = NUM3.summarize(alpha)
        ordinary_summary = NUM3.summarize(ordinary)
        if alpha_summary != ordinary_summary:
            raise ArithmeticError(f"independent summary mismatch B={B}")
        rows.append({
            "bound": B,
            "objects": len(alpha),
            "raw_object_mask_sets_equal": True,
            "independent_num3_summary_equal": True,
            "alpha_profile": ap,
            "ordinary_num3_index_profile": index_profile,
            "ordinary_num3_kernel_profile": kernel_profile,
            "summary": alpha_summary,
            "wall_seconds_combined": time.perf_counter() - t0,
        })
        previous_alpha = alpha
        previous_bound = B
    return rows


def num1_expected():
    m = json.loads(NUM1_MANIFEST.read_text(encoding="utf-8"))
    return {
        "counts": m["counts"],
        "distinct_physical_cuboids": m["counts"]["total"] + m["counts"]["triple"],
        "object_key_sha256": m["hashes"]["object_key_sha256"],
        "object_key_mask_sha256": m["hashes"]["object_key_mask_sha256"],
        "graph": {
            "raw_pair_edges": m["graph"]["raw_pair_edges"],
            "active_oriented_face_vertices": m["graph"]["active_oriented_face_vertices"],
            "max_degree": m["graph"]["max_degree"],
            "vertex_ledger_sha256": m["hashes"]["vertex_ledger_sha256"],
            "edge_ledger_sha256": m["hashes"]["edge_ledger_sha256"],
        },
    }


def num3_expected(B: int):
    m = json.loads(NUM3_MANIFEST.read_text(encoding="utf-8"))
    return m["completed_cutoffs"][str(B)]


def compare_summary_to_frozen(B: int, got: dict, want: dict):
    checks = {
        "counts": got["counts"] == want["counts"],
        "distinct_physical_cuboids": got["distinct_physical_cuboids"] == want["distinct_physical_cuboids"],
        "object_key_sha256": got["object_key_sha256"] == want["object_key_sha256"],
        "object_key_mask_sha256": got["object_key_mask_sha256"] == want["object_key_mask_sha256"],
        "raw_pair_edges": got["graph"]["raw_pair_edges"] == want["graph"]["raw_pair_edges"],
        "active_oriented_face_vertices": got["graph"]["active_oriented_face_vertices"] == want["graph"]["active_oriented_face_vertices"],
        "max_degree": got["graph"]["max_degree"] == want["graph"]["max_degree"],
        "vertex_ledger_sha256": got["graph"]["vertex_ledger_sha256"] == want["graph"]["vertex_ledger_sha256"],
        "edge_ledger_sha256": got["graph"]["edge_ledger_sha256"] == want["graph"]["edge_ledger_sha256"],
    }
    if not all(checks.values()):
        raise ArithmeticError(f"frozen equality matrix mismatch at B={B}: {checks}")
    return checks


def compare_large_frozen_matrix():
    t0 = time.perf_counter()
    objects, profile = A5.stream_pruned(MAX_LARGE_BOUND)
    rows = []
    previous = set()
    for B in LARGE_MATRIX_CUTS:
        subset = {r for r in objects if r[3] <= B}
        if previous and not previous <= subset:
            raise ArithmeticError(f"large alpha census nesting failure at B={B}")
        got = NUM3.summarize(subset)
        want = num1_expected() if B == 2_000_000 else num3_expected(B)
        checks = compare_summary_to_frozen(B, got, want)
        rows.append({
            "bound": B,
            "objects": len(subset),
            "all_frozen_fields_equal": True,
            "checks": checks,
            "summary": got,
            "frozen_source": "Stage14-num1" if B == 2_000_000 else "Stage14-num3",
        })
        previous = subset
    return {
        "single_alpha5_stream_bound": MAX_LARGE_BOUND,
        "stream_profile": profile,
        "matrix": rows,
        "wall_seconds": time.perf_counter() - t0,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    small = compare_small_direct()
    large = compare_large_frozen_matrix()
    report = {
        "stage": "14-num-alpha6",
        "classification": "FINITE_EXACT_INDEPENDENT_EQUALITY_MATRIX",
        "small_direct_crosschecks": small,
        "large_frozen_matrix": large,
        "decision": {
            "STAGE14_NUM_ALPHA6": "COMPLETE_INDEPENDENT_EQUALITY_MATRIX_AND_REGRESSION_PACK",
            "SMALL_RAW_OBJECT_MASK_SETS_EQUAL_NUM3": True,
            "SMALL_CUTOFFS": list(SMALL_DIRECT_CUTS),
            "LARGE_FROZEN_CUTOFFS": list(LARGE_MATRIX_CUTS),
            "B2M_NUM1_ALL_HASHES_AND_GRAPH_MATCH": True,
            "B5M_NUM3_ALL_HASHES_AND_GRAPH_MATCH": True,
            "B10M_NUM3_ALL_HASHES_AND_GRAPH_MATCH": True,
            "CENSUS_NESTING_CHECKED": True,
            "INDEPENDENT_NUM3_SUMMARIZER_USED": True,
            "FINITE_DIAGNOSTIC_ONLY": True,
            "MEANINGFUL_END_TO_END_SPEEDUP_PROVED": False,
            "NEXT": "Stage14-num-alpha7 benchmark ordinary num versus alpha end-to-end crossover",
        },
    }
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
