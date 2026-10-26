#!/usr/bin/env python3
"""Exact all140 projection/congruence/orbit-mass sieve before FP57.

For each of the five d18/e8 base4 keys:
  1. project the exact outer bad-shell ellipsoid to every one of 140 pairings;
  2. intersect with the exact one-coordinate lattice congruence induced by
     the saturated 58D kernel and nonnegative block bounds;
  3. enforce the four exact Aut-orbit mass sums by finite DP.

The resulting coordinate domains are necessary conditions only.  Empty
support for any orbit proves bad-shell UNSAT without lattice enumeration.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import sys
from pathlib import Path

from sympy import Matrix

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


def supported_domains(domains: list[list[int]], target: int) -> tuple[bool, list[list[int]]]:
    """Exact per-coordinate support under sum(domains)==target."""
    n = len(domains)
    prefix = [{0}]
    for vals in domains:
        nxt = set()
        for a in prefix[-1]:
            for v in vals:
                s = a + v
                if s <= target:
                    nxt.add(s)
        prefix.append(nxt)
    if target not in prefix[-1]:
        return False, [[] for _ in domains]

    suffix = [set() for _ in range(n + 1)]
    suffix[n] = {0}
    for i in range(n - 1, -1, -1):
        nxt = set()
        for a in suffix[i + 1]:
            for v in domains[i]:
                s = a + v
                if s <= target:
                    nxt.add(s)
        suffix[i] = nxt

    out = []
    for i, vals in enumerate(domains):
        keep = []
        right = suffix[i + 1]
        for v in vals:
            ok = any((target - v - a) in right for a in prefix[i] if target - v - a >= 0)
            if ok:
                keep.append(v)
        out.append(keep)
    return True, out


def main() -> None:
    req(ENGINE.is_file() and blob(ENGINE) == ENGINE_BLOB, "FP58 engine drift")
    eng = load(ENGINE, "stage32ex5_eff_affine11_engine")
    F, A, I, RK, R, _L, _diag, _coeff, _dual, P, gram = eng.build()
    H, E = F.row(0), F.row(1)

    req(sum((P.row(i) for i in range(0, 32)), Matrix.zeros(1, 64)) == 4 * H - 2 * E,
        "orbit0 mass")
    req(sum((P.row(i) for i in range(32, 44)), Matrix.zeros(1, 64)) == 3 * H - E,
        "orbit1 mass")
    req(sum((P.row(i) for i in range(44, 92)), Matrix.zeros(1, 64)) == 12 * H - 2 * E,
        "orbit2 mass")
    req(sum((P.row(i) for i in range(92, 140)), Matrix.zeros(1, 64)) == E,
        "orbit3 mass")

    solve_r = ldl_solver(R)
    V = P * RK
    dual = []
    step = []
    for i in range(140):
        v = V.row(i).T
        q = (v.T * solve_r(v))[0]
        req(q > 0, f"pairing {i} dual norm")
        dual.append(q)
        g = 0
        for a in V.row(i):
            g = math.gcd(g, abs(int(a)))
        req(g > 0, f"pairing {i} kernel gcd")
        step.append(g)

    rows = []
    total_supported = 0
    for base4 in SAMPLE_BASE4:
        target = Matrix([eng.D, eng.E, *base4])
        ic = I.inv() * target
        req(all(getattr(x, "q", 1) == 1 for x in ic), "sample base4 HNF image")
        bp = A * ic
        req(all(getattr(x, "q", 1) == 1 for x in bp), "integral affine base")
        cross = RK.T * gram * bp
        center = solve_r(cross)
        radius = (bp.T * gram * bp)[0] - eng.LOW + (cross.T * center)[0]
        req(radius >= 0, "outer radius")
        center_class = bp + RK * center
        pcenter = P * center_class
        pbase = P * bp

        raw_domains = []
        for i in range(140):
            upper = eng.NORMAL_MASS if i < 92 else eng.E
            g = step[i]
            residue = int(pbase[i, 0]) % g
            lim2 = radius * dual[i]
            vals = [
                k for k in range(upper + 1)
                if k % g == residue and
                   (k - pcenter[i, 0]) * (k - pcenter[i, 0]) <= lim2
            ]
            raw_domains.append(vals)

        orbit_rows = []
        supported = [None] * 140
        key_possible = True
        for lo, hi, mass in ORBITS:
            feasible, refined = supported_domains(raw_domains[lo:hi], mass)
            key_possible = key_possible and feasible
            for j, vals in enumerate(refined, start=lo):
                supported[j] = vals
            orbit_rows.append({
                "first_index": lo,
                "last_index": hi - 1,
                "size": hi - lo,
                "mass": mass,
                "sum_feasible": feasible,
                "raw_domain_total": sum(len(raw_domains[i]) for i in range(lo, hi)),
                "supported_domain_total": sum(len(v) for v in refined),
                "min_supported_domain_size": min((len(v) for v in refined), default=0),
                "max_supported_domain_size": max((len(v) for v in refined), default=0),
            })

        req(all(v is not None for v in supported), "supported domain coverage")
        candidates = []
        for i in range(140):
            candidates.append({
                "index": i,
                "label_1based": i + 1,
                "orbit": next(k for k, (lo, hi, _m) in enumerate(ORBITS) if lo <= i < hi),
                "kernel_gcd": step[i],
                "dual_norm": str(dual[i]),
                "raw_domain": raw_domains[i],
                "supported_domain": supported[i],
                "supported_count": len(supported[i]),
            })
        candidates.sort(key=lambda r: (r["supported_count"], len(r["raw_domain"]), r["index"]))
        total_supported += sum(r["supported_count"] for r in candidates)

        rows.append({
            "base4": list(base4),
            "classification": (
                "BAD_SHELL_UNSAT_EXACT_PROJECTION_MASS_SIEVE"
                if not key_possible else
                "PROJECTION_MASS_SIEVE_FEASIBLE_SUPERSET"
            ),
            "outer_radius": str(radius),
            "all_orbit_sums_feasible": key_possible,
            "orbits": orbit_rows,
            "best_conditioning_coordinates": candidates[:12],
            "zero_supported_coordinate_count": sum(r["supported_count"] == 0 for r in candidates),
            "singleton_supported_coordinate_count": sum(r["supported_count"] == 1 for r in candidates),
        })

    out = {
        "schema": "STAGE32EX5_EFF_AFFINE11_ALL140_PROJECTION_MASS_SIEVE_V1",
        "status": "PASS_EXACT_ALL140_PROJECTION_CONGRUENCE_MASS_SIEVE",
        "bad_shell_outer_condition": f"C2>={eng.LOW}",
        "kernel_dimension": eng.N,
        "orbit_masses": [
            {"range": [lo, hi - 1], "size": hi - lo, "mass": mass}
            for lo, hi, mass in ORBITS
        ],
        "rows": rows,
        "summary": {
            "sample_count": len(rows),
            "keys_closed": sum(not r["all_orbit_sums_feasible"] for r in rows),
            "keys_remaining": sum(r["all_orbit_sums_feasible"] for r in rows),
            "total_supported_coordinate_domain_mass": total_supported,
        },
        "interpretation": {
            "what_is_proved": "Every bad-shell witness must lie in the retained per-coordinate domains and satisfy each exact orbit mass sum.",
            "next_exact_unit": "Choose the smallest supported pairing coordinate(s) from this exact sieve and condition the lattice before any FP run.",
            "what_is_not_proved": "A feasible product of one-coordinate domains need not come from one Picard class; surviving keys remain unresolved.",
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
    print("EFF_AFFINE11_ALL140_SIEVE=" + json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
