#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import math
from pathlib import Path

import sympy
import z3
from sympy import Matrix, Rational

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
N345_PATH = HERE.parent / "N345/verify_n345_kernel14_integral_self_square.py"

N345_RUN_ID = 34429852662
N345_VERIFY_JOB_ID = 102722838215
N345_LEDGER_JOB_ID = 102724064514
N345_CANONICAL = "0b5eb496404395574f85e0f5cbf47101691566ea6e153b43e75a71fbecbb672d"
N345_VERIFIER_BLOB = "61094d69c20dfd1d47c5a94aab435c5976eb6c5b"
N345_LEDGER = "SAT=8 UNSAT=0 UNKNOWN=13"
UNKNOWN_TARGETS = {
    "g0-d176": [3, 7, 15, 27, 39],
    "g1-d192": [3, 7, 11, 15, 19, 27, 31, 35],
}
PER_TERMINAL_TIMEOUT_MS = 15000


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import: {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def floor_sqrt_rational(value: Rational) -> int:
    value = Rational(value)
    if value < 0:
        raise ValueError("negative rational square root")
    p, q = int(value.p), int(value.q)
    n = math.isqrt(p // q) if p >= q else 0
    while (n + 1) * (n + 1) * q <= p:
        n += 1
    while n * n * q > p:
        n -= 1
    return n


def ceil_sqrt_int(value: int) -> int:
    if value < 0:
        raise ValueError("negative integer square root")
    r = math.isqrt(value)
    return r if r * r == value else r + 1


def lcm_denominators(values) -> int:
    den = 1
    for value in values:
        den = math.lcm(den, int(Rational(value).q))
    return den


def qeval(gram: Matrix, xvals: list[int]) -> int:
    x = Matrix(xvals)
    return int((x.T * gram * x)[0])


def main() -> None:
    n345 = load_module(N345_PATH, "s32_n346_n345")
    bundle = n345.load_retained(n345.RETAINED, "s32_n346_bundle")
    marking = n345.load_retained(n345.MARKING, "s32_n346_marking")
    if bundle.get("canonical_sha256") != n345.EXPECTED_BUNDLE_CANONICAL:
        raise ValueError("retained bundle canonical regression")
    if marking.get("canonical_sha256") != n345.EXPECTED_MARKING_CANONICAL:
        raise ValueError("retained marking canonical regression")

    adapter = n345.HperpIntegralPairingAdapter.from_retained(marking, bundle)
    P = adapter.pairing_matrix
    gram = Matrix(bundle["picard_gram_64x64"])
    normal_total_row = Matrix([[sum(int(P[r, c]) for r in range(92)) for c in range(64)]])
    exceptional_rows = P.extract([label - 1 for label in n345.EXCEPTIONAL_LABELS], list(range(64)))
    x4_row = P.extract([n345.X4_LABEL - 1], list(range(64)))
    A = normal_total_row.col_join(exceptional_rows).col_join(x4_row)
    if A.shape != (50, 64) or int(A.rank()) != 50:
        raise ValueError("N346 equality matrix rank regression")

    _, pivots = A.rref()
    pivot_columns = list(pivots)
    free_columns = [j for j in range(64) if j not in pivot_columns]
    if free_columns != [7, 39, 47, 52, 53, 55, 56, 57, 58, 59, 60, 61, 62, 63]:
        raise ValueError(f"N346 free-column regression: {free_columns}")
    Ap = A.extract(list(range(50)), pivot_columns)
    Af = A.extract(list(range(50)), free_columns)
    Ap_inv = Ap.inv()
    M = Ap_inv * Af
    affine_denominator = lcm_denominators(list(Ap_inv) + list(M))
    if affine_denominator != 304:
        raise ValueError(f"N346 affine denominator regression: {affine_denominator}")
    scaled_M = M * affine_denominator
    if any(sympy.denom(v) != 1 for v in scaled_M):
        raise ValueError("N346 scaled kernel coefficient regression")

    # The quadratic Hessian on the 14 free coordinates is target-independent.
    C = Matrix.zeros(64, 14)
    for j, column in enumerate(free_columns):
        C[column, j] = 1
    for i, column in enumerate(pivot_columns):
        for j in range(14):
            C[column, j] = -M[i, j]
    H = C.T * gram * C
    K = -H
    if K != K.T:
        raise ValueError("N346 restricted positive form symmetry regression")
    leading_minors = [Rational(K[:i, :i].det()) for i in range(1, 15)]
    if not all(v > 0 for v in leading_minors):
        raise ValueError("N346 restricted form is not positive definite")

    k_den = lcm_denominators(list(K))
    Kint = K * k_den
    if any(sympy.denom(v) != 1 for v in Kint):
        raise ValueError("N346 integralized restricted form regression")
    row_weights = [sum(abs(int(Kint[i, j])) for j in range(14)) for i in range(14)]
    root_weights = [ceil_sqrt_int(w) for w in row_weights]
    if min(root_weights) <= 0:
        raise ValueError("N346 invalid cross-polytope weights")

    target_meta = {t["row_id"]: t for t in n345.TARGETS}
    expected_count = sum(len(v) for v in UNKNOWN_TARGETS.values())
    if expected_count != 13:
        raise ValueError("N346 unknown target count regression")

    rows = []
    witness_count = 0
    unresolved_count = 0
    for row_id, x4_values in UNKNOWN_TARGETS.items():
        target = target_meta[row_id]
        mass = int(target["normal_mass"])
        degree = int(target["degree"])
        genus = int(target["genus"])
        lower = -degree - 2 + 2 * genus
        for x4 in x4_values:
            b = Matrix([mass] + [1] * 48 + [int(x4)])
            ppart = Ap_inv * b
            a = Matrix.zeros(64, 1)
            for i, column in enumerate(pivot_columns):
                a[column, 0] = ppart[i, 0]

            linear = 2 * C.T * gram * a
            const = Rational((a.T * gram * a)[0])
            Kinv = K.inv()
            center = Kinv * linear / 2
            qmax = Rational(const + (linear.T * Kinv * linear)[0] / 4)
            radius_budget = Rational(qmax - lower)
            if radius_budget <= 0:
                raise ValueError(f"N346 contradicts N343 real survival at {row_id} x4={x4}")

            # Exact inner cross-polytope certificate:
            # d^T K d <= (sum_i ceil(sqrt(W_i))*|d_i|)^2 / k_den.
            # Therefore sum_i weight_i*|d_i| <= floor(sqrt(R*k_den))
            # is a sufficient linear condition for q(t) >= lower.
            budget = floor_sqrt_rational(radius_budget * k_den)
            center_den = lcm_denominators(list(center))
            center_nums = [int(Rational(center[i]).p * (center_den // int(Rational(center[i]).q))) for i in range(14)]

            tvars = [z3.Int(f"t_{row_id}_{x4}_{j}") for j in range(14)]
            scaled_x = [None] * 64
            for j, column in enumerate(free_columns):
                scaled_x[column] = affine_denominator * tvars[j]
            scaled_ppart = ppart * affine_denominator
            for i, column in enumerate(pivot_columns):
                const_num = int(scaled_ppart[i, 0])
                coeffs = [-int(scaled_M[i, j]) for j in range(14)]
                terms = [z3.IntVal(const_num)] + [coeffs[j] * tvars[j] for j in range(14) if coeffs[j]]
                scaled_x[column] = z3.Sum(terms)

            solver = z3.SolverFor("QF_LIA")
            solver.set(timeout=PER_TERMINAL_TIMEOUT_MS)
            for column in pivot_columns:
                solver.add(scaled_x[column] % affine_denominator == 0)
            for label in n345.NORMAL_LABELS:
                expr = z3.Sum([int(P[label - 1, i]) * scaled_x[i] for i in range(64) if int(P[label - 1, i])])
                solver.add(expr >= 0, expr <= affine_denominator * mass)

            abs_terms = []
            for j, tv in enumerate(tvars):
                delta_num = center_den * tv - center_nums[j]
                abs_num = z3.If(delta_num >= 0, delta_num, -delta_num)
                abs_terms.append(root_weights[j] * abs_num)
            solver.add(z3.Sum(abs_terms) <= budget * center_den)

            result = solver.check()
            out = {
                "row_id": row_id,
                "g": genus,
                "d": degree,
                "e": int(target["e"]),
                "x4": int(x4),
                "required_self_square_lower": lower,
                "continuous_qmax": str(qmax),
                "crosspolytope_budget": budget,
                "center_denominator": center_den,
            }
            if result == z3.sat:
                model = solver.model()
                tvals = [int(model.eval(v, model_completion=True).as_long()) for v in tvars]
                xvals = [0] * 64
                for j, column in enumerate(free_columns):
                    xvals[column] = tvals[j]
                for i, column in enumerate(pivot_columns):
                    num = int(scaled_ppart[i, 0]) - sum(int(scaled_M[i, j]) * tvals[j] for j in range(14))
                    if num % affine_denominator:
                        raise ValueError("N346 pivot integrality replay regression")
                    xvals[column] = num // affine_denominator
                pairings = [sum(int(P[r, i]) * xvals[i] for i in range(64)) for r in range(140)]
                self_square = qeval(gram, xvals)
                if pairings[92:] != [1] * 48:
                    raise ValueError("N346 exceptional replay regression")
                if min(pairings[:92]) < 0 or sum(pairings[:92]) != mass:
                    raise ValueError("N346 normal replay regression")
                if pairings[n345.X4_LABEL - 1] != int(x4):
                    raise ValueError("N346 x4 replay regression")
                if self_square < lower:
                    raise ValueError("N346 inner-polytope sufficiency/replay regression")
                witness = {
                    "free_columns_0based": free_columns,
                    "free_values": tvals,
                    "picard_coordinates": xvals,
                    "all140_pairings": pairings,
                    "self_square": self_square,
                }
                out.update({
                    "verdict": "SAT_EXACT_INNER_CROSSPOLYTOPE_WITNESS",
                    "self_square": self_square,
                    "witness_sha256": csha(witness),
                })
                witness_count += 1
            else:
                out.update({
                    "verdict": "UNRESOLVED_NO_INNER_CROSSPOLYTOPE_WITNESS",
                    "lia_status": str(result),
                    "reason_unknown": solver.reason_unknown() if result == z3.unknown else None,
                })
                unresolved_count += 1
            rows.append(out)

    body = {
        "schema": "STAGE32_32_01_178_N346_INNER_CROSSPOLYTOPE_WITNESS_V1",
        "source_locks": {
            "n345_run_id": N345_RUN_ID,
            "n345_verify_job_id": N345_VERIFY_JOB_ID,
            "n345_ledger_job_id": N345_LEDGER_JOB_ID,
            "n345_canonical_sha256": N345_CANONICAL,
            "n345_verifier_blob_sha1": N345_VERIFIER_BLOB,
            "n345_observed_ledger": N345_LEDGER,
            "n345_unknown_targets": UNKNOWN_TARGETS,
        },
        "exact_reduction": {
            "free_integer_coordinates": 14,
            "free_columns_0based": free_columns,
            "affine_denominator": affine_denominator,
            "restricted_positive_form_common_denominator": k_den,
            "inner_region": "weighted L1 cross-polytope rigorously contained in q(t)>=threshold ellipsoid",
            "solver_logic": "QF_LIA only; nonlinear inequality is not delegated to the solver",
            "per_terminal_timeout_ms": PER_TERMINAL_TIMEOUT_MS,
        },
        "aggregate": {
            "input_unknown_count": expected_count,
            "exact_sat_witness_count": witness_count,
            "unresolved_count": unresolved_count,
            "exact_unsat_credit_count": 0,
        },
        "rows": rows,
        "semantics": {
            "sat_witnesses_are_exactly_replayed_against_picard_pairings_and_self_square": True,
            "no_inner_polytope_witness_does_not_imply_full_ellipsoid_unsat": True,
            "unresolved_receives_zero_pruning_credit": True,
            "n350_producer_registry_unchanged": True,
            "full178_complete": False,
            "effectivity_credit": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "merge_authorized": False,
        },
    }
    print(json.dumps({**body, "canonical_sha256_without_this_field": csha(body)}, sort_keys=True))


if __name__ == "__main__":
    main()
