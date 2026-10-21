#!/usr/bin/env python3
"""Exact orbit-subset energy-vs-Hperp gap search.

Search all 15 nonempty subsets of the four exact Aut-orbits.  For each subset
we certify a dyadic lambda with

    E_subset <= lambda * Q + mu(base4)

on the fixed 58D affine fiber, then compare the bad-shell upper bound with the
exact discrete lower bound forced by the fixed orbit masses.

This is a cheap exact obstruction search; it grants no downstream credit.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

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
ORBITS = (
    (0, 32, 56),
    (32, 44, 46),
    (44, 92, 200),
    (92, 140, 8),
)
DYADIC_STEPS = 10


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
    q, r = divmod(total, count)
    return (count - r) * q * q + r * (q + 1) * (q + 1)


def lambda_upper(R: Matrix, Eform: Matrix) -> Rational:
    hi = Rational(1)
    while not pd(hi * R - Eform):
        hi *= 2
        req(hi <= (1 << 20), "lambda search cap")
    lo = hi / 2
    if pd(lo * R - Eform):
        while lo > 0 and pd(lo * R - Eform):
            hi = lo
            lo /= 2
    for _ in range(DYADIC_STEPS):
        mid = (lo + hi) / 2
        if pd(mid * R - Eform):
            hi = mid
        else:
            lo = mid
    req(pd(hi * R - Eform), "final lambda domination")
    return hi


def main() -> None:
    req(ENGINE.is_file() and blob(ENGINE) == ENGINE_BLOB, "FP58 engine drift")
    eng = load(ENGINE, "stage32ex5_eff_affine12_engine")
    _F, A, I, RK, R, _L, _diag, _coeff, _dual, P, gram = eng.build()
    req(pd(R), "Q kernel")

    q_bad_upper = Rational(eng.D * eng.D, 16) - eng.LOW
    req(q_bad_upper == Rational(161, 4), "bad shell Q upper")

    orbit_rows = [P[lo:hi, :] for lo, hi, _m in ORBITS]
    orbit_forms = [(O * RK).T * (O * RK) for O in orbit_rows]
    orbit_lbs = [min_square_sum(m, hi - lo) for lo, hi, m in ORBITS]

    subset_specs = []
    for mask in range(1, 1 << len(ORBITS)):
        chosen = [i for i in range(len(ORBITS)) if mask & (1 << i)]
        Psub = Matrix.vstack(*[orbit_rows[i] for i in chosen])
        Eform = sum((orbit_forms[i] for i in chosen), Matrix.zeros(eng.N, eng.N))
        lam = lambda_upper(R, Eform)
        dom = lam * R - Eform
        solve_dom = ldl_solver(dom)
        lower = sum(orbit_lbs[i] for i in chosen)
        subset_specs.append((mask, chosen, Psub, lam, solve_dom, lower))

    per_key = []
    for base4 in SAMPLE_BASE4:
        target = Matrix([eng.D, eng.E, *base4])
        ic = I.inv() * target
        req(all(getattr(x, "q", 1) == 1 for x in ic), "sample base4 image")
        bp = A * ic
        req(all(getattr(x, "q", 1) == 1 for x in bp), "integral affine base")
        q0 = (bp.T * gram * bp)[0]
        cross = RK.T * gram * bp

        trials = []
        for mask, chosen, Psub, lam, solve_dom, lower in subset_specs:
            p0 = Psub * bp
            V = Psub * RK
            s = V.T * p0
            e0 = (p0.T * p0)[0]
            b = -lam * cross - s
            c = lam * (Rational(eng.D * eng.D, 16) - q0) - e0
            y = solve_dom(b)
            min_gap = c - (b.T * y)[0]
            mu = -min_gap
            upper = lam * q_bad_upper + mu
            gap = Rational(lower) - upper
            trials.append({
                "mask": mask,
                "orbits": chosen,
                "lambda": str(lam),
                "energy_lower": lower,
                "bad_shell_energy_upper": str(upper),
                "strict_gap": str(gap),
                "bad_shell_unsat": bool(gap > 0),
            })

        trials.sort(key=lambda r: Rational(r["strict_gap"]), reverse=True)
        best = trials[0]
        per_key.append({
            "base4": list(base4),
            "closed": bool(best["bad_shell_unsat"]),
            "best": best,
            "positive_gap_subset_count": sum(t["bad_shell_unsat"] for t in trials),
            "all_subsets": trials,
        })

    out = {
        "schema": "STAGE32EX5_EFF_AFFINE12_ORBIT_SUBSET_ENERGY_GAP_V1",
        "status": "PASS_EXACT_ORBIT_SUBSET_ENERGY_GAP_SEARCH",
        "dyadic_refinement_steps": DYADIC_STEPS,
        "orbit_specs": [
            {
                "index": i,
                "range": [lo, hi - 1],
                "size": hi - lo,
                "mass": mass,
                "minimum_integer_square_energy": orbit_lbs[i],
            }
            for i, (lo, hi, mass) in enumerate(ORBITS)
        ],
        "bad_shell_Q_upper": str(q_bad_upper),
        "per_key": per_key,
        "summary": {
            "sample_count": len(per_key),
            "closed_key_count": sum(r["closed"] for r in per_key),
            "remaining_key_count": sum(not r["closed"] for r in per_key),
        },
        "interpretation": {
            "what_is_proved": "Any positive subset gap is an exact bad-shell UNSAT certificate using only fixed orbit masses and exact quadratic domination.",
            "next_exact_unit": "If no subset closes a key, use the best subset only as a heuristic and continue with projection-forced equalities or FP on the reduced fiber.",
            "what_is_not_proved": "Nonpositive gaps do not imply feasibility.",
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
    print("EFF_AFFINE12_ORBIT_SUBSET_GAP=" + json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
