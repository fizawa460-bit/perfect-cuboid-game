#!/usr/bin/env python3
"""Exact optimized two-halfspace dual separation for AFFINE20 residual fibers.

AFFINE21 tested equal-weight sums of two pairing inequalities and found no new
separation.  Here the nonnegative dual multipliers are optimized exactly.

At the completed-square center write every violated box constraint as
    a_i(y) >= b_i > 0
on the centered kernel coordinate y with ellipsoid y^T R y <= radius.
For any lambda_i >= 0,
    (lambda^T b)^2 <= (y^T R y) * (lambda^T G lambda)
is necessary, where G is the exact dual Gram matrix.  For each pair of
violated constraints with positive-definite 2x2 Gram, the unconstrained optimum
lambda=G^{-1}b is exact.  If both multipliers are positive and
    b^T G^{-1} b > radius,
the whole affine fiber is exactly bad-shell UNSAT.
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
AFF20 = ROOT / "stages/stage32-ex5/effectivity-affine/eff_affine20_pairing_ellipsoid_separation.py"
AFF20_BLOB = "f3bf868bfa9d2a35ef6b6f6d464197b5b2376321"


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
    req(AFF20.is_file() and blob(AFF20) == AFF20_BLOB, "AFFINE20 drift")

    eng = load(ENGINE, "stage32ex5_eff_affine22_engine")
    aff17 = load(AFF17, "stage32ex5_eff_affine22_aff17")
    aff15 = load(AFF15, "stage32ex5_eff_affine22_aff15")

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
    pair_upper = [eng.NORMAL_MASS] * 92 + [eng.E] * 48

    dual_gram = {}
    for mask, ctx in contexts.items():
        V = P * ctx["K"]
        W = ctx["solve_r"](V.T)
        G = V * W
        req(G == G.T, f"dual Gram symmetry mask {mask}")
        req(all(G[i, i] >= 0 for i in range(140)), f"dual Gram diagonal mask {mask}")
        dual_gram[mask] = G

    hnf_unsat = 0
    negative_radius_unsat = 0
    single_separated = 0
    affine20_unresolved = 0
    optimized_pair_separated = 0
    final_unresolved = 0
    sep_dim_hist = {}
    final_dim_hist = {}
    per_key = []
    cert_examples = []
    unresolved_examples = []

    for base4 in aff15.SAMPLE_BASE4:
        key_aff20 = key_sep = key_final = 0
        for row in (x for x in candidates if x["base4"] == base4):
            ctx = contexts[row["mask"]]
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

            affine20_unresolved += 1
            key_aff20 += 1
            dim = ctx["kernel_dimension"]

            # Signed violated constraints a(y)>=b>0.
            violations = []
            for k in range(140):
                c = fixed[k]
                upper = pair_upper[k]
                if c < 0:
                    violations.append((k, 1, -c, "LOW"))
                elif c > upper:
                    violations.append((k, -1, c - upper, "HIGH"))

            cert = None
            for p in range(len(violations)):
                i, si, bi, side_i = violations[p]
                g11 = G[i, i]
                for qidx in range(p + 1, len(violations)):
                    j, sj, bj, side_j = violations[qidx]
                    g22 = G[j, j]
                    g12 = si * sj * G[i, j]
                    det = g11 * g22 - g12 * g12
                    if det <= 0:
                        continue
                    lam1 = (g22 * bi - g12 * bj) / det
                    lam2 = (g11 * bj - g12 * bi) / det
                    if lam1 <= 0 or lam2 <= 0:
                        continue
                    energy = bi * lam1 + bj * lam2
                    if energy > radius:
                        cert = {
                            "pairing_indices_zero_based": [i, j],
                            "pairing_labels_one_based": [i + 1, j + 1],
                            "constraint_sides": [side_i, side_j],
                            "required_distances": [str(bi), str(bj)],
                            "dual_gram_2x2": [
                                [str(g11), str(g12)],
                                [str(g12), str(g22)],
                            ],
                            "optimal_nonnegative_multipliers": [str(lam1), str(lam2)],
                            "exact_dual_energy_lower_bound": str(energy),
                            "exact_radius_squared": str(radius),
                            "strict_gap": str(energy - radius),
                        }
                        break
                if cert is not None:
                    break

            if cert is not None:
                optimized_pair_separated += 1
                key_sep += 1
                sep_dim_hist[dim] = sep_dim_hist.get(dim, 0) + 1
                if len(cert_examples) < 20:
                    cert_examples.append({
                        "base4": list(base4),
                        "A": row["A"], "AB": row["AB"], "B": row["B"],
                        "C": row["C"], "D": row["D"], "p100": row["p100"],
                        "zero_pattern_mask": row["mask"],
                        "kernel_dimension": dim,
                        "certificate": cert,
                    })
            else:
                final_unresolved += 1
                key_final += 1
                final_dim_hist[dim] = final_dim_hist.get(dim, 0) + 1
                if len(unresolved_examples) < 30:
                    unresolved_examples.append({
                        "base4": list(base4),
                        "A": row["A"], "AB": row["AB"], "B": row["B"],
                        "C": row["C"], "D": row["D"], "p100": row["p100"],
                        "zero_pattern_mask": row["mask"],
                        "kernel_dimension": dim,
                        "exact_radius_squared": str(radius),
                        "exact_real_max_C2": str(eng.LOW + radius),
                        "violated_center_constraint_count": len(violations),
                    })

        per_key.append({
            "base4": list(base4),
            "affine20_unresolved": key_aff20,
            "optimized_two_halfspace_unsat": key_sep,
            "unresolved_after_optimized_two_halfspace": key_final,
        })

    req(hnf_unsat == 478, f"AFFINE15 HNF drift: {hnf_unsat}")
    req(negative_radius_unsat == 43, f"AFFINE17 negative-radius drift: {negative_radius_unsat}")
    req(single_separated == 226, f"AFFINE20 separation drift: {single_separated}")
    req(affine20_unresolved == 27, f"AFFINE20 unresolved drift: {affine20_unresolved}")
    req(optimized_pair_separated + final_unresolved == 27, "optimized pair partition")

    out = {
        "schema": "STAGE32EX5_EFF_AFFINE22_OPTIMIZED_TWO_HALFSPACE_DUAL_V1",
        "status": "PASS_EXACT_OPTIMIZED_TWO_HALFSPACE_DUAL_SWEEP",
        "bad_shell": [eng.LOW, eng.HIGH],
        "population": {
            "affine14_hnf_compatible": 774,
            "affine15_hnf_unsat": hnf_unsat,
            "affine17_negative_radius_unsat": negative_radius_unsat,
            "affine20_single_pairing_unsat": single_separated,
            "affine20_unresolved": affine20_unresolved,
        },
        "optimized_two_halfspace_unsat": optimized_pair_separated,
        "unresolved_after_optimized_two_halfspace": final_unresolved,
        "separated_kernel_dimension_histogram": {
            str(k): sep_dim_hist[k] for k in sorted(sep_dim_hist)
        },
        "final_unresolved_kernel_dimension_histogram": {
            str(k): final_dim_hist[k] for k in sorted(final_dim_hist)
        },
        "rows": per_key,
        "certificate_examples": cert_examples,
        "unresolved_examples": unresolved_examples,
        "interpretation": {
            "what_is_proved": (
                "Each separated fiber has an exact nonnegative two-constraint dual "
                "certificate whose minimum R-norm exceeds the completed-square radius. "
                "The full refined affine bad-shell fiber is therefore empty over the "
                "reals, hence also over the lattice."
            ),
            "next_exact_unit": (
                "Use exact FP on any surviving 43D fibers. For surviving 54D fibers, "
                "extend the same dual certificate to a small active set or add one exact "
                "conditioning observable before broad enumeration."
            ),
            "what_is_not_proved": (
                "Unresolved fibers remain open and no effectivity, MAIN, receiver, "
                "theorem, endpoint, or merge credit is self-promoted."
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
    print("EFF_AFFINE22_OPTIMIZED_TWO_HALFSPACE=" + json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
