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
N345_PATH = HERE.parent / "N345/verify_n345_kernel14_integral_self_square.py"

N346_RUN_ID = 34430511056
N346_VERIFY_JOB_ID = 102724854273
N346_LEDGER_JOB_ID = 102725527580
N346_CANONICAL = "63c7cc0d8433449dfef344f20c066ff049befe06e8b39b93ada82bd10aecc99c"
N346_VERIFIER_BLOB = "274c3cf9964a5c411735cca044630e24d9f0bf0a"
N346_LEDGER = "SAT=0 UNRESOLVED=13"
UNKNOWN_TARGETS = {
    "g0-d176": [3, 7, 15, 27, 39],
    "g1-d192": [3, 7, 11, 15, 19, 27, 31, 35],
}
RADIUS_SCHEDULE = [2, 4, 8, 16, 32, 64]
PER_CHECK_TIMEOUT_MS = 2500
MAX_CANDIDATES_PER_RADIUS = 32


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import: {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def lcm_denominators(values) -> int:
    den = 1
    for value in values:
        den = math.lcm(den, int(Rational(value).q))
    return den


def qeval(gram: Matrix, xvals: list[int]) -> int:
    x = Matrix(xvals)
    return int((x.T * gram * x)[0])


def main() -> None:
    n345 = load_module(N345_PATH, "s32_n347_n345")
    bundle = n345.load_retained(n345.RETAINED, "s32_n347_bundle")
    marking = n345.load_retained(n345.MARKING, "s32_n347_marking")
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
        raise ValueError("N347 equality matrix rank regression")

    _, pivots = A.rref()
    pivot_columns = list(pivots)
    free_columns = [j for j in range(64) if j not in pivot_columns]
    expected_free = [7, 39, 47, 52, 53, 55, 56, 57, 58, 59, 60, 61, 62, 63]
    if free_columns != expected_free:
        raise ValueError(f"N347 free-column regression: {free_columns}")

    Ap = A.extract(list(range(50)), pivot_columns)
    Af = A.extract(list(range(50)), free_columns)
    Ap_inv = Ap.inv()
    M = Ap_inv * Af
    affine_denominator = lcm_denominators(list(Ap_inv) + list(M))
    if affine_denominator != 304:
        raise ValueError(f"N347 affine denominator regression: {affine_denominator}")
    scaled_M = M * affine_denominator
    if any(sympy.denom(v) != 1 for v in scaled_M):
        raise ValueError("N347 scaled kernel coefficient regression")

    # q(t)=qmax-(t-center)^T K (t-center), with K positive definite.
    C = Matrix.zeros(64, 14)
    for j, column in enumerate(free_columns):
        C[column, j] = 1
    for i, column in enumerate(pivot_columns):
        for j in range(14):
            C[column, j] = -M[i, j]
    H = C.T * gram * C
    K = -H
    if K != K.T:
        raise ValueError("N347 restricted form symmetry regression")
    if not all(Rational(K[:i, :i].det()) > 0 for i in range(1, 15)):
        raise ValueError("N347 restricted form is not positive definite")
    Kinv = K.inv()

    target_meta = {t["row_id"]: t for t in n345.TARGETS}
    if sum(len(v) for v in UNKNOWN_TARGETS.values()) != 13:
        raise ValueError("N347 target count regression")

    rows = []
    witness_count = unresolved_count = 0
    total_candidate_replays = 0

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
            center = Kinv * linear / 2
            qmax = Rational(const + (linear.T * Kinv * linear)[0] / 4)
            if qmax < lower:
                raise ValueError(f"N347 real-survival regression at {row_id} x4={x4}")
            center_den = lcm_denominators(list(center))
            center_nums = [int(Rational(center[i]).p * (center_den // int(Rational(center[i]).q))) for i in range(14)]

            scaled_ppart = ppart * affine_denominator
            if any(sympy.denom(v) != 1 for v in scaled_ppart):
                raise ValueError("N347 scaled particular regression")

            found = None
            probe_ledger = []
            row_replays = 0

            for radius in RADIUS_SCHEDULE:
                tvars = [z3.Int(f"t_{row_id}_{x4}_{radius}_{j}") for j in range(14)]
                scaled_x = [None] * 64
                for j, column in enumerate(free_columns):
                    scaled_x[column] = affine_denominator * tvars[j]
                for i, column in enumerate(pivot_columns):
                    terms = [z3.IntVal(int(scaled_ppart[i, 0]))]
                    terms.extend(-int(scaled_M[i, j]) * tvars[j] for j in range(14) if int(scaled_M[i, j]))
                    scaled_x[column] = z3.Sum(terms)

                solver = z3.SolverFor("QF_LIA")
                solver.set(timeout=PER_CHECK_TIMEOUT_MS)
                for column in pivot_columns:
                    solver.add(scaled_x[column] % affine_denominator == 0)
                for label in n345.NORMAL_LABELS:
                    expr = z3.Sum([int(P[label - 1, i]) * scaled_x[i] for i in range(64) if int(P[label - 1, i])])
                    solver.add(expr >= 0, expr <= affine_denominator * mass)
                # Deterministic Chebyshev box around the exact real q-maximum center.
                for j, tv in enumerate(tvars):
                    delta = center_den * tv - center_nums[j]
                    solver.add(delta <= radius * center_den, delta >= -radius * center_den)

                status = solver.check()
                radius_entry = {"radius": radius, "initial_status": str(status), "candidate_replays": 0}
                if status == z3.unknown:
                    radius_entry["reason_unknown"] = solver.reason_unknown()
                    probe_ledger.append(radius_entry)
                    continue
                if status == z3.unsat:
                    probe_ledger.append(radius_entry)
                    continue

                # Enumerate a bounded deterministic set of exact LIA-feasible points.
                # Every candidate is replayed against the original 64D Picard data and
                # the quadratic threshold; lack of a hit never receives UNSAT credit.
                for _ in range(MAX_CANDIDATES_PER_RADIUS):
                    model = solver.model()
                    tvals = [int(model.eval(v, model_completion=True).as_long()) for v in tvars]
                    xvals = [0] * 64
                    for j, column in enumerate(free_columns):
                        xvals[column] = tvals[j]
                    for i, column in enumerate(pivot_columns):
                        num = int(scaled_ppart[i, 0]) - sum(int(scaled_M[i, j]) * tvals[j] for j in range(14))
                        if num % affine_denominator:
                            raise ValueError("N347 pivot integrality replay regression")
                        xvals[column] = num // affine_denominator

                    pairings = [sum(int(P[r, i]) * xvals[i] for i in range(64)) for r in range(140)]
                    self_square = qeval(gram, xvals)
                    if pairings[92:] != [1] * 48:
                        raise ValueError("N347 exceptional replay regression")
                    if min(pairings[:92]) < 0 or sum(pairings[:92]) != mass:
                        raise ValueError("N347 normal replay regression")
                    if pairings[n345.X4_LABEL - 1] != int(x4):
                        raise ValueError("N347 x4 replay regression")

                    row_replays += 1
                    total_candidate_replays += 1
                    radius_entry["candidate_replays"] += 1
                    if self_square >= lower:
                        witness = {
                            "free_columns_0based": free_columns,
                            "free_values": tvals,
                            "picard_coordinates": xvals,
                            "all140_pairings": pairings,
                            "self_square": self_square,
                        }
                        found = {
                            "radius": radius,
                            "self_square": self_square,
                            "witness_sha256": csha(witness),
                        }
                        break

                    solver.add(z3.Or([v != z3.IntVal(val) for v, val in zip(tvars, tvals)]))
                    status = solver.check()
                    if status != z3.sat:
                        if status == z3.unknown:
                            radius_entry["enumeration_reason_unknown"] = solver.reason_unknown()
                        break

                probe_ledger.append(radius_entry)
                if found is not None:
                    break

            out = {
                "row_id": row_id,
                "g": genus,
                "d": degree,
                "e": int(target["e"]),
                "x4": int(x4),
                "required_self_square_lower": lower,
                "continuous_qmax": str(qmax),
                "center_denominator": center_den,
                "candidate_replays": row_replays,
                "probe_ledger": probe_ledger,
            }
            if found is not None:
                witness_count += 1
                out.update({"verdict": "SAT_EXACT_CENTER_BOX_WITNESS", **found})
            else:
                unresolved_count += 1
                out["verdict"] = "UNRESOLVED_NO_CENTER_BOX_WITNESS"
            rows.append(out)

    body = {
        "schema": "STAGE32_32_01_178_N347_CENTER_BOX_WITNESS_V1",
        "source_locks": {
            "n346_run_id": N346_RUN_ID,
            "n346_verify_job_id": N346_VERIFY_JOB_ID,
            "n346_ledger_job_id": N346_LEDGER_JOB_ID,
            "n346_canonical_sha256": N346_CANONICAL,
            "n346_verifier_blob_sha1": N346_VERIFIER_BLOB,
            "n346_observed_ledger": N346_LEDGER,
            "n346_unresolved_targets": UNKNOWN_TARGETS,
            "n345_canonical_sha256": n345.N345_CANONICAL if hasattr(n345, "N345_CANONICAL") else "0b5eb496404395574f85e0f5cbf47101691566ea6e153b43e75a71fbecbb672d",
        },
        "exact_reduction": {
            "free_integer_coordinates": 14,
            "free_columns_0based": free_columns,
            "affine_denominator": affine_denominator,
            "search_geometry": "deterministic expanding L-infinity boxes around exact real q-maximum center",
            "radius_schedule": RADIUS_SCHEDULE,
            "solver_logic": "QF_LIA only",
            "per_check_timeout_ms": PER_CHECK_TIMEOUT_MS,
            "max_candidate_replays_per_radius": MAX_CANDIDATES_PER_RADIUS,
            "quadratic_condition": "checked only by exact 64D replay after each LIA candidate",
        },
        "aggregate": {
            "input_unresolved_count": 13,
            "exact_sat_witness_count": witness_count,
            "unresolved_count": unresolved_count,
            "exact_unsat_credit_count": 0,
            "total_candidate_replays": total_candidate_replays,
        },
        "rows": rows,
        "semantics": {
            "sat_witnesses_are_exactly_replayed_against_picard_pairings_and_self_square": True,
            "no_center_box_witness_does_not_imply_ellipsoid_unsat": True,
            "unresolved_receives_zero_pruning_credit": True,
            "sat_is_only_a_picard_numerical_class_not_effective_curve_existence": True,
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
