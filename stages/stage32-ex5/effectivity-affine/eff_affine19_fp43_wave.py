#!/usr/bin/env python3
"""Exact FP43 wave over the smallest-radius AFFINE17 residual fibers.

Reconstruct the full AFFINE17 population, retain exactly the nonnegative-radius
43D survivors, sort them by the same deterministic key, and run a bounded exact
Fincke--Pohst search on the first WAVE_SIZE fibers.

LLL/LDL data are cached per forced-zero mask.  A per-fiber and aggregate node
cap make this a bounded research wave: completed SAT/UNSAT classifications are
exact; capped fibers remain UNKNOWN with zero downstream credit.
"""
from __future__ import annotations

import hashlib
import importlib.util
import itertools
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

WAVE_SIZE = 16
PER_FIBER_NODE_CAP = 50000
TOTAL_NODE_CAP = 250000


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


def build_lll_context(ctx, P: Matrix, gram: Matrix):
    K = ctx["K"]
    dim = ctx["kernel_dimension"]
    req(dim == 43, "AFFINE19 requires 43D context")
    Q = -(K.T * gram * K)
    qf, lf = fmpz_mat(
        [[int(Q[i, j]) for j in range(dim)] for i in range(dim)]
    ).lll(transform=True, rep="gram", gram="exact")
    U = Matrix([[int(lf[i, j]) for j in range(dim)] for i in range(dim)])
    R = Matrix([[int(qf[i, j]) for j in range(dim)] for i in range(dim)])
    RK = K * U.T
    req(abs(int(lf.det())) == 1, "LLL transform")
    req(R == -(RK.T * gram * RK), "LLL replay")

    Ls, Ds = R.LDLdecomposition(hermitian=False)
    req(R == Ls * Ds * Ls.T, "LDL replay")
    diag = [fq(Ds[i, i]) for i in range(dim)]
    req(all(x > 0 for x in diag), "positive definite")
    L = [[fq(Ls[i, j]) for j in range(dim)] for i in range(dim)]

    IR = P * RK
    coeff = []
    for k in range(140):
        src = [fmpq(int(IR[k, j])) for j in range(dim)]
        row = []
        for j in range(dim):
            z = src[j]
            for i in range(j):
                z -= row[i] * L[j][i]
            row.append(z)
        coeff.append(row)

    dual = []
    for row in coeff:
        s = fmpq(0)
        q = []
        for i in range(dim):
            s += row[i] * row[i] / diag[i]
            q.append(s)
        dual.append(q)

    return {
        "RK": RK,
        "R": R,
        "L": L,
        "diag": diag,
        "coeff": coeff,
        "dual": dual,
    }


def solve_one(row, ctx, lc, P: Matrix, gram: Matrix, eng, total_nodes_used: int):
    t = ctx["selected_target"](row["base10"])
    icoord = ctx["invI"] * t
    req(all(getattr(v, "q", 1) == 1 for v in icoord), "wave HNF survivor drift")
    bp = ctx["A"] * icoord
    req(all(getattr(v, "q", 1) == 1 for v in bp), "integral base point")

    RK = lc["RK"]
    R = lc["R"]
    L = lc["L"]
    diag = lc["diag"]
    coeff = lc["coeff"]
    dual = lc["dual"]
    dim = 43

    q0 = (bp.T * gram * bp)[0]
    cross = RK.T * gram * bp
    center_s = R.inv() * cross
    center = [fq(x) for x in center_s]
    radius_s = q0 - eng.LOW + (cross.T * R.inv() * cross)[0]
    req(radius_s >= 0, "selected residual radius")
    radius = fq(radius_s)
    max_real_c2 = Rational(eng.LOW) + radius_s

    fixed = [fq(x) for x in P * (bp + RK * center_s)]
    forced = ctx["forced_indices"]
    for idx in forced:
        req(all(coeff[idx][j] == 0 for j in range(dim)), f"forced row {idx} kernel drift")
        req(fixed[idx] == 0, f"forced row {idx} affine drift")

    pair_upper = [eng.NORMAL_MASS] * 92 + [eng.E] * 48
    coords = [0] * dim
    nodes = prunes = leaves = 0
    lower_prunes = upper_prunes = 0
    witness = None
    capped = False
    tr = hashlib.sha256()
    remaining_total = max(0, TOTAL_NODE_CAP - total_nodes_used)
    local_cap = min(PER_FIBER_NODE_CAP, remaining_total)

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
        if nodes >= local_cap:
            capped = True
            return
        nodes += 1
        ev("N", i, rem)
        alpha = -center[i]
        for j in range(i + 1, dim):
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
                        if c2 <= eng.HIGH:
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
    if local_cap == 0:
        capped = True
    else:
        rec(dim - 1, radius)
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

    return {
        "base4": list(row["base4"]),
        "A": row["A"],
        "AB": row["AB"],
        "B": row["B"],
        "C": row["C"],
        "D": row["D"],
        "p100": row["p100"],
        "zero_pattern_mask": row["mask"],
        "kernel_dimension": 43,
        "exact_radius_squared": str(radius),
        "exact_real_max_C2": str(max_real_c2),
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
    }


def main() -> None:
    req(ENGINE.is_file() and blob(ENGINE) == ENGINE_BLOB, "FP58 engine drift")
    req(AFF17.is_file() and blob(AFF17) == AFF17_BLOB, "AFFINE17 drift")
    eng = load(ENGINE, "stage32ex5_eff_affine19_engine")
    aff17 = load(AFF17, "stage32ex5_eff_affine19_aff17")

    F6, A6, I6, RK58, R58, _L, _d, _c, _u, P, gram = eng.build()
    solve58 = aff17.load(
        ROOT / "stages/stage32-ex5/effectivity-affine/eff_affine15_forced_zero_collapse.py",
        "stage32ex5_eff_affine19_aff15",
    ).ldl_solver(R58)
    aff15 = sys.modules["stage32ex5_eff_affine19_aff15"]

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
    raw_contexts = {m: aff17.build_context(m, base_rows, P, gram, aff15) for m in masks}
    contexts = {}
    residual = []
    for row in candidates:
        raw = raw_contexts[row["mask"]]
        t = aff17.selected_target(raw, row["base10"])
        icoord = raw["invI"] * t
        if not all(getattr(v, "q", 1) == 1 for v in icoord):
            continue
        bp = raw["A"] * icoord
        q0 = (bp.T * gram * bp)[0]
        cross = raw["K"].T * gram * bp
        center = raw["solve_r"](cross)
        radius = q0 - eng.LOW + (cross.T * center)[0]
        if radius < 0 or raw["kernel_dimension"] != 43:
            continue
        residual.append((
            raw["kernel_dimension"], radius, tuple(row["base4"]),
            row["A"], row["AB"], row["C"], row["p100"], row["mask"], row
        ))
    residual.sort(key=lambda x: x[:-1])
    req(len(residual) == 95, f"AFFINE17 43D residual drift: {len(residual)}")

    wave = [x[-1] for x in residual[:WAVE_SIZE]]
    used_masks = sorted({row["mask"] for row in wave})
    for mask in used_masks:
        raw = raw_contexts[mask]
        ctx = dict(raw)
        ctx["selected_target"] = lambda base10, _ctx=raw: aff17.selected_target(_ctx, base10)
        contexts[mask] = ctx
    lll = {mask: build_lll_context(contexts[mask], P, gram) for mask in used_masks}

    rows = []
    total_nodes = 0
    for row in wave:
        out = solve_one(row, contexts[row["mask"]], lll[row["mask"]], P, gram, eng, total_nodes)
        rows.append(out)
        total_nodes += out["node_count"]
        if total_nodes >= TOTAL_NODE_CAP:
            break

    counts = {}
    for row in rows:
        counts[row["classification"]] = counts.get(row["classification"], 0) + 1

    out = {
        "schema": "STAGE32EX5_EFF_AFFINE19_FP43_WAVE_V1",
        "status": "PASS_BOUNDED_EXACT_FP43_WAVE",
        "selection": {
            "population": "AFFINE17 nonnegative-radius kernel_dimension=43 survivors",
            "population_count": 95,
            "ordering": "kernel_dimension,radius,base4,A,AB,C,p100,mask",
            "requested_wave_size": WAVE_SIZE,
            "executed_wave_size": len(rows),
        },
        "caps": {
            "per_fiber_node_cap": PER_FIBER_NODE_CAP,
            "total_node_cap": TOTAL_NODE_CAP,
        },
        "classification_counts": counts,
        "total_node_count": total_nodes,
        "all_executed_complete": all(r["complete"] for r in rows),
        "rows": rows,
        "interpretation": {
            "what_is_proved": (
                "Every completed row is an exact saturated-fiber SAT/UNSAT result. "
                "Unknown rows, if any, are only bounded benchmark results."
            ),
            "next_exact_unit": (
                "If this low-radius wave remains cheap and complete, enlarge the retained "
                "43D wave in radius order. Otherwise condition the first expensive fiber "
                "with one additional exact pairing projection."
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
    print("EFF_AFFINE19_FP43_WAVE=" + json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
