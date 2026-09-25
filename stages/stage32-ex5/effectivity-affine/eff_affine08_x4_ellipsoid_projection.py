#!/usr/bin/env python3
"""Exact x4 projection of the d18/e8 bad-shell outer ellipsoid."""
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

from sympy import Matrix

ROOT = Path(__file__).resolve().parents[3]
ENGINE = ROOT / "stages/stage32-ex5/effectivity-affine/eff_affine01_fp58_engine.py"
ENGINE_BLOB = "e7857e9213ca9107edada1424012a7a1c902a625"
X4_PAIRING_INDEX = 48  # retained label 49 -> pairings[label-1]

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
        req(A * out == b, "LDL solve replay")
        return out

    return solve


def main() -> None:
    req(ENGINE.is_file() and blob(ENGINE) == ENGINE_BLOB, "FP58 engine drift")
    eng = load(ENGINE, "stage32ex5_eff_affine08_engine")
    _F, A, I, RK, R, _L, _diag, _coeff, _dual, P, gram = eng.build()

    solve_r = ldl_solver(R)
    x4_kernel = (P * RK).row(X4_PAIRING_INDEX).T
    x4_dual = (x4_kernel.T * solve_r(x4_kernel))[0]
    req(x4_dual > 0, "x4 dual norm")

    rows = []
    for base4 in SAMPLE_BASE4:
        target = Matrix([eng.D, eng.E, *base4])
        ic = I.inv() * target
        integral = all(getattr(x, "q", 1) == 1 for x in ic)
        row = {"base4": list(base4), "hnf_image_integral": integral}
        if not integral:
            row.update({"classification": "HNF_IMAGE_UNSAT", "possible_x4": []})
            rows.append(row)
            continue

        bp = A * ic
        req(all(getattr(x, "q", 1) == 1 for x in bp), "integral affine base")
        cross = RK.T * gram * bp
        center = solve_r(cross)
        radius = (bp.T * gram * bp)[0] - eng.LOW + (cross.T * center)[0]
        req(radius >= 0, "outer ellipsoid radius")

        x4_center = (P.row(X4_PAIRING_INDEX) * (bp + RK * center))[0]
        limit2 = radius * x4_dual
        possible = [
            k for k in range(eng.NORMAL_MASS + 1)
            if (k - x4_center) * (k - x4_center) <= limit2
        ]
        row.update({
            "classification": "OUTER_ELLIPSOID_X4_PROJECTED",
            "x4_center": str(x4_center),
            "x4_dual_norm": str(x4_dual),
            "outer_radius": str(radius),
            "projection_squared_radius": str(limit2),
            "possible_x4_count": len(possible),
            "possible_x4_min": min(possible) if possible else None,
            "possible_x4_max": max(possible) if possible else None,
            "possible_x4": possible,
            "reduction_from_303": 303 - len(possible),
        })
        rows.append(row)

    out = {
        "schema": "STAGE32EX5_EFF_AFFINE08_X4_ELLIPSOID_PROJECTION_V1",
        "status": "PASS_EXACT_X4_OUTER_ELLIPSOID_PROJECTION",
        "x4_pairing_label_1based": 49,
        "x4_pairing_index_0based": X4_PAIRING_INDEX,
        "source_x4_domain": [0, eng.NORMAL_MASS],
        "source_x4_count": eng.NORMAL_MASS + 1,
        "bad_shell_outer_condition": f"C2>={eng.LOW}",
        "rows": rows,
        "summary": {
            "max_possible_x4_count": max((r.get("possible_x4_count", 0) for r in rows), default=0),
            "min_possible_x4_count": min((r.get("possible_x4_count", 0) for r in rows if r["hnf_image_integral"]), default=0),
        },
        "interpretation": "Exact continuous projection only: every integral bad-shell witness must use an x4 in the listed interval; no listed x4 is asserted feasible.",
        "credit": {
            "effectivity": False,
            "main": False,
            "receiver": False,
            "theorem": False,
            "endpoint": False,
            "merge": False,
        },
    }
    print("EFF_AFFINE08_X4_PROJECTION=" + json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
