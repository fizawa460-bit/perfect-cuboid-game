#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import z3
from sympy import Matrix

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
RETAINED = ROOT / "stages/stage33/33-07/picard_base_rows_retained.py"
MARKING = ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py"
N260_STATE = HERE.parent / "N260/STATE.json"
sys.path.insert(0, str(RESIDUAL))

from hperp_integral_adapter import HperpIntegralPairingAdapter
from pairing_prefix_engine import RetainedBasisPairingTransform

EXPECTED_BUNDLE_CANONICAL = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
EXPECTED_MARKING_CANONICAL = "e06291dddfc529fca2c0b0fe58dd43151faccd3d7997d9aa5797e1978227bb7c"
EXCEPTIONAL_LABELS = list(range(93, 141))
NORMAL_LABELS = list(range(1, 93))
X4_LABEL = 49
TARGETS = [
    {"row_id":"g0-d176","degree":176,"e":48,"normal_mass":3104,"x4_max":84},
    {"row_id":"g1-d192","degree":192,"e":48,"normal_mass":3408,"x4_max":92},
]


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


def zsum(coeffs, vars_):
    return z3.Sum([int(a) * v for a, v in zip(coeffs, vars_)])


def main() -> None:
    n260 = json.loads(N260_STATE.read_text())
    if n260.get("node_id") != "N260" or n260["proof"].get("full_exceptional_vector") != "[1]^48":
        raise ValueError("N260 [1]^48 authority regression")

    bundle = load_retained(RETAINED, "s32_n341_bundle")
    marking = load_retained(MARKING, "s32_n341_marking")
    if bundle.get("canonical_sha256") != EXPECTED_BUNDLE_CANONICAL:
        raise ValueError("retained bundle canonical regression")
    if marking.get("canonical_sha256") != EXPECTED_MARKING_CANONICAL:
        raise ValueError("retained marking canonical regression")

    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    transform = RetainedBasisPairingTransform.from_bundle(bundle)
    if transform.den != 8:
        raise ValueError(f"selected64 denominator regression: {transform.den}")
    selected_labels = list(transform.certificate["selected_known_indices_1based"])
    if len(selected_labels) != 64 or sum(1 for v in selected_labels if v > 92) != 29:
        raise ValueError("selected64 label partition regression")
    if any(v <= 92 for v in selected_labels[:29]) or any(v > 92 for v in selected_labels[29:]):
        raise ValueError("selected64 exceptionals-first regression")

    # y consists of 29 fixed exceptional selected pairings (=1) followed by 35 unknown normal selected pairings.
    yn = [z3.Int(f"yn_{j}") for j in range(35)]
    yexpr = [z3.IntVal(1) for _ in range(29)] + yn
    B = transform.inverse_integer
    P = adapter.pairing_matrix
    # num = 8*x in retained Picard basis. all140 numerator pairings are P*num = 8*pairing.
    num_expr = [zsum([B[i, j] for j in range(64)], yexpr) for i in range(64)]
    pairing_num = [zsum([P[r, i] for i in range(64)], num_expr) for r in range(140)]

    base = z3.SolverFor("QF_LIA")
    # Exact Picard integrality: every coordinate numerator is divisible by 8.
    for expr in num_expr:
        base.add(expr % 8 == 0)
    # Full [1]^48 exceptional target, including the 19 exceptionals not selected among the 64 coordinates.
    for label in EXCEPTIONAL_LABELS:
        base.add(pairing_num[label - 1] == 8)
    # All normal pairings nonnegative. Selected normal coordinates are also explicitly bounded.
    for label in NORMAL_LABELS:
        base.add(pairing_num[label - 1] >= 0)

    normal_total_num = z3.Sum([pairing_num[label - 1] for label in NORMAL_LABELS])
    x4_num = pairing_num[X4_LABEL - 1]

    out_targets = []
    total = sat_total = unsat_total = unknown_total = 0
    first_sat_witness = None
    for target in TARGETS:
        sat_x4, unsat_x4, unknown_x4 = [], [], []
        witness_sha = []
        mass = int(target["normal_mass"])
        # Bound selected normal pairings by total normal mass to strengthen propagation without changing semantics.
        base.push()
        for v in yn:
            base.add(v >= 0, v <= mass)
        base.add(normal_total_num == 8 * mass)
        for x4 in range(int(target["x4_max"]) + 1):
            base.push()
            base.add(x4_num == 8 * x4)
            result = base.check()
            if result == z3.sat:
                sat_x4.append(x4)
                model = base.model()
                yvals = [1] * 29 + [int(model.eval(v, model_completion=True).as_long()) for v in yn]
                if not transform.full_membership(yvals):
                    raise ValueError("SAT selected64 membership replay regression")
                xvals = transform.reconstruct_picard_basis(yvals)
                pairings = [sum(int(P[r, i]) * xvals[i] for i in range(64)) for r in range(140)]
                if pairings[92:] != [1] * 48:
                    raise ValueError("SAT exceptional replay regression")
                if min(pairings[:92]) < 0 or sum(pairings[:92]) != mass or pairings[X4_LABEL - 1] != x4:
                    raise ValueError("SAT normal/x4 replay regression")
                ws = csha({"selected64_pairings": yvals, "picard_coordinates": xvals, "all140_pairings": pairings})
                witness_sha.append([x4, ws])
                if first_sat_witness is None:
                    first_sat_witness = {
                        "row_id": target["row_id"], "x4": x4,
                        "selected64_pairings": yvals,
                        "picard_coordinates": xvals,
                        "all140_pairings": pairings,
                        "witness_sha256": ws,
                    }
            elif result == z3.unsat:
                unsat_x4.append(x4)
            else:
                unknown_x4.append(x4)
            base.pop()
        base.pop()
        count = int(target["x4_max"]) + 1
        total += count; sat_total += len(sat_x4); unsat_total += len(unsat_x4); unknown_total += len(unknown_x4)
        out_targets.append({**target,
            "candidate_count_after_n310": count,
            "integral_picard_sat_count": len(sat_x4),
            "integral_picard_unsat_count": len(unsat_x4),
            "unknown_count": len(unknown_x4),
            "sat_x4": sat_x4,
            "unsat_x4": unsat_x4,
            "witness_sha_by_sat_x4": witness_sha,
        })

    body = {
        "schema": "STAGE32_32_01_178_N341_SELECTED64_INTEGRAL_PICARD_COMPLETION_V1",
        "source_scope": "N310-reduced 178 terminals in g0-d176/e48 and g1-d192/e48",
        "coordinate_model": {
            "selected64_denominator": 8,
            "selected64_labels_1based": selected_labels,
            "fixed_selected_exceptional_count": 29,
            "unknown_selected_normal_count": 35,
            "picard_integrality": "inverse_integer*y divisible coordinatewise by 8",
            "all48_exceptional_pairings": "exactly 1",
            "all92_normal_pairings": "nonnegative",
            "normal_total": "19*d-5*e",
            "x4_label_1based": 49,
        },
        "targets": out_targets,
        "aggregate": {"candidate_count_after_n310": total, "integral_picard_sat_count": sat_total, "integral_picard_unsat_count": unsat_total, "unknown_count": unknown_total},
        "first_sat_witness": first_sat_witness,
        "semantics": {
            "same_exact_picard64_problem_as_n340_v1": True,
            "n340_v1_timeout_does_not_grant_credit": True,
            "selected64_is_exact_full_rank_pairing_coordinate_system": True,
            "integral_unsat_is_exact_no_integral_picard64_completion": True,
            "integral_sat_is_picard64_completion_only_not_full_production_leaf": True,
            "does_not_compute_reynolds_projection_or_59d_node_support": True,
            "does_not_run_ex5_exceptional_branching": True,
            "n260_n310_hostile_audits_required_before_main_credit": True,
            "full178_complete": False,
            "heavy_compute": False,
            "theorem_credit": False,
        },
    }
    print(json.dumps({**body, "canonical_sha256_without_this_field": csha(body)}, sort_keys=True))


if __name__ == "__main__":
    main()
