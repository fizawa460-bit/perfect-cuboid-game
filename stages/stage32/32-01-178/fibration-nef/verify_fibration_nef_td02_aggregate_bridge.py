#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import sympy
from sympy import Matrix, Rational

HERE = Path(__file__).resolve().parent
RECOVERABILITY = HERE / "verify_fibration_nef_recoverability.py"
BNB = HERE / "verify_fibration_nef_branch_and_bound_preflight.py"
LOCKS = {
    "recoverability": (RECOVERABILITY, "fbd8dad2194378a6bf77d12cc2c65ac03782f112"),
    "branch_and_bound_preflight": (BNB, "5c93d54ff8244e86d5d1cb8b7d9eb322bea5a4f3"),
}


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def matrix_qstr(m: Matrix) -> list[list[str]]:
    return [[str(sympy.factor(m[i, j])) for j in range(m.cols)] for i in range(m.rows)]


def vector_qstr(v: Matrix) -> list[str]:
    return [str(sympy.factor(v[i, 0])) for i in range(v.rows)]


def main() -> None:
    for name, (path, expected) in LOCKS.items():
        req(path.is_file(), f"missing source lock {name}")
        req(git_blob(path) == expected, f"source drift {name}")

    vf = load_module(RECOVERABILITY, "stage32_178_fibration_recoverability_bridge")
    bnb = load_module(BNB, "stage32_178_fibration_bnb_bridge")
    vf.lock_sources()
    bnb.lock_extra_sources()
    kernel = bnb.build_kernel(vf)

    # Existing TD02 aggregate coordinates in exact assignment order
    #   x=(x0,...,x10) = labels (95,99,103,102,49,97,94,101,93,98,96).
    # The bounded TD02 producer already retains
    #   a=x2+x3+x7,
    #   b=x1+x5+x9,
    #   c=x0+x6+x8+x10,
    #   t=x0+x1+x6+x9,
    #   x4.
    L = Matrix([
        [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],  # a
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],  # b
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],  # c
        [1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0],  # t
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # x4
    ])
    req(int(L.rank()) == 5, "TD02 aggregate map lost rank")

    # Exact row-space test: if C factors through L, then the five-dimensional
    # conditional Hperp center needs only (a,b,c,t,x4), not all eleven x_i.
    gram = L * L.T
    req(gram.det() != 0, "TD02 aggregate Gram singular")
    factor = sympy.simplify(kernel.center * L.T * gram.inv())
    req(sympy.simplify(kernel.center - factor * L) == Matrix.zeros(5, 11),
        "conditional center does not factor through TD02 aggregates")

    pos = {lab: i for i, lab in enumerate(bnb.ASSIGNMENT)}
    observed = set(kernel.observed_exceptionals)
    known_rows = []
    for block in kernel.blocks:
        row = [0] * 11
        for lab in block:
            if lab in observed:
                row[pos[lab]] += 1
        known_rows.append(row)
    known = Matrix(known_rows)
    # Six recovered base-locus blocks have known masses
    #   (b+c, a, 0, 0, 0, 0).
    expected_known = Matrix.vstack(L.row(1) + L.row(2), L.row(0), *[Matrix([[0] * 11]) for _ in range(4)])
    req(known == expected_known, "fibration known block masses do not reduce to (b+c,a,0,0,0,0)")

    # M10 is the total already-observed exceptional mass.
    m10_row = Matrix([[1 if i != 4 else 0 for i in range(11)]])
    req(m10_row == L.row(0) + L.row(1) + L.row(2), "M10 != a+b+c")

    # z_x=x-d*d_x/16 and d_x is zero except d_x4=4.  Therefore
    #   mu = C z_x + d*d_r/16
    #      = F(a,b,c,t,x4) + d*(d_r/16-F[:,x4]/4).
    d_shift = Matrix([
        Rational(kernel.r_degrees[i], 16) - Rational(factor[i, 4], 4)
        for i in range(5)
    ])

    out = {
        "schema": "STAGE32_32_01_178_FIBRATION_NEF_TD02_AGGREGATE_BRIDGE_V1",
        "purpose": "prove exact sufficiency of existing TD02 aggregate coordinates for the fibration-nef conditional kernel; no FULL178 census is run here",
        "td02_aggregate_order": ["a", "b", "c", "t", "x4"],
        "td02_aggregate_definitions": {
            "a": "x2+x3+x7",
            "b": "x1+x5+x9",
            "c": "x0+x6+x8+x10",
            "t": "x0+x1+x6+x9",
            "x4": "x4",
        },
        "known_fibration_block_masses": ["b+c", "a", "0", "0", "0", "0"],
        "audited_total_observed_exceptional_mass_M10": "a+b+c",
        "remaining_hidden_exceptional_mass": "e-a-b-c",
        "conditional_center_factors_through_td02_aggregates": True,
        "conditional_center_factor_F": matrix_qstr(factor),
        "conditional_center_formula": "mu = F*(a,b,c,t,x4)^T + d*d_shift",
        "conditional_center_d_shift": vector_qstr(d_shift),
        "old_GRF04_budget_state": ["q", "t", "x4", "d", "g"],
        "combined_exact_state_sufficient_for_fibration_kernel": ["a", "b", "c", "q", "t", "x4", "e", "d", "g"],
        "eleven_coordinate_reinflation_required": False,
        "individual_48node_semantic_bijection_required": False,
        "next_exact_step": "compose the residual five-block integer penalty minimum with the TD02 aggregate/full178 scaleout state",
        "full178_fibration_census_run": False,
        "main_credit_changed": False,
        "theorem_credit_changed": False,
        "endpoint_credit_changed": False,
        "merge": False,
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
