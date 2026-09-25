#!/usr/bin/env python3
"""Exact x4-conditioned energy-vs-Hperp gap over saturated 57D fibers."""
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

from flint import fmpz_mat
from sympy import Matrix, Rational

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


def pd(A: Matrix) -> bool:
    if A != A.T:
        return False
    try:
        L, D = A.LDLdecomposition(hermitian=False)
    except Exception:
        return False
    return A == L * D * L.T and all(D[i, i] > 0 for i in range(D.rows))


def ldl_solver(A: Matrix):
    L, D = A.LDLdecomposition(hermitian=False)
    req(A == L * D * L.T and all(D[i, i] > 0 for i in range(D.rows)), "LDL")

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


def min_square_sum(total: int, count: int) -> int:
    req(total >= 0 and count > 0, "mass/count")
    q, r = divmod(total, count)
    return (count - r) * q * q + r * (q + 1) * (q + 1)


def main() -> None:
    req(ENGINE.is_file() and blob(ENGINE) == ENGINE_BLOB, "FP58 engine drift")
    eng = load(ENGINE, "stage32ex5_eff_affine10_engine")
    F6, A6, I6, RK58, R58, _L, _diag, _coeff, _dual, P, gram = eng.build()
    H, E = F6.row(0), F6.row(1)

    # Lock the exact four Aut-orbit mass identities discovered by AFFINE07.
    req(sum((P.row(i) for i in range(0, 32)), Matrix.zeros(1, 64)) == 4 * H - 2 * E,
        "orbit0 mass identity")
    req(sum((P.row(i) for i in range(32, 44)), Matrix.zeros(1, 64)) == 3 * H - E,
        "orbit1 mass identity")
    req(sum((P.row(i) for i in range(44, 92)), Matrix.zeros(1, 64)) == 12 * H - 2 * E,
        "orbit2 mass identity")
    req(sum((P.row(i) for i in range(92, 140)), Matrix.zeros(1, 64)) == E,
        "orbit3 mass identity")

    x4row = P.row(X4_INDEX)
    F7 = F6.col_join(x4row)
    req(F7.rank() == 7, "fixed rank7")
    hf, tf = fmpz_mat(
        [[int(F7[i, j]) for j in range(64)] for i in range(7)]
    ).transpose().hnf(transform=True)
    T = Matrix([[int(tf[i, j]) for j in range(tf.ncols())] for i in range(tf.nrows())])
    A7 = T.T[:, :7]
    K7 = T.T[:, 7:]
    I7 = F7 * A7
    req(K7.shape == (64, 57) and F7 * K7 == Matrix.zeros(7, 57), "kernel57")

    R7 = -(K7.T * gram * K7)
    req(pd(R7), "Q kernel57 positive definite")
    V7 = P * K7
    energy7 = V7.T * V7
    req(pd(energy7), "pairing energy kernel57 positive definite")

    hi = 1
    while not pd(hi * R7 - energy7):
        hi *= 2
        req(hi <= (1 << 20), "lambda cap")
    lo = 0
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if pd(mid * R7 - energy7):
            hi = mid
        else:
            lo = mid
    lam = hi
    dom = lam * R7 - energy7
    solve_dom = ldl_solver(dom)

    # Outer x4 projection from the original 58D fiber.
    solve58 = ldl_solver(R58)
    x4kernel58 = (P * RK58).row(X4_INDEX).T
    x4dual = (x4kernel58.T * solve58(x4kernel58))[0]

    q_bad_upper = Rational(eng.D * eng.D, 16) - eng.LOW
    req(q_bad_upper == Rational(161, 4), "bad shell Q upper")

    fixed_other_orbit_lb = (
        min_square_sum(56, 32)
        + min_square_sum(46, 12)
        + min_square_sum(8, 48)
    )

    rows = []
    total_fibers = exact_unsat = inconclusive = 0
    per_key = []
    inv7 = I7.inv()

    for base4 in SAMPLE_BASE4:
        target6 = Matrix([eng.D, eng.E, *base4])
        ic6 = I6.inv() * target6
        req(all(getattr(x, "q", 1) == 1 for x in ic6), "sample base4 image")
        bp6 = A6 * ic6
        cross58 = RK58.T * gram * bp6
        center58 = solve58(cross58)
        radius58 = (bp6.T * gram * bp6)[0] - eng.LOW + (cross58.T * center58)[0]
        x4center = (x4row * (bp6 + RK58 * center58))[0]
        limit2 = radius58 * x4dual
        projected = [
            k for k in range(eng.NORMAL_MASS + 1)
            if (k - x4center) * (k - x4center) <= limit2
        ]

        key_rows = []
        for x4 in projected:
            target7 = Matrix([eng.D, eng.E, *base4, x4])
            ic7 = inv7 * target7
            if not all(getattr(x, "q", 1) == 1 for x in ic7):
                continue
            bp = A7 * ic7
            req(all(getattr(x, "q", 1) == 1 for x in bp), "integral x4 affine base")
            p0 = P * bp
            q0 = (bp.T * gram * bp)[0]
            cross = K7.T * gram * bp
            s = K7.T * P.T * p0
            e0 = (p0.T * p0)[0]

            b = -lam * cross - s
            c = lam * (Rational(eng.D * eng.D, 16) - q0) - e0
            y = solve_dom(b)
            min_gap = c - (b.T * y)[0]
            mu = -min_gap
            upper = lam * q_bad_upper + mu

            # Orbit 44..91 has mass 200 and contains x4 at index 48.
            lower = (
                fixed_other_orbit_lb
                + x4 * x4
                + min_square_sum(200 - x4, 47)
            )
            gap = Rational(lower) - upper
            proved = bool(gap > 0)
            cls = "BAD_SHELL_UNSAT_EXACT_X4_ENERGY_GAP" if proved else "X4_ENERGY_GAP_INCONCLUSIVE"
            key_rows.append({
                "x4": x4,
                "classification": cls,
                "pairing_energy_lower": lower,
                "pairing_energy_upper_on_bad_shell": str(upper),
                "strict_gap": str(gap),
            })
            total_fibers += 1
            exact_unsat += int(proved)
            inconclusive += int(not proved)

        key_closed = bool(key_rows) and all(r["classification"] == "BAD_SHELL_UNSAT_EXACT_X4_ENERGY_GAP" for r in key_rows)
        per_key.append({
            "base4": list(base4),
            "projected_x4_count": len(projected),
            "hnf_compatible_x4_count": len(key_rows),
            "exact_unsat_x4_count": sum(r["classification"] == "BAD_SHELL_UNSAT_EXACT_X4_ENERGY_GAP" for r in key_rows),
            "inconclusive_x4_count": sum(r["classification"] == "X4_ENERGY_GAP_INCONCLUSIVE" for r in key_rows),
            "all_hnf_compatible_x4_closed": key_closed,
            "fibers": key_rows,
        })

    out = {
        "schema": "STAGE32EX5_EFF_AFFINE10_X4_ENERGY_GAP_V1",
        "status": "PASS_EXACT_X4_CONDITIONED_ENERGY_GAP",
        "kernel_dimension": 57,
        "lambda_min_integer_pd": lam,
        "orbit_mass_identities_replayed": True,
        "bad_shell_Q_upper": str(q_bad_upper),
        "per_key": per_key,
        "summary": {
            "hnf_compatible_x4_fibers": total_fibers,
            "exact_bad_shell_unsat_x4_fibers": exact_unsat,
            "inconclusive_x4_fibers": inconclusive,
            "fully_closed_base4_keys": sum(r["all_hnf_compatible_x4_closed"] for r in per_key),
        },
        "interpretation": {
            "what_is_proved": "Any x4 fiber classified UNSAT has no all140-nonnegative integral bad-shell class under the exact fixed observables.",
            "next_exact_unit": "Run FP57 only on inconclusive x4 fibers; do not enumerate fibers already closed by this gap certificate.",
            "what_is_not_proved": "Inconclusive fibers are not asserted feasible; no MAIN/effectivity credit is promoted here.",
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
    print("EFF_AFFINE10_X4_ENERGY_GAP=" + json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
