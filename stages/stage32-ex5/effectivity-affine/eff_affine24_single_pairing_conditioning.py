#!/usr/bin/env python3
"""Exact one-pairing conditioning probe for the AFFINE23 capped residual.

AFFINE23's smallest-radius 43D residual hit its 50k-node cap. Do not scale
that search horizontally. Instead, rank individual all140 pairing observables
by their exact lattice/ellipsoid projection domain, then refine the best
bounded candidates by one equality p_k=v.

Each value branch is classified only by exact HNF image membership, exact
completed-square emptiness, or exact one-pairing real separation. Any branch
left after those tests remains UNKNOWN. This leaf is a bounded research probe
and grants no downstream credit.
"""
from __future__ import annotations

import hashlib
import importlib.util
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
AFF22 = ROOT / "stages/stage32-ex5/effectivity-affine/eff_affine22_optimized_two_halfspace_dual.py"
AFF22_BLOB = "0fda364e20bc5f41e466951793e806ce0169c1cd"
AFF23 = ROOT / "stages/stage32-ex5/effectivity-affine/eff_affine23_fp43_residual_benchmark.py"
AFF23_BLOB = "e476348485ea03633cc9d3063d899446c976fb34"

TARGET_BASE4 = (0, 1, 1, 1)
TARGET_A = 5
TARGET_AB = 6
TARGET_C = 2
TARGET_P100 = 0
TARGET_MASK = 8
TARGET_RADIUS = "4229/120"
CANDIDATE_LIMIT = 16


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


def build_conditioned_context(pair_idx: int, base_rows, P: Matrix, gram: Matrix, aff15):
    rows = list(base_rows)
    forced_indices = []
    for bit, (_name, indices) in enumerate(aff15.GROUPS):
        if not (TARGET_MASK & (1 << bit)):
            continue
        for idx in indices:
            rows.append(P.row(idx))
            forced_indices.append(idx)
    rows.append(P.row(pair_idx))

    full = Matrix.vstack(*rows)
    pivots = list(full.T.rref()[1])
    F = full[pivots, :]
    rank = F.rows
    if rank != 22:
        return None
    req(F.rank() == 22, "conditioned fixed rank")

    hf, tf = fmpz_mat(
        [[int(F[i, j]) for j in range(64)] for i in range(rank)]
    ).transpose().hnf(transform=True)
    H = Matrix([[int(hf[i, j]) for j in range(hf.ncols())] for i in range(hf.nrows())])
    T = Matrix([[int(tf[i, j]) for j in range(tf.ncols())] for i in range(tf.nrows())])
    req(abs(int(tf.det())) == 1 and H == T * F.T, "conditioned HNF replay")

    A = T.T[:, :rank]
    K = T.T[:, rank:]
    I = F * A
    req(K.shape == (64, 42), "conditioned kernel shape")
    req(F * K == Matrix.zeros(rank, 42), "conditioned kernel equality")
    R = -(K.T * gram * K)
    solve_r = aff15.ldl_solver(R)

    V = P * K
    W = solve_r(V.T)
    G = V * W
    req(G == G.T, "conditioned dual Gram symmetry")

    return {
        "pair_idx": pair_idx,
        "forced_indices": forced_indices,
        "pivots": pivots,
        "rank": rank,
        "kernel_dimension": 42,
        "image_index": abs(int(I.det())),
        "A": A,
        "K": K,
        "invI": I.inv(),
        "solve_r": solve_r,
        "dual_diag": [G[i, i] for i in range(140)],
    }


def selected_target(ctx, base10, pair_value: int) -> Matrix:
    all_targets = list(base10) + [0] * len(ctx["forced_indices"]) + [pair_value]
    return Matrix([all_targets[i] for i in ctx["pivots"]])


def branch_classification(ctx, base10, pair_value, P, gram, eng):
    t = selected_target(ctx, base10, pair_value)
    icoord = ctx["invI"] * t
    if not all(getattr(v, "q", 1) == 1 for v in icoord):
        return {"value": pair_value, "classification": "HNF_IMAGE_UNSAT"}

    bp = ctx["A"] * icoord
    req(all(getattr(v, "q", 1) == 1 for v in bp), "conditioned integral base point")
    K = ctx["K"]
    cross = K.T * gram * bp
    center = ctx["solve_r"](cross)
    q0 = (bp.T * gram * bp)[0]
    radius = q0 - eng.LOW + (cross.T * center)[0]
    if radius < 0:
        return {
            "value": pair_value,
            "classification": "EMPTY_ELLIPSOID_UNSAT",
            "exact_radius_squared": str(radius),
        }

    fixed = P * (bp + K * center)
    pair_upper = [eng.NORMAL_MASS] * 92 + [eng.E] * 48
    for k in range(140):
        c = fixed[k]
        upper = pair_upper[k]
        q = ctx["dual_diag"][k]
        if c < 0 and c * c > radius * q:
            return {
                "value": pair_value,
                "classification": "REAL_PAIRING_SEPARATION_UNSAT",
                "separator_index": k,
                "separator_side": "LOW",
                "exact_radius_squared": str(radius),
            }
        if c > upper and (c - upper) * (c - upper) > radius * q:
            return {
                "value": pair_value,
                "classification": "REAL_PAIRING_SEPARATION_UNSAT",
                "separator_index": k,
                "separator_side": "HIGH",
                "exact_radius_squared": str(radius),
            }

    return {
        "value": pair_value,
        "classification": "UNRESOLVED_AFTER_ONE_PAIRING_CONDITIONING",
        "kernel_dimension": 42,
        "exact_radius_squared": str(radius),
        "exact_real_max_C2": str(eng.LOW + radius),
    }


def main() -> None:
    for path, expected, label in (
        (ENGINE, ENGINE_BLOB, "FP58 engine"),
        (AFF15, AFF15_BLOB, "AFFINE15"),
        (AFF17, AFF17_BLOB, "AFFINE17"),
        (AFF22, AFF22_BLOB, "AFFINE22"),
        (AFF23, AFF23_BLOB, "AFFINE23"),
    ):
        req(path.is_file() and blob(path) == expected, label + " drift")

    eng = load(ENGINE, "stage32ex5_eff_affine24_engine")
    aff15 = load(AFF15, "stage32ex5_eff_affine24_aff15")
    aff17 = load(AFF17, "stage32ex5_eff_affine24_aff17")

    F6, A6, I6, RK58, R58, _L, _d, _c, _u, P, gram = eng.build()
    Arow = sum((P.row(i) for i in range(92, 104)), Matrix.zeros(1, 64))
    ABrow = sum((P.row(i) for i in range(92, 116)), Matrix.zeros(1, 64))
    Crow = sum((P.row(i) for i in range(116, 128)), Matrix.zeros(1, 64))
    P100row = P.row(aff15.P100_INDEX)
    base_rows = [F6.row(i) for i in range(6)] + [Arow, ABrow, Crow, P100row]

    base10 = [
        eng.D, eng.E, *TARGET_BASE4,
        TARGET_A, TARGET_AB, TARGET_C, TARGET_P100,
    ]
    raw = aff17.build_context(TARGET_MASK, base_rows, P, gram, aff15)
    req(raw["rank"] == 21 and raw["kernel_dimension"] == 43, "AFFINE23 raw dimension drift")
    t = aff17.selected_target(raw, base10)
    icoord = raw["invI"] * t
    req(all(getattr(v, "q", 1) == 1 for v in icoord), "AFFINE23 target HNF drift")
    bp = raw["A"] * icoord
    q0 = (bp.T * gram * bp)[0]
    cross = raw["K"].T * gram * bp
    center = raw["solve_r"](cross)
    radius = q0 - eng.LOW + (cross.T * center)[0]
    req(str(radius) == TARGET_RADIUS, f"AFFINE23 radius drift: {radius}")

    raw_R = -(raw["K"].T * gram * raw["K"])
    pair_upper = [eng.NORMAL_MASS] * 92 + [eng.E] * 48
    forced = set(raw["forced_indices"])

    projection_rows = []
    for pair_idx in range(140):
        if pair_idx in forced:
            continue
        coeff = P.row(pair_idx) * raw["K"]
        if all(v == 0 for v in coeff):
            continue
        domain = aff15.allowed_projection(
            P.row(pair_idx), bp, raw["K"], raw_R, raw["solve_r"],
            gram, eng.LOW, pair_upper[pair_idx],
        )
        projection_rows.append({
            "pairing_index": pair_idx,
            "block": "normal" if pair_idx < 92 else "exceptional",
            "domain": domain,
            "domain_size": len(domain),
        })

    req(projection_rows, "no conditioning candidates")
    projection_rows.sort(key=lambda r: (
        r["domain_size"],
        0 if r["block"] == "exceptional" else 1,
        r["pairing_index"],
    ))

    immediate = next((r for r in projection_rows if r["domain_size"] == 0), None)
    evaluated = []
    if immediate is None:
        for cand in projection_rows[:CANDIDATE_LIMIT]:
            ctx = build_conditioned_context(cand["pairing_index"], base_rows, P, gram, aff15)
            if ctx is None:
                continue
            branches = [
                branch_classification(ctx, base10, value, P, gram, eng)
                for value in cand["domain"]
            ]
            unresolved = [
                b for b in branches
                if b["classification"] == "UNRESOLVED_AFTER_ONE_PAIRING_CONDITIONING"
            ]
            evaluated.append({
                "pairing_index": cand["pairing_index"],
                "block": cand["block"],
                "projection_domain": cand["domain"],
                "projection_domain_size": cand["domain_size"],
                "conditioned_image_index": ctx["image_index"],
                "branch_counts": {
                    key: sum(1 for b in branches if b["classification"] == key)
                    for key in sorted({b["classification"] for b in branches})
                },
                "unresolved_branch_count": len(unresolved),
                "unresolved_branches": unresolved,
                "branches": branches,
            })

    if immediate is not None:
        best = {
            "pairing_index": immediate["pairing_index"],
            "block": immediate["block"],
            "projection_domain": [],
            "projection_domain_size": 0,
            "unresolved_branch_count": 0,
            "branches": [],
            "classification": "SELECTED_AFFINE23_FIBER_UNSAT_EMPTY_INTEGER_PROJECTION",
        }
    else:
        req(evaluated, "no independent conditioned candidates")
        evaluated.sort(key=lambda r: (
            r["unresolved_branch_count"],
            r["projection_domain_size"],
            r["pairing_index"],
        ))
        best = evaluated[0]

    closed = best["unresolved_branch_count"] == 0
    out = {
        "schema": "STAGE32EX5_EFF_AFFINE24_SINGLE_PAIRING_CONDITIONING_V1",
        "status": "PASS_BOUNDED_EXACT_SINGLE_PAIRING_CONDITIONING_PROBE",
        "predecessor": {
            "affine23_classification": "UNKNOWN_BENCHMARK_NODE_CAP",
            "base4": list(TARGET_BASE4),
            "A": TARGET_A,
            "AB": TARGET_AB,
            "B": TARGET_AB - TARGET_A,
            "C": TARGET_C,
            "D": eng.E - TARGET_AB - TARGET_C,
            "p100": TARGET_P100,
            "zero_pattern_mask": TARGET_MASK,
            "kernel_dimension": 43,
            "exact_radius_squared": str(radius),
            "node_cap": 50000,
        },
        "selection": {
            "candidate_universe": len(projection_rows),
            "candidate_limit": CANDIDATE_LIMIT,
            "ordering": "projection_domain_size,exceptional_first,pairing_index",
            "smallest_projection_candidates": projection_rows[:CANDIDATE_LIMIT],
        },
        "evaluated": evaluated,
        "best_conditioner": best,
        "selected_fiber_closed_exactly": closed,
        "interpretation": {
            "what_is_proved": (
                "Every classified branch uses only exact saturated HNF image membership, "
                "exact completed-square emptiness, or exact real pairing separation. "
                "If selected_fiber_closed_exactly=true, the AFFINE23 capped 43D fiber is "
                "UNSAT without broad Fincke--Pohst scaleout."
            ),
            "next_exact_unit": (
                "If the selected fiber closes, apply the same deterministic conditioner "
                "criterion to the remaining AFFINE22 43D residuals. Otherwise run one bounded "
                "exact FP42 benchmark only on the smallest unresolved conditioned branch."
            ),
            "what_is_not_proved": (
                "Unresolved conditioned branches remain UNKNOWN. No effectivity, MAIN, "
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
    print("EFF_AFFINE24_SINGLE_PAIRING=" + json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
