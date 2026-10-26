#!/usr/bin/env python3
"""Exact pairing/ellipsoid separation sweep over all AFFINE17 residual fibers.

AFFINE19 showed that its first 16 FP43 fibers all die at the recursion root:
the completed-square real ellipsoid cannot reach at least one required pairing
interval.  This file extracts that invariant criterion and applies it to every
AFFINE17 nonnegative-radius survivor, in dimensions 43, 48, and 54.

For a pairing functional l with ellipsoid center value c and dual norm q,
its attainable interval over radius r is c +/- sqrt(r*q).  Therefore if
c < lower and (lower-c)^2 > r*q, or c > upper and (c-upper)^2 > r*q,
the entire affine ellipsoid misses the required pairing half-space.  This is
an exact real-separation UNSAT certificate, stronger than integer enumeration.
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
AFF17 = ROOT / "stages/stage32-ex5/effectivity-affine/eff_affine17_empty_ellipsoid_sweep.py"
AFF17_BLOB = "2f173365fe48d91630b1d88d454951469537c42b"
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


def main() -> None:
    req(ENGINE.is_file() and blob(ENGINE) == ENGINE_BLOB, "FP58 engine drift")
    req(AFF17.is_file() and blob(AFF17) == AFF17_BLOB, "AFFINE17 drift")
    req(AFF15.is_file() and blob(AFF15) == AFF15_BLOB, "AFFINE15 drift")

    eng = load(ENGINE, "stage32ex5_eff_affine20_engine")
    aff17 = load(AFF17, "stage32ex5_eff_affine20_aff17")
    aff15 = load(AFF15, "stage32ex5_eff_affine20_aff15")

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
    contexts = {m: aff17.build_context(m, base_rows, P, gram, aff15) for m in masks}

    # Dual norms of every pairing row depend only on the forced-zero mask.
    pair_upper = [eng.NORMAL_MASS] * 92 + [eng.E] * 48
    dual_by_mask = {}
    for mask, ctx in contexts.items():
        K = ctx["K"]
        solve_r = ctx["solve_r"]
        dual = []
        for k in range(140):
            v = (P.row(k) * K).T
            dual.append((v.T * solve_r(v))[0])
        req(all(q >= 0 for q in dual), f"dual norm mask {mask}")
        dual_by_mask[mask] = dual

    hnf_unsat = 0
    negative_radius_unsat = 0
    residual = 0
    separated = 0
    unresolved = 0
    lower_sep = upper_sep = 0
    residual_dim_hist = {}
    separated_dim_hist = {}
    unresolved_dim_hist = {}
    per_key = []
    unresolved_examples = []
    separator_examples = []

    for base4 in aff15.SAMPLE_BASE4:
        key_hnf = key_neg = key_residual = key_sep = key_unres = 0
        for row in (x for x in candidates if x["base4"] == base4):
            ctx = contexts[row["mask"]]
            t = aff17.selected_target(ctx, row["base10"])
            icoord = ctx["invI"] * t
            if not all(getattr(v, "q", 1) == 1 for v in icoord):
                hnf_unsat += 1
                key_hnf += 1
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
                key_neg += 1
                continue

            residual += 1
            key_residual += 1
            dim = ctx["kernel_dimension"]
            residual_dim_hist[dim] = residual_dim_hist.get(dim, 0) + 1
            fixed = P * (bp + K * center)
            dual = dual_by_mask[row["mask"]]
            cert = None
            for k in range(140):
                c = fixed[k]
                upper = pair_upper[k]
                if c < 0:
                    dist = -c
                    gap = dist * dist - radius * dual[k]
                    if gap > 0:
                        cert = (k, "LOW", c, upper, dual[k], gap)
                        break
                elif c > upper:
                    dist = c - upper
                    gap = dist * dist - radius * dual[k]
                    if gap > 0:
                        cert = (k, "HIGH", c, upper, dual[k], gap)
                        break

            if cert is not None:
                separated += 1
                key_sep += 1
                separated_dim_hist[dim] = separated_dim_hist.get(dim, 0) + 1
                if cert[1] == "LOW":
                    lower_sep += 1
                else:
                    upper_sep += 1
                if len(separator_examples) < 20:
                    k, side, c, upper, dual_norm, gap = cert
                    separator_examples.append({
                        "base4": list(base4),
                        "A": row["A"], "AB": row["AB"], "B": row["B"],
                        "C": row["C"], "D": row["D"], "p100": row["p100"],
                        "zero_pattern_mask": row["mask"],
                        "kernel_dimension": dim,
                        "exact_radius_squared": str(radius),
                        "pairing_index_zero_based": k,
                        "pairing_label_one_based": k + 1,
                        "side": side,
                        "center_value": str(c),
                        "required_upper": upper,
                        "dual_norm": str(dual_norm),
                        "strict_separation_gap": str(gap),
                    })
            else:
                unresolved += 1
                key_unres += 1
                unresolved_dim_hist[dim] = unresolved_dim_hist.get(dim, 0) + 1
                if len(unresolved_examples) < 30:
                    unresolved_examples.append({
                        "base4": list(base4),
                        "A": row["A"], "AB": row["AB"], "B": row["B"],
                        "C": row["C"], "D": row["D"], "p100": row["p100"],
                        "zero_pattern_mask": row["mask"],
                        "kernel_dimension": dim,
                        "exact_radius_squared": str(radius),
                        "exact_real_max_C2": str(eng.LOW + radius),
                    })

        per_key.append({
            "base4": list(base4),
            "affine15_hnf_unsat": key_hnf,
            "affine17_negative_radius_unsat": key_neg,
            "affine17_nonnegative_radius_residual": key_residual,
            "pairing_ellipsoid_separation_unsat": key_sep,
            "unresolved_after_separation": key_unres,
        })

    req(hnf_unsat == 478, f"AFFINE15 HNF UNSAT drift: {hnf_unsat}")
    req(negative_radius_unsat == 43, f"AFFINE17 empty ellipsoid drift: {negative_radius_unsat}")
    req(residual == 253, f"AFFINE17 residual drift: {residual}")
    req(residual_dim_hist == {43: 95, 48: 29, 54: 129}, f"residual dimension drift: {residual_dim_hist}")
    req(separated + unresolved == residual, "separation partition")

    out = {
        "schema": "STAGE32EX5_EFF_AFFINE20_PAIRING_ELLIPSOID_SEPARATION_V1",
        "status": "PASS_EXACT_PAIRING_ELLIPSOID_SEPARATION_SWEEP",
        "bad_shell": [eng.LOW, eng.HIGH],
        "population": {
            "affine14_hnf_compatible": 774,
            "affine15_hnf_unsat": hnf_unsat,
            "affine17_negative_radius_unsat": negative_radius_unsat,
            "affine17_nonnegative_radius_residual": residual,
        },
        "pairing_ellipsoid_separation_unsat": separated,
        "unresolved_after_separation": unresolved,
        "lower_separation_count": lower_sep,
        "upper_separation_count": upper_sep,
        "residual_kernel_dimension_histogram": {
            str(k): residual_dim_hist[k] for k in sorted(residual_dim_hist)
        },
        "separated_kernel_dimension_histogram": {
            str(k): separated_dim_hist[k] for k in sorted(separated_dim_hist)
        },
        "unresolved_kernel_dimension_histogram": {
            str(k): unresolved_dim_hist[k] for k in sorted(unresolved_dim_hist)
        },
        "rows": per_key,
        "separator_examples": separator_examples,
        "unresolved_examples": unresolved_examples,
        "interpretation": {
            "what_is_proved": (
                "Each separated fiber has an exact pairing functional whose required "
                "interval is strictly disjoint from the full completed-square real "
                "ellipsoid. Therefore that entire refined affine fiber is bad-shell UNSAT "
                "without lattice enumeration."
            ),
            "next_exact_unit": (
                "If many residual fibers separate, restrict future FP work to the exact "
                "unresolved complement. If none remain, retain the five-key producer "
                "certificate and prepare, but do not self-promote, the downstream adapter."
            ),
            "what_is_not_proved": (
                "This remains an EX5 producer result; effectivity, MAIN, receiver, theorem, "
                "endpoint, and merge credit remain false until the owning downstream "
                "contract/audit consumes it."
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
    print("EFF_AFFINE20_PAIRING_SEPARATION=" + json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
