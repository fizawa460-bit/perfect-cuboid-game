#!/usr/bin/env python3
"""Exact restricted pairing-square frame test on the 58D fixed fiber."""
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


def upper(m: Matrix) -> Matrix:
    return Matrix([m[i, j] for i in range(m.rows) for j in range(i, m.cols)])


def main() -> None:
    req(ENGINE.is_file() and blob(ENGINE) == ENGINE_BLOB, "FP58 engine drift")
    eng = load(ENGINE, "stage32ex5_eff_affine06_engine")
    _F, _A, _I, RK, R, _L, _diag, _coeff, _dual, P, _gram = eng.build()

    V = P * RK
    forms = [V.row(i).T * V.row(i) for i in range(V.rows)]
    A = Matrix.hstack(*[upper(f) for f in forms])
    b = upper(R)

    Af = fmpz_mat([[int(A[i, j]) for j in range(A.cols)] for i in range(A.rows)])
    Augf = fmpz_mat([
        [int(A[i, j]) for j in range(A.cols)] + [int(b[i, 0])]
        for i in range(A.rows)
    ])
    rank_a = int(Af.rank())
    aug_rank = int(Augf.rank())
    in_span = rank_a == aug_rank

    coeff = None
    free_dimension = None
    if in_span:
        sol, params = A.gauss_jordan_solve(b)
        free_dimension = int(params.rows)
        # Canonical specialization: set all free parameters to zero.
        if params.rows:
            syms = sorted(
                set().union(*(x.free_symbols for x in sol)),
                key=lambda x: str(x),
            )
            sol = sol.subs({s: 0 for s in syms})
        coeff = [str(sol[i, 0]) for i in range(sol.rows)]
        replay = sum((sol[i, 0] * forms[i] for i in range(len(forms))), Matrix.zeros(eng.N, eng.N))
        req(replay == R, "restricted frame replay")

    out = {
        "schema": "STAGE32EX5_EFF_AFFINE06_RESTRICTED_PAIRING_FRAME_V1",
        "status": "PASS_RESTRICTED_FRAME_TEST",
        "kernel_dimension": eng.N,
        "pairing_count": V.rows,
        "symmetric_coordinate_count": eng.N * (eng.N + 1) // 2,
        "pairing_square_span_rank": rank_a,
        "augmented_rank_with_Q": aug_rank,
        "Q_in_restricted_pairing_square_span": in_span,
        "solution_free_dimension": free_dimension,
        "canonical_coefficients": coeff,
        "interpretation": (
            "EXACT_PAIRING_SQUARE_RECONSTRUCTION_AVAILABLE__NEXT_OPTIMIZE_DISCRETE_MASS_POLYTOPE"
            if in_span
            else
            "NO_RESTRICTED_PAIRING_SQUARE_IDENTITY__FP_OR_STRONGER_INEQUALITY_STILL_REQUIRED"
        ),
        "credit": {
            "effectivity": False,
            "main": False,
            "receiver": False,
            "theorem": False,
            "endpoint": False,
            "merge": False,
        },
    }
    print("EFF_AFFINE06_RESTRICTED_FRAME=" + json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
