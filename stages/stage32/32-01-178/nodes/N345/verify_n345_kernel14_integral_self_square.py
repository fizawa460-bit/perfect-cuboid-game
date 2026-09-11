#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import sys
from pathlib import Path

import sympy
import z3
from sympy import Matrix, Rational

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
RETAINED = ROOT / "stages/stage33/33-07/picard_base_rows_retained.py"
MARKING = ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py"
N260_STATE = HERE.parent / "N260/STATE.json"
N342_RESULT = HERE.parent / "N342/RESULT.json"
sys.path.insert(0, str(RESIDUAL))

from hperp_integral_adapter import HperpIntegralPairingAdapter

EXPECTED_BUNDLE_CANONICAL = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
EXPECTED_MARKING_CANONICAL = "e06291dddfc529fca2c0b0fe58dd43151faccd3d7997d9aa5797e1978227bb7c"
EXPECTED_N342_CHECKPOINT_CANONICAL = "0a556575c4ad365d5f0816a60c380de16ca609310961e58f6e63834082a61c88"
N344_RUN = 34428307787
N344_VERIFY_JOB = 102718165273
N344_LEDGER_JOB = 102719341587
N344_VERIFIER_BLOB = "83f6e2b4d8ed04b89a8ccb90980e589651155542"
EXCEPTIONAL_LABELS = list(range(93, 141))
NORMAL_LABELS = list(range(1, 93))
X4_LABEL = 49
TARGETS = [
    {"row_id":"g0-d176","genus":0,"degree":176,"e":48,"normal_mass":3104,
     "x4_values":[3,7,11,15,19,23,27,31,35,39]},
    {"row_id":"g1-d192","genus":1,"degree":192,"e":48,"normal_mass":3408,
     "x4_values":[3,7,11,15,19,23,27,31,35,39,43]},
]
PER_TERMINAL_TIMEOUT_MS = 20000


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


def lcm_denominators(values) -> int:
    den = 1
    for value in values:
        den = math.lcm(den, int(Rational(value).q))
    return den


def zlinear(constant: int, coeffs, vars_):
    terms = [z3.IntVal(int(constant))]
    terms.extend(int(a) * v for a, v in zip(coeffs, vars_) if int(a) != 0)
    return z3.Sum(terms)


def quadratic_expr(gram: Matrix, nums):
    terms = []
    for i in range(64):
        gii = int(gram[i, i])
        if gii:
            terms.append(gii * nums[i] * nums[i])
        for j in range(i + 1, 64):
            gij = int(gram[i, j])
            if gij:
                terms.append(2 * gij * nums[i] * nums[j])
    return z3.Sum(terms) if terms else z3.IntVal(0)


def main() -> None:
    n260 = json.loads(N260_STATE.read_text())
    if n260.get("node_id") != "N260" or n260["proof"].get("full_exceptional_vector") != "[1]^48":
        raise ValueError("N260 [1]^48 authority regression")

    n342 = json.loads(N342_RESULT.read_text())
    claimed = n342.get("canonical_sha256_without_this_field")
    body342 = dict(n342)
    body342.pop("canonical_sha256_without_this_field", None)
    if claimed != EXPECTED_N342_CHECKPOINT_CANONICAL or csha(body342) != claimed:
        raise ValueError("N342 checkpoint canonical regression")
    if n342.get("aggregate", {}).get("sat_terminal_count") != 21:
        raise ValueError("N342 residual count regression")
    if n342.get("sat_x4", {}).get("g0-d176") != TARGETS[0]["x4_values"]:
        raise ValueError("N342 g0 x4 residual set regression")
    if n342.get("sat_x4", {}).get("g1-d192") != TARGETS[1]["x4_values"]:
        raise ValueError("N342 g1 x4 residual set regression")

    bundle = load_retained(RETAINED, "s32_n345_bundle")
    marking = load_retained(MARKING, "s32_n345_marking")
    if bundle.get("canonical_sha256") != EXPECTED_BUNDLE_CANONICAL:
        raise ValueError("retained bundle canonical regression")
    if marking.get("canonical_sha256") != EXPECTED_MARKING_CANONICAL:
        raise ValueError("retained marking canonical regression")

    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    P = adapter.pairing_matrix
    gram = Matrix(bundle["picard_gram_64x64"])
    if P.shape != (140, 64) or gram.shape != (64, 64) or gram != gram.T:
        raise ValueError("retained Picard matrix shape/symmetry regression")

    normal_total_row = Matrix([[sum(int(P[r, c]) for r in range(92)) for c in range(64)]])
    exceptional_rows = P.extract([label - 1 for label in EXCEPTIONAL_LABELS], list(range(64)))
    x4_row = P.extract([X4_LABEL - 1], list(range(64)))
    A = normal_total_row.col_join(exceptional_rows).col_join(x4_row)
    if A.shape != (50, 64):
        raise ValueError(f"N345 equality matrix shape regression: {A.shape}")
    rank = int(A.rank())
    if rank != 50:
        raise ValueError(f"N345 equality rank regression: {rank}")

    _, pivot_tuple = A.rref()
    pivot_columns = list(pivot_tuple)
    free_columns = [j for j in range(64) if j not in pivot_columns]
    if len(pivot_columns) != 50 or len(free_columns) != 14:
        raise ValueError("N345 50+14 pivot/free split regression")

    Ap = A.extract(list(range(50)), pivot_columns)
    Af = A.extract(list(range(50)), free_columns)
    if Ap.det() == 0:
        raise ValueError("N345 pivot block singular")
    Ap_inv = Ap.inv()
    M = Ap_inv * Af
    denominator = lcm_denominators(list(Ap_inv) + list(M))
    if denominator <= 0:
        raise ValueError("N345 invalid common denominator")

    # Integer exactness of the scaled affine reconstruction.
    scaled_M = M * denominator
    if any(sympy.denom(v) != 1 for v in scaled_M):
        raise ValueError("N345 scaled kernel coefficient nonintegral")

    rows = []
    sat_total = unsat_total = unknown_total = 0
    for target in TARGETS:
        mass = int(target["normal_mass"])
        degree = int(target["degree"])
        genus = int(target["genus"])
        required_lower = -degree - 2 + 2 * genus
        for x4 in target["x4_values"]:
            target_vec = Matrix([mass] + [1] * 48 + [int(x4)])
            particular_p = Ap_inv * target_vec
            scaled_particular_p = particular_p * denominator
            if any(sympy.denom(v) != 1 for v in scaled_particular_p):
                raise ValueError("N345 scaled particular solution nonintegral")

            free_vars = [z3.Int(f"t_{target['row_id']}_{x4}_{j}") for j in range(14)]
            scaled_x = [None] * 64
            for j, column in enumerate(free_columns):
                scaled_x[column] = denominator * free_vars[j]
            for i, column in enumerate(pivot_columns):
                const = int(scaled_particular_p[i, 0])
                coeffs = [-int(scaled_M[i, j]) for j in range(14)]
                scaled_x[column] = zlinear(const, coeffs, free_vars)
            if any(v is None for v in scaled_x):
                raise ValueError("N345 scaled affine reconstruction incomplete")

            solver = z3.SolverFor("QF_NIA")
            solver.set(timeout=PER_TERMINAL_TIMEOUT_MS)
            for column in pivot_columns:
                solver.add(scaled_x[column] % denominator == 0)

            normal_nums = []
            for label in NORMAL_LABELS:
                expr = z3.Sum([int(P[label - 1, i]) * scaled_x[i] for i in range(64) if int(P[label - 1, i]) != 0])
                normal_nums.append(expr)
                solver.add(expr >= 0, expr <= denominator * mass)

            # Equality rows are implied algebraically by the affine reconstruction;
            # replay them in the model below. The nonlinear condition is exactly
            # denominator^2 * x^T G x >= denominator^2 * required_lower.
            square_num = quadratic_expr(gram, scaled_x)
            solver.add(square_num >= denominator * denominator * required_lower)

            result = solver.check()
            row = {
                "row_id": target["row_id"],
                "g": genus,
                "d": degree,
                "e": int(target["e"]),
                "x4": int(x4),
                "required_self_square_lower": required_lower,
            }
            if result == z3.sat:
                sat_total += 1
                model = solver.model()
                tvals = [int(model.eval(v, model_completion=True).as_long()) for v in free_vars]
                xvals = [0] * 64
                for j, column in enumerate(free_columns):
                    xvals[column] = tvals[j]
                for i, column in enumerate(pivot_columns):
                    num = int(scaled_particular_p[i, 0]) - sum(int(scaled_M[i, j]) * tvals[j] for j in range(14))
                    if num % denominator != 0:
                        raise ValueError("N345 SAT pivot integrality replay regression")
                    xvals[column] = num // denominator

                pairings = [sum(int(P[r, i]) * xvals[i] for i in range(64)) for r in range(140)]
                if pairings[92:] != [1] * 48:
                    raise ValueError("N345 SAT exceptional replay regression")
                if min(pairings[:92]) < 0 or sum(pairings[:92]) != mass:
                    raise ValueError("N345 SAT normal mass replay regression")
                if pairings[X4_LABEL - 1] != int(x4):
                    raise ValueError("N345 SAT x4 replay regression")
                self_square = int((Matrix(xvals).T * gram * Matrix(xvals))[0])
                if self_square < required_lower:
                    raise ValueError("N345 SAT self-square replay regression")
                witness = {
                    "free_columns_0based": free_columns,
                    "free_values": tvals,
                    "picard_coordinates": xvals,
                    "all140_pairings": pairings,
                    "self_square": self_square,
                }
                row.update({
                    "verdict": "SAT_KERNEL14_THRESHOLD",
                    "self_square": self_square,
                    "witness_sha256": csha(witness),
                })
            elif result == z3.unsat:
                unsat_total += 1
                row["verdict"] = "UNSAT_KERNEL14_THRESHOLD"
            else:
                unknown_total += 1
                row.update({"verdict": "UNKNOWN", "reason_unknown": solver.reason_unknown()})
            rows.append(row)

    body = {
        "schema": "STAGE32_32_01_178_N345_KERNEL14_INTEGRAL_SELF_SQUARE_V1",
        "source_locks": {
            "n342_checkpoint_canonical_sha256": EXPECTED_N342_CHECKPOINT_CANONICAL,
            "n344_run_id": N344_RUN,
            "n344_verify_job_id": N344_VERIFY_JOB,
            "n344_ledger_job_id": N344_LEDGER_JOB,
            "n344_observed_ledger": "SAT=0 UNSAT=0 UNKNOWN=21",
            "n344_verifier_blob_sha1": N344_VERIFIER_BLOB,
            "retained_bundle_canonical_sha256": EXPECTED_BUNDLE_CANONICAL,
            "retained_marking_canonical_sha256": EXPECTED_MARKING_CANONICAL,
        },
        "exact_reduction": {
            "picard_integer_variables_original": 64,
            "linear_equality_rank": rank,
            "free_integer_coordinates": len(free_columns),
            "free_columns_0based": free_columns,
            "pivot_columns_0based": pivot_columns,
            "common_affine_denominator": denominator,
            "equalities": "normal-total + all48 exceptional pairings=1 + x4",
            "pivot_integrality": "scaled pivot affine numerators divisible by common denominator",
            "all92_normal_pairings": "0 <= pairing <= normal_mass",
            "self_square_condition": "x^T G x >= -d-2+2g",
            "solver_logic": "QF_NIA",
            "per_terminal_timeout_ms": PER_TERMINAL_TIMEOUT_MS,
        },
        "aggregate": {
            "terminal_count": len(rows),
            "sat_threshold_count": sat_total,
            "unsat_threshold_count": unsat_total,
            "unknown_count": unknown_total,
        },
        "rows": rows,
        "semantics": {
            "reduction_is_exact_for_integer_picard_classes_satisfying_the_stated_linear_equalities": True,
            "unsat_is_exact_no_integral_picard_completion_meeting_normal_nonnegativity_and_self_square_necessary_condition": True,
            "sat_is_only_a_picard_numerical_class_not_effective_curve_existence": True,
            "unknown_or_timeout_receives_zero_pruning_credit": True,
            "n350_producer_registry_unchanged": True,
            "hostile_audit_required_before_main_credit": True,
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
