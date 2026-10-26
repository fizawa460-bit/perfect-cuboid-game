#!/usr/bin/env python3
"""Exact Aut-orbit mass identities and discrete energy lower bound."""
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


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, "module spec " + name)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def min_square_sum(total: int, count: int) -> int:
    req(total >= 0 and count > 0, "mass/count")
    q, r = divmod(total, count)
    return (count - r) * q * q + r * (q + 1) * (q + 1)


def main() -> None:
    req(ENGINE.is_file() and blob(ENGINE) == ENGINE_BLOB, "FP58 engine drift")
    eng = load(ENGINE, "stage32ex5_eff_affine07_engine")

    F, _A, _I, _RK, _R, _L, _diag, _coeff, _dual, P, _gram = eng.build()
    H = F.row(0)
    E = F.row(1)
    marking = eng.load(eng.MARKING, "stage32ex5_eff_affine07_marking").load()
    gens = [tuple(int(v) - 1 for v in p) for p in marking["aut_action"]["permutations_1based"]]
    req(gens and all(len(g) == 140 and sorted(g) == list(range(140)) for g in gens),
        "Aut generators")

    def point_orbit(seed: int) -> tuple[int, ...]:
        seen = {seed}
        queue = [seed]
        while queue:
            cur = queue.pop()
            for gen in gens:
                nxt = gen[cur]
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append(nxt)
        return tuple(sorted(seen))

    orbits = [point_orbit(seed) for seed in (0, 32, 44, 92)]
    expected = [tuple(range(0, 32)), tuple(range(32, 44)), tuple(range(44, 92)), tuple(range(92, 140))]
    req(orbits == expected, "Aut point-orbit partition drift")
    span = Matrix.hstack(H.T, E.T)
    rows = []
    total_lb = 0
    all_fixed = True

    for orbit in orbits:
        s = sum((P.row(i) for i in orbit), Matrix.zeros(1, 64))
        try:
            sol, params = span.gauss_jordan_solve(s.T)
            fixed = params.rows == 0
        except ValueError:
            fixed = False
            sol = None
        row = {
            "first_index": min(orbit),
            "size": len(orbit),
            "population": (
                "normal" if max(orbit) < 92
                else "exceptional" if min(orbit) >= 92
                else "mixed"
            ),
            "sum_in_span_H_E": fixed,
        }
        if fixed:
            alpha, beta = sol[0, 0], sol[1, 0]
            mass = alpha * eng.D + beta * eng.E
            row.update({
                "sum_identity": f"({alpha})*d+({beta})*e",
                "mass_at_d18_e8": str(mass),
            })
            if getattr(mass, "q", 1) == 1 and int(mass) >= 0:
                lb = min_square_sum(int(mass), len(orbit))
                row["integer_nonnegative_square_energy_lower_bound"] = lb
                total_lb += lb
            else:
                row["integer_nonnegative_square_energy_lower_bound"] = None
                all_fixed = False
        else:
            row["sum_identity"] = None
            row["mass_at_d18_e8"] = None
            row["integer_nonnegative_square_energy_lower_bound"] = None
            all_fixed = False
        rows.append(row)

    coarse_lb = min_square_sum(eng.NORMAL_MASS, 92) + min_square_sum(eng.E, 48)
    out = {
        "schema": "STAGE32EX5_EFF_AFFINE07_ORBIT_MASS_ENERGY_V1",
        "status": "PASS_EXACT_AUT_ORBIT_MASS_TEST",
        "aut_generator_count": len(gens),
        "orbits": rows,
        "all_orbit_masses_fixed_by_d_e": all_fixed,
        "coarse_block_energy_lower_bound": coarse_lb,
        "orbit_split_energy_lower_bound": total_lb if all_fixed else None,
        "improvement": (total_lb - coarse_lb) if all_fixed else None,
        "interpretation": (
            "ORBIT_SPLIT_MASS_STRENGTHENING_AVAILABLE"
            if all_fixed and total_lb > coarse_lb
            else "NO_STRICT_ORBIT_SPLIT_ENERGY_STRENGTHENING"
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
    print("EFF_AFFINE07_ORBIT_MASS=" + json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
