#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import time
from collections import Counter
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
A2_PATH = ROOT / "stages/stage14/scripts/14-num-alpha2/alpha_reference_overlap.py"
A3_PATH = ROOT / "stages/stage14/scripts/14-num-alpha3/representation_generation_audit.py"
A4_PATH = ROOT / "stages/stage14/scripts/14-num-alpha4/collision_engine_audit.py"
MANIFEST_PATH = ROOT / "stages/stage14/data/14-num1/baseline_manifest.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


A2 = load_module("stage14_num_alpha2", A2_PATH)
A3 = load_module("stage14_num_alpha3", A3_PATH)
A4 = load_module("stage14_num_alpha4", A4_PATH)


def positive_unordered_rep_count_for_split_d(fac) -> int:
    """Number of positive unordered nontrivial reps d^2=x^2+y^2 for all-split d.

    If d=prod p_i^e_i with every p_i == 1 mod 4, then
      r_2(d^2)=4 prod(2e_i+1).
    Removing the four axis representations and quotienting by 8 sign/order
    symmetries gives (prod(2e_i+1)-1)/2.
    """
    if not fac:
        return 0
    if any(p % 4 != 1 for p, _ in fac):
        raise ValueError("formula is only for odd all-split diagonals")
    prod = 1
    for _, e in fac:
        prod *= 2 * e + 1
    return (prod - 1) // 2


def classify_diagonal(d: int, fac):
    """Return (keep, reason, exact_rep_count_if_split).

    Primitive Stage14 objects with >=1 integral face cannot have 2 or a
    3 mod 4 prime dividing d: from d^2=a^2+F^2 such a prime forces a,F,
    then the two edges under F, to share that prime. Hence the box is not
    primitive. For all-split d, at least two distinct nontrivial reps are
    necessary for an alpha pair collision.
    """
    if d <= 1:
        return False, "TRIVIAL", 0
    if d % 2 == 0:
        return False, "EVEN_DIAGONAL_NONPRIMITIVE", None
    if any(p % 4 == 3 for p, _ in fac):
        return False, "INERT_3MOD4_FACTOR_NONPRIMITIVE", None
    # Odd and no 3 mod 4 factor: every prime factor is 1 mod 4.
    rep_count = positive_unordered_rep_count_for_split_d(fac)
    if rep_count < 2:
        return False, "FEWER_THAN_TWO_NONTRIVIAL_REPRESENTATIONS", rep_count
    return True, "KEEP", rep_count


def collide_reps_pruned(d: int, reps, profile: dict, objects: set):
    rr = sorted(reps)
    if len(rr) < 2:
        return
    profile["diagonals_with_two_plus_reps"] += 1
    from itertools import combinations
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
            if c2 <= 0:
                raise ArithmeticError("alpha4 positive-role compression emitted nonpositive residual")
            profile["candidate_positive_residuals"] += 1

            # Stage14 canonical semantics require strict edge inequalities.
            if x == y:
                profile["equal_edge_rejects_before_sqrt"] += 1
                continue

            # If p | gcd(d,x,y) and c^2=d^2-x^2-y^2 is a square, then p|c.
            # Such a hit is necessarily nonprimitive, so reject before sqrt.
            if gcd(d, gcd(x, y)) > 1:
                profile["common_divisor_rejects_before_sqrt"] += 1
                continue

            c = A4.square_after_residue_filter(c2, profile)
            if c is None:
                continue
            profile["square_hits"] += 1
            rec = A4.canonical_record(x, y, c, d)
            if rec is not None:
                objects.add(rec)


def stream_pruned(bound: int):
    t0 = time.perf_counter()
    spf = A3.spf_sieve(bound)
    cache = {}
    objects = set()
    reasons = Counter()
    profile = {
        "diagonals_scanned": bound,
        "diagonals_kept_by_outer_sieve": 0,
        "diagonals_with_two_plus_reps": 0,
        "representation_count_formula_checks": 0,
        "representation_pair_tests": 0,
        "algebraic_candidate_residuals": 0,
        "candidate_positive_residuals": 0,
        "equal_edge_rejects_before_sqrt": 0,
        "common_divisor_rejects_before_sqrt": 0,
        "positive_residuals": 0,
        "residue_filter_rejects": 0,
        "isqrt_tests": 0,
        "square_hits": 0,
    }

    for d in range(1, bound + 1):
        fac = A3.factor(d, spf)
        keep, reason, expected_reps = classify_diagonal(d, fac)
        reasons[reason] += 1
        if not keep:
            continue
        profile["diagonals_kept_by_outer_sieve"] += 1
        reps = A3.gaussian_reps_for_d(d, spf, cache)
        profile["representation_count_formula_checks"] += 1
        if len(reps) != expected_reps:
            raise ArithmeticError(
                f"sum-of-two-squares count formula mismatch at d={d}: "
                f"expected={expected_reps} got={len(reps)}"
            )
        collide_reps_pruned(d, reps, profile, objects)

    profile["outer_sieve_reasons"] = dict(sorted(reasons.items()))
    profile["objects"] = len(objects)
    profile["prime_sum2_cache"] = len(cache)
    profile["seconds"] = time.perf_counter() - t0
    return objects, profile


def compare_against_alpha4(bound: int):
    baseline, bp = A4.stream_compressed(bound)
    pruned, pp = stream_pruned(bound)
    if baseline != pruned:
        raise ArithmeticError(
            f"alpha5 pruning mismatch B={bound}; "
            f"missing={sorted(baseline-pruned)[:10]} extra={sorted(pruned-baseline)[:10]}"
        )
    return {
        "bound": bound,
        "object_sets_equal": True,
        "objects": len(pruned),
        "alpha4_baseline_profile": bp,
        "alpha5_pruned_profile": pp,
        "seconds_ratio_alpha4_over_alpha5": bp["seconds"] / max(pp["seconds"], 1e-12),
    }


def verify_frozen(bound: int):
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    objects, profile = stream_pruned(bound)
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
        raise ArithmeticError(f"alpha5 frozen B={bound} regression failed: {checks}")
    return {"bound": bound, "checks": checks, "summary": got, "profile": profile}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--audit-bound", type=int, default=200_000)
    ap.add_argument("--frozen-bound", type=int, default=2_000_000)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    audit = compare_against_alpha4(args.audit_bound)
    frozen = verify_frozen(args.frozen_bound)
    report = {
        "stage": "14-num-alpha5",
        "classification": "FINITE_EXACT_SAFE_PRIMITIVE_SIEVE_AUDIT",
        "audit": audit,
        "frozen_regression": frozen,
        "decision": {
            "STAGE14_NUM_ALPHA5": "COMPLETE_SAFE_PRIMITIVE_DIAGONAL_AND_PAIR_SIEVE",
            "PRIMITIVE_DIAGONAL_ODD_PROVED": True,
            "PRIMITIVE_DIAGONAL_NO_3MOD4_PRIME_FACTOR_PROVED": True,
            "ALL_PRIMITIVE_DIAGONAL_PRIMES_1MOD4": True,
            "EXACT_REPRESENTATION_COUNT_FORMULA_USED": True,
            "TWO_DISTINCT_REPRESENTATIONS_NECESSARY": True,
            "PAIR_COMMON_DIVISOR_PREFILTER_SAFE": True,
            "STRICT_EQUAL_EDGE_PREFILTER_MATCHES_STAGE14_CANONICAL_SEMANTICS": True,
            "PRUNED_OBJECT_SET_EQUALS_ALPHA4": True,
            "PRUNED_B2M_MATCHES_FROZEN_NUM1": True,
            "HISTORICAL_MOD11_MOD19_PRUNING_IMPORTED": False,
            "MEANINGFUL_END_TO_END_SPEEDUP_PROVED": False,
            "FINITE_DIAGNOSTIC_ONLY": True,
            "NEXT": "Stage14-num-alpha6 exact frozen-cutoff equality matrix and independent regression pack",
        },
    }
    txt = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(txt, encoding="utf-8")
    print(txt, end="")


if __name__ == "__main__":
    main()
