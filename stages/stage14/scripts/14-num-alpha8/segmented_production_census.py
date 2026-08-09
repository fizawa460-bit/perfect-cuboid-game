#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import bz2
import importlib.util
import json
import time
from math import isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
A5_PATH = ROOT / "stages/stage14/scripts/14-num-alpha5/safe_primitive_sieve_audit.py"
NUM3_PATH = ROOT / "stages/stage14/scripts/14-num3/extended_exact_census.py"
NUM6_MANIFEST = ROOT / "stages/stage14/data/14-num6/rolling_append_manifest.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


A5 = load_module("stage14_num_alpha5_prod", A5_PATH)
NUM3 = load_module("stage14_num3_prod", NUM3_PATH)


def primes_upto(n: int):
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            start = p * p
            count = (n - start) // p + 1
            sieve[start:n + 1:p] = b"\x00" * count
    return [p for p in range(2, n + 1) if sieve[p]]


def cmul(z, w):
    a, b = z
    c, d = w
    return a * c - b * d, a * d + b * c


def cpow(z, e: int):
    out = (1, 0)
    base = z
    while e:
        if e & 1:
            out = cmul(out, base)
        base = cmul(base, base)
        e >>= 1
    return out


def prime_sum2_cornacchia(p: int, cache: dict[int, tuple[int, int]], cache_limit: int):
    if p <= cache_limit and p in cache:
        return cache[p]
    if p == 2:
        ans = (1, 1)
    else:
        if p % 4 != 1:
            raise ArithmeticError(f"Cornacchia called on nonsplit prime p={p}")
        z = 2
        while pow(z, (p - 1) // 2, p) != p - 1:
            z += 1
        r = pow(z, (p - 1) // 4, p)
        ans = None
        for root in (r, p - r):
            a, b = p, root
            while b * b > p:
                a, b = b, a % b
            x = abs(b)
            y2 = p - x * x
            if y2 < 0:
                continue
            y = isqrt(y2)
            if y * y == y2:
                ans = (min(x, y), max(x, y))
                break
        if ans is None:
            raise ArithmeticError(f"Cornacchia failed for split prime p={p}")
    if p <= cache_limit:
        cache[p] = ans
    return ans


def gaussian_reps_from_factorization(d: int, fac, cache, cache_limit: int):
    states = {(1, 0)}
    for p, e in fac:
        pi = prime_sum2_cornacchia(p, cache, cache_limit)
        pib = (pi[0], -pi[1])
        pi_pow = [cpow(pi, k) for k in range(2 * e + 1)]
        pib_pow = [cpow(pib, k) for k in range(2 * e + 1)]
        nxt = set()
        for k in range(2 * e + 1):
            factor_z = cmul(pi_pow[k], pib_pow[2 * e - k])
            for z in states:
                nxt.add(cmul(z, factor_z))
        states = nxt

    reps = set()
    for a, b in states:
        a = abs(a)
        b = abs(b)
        if a == 0 or b == 0:
            continue
        if a > b:
            a, b = b, a
        if a * a + b * b != d * d:
            raise ArithmeticError(f"Gaussian norm mismatch at d={d}")
        reps.add((a, b))
    return reps


def expected_rep_count(fac):
    prod = 1
    for _, e in fac:
        prod *= 2 * e + 1
    return (prod - 1) // 2


def scan_segment(seg_lo: int, seg_hi: int, small_primes, cache, cache_limit: int, objects: set, profile: dict):
    odd_lo = seg_lo if seg_lo & 1 else seg_lo + 1
    if odd_lo > seg_hi:
        return
    n = (seg_hi - odd_lo) // 2 + 1
    rem = [odd_lo + 2 * i for i in range(n)]
    bad = bytearray(n)
    facs = [None] * n

    for p in small_primes:
        if p == 2:
            continue
        if p * p > seg_hi:
            break
        start = ((odd_lo + p - 1) // p) * p
        if start % 2 == 0:
            start += p
        step = 2 * p
        if p % 4 == 3:
            for m in range(start, seg_hi + 1, step):
                bad[(m - odd_lo) // 2] = 1
            continue

        for m in range(start, seg_hi + 1, step):
            i = (m - odd_lo) // 2
            if bad[i]:
                continue
            x = rem[i]
            if x % p:
                continue
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            rem[i] = x
            if facs[i] is None:
                facs[i] = [(p, e)]
            else:
                facs[i].append((p, e))

    for i in range(n):
        profile["odd_diagonals_examined"] += 1
        if bad[i]:
            profile["small_inert_factor_rejects"] += 1
            continue
        d = odd_lo + 2 * i
        r = rem[i]
        fac = list(facs[i] or ())
        if r > 1:
            if r % 4 != 1:
                profile["large_inert_residual_rejects"] += 1
                continue
            fac.append((r, 1))
        if not fac:
            profile["trivial_rejects"] += 1
            continue

        want_reps = expected_rep_count(fac)
        if want_reps < 2:
            profile["fewer_than_two_rep_rejects"] += 1
            continue

        profile["diagonals_kept_by_outer_sieve"] += 1
        reps = gaussian_reps_from_factorization(d, fac, cache, cache_limit)
        profile["representation_count_formula_checks"] += 1
        if len(reps) != want_reps:
            raise ArithmeticError(
                f"representation count mismatch d={d}: expected={want_reps} got={len(reps)} fac={fac}"
            )
        A5.collide_reps_pruned(d, reps, profile, objects)


def scan_range(lo: int, hi: int, segment_size: int, cache_limit: int):
    if lo < 1 or hi < lo:
        raise ValueError("invalid scan range")
    t0 = time.perf_counter()
    small_primes = primes_upto(isqrt(hi))
    cache = {}
    objects = set()
    profile = {
        "range_lo": lo,
        "range_hi": hi,
        "segment_size": segment_size,
        "diagonals_scanned": hi - lo + 1,
        "odd_diagonals_examined": 0,
        "small_inert_factor_rejects": 0,
        "large_inert_residual_rejects": 0,
        "trivial_rejects": 0,
        "fewer_than_two_rep_rejects": 0,
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
    seg_lo = lo
    while seg_lo <= hi:
        seg_hi = min(hi, seg_lo + segment_size - 1)
        scan_segment(seg_lo, seg_hi, small_primes, cache, cache_limit, objects, profile)
        seg_lo = seg_hi + 1
    profile["prime_sum2_cache_entries"] = len(cache)
    profile["objects"] = len(objects)
    profile["seconds"] = time.perf_counter() - t0
    return objects, profile


def compare_summary(got: dict, want: dict):
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
    return checks


def write_object_source(objects, path: Path):
    rows = ["a,b,c,d,mask"]
    rows.extend(",".join(map(str, r)) for r in sorted(objects))
    raw = ("\n".join(rows) + "\n").encode("utf-8")
    encoded = base64.b64encode(bz2.compress(raw, compresslevel=9)).decode("ascii")
    path.write_text(encoded + "\n", encoding="utf-8")
    return {
        "rows": len(objects),
        "raw_bytes": len(raw),
        "bz2_base64_chars": len(encoded),
    }


def cmd_scan(args):
    objects, profile = scan_range(args.lo, args.hi, args.segment_size, args.cache_limit)
    payload = {
        "range": [args.lo, args.hi],
        "objects": [list(r) for r in sorted(objects)],
        "profile": profile,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, separators=(",", ":")) + "\n", encoding="utf-8")
    print(json.dumps({"range": payload["range"], "objects": len(objects), "profile": profile}, indent=2, sort_keys=True))


def cmd_aggregate(args):
    t0 = time.perf_counter()
    files = sorted(args.input_dir.glob("shard-*.json"))
    if not files:
        raise RuntimeError("no shard files found")
    shards = []
    objects = set()
    profiles = []
    for path in files:
        data = json.loads(path.read_text(encoding="utf-8"))
        lo, hi = data["range"]
        shards.append((lo, hi))
        profiles.append(data["profile"])
        for row in data["objects"]:
            rec = tuple(row)
            if rec in objects:
                raise ArithmeticError(f"duplicate record across shards: {rec}")
            objects.add(rec)
    shards.sort()
    expect = 1
    for lo, hi in shards:
        if lo != expect:
            raise ArithmeticError(f"shard coverage gap/overlap: expected lo={expect}, got {lo}")
        expect = hi + 1
    if expect != args.bound + 1:
        raise ArithmeticError(f"shards end at {expect-1}, expected {args.bound}")

    manifest = json.loads(NUM6_MANIFEST.read_text(encoding="utf-8"))
    subset = {r for r in objects if r[3] <= args.regression_bound}
    got_reg = NUM3.summarize(subset)
    want_reg = manifest["exact_cutoff_B150m"]
    checks = compare_summary(got_reg, want_reg)
    if not all(checks.values()):
        raise ArithmeticError(f"B150m alpha8 regression mismatch: {checks}")

    summary = NUM3.summarize(objects)
    source_profile = write_object_source(objects, args.object_source)
    new_counts = {
        k: summary["counts"][k] - got_reg["counts"][k]
        for k in ("a", "b", "c", "total", "triple")
    }
    report = {
        "stage": "14-num-alpha8",
        "classification": "FINITE_EXACT_SEGMENTED_ALPHA_SCALEOUT",
        "bound": args.bound,
        "regression_bound": args.regression_bound,
        "shards": [{"range": list(r), "profile": p} for r, p in zip(shards, profiles)],
        "B150m_regression": {"all_fields_equal": True, "checks": checks, "summary": got_reg},
        "B200m_exact": summary,
        "new_shell_150m_to_200m_counts": new_counts,
        "object_source": source_profile,
        "aggregate_seconds": time.perf_counter() - t0,
        "decision": {
            "STAGE14_NUM_ALPHA8": "COMPLETE_EXACT_B200M_ALPHA_SCALEOUT",
            "SEGMENTED_DIAGONAL_SHARDS_EXACT_DISJOINT_UNION": True,
            "B150M_NUM6_FULL_HASH_REGRESSION_MATCH": True,
            "B200M_EXACT_CENSUS_FROZEN": True,
            "EXTENDS_BEYOND_ORDINARY_B150M_CUTOFF": True,
            "PERFECT_CUBOID_EMERGENCY": summary["counts"]["triple"] > 0,
            "FINITE_DIAGNOSTIC_ONLY": True,
            "ASYMPTOTIC_CLAIM": False,
            "NEXT": "Stage14-num-alpha9 optional historical-interval validation / alpha10+ only on demonstrated value",
        },
    }
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("scan")
    sp.add_argument("--lo", type=int, required=True)
    sp.add_argument("--hi", type=int, required=True)
    sp.add_argument("--segment-size", type=int, default=250_000)
    sp.add_argument("--cache-limit", type=int, default=2_000_000)
    sp.add_argument("--output", type=Path, required=True)
    sp.set_defaults(func=cmd_scan)

    ag = sub.add_parser("aggregate")
    ag.add_argument("--input-dir", type=Path, required=True)
    ag.add_argument("--bound", type=int, default=200_000_000)
    ag.add_argument("--regression-bound", type=int, default=150_000_000)
    ag.add_argument("--output", type=Path, required=True)
    ag.add_argument("--object-source", type=Path, required=True)
    ag.set_defaults(func=cmd_aggregate)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
