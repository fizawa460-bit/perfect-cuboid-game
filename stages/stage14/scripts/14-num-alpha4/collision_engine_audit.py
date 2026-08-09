#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import time
from collections import defaultdict
from itertools import combinations
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
ALPHA2_SCRIPT = ROOT / "stages/stage14/scripts/14-num-alpha2/alpha_reference_overlap.py"
ALPHA3_SCRIPT = ROOT / "stages/stage14/scripts/14-num-alpha3/representation_generation_audit.py"
NUM1_MANIFEST = ROOT / "stages/stage14/data/14-num1/baseline_manifest.json"

SQ64 = {i * i % 64 for i in range(64)}
SQ63 = {i * i % 63 for i in range(63)}


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


A2 = load_module("stage14_num_alpha2", ALPHA2_SCRIPT)
A3 = load_module("stage14_num_alpha3", ALPHA3_SCRIPT)


def square_after_residue_filter(n: int, profile: dict) -> int | None:
    if n <= 0:
        return None
    profile["positive_residuals"] += 1
    if n % 64 not in SQ64 or n % 63 not in SQ63:
        profile["residue_filter_rejects"] += 1
        return None
    profile["isqrt_tests"] += 1
    r = isqrt(n)
    return r if r * r == n else None


def canonical_record(x: int, y: int, z: int, d: int):
    a, b, c = sorted((x, y, z))
    if not (0 < a < b < c):
        return None
    if gcd(a, gcd(b, c)) != 1:
        return None
    if a * a + b * b + c * c != d * d:
        raise ArithmeticError("collision reconstruction failed")
    mask, _ = A2.face_mask(a, b, c)
    if mask.bit_count() < 2:
        raise ArithmeticError("collision produced fewer than two integral faces")
    return (a, b, c, d, mask)


def brute_collide_table(table):
    """Alpha2 ordered-role reference, but reuse a supplied representation table."""
    t0 = time.perf_counter()
    objects = set()
    profile = {
        "diagonals_with_two_plus_reps": 0,
        "ordered_role_pair_tests": 0,
        "positive_residuals": 0,
        "isqrt_tests": 0,
        "square_hits": 0,
    }
    for d, reps in table.items():
        if len(reps) < 2:
            continue
        profile["diagonals_with_two_plus_reps"] += 1
        roles = []
        for u, v in sorted(reps):
            roles.append((u, v))
            roles.append((v, u))
        for (a, fa), (b, fb) in combinations(roles, 2):
            profile["ordered_role_pair_tests"] += 1
            if a == b:
                continue
            c2 = d * d - a * a - b * b
            if c2 <= 0:
                continue
            profile["positive_residuals"] += 1
            profile["isqrt_tests"] += 1
            c = isqrt(c2)
            if c * c != c2:
                continue
            if fa * fa - b * b != c2 or fb * fb - a * a != c2:
                raise ArithmeticError("ordered-role identity failure")
            profile["square_hits"] += 1
            rec = canonical_record(a, b, c, d)
            if rec is not None:
                objects.add(rec)
    profile["objects"] = len(objects)
    profile["seconds"] = time.perf_counter() - t0
    return objects, profile


def compressed_collide_reps(d: int, reps, profile: dict, objects: set):
    """Exact algebraic compression of all positive ordered-role residuals.

    Let two unordered representations be (A,F),(B,E) with A<B and hence F>E.
    The four cross-role choices have residuals

      (A,B): E^2-A^2
      (A,E): B^2-A^2
      (F,B): A^2-B^2 < 0
      (F,E): A^2-E^2

    so only the first two, plus the last when A>E, can be positive.  This is
    exactly the alpha2 ordered-role search with the impossible branch removed.
    """
    rr = sorted(reps)
    if len(rr) < 2:
        return
    profile["diagonals_with_two_plus_reps"] += 1
    for (A, F), (B, E) in combinations(rr, 2):
        profile["representation_pair_tests"] += 1
        if not (A < B and F > E):
            raise ArithmeticError("fixed-norm representation ordering invariant failed")

        candidates = [
            (A, B, E * E - A * A),
            (A, E, B * B - A * A),
        ]
        if A > E:
            candidates.append((F, E, A * A - E * E))
        profile["algebraic_candidate_residuals"] += len(candidates)

        for x, y, c2 in candidates:
            c = square_after_residue_filter(c2, profile)
            if c is None:
                continue
            profile["square_hits"] += 1
            rec = canonical_record(x, y, c, d)
            if rec is not None:
                objects.add(rec)


def compressed_collide_table(table):
    t0 = time.perf_counter()
    objects = set()
    profile = {
        "diagonals_with_two_plus_reps": 0,
        "representation_pair_tests": 0,
        "algebraic_candidate_residuals": 0,
        "positive_residuals": 0,
        "residue_filter_rejects": 0,
        "isqrt_tests": 0,
        "square_hits": 0,
    }
    for d, reps in table.items():
        compressed_collide_reps(d, reps, profile, objects)
    profile["objects"] = len(objects)
    profile["seconds"] = time.perf_counter() - t0
    return objects, profile


def compare_collision_engines(bound: int):
    table, generation = A3.gaussian_table(bound)
    brute, bp = brute_collide_table(table)
    compact, cp = compressed_collide_table(table)
    if brute != compact:
        raise ArithmeticError(
            f"compressed collision mismatch; missing={sorted(brute-compact)[:10]} extra={sorted(compact-brute)[:10]}"
        )
    return {
        "bound": bound,
        "representation_generation": generation,
        "objects": len(brute),
        "object_sets_equal": True,
        "brute": bp,
        "compressed": cp,
        "isqrt_reduction_fraction": 1.0 - cp["isqrt_tests"] / max(1, bp["isqrt_tests"]),
        "collision_seconds_ratio_brute_over_compressed": bp["seconds"] / max(cp["seconds"], 1e-12),
    }


def stream_compressed(bound: int):
    """Memory-light alpha3 generation + alpha4 collision path, one d at a time."""
    t0 = time.perf_counter()
    spf = A3.spf_sieve(bound)
    cache = {}
    objects = set()
    profile = {
        "diagonals_scanned": bound,
        "diagonals_with_any_nontrivial_rep": 0,
        "diagonals_with_two_plus_reps": 0,
        "representation_pair_tests": 0,
        "algebraic_candidate_residuals": 0,
        "positive_residuals": 0,
        "residue_filter_rejects": 0,
        "isqrt_tests": 0,
        "square_hits": 0,
    }
    for d in range(1, bound + 1):
        fac = A3.factor(d, spf)
        if not any(p % 4 == 1 for p, _ in fac):
            continue
        reps = A3.gaussian_reps_for_d(d, spf, cache)
        if reps:
            profile["diagonals_with_any_nontrivial_rep"] += 1
        compressed_collide_reps(d, reps, profile, objects)
    profile["objects"] = len(objects)
    profile["prime_sum2_cache"] = len(cache)
    profile["seconds"] = time.perf_counter() - t0
    return objects, profile


def verify_frozen_b2m(bound: int):
    manifest = json.loads(NUM1_MANIFEST.read_text(encoding="utf-8"))
    objects, profile = stream_compressed(bound)
    got = A2.summarize(objects)
    want_hashes = manifest["hashes"]
    checks = {
        "counts": got["counts"] == manifest["counts"],
        "graph_counts": all(
            got["graph"][k] == manifest["graph"][k]
            for k in ("raw_pair_edges", "active_oriented_face_vertices", "max_degree")
        ),
        "object_key_sha256": got["object_key_sha256"] == want_hashes["object_key_sha256"],
        "object_key_mask_sha256": got["object_key_mask_sha256"] == want_hashes["object_key_mask_sha256"],
        "vertex_ledger_sha256": got["graph"]["vertex_ledger_sha256"] == want_hashes["vertex_ledger_sha256"],
        "edge_ledger_sha256": got["graph"]["edge_ledger_sha256"] == want_hashes["edge_ledger_sha256"],
    }
    if not all(checks.values()):
        raise ArithmeticError(f"alpha4 frozen B={bound} regression failed: {checks}")
    return {"bound": bound, "checks": checks, "summary": got, "profile": profile}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--audit-bound", type=int, default=200_000)
    ap.add_argument("--frozen-bound", type=int, default=2_000_000)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    audit = compare_collision_engines(args.audit_bound)
    frozen = verify_frozen_b2m(args.frozen_bound)
    report = {
        "stage": "14-num-alpha4",
        "classification": "FINITE_EXACT_COLLISION_ENGINE_AUDIT",
        "audit": audit,
        "frozen_regression": frozen,
        "decision": {
            "STAGE14_NUM_ALPHA4": "COMPLETE_EXACT_COMPRESSED_COLLISION_ENGINE",
            "COMPRESSED_COLLISION_OBJECT_SET_EQUALS_ORDERED_ROLE_REFERENCE": True,
            "ALGEBRAIC_POSITIVE_ROLE_COMPRESSION_EXACT": True,
            "SQUARE_RESIDUE_PREFILTER_EXACT_NO_FALSE_NEGATIVES": True,
            "STREAMED_GAUSSIAN_COLLISION_B2M_MATCHES_FROZEN_NUM1": True,
            "ALPHA3_CI_SUCCESS_IMPORTED": True,
            "MEANINGFUL_END_TO_END_SPEEDUP_PROVED": False,
            "FINITE_DIAGNOSTIC_ONLY": True,
            "NEXT": "Stage14-num-alpha5 safe-pruning theorem pack / primitive diagonal transfer",
        },
    }
    txt = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(txt, encoding="utf-8")
    print(txt, end="")


if __name__ == "__main__":
    main()
