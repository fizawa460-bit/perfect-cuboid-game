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
PREFIX = ROOT / "stages/stage32/residual-32-01-production/pairing_prefix_engine.py"
PREFIX_BLOB = "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b"


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
    req(PREFIX.is_file() and blob(PREFIX) == PREFIX_BLOB, "pairing-prefix engine drift")
    eng = load(ENGINE, "stage32ex5_eff_affine07_engine")
    prefix = load(PREFIX, "stage32ex5_eff_affine07_prefix")

    _F, _A, _I, _RK, _R, _L, _diag, _coeff, _dual, P, _gram = eng.build()
    marking = eng.load(eng.MARKING, "stage32ex5_eff_affine07_marking").load()
    bundle = eng.load(eng.RETAINED, "stage32ex5_eff_affine07_bundle").load()
    base = eng.load(eng.BASE, "stage32ex5_eff_affine07_base")
    data = base.reconstruct_translation_data(marking, bundle)
    bridge = data["bridge"]
    H = Matrix(1, 64, bridge.degree_functional)
    E = Matrix(1, 64, bridge.exceptional_mass_functional)

    group = prefix.close_permutation_group(marking["aut_action"]["permutations_1based"])
    unseen = set(range(140))
    orbits = []
    while unseen:
        seed = min(unseen)
        orbit = tuple(sorted({g[seed] for g in group}))
        orbits.append(orbit)
        unseen.difference_update(orbit)

    req(sorted(len(o) for o in orbits) == [12, 32, 48, 48], "Aut orbit partition drift")
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
        "aut_group_order": len(group),
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
