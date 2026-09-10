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
    bundle = load_retained(RETAINED, "s32_n330_bundle")
    marking = load_retained(MARKING, "s32_n330_marking")
    if bundle.get("canonical_sha256") != EXPECTED_BUNDLE_CANONICAL:
        raise ValueError("retained bundle canonical regression")
    if marking.get("canonical_sha256") != EXPECTED_MARKING_CANONICAL:
        raise ValueError("retained marking canonical regression")
    P = HperpIntegralPairingAdapter.from_retained(marking, bundle).pairing_matrix
    if P.shape != (140, PICARD_RANK):
        raise ValueError(f"pairing matrix shape regression: {P.shape}")

    xs = [z3.Real(f"u_{j}") for j in range(PICARD_RANK)]
    solver = z3.Solver()
    normal_expr = []
    for label in NORMAL_LABELS:
        expr = dot_int([P[label - 1, j] for j in range(PICARD_RANK)], xs)
        normal_expr.append(expr)
        solver.add(expr >= 0)
    for label in EXCEPTIONAL_LABELS:
        solver.add(dot_int([P[label - 1, j] for j in range(PICARD_RANK)], xs) == 1)
    x4_expr = normal_expr[X4_LABEL - 1]
    normal_total_expr = z3.Sum(normal_expr)

    out_targets = []
    total = sat_total = unsat_total = unknown_total = 0
    for target in TARGETS:
        feasible = []
        rejected = []
        unknown = []
        for x4 in range(int(target["x4_max"]) + 1):
            solver.push()
            solver.add(normal_total_expr == int(target["normal_mass"]))
            solver.add(x4_expr == x4)
            result = solver.check()
            solver.pop()
            if result == z3.sat:
                feasible.append(x4)
            elif result == z3.unsat:
                rejected.append(x4)
            else:
                unknown.append(x4)
        count = int(target["x4_max"]) + 1
        total += count
        sat_total += len(feasible)
        unsat_total += len(rejected)
        unknown_total += len(unknown)
        out_targets.append({
            **target,
            "candidate_count_after_n310": count,
            "rational_feasible_count": len(feasible),
            "rational_infeasible_count": len(rejected),
            "unknown_count": len(unknown),
            "rational_feasible_x4": feasible,
            "rational_infeasible_x4": rejected,
        })

    body = {
        "schema": "STAGE32_32_01_178_N330_RATIONAL_NONNEGATIVE_PICARD_RELAXATION_V1",
        "source_scope": "N310 survivors in g0-d176/e48 and g1-d192/e48 only",
        "model": {
            "picard_basis_variables": 64,
            "variable_sort": "Real",
            "fixed_exceptional_pairings": "labels93..140 all equal 1",
            "normal_pairings_nonnegative": "labels1..92 >=0",
            "normal_total": "19*d-5*e",
            "x4_label_1based": 49,
            "integer_picard_integrality_relaxed": True,
            "solver_logic": "exact linear rational arithmetic",
        },
        "targets": out_targets,
        "aggregate": {
            "candidate_count_after_n310": total,
            "rational_feasible_count": sat_total,
            "rational_infeasible_count": unsat_total,
            "unknown_count": unknown_total,
        },
        "semantics": {
            "rational_unsat_implies_no_integral_picard_completion": True,
            "rational_sat_does_not_imply_integral_picard_completion": True,
            "does_not_run_ex5_adaptive_exceptional_partition": True,
            "does_not_claim_picard_integer_sat": True,
            "n260_n310_hostile_audits_required_before_credit_consumption": True,
            "heavy_compute": False,
            "full178_complete": False,
            "theorem_credit": False,
        },
    }
    print(json.dumps({**body, "canonical_sha256_without_this_field": csha(body)}, sort_keys=True))


if __name__ == "__main__":
    main()
