#!/usr/bin/env python3
"""Bounded exact Fincke--Pohst benchmark on the best AFFINE17 43D survivor.

Selected deterministically by AFFINE17 ordering:
  base4=(0,6,2,6), A=5, AB=6, C=0, p100=4.
The zero C-group forces pairings 116..127 to vanish individually, yielding
rank 21 / kernel dimension 43.  AFFINE17 gives exact completed-square radius
89/120, so the entire real ellipsoid also lies below HIGH=3.

This benchmark grants no downstream credit by itself.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
import time
from pathlib import Path

from flint import fmpq, fmpz_mat
from sympy import Matrix, Rational

ROOT = Path(__file__).resolve().parents[3]
ENGINE = ROOT / "stages/stage32-ex5/effectivity-affine/eff_affine01_fp58_engine.py"
ENGINE_BLOB = "e7857e9213ca9107edada1424012a7a1c902a625"
AFF17 = ROOT / "stages/stage32-ex5/effectivity-affine/eff_affine17_empty_ellipsoid_sweep.py"
AFF17_BLOB = "2f173365fe48d91630b1d88d454951469537c42b"

BASE4 = (0, 6, 2, 6)
A_MASS = 5
AB_MASS = 6
C_MASS = 0
P100 = 4
P100_INDEX = 99
NODE_CAP = 250000


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


def fq(x):
    x = Rational(x)
    return fmpq(int(x.p), int(x.q))


def csha(x) -> str:
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def main() -> None:
    req(ENGINE.is_file() and blob(ENGINE) == ENGINE_BLOB, "FP58 engine drift")
    req(AFF17.is_file() and blob(AFF17) == AFF17_BLOB, "AFFINE17 ranking drift")
    eng = load(ENGINE, "stage32ex5_eff_affine18_engine")
    F6, _A6, _I6, _RK58, _R58, _L58, _d58, _c58, _u58, P, gram = eng.build()

    Arow = sum((P.row(i) for i in range(92, 104)), Matrix.zeros(1, 64))
    ABrow = sum((P.row(i) for i in range(92, 116)), Matrix.zeros(1, 64))
    Crow = sum((P.row(i) for i in range(116, 128)), Matrix.zeros(1, 64))
    P100row = P.row(P100_INDEX)
    base_rows = [F6.row(i) for i in range(6)] + [Arow, ABrow, Crow, P100row]
    base10 = [eng.D, eng.E, *BASE4, A_MASS, AB_MASS, C_MASS, P100]

    req(C_MASS == 0, "target zero-pattern drift")
    forced = tuple(range(116, 128))
    req(len(forced) == 12, "forced-zero count")

    full_rows = base_rows + [P.row(i) for i in forced]
    full = Matrix.vstack(*full_rows)
    pivots = list(full.T.rref()[1])
    F = full[pivots, :]
    rank = F.rows
    req(rank == 21 and rank == F.rank(), f"expected rank21, got {rank}")

    all_targets = base10 + [0] * len(forced)
    target = Matrix([all_targets[i] for i in pivots])

    hf, tf = fmpz_mat(
        [[int(F[i, j]) for j in range(64)] for i in range(rank)]
    ).transpose().hnf(transform=True)
    H = Matrix([[int(hf[i, j]) for j in range(hf.ncols())] for i in range(hf.nrows())])
    T = Matrix([[int(tf[i, j]) for j in range(tf.ncols())] for i in range(tf.nrows())])
    req(abs(int(tf.det())) == 1 and H == T * F.T, "HNF replay")

    A = T.T[:, :rank]
    K = T.T[:, rank:]
    I = F * A
    req(K.shape == (64, 43) and F * K == Matrix.zeros(rank, 43), "kernel43")

    ic = I.inv() * target
    req(all(getattr(v, "q", 1) == 1 for v in ic), "selected survivor HNF image")
    bp = A * ic
    req(all(getattr(v, "q", 1) == 1 for v in bp), "integral base point")
    req(F * bp == target, "affine target replay")

    Q = -(K.T * gram * K)
    qf, lf = fmpz_mat(
        [[int(Q[i, j]) for j in range(43)] for i in range(43)]
    ).lll(transform=True, rep="gram", gram="exact")
    U = Matrix([[int(lf[i, j]) for j in range(43)] for i in range(43)])
    R = Matrix([[int(qf[i, j]) for j in range(43)] for i in range(43)])
    RK = K * U.T
    req(abs(int(lf.det())) == 1, "LLL transform")
    req(R == -(RK.T * gram * RK), "LLL replay")

    Ls, Ds = R.LDLdecomposition(hermitian=False)
    req(R == Ls * Ds * Ls.T, "LDL replay")
    diag = [fq(Ds[i, i]) for i in range(43)]
    req(all(x > 0 for x in diag), "positive definite")
    L = [[fq(Ls[i, j]) for j in range(43)] for i in range(43)]

    IR = P * RK
    coeff = []
    for k in range(140):
        src = [fmpq(int(IR[k, j])) for j in range(43)]
        row = []
        for j in range(43):
            z = src[j]
            for i in range(j):
                z -= row[i] * L[j][i]
            row.append(z)
        coeff.append(row)

    dual = []
    for row in coeff:
        s = fmpq(0)
        q = []
        for i in range(43):
            s += row[i] * row[i] / diag[i]
            q.append(s)
        dual.append(q)

    q0 = (bp.T * gram * bp)[0]
    cross = RK.T * gram * bp
    center_s = R.inv() * cross
    center = [fq(x) for x in center_s]
    radius_s = q0 - eng.LOW + (cross.T * R.inv() * cross)[0]
    req(radius_s == Rational(89, 120), f"AFFINE17 radius drift: {radius_s}")
    radius = fq(radius_s)
    max_real_c2 = Rational(eng.LOW) + radius_s
    req(max_real_c2 == Rational(-2311, 120), "max C2 drift")
    req(max_real_c2 <= eng.HIGH, "ellipsoid not contained in bad shell upper edge")

    fixed = [fq(x) for x in P * (bp + RK * center_s)]
    for idx in forced:
        req(all(coeff[idx][j] == 0 for j in range(43)), f"forced row {idx} kernel drift")
        req(fixed[idx] == 0, f"forced row {idx} affine drift")

    pair_upper = [eng.NORMAL_MASS] * 92 + [eng.E] * 48
    coords = [0] * 43
    nodes = prunes = leaves = 0
    lower_prunes = upper_prunes = 0
    witness = None
    capped = False
    tr = hashlib.sha256()

    def ev(*parts):
        tr.update(("|".join(map(str, parts)) + "\n").encode())

    def viable(next_i, rem):
        nonlocal prunes, lower_prunes, upper_prunes
        for k in range(140):
            v = fixed[k]
            upper = fmpq(pair_upper[k])
            if 0 <= v <= upper:
                continue
            dist = -v if v < 0 else v - upper
            impossible = next_i < 0 or dist * dist > rem * dual[k][next_i]
            if impossible:
                prunes += 1
                if v < 0:
                    lower_prunes += 1
                    side = "LOW"
                else:
                    upper_prunes += 1
                    side = "HIGH"
                ev("P2", next_i, k, side, v, upper, rem)
                return False
        return True

    def rec(i, rem):
        nonlocal nodes, leaves, witness, capped
        if witness is not None or capped:
            return
        nodes += 1
        if nodes > NODE_CAP:
            capped = True
            return
        ev("N", i, rem)
        alpha = -center[i]
        for j in range(i + 1, 43):
            alpha += L[j][i] * (coords[j] - center[j])
        exact = -alpha
        base = int(exact.p) // int(exact.q)
        step = 0
        while True:
            vals = [base] if step == 0 else [base - step, base + step]
            any_possible = False
            for val in vals:
                transformed = val + alpha
                cost = diag[i] * transformed * transformed
                if cost > rem:
                    continue
                any_possible = True
                coords[i] = val
                for k in range(140):
                    fixed[k] += coeff[k][i] * transformed
                nr = rem - cost
                if viable(i - 1, nr):
                    if i:
                        rec(i - 1, nr)
                    else:
                        leaves += 1
                        x = bp + RK * Matrix(coords)
                        pair = P * x
                        c2 = int((x.T * gram * x)[0])
                        req(min(pair) >= 0 and c2 >= eng.LOW, "leaf verification")
                        req(max(pair[:92, :]) <= eng.NORMAL_MASS, "normal upper")
                        req(max(pair[92:, :]) <= eng.E, "exceptional upper")
                        req(c2 <= eng.HIGH, "leaf outside bad shell despite real max")
                        witness = {
                            "C2": c2,
                            "picard_coordinates": [int(v) for v in x],
                            "pairings_sha256": csha([int(v) for v in pair]),
                        }
                for k in range(140):
                    fixed[k] -= coeff[k][i] * transformed
                if witness is not None or capped:
                    return
            if step > 0 and not any_possible:
                left = fq(base - step) + alpha
                right = fq(base + step) + alpha
                if diag[i] * left * left > rem and diag[i] * right * right > rem:
                    break
            step += 1

    t0 = time.perf_counter()
    rec(42, radius)
    elapsed = time.perf_counter() - t0

    if witness is not None:
        classification = "BAD_SHELL_SAT_WITNESS_EXACT_FP43"
        complete = True
    elif capped:
        classification = "UNKNOWN_BENCHMARK_NODE_CAP"
        complete = False
    else:
        classification = "BAD_SHELL_UNSAT_EXACT_FP43"
        complete = True

    out = {
        "schema": "STAGE32EX5_EFF_AFFINE18_FP43_BENCHMARK_V1",
        "status": "PASS_BOUNDED_EXACT_FP43_BENCHMARK",
        "selection_provenance": "AFFINE17 best_remaining_fibers[0]",
        "target": {
            "base4": list(BASE4),
            "A": A_MASS,
            "AB": AB_MASS,
            "B": AB_MASS - A_MASS,
            "C": C_MASS,
            "D": eng.E - AB_MASS - C_MASS,
            "p100": P100,
            "zero_pattern_mask": 4,
            "forced_zero_pairing_count": len(forced),
        },
        "fixed_rank": rank,
        "kernel_dimension": 43,
        "hnf_image_index": abs(int(I.det())),
        "bad_shell": [eng.LOW, eng.HIGH],
        "outer_radius_squared": str(radius),
        "exact_real_max_C2": str(max_real_c2),
        "node_cap": NODE_CAP,
        "classification": classification,
        "complete": complete,
        "node_count": nodes,
        "intersection_prune_count": prunes,
        "lower_pairing_prune_count": lower_prunes,
        "upper_pairing_prune_count": upper_prunes,
        "feasible_leaf_count": leaves,
        "elapsed_seconds": elapsed,
        "transcript_sha256": tr.hexdigest(),
        "witness": witness,
        "interpretation": {
            "what_is_proved": (
                "This exact bounded FP recursion resolves the smallest-dimension, "
                "smallest-radius AFFINE17 residual fiber if it completes before the cap."
            ),
            "next_exact_unit": (
                "If complete UNSAT, promote this selection rule into a retained worker "
                "over the remaining 43D fibers in increasing exact radius order. If the "
                "cap is hit, add one more exact pairing projection before scaleout."
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
    print("EFF_AFFINE18_FP43=" + json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
