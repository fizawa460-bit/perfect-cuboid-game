#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import sys
from pathlib import Path

import sympy
from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form

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
X4_LABEL = 49
NORMAL_LABEL_COUNT = 92
PICARD_RANK = 64


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def matrix_csha(m: Matrix) -> str:
    return csha([[int(m[i, j]) for j in range(m.cols)] for i in range(m.rows)])


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


def parse_degree(row_id: str) -> int:
    return int(str(row_id).split("-d", 1)[1])


def main() -> None:
    n260 = json.loads(N260_STATE.read_text())
    if n260.get("node_id") != "N260":
        raise ValueError("N260 authority regression")
    if n260["proof"].get("full_exceptional_vector") != "[1]^48":
        raise ValueError("N260 [1]^48 authority missing")
    observed = {
        (str(row["row_id"]), parse_degree(row["row_id"]), int(row["e"])): int(row["normal_x4_block"])
        for row in n260["retained_result"]["one_block_strata"]
    }
    if observed != EXPECTED_STRATA:
        raise ValueError(f"N260 four-stratum regression: {observed}")

    bundle = load_retained(RETAINED, "s32_n280_picard_bundle")
    marking = load_retained(MARKING, "s32_n280_marking")
    if bundle.get("canonical_sha256") != EXPECTED_BUNDLE_CANONICAL:
        raise ValueError("retained Picard bundle canonical regression")
    if marking.get("canonical_sha256") != EXPECTED_MARKING_CANONICAL:
        raise ValueError("retained Stage32 marking canonical regression")

    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    P = adapter.pairing_matrix
    if P.shape != (140, PICARD_RANK):
        raise ValueError(f"all140 pairing matrix shape regression: {P.shape}")

    rows = [P.row(label - 1) for label in EXCEPTIONAL_LABELS]
    rows.append(P.row(X4_LABEL - 1))
    normal_sum_row = Matrix.zeros(1, PICARD_RANK)
    for i in range(NORMAL_LABEL_COUNT):
        normal_sum_row += P.row(i)
    rows.append(normal_sum_row)
    A = Matrix.vstack(*rows)
    if A.shape != (50, PICARD_RANK):
        raise ValueError(f"augmented functional matrix shape regression: {A.shape}")

    H = hermite_normal_form(A)
    if H.shape != (50, 50) or H.det() == 0:
        raise ValueError(f"augmented functionals lack full row rank: {H.shape}")
    Hinv = H.inv()
    modulus = 1
    for q in Hinv:
        modulus = math.lcm(modulus, int(sympy.denom(q)))
    Hinv_int_q = Hinv * modulus
    if any(sympy.denom(q) != 1 for q in Hinv_int_q):
        raise ValueError("augmented HNF inverse scaling regression")
    Hinv_int = Matrix([
        [int(Hinv_int_q[i, j]) for j in range(Hinv_int_q.cols)]
        for i in range(Hinv_int_q.rows)
    ])

    def feasible_x4_values(normal_mass: int) -> list[int]:
        constants = []
        slopes = []
        for i in range(50):
            row = [int(Hinv_int[i, j]) for j in range(50)]
            constant = sum(row[j] for j in range(48)) + row[49] * normal_mass
            constants.append(constant % modulus)
            slopes.append(row[48] % modulus)
        return [
            x4 for x4 in range(normal_mass + 1)
            if all((c + a * x4) % modulus == 0 for c, a in zip(constants, slopes))
        ]

    strata = []
    total = rejected_total = feasible_total = 0
    for (row_id, degree, e), block in sorted(EXPECTED_STRATA.items()):
        normal_mass = 19 * degree - 5 * e
        if block != normal_mass + 1:
            raise ValueError("N260 x4 block / normal-mass identity regression")
        feasible = feasible_x4_values(normal_mass)
        rejected = block - len(feasible)
        strata.append({
            "row_id": row_id,
            "degree": degree,
            "e": e,
            "normal_pairing_mass": normal_mass,
            "x4_range": [0, normal_mass],
            "terminal_count": block,
            "lattice_feasible_x4_count": len(feasible),
            "lattice_rejected_x4_count": rejected,
            "all_x4_lattice_rejected": not feasible,
            "feasible_x4_values": feasible if len(feasible) <= 64 else None,
            "feasible_x4_residues_mod_hnf_modulus": sorted({v % modulus for v in feasible}),
        })
        total += block
        rejected_total += rejected
        feasible_total += len(feasible)

    body = {
        "schema": "STAGE32_32_01_178_N280_ALL48_X4_NORMALMASS_LATTICE_V1",
        "source_scope": "N260 four e=K=48 strata only",
        "functionals": {
            "fixed_exceptional_pairings": "labels93..140 all equal 1",
            "x4_normal_label_1based": X4_LABEL,
            "normal_pairing_sum": "sum labels1..92 = 19*d-5*e",
            "remaining_individual_normal_pairings_unfixed": 91,
            "functional_matrix_shape": [50, 64],
            "functional_matrix_sha256": matrix_csha(A),
        },
        "lattice": {
            "hnf_shape": [H.rows, H.cols],
            "hnf_sha256": matrix_csha(H),
            "image_index": str(abs(int(H.det()))),
            "inverse_denominator_modulus": modulus,
        },
        "strata": strata,
        "aggregate": {
            "terminal_count": total,
            "lattice_rejected_terminal_count": rejected_total,
            "lattice_survivor_terminal_count": feasible_total,
            "all_four_strata_lattice_empty": feasible_total == 0,
        },
        "semantics": {
            "exact_integer_lattice_membership_necessary_condition": True,
            "includes_normal_mass_unlike_n270": True,
            "rejection_implies_no_integral_picard64_class_with_required_pairing_functionals": True,
            "feasible_does_not_imply_nonnegative_all140_or_picard_sat": True,
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
