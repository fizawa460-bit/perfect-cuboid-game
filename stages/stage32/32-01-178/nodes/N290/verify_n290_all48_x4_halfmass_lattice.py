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

from direct_picard_slice_bridge import DirectPicardSliceBridge
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
FIRST_NORMAL_HALF_COUNT = 46
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


def primitive_integer_vector(v: Matrix) -> list[int]:
    lcm = 1
    for q in v:
        lcm = math.lcm(lcm, int(sympy.denom(q)))
    vals = [int(q * lcm) for q in v]
    g = 0
    for x in vals:
        g = math.gcd(g, abs(x))
    if g:
        vals = [x // g for x in vals]
    if vals[-1] < 0:
        vals = [-x for x in vals]
    return vals


def main() -> None:
    n260 = json.loads(N260_STATE.read_text())
    if n260.get("node_id") != "N260" or n260["proof"].get("full_exceptional_vector") != "[1]^48":
        raise ValueError("N260 rigidity authority regression")
    observed = {
        (str(row["row_id"]), parse_degree(row["row_id"]), int(row["e"])): int(row["normal_x4_block"])
        for row in n260["retained_result"]["one_block_strata"]
    }
    if observed != EXPECTED_STRATA:
        raise ValueError(f"N260 four-stratum regression: {observed}")

    bundle = load_retained(RETAINED, "s32_n290_picard_bundle")
    marking = load_retained(MARKING, "s32_n290_marking")
    if bundle.get("canonical_sha256") != EXPECTED_BUNDLE_CANONICAL:
        raise ValueError("retained Picard bundle canonical regression")
    if marking.get("canonical_sha256") != EXPECTED_MARKING_CANONICAL:
        raise ValueError("retained Stage32 marking canonical regression")

    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    bridge = DirectPicardSliceBridge.from_retained(marking, bundle)
    P = adapter.pairing_matrix
    if P.shape != (140, PICARD_RANK):
        raise ValueError(f"all140 pairing matrix shape regression: {P.shape}")

    exceptional_sum = Matrix.zeros(1, PICARD_RANK)
    normal_sum = Matrix.zeros(1, PICARD_RANK)
    first_half_sum = Matrix.zeros(1, PICARD_RANK)
    for i in range(NORMAL_LABEL_COUNT):
        normal_sum += P.row(i)
        if i < FIRST_NORMAL_HALF_COUNT:
            first_half_sum += P.row(i)
    for i in range(NORMAL_LABEL_COUNT, NORMAL_LABEL_COUNT + 48):
        exceptional_sum += P.row(i)
    if tuple(int(first_half_sum[0, j]) for j in range(PICARD_RANK)) != bridge.first_normal_half_functional:
        raise ValueError("first-normal-half functional source-lock regression")
    if tuple(int(exceptional_sum[0, j]) for j in range(PICARD_RANK)) != bridge.exceptional_mass_functional:
        raise ValueError("exceptional functional source-lock regression")
    if normal_sum + 5 * exceptional_sum != 19 * Matrix([list(bridge.degree_functional)]):
        raise ValueError("normal + 5 exceptional = 19 degree identity regression")

    base_rows = [P.row(label - 1) for label in EXCEPTIONAL_LABELS]
    base_rows.append(P.row(X4_LABEL - 1))
    base_rows.append(normal_sum)
    A50 = Matrix.vstack(*base_rows)
    if A50.shape != (50, PICARD_RANK) or A50.rank() != 50:
        raise ValueError(f"N280 base functional rank regression: {A50.shape}, rank={A50.rank()}")

    H = hermite_normal_form(A50)
    if H.shape != (50, 50) or H.det() == 0:
        raise ValueError(f"N280 base HNF regression: {H.shape}")
    Hinv = H.inv()
    modulus = 1
    for q in Hinv:
        modulus = math.lcm(modulus, int(sympy.denom(q)))
    Hinv_int_q = Hinv * modulus
    if any(sympy.denom(q) != 1 for q in Hinv_int_q):
        raise ValueError("base HNF inverse scaling regression")
    Hinv_int = Matrix([
        [int(Hinv_int_q[i, j]) for j in range(Hinv_int_q.cols)]
        for i in range(Hinv_int_q.rows)
    ])

    A51 = A50.col_join(first_half_sum)
    if A51.rank() != 50:
        raise ValueError(f"first-half augmented rank unexpectedly changed: {A51.rank()}")
    left_null = A51.T.nullspace()
    if len(left_null) != 1:
        raise ValueError(f"expected one exact left-null relation, got {len(left_null)}")
    relation = primitive_integer_vector(left_null[0])
    if len(relation) != 51 or relation[-1] == 0:
        raise ValueError("invalid first-half dependence relation")
    if any(int((Matrix([relation]).T.T * A51)[0, j]) != 0 for j in range(A51.cols)):
        raise ValueError("primitive left-null relation replay regression")

    rel_exc_constant = sum(relation[:48])
    rel_x4 = relation[48]
    rel_normal = relation[49]
    rel_a = relation[50]

    def base_lattice_feasible(x4: int, normal_mass: int) -> bool:
        b = Matrix([1] * 48 + [int(x4), int(normal_mass)])
        y = Hinv_int * b
        return all(int(v) % modulus == 0 for v in y)

    def forced_a(x4: int, normal_mass: int) -> tuple[bool, int | None]:
        numerator = -(rel_exc_constant + rel_x4 * int(x4) + rel_normal * int(normal_mass))
        if numerator % rel_a:
            return False, None
        return True, numerator // rel_a

    strata = []
    total = n280_rejected_total = n290_extra_rejected_total = feasible_total = 0
    for (row_id, degree, e), block in sorted(EXPECTED_STRATA.items()):
        normal_mass = 19 * degree - 5 * e
        if block != normal_mass + 1:
            raise ValueError("N260 x4 block / normal-mass identity regression")
        n280_rejected = 0
        extra_rejected = 0
        feasible = []
        forced_a_samples = []
        for x4 in range(normal_mass + 1):
            if not base_lattice_feasible(x4, normal_mass):
                n280_rejected += 1
                continue
            integral, a = forced_a(x4, normal_mass)
            if not integral or a is None or not (0 <= a <= normal_mass):
                extra_rejected += 1
                continue
            feasible.append(x4)
            if len(forced_a_samples) < 5:
                forced_a_samples.append([x4, a])
        strata.append({
            "row_id": row_id,
            "degree": degree,
            "e": e,
            "normal_pairing_mass": normal_mass,
            "terminal_count": block,
            "n280_base_lattice_rejected": n280_rejected,
            "n290_additional_halfmass_rejected": extra_rejected,
            "n290_survivor_count": len(feasible),
            "all_x4_rejected_after_n290": len(feasible) == 0,
            "survivor_x4_min": min(feasible) if feasible else None,
            "survivor_x4_max": max(feasible) if feasible else None,
            "forced_a_samples_x4_a": forced_a_samples,
        })
        total += block
        n280_rejected_total += n280_rejected
        n290_extra_rejected_total += extra_rejected
        feasible_total += len(feasible)

    body = {
        "schema": "STAGE32_32_01_178_N290_ALL48_X4_HALFMASS_DEPENDENCE_V2",
        "source_scope": "N260 four e=K=48 strata only",
        "linear_dependence": {
            "base_functionals": "48 exceptional pairings + label49=x4 + normal_total",
            "base_rank": 50,
            "first_normal_half_adds_rank": 0,
            "primitive_left_null_relation": relation,
            "forced_a_formula": {
                "numerator_exceptional_allones_constant": -rel_exc_constant,
                "numerator_x4_coefficient": -rel_x4,
                "numerator_normal_mass_coefficient": -rel_normal,
                "denominator": rel_a,
                "meaning": "a = (constant + coeff_x4*x4 + coeff_normal*normal_mass)/denominator"
            },
            "first_normal_half_bound": "0 <= a <= normal_total",
            "direct_slice_bridge_sha256": bridge.certificate["canonical_sha256_without_this_field"],
        },
        "base_lattice": {
            "hnf_sha256": matrix_csha(H),
            "image_index": str(abs(int(H.det()))),
            "inverse_denominator_modulus": modulus,
        },
        "strata": strata,
        "aggregate": {
            "terminal_count": total,
            "n280_base_lattice_rejected": n280_rejected_total,
            "n290_additional_halfmass_rejected": n290_extra_rejected_total,
            "n290_survivor_terminal_count": feasible_total,
        },
        "semantics": {
            "exact_linear_dependence_and_integral_lattice_test": True,
            "bounded_first_normal_half_is_source_locked_necessary_condition": True,
            "rejection_is_safe_relative_to_n260_rigidity": True,
            "survival_is_not_picard_sat": True,
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
