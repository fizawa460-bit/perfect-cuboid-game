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
N342_RESULT = HERE.parent / "N342/RESULT.json"
sys.path.insert(0, str(RESIDUAL))

from hperp_integral_adapter import HperpIntegralPairingAdapter
from pairing_prefix_engine import RetainedBasisPairingTransform

EXPECTED_BUNDLE_CANONICAL = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
EXPECTED_MARKING_CANONICAL = "e06291dddfc529fca2c0b0fe58dd43151faccd3d7997d9aa5797e1978227bb7c"
EXPECTED_N342_CHECKPOINT_CANONICAL = "0a556575c4ad365d5f0816a60c380de16ca609310961e58f6e63834082a61c88"
N341_RUN = 34424019499
N341_JOB = 102705288033
N341_CANONICAL = "672ca52e1b71e7bde2b14de6320ae57dddcbf6f0d3817f3244f27eec20cce315"
N341_VERIFIER_BLOB = "70d17967f7a965de4994dce1bc70a398468ef42e"
EXCEPTIONAL_LABELS = list(range(93, 141))
NORMAL_LABELS = list(range(1, 93))
X4_LABEL = 49
TARGETS = [
    {"row_id":"g0-d176","genus":0,"degree":176,"e":48,"normal_mass":3104,
     "x4_values":[3,7,11,15,19,23,27,31,35,39]},
    {"row_id":"g1-d192","genus":1,"degree":192,"e":48,"normal_mass":3408,
     "x4_values":[3,7,11,15,19,23,27,31,35,39,43]},
]
PER_TERMINAL_TIMEOUT_MS = 15000


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
    terms = [int(a) * v for a, v in zip(coeffs, vars_) if int(a) != 0]
    return z3.Sum(terms) if terms else z3.IntVal(0)


def quadratic_num_expr(gram: Matrix, nums):
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
    if n342.get("ledger", {}).get("picard_integral_sat") != 21:
        raise ValueError("N342 residual count regression")

    bundle = load_retained(RETAINED, "s32_n344_bundle")
    marking = load_retained(MARKING, "s32_n344_marking")
    if bundle.get("canonical_sha256") != EXPECTED_BUNDLE_CANONICAL:
        raise ValueError("retained bundle canonical regression")
    if marking.get("canonical_sha256") != EXPECTED_MARKING_CANONICAL:
        raise ValueError("retained marking canonical regression")

    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    transform = RetainedBasisPairingTransform.from_bundle(bundle)
    if transform.den != 8:
        raise ValueError("selected64 denominator regression")
    selected_labels = list(transform.certificate["selected_known_indices_1based"])
    if len(selected_labels) != 64 or sum(v > 92 for v in selected_labels) != 29:
        raise ValueError("selected64 partition regression")

    yn = [z3.Int(f"yn_{j}") for j in range(35)]
    yexpr = [z3.IntVal(1) for _ in range(29)] + yn
    B = transform.inverse_integer
    P = adapter.pairing_matrix
    gram = Matrix(bundle["picard_gram_64x64"])

    # num_expr = 8*x in the retained integral Picard basis.
    num_expr = [zsum([B[i, j] for j in range(64)], yexpr) for i in range(64)]
    pairing_num = [zsum([P[r, i] for i in range(64)], num_expr) for r in range(140)]
    square_num = quadratic_num_expr(gram, num_expr)  # = 64 * (x^T G x)

    base = z3.SolverFor("QF_NIA")
    base.set(timeout=PER_TERMINAL_TIMEOUT_MS)
    for expr in num_expr:
        base.add(expr % 8 == 0)
    for label in EXCEPTIONAL_LABELS:
        base.add(pairing_num[label - 1] == 8)
    for label in NORMAL_LABELS:
        base.add(pairing_num[label - 1] >= 0)

    normal_total_num = z3.Sum([pairing_num[label - 1] for label in NORMAL_LABELS])
    x4_num = pairing_num[X4_LABEL - 1]

    rows = []
    sat_total = unsat_total = unknown_total = 0
    for target in TARGETS:
        mass = int(target["normal_mass"])
        degree = int(target["degree"])
        genus = int(target["genus"])
        required_lower = -degree - 2 + 2 * genus
        base.push()
        for v in yn:
            base.add(v >= 0, v <= mass)
        base.add(normal_total_num == 8 * mass)

        for x4 in target["x4_values"]:
            base.push()
            base.add(x4_num == 8 * int(x4))
            base.add(square_num >= 64 * required_lower)
            result = base.check()
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
                model = base.model()
                yvals = [1] * 29 + [int(model.eval(v, model_completion=True).as_long()) for v in yn]
                if not transform.full_membership(yvals):
                    raise ValueError("SAT selected64 membership replay regression")
                xvals = transform.reconstruct_picard_basis(yvals)
                pairings = [sum(int(P[r, i]) * xvals[i] for i in range(64)) for r in range(140)]
                self_square = int((Matrix(xvals).T * gram * Matrix(xvals))[0])
                if pairings[92:] != [1] * 48:
                    raise ValueError("SAT exceptional replay regression")
                if min(pairings[:92]) < 0 or sum(pairings[:92]) != mass or pairings[X4_LABEL - 1] != int(x4):
                    raise ValueError("SAT normal/x4 replay regression")
                if self_square < required_lower:
                    raise ValueError("SAT self-square replay regression")
                witness = {
                    "selected64_pairings": yvals,
                    "picard_coordinates": xvals,
                    "all140_pairings": pairings,
                    "self_square": self_square,
                }
                row.update({
                    "verdict": "SAT_THRESHOLD",
                    "self_square": self_square,
                    "witness_sha256": csha(witness),
                })
            elif result == z3.unsat:
                unsat_total += 1
                row["verdict"] = "UNSAT_THRESHOLD"
            else:
                unknown_total += 1
                row.update({"verdict": "UNKNOWN", "reason_unknown": base.reason_unknown()})
            rows.append(row)
            base.pop()
        base.pop()

    body = {
        "schema": "STAGE32_32_01_178_N344_INTEGRAL_SELF_SQUARE_THRESHOLD_V1",
        "source_locks": {
            "n341_run_id": N341_RUN,
            "n341_job_id": N341_JOB,
            "n341_canonical_sha256": N341_CANONICAL,
            "n341_verifier_blob_sha1": N341_VERIFIER_BLOB,
            "n342_checkpoint_canonical_sha256": EXPECTED_N342_CHECKPOINT_CANONICAL,
            "retained_bundle_canonical_sha256": EXPECTED_BUNDLE_CANONICAL,
            "retained_marking_canonical_sha256": EXPECTED_MARKING_CANONICAL,
        },
        "problem": {
            "terminal_count": 21,
            "selected_normal_integer_variables": 35,
            "picard_integrality_denominator": 8,
            "all48_exceptional_pairings": "exactly 1",
            "all92_normal_pairings": "nonnegative",
            "normal_total": "19*d-5*e",
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
            "unsat_threshold_is_exact_no_integral_picard_completion_meeting_the_stated_self_square_necessary_condition": True,
            "sat_threshold_is_only_a_picard_numerical_class_not_effective_curve_existence": True,
            "unknown_or_timeout_receives_zero_pruning_credit": True,
            "n341_157_integral_unsat_not_recomputed": True,
            "n342_node_support_not_recomputed": True,
            "n350_producer_registry_unchanged": True,
            "hostile_audits_required_before_main_credit": True,
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
