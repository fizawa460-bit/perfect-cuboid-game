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
BNB = HERE / "verify_fibration_nef_branch_and_bound_preflight.py"
BNB_BLOB = "6d4c79db4246b8b54cdc45bc6423f00d622740e6"
ASSIGNMENT = (95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96)
SIGNATURE_ORDER = ("a", "b", "c", "t", "x4", "qexc", "e", "d", "g")


def req(value: bool, message: str) -> None:
    if not value:
        raise SystemExit("FAIL: " + message)


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


def aggregate(x: tuple[int, ...]) -> tuple[int, int, int, int, int, int]:
    a = x[2] + x[3] + x[7]
    b = x[1] + x[5] + x[9]
    c = x[0] + x[6] + x[8] + x[10]
    t = x[0] + x[1] + x[6] + x[9]
    x4 = x[4]
    qexc = sum(x[i] * x[i] for i in range(11) if i != 4)
    return a, b, c, t, x4, qexc


def signature_problem(bnb, kernel, *, g: int, d: int, e: int, sig: tuple[int, ...]) -> dict:
    a, b, c, t, x4, qexc = (int(v) for v in sig)
    m10 = a + b + c
    remaining = e - m10
    if remaining < 0:
        return {"structurally_infeasible": True, "reason": "e_minus_M10_negative"}

    known = (b + c, a, 0, 0, 0, 0)
    caps = []
    for i in range(5):
        if d - known[i] < 0:
            return {"structurally_infeasible": True, "reason": f"nef_block_{i}_already_negative"}
        caps.append(min(remaining, d - known[i]))
    if d - known[5] < 0:
        return {"structurally_infeasible": True, "reason": "nef_block_5_already_negative"}
    sum_lo = max(0, remaining - (d - known[5]))
    sum_hi = remaining
    if sum(caps) < sum_lo:
        return {"structurally_infeasible": True, "reason": "nef_simplex_empty"}

    old_rho = Rational(qexc, 2) + Rational(1, 12) * (Rational(d, 2) - 2 * x4 - t) ** 2
    genus_budget = Rational(d * d, 16) + d + 2 - 2 * g
    penalty_budget = sympy.factor(genus_budget - old_rho)
    if penalty_budget < 0:
        return {"structurally_infeasible": True, "reason": "already_rejected_by_GRF04"}

    bridge = bnb.td02_aggregate_bridge(kernel)
    F = Matrix([[Rational(v) for v in row] for row in bridge["F"]])
    d_shift = Matrix([Rational(v) for v in bridge["d_shift"]])
    mu = F * Matrix([a, b, c, t, x4]) + d * d_shift
    return {
        "structurally_infeasible": False,
        "m10": m10,
        "remaining": remaining,
        "known_block_masses": known,
        "caps": tuple(caps),
        "sum_lo": sum_lo,
        "sum_hi": sum_hi,
        "old_rho": old_rho,
        "genus_budget": genus_budget,
        "penalty_budget": penalty_budget,
        "mu": mu,
    }


def same_problem(lhs: dict, rhs: dict) -> bool:
    if lhs.keys() != rhs.keys():
        return False
    for key in lhs:
        a, b = lhs[key], rhs[key]
        if isinstance(a, Matrix) or isinstance(b, Matrix):
            if Matrix(a) != Matrix(b):
                return False
        elif sympy.simplify(a - b) != 0 if isinstance(a, sympy.Basic) and isinstance(b, sympy.Basic) else a != b:
            return False
    return True


def main() -> None:
    req(BNB.is_file(), "missing branch-and-bound carrier")
    req(git_blob(BNB) == BNB_BLOB, "branch-and-bound carrier drift")
    bnb = load_module(BNB, "stage32_178_signature_bnb")
    bnb.lock_extra_sources()
    vf = bnb.load_module(bnb.RECOVERABILITY, "stage32_178_signature_recoverability")
    vf.lock_sources()
    kernel = bnb.build_kernel(vf)

    pos = {lab: i for i, lab in enumerate(ASSIGNMENT)}
    xs = sympy.symbols("x0:11")
    known_forms = []
    for block in kernel.blocks:
        known_forms.append(sympy.expand(sum(xs[pos[lab]] for lab in block if lab in pos and lab >= 93)))
    a = xs[2] + xs[3] + xs[7]
    b = xs[1] + xs[5] + xs[9]
    c = xs[0] + xs[6] + xs[8] + xs[10]
    t = xs[0] + xs[1] + xs[6] + xs[9]
    req(len(known_forms) == 6, "fibration block count regression")
    req(sympy.expand(known_forms[0] - (b + c)) == 0, "block0 mass != b+c")
    req(sympy.expand(known_forms[1] - a) == 0, "block1 mass != a")
    req(all(sympy.expand(v) == 0 for v in known_forms[2:]), "later blocks unexpectedly contain assigned exceptionals")
    m10 = sum(xs[i] for i, lab in enumerate(ASSIGNMENT) if lab >= 93)
    req(sympy.expand(m10 - (a + b + c)) == 0, "M10 != a+b+c")

    bridge = bnb.td02_aggregate_bridge(kernel)
    req(bridge["exact_factorization_C_equals_F_L"] is True, "center no longer factors through TD02 aggregates")
    req(tuple(bridge["aggregate_order"]) == ("a", "b", "c", "t", "x4"), "aggregate order regression")

    # Bounded exact regression: compare the legacy eleven-coordinate consumer
    # against the compact-signature reconstruction on legal terminal fixtures.
    checked = 0
    for d in range(4, 13, 2):
        for e in range(0, d + 1, 2):
            for x0 in range(0, min(e, 3) + 1):
                for x1 in range(x0, min(e - x0, 4) + 1):
                    x = (x0, x1, 0, 0, min(2, max(0, 19 * d - 5 * e)), 0, 0, 0, 0, 0, 0)
                    if sum(x[i] for i in range(11) if i != 4) > e:
                        continue
                    sig = aggregate(x)
                    for g in (0, 1):
                        direct = bnb.residual_problem(kernel, g=g, d=d, e=e, x=x)
                        compact = signature_problem(bnb, kernel, g=g, d=d, e=e, sig=sig)
                        req(same_problem(direct, compact), f"signature reconstruction mismatch d={d} e={e} g={g} x={x}")
                        checked += 1

    out = {
        "schema": "STAGE32_32_01_178_FIBRATION_NEF_SIGNATURE_FACTORIZATION_V1",
        "purpose": "prove that the retained fibration-nef residual consumer can be evaluated from a compact weighted terminal signature instead of the full eleven-coordinate assignment",
        "signature_order": list(SIGNATURE_ORDER),
        "exact_symbolic_factorization": {
            "M10": "a+b+c",
            "known_fibration_block_masses": ["b+c", "a", "0", "0", "0", "0"],
            "conditional_center": "F*(a,b,c,t,x4)^T + d*d_shift",
            "GRF04_rho": "qexc/2 + (d/2-2*x4-t)^2/12",
            "nef_caps_and_simplex_depend_only_on": ["a", "b", "c", "e", "d"],
            "picard_static_observables_depend_only_on": ["a", "b", "c", "t", "x4", "e", "d"],
            "full_eleven_coordinate_reinflation_required_by_residual_consumers": False,
        },
        "bounded_exact_regression_cases": checked,
        "bounded_regression_all_match": True,
        "next_exact_step": "construct an exact weighted counter for production terminals by (a,b,c,t,x4,qexc), then run the baseline/Picard residual oracle once per realized signature and charge its exact multiplicity",
        "full178_census_claimed": False,
        "main_credit_changed": False,
        "theorem_credit_changed": False,
        "endpoint_credit_changed": False,
        "merge": False,
    }
    print("SIGNATURE_FACTORIZATION_SUMMARY=" + json.dumps({
        "signature": list(SIGNATURE_ORDER),
        "regression_cases": checked,
        "symbolic": True,
    }, sort_keys=True))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
