#!/usr/bin/env python3
"""Exact empty-adjunction-ellipsoid sweep over all AFFINE15 HNF survivors.

For each refined forced-zero affine fiber retained by AFFINE15, complete the
intersection square exactly on its saturated integer kernel.  If

  radius = max(C^2 on the real affine fiber) - LOW

is negative, then the entire affine fiber has C^2 < LOW and therefore contains
no class in the enlarged bad shell [LOW,HIGH].  This is an exact UNSAT
certificate requiring no Fincke--Pohst enumeration.

Fibers with nonnegative radius remain unresolved here; no downstream credit is
promoted by this producer sweep.
"""
from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
import sys
from pathlib import Path

from flint import fmpz_mat
from sympy import Matrix

ROOT = Path(__file__).resolve().parents[3]
ENGINE = ROOT / "stages/stage32-ex5/effectivity-affine/eff_affine01_fp58_engine.py"
ENGINE_BLOB = "e7857e9213ca9107edada1424012a7a1c902a625"
AFF15 = ROOT / "stages/stage32-ex5/effectivity-affine/eff_affine15_forced_zero_collapse.py"
AFF15_BLOB = "40255b3c62753f3df837c006b9481f3a8c02c717"


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


def build_context(mask: int, base_rows: list[Matrix], P: Matrix, gram: Matrix, aff15):
    rows = list(base_rows)
    forced_indices = []
    for bit, (_name, indices) in enumerate(aff15.GROUPS):
        if not (mask & (1 << bit)):
            continue
        for idx in indices:
            rows.append(P.row(idx))
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
    dim = 64 - rank
    req(K.shape == (64, dim) and F * K == Matrix.zeros(rank, dim), "kernel")
    R = -(K.T * gram * K)
    solve_r = aff15.ldl_solver(R)

    return {
        "mask": mask,
        "forced_indices": forced_indices,
        "pivots": pivots,
        "rank": rank,
        "kernel_dimension": dim,
        "image_index": abs(int(I.det())),
        "A": A,
        "K": K,
        "invI": I.inv(),
        "solve_r": solve_r,
    }


def selected_target(ctx, base10: list[int]) -> Matrix:
    all_targets = list(base10) + [0] * len(ctx["forced_indices"])
    return Matrix([all_targets[i] for i in ctx["pivots"]])


def main() -> None:
    req(ENGINE.is_file() and blob(ENGINE) == ENGINE_BLOB, "FP58 engine drift")
    req(AFF15.is_file() and blob(AFF15) == AFF15_BLOB, "AFFINE15 drift")
    eng = load(ENGINE, "stage32ex5_eff_affine17_engine")
    aff15 = load(AFF15, "stage32ex5_eff_affine17_aff15")

    F6, A6, I6, RK58, R58, _L, _d, _c, _u, P, gram = eng.build()
    solve58 = aff15.ldl_solver(R58)

    Arow = sum((P.row(i) for i in range(92, 104)), Matrix.zeros(1, 64))
    ABrow = sum((P.row(i) for i in range(92, 116)), Matrix.zeros(1, 64))
    Crow = sum((P.row(i) for i in range(116, 128)), Matrix.zeros(1, 64))
    P100row = P.row(aff15.P100_INDEX)
    extra_rows = [Arow, ABrow, Crow, P100row]
    base_rows = [F6.row(i) for i in range(6)] + extra_rows
    F10 = Matrix.vstack(*base_rows)
    req(F10.rank() == 10, "fixed10 rank drift")

    hf10, tf10 = fmpz_mat(
        [[int(F10[i, j]) for j in range(64)] for i in range(10)]
    ).transpose().hnf(transform=True)
    T10 = Matrix([[int(tf10[i, j]) for j in range(tf10.ncols())] for i in range(tf10.nrows())])
    A10 = T10.T[:, :10]
    I10 = F10 * A10
    invI10 = I10.inv()
    invI6 = I6.inv()

    candidates = []
    for base4 in aff15.SAMPLE_BASE4:
        target6 = Matrix([eng.D, eng.E, *base4])
        ic6 = invI6 * target6
        req(all(getattr(v, "q", 1) == 1 for v in ic6), "sample base4 image")
        bp6 = A6 * ic6
        domains = [
            aff15.allowed_projection(r, bp6, RK58, R58, solve58, gram, eng.LOW, eng.E)
            for r in extra_rows
        ]
        for a, ab, c, p100 in itertools.product(*domains):
            if not (0 <= a <= ab <= eng.E and 0 <= c <= eng.E - ab and 0 <= p100 <= a):
                continue
            base10 = [eng.D, eng.E, *base4, a, ab, c, p100]
            icoord = invI10 * Matrix(base10)
            if not all(getattr(v, "q", 1) == 1 for v in icoord):
                continue
            candidates.append({
                "base4": base4,
                "A": a,
                "AB": ab,
                "B": ab - a,
                "C": c,
                "D": eng.E - ab - c,
                "p100": p100,
                "base10": base10,
                "mask": aff15.pattern_mask(a, ab, c, p100, eng.E),
            })

    req(len(candidates) == 774, "AFFINE14 compatible population drift")
    masks = sorted({row["mask"] for row in candidates})
    contexts = {m: build_context(m, base_rows, P, gram, aff15) for m in masks}

    hnf_unsat = 0
    hnf_survivors = 0
    empty_unsat = 0
    radius_survivors = 0
    empty_by_dim = {}
    survivor_by_dim = {}
    per_key = []

    for base4 in aff15.SAMPLE_BASE4:
        key_rows = [r for r in candidates if r["base4"] == base4]
        key_hnf = key_empty = key_survive = 0
        examples = []
        for row in key_rows:
            ctx = contexts[row["mask"]]
            t = selected_target(ctx, row["base10"])
            icoord = ctx["invI"] * t
            if not all(getattr(v, "q", 1) == 1 for v in icoord):
                hnf_unsat += 1
                continue

            hnf_survivors += 1
            key_hnf += 1
            bp = ctx["A"] * icoord
            req(all(getattr(v, "q", 1) == 1 for v in bp), "integral base point")
            req((Matrix.vstack(*(
                base_rows + [P.row(i) for i in ctx["forced_indices"]]
            ))[ctx["pivots"], :] * bp) == t, "affine target replay")

            K = ctx["K"]
            q0 = (bp.T * gram * bp)[0]
            cross = K.T * gram * bp
            center = ctx["solve_r"](cross)
            radius = q0 - eng.LOW + (cross.T * center)[0]
            dim = ctx["kernel_dimension"]

            if radius < 0:
                empty_unsat += 1
                key_empty += 1
                empty_by_dim[dim] = empty_by_dim.get(dim, 0) + 1
            else:
                radius_survivors += 1
                key_survive += 1
                survivor_by_dim[dim] = survivor_by_dim.get(dim, 0) + 1
                if len(examples) < 12:
                    examples.append({
                        "A": row["A"], "AB": row["AB"], "B": row["B"],
                        "C": row["C"], "D": row["D"], "p100": row["p100"],
                        "zero_pattern_mask": row["mask"],
                        "kernel_dimension": dim,
                        "exact_radius_squared": str(radius),
                        "exact_real_max_C2": str(eng.LOW + radius),
                    })

        per_key.append({
            "base4": list(base4),
            "affine15_hnf_survivors": key_hnf,
            "empty_adjunction_ellipsoid_unsat": key_empty,
            "nonnegative_radius_survivors": key_survive,
            "survivor_examples": examples,
        })

    req(hnf_unsat == 478, "AFFINE15 HNF UNSAT drift")
    req(hnf_survivors == 296, "AFFINE15 survivor drift")
    req(empty_unsat + radius_survivors == 296, "radius partition")

    out = {
        "schema": "STAGE32EX5_EFF_AFFINE17_EMPTY_ELLIPSOID_SWEEP_V1",
        "status": "PASS_EXACT_EMPTY_ADJUNCTION_ELLIPSOID_SWEEP",
        "bad_shell": [eng.LOW, eng.HIGH],
        "affine14_hnf_compatible_population": 774,
        "affine15_hnf_unsat": hnf_unsat,
        "affine15_hnf_survivors": hnf_survivors,
        "empty_adjunction_ellipsoid_unsat": empty_unsat,
        "nonnegative_radius_survivors": radius_survivors,
        "empty_unsat_kernel_dimension_histogram": {
            str(k): empty_by_dim[k] for k in sorted(empty_by_dim)
        },
        "survivor_kernel_dimension_histogram": {
            str(k): survivor_by_dim[k] for k in sorted(survivor_by_dim)
        },
        "rows": per_key,
        "interpretation": {
            "what_is_proved": (
                "For every AFFINE15 HNF survivor with negative exact completed-square "
                "radius, the full refined real affine fiber has C^2 below the adjunction "
                "lower edge, hence the enlarged bad shell is exactly empty."
            ),
            "next_exact_unit": (
                "Run bounded exact Fincke--Pohst only on the nonnegative-radius survivors, "
                "prioritizing the smallest kernel dimension and smallest exact radius."
            ),
            "what_is_not_proved": (
                "Nonnegative-radius fibers remain unresolved. This producer sweep grants "
                "no effectivity, MAIN, receiver, theorem, endpoint, or merge credit."
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
    print("EFF_AFFINE17_EMPTY_ELLIPSOID=" + json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
