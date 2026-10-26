#!/usr/bin/env python3
"""Exact forced-zero HNF sweep over all AFFINE14 hierarchy fibers.

For every projected/HNF-compatible (base4,A,AB,C,p100) hierarchy fiber, use
all140 nonnegativity to turn every zero exceptional group mass into individual
pairing=0 equalities.  The A quarter also collapses when A=p100, because the
other 11 nonnegative entries then have total mass zero.

Each distinct zero pattern gets one exact saturated fixed-map/HNF context.
A target outside that refined HNF image is an exact impossibility certificate
for the whole hierarchy fiber, before Fincke--Pohst enumeration.
"""
from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
import math
import sys
from pathlib import Path

from flint import fmpz_mat
from sympy import Matrix

ROOT = Path(__file__).resolve().parents[3]
ENGINE = ROOT / "stages/stage32-ex5/effectivity-affine/eff_affine01_fp58_engine.py"
ENGINE_BLOB = "e7857e9213ca9107edada1424012a7a1c902a625"

SAMPLE_BASE4 = (
    (0, 1, 1, 1),
    (0, 4, 4, 8),
    (0, 6, 2, 6),
    (1, 2, 2, 2),
    (1, 3, 3, 3),
)
P100_INDEX = 99
GROUPS = (
    ("A_rest_zero", tuple(i for i in range(92, 104) if i != P100_INDEX)),
    ("B_zero", tuple(range(104, 116))),
    ("C_zero", tuple(range(116, 128))),
    ("D_zero", tuple(range(128, 140))),
)


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, "module spec")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def pd(A: Matrix) -> bool:
    if A != A.T:
        return False
    try:
        L, D = A.LDLdecomposition(hermitian=False)
    except Exception:
        return False
    return A == L * D * L.T and all(D[i, i] > 0 for i in range(D.rows))


def ldl_solver(A: Matrix):
    L, D = A.LDLdecomposition(hermitian=False)
    req(A == L * D * L.T and all(D[i, i] > 0 for i in range(D.rows)), "LDL")

    def solve(b: Matrix) -> Matrix:
        cols = []
        for col in range(b.cols):
            y = [0] * A.rows
            for i in range(A.rows):
                v = b[i, col]
                for j in range(i):
                    v -= L[i, j] * y[j]
                y[i] = v / L[i, i]
            z = [y[i] / D[i, i] for i in range(A.rows)]
            x = [0] * A.rows
            for i in range(A.rows - 1, -1, -1):
                v = z[i]
                for j in range(i + 1, A.rows):
                    v -= L[j, i] * x[j]
                x[i] = v / L[i, i]
            cols.append(Matrix(x))
        out = Matrix.hstack(*cols)
        req(A * out == b, "LDL solve replay")
        return out

    return solve


def allowed_projection(row: Matrix, bp: Matrix, RK: Matrix, R: Matrix, solve_r,
                       gram: Matrix, low: int, upper: int) -> list[int]:
    coeff = row * RK
    g = 0
    for v in coeff:
        g = math.gcd(g, abs(int(v)))
    req(g > 0, "projection gcd")
    q0 = (bp.T * gram * bp)[0]
    cross = RK.T * gram * bp
    center = solve_r(cross)
    radius = q0 - low + (cross.T * center)[0]
    req(radius >= 0, "outer radius")
    c = (row * (bp + RK * center))[0]
    v = coeff.T
    dual = (v.T * solve_r(v))[0]
    req(dual > 0, "projection dual")
    residue = int((row * bp)[0]) % g
    return [
        k for k in range(upper + 1)
        if k % g == residue and (k - c) * (k - c) <= radius * dual
    ]


def pattern_mask(a: int, ab: int, c: int, p100: int, e: int) -> int:
    b = ab - a
    d = e - ab - c
    flags = (a - p100 == 0, b == 0, c == 0, d == 0)
    return sum((1 << i) for i, flag in enumerate(flags) if flag)


def build_pattern_context(mask: int, base_rows: list[Matrix], P: Matrix, gram: Matrix):
    rows = list(base_rows)
    row_kinds = list(range(10))
    forced_indices = []
    for bit, (_name, indices) in enumerate(GROUPS):
        if not (mask & (1 << bit)):
            continue
        for idx in indices:
            rows.append(P.row(idx))
            row_kinds.append(10 + len(forced_indices))
            forced_indices.append(idx)

    full = Matrix.vstack(*rows)
    pivots = list(full.T.rref()[1])
    F = full[pivots, :]
    rank = F.rows
    req(rank == F.rank(), "independent fixed-map extraction")

    hf, tf = fmpz_mat(
        [[int(F[i, j]) for j in range(64)] for i in range(rank)]
    ).transpose().hnf(transform=True)
    H = Matrix([[int(hf[i, j]) for j in range(hf.ncols())] for i in range(hf.nrows())])
    T = Matrix([[int(tf[i, j]) for j in range(tf.ncols())] for i in range(tf.nrows())])
    req(abs(int(tf.det())) == 1 and H == T * F.T, "pattern HNF replay")

    A = T.T[:, :rank]
    K = T.T[:, rank:]
    I = F * A
    req(K.shape == (64, 64 - rank), "pattern kernel shape")
    req(F * K == Matrix.zeros(rank, 64 - rank), "pattern kernel equality")
    R = -(K.T * gram * K)
    req(pd(R), "pattern restricted negative form")

    return {
        "mask": mask,
        "forced_indices": forced_indices,
        "pivots": pivots,
        "rank": rank,
        "kernel_dimension": 64 - rank,
        "image_index": abs(int(I.det())),
        "invI": I.inv(),
    }


def selected_target(ctx, base10: list[int]) -> Matrix:
    all_targets = list(base10) + [0] * len(ctx["forced_indices"])
    return Matrix([all_targets[i] for i in ctx["pivots"]])


def main() -> None:
    req(ENGINE.is_file() and blob(ENGINE) == ENGINE_BLOB, "FP58 engine drift")
    eng = load(ENGINE, "stage32ex5_eff_affine15_engine")
    F6, A6, I6, RK58, R58, _L, _d, _c, _u, P, gram = eng.build()
    req(pd(R58), "58D outer kernel")
    solve58 = ldl_solver(R58)

    Arow = sum((P.row(i) for i in range(92, 104)), Matrix.zeros(1, 64))
    ABrow = sum((P.row(i) for i in range(92, 116)), Matrix.zeros(1, 64))
    Crow = sum((P.row(i) for i in range(116, 128)), Matrix.zeros(1, 64))
    P100row = P.row(P100_INDEX)
    extra_rows = [Arow, ABrow, Crow, P100row]
    base_rows = [F6.row(i) for i in range(6)] + extra_rows
    F10 = Matrix.vstack(*base_rows)
    req(F10.rank() == 10, "AFFINE14 fixed10 rank drift")

    hf10, tf10 = fmpz_mat(
        [[int(F10[i, j]) for j in range(64)] for i in range(10)]
    ).transpose().hnf(transform=True)
    T10 = Matrix([[int(tf10[i, j]) for j in range(tf10.ncols())] for i in range(tf10.nrows())])
    A10 = T10.T[:, :10]
    I10 = F10 * A10
    invI10 = I10.inv()
    invI6 = I6.inv()

    # First enumerate exactly the same hierarchy target population as AFFINE14.
    candidates = []
    per_key_projected = {}
    for base4 in SAMPLE_BASE4:
        target6 = Matrix([eng.D, eng.E, *base4])
        ic6 = invI6 * target6
        req(all(getattr(v, "q", 1) == 1 for v in ic6), "sample base4 image")
        bp6 = A6 * ic6
        domains = [
            allowed_projection(r, bp6, RK58, R58, solve58, gram, eng.LOW, eng.E)
            for r in extra_rows
        ]
        projected = 0
        compatible = 0
        for a, ab, c, p100 in itertools.product(*domains):
            if not (0 <= a <= ab <= eng.E and 0 <= c <= eng.E - ab and 0 <= p100 <= a):
                continue
            projected += 1
            base10 = [eng.D, eng.E, *base4, a, ab, c, p100]
            icoord = invI10 * Matrix(base10)
            if not all(getattr(v, "q", 1) == 1 for v in icoord):
                continue
            compatible += 1
            candidates.append({
                "base4": base4,
                "A": a,
                "AB": ab,
                "C": c,
                "p100": p100,
                "B": ab - a,
                "D": eng.E - ab - c,
                "base10": base10,
                "mask": pattern_mask(a, ab, c, p100, eng.E),
            })
        per_key_projected[base4] = (projected, compatible, domains)

    req(len(candidates) == 774, "AFFINE14 compatible population drift")

    observed_masks = sorted({row["mask"] for row in candidates})
    contexts = {mask: build_pattern_context(mask, base_rows, P, gram) for mask in observed_masks}

    per_key = []
    total_unsat = total_survivors = 0
    dimension_hist = {}
    for base4 in SAMPLE_BASE4:
        rows = [row for row in candidates if row["base4"] == base4]
        survivors = []
        unsat = 0
        for row in rows:
            ctx = contexts[row["mask"]]
            t = selected_target(ctx, row["base10"])
            image = ctx["invI"] * t
            integral = all(getattr(v, "q", 1) == 1 for v in image)
            if not integral:
                unsat += 1
                continue
            dim = ctx["kernel_dimension"]
            dimension_hist[dim] = dimension_hist.get(dim, 0) + 1
            survivors.append({
                "A": row["A"],
                "AB": row["AB"],
                "B": row["B"],
                "C": row["C"],
                "D": row["D"],
                "p100": row["p100"],
                "zero_pattern_mask": row["mask"],
                "kernel_dimension": dim,
                "forced_zero_pairing_count": len(ctx["forced_indices"]),
                "refined_hnf_image_index": ctx["image_index"],
            })

        survivors.sort(key=lambda x: (
            x["kernel_dimension"],
            -x["forced_zero_pairing_count"],
            -x["p100"],
            x["A"], x["AB"], x["C"],
        ))
        projected, compatible, domains = per_key_projected[base4]
        per_key.append({
            "base4": list(base4),
            "projection_domains": {
                "A": domains[0], "AB": domains[1], "C": domains[2], "p100": domains[3],
            },
            "projected_tuple_count": projected,
            "affine14_hnf_compatible_count": compatible,
            "forced_zero_hnf_unsat_count": unsat,
            "forced_zero_hnf_survivor_count": len(survivors),
            "fully_closed_by_forced_zero_hnf": len(survivors) == 0,
            "smallest_surviving_kernel_dimension": (
                survivors[0]["kernel_dimension"] if survivors else None
            ),
            "best_survivor_examples": survivors[:20],
        })
        total_unsat += unsat
        total_survivors += len(survivors)

    pattern_report = []
    for mask in observed_masks:
        ctx = contexts[mask]
        pattern_report.append({
            "mask": mask,
            "forced_groups": [
                name for bit, (name, _indices) in enumerate(GROUPS) if mask & (1 << bit)
            ],
            "forced_zero_pairing_count": len(ctx["forced_indices"]),
            "independent_fixed_rank": ctx["rank"],
            "kernel_dimension": ctx["kernel_dimension"],
            "hnf_image_index": ctx["image_index"],
        })

    out = {
        "schema": "STAGE32EX5_EFF_AFFINE15_FORCED_ZERO_HNF_SWEEP_V2",
        "status": "PASS_EXACT_FORCED_ZERO_HNF_SWEEP",
        "affine14_population_replayed": 774,
        "observed_zero_patterns": pattern_report,
        "rows": per_key,
        "summary": {
            "affine14_hnf_compatible_fibers": len(candidates),
            "forced_zero_hnf_unsat_fibers": total_unsat,
            "forced_zero_hnf_survivors": total_survivors,
            "fully_closed_base4_keys": sum(r["fully_closed_by_forced_zero_hnf"] for r in per_key),
            "survivor_kernel_dimension_histogram": {
                str(k): dimension_hist[k] for k in sorted(dimension_hist)
            },
        },
        "interpretation": {
            "what_is_proved": (
                "Whenever a hierarchy group has zero nonnegative mass, every pairing in "
                "that group is exactly zero. Refined HNF-image failure therefore proves "
                "the entire hierarchy fiber impossible without any lattice enumeration."
            ),
            "next_exact_unit": (
                "Select the smallest-dimensional surviving refined fiber and run one "
                "bounded historical-style exact Fincke-Pohst benchmark there."
            ),
            "what_is_not_proved": (
                "Refined-HNF survivors remain unresolved; no effectivity or downstream "
                "credit is promoted."
            ),
        },
        "credit": {
            "effectivity": False,
            "main": False,
            "receiver": False,
            "theorem": False,
            "endpoint": False,
            "merge": False,
        },
    }
    print("EFF_AFFINE15_ZERO_COLLAPSE=" + json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
