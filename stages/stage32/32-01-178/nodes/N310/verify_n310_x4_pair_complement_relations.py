#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
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
EXPECTED_STRATA = {
    ("g0-d174", 174, 48): 3067,
    ("g0-d176", 176, 48): 3105,
    ("g1-d190", 190, 48): 3371,
    ("g1-d192", 192, 48): 3409,
}
EXCEPTIONAL_LABELS = list(range(93, 141))
NORMAL_LABELS = list(range(1, 93))
X4_LABEL = 49
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


def qpair(q: sympy.Rational) -> list[int]:
    q = sympy.Rational(q)
    return [int(sympy.numer(q)), int(sympy.denom(q))]


def main() -> None:
    n260 = json.loads(N260_STATE.read_text())
    if n260.get("node_id") != "N260" or n260["proof"].get("full_exceptional_vector") != "[1]^48":
        raise ValueError("N260 [1]^48 authority regression")

    bundle = load_retained(RETAINED, "s32_n310_picard_bundle")
    marking = load_retained(MARKING, "s32_n310_marking")
    if bundle.get("canonical_sha256") != EXPECTED_BUNDLE_CANONICAL:
        raise ValueError("retained Picard bundle canonical regression")
    if marking.get("canonical_sha256") != EXPECTED_MARKING_CANONICAL:
        raise ValueError("retained marking canonical regression")
    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    P = adapter.pairing_matrix
    if P.shape != (140, PICARD_RANK):
        raise ValueError(f"pairing matrix shape regression: {P.shape}")

    normal_sum = Matrix.zeros(1, PICARD_RANK)
    for label in NORMAL_LABELS:
        normal_sum += P.row(label - 1)
    base = Matrix.vstack(*([P.row(label - 1) for label in EXCEPTIONAL_LABELS] + [normal_sum]))
    if base.shape != (49, 64) or base.rank() != 49:
        raise ValueError(f"base functional rank regression: {base.shape}, rank={base.rank()}")

    _, pivot_cols = base.rref()
    if len(pivot_cols) != 49:
        raise ValueError("failed to extract 49 pivot columns")
    square = base[:, list(pivot_cols)]
    if square.det() == 0:
        raise ValueError("pivot square singular")
    square_inv = square.inv()

    relations = []
    x4row = P.row(X4_LABEL - 1)
    for label in NORMAL_LABELS:
        if label == X4_LABEL:
            continue
        target = x4row + P.row(label - 1)
        coeff = target[:, list(pivot_cols)] * square_inv
        if coeff * base != target:
            continue
        exc_const = sum(sympy.Rational(coeff[0, j]) for j in range(48))
        normal_coeff = sympy.Rational(coeff[0, 48])
        per_stratum = []
        best_extra = 0
        for row_id, degree, e in sorted(EXPECTED_STRATA):
            normal_mass = 19 * degree - 5 * e
            fixed_sum = sympy.factor(exc_const + normal_coeff * normal_mass)
            cap = int(sympy.floor(fixed_sum)) if fixed_sum >= 0 else -1
            old_block = EXPECTED_STRATA[(row_id, degree, e)]
            rejected_by_pair_cap = old_block if cap < 0 else max(0, old_block - (cap + 1))
            per_stratum.append({
                "row_id": row_id,
                "degree": degree,
                "e": e,
                "normal_mass": normal_mass,
                "fixed_x4_plus_partner": qpair(fixed_sum),
                "necessary_x4_cap_from_partner_nonnegativity": cap,
                "rejected_vs_full_x4_block": rejected_by_pair_cap,
            })
            best_extra = max(best_extra, rejected_by_pair_cap)
        relations.append({
            "partner_normal_label_1based": label,
            "exceptional_allones_constant": qpair(exc_const),
            "normal_mass_coefficient": qpair(normal_coeff),
            "strata": per_stratum,
            "max_rejected_vs_full_x4_block": best_extra,
        })

    relations.sort(key=lambda r: (-int(r["max_rejected_vs_full_x4_block"]), int(r["partner_normal_label_1based"])))
    body = {
        "schema": "STAGE32_32_01_178_N310_X4_PAIR_COMPLEMENT_RELATIONS_V1",
        "source_scope": "N260 four e=K=48 strata only",
        "base_functionals": {
            "fixed_exceptional_pairings": "labels93..140 all equal 1",
            "normal_total": "sum labels1..92 = 19*d-5*e",
            "rank": 49,
        },
        "search": {
            "target_form": "pairing(label49=x4) + pairing(other normal label)",
            "normal_partner_candidates": 91,
            "exact_relations_found": len(relations),
            "nonnegativity_consequence": "partner>=0 implies x4<=fixed pair sum",
        },
        "relations": relations,
        "best_relation": relations[0] if relations else None,
        "semantics": {
            "exact_rational_rowspace_search": True,
            "rejection_is_zero_loss_relative_to_n260_and_normal_mass_authority": True,
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
