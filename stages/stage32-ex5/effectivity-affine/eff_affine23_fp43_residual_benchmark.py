#!/usr/bin/env python3
"""Bounded exact FP43 benchmark on the AFFINE22 residual frontier.

AFFINE20/22 leave 27 exact affine fibers unresolved by real ellipsoid
separation: 14 with kernel dimension 43 and 13 with kernel dimension 54.
This leaf reconstructs that exact predecessor partition, selects the
smallest-radius 43D residual deterministically, and runs one bounded exact
Fincke--Pohst search using the retained AFFINE19 engine.

A completed SAT/UNSAT row is exact for that one saturated affine fiber.
A node-cap outcome remains UNKNOWN. No downstream credit is self-promoted.
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
AFF17 = ROOT / "stages/stage32-ex5/effectivity-affine/eff_affine17_empty_ellipsoid_sweep.py"
AFF17_BLOB = "2f173365fe48d91630b1d88d454951469537c42b"
AFF19 = ROOT / "stages/stage32-ex5/effectivity-affine/eff_affine19_fp43_wave.py"
AFF19_BLOB = "d9e977f88072fa39f528a954c980de7ada84c9f5"
AFF22 = ROOT / "stages/stage32-ex5/effectivity-affine/eff_affine22_optimized_two_halfspace_dual.py"
AFF22_BLOB = "0fda364e20bc5f41e466951793e806ce0169c1cd"

PER_FIBER_NODE_CAP = 50000
TOTAL_NODE_CAP = 50000


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


def main() -> None:
    # Lock every executable predecessor before importing any of it.
    req(ENGINE.is_file() and blob(ENGINE) == ENGINE_BLOB, "FP58 engine drift")
    req(AFF15.is_file() and blob(AFF15) == AFF15_BLOB, "AFFINE15 drift")
    req(AFF17.is_file() and blob(AFF17) == AFF17_BLOB, "AFFINE17 drift")
    req(AFF19.is_file() and blob(AFF19) == AFF19_BLOB, "AFFINE19 drift")
    req(AFF22.is_file() and blob(AFF22) == AFF22_BLOB, "AFFINE22 drift")

    eng = load(ENGINE, "stage32ex5_eff_affine23_engine")
    aff15 = load(AFF15, "stage32ex5_eff_affine23_aff15")
    aff17 = load(AFF17, "stage32ex5_eff_affine23_aff17")
    aff19 = load(AFF19, "stage32ex5_eff_affine23_aff19")

    # This is intentionally a one-fiber benchmark, not a scaleout.
    aff19.PER_FIBER_NODE_CAP = PER_FIBER_NODE_CAP
    aff19.TOTAL_NODE_CAP = TOTAL_NODE_CAP

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
    raw_contexts = {m: aff17.build_context(m, base_rows, P, gram, aff15) for m in masks}
    pair_upper = [eng.NORMAL_MASS] * 92 + [eng.E] * 48

    dual_gram = {}
    for mask, ctx in raw_contexts.items():
        V = P * ctx["K"]
        W = ctx["solve_r"](V.T)
        G = V * W
        req(G == G.T, f"dual Gram symmetry mask {mask}")
        dual_gram[mask] = G

    hnf_unsat = 0
    negative_radius_unsat = 0
    single_separated = 0
    unresolved = []
    residual43 = []

    for row in candidates:
        ctx = raw_contexts[row["mask"]]
        t = aff17.selected_target(ctx, row["base10"])
        icoord = ctx["invI"] * t
        if not all(getattr(v, "q", 1) == 1 for v in icoord):
            hnf_unsat += 1
            continue

        bp = ctx["A"] * icoord
        req(all(getattr(v, "q", 1) == 1 for v in bp), "integral base point")
        K = ctx["K"]
        cross = K.T * gram * bp
        center = ctx["solve_r"](cross)
        q0 = (bp.T * gram * bp)[0]
        radius = q0 - eng.LOW + (cross.T * center)[0]
        if radius < 0:
            negative_radius_unsat += 1
            continue

        fixed = P * (bp + K * center)
        G = dual_gram[row["mask"]]
        single = False
        for k in range(140):
            c = fixed[k]
            upper = pair_upper[k]
            q = G[k, k]
            if c < 0 and c * c > radius * q:
                single = True
                break
            if c > upper and (c - upper) * (c - upper) > radius * q:
                single = True
                break
        if single:
            single_separated += 1
            continue

        item = dict(row)
        item["radius"] = radius
        item["kernel_dimension"] = ctx["kernel_dimension"]
        unresolved.append(item)
        if ctx["kernel_dimension"] == 43:
            residual43.append(item)

    req(hnf_unsat == 478, f"AFFINE15 HNF drift: {hnf_unsat}")
    req(negative_radius_unsat == 43, f"AFFINE17 negative-radius drift: {negative_radius_unsat}")
    req(single_separated == 226, f"AFFINE20 separation drift: {single_separated}")
    req(len(unresolved) == 27, f"AFFINE22 unresolved drift: {len(unresolved)}")
    req(len(residual43) == 14, f"AFFINE22 43D residual drift: {len(residual43)}")
    req(sum(1 for x in unresolved if x["kernel_dimension"] == 54) == 13, "AFFINE22 54D residual drift")

    residual43.sort(key=lambda r: (
        r["radius"], tuple(r["base4"]), r["A"], r["AB"], r["C"], r["p100"], r["mask"]
    ))
    target = residual43[0]

    # Bind the deterministic selection. This is the smallest exact radius among
    # the 14 AFFINE22 residual 43D fibers.
    req(tuple(target["base4"]) == (0, 1, 1, 1), "selected base4 drift")
    req(
        (target["A"], target["AB"], target["C"], target["p100"], target["mask"]) == (5, 6, 2, 0, 8),
        "selected affine tuple drift",
    )
    req(str(target["radius"]) == "4229/120", f"selected radius drift: {target['radius']}")

    raw = raw_contexts[target["mask"]]
    ctx = dict(raw)
    ctx["selected_target"] = lambda base10, _ctx=raw: aff17.selected_target(_ctx, base10)
    lc = aff19.build_lll_context(ctx, P, gram)
    result = aff19.solve_one(target, ctx, lc, P, gram, eng, 0)

    out = {
        "schema": "STAGE32EX5_EFF_AFFINE23_FP43_RESIDUAL_BENCHMARK_V1",
        "status": "PASS_BOUNDED_EXACT_FP43_RESIDUAL_BENCHMARK",
        "predecessor_partition": {
            "affine14_hnf_compatible": 774,
            "affine15_hnf_unsat": hnf_unsat,
            "affine17_negative_radius_unsat": negative_radius_unsat,
            "affine20_single_pairing_unsat": single_separated,
            "affine22_unresolved": len(unresolved),
            "affine22_unresolved_43d": len(residual43),
            "affine22_unresolved_54d": 13,
        },
        "selection": {
            "rule": "smallest exact radius among AFFINE22 unresolved kernel_dimension=43 fibers",
            "node_cap": PER_FIBER_NODE_CAP,
        },
        "result": result,
        "interpretation": {
            "what_is_proved": (
                "If complete=true, this one saturated AFFINE22 residual 43D fiber is "
                "resolved exactly by Fincke--Pohst. If complete=false, it remains UNKNOWN."
            ),
            "next_exact_unit": (
                "If this benchmark completes cheaply, extend the same retained solver over "
                "the remaining 13 residual 43D fibers in exact-radius order. If it hits the "
                "node cap, do not scale out: add one exact conditioning observable first."
            ),
            "what_is_not_proved": (
                "The remaining AFFINE22 residual fibers are untouched. No effectivity, MAIN, "
                "receiver, theorem, endpoint, or merge credit is self-promoted."
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
    print("EFF_AFFINE23_FP43_RESIDUAL=" + json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
