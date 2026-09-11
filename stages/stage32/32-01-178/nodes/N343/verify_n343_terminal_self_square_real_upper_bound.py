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
ROOT = HERE.parents[4]
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
RETAINED = ROOT / "stages/stage33/33-07/picard_base_rows_retained.py"
MARKING = ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py"
N342_RESULT = HERE.parent / "N342/RESULT.json"
sys.path.insert(0, str(RESIDUAL))

from direct_picard_slice_bridge import DirectPicardSliceBridge
from hperp_integral_adapter import HperpIntegralPairingAdapter

EXPECTED_BUNDLE_CANONICAL = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
EXPECTED_MARKING_CANONICAL = "e06291dddfc529fca2c0b0fe58dd43151faccd3d7997d9aa5797e1978227bb7c"
EXPECTED_N342_CHECKPOINT_CANONICAL = "0a556575c4ad365d5f0816a60c380de16ca609310961e58f6e63834082a61c88"
EXPECTED_N342_RESULT_CANONICAL = "2e1cd942950aabb8d5e5888a5804f937316e5bbbf157dc3053eb0023d43c8124"
EXCEPTIONAL_LABELS = list(range(93, 141))
X4_LABEL = 49
TARGETS = [
    ("g0-d176", 0, 176, [3,7,11,15,19,23,27,31,35,39]),
    ("g1-d192", 1, 192, [3,7,11,15,19,23,27,31,35,39,43]),
]


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


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


def qstr(q) -> str:
    q = Rational(q)
    return str(int(q.p)) if q.q == 1 else f"{int(q.p)}/{int(q.q)}"


def main() -> None:
    n342 = json.loads(N342_RESULT.read_text())
    body342 = dict(n342)
    claimed342 = body342.pop("canonical_sha256_without_this_field")
    if claimed342 != EXPECTED_N342_CHECKPOINT_CANONICAL or csha(body342) != claimed342:
        raise ValueError("N342 retained checkpoint canonical drift")
    if n342["source_locks"].get("n342_result_canonical_sha256") != EXPECTED_N342_RESULT_CANONICAL:
        raise ValueError("N342 workflow-result source lock drift")
    if n342["aggregate"].get("sat_terminal_count") != 21:
        raise ValueError("N342 residual terminal count drift")
    if n342["sat_x4"].get("g0-d176") != TARGETS[0][3] or n342["sat_x4"].get("g1-d192") != TARGETS[1][3]:
        raise ValueError("N342 residual x4 set drift")

    bundle = load_retained(RETAINED, "s32_n343_bundle")
    marking = load_retained(MARKING, "s32_n343_marking")
    if bundle.get("canonical_sha256") != EXPECTED_BUNDLE_CANONICAL:
        raise ValueError("retained Picard bundle canonical drift")
    if marking.get("canonical_sha256") != EXPECTED_MARKING_CANONICAL:
        raise ValueError("retained Stage32 marking canonical drift")

    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    bridge = DirectPicardSliceBridge.from_retained(marking, bundle)
    P = adapter.pairing_matrix
    G = Matrix(bundle["picard_gram_64x64"])
    if P.shape != (140, 64) or G.shape != (64, 64) or G != G.T:
        raise ValueError("Picard matrix shape/symmetry drift")

    degree_row = Matrix([list(bridge.degree_functional)])
    exceptional_rows = P.extract([label - 1 for label in EXCEPTIONAL_LABELS], list(range(64)))
    x4_row = P.extract([X4_LABEL - 1], list(range(64)))
    A = degree_row.col_join(exceptional_rows).col_join(x4_row)
    if A.shape != (50, 64):
        raise ValueError(f"constraint matrix shape drift: {A.shape}")
    rank = int(A.rank())
    if rank != 50:
        raise ValueError(f"degree+48 exceptional+x4 constraint rank drift: {rank}")

    _, pivot_columns = A.rref()
    pivot_columns = list(pivot_columns)
    if len(pivot_columns) != rank:
        raise ValueError("pivot-column count drift")
    square = A.extract(list(range(50)), pivot_columns)
    if square.det() == 0:
        raise ValueError("pivot square unexpectedly singular")
    square_inv = square.inv()

    null = A.nullspace()
    if len(null) != 14:
        raise ValueError(f"affine real kernel dimension drift: {len(null)}")
    K = Matrix.hstack(*null)
    if A * K != Matrix.zeros(50, 14):
        raise ValueError("affine kernel replay failed")

    Q = K.T * G * K
    if Q != Q.T:
        raise ValueError("restricted Gram is not symmetric")

    # Exact Sylvester criterion: Q is negative definite iff (-1)^k times
    # every leading principal determinant is positive.
    signed_leading = []
    for k in range(1, Q.rows + 1):
        det = sympy.factor(Q[:k, :k].det(method="domain-ge"))
        signed = ((-1) ** k) * det
        if not bool(signed > 0):
            raise ValueError(f"restricted degree-zero Gram not negative definite at k={k}: {det}")
        signed_leading.append(qstr(signed))

    qinv = Q.inv()
    rows = []
    pruned = 0
    for row_id, genus, degree, x4s in TARGETS:
        required_lower = -degree - 2 + 2 * genus
        for x4 in x4s:
            target = Matrix([degree] + [1] * 48 + [x4])
            x0 = Matrix.zeros(64, 1)
            pivot_solution = square_inv * target
            for i, column in enumerate(pivot_columns):
                x0[column, 0] = pivot_solution[i, 0]
            if A * x0 != target:
                raise ValueError(f"particular solution replay failed: {row_id}/x4={x4}")

            linear = K.T * G * x0
            stationary_t = -qinv * linear
            stationary_x = x0 + K * stationary_t
            if A * stationary_x != target:
                raise ValueError("stationary affine constraint replay failed")
            max_square = sympy.factor((stationary_x.T * G * stationary_x)[0])
            formula_square = sympy.factor((x0.T * G * x0)[0] - (linear.T * qinv * linear)[0])
            if max_square != formula_square:
                raise ValueError("quadratic maximum formula replay failed")

            below = bool(max_square < required_lower)
            if below:
                pruned += 1
            rows.append({
                "row_id": row_id,
                "g": genus,
                "d": degree,
                "x4": x4,
                "required_self_square_lower": required_lower,
                "real_affine_max_self_square": qstr(max_square),
                "real_affine_max_below_required": below,
                "stationary_point_integral": all(sympy.denom(v) == 1 for v in stationary_x),
            })

    body = {
        "schema": "STAGE32_32_01_178_N343_TERMINAL_SELF_SQUARE_REAL_UPPER_BOUND_V1",
        "source_scope": "N342 residual 21 terminals only",
        "source_locks": {
            "n342_checkpoint_canonical_sha256": EXPECTED_N342_CHECKPOINT_CANONICAL,
            "n342_result_canonical_sha256": EXPECTED_N342_RESULT_CANONICAL,
            "retained_bundle_canonical_sha256": EXPECTED_BUNDLE_CANONICAL,
            "retained_marking_canonical_sha256": EXPECTED_MARKING_CANONICAL,
        },
        "constraint_model": {
            "picard_rank": 64,
            "equalities": "degree + all48 exceptional pairings=1 + x4",
            "equality_rank": rank,
            "real_affine_kernel_dimension": K.cols,
            "normal_nonnegativity_omitted_for_safe_upper_bound": True,
            "integrality_omitted_for_safe_upper_bound": True,
            "restricted_gram_negative_definite_exact": True,
            "sylvester_signed_leading_principal_minors": signed_leading,
            "optimization": "exact unconstrained concave quadratic maximum on equality affine space",
        },
        "aggregate": {
            "terminal_count": len(rows),
            "real_upper_bound_pruned_count": pruned,
            "real_upper_bound_survivor_count": len(rows) - pruned,
            "all_21_pruned_by_real_upper_bound": pruned == len(rows),
        },
        "rows": rows,
        "semantics": {
            "if_real_affine_max_below_required_then_no_integral_picard64_completion_can_meet_self_square_lower": True,
            "real_affine_survival_does_not_imply_integral_or_effective_curve_existence": True,
            "does_not_change_n350_producer_registry": True,
            "n350_external_hostile_audit_still_required_before_registration": True,
            "n260_n280_n310_n341_n342_audit_boundaries_preserved": True,
            "full178_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "merge_authorized": False,
        },
    }
    print(json.dumps({**body, "canonical_sha256_without_this_field": csha(body)}, sort_keys=True))


if __name__ == "__main__":
    main()
