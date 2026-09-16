#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import math
import sys
from pathlib import Path

import sympy
from sympy import Matrix

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
RES = ROOT / "stages" / "stage32" / "residual-32-01-production"
ST33 = ROOT / "stages" / "stage33" / "33-07"
RECOVERABILITY = HERE / "verify_fibration_nef_recoverability.py"

EXPECTED_SUPPORTS = [
    [100],
    [104, 105, 106, 107, 108],
    [109, 110, 111, 112, 113, 114, 115, 116],
    [117, 118, 119, 120, 121, 122, 123, 124],
    [125, 126, 127, 128, 129, 130, 131, 132],
]


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def qstr(v: sympy.Expr) -> str:
    return str(sympy.factor(v))


def matrix_qstr(m: Matrix) -> list[list[str]]:
    return [[qstr(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]


def leading_minors(m: Matrix) -> list[sympy.Expr]:
    return [sympy.factor(m[:k, :k].det()) for k in range(1, m.rows + 1)]


def denominator_lcm(m: Matrix) -> int:
    out = 1
    for v in m:
        out = math.lcm(out, int(sympy.denom(v)))
    return out


def main() -> None:
    vf = load_module(RECOVERABILITY, "stage32_178_fibration_recoverability")
    vf.lock_sources()
    blocks, _ = vf.recover_unordered_fibration_blocks()
    observed = {x for x in vf.ASSIGNMENT_LABELS if x >= 93}
    supports = [sorted(set(block) - observed) for block in blocks[:5]]
    if supports != EXPECTED_SUPPORTS:
        raise ValueError(f"five-residual support regression: {supports}")

    sys.path.insert(0, str(RES))
    from hperp_integral_adapter import _parse_hperp  # noqa: E402

    marking = vf.load_retained(ST33 / "stage32_picard_marking_retained.py", "producer_marking")
    q, degree, linear, _caps, hmeta = _parse_hperp(marking["hperp_text"])
    if q.shape != (63, 63) or linear.shape != (140, 63):
        raise ValueError("Hperp shape regression")

    assignment = list(vf.ASSIGNMENT_LABELS)
    x_rows = linear.extract([lab - 1 for lab in assignment], list(range(63)))
    r_rows = []
    for support in supports:
        row = Matrix([[0] * 63])
        for lab in support:
            row += linear.row(lab - 1)
        r_rows.append(row)
    a = Matrix.vstack(x_rows, *r_rows)

    rank_x = int(x_rows.rank())
    rank_joint = int(a.rank())
    if rank_x != 11 or rank_joint != 16:
        raise ValueError(f"aggregate Hperp rank regression: x={rank_x} joint={rank_joint}")

    qinv = q.inv()
    s = sympy.simplify(a * qinv * a.T)
    if s.shape != (16, 16) or s != s.T:
        raise ValueError("joint constraint Gram regression")
    s_leading = leading_minors(s)
    if not all(v > 0 for v in s_leading):
        raise ValueError("joint constraint Gram is not positive definite")

    sxx = s[:11, :11]
    sxr = s[:11, 11:]
    srx = s[11:, :11]
    srr = s[11:, 11:]
    center = sympy.simplify(srx * sxx.inv())
    schur = sympy.simplify(srr - srx * sxx.inv() * sxr)
    schur_leading = leading_minors(schur)
    if schur.shape != (5, 5) or schur != schur.T or not all(v > 0 for v in schur_leading):
        raise ValueError("five-residual conditional Schur complement is not positive definite")
    schur_inv = sympy.simplify(schur.inv())

    # Verify the exact block-inverse identity underlying the completion formula
    #   joint_norm = old_norm + (z_r-C z_x)^T T^{-1}(z_r-C z_x).
    sxx_inv = sxx.inv()
    expected_inv = Matrix.vstack(
        Matrix.hstack(
            sxx_inv + sxx_inv * sxr * schur_inv * srx * sxx_inv,
            -sxx_inv * sxr * schur_inv,
        ),
        Matrix.hstack(
            -schur_inv * srx * sxx_inv,
            schur_inv,
        ),
    )
    if sympy.simplify(s.inv() - expected_inv) != Matrix.zeros(16, 16):
        raise ValueError("conditional block-inverse identity regression")

    x_degrees = [int(degree[lab - 1, 0]) for lab in assignment]
    r_degrees = [sum(int(degree[lab - 1, 0]) for lab in support) for support in supports]

    den = denominator_lcm(schur_inv)
    schur_inv_integer = sympy.simplify(schur_inv * den)
    if any(sympy.denom(v) != 1 for v in schur_inv_integer):
        raise ValueError("Schur inverse denominator clearing regression")

    out = {
        "schema": "STAGE32_32_01_178_FIVE_RESIDUAL_AGGREGATE_HPERP_PREFLIGHT_V1",
        "purpose": "exact producer kernel for the five minimal residual fibration-block observables; no bounded census is run here",
        "assignment_labels_1based": assignment,
        "residual_observables": [
            {
                "index": i,
                "support_exceptional_labels_1based": support,
                "support_size": len(support),
                "aggregate_known_curve_degree": r_degrees[i],
            }
            for i, support in enumerate(supports)
        ],
        "existing_assignment_rank_in_Hperp": rank_x,
        "joint_11_plus_5_rank_in_Hperp": rank_joint,
        "five_new_forms_independent_mod_existing_Hperp_forms": rank_joint - rank_x == 5,
        "hperp": hmeta,
        "affine_pairing_coordinates": {
            "existing": "z_x = x - d*d_x/16",
            "residual": "z_r = r - d*d_r/16",
            "existing_known_curve_degrees": x_degrees,
            "residual_aggregate_degrees": r_degrees,
        },
        "conditional_completion_identity": "min Hperp norm at fixed (x,r) = z_x^T S_xx^-1 z_x + (z_r-C*z_x)^T T^-1 (z_r-C*z_x)",
        "conditional_center_matrix_C_equals_Srx_Sxx_inverse": matrix_qstr(center),
        "conditional_schur_T": matrix_qstr(schur),
        "conditional_schur_T_leading_principal_minors": [qstr(v) for v in schur_leading],
        "conditional_schur_T_positive_definite": True,
        "conditional_penalty_T_inverse": matrix_qstr(schur_inv),
        "conditional_penalty_integer_scale": den,
        "conditional_penalty_integer_matrix": [
            [int(schur_inv_integer[i, j]) for j in range(5)] for i in range(5)
        ],
        "joint_constraint_gram_determinant": qstr(sympy.factor(s.det())),
        "joint_constraint_gram_positive_definite": True,
        "producer_feasibility": "FIVE_AGGREGATE_LINEAR_FORMS_HAVE_AN_EXACT_5D_POSITIVE_DEFINITE_COMPLETION_KERNEL",
        "bounded_violation_census_run": False,
        "main_credit_changed": False,
        "theorem_credit_changed": False,
        "endpoint_credit_changed": False,
        "td02_additive_credit_claimed": False,
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
