#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
import sys
from pathlib import Path

import sympy
from sympy import Matrix

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
N260_STATE = HERE.parent / "N260/STATE.json"
RETAINED = ROOT / "stages/stage33/33-07/picard_base_rows_retained.py"
MARKING = ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py"
sys.path.insert(0, str(RESIDUAL))

from hperp_integral_adapter import HperpIntegralPairingAdapter

EXPECTED_BUNDLE_CANONICAL = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
EXPECTED_MARKING_CANONICAL = "e06291dddfc529fca2c0b0fe58dd43151faccd3d7997d9aa5797e1978227bb7c"
EXCEPTIONAL_LABELS = list(range(93, 141))
NORMAL_LABELS = list(range(1, 93))
X4_LABEL = 49
TARGET_STRATA = [("g0-d176",176,48,3104), ("g1-d192",192,48,3408)]
PICARD_RANK = 64


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_retained(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import retained payload: {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    payload = mod.load()
    if not isinstance(payload, dict):
        raise ValueError(f"retained payload is not dict: {path}")
    return payload


def qp(q: sympy.Rational) -> list[int]:
    q = sympy.Rational(q)
    return [int(sympy.numer(q)), int(sympy.denom(q))]


def solve_two(qj: tuple[sympy.Rational, ...], qk: tuple[sympy.Rational, ...], target: tuple[sympy.Rational, ...]):
    n = len(target)
    for p in range(n):
        for q in range(p + 1, n):
            det = qj[p] * qk[q] - qj[q] * qk[p]
            if det == 0:
                continue
            rhs_p = -target[p]
            rhs_q = -target[q]
            a = (rhs_p * qk[q] - rhs_q * qk[p]) / det
            b = (qj[p] * rhs_q - qj[q] * rhs_p) / det
            if all(target[t] + a * qj[t] + b * qk[t] == 0 for t in range(n)):
                return sympy.Rational(a), sympy.Rational(b)
            return None
    return None


def main() -> None:
    n260 = json.loads(N260_STATE.read_text())
    if n260.get("node_id") != "N260" or n260["proof"].get("full_exceptional_vector") != "[1]^48":
        raise ValueError("N260 [1]^48 authority regression")
    bundle = load_retained(RETAINED, "s32_n320_bundle")
    marking = load_retained(MARKING, "s32_n320_marking")
    if bundle.get("canonical_sha256") != EXPECTED_BUNDLE_CANONICAL:
        raise ValueError("retained bundle canonical regression")
    if marking.get("canonical_sha256") != EXPECTED_MARKING_CANONICAL:
        raise ValueError("retained marking canonical regression")
    P = HperpIntegralPairingAdapter.from_retained(marking, bundle).pairing_matrix
    if P.shape != (140, PICARD_RANK):
        raise ValueError("pairing matrix shape regression")

    normal_sum = Matrix.zeros(1, PICARD_RANK)
    for label in NORMAL_LABELS:
        normal_sum += P.row(label - 1)
    base = Matrix.vstack(*([P.row(label - 1) for label in EXCEPTIONAL_LABELS] + [normal_sum]))
    if base.rank() != 49:
        raise ValueError("base rank regression")
    null = base.nullspace()
    if len(null) != 15:
        raise ValueError(f"base quotient dimension regression: {len(null)}")
    N = Matrix.hstack(*null)
    qsig = {label: tuple(sympy.Rational(v) for v in (P.row(label - 1) * N)) for label in NORMAL_LABELS}
    q49 = qsig[X4_LABEL]

    _, pivots = base.rref()
    square = base[:, list(pivots)]
    square_inv = square.inv()

    candidates = []
    others = [label for label in NORMAL_LABELS if label != X4_LABEL]
    for j, k in itertools.combinations(others, 2):
        solved = solve_two(qsig[j], qsig[k], q49)
        if solved is None:
            continue
        a, b = solved
        if a <= 0 or b <= 0:
            continue
        target_row = P.row(X4_LABEL - 1) + a * P.row(j - 1) + b * P.row(k - 1)
        coeff = target_row[:, list(pivots)] * square_inv
        if coeff * base != target_row:
            raise ValueError("quotient-zero relation failed rowspace replay")
        exc_const = sum(sympy.Rational(coeff[0, t]) for t in range(48))
        mass_coeff = sympy.Rational(coeff[0, 48])
        strata = []
        max_cap = -1
        for row_id, degree, e, normal_mass in TARGET_STRATA:
            fixed = sympy.factor(exc_const + mass_coeff * normal_mass)
            cap = int(sympy.floor(fixed)) if fixed >= 0 else -1
            strata.append({
                "row_id": row_id,
                "fixed_weighted_sum": qp(fixed),
                "necessary_x4_cap": cap,
            })
            max_cap = max(max_cap, cap)
        candidates.append({
            "partner_labels_1based": [j, k],
            "partner_weights": [qp(a), qp(b)],
            "exceptional_allones_constant": qp(exc_const),
            "normal_mass_coefficient": qp(mass_coeff),
            "strata": strata,
            "max_cap_across_two_survivor_strata": max_cap,
        })

    candidates.sort(key=lambda r: (int(r["max_cap_across_two_survivor_strata"]), r["partner_labels_1based"]))
    body = {
        "schema": "STAGE32_32_01_178_N320_SPARSE_POSITIVE_X4_RELATIONS_V1",
        "source_scope": "N260 full-exceptional rigidity; focus on N280-surviving d176/d192 strata",
        "quotient": {
            "base_rank": 49,
            "quotient_dimension": 15,
            "base_functionals": "48 exceptional rows + normal_total",
        },
        "search": {
            "form": "x4 + a*y_j + b*y_k = fixed(base), a>0,b>0",
            "candidate_partner_pairs": len(list(itertools.combinations(others, 2))),
            "positive_exact_relations_found": len(candidates),
            "nonnegativity_implication": "x4 <= fixed weighted sum",
        },
        "best_relation": candidates[0] if candidates else None,
        "relations": candidates[:50],
        "semantics": {
            "exact_rational_quotient_search": True,
            "all_partner_weights_strictly_positive": True,
            "rejection_zero_loss_relative_to_n260_and_normal_mass_authority": True,
            "does_not_run_z3": True,
            "does_not_duplicate_ex5_adaptive_exceptional_partition": True,
            "n260_hostile_audit_required_before_credit_consumption": True,
            "full178_complete": False,
            "heavy_compute": False,
            "theorem_credit": False,
        },
    }
    print(json.dumps({**body, "canonical_sha256_without_this_field": csha(body)}, sort_keys=True))


if __name__ == "__main__":
    main()
