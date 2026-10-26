#!/usr/bin/env python3
"""Exact x4-conditioned saturated 57D affine kernel preflight."""
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
X4_INDEX = 48

SAMPLE_BASE4 = (
    (0, 1, 1, 1),
    (0, 4, 4, 8),
    (0, 6, 2, 6),
    (1, 2, 2, 2),
    (1, 3, 3, 3),
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


def ldl_solver(A: Matrix):
    L, D = A.LDLdecomposition(hermitian=False)
    req(A == L * D * L.T, "LDL replay")
    req(all(D[i, i] > 0 for i in range(D.rows)), "positive diagonal")

    def solve(b: Matrix) -> Matrix:
        n = A.rows
        y = [0] * n
        for i in range(n):
            v = b[i, 0]
            for j in range(i):
                v -= L[i, j] * y[j]
            y[i] = v / L[i, i]
        z = [y[i] / D[i, i] for i in range(n)]
        x = [0] * n
        for i in range(n - 1, -1, -1):
            v = z[i]
            for j in range(i + 1, n):
                v -= L[j, i] * x[j]
            x[i] = v / L[i, i]
        out = Matrix(x)
        req(A * out == b, "LDL solve")
        return out

    return solve


def matrix_sha(m: Matrix) -> str:
    payload = [[str(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]
    return hashlib.sha256(json.dumps(payload, separators=(",", ":")).encode()).hexdigest()


def main() -> None:
    req(ENGINE.is_file() and blob(ENGINE) == ENGINE_BLOB, "FP58 engine drift")
    eng = load(ENGINE, "stage32ex5_eff_affine09_engine")
    F6, _A6, I6, RK58, R58, _L, _diag, _coeff, _dual, P, gram = eng.build()

    x4row = P.row(X4_INDEX)
    F7 = F6.col_join(x4row)
    req(F7.shape == (7, 64) and F7.rank() == 7, "x4 fixed map rank")

    hf, tf = fmpz_mat(
        [[int(F7[i, j]) for j in range(64)] for i in range(7)]
    ).transpose().hnf(transform=True)
    T = Matrix([[int(tf[i, j]) for j in range(tf.ncols())] for i in range(tf.nrows())])
    A7 = T.T[:, :7]
    K7 = T.T[:, 7:]
    I7 = F7 * A7
    req(K7.shape == (64, 57) and F7 * K7 == Matrix.zeros(7, 57), "kernel57")
    req(abs(int(tf.det())) == 1, "HNF transform unimodular")

    Q7 = -(K7.T * gram * K7)
    qf, lf = fmpz_mat(
        [[int(Q7[i, j]) for j in range(57)] for i in range(57)]
    ).lll(transform=True, rep="gram", gram="exact")
    U7 = Matrix([[int(lf[i, j]) for j in range(57)] for i in range(57)])
    R7 = Matrix([[int(qf[i, j]) for j in range(57)] for i in range(57)])
    RK57 = K7 * U7.T
    req(abs(int(lf.det())) == 1, "LLL transform unimodular")
    req(R7 == -(RK57.T * gram * RK57), "LLL replay")
    L7, D7 = R7.LDLdecomposition(hermitian=False)
    req(R7 == L7 * D7 * L7.T and all(D7[i, i] > 0 for i in range(57)),
        "kernel57 positive definite")

    # Recompute the exact x4 projection from the 58D outer ellipsoid.
    solve58 = ldl_solver(R58)
    x4_kernel = (P * RK58).row(X4_INDEX).T
    x4_dual = (x4_kernel.T * solve58(x4_kernel))[0]
    rows = []
    total_projected = total_hnf = 0
    for base4 in SAMPLE_BASE4:
        target6 = Matrix([eng.D, eng.E, *base4])
        ic6 = I6.inv() * target6
        req(all(getattr(x, "q", 1) == 1 for x in ic6), "sample base4 image")
        # Reconstruct the same 58D affine base using the six-observable HNF.
        # A6 is recoverable from the original transform through target solve:
        # solve F6*x=target via the canonical image columns embedded in build.
        # The original engine does not return A6 after this point, so rebuild
        # the affine point from the HNF image coordinates using F6's transform.
        # We retained A6 from build above in the actual binding.
        # (The name is kept explicit below to prevent accidental basis mixing.)
        A6 = _A6
        bp = A6 * ic6
        cross = RK58.T * gram * bp
        center = solve58(cross)
        radius = (bp.T * gram * bp)[0] - eng.LOW + (cross.T * center)[0]
        x4_center = (x4row * (bp + RK58 * center))[0]
        limit2 = radius * x4_dual
        projected = [
            k for k in range(eng.NORMAL_MASS + 1)
            if (k - x4_center) * (k - x4_center) <= limit2
        ]

        inv7 = I7.inv()
        hnf_ok = []
        for x4 in projected:
            target7 = Matrix([eng.D, eng.E, *base4, x4])
            ic7 = inv7 * target7
            if all(getattr(x, "q", 1) == 1 for x in ic7):
                hnf_ok.append(x4)

        total_projected += len(projected)
        total_hnf += len(hnf_ok)
        rows.append({
            "base4": list(base4),
            "projected_x4": projected,
            "projected_count": len(projected),
            "hnf_image_compatible_x4": hnf_ok,
            "hnf_image_compatible_count": len(hnf_ok),
            "projection_to_hnf_reduction": len(projected) - len(hnf_ok),
        })

    out = {
        "schema": "STAGE32EX5_EFF_AFFINE09_X4_CONDITIONED_KERNEL57_V1",
        "status": "PASS_X4_CONDITIONED_SATURATED_KERNEL57",
        "fixed_observables": ["d", "e", "a", "b", "c", "t", "x4"],
        "fixed_map_rank": 7,
        "kernel_dimension": 57,
        "x4_pairing_label_1based": 49,
        "hnf_image_diagonal": [int(I7[i, i]) for i in range(7)],
        "hnf_image_index": abs(int(I7.det())),
        "fixed_map_sha256": matrix_sha(F7),
        "kernel_sha256": matrix_sha(K7),
        "reduced_gram_sha256": matrix_sha(R7),
        "restricted_negative_gram_positive_definite": True,
        "rows": rows,
        "summary": {
            "projected_x4_total": total_projected,
            "hnf_image_compatible_x4_total": total_hnf,
            "max_hnf_image_compatible_per_key": max(r["hnf_image_compatible_count"] for r in rows),
            "min_hnf_image_compatible_per_key": min(r["hnf_image_compatible_count"] for r in rows),
        },
        "interpretation": {
            "what_is_proved": "Every d18/e8 five-key bad-shell witness lies in one of the retained x4-conditioned saturated 57D affine fibers listed here.",
            "next_exact_unit": "Port the all140 exact FP recursion to the 57D x4-conditioned fibers and benchmark one bounded fiber before any heavy authorization.",
            "what_is_not_proved": "No listed fiber is asserted feasible or infeasible; no effectivity or MAIN credit.",
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
    print("EFF_AFFINE09_X4_KERNEL57=" + json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
