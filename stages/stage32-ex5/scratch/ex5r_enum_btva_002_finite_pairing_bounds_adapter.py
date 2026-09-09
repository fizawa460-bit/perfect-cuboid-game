#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import sympy
from sympy import Matrix

BACKEND = Path(__file__).resolve().parents[2] / "stage32" / "residual-32-01-production"
if str(BACKEND) not in sys.path:
    sys.path.insert(0, str(BACKEND))

from direct_picard_slice_bridge import DirectPicardSliceBridge
from hperp_integral_adapter import HperpIntegralPairingAdapter
from pairing_prefix_engine import INDLIST

ROUTE_ID = "EX5R-ENUM-BTVA-002"
ROW_ID = "g0-d008"
GENUS = 0
DEGREE = 8
LOWER = -DEGREE - 2 + 2 * GENUS
EXPECTED_FACTOR_G0_D008 = 224


def load_retained(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import retained payload: {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    value = mod.load()
    if not isinstance(value, dict):
        raise ValueError(f"retained payload did not return dict: {path}")
    return value


def exact_fraction(value: object) -> Fraction:
    q = sympy.Rational(value)
    return Fraction(int(q.p), int(q.q))


def exact_positive_definite(a: Matrix) -> dict:
    """Exact rational LDL^T positivity certificate, with no floating point."""
    if a.rows != a.cols or a != a.T:
        raise ValueError("matrix must be symmetric square")
    n = a.rows
    aa = [[exact_fraction(a[i, j]) for j in range(n)] for i in range(n)]
    ell = [[Fraction(0, 1) for _ in range(n)] for _ in range(n)]
    diag: list[Fraction] = []
    for i in range(n):
        ell[i][i] = Fraction(1, 1)
        pivot = aa[i][i] - sum(ell[i][k] * ell[i][k] * diag[k] for k in range(i))
        if pivot <= 0:
            raise ValueError(f"negative metric is not positive definite at LDL pivot {i}")
        diag.append(pivot)
        for j in range(i + 1, n):
            num = aa[j][i] - sum(ell[j][k] * ell[i][k] * diag[k] for k in range(i))
            ell[j][i] = num / pivot
    return {
        "dimension": n,
        "all_pivots_positive": True,
        "pivot_numerators": [v.numerator for v in diag],
        "pivot_denominators": [v.denominator for v in diag],
    }


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def derive_bounds(marking: dict, bundle: dict, d: int = DEGREE, g: int = GENUS) -> dict:
    if (d, g) != (DEGREE, GENUS):
        raise ValueError("this source is intentionally scoped to g0-d008")
    lower = -d - 2 + 2 * g
    factor = d * d - 16 * lower
    if lower != -10 or factor != EXPECTED_FACTOR_G0_D008:
        raise ValueError("g0-d008 lower/factor regression")

    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    bridge = DirectPicardSliceBridge.from_retained(marking, bundle)
    gram = Matrix(bundle["picard_gram_64x64"])
    h = Matrix(list(bridge.hyperplane_coordinates))
    if int((h.T * gram * h)[0]) != 16:
        raise ValueError("hyperplane square regression")
    degree_fn = h.T * gram
    if [int(v) for v in degree_fn] != list(bridge.degree_functional):
        raise ValueError("degree functional regression")

    # Rational h-perp has rank 63. Prove its negative Gram positive definite
    # exactly before applying Cauchy; this imports no unverified signature claim.
    null = degree_fn.nullspace()
    if len(null) != 63:
        raise ValueError(f"h-perp rank regression: {len(null)}")
    basis = Matrix.hstack(*null)
    minus_hperp_gram = -(basis.T * gram * basis)
    pd = exact_positive_definite(minus_hperp_gram)

    coords = adapter.class_coordinates_in_retained_basis
    selected = [j - 1 for j in INDLIST]
    if len(selected) != 64 or len(set(selected)) != 64:
        raise ValueError("selected64 regression")

    bounds = []
    for slot, known_index in enumerate(selected):
        c = coords[known_index, :].T
        delta = int((h.T * gram * c)[0])
        q = int((c.T * gram * c)[0])
        orthogonal_norm_numerator = delta * delta - 16 * q
        if orthogonal_norm_numerator <= 0:
            raise ValueError(f"nonpositive orthogonal norm at selected slot {slot}")
        radicand = factor * orthogonal_norm_numerator
        radius_floor = math.isqrt(radicand)
        lo = ceil_div(d * delta - radius_floor, 16)
        hi = (d * delta + radius_floor) // 16
        if lo > hi:
            raise ValueError(f"empty Cauchy interval at selected slot {slot}")
        bounds.append({
            "selected_slot_0based": slot,
            "known_curve_label_1based": known_index + 1,
            "curve_degree": delta,
            "curve_self_intersection": q,
            "orthogonal_norm_numerator": orthogonal_norm_numerator,
            "radicand": radicand,
            "radius_floor": radius_floor,
            "pairing_min": lo,
            "pairing_max": hi,
            "integer_width": hi - lo + 1,
        })

    return {
        "schema": "STAGE32EX5_EX5R_ENUM_BTVA_002_G0_D008_FINITE_PAIRING_BOUNDS_RUNTIME_V1",
        "route_id": ROUTE_ID,
        "row_id": ROW_ID,
        "target": {
            "g": g,
            "d": d,
            "lower_self_intersection": lower,
            "factor_d2_minus_16lower": factor,
        },
        "proof": {
            "hyperplane_square": 16,
            "hperp_rank": 63,
            "negative_hperp_gram_exact_positive_definite": True,
            "ldl": pd,
            "inequality": "(16*p-d*delta)^2 <= (d^2-16*lower)*(delta^2-16*q)",
            "scope": "every Picard64 class x with h.x=d and x^2>=lower",
            "floating_point_used": False,
        },
        "selected64_pairing_bounds": bounds,
        "summary": {
            "coordinate_count": len(bounds),
            "maximum_integer_width": max(rec["integer_width"] for rec in bounds),
            "finite_cartesian_box_certified": True,
            "cartesian_box_enumerated": False,
        },
        "credit": {
            "receiver_credit": False,
            "route_credit": False,
            "stage32_main_credit": False,
            "Q602_credit": False,
            "O210_credit": False,
        },
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    bundle = load_retained(args.retained, "s32_ex5_btva_picard")
    marking = load_retained(args.marking, "s32_ex5_btva_marking")
    result = derive_bounds(marking, bundle)
    text = json.dumps(result, sort_keys=True, separators=(",", ":"))
    if args.output is None:
        print(text)
    else:
        args.output.write_text(text + "\n")


if __name__ == "__main__":
    main()
