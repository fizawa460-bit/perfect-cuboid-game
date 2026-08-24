#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import pathlib
import subprocess
import time
from collections import Counter

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
        old_t, t = t, old_t - q * t
    if old_r < 0:
        old_r, old_s, old_t = -old_r, -old_s, -old_t
    return old_r, old_s, old_t


def matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    bt = list(zip(*b))
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def transpose(a: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*a)]


def row_times_matrix(row: list[int], matrix: list[list[int]]) -> list[int]:
    return [sum(row[i] * matrix[i][j] for i in range(len(row))) for j in range(len(matrix[0]))]


def kernel_basis_primitive_row(row: list[int]) -> tuple[list[list[int]], int]:
    """Return a full Z-basis of ker(row) as columns via unimodular Bezout steps."""
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
        # Right multiply columns (0,j) by [[s,-b/d],[t,a/d]], determinant 1.
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


def gram_on_kernel(gram: list[list[int]], basis: list[list[int]]) -> list[list[int]]:
    gb = matmul(gram, basis)
    btgb = matmul(transpose(basis), gb)
    q = [[-value for value in row] for row in btgb]
    assert len(q) == 63 and all(len(row) == 63 for row in q)
    assert q == transpose(q)
    return q


def gp_matrix(matrix: list[list[int]]) -> str:
    return "[" + ";".join(",".join(str(v) for v in row) for row in matrix) + "]"


def parse_vector(text: str) -> list[int]:
    text = text.strip()
    assert text.startswith("[") and text.endswith("]")
    body = text[1:-1].strip()
    return [] if not body else [int(x.strip()) for x in body.split(",")]


def run_pari(q: list[list[int]], bound: int, stored_pairs: int, timeout_seconds: float) -> dict:
    code = f"""
Q={gp_matrix(q)};
T=qflllgram(Q,1);
R=T~*Q*T;
r=qfminim(R,{bound},{stored_pairs},0);
V=r[3];
c=matsize(V)[2];
print("META|",r[1],"|",r[2],"|",c);
for(i=1,c,w=T*V[,i];print("V|",i,"|",Vec(w)));
quit;
"""
    started = time.perf_counter()
    try:
        proc = subprocess.run(
            ["gp", "-q"], input=code, text=True, capture_output=True,
            timeout=timeout_seconds, check=False,
        )
    except subprocess.TimeoutExpired as exc:
        return {
            "status": "TIMEOUT",
            "elapsed_seconds": round(time.perf_counter() - started, 6),
            "stdout_tail": (exc.stdout or "")[-1000:] if isinstance(exc.stdout, str) else "",
        }
    elapsed = time.perf_counter() - started
    if proc.returncode != 0:
        return {
            "status": "ERROR",
            "elapsed_seconds": round(elapsed, 6),
            "returncode": proc.returncode,
            "stderr_tail": proc.stderr[-2000:],
            "stdout_tail": proc.stdout[-2000:],
        }
    meta = None
    vectors: list[list[int]] = []
    for raw in proc.stdout.splitlines():
        line = raw.strip()
        if line.startswith("META|"):
            _, n, maxnorm, cols = line.split("|", 3)
            meta = (int(n), int(maxnorm), int(cols))
        elif line.startswith("V|"):
            _, _, payload = line.split("|", 2)
            vectors.append(parse_vector(payload))
    if meta is None:
        return {
            "status": "PARSE_ERROR",
            "elapsed_seconds": round(elapsed, 6),
            "stdout_tail": proc.stdout[-2000:],
            "stderr_tail": proc.stderr[-2000:],
        }
    n, maxnorm, cols = meta
    assert cols == len(vectors)
    return {
        "status": "COMPLETE_ENUMERATION_COUNT",
        "elapsed_seconds": round(elapsed, 6),
        "total_nonzero_vectors_including_sign": n,
        "maximum_norm_enumerated": maxnorm,
        "stored_representative_pairs": cols,
        "vectors": vectors,
    }


def exact_filter(core: dict, basis: list[list[int]], z: list[int]) -> list[dict]:
    gram = [[int(v) for v in row] for row in core["basis_gram"]]
    h = [int(v) for v in core["hyperplane"]]
    known = [[int(v) for v in row] for row in core["raw_cross_pairings_with_basis"]]
    y = [sum(basis[i][j] * z[j] for j in range(63)) for i in range(64)]
    y2 = sum(y[i] * gram[i][j] * y[j] for i in range(64) for j in range(64))
    norm = -y2
    assert 0 < norm <= NORM_BOUND
    out = []
    for sign in (1, -1):
        c = [h[i] + sign * y[i] for i in range(64)]
        pairings = [sum(row[i] * c[i] for i in range(64)) for row in known]
        if not all(0 <= pairings[i] <= NORMAL_CAP for i in range(92)):
            continue
        if not all(0 <= pairings[i] <= EXCEPTIONAL_CAP for i in range(92, 140)):
            continue
        c2 = sum(c[i] * gram[i][j] * c[j] for i in range(64) for j in range(64))
        assert c2 == DEGREE - norm
        if c2 < -DEGREE - 2 + 2 * GENUS:
            continue
        out.append({
            "norm": norm,
            "self_intersection": c2,
            "exceptional_mass": sum(pairings[92:]),
            "curve_group_mass": sum(pairings[:46]),
            "basis_coordinates_sha256": hashlib.sha256(
                json.dumps(c, separators=(",", ":")).encode()
            ).hexdigest(),
        })
    return out


def zero_filter(core: dict) -> bool:
    h = [int(v) for v in core["hyperplane"]]
    known = [[int(v) for v in row] for row in core["raw_cross_pairings_with_basis"]]
    p = [sum(row[i] * h[i] for i in range(64)) for row in known]
    return all(0 <= p[i] <= NORMAL_CAP for i in range(92)) and all(
        0 <= p[i] <= EXCEPTIONAL_CAP for i in range(92, 140)
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--core", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    ap.add_argument("--bounds", default="2,4,6,8,10,12,16,20,26,34")
    ap.add_argument("--stored-pairs", type=int, default=5000)
    ap.add_argument("--per-bound-seconds", type=float, default=120.0)
    ap.add_argument("--stop-count", type=int, default=2_000_000)
    args = ap.parse_args()

    core = json.loads(args.core.read_text())
    unsigned = dict(core)
    claimed = unsigned.pop("canonical_sha256_without_this_field")
    assert claimed == EXPECTED_CORE_SHA == csha(unsigned)
    assert core["source"]["git_blob_sha1"] == EXPECTED_SOURCE_BLOB
    gram = [[int(v) for v in row] for row in core["basis_gram"]]
    h = [int(v) for v in core["hyperplane"]]
    hrow = [sum(h[i] * gram[i][j] for i in range(64)) for j in range(64)]
    assert sum(hrow[i] * h[i] for i in range(64)) == 16

    basis, hrow_content = kernel_basis_primitive_row(hrow)
    q = gram_on_kernel(gram, basis)
    # Exact sanity checks on the kernel model.
    assert hrow_content == 2
    assert all(value == 0 for value in row_times_matrix(hrow, basis))
    assert all(q[i][i] > 0 for i in range(63))

    bounds = [int(x) for x in args.bounds.split(",") if x.strip()]
    assert bounds == sorted(set(bounds)) and bounds[-1] <= NORM_BOUND
    tiers = []
    survivor_digest = hashlib.sha256()
    stopped_reason = "BOUNDS_EXHAUSTED"

    for bound in bounds:
        result = run_pari(q, bound, args.stored_pairs, args.per_bound_seconds)
        tier = {k: v for k, v in result.items() if k != "vectors"}
        tier["bound"] = bound
        if result["status"] != "COMPLETE_ENUMERATION_COUNT":
            tiers.append(tier)
            stopped_reason = result["status"]
            break

        total = int(result["total_nonzero_vectors_including_sign"])
        vectors = result["vectors"]
        stored_complete = total <= 2 * len(vectors)
        survivors = []
        parent_hist: Counter[tuple[int, int]] = Counter()
        norm_hist: Counter[int] = Counter()
        for z in vectors:
            assert len(z) == 63
            for row in exact_filter(core, basis, z):
                survivors.append(row)
                norm_hist[int(row["norm"])] += 1
                parent_hist[(int(row["exceptional_mass"]), int(row["curve_group_mass"]))] += 1
                survivor_digest.update(row["basis_coordinates_sha256"].encode())
        tier.update({
            "stored_pairs_cover_all_pairs": stored_complete,
            "postfilter_survivors_in_stored_pairs_both_signs": len(survivors),
            "postfilter_count_is_complete_for_nonzero_ball": stored_complete,
            "complete_postfilter_survivor_count_nonzero": len(survivors) if stored_complete else None,
            "postfilter_norm_histogram": {str(k): v for k, v in sorted(norm_hist.items())},
            "postfilter_parent_top10": [
                {"exceptional_mass": e, "curve_group_mass": a, "count": n}
                for (e, a), n in parent_hist.most_common(10)
            ],
        })
        tiers.append(tier)
        if total > args.stop_count:
            stopped_reason = "ENUMERATION_COUNT_STOP"
            break

    report = {
        "schema": "STAGE32_SCOUT_D16_HPERP_PARI_FINCKE_POHST_V1",
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
            "bounds": bounds,
            "stored_pairs_per_tier": args.stored_pairs,
            "per_bound_seconds": args.per_bound_seconds,
            "stop_count": args.stop_count,
        },
        "architecture": {
            "direction": "H_PERP_SHORT_VECTORS_FIRST_THEN_140_INTERSECTION_FILTER",
            "enumerator": "PARI_GP_QFMINIM_FINCKE_POHST_WITH_EXACT_INTEGER_GRAM",
            "kernel_basis_construction": "UNIMODULAR_BEZOUT_EXACT_Z_KERNEL",
            "hrow_content": hrow_content,
            "exceptional_assignment_materialization": False,
            "signature_cell_materialization": False,
            "materialized_branch_count_constructed": 0,
        },
        "zero_vector_H_candidate_passes_140_caps": zero_filter(core),
        "tiers": tiers,
        "stopped_reason": stopped_reason,
        "survivor_stream_digest": survivor_digest.hexdigest(),
        "interpretation": {
            "purpose": "TEST_WHETHER_D16_CAN_BYPASS_D8_STYLE_COMBINATORIAL_MATERIALIZATION_USING_SHORT_VECTOR_ENUMERATION",
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
        "stopped_reason": stopped_reason,
        "tiers": [{k: t.get(k) for k in (
            "bound", "status", "total_nonzero_vectors_including_sign",
            "stored_representative_pairs", "postfilter_survivors_in_stored_pairs_both_signs",
            "postfilter_count_is_complete_for_nonzero_ball", "elapsed_seconds"
        )} for t in tiers],
        "sha": report["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
