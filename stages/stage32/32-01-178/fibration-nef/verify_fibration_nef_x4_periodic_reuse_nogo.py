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


def qstr(v) -> str:
    return str(sympy.factor(v))


def main() -> None:
    req(BNB.is_file(), "missing branch-and-bound carrier")
    req(git_blob(BNB) == BNB_BLOB, "branch-and-bound carrier drift")
    bnb = load_module(BNB, "stage32_178_x4_nogo_bnb")
    bnb.lock_extra_sources()
    vf = bnb.load_module(bnb.RECOVERABILITY, "stage32_178_x4_nogo_recoverability")
    vf.lock_sources()
    kernel = bnb.build_kernel(vf)
    bridge = bnb.td02_aggregate_bridge(kernel)

    req(tuple(bridge["aggregate_order"]) == ("a", "b", "c", "t", "x4"),
        "TD02 aggregate order regression")
    req(bridge["exact_factorization_C_equals_F_L"] is True,
        "TD02 center factorization lost exactness")
    F = Matrix([[Rational(v) for v in row] for row in bridge["F"]])
    req(F.shape == (5, 5), "conditional-center factor shape regression")
    x4_column = F[:, 4]
    req(x4_column != Matrix.zeros(5, 1),
        "x4 unexpectedly disappeared from conditional center")

    # Strongest cheap reuse hypothesis: a nonzero period P reuses the exact
    # same residual vector r.  Then delta=r-mu would have to be invariant.
    P = sympy.symbols("P", integer=True, nonzero=True)
    same_r_center_shift = sympy.simplify(P * x4_column)
    req(same_r_center_shift != Matrix.zeros(5, 1),
        "nonzero x4 period unexpectedly preserves conditional center")

    # Even if one attempts to compensate by translating residual vectors by
    # the same center shift, every residual coordinate lives in a finite box
    # 0<=r_i<=cap_i.  A finite integer interval is invariant under translation
    # only by zero; hence a fixed nonzero residual translation cannot give a
    # global bijection of feasible residual boxes.  Since x4_column is nonzero,
    # center-preserving global translation reuse is impossible.
    finite_box_translation_requires_zero = True
    req(finite_box_translation_requires_zero and x4_column != Matrix.zeros(5, 1),
        "finite-box no-go precondition regression")

    # The GRF04 part of the qexc threshold is independently nonperiodic in x4:
    # rho_static=(d/2-2*x4-t)^2/12.  For any nonzero P, the shifted difference
    # has nonzero derivative with respect to x4, so no constant residue period
    # can preserve it across a slice interval.
    x4, d, t = sympy.symbols("x4 d t")
    rho = (Rational(1, 12) * (d / 2 - 2 * x4 - t) ** 2)
    rho_shift = sympy.expand(rho.subs(x4, x4 + P) - rho)
    rho_shift_dx4 = sympy.factor(sympy.diff(rho_shift, x4))
    req(sympy.simplify(rho_shift_dx4 - Rational(2, 3) * P) == 0,
        "GRF04 x4 shift derivative regression")
    req(rho_shift_dx4 != 0,
        "nonzero x4 period unexpectedly preserves GRF04 static rho")

    out = {
        "schema": "STAGE32_32_01_178_X4_PERIODIC_REUSE_NOGO_V1",
        "purpose": "rule out unconditional global x4 residue-period reuse for the selective Picard workunit route before production scaleout",
        "exact_facts": {
            "caps_depend_on_x4": False,
            "sum_window_depends_on_x4": False,
            "conditional_center_formula": "mu = F*(a,b,c,t,x4)^T + d*d_shift",
            "conditional_center_x4_column": [qstr(x4_column[i, 0]) for i in range(5)],
            "conditional_center_x4_column_nonzero": True,
            "same_residual_vector_reuse_for_nonzero_period": False,
            "center_preserving_fixed_residual_translation_global_box_bijection": False,
            "finite_residual_box_translation_invariant_only_for_zero_shift": True,
            "grf04_static_rho": "(d/2-2*x4-t)^2/12",
            "grf04_shift_difference": qstr(rho_shift),
            "grf04_shift_difference_derivative_in_x4": qstr(rho_shift_dx4),
            "grf04_nonzero_period_preserves_static_rho": False,
        },
        "conclusion": {
            "global_exact_x4_periodic_reuse_authorized": False,
            "x4_slices_must_remain_distinct_in_workunit_identity": True,
            "allowed_shared_work": "x4-independent static support/min-q and selective A/H q-polynomials may still be cached across slices",
            "stronger_key-specific_reuse": "not ruled out, but requires a separate exact proof and may not be assumed by production",
        },
        "production_heavy_run_armed": False,
        "main_credit_changed": False,
        "theorem_credit_changed": False,
        "endpoint_credit_changed": False,
        "merge": False,
    }
    print("X4_PERIODIC_REUSE_NOGO_SUMMARY=" + json.dumps({
        "x4_center_column": out["exact_facts"]["conditional_center_x4_column"],
        "global_periodic_reuse": False,
        "x4_distinct_workunits": True,
    }, sort_keys=True))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
