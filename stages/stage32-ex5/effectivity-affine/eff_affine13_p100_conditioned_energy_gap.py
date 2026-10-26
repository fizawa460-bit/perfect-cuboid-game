#!/usr/bin/env python3
"""Exact pairing-100 conditioned 57D energy-gap probe.

AFFINE11 identifies retained pairing label 100 (index 99) as the smallest
one-coordinate exact branch for all five d18/e8 sample base4 keys: the
saturated 58D kernel forces an even congruence and leaves only 4--5 values.

This probe fixes that pairing, constructs the saturated 57D kernel exactly,
and retries the full all140 energy-vs-Hperp gap on only those fibers.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import sys
from pathlib import Path

from flint import fmpz_mat
from sympy import Matrix, Rational

ROOT = Path(__file__).resolve().parents[3]
ENGINE = ROOT / "stages/stage32-ex5/effectivity-affine/eff_affine01_fp58_engine.py"
ENGINE_BLOB = "e7857e9213ca9107edada1424012a7a1c902a625"
COND_INDEX = 99
COND_LABEL = 100

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
    eng = load(ENGINE, "stage32ex5_eff_affine13_engine")
    F6, A6, I6, RK58, R58, _L, _diag, _coeff, _dual, P, gram = eng.build()

    cond_row = P.row(COND_INDEX)
    F7 = F6.col_join(cond_row)
    req(F7.shape == (7, 64) and F7.rank() == 7, "conditioned fixed-map rank")

    hf, tf = fmpz_mat(
        [[int(F7[i, j]) for j in range(64)] for i in range(7)]
    ).transpose().hnf(transform=True)
    T = Matrix([[int(tf[i, j]) for j in range(tf.ncols())] for i in range(tf.nrows())])
    A7 = T.T[:, :7]
    K7 = T.T[:, 7:]
    I7 = F7 * A7
    req(K7.shape == (64, 57) and F7 * K7 == Matrix.zeros(7, 57), "kernel57")
    req(abs(int(tf.det())) == 1, "HNF transform")

    R7 = -(K7.T * gram * K7)
    req(pd(R7), "conditioned Q kernel")
    V7 = P * K7
    E7 = V7.T * V7

    hi = 1
    while not pd(hi * R7 - E7):
        hi *= 2
        req(hi <= (1 << 20), "lambda cap")
    lo = 0
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if pd(mid * R7 - E7):
            hi = mid
        else:
            lo = mid
    lam = hi
    dom = lam * R7 - E7
    solve_dom = ldl_solver(dom)

    # Exact one-coordinate projection/congruence from the original 58D fiber.
    solve58 = ldl_solver(R58)
    vcond = (P * RK58).row(COND_INDEX).T
    dual = (vcond.T * solve58(vcond))[0]
    req(dual > 0, "condition dual")
    gcd_step = 0
    for a in (P * RK58).row(COND_INDEX):
        gcd_step = math.gcd(gcd_step, abs(int(a)))
    req(gcd_step == 2, "AFFINE11 even congruence drift for pairing100")

    q_bad_upper = Rational(eng.D * eng.D, 16) - eng.LOW
    req(q_bad_upper == Rational(161, 4), "bad shell Q upper")

    # Exact Aut-orbit mass lower bounds. Pairing100 is in exceptional orbit.
    fixed_normal_lb = (
        min_square_sum(56, 32)
        + min_square_sum(46, 12)
        + min_square_sum(200, 48)
    )

    inv7 = I7.inv()
    per_key = []
    total_fibers = exact_unsat = inconclusive = 0

    for base4 in SAMPLE_BASE4:
        target6 = Matrix([eng.D, eng.E, *base4])
        ic6 = I6.inv() * target6
        req(all(getattr(x, "q", 1) == 1 for x in ic6), "sample base4 image")
        bp6 = A6 * ic6
        cross58 = RK58.T * gram * bp6
        center58 = solve58(cross58)
        radius58 = (bp6.T * gram * bp6)[0] - eng.LOW + (cross58.T * center58)[0]
        pcenter = (cond_row * (bp6 + RK58 * center58))[0]
        pbase = int((cond_row * bp6)[0])
        residue = pbase % gcd_step
        projected = [
            k for k in range(eng.E + 1)
            if k % gcd_step == residue
            and (k - pcenter) * (k - pcenter) <= radius58 * dual
        ]

        fibers = []
        for value in projected:
            target7 = Matrix([eng.D, eng.E, *base4, value])
            ic7 = inv7 * target7
            if not all(getattr(x, "q", 1) == 1 for x in ic7):
                continue
            bp = A7 * ic7
            req(all(getattr(x, "q", 1) == 1 for x in bp), "integral conditioned base")
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

            remaining_exceptional = eng.E - value
            lower = (
                fixed_normal_lb
                + value * value
                + min_square_sum(remaining_exceptional, 47)
            )
            gap = Rational(lower) - upper
            proved = bool(gap > 0)
            fibers.append({
                "pairing100": value,
                "classification": (
                    "BAD_SHELL_UNSAT_EXACT_P100_ENERGY_GAP"
                    if proved else
                    "P100_ENERGY_GAP_INCONCLUSIVE"
                ),
                "pairing_energy_lower": lower,
                "bad_shell_pairing_energy_upper": str(upper),
                "strict_gap": str(gap),
            })
            total_fibers += 1
            exact_unsat += int(proved)
            inconclusive += int(not proved)

        per_key.append({
            "base4": list(base4),
            "projected_pairing100": projected,
            "projected_count": len(projected),
            "hnf_compatible_count": len(fibers),
            "exact_unsat_count": sum(f["classification"] == "BAD_SHELL_UNSAT_EXACT_P100_ENERGY_GAP" for f in fibers),
            "inconclusive_count": sum(f["classification"] == "P100_ENERGY_GAP_INCONCLUSIVE" for f in fibers),
            "fully_closed": bool(fibers) and all(f["classification"] == "BAD_SHELL_UNSAT_EXACT_P100_ENERGY_GAP" for f in fibers),
            "fibers": fibers,
        })

    out = {
        "schema": "STAGE32EX5_EFF_AFFINE13_P100_CONDITIONED_ENERGY_GAP_V1",
        "status": "PASS_EXACT_P100_CONDITIONED_57D_GAP",
        "conditioned_pairing_index_0based": COND_INDEX,
        "conditioned_pairing_label_1based": COND_LABEL,
        "kernel_congruence_step": gcd_step,
        "kernel_dimension": 57,
        "hnf_image_index": abs(int(I7.det())),
        "lambda_min_integer_pd": lam,
        "bad_shell_Q_upper": str(q_bad_upper),
        "per_key": per_key,
        "summary": {
            "hnf_compatible_p100_fibers": total_fibers,
            "exact_bad_shell_unsat_fibers": exact_unsat,
            "inconclusive_fibers": inconclusive,
            "fully_closed_base4_keys": sum(r["fully_closed"] for r in per_key),
        },
        "interpretation": {
            "what_is_proved": "Every surviving bad-shell witness is confined to the listed pairing100-conditioned saturated 57D fibers; positive gaps close individual fibers exactly.",
            "next_exact_unit": "Run exact FP57 only on the remaining inconclusive pairing100 fibers; this is strictly smaller branching than the x4-conditioned surface.",
            "what_is_not_proved": "Inconclusive fibers are not feasible certificates and no downstream credit is promoted.",
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
    print("EFF_AFFINE13_P100_GAP=" + json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
