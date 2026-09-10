#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import z3

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
RETAINED = ROOT / "stages/stage33/33-07/picard_base_rows_retained.py"
MARKING = ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py"
N260_STATE = HERE.parent / "N260/STATE.json"
sys.path.insert(0, str(RESIDUAL))

from hperp_integral_adapter import HperpIntegralPairingAdapter

EXPECTED_BUNDLE_CANONICAL = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
EXPECTED_MARKING_CANONICAL = "e06291dddfc529fca2c0b0fe58dd43151faccd3d7997d9aa5797e1978227bb7c"
EXCEPTIONAL_LABELS = list(range(93, 141))
NORMAL_LABELS = list(range(1, 93))
X4_LABEL = 49
TARGETS = [
    {"row_id":"g0-d176","degree":176,"e":48,"normal_mass":3104,"x4_max":84},
    {"row_id":"g1-d192","degree":192,"e":48,"normal_mass":3408,"x4_max":92},
]
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


def dot_int(row, xs):
    return z3.Sum([int(row[j]) * xs[j] for j in range(len(xs))])


def main() -> None:
    n260 = json.loads(N260_STATE.read_text())
    if n260.get("node_id") != "N260" or n260["proof"].get("full_exceptional_vector") != "[1]^48":
        raise ValueError("N260 [1]^48 authority regression")

    bundle = load_retained(RETAINED, "s32_n340_bundle")
    marking = load_retained(MARKING, "s32_n340_marking")
    if bundle.get("canonical_sha256") != EXPECTED_BUNDLE_CANONICAL:
        raise ValueError("retained bundle canonical regression")
    if marking.get("canonical_sha256") != EXPECTED_MARKING_CANONICAL:
        raise ValueError("retained marking canonical regression")
    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    P = adapter.pairing_matrix
    if P.shape != (140, PICARD_RANK):
        raise ValueError(f"pairing matrix shape regression: {P.shape}")

    xs = [z3.Int(f"x_{j}") for j in range(PICARD_RANK)]
    solver = z3.SolverFor("QF_LIA")
    normal_expr = []
    for label in NORMAL_LABELS:
        expr = dot_int([P[label - 1, j] for j in range(PICARD_RANK)], xs)
        normal_expr.append(expr)
        solver.add(expr >= 0)
    for label in EXCEPTIONAL_LABELS:
        solver.add(dot_int([P[label - 1, j] for j in range(PICARD_RANK)], xs) == 1)
    normal_total_expr = z3.Sum(normal_expr)
    x4_expr = normal_expr[X4_LABEL - 1]

    targets_out = []
    total = sat_total = unsat_total = unknown_total = 0
    first_sat_witness = None
    for target in TARGETS:
        sat_x4 = []
        unsat_x4 = []
        unknown_x4 = []
        witness_sha_by_x4 = []
        for x4 in range(int(target["x4_max"]) + 1):
            solver.push()
            solver.add(normal_total_expr == int(target["normal_mass"]))
            solver.add(x4_expr == x4)
            result = solver.check()
            if result == z3.sat:
                sat_x4.append(x4)
                model = solver.model()
                xv = [int(model.eval(v, model_completion=True).as_long()) for v in xs]
                pairings = [sum(int(P[i, j]) * xv[j] for j in range(PICARD_RANK)) for i in range(140)]
                if pairings[92:] != [1] * 48:
                    raise ValueError("SAT exceptional replay regression")
                if min(pairings[:92]) < 0 or sum(pairings[:92]) != int(target["normal_mass"]):
                    raise ValueError("SAT normal replay regression")
                if pairings[X4_LABEL - 1] != x4:
                    raise ValueError("SAT x4 replay regression")
                wsha = csha({"picard_coordinates": xv, "all140_pairings": pairings})
                witness_sha_by_x4.append([x4, wsha])
                if first_sat_witness is None:
                    first_sat_witness = {
                        "row_id": target["row_id"],
                        "x4": x4,
                        "picard_coordinates": xv,
                        "all140_pairings": pairings,
                        "witness_sha256": wsha,
                    }
            elif result == z3.unsat:
                unsat_x4.append(x4)
            else:
                unknown_x4.append(x4)
            solver.pop()
        count = int(target["x4_max"]) + 1
        total += count
        sat_total += len(sat_x4)
        unsat_total += len(unsat_x4)
        unknown_total += len(unknown_x4)
        targets_out.append({
            **target,
            "candidate_count_after_n310": count,
            "integral_picard_sat_count": len(sat_x4),
            "integral_picard_unsat_count": len(unsat_x4),
            "unknown_count": len(unknown_x4),
            "sat_x4": sat_x4,
            "unsat_x4": unsat_x4,
            "witness_sha_by_sat_x4": witness_sha_by_x4,
        })

    body = {
        "schema": "STAGE32_32_01_178_N340_LOCAL_INTEGRAL_PICARD_COMPLETION_V1",
        "source_scope": "N310-reduced 178 local terminals in g0-d176/e48 and g1-d192/e48",
        "model": {
            "picard_basis_variables": 64,
            "variable_sort": "Int",
            "fixed_exceptional_pairings": "labels93..140 all equal 1",
            "normal_pairings_nonnegative": "labels1..92 >=0",
            "normal_total": "19*d-5*e",
            "x4_label_1based": 49,
            "solver_logic": "QF_LIA",
            "retained_pairing_adapter_canonical": adapter.certificate["canonical_sha256_without_this_field"],
        },
        "targets": targets_out,
        "aggregate": {
            "candidate_count_after_n310": total,
            "integral_picard_sat_count": sat_total,
            "integral_picard_unsat_count": unsat_total,
            "unknown_count": unknown_total,
        },
        "first_sat_witness": first_sat_witness,
        "semantics": {
            "integral_unsat_is_exact_no_integral_picard64_class_with_stated_pairings": True,
            "integral_sat_is_picard64_completion_only_not_full_production_leaf": True,
            "does_not_compute_reynolds_projection_or_59d_node_support": True,
            "does_not_claim_full178_completion": True,
            "n260_n310_hostile_audits_required_before_main_credit": True,
            "ex5_population_wide_credit_not_imported": True,
            "heavy_compute": False,
            "theorem_credit": False,
        },
    }
    print(json.dumps({**body, "canonical_sha256_without_this_field": csha(body)}, sort_keys=True))


if __name__ == "__main__":
    main()
