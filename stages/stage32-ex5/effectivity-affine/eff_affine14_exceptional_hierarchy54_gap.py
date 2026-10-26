#!/usr/bin/env python3
"""Exact 54D exceptional-hierarchy energy-gap probe.

The base4/e/d fiber fixes 6 independent observables (kernel 58D).  The
historical Stage32 exact backend was practical on a 54D kernel.  Here we add
four bounded exceptional-block observables:

  A    = sum pairings[92:104]
  AB   = sum pairings[92:116]
  C    = sum pairings[116:128]
  p100 = pairing[99]  (label 100)

Since total exceptional mass is e=8, every added observable lies in 0..8.
We first project the outer adjunction ellipsoid exactly to these four
coordinates, enumerate only compatible integer tuples, apply the saturated
10-row HNF image test, and retry the exact all140 pairing-energy domination
on each resulting 54D fiber.

No effectivity or MAIN credit is granted by this research probe.
"""
from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
import math
import sys
from pathlib import Path

from flint import fmpz_mat
from sympy import Matrix, Rational

ROOT = Path(__file__).resolve().parents[3]
ENGINE = ROOT / "stages/stage32-ex5/effectivity-affine/eff_affine01_fp58_engine.py"
ENGINE_BLOB = "e7857e9213ca9107edada1424012a7a1c902a625"

SAMPLE_BASE4 = (
    (0, 1, 1, 1),
    (0, 4, 4, 8),
    (0, 6, 2, 6),
    (1, 2, 2, 2),
    (1, 3, 3, 3),
)
P100_INDEX = 99
NORMAL_ORBIT_ENERGY_LOWER = 104 + 178 + 840


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
        req(b.rows == A.rows, "solve row count")
        cols = []
        for col in range(b.cols):
            y = [0] * A.rows
            for i in range(A.rows):
                v = b[i, col]
                for j in range(i):
                    v -= L[i, j] * y[j]
                y[i] = v / L[i, i]
            z = [y[i] / D[i, i] for i in range(A.rows)]
            x = [0] * A.rows
            for i in range(A.rows - 1, -1, -1):
                v = z[i]
                for j in range(i + 1, A.rows):
                    v -= L[j, i] * x[j]
                x[i] = v / L[i, i]
            cols.append(Matrix(x))
        out = Matrix.hstack(*cols)
        req(A * out == b, "LDL solve replay")
        return out

    return solve


def min_square_sum(total: int, count: int) -> int:
    req(total >= 0 and count > 0, "mass/count")
    q, r = divmod(total, count)
    return (count - r) * q * q + r * (q + 1) * (q + 1)


def allowed_projection(row: Matrix, bp: Matrix, RK: Matrix, R: Matrix, solve_r,
                       P: Matrix, gram: Matrix, low: int, upper: int) -> list[int]:
    coeff = row * RK
    g = 0
    for v in coeff:
        g = math.gcd(g, abs(int(v)))
    req(g > 0, "projection gcd")
    q0 = (bp.T * gram * bp)[0]
    cross = RK.T * gram * bp
    center = solve_r(cross)
    radius = q0 - low + (cross.T * center)[0]
    req(radius >= 0, "outer radius")
    center_class = bp + RK * center
    c = (row * center_class)[0]
    v = coeff.T
    dual = (v.T * solve_r(v))[0]
    req(dual > 0, "projection dual")
    residue = int((row * bp)[0]) % g
    return [
        k for k in range(upper + 1)
        if k % g == residue and (k - c) * (k - c) <= radius * dual
    ]


def main() -> None:
    req(ENGINE.is_file() and blob(ENGINE) == ENGINE_BLOB, "FP58 engine drift")
    eng = load(ENGINE, "stage32ex5_eff_affine14_engine")
    F6, A6, I6, RK58, R58, _L58, _d58, _c58, _u58, P, gram = eng.build()
    req(R58.rows == 58 and pd(R58), "58D outer kernel")

    Arow = sum((P.row(i) for i in range(92, 104)), Matrix.zeros(1, 64))
    ABrow = sum((P.row(i) for i in range(92, 116)), Matrix.zeros(1, 64))
    Crow = sum((P.row(i) for i in range(116, 128)), Matrix.zeros(1, 64))
    P100row = P.row(P100_INDEX)
    extra_rows = [Arow, ABrow, Crow, P100row]

    F10 = Matrix.vstack(F6, *extra_rows)
    req(F10.shape == (10, 64), "fixed10 shape")
    req(F10.rank() == 10, "fixed10 rank")

    hf, tf = fmpz_mat(
        [[int(F10[i, j]) for j in range(64)] for i in range(10)]
    ).transpose().hnf(transform=True)
    T = Matrix([[int(tf[i, j]) for j in range(tf.ncols())] for i in range(tf.nrows())])
    req(abs(int(tf.det())) == 1, "fixed10 HNF transform")
    A10 = T.T[:, :10]
    K54 = T.T[:, 10:]
    I10 = F10 * A10
    req(K54.shape == (64, 54) and F10 * K54 == Matrix.zeros(10, 54), "kernel54")
    req(abs(int(I10.det())) > 0, "fixed10 image basis")

    R54 = -(K54.T * gram * K54)
    req(pd(R54), "54D negative intersection form")
    V54 = P * K54
    E54 = V54.T * V54

    lam_hi = 1
    while not pd(lam_hi * R54 - E54):
        lam_hi *= 2
        req(lam_hi <= (1 << 20), "lambda cap")
    lam_lo = 0
    while lam_lo + 1 < lam_hi:
        mid = (lam_lo + lam_hi) // 2
        if pd(mid * R54 - E54):
            lam_hi = mid
        else:
            lam_lo = mid
    lam = lam_hi
    dom = lam * R54 - E54
    solve_dom = ldl_solver(dom)

    # Precompute the affine quadratic gap on target10 coordinates.  This turns
    # every candidate-fiber gap evaluation into one exact 10D quadratic form.
    invI10 = I10.inv()
    B = A10 * invI10
    J = Matrix.zeros(10, 10)
    J[0, 0] = Rational(1, 16)
    PB = P * B
    cross_map = K54.T * gram * B
    energy_cross_map = K54.T * P.T * PB
    M = -lam * cross_map - energy_cross_map
    C = lam * (J - B.T * gram * B) - PB.T * PB
    gap_form = C - M.T * solve_dom(M)
    req(gap_form == gap_form.T, "target gap form symmetry")

    solve58 = ldl_solver(R58)
    invI6 = I6.inv()
    q_bad_upper = Rational(eng.D * eng.D, 16) - eng.LOW
    req(q_bad_upper == Rational(161, 4), "bad shell Q upper")

    rows = []
    total_projected = total_hnf = total_closed = total_open = 0

    for base4 in SAMPLE_BASE4:
        target6 = Matrix([eng.D, eng.E, *base4])
        ic6 = invI6 * target6
        req(all(getattr(x, "q", 1) == 1 for x in ic6), "sample base4 HNF image")
        bp6 = A6 * ic6
        req(all(getattr(x, "q", 1) == 1 for x in bp6), "integral base6")

        domains = [
            allowed_projection(r, bp6, RK58, R58, solve58, P, gram, eng.LOW, eng.E)
            for r in extra_rows
        ]
        projected = []
        for a, ab, c, p100 in itertools.product(*domains):
            # Four 12-element exceptional quarters have masses
            # A=a, B=ab-a, C=c, D=e-ab-c.  p100 lies in quarter A.
            if not (0 <= a <= ab <= eng.E):
                continue
            if not (0 <= c <= eng.E - ab):
                continue
            if not (0 <= p100 <= a):
                continue
            projected.append((a, ab, c, p100))

        compatible = []
        for a, ab, c, p100 in projected:
            target10 = Matrix([eng.D, eng.E, *base4, a, ab, c, p100])
            icoord = invI10 * target10
            if not all(getattr(x, "q", 1) == 1 for x in icoord):
                continue

            min_gap = (target10.T * gap_form * target10)[0]
            upper = lam * q_bad_upper - min_gap
            bmass = ab - a
            dmass = eng.E - ab - c
            lower = (
                NORMAL_ORBIT_ENERGY_LOWER
                + p100 * p100
                + min_square_sum(a - p100, 11)
                + min_square_sum(bmass, 12)
                + min_square_sum(c, 12)
                + min_square_sum(dmass, 12)
            )
            gap = Rational(lower) - upper
            compatible.append({
                "A": a,
                "AB": ab,
                "C": c,
                "p100": p100,
                "B": bmass,
                "D": dmass,
                "pairing_energy_lower": lower,
                "bad_shell_pairing_energy_upper": str(upper),
                "strict_gap": str(gap),
                "bad_shell_unsat": bool(gap > 0),
            })

        compatible.sort(key=lambda x: Rational(x["strict_gap"]), reverse=True)
        closed = sum(x["bad_shell_unsat"] for x in compatible)
        open_count = len(compatible) - closed
        fully_closed = open_count == 0
        total_projected += len(projected)
        total_hnf += len(compatible)
        total_closed += closed
        total_open += open_count

        rows.append({
            "base4": list(base4),
            "projection_domains": {
                "A_sum_92_103": domains[0],
                "AB_sum_92_115": domains[1],
                "C_sum_116_127": domains[2],
                "p100_index99": domains[3],
            },
            "projected_tuple_count_after_mass_order": len(projected),
            "hnf_compatible_54d_fiber_count": len(compatible),
            "exact_energy_gap_unsat_fiber_count": closed,
            "inconclusive_54d_fiber_count": open_count,
            "fully_closed": fully_closed,
            "best_inconclusive_fibers": [x for x in compatible if not x["bad_shell_unsat"]][:16],
        })

    out = {
        "schema": "STAGE32EX5_EFF_AFFINE14_EXCEPTIONAL_HIERARCHY54_GAP_V1",
        "status": "PASS_EXACT_EXCEPTIONAL_HIERARCHY54_GAP",
        "fixed_observables": [
            "d", "e", "a", "b", "c", "t",
            "E92_103", "E92_115", "E116_127", "pairing100",
        ],
        "fixed_map_rank": 10,
        "kernel_dimension": 54,
        "hnf_image_index": abs(int(I10.det())),
        "lambda_min_integer_pd": lam,
        "bad_shell_Q_upper": str(q_bad_upper),
        "rows": rows,
        "summary": {
            "sample_count": len(rows),
            "projected_tuple_count": total_projected,
            "hnf_compatible_54d_fiber_count": total_hnf,
            "exact_energy_gap_unsat_fiber_count": total_closed,
            "inconclusive_54d_fiber_count": total_open,
            "fully_closed_base4_keys": sum(r["fully_closed"] for r in rows),
        },
        "interpretation": {
            "what_is_proved": (
                "Every bad-shell witness under a sample base4 key must occur in one of the "
                "listed HNF-compatible 54D exceptional-hierarchy fibers; positive energy "
                "gaps close individual fibers exactly."
            ),
            "next_exact_unit": (
                "If any fibers remain, benchmark exact historical-style FP140 recursion "
                "only on the best remaining 54D fiber before authorizing any scaleout."
            ),
            "what_is_not_proved": (
                "Inconclusive 54D fibers are not feasibility certificates; no effectivity "
                "or downstream credit is promoted."
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
    print("EFF_AFFINE14_HIERARCHY54_GAP=" + json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
