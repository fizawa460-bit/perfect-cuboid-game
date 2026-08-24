#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import pathlib
import time
from collections import Counter

import z3

EXPECTED_CORE_SHA = "de84f4511ea2ea747fd712e2f5f09c7f8d94ae3633e55678b81cfe63f6ed2870"
EXPECTED_SOURCE_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
DEGREE = 16
GENUS = 0
NORM_BOUND = 34
NORMAL_CAP = 8
EXCEPTIONAL_CAP = 4


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    ).hexdigest()


def egcd(a: int, b: int) -> tuple[int, int, int]:
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = old_t - q * t, old_t
    # Repair the t-update above by recomputing if necessary.  Keeping the
    # implementation explicit avoids relying on external algebra packages.
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    if old_r < 0:
        old_r, old_s, old_t = -old_r, -old_s, -old_t
    return old_r, old_s, old_t


def row_times_matrix(row: list[int], matrix: list[list[int]]) -> list[int]:
    return [sum(row[i] * matrix[i][j] for i in range(len(row))) for j in range(len(matrix[0]))]


def kernel_basis_primitive_row(row: list[int]) -> tuple[list[list[int]], int]:
    n = len(row)
    g_all = 0
    for value in row:
        g_all = math.gcd(g_all, abs(value))
    assert g_all > 0
    r = [value // g_all for value in row]
    v = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    pivot = next(i for i, value in enumerate(r) if value)
    if pivot:
        for i in range(n):
            v[i][0], v[i][pivot] = v[i][pivot], v[i][0]
        r[0], r[pivot] = r[pivot], r[0]
    for j in range(1, n):
        if r[j] == 0:
            continue
        d, s, t = egcd(r[0], r[j])
        a, b = r[0], r[j]
        old0 = [v[i][0] for i in range(n)]
        oldj = [v[i][j] for i in range(n)]
        for i in range(n):
            v[i][0] = s * old0[i] + t * oldj[i]
            v[i][j] = (-b // d) * old0[i] + (a // d) * oldj[i]
        r[0] = d
        r[j] = 0
    assert abs(r[0]) == 1 and all(value == 0 for value in r[1:])
    basis = [[v[i][j] for j in range(1, n)] for i in range(n)]
    primitive = [value // g_all for value in row]
    assert all(value == 0 for value in row_times_matrix(primitive, basis))
    return basis, g_all


def rank_mod(rows: list[list[int]], p: int) -> int:
    a = [[v % p for v in row] for row in rows]
    m, n = len(a), len(a[0])
    rank = 0
    for col in range(n):
        pivot = next((r for r in range(rank, m) if a[r][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], p - 2, p)
        a[rank] = [(v * inv) % p for v in a[rank]]
        for r in range(m):
            if r == rank or not a[r][col]:
                continue
            f = a[r][col]
            a[r] = [(a[r][c] - f * a[rank][c]) % p for c in range(n)]
        rank += 1
        if rank == n:
            break
    return rank


def linexpr(coeffs: list[int], vars_: list[z3.ArithRef], offset: int = 0) -> z3.ArithRef:
    terms = [int(a) * vars_[i] for i, a in enumerate(coeffs) if int(a)]
    if offset:
        terms.append(z3.IntVal(int(offset)))
    return z3.Sum(terms) if terms else z3.IntVal(0)


def exact_norm(gram: list[list[int]], basis: list[list[int]], z: list[int]) -> tuple[int, list[int]]:
    y = [sum(basis[i][j] * z[j] for j in range(63)) for i in range(64)]
    y2 = sum(y[i] * gram[i][j] * y[j] for i in range(64) for j in range(64))
    return -y2, y


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--core", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    ap.add_argument("--max-models", type=int, default=200000)
    ap.add_argument("--max-seconds", type=float, default=600.0)
    ap.add_argument("--check-timeout-ms", type=int, default=10000)
    args = ap.parse_args()

    core = json.loads(args.core.read_text())
    unsigned = dict(core)
    claimed = unsigned.pop("canonical_sha256_without_this_field")
    assert claimed == EXPECTED_CORE_SHA == csha(unsigned)
    assert core["source"]["git_blob_sha1"] == EXPECTED_SOURCE_BLOB
    assert int(core["rank"]) == 64 and int(core["h2"]) == 16

    gram = [[int(v) for v in row] for row in core["basis_gram"]]
    h = [int(v) for v in core["hyperplane"]]
    known = [[int(v) for v in row] for row in core["raw_cross_pairings_with_basis"]]
    assert len(known) == 140
    hrow = [sum(h[i] * gram[i][j] for i in range(64)) for j in range(64)]
    assert sum(hrow[i] * h[i] for i in range(64)) == DEGREE

    basis, hrow_content = kernel_basis_primitive_row(hrow)
    assert hrow_content == 2
    assert all(v == 0 for v in row_times_matrix(hrow, basis))

    offsets = [sum(row[i] * h[i] for i in range(64)) for row in known]
    coeffs = [row_times_matrix(row, basis) for row in known]
    rank_1000003 = rank_mod(coeffs, 1_000_003)
    rank_1000033 = rank_mod(coeffs, 1_000_033)
    assert rank_1000003 == rank_1000033 == 63

    # The 140 bounded linear pairings have full H-perp rank, so this is a
    # bounded integer polytope.  Enumerate that polytope first; only then
    # evaluate the expensive exact quadratic norm.
    z = [z3.Int(f"z{i}") for i in range(63)]
    solver = z3.SolverFor("QF_LIA")
    solver.set(random_seed=0, timeout=int(args.check_timeout_ms))

    # Put the tighter exceptional caps first, then the normal caps.  Z3 sees
    # all constraints simultaneously, but this records the intended pruning
    # architecture and keeps the formula purely linear.
    order = list(range(92, 140)) + list(range(92))
    for i in order:
        p = linexpr(coeffs[i], z, offsets[i])
        cap = EXCEPTIONAL_CAP if i >= 92 else NORMAL_CAP
        solver.add(p >= 0, p <= cap)

    started = time.perf_counter()
    models = 0
    norm_survivors = 0
    terminal = "RUNNING"
    norm_hist: Counter[int] = Counter()
    parent_hist: Counter[tuple[int, int]] = Counter()
    sample: list[dict] = []
    stream_digest = hashlib.sha256()
    min_norm_seen: int | None = None
    max_abs_z_seen = 0
    last_check_seconds = 0.0

    while True:
        if models >= args.max_models:
            terminal = "MODEL_CAP"
            break
        if time.perf_counter() - started >= args.max_seconds:
            terminal = "WALL_TIME_CAP"
            break
        t0 = time.perf_counter()
        result = solver.check()
        last_check_seconds = time.perf_counter() - t0
        if result == z3.unsat:
            terminal = "POLYTOPE_EXHAUSTED_UNSAT_AFTER_BLOCKS"
            break
        if result == z3.unknown:
            terminal = "UNKNOWN"
            break

        model = solver.model()
        zv = [model.eval(v, model_completion=True).as_long() for v in z]
        models += 1
        max_abs_z_seen = max(max_abs_z_seen, max(abs(v) for v in zv))

        pairings = [offsets[i] + sum(coeffs[i][j] * zv[j] for j in range(63)) for i in range(140)]
        assert all(0 <= pairings[i] <= NORMAL_CAP for i in range(92))
        assert all(0 <= pairings[i] <= EXCEPTIONAL_CAP for i in range(92, 140))

        norm, y = exact_norm(gram, basis, zv)
        min_norm_seen = norm if min_norm_seen is None else min(min_norm_seen, norm)
        raw = json.dumps(zv, separators=(",", ":")).encode()
        stream_digest.update(hashlib.sha256(raw).digest())

        if 0 <= norm <= NORM_BOUND:
            c = [h[i] + y[i] for i in range(64)]
            c2 = sum(c[i] * gram[i][j] * c[j] for i in range(64) for j in range(64))
            assert c2 == DEGREE - norm
            if c2 >= -DEGREE - 2 + 2 * GENUS:
                norm_survivors += 1
                norm_hist[norm] += 1
                parent = (sum(pairings[92:]), sum(pairings[:46]))
                parent_hist[parent] += 1
                if len(sample) < 20:
                    sample.append({
                        "norm": norm,
                        "self_intersection": c2,
                        "exceptional_mass": parent[0],
                        "curve_group_mass": parent[1],
                        "z_sha256": hashlib.sha256(raw).hexdigest(),
                    })

        solver.add(z3.Or([z[j] != zv[j] for j in range(63)]))

    elapsed = time.perf_counter() - started
    report = {
        "schema": "STAGE32_SCOUT_D16_140FIRST_QF_LIA_THEN_EXACT_NORM_V1",
        "scope": "SCOUT_ONLY_NO_CREDIT",
        "source_core_canonical_sha256": EXPECTED_CORE_SHA,
        "source_blob_sha1": EXPECTED_SOURCE_BLOB,
        "parameters": {
            "degree": DEGREE,
            "genus": GENUS,
            "hperp_rank": 63,
            "hperp_norm_bound": NORM_BOUND,
            "normal_intersection_cap": NORMAL_CAP,
            "exceptional_intersection_cap": EXCEPTIONAL_CAP,
            "max_models": args.max_models,
            "max_seconds": args.max_seconds,
            "check_timeout_ms": args.check_timeout_ms,
        },
        "architecture": {
            "direction": "ALL_140_LINEAR_INTERSECTION_CAPS_FIRST_THEN_EXACT_QUADRATIC_NORM",
            "solver": "Z3_QF_LIA_ONLY",
            "quadratic_constraint_inside_solver": False,
            "exceptional_caps_added_before_normal_caps": True,
            "bounded_polytope_rank_mod_1000003": rank_1000003,
            "bounded_polytope_rank_mod_1000033": rank_1000033,
            "materialized_branch_count_constructed": 0,
            "short_vector_ball_materialized": False,
        },
        "terminal_status": terminal,
        "linear_models_exactly_checked": models,
        "norm_le_34_survivors_in_prefix": norm_survivors,
        "elapsed_seconds": round(elapsed, 6),
        "last_solver_check_seconds": round(last_check_seconds, 6),
        "models_per_second": round(models / elapsed, 6) if elapsed else None,
        "minimum_exact_norm_seen": min_norm_seen,
        "maximum_abs_kernel_coordinate_seen": max_abs_z_seen,
        "norm_histogram_survivors": {str(k): v for k, v in sorted(norm_hist.items())},
        "parent_histogram_top20": [
            {"exceptional_mass": e, "curve_group_mass": a, "count": n}
            for (e, a), n in parent_hist.most_common(20)
        ],
        "sample_survivors": sample,
        "linear_model_stream_digest": stream_digest.hexdigest(),
        "interpretation": {
            "purpose": "TEST_CONSTRAINT_ORDERING_TO_BYPASS_BOTH_QFNIA_UNKNOWN_AND_NORM8_SHORT_VECTOR_EXPLOSION",
            "prefix_only_unless_polytope_exhausted": terminal != "POLYTOPE_EXHAUSTED_UNSAT_AFTER_BLOCKS",
            "no_row_completeness_credit": True,
            "no_theorem_credit": True,
        },
        "THEOREM_CREDIT": False,
        "RECEIVER_CREDIT": False,
        "FULL_D16_G0_ROW_COMPLETE": False,
        "FULL_D176_D192_NUMERICAL_ORBIT_CENSUS": False,
        "R29_LG2_NUMERICAL_COMPONENT_COMPLETE": False,
        "R29_LG2": "NOT_DISCHARGED",
        "G10_LOWGENUS_PICARD": "AMBER",
    }
    report["canonical_sha256_without_this_field"] = csha(report)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "terminal": terminal,
        "models": models,
        "norm_survivors": norm_survivors,
        "min_norm": min_norm_seen,
        "models_per_second": report["models_per_second"],
        "seconds": round(elapsed, 3),
        "sha": report["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
