#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import sympy
from sympy import Matrix
from z3 import Int, SolverFor, get_version_string, sat, unknown, unsat

import bc2_02_one_indexed_full178_terminal_to_picard64_completion as v1
from pairing_prefix_engine import INDLIST

SCHEMA = "STAGE32EX5_BC2_02_ONE_INDEXED_FULL178_TERMINAL_PAIRING_COORDINATE_COMPLETION_V1"
NORMAL_COUNT = 92
EXCEPTIONAL_COUNT = 48


def matrix_payload(m: Matrix) -> list[list[int]]:
    return [[int(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]


def lcm_denominator(m: Matrix) -> int:
    den = 1
    for value in m:
        den = math.lcm(den, int(sympy.denom(value)))
    return den


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--prefix-checkpoint", type=Path, required=True)
    ap.add_argument("--adapter-preflight", type=Path, required=True)
    ap.add_argument("--prior-v1", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--solver-timeout-ms", type=int, default=120000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if args.solver_timeout_ms <= 0:
        raise ValueError("solver timeout must be positive")

    manifest, manifest_canonical = v1.load_canonical_json(args.manifest)
    if v1.ROW_ID not in v1.parse_manifest_rows(manifest):
        raise ValueError("representative row absent from FULL178 manifest")
    checkpoint, checkpoint_canonical = v1.load_canonical_json(args.prefix_checkpoint)
    adapter_preflight, adapter_preflight_canonical = v1.load_canonical_json(args.adapter_preflight)
    prior, prior_canonical = v1.load_canonical_json(args.prior_v1)
    if prior["schema"] != v1.SCHEMA or prior["result"]["status"] != "UNKNOWN":
        raise ValueError("expected retained V1 UNKNOWN prototype")
    if prior["exact_completion_problem"]["reason_unknown"] != "timeout":
        raise ValueError("retained V1 UNKNOWN is not timeout")
    if adapter_preflight["preflight_findings"]["direct_index_to_z_shortcut_authorized"] is not False:
        raise ValueError("unsafe direct index-to-z shortcut became authorized")
    if checkpoint["exact_terminal_family"]["assignment_order_known_labels_1based"] != v1.EXPECTED_ASSIGNMENT_ORDER:
        raise ValueError("compressed terminal label-order regression")

    indexer = v1.CompressedTerminalIndexer(v1.EXCEPTIONAL_MASS, v1.DEGREE)
    terminal = tuple(int(q) for q in indexer.unrank(v1.TERMINAL_RANK))
    if indexer.rank(terminal) != v1.TERMINAL_RANK:
        raise ValueError("compressed terminal rank/unrank regression")
    if list(terminal) != prior["indexed_terminal"]["pairings"]:
        raise ValueError("retained V1 terminal pairing regression")

    bundle = v1.load_retained(args.retained, "s32ex5_bc2_02_paircoord_picard")
    marking = v1.load_retained(args.marking, "s32ex5_bc2_02_paircoord_marking")
    data = v1.reconstruct_translation_data(marking, bundle)
    adapter = data["adapter"]
    bridge = data["bridge"]
    P = adapter.pairing_matrix
    if P.shape != (v1.ALL140_COUNT, v1.PICARD_RANK):
        raise ValueError("all140 pairing matrix shape regression")

    selected_indices = [int(label) - 1 for label in INDLIST]
    if len(selected_indices) != v1.PICARD_RANK or len(set(selected_indices)) != v1.PICARD_RANK:
        raise ValueError("selected64 label-set regression")
    Psel = P.extract(selected_indices, list(range(v1.PICARD_RANK)))
    det = int(Psel.det())
    if det == 0:
        raise ValueError("actual retained-coordinate selected64 pairing matrix is singular")
    Pinv = Psel.inv()
    den = lcm_denominator(Pinv)
    Binv = Pinv * den
    if any(sympy.denom(q) != 1 for q in Binv):
        raise ValueError("selected64 inverse scaling regression")
    Binv = Matrix([[int(Binv[i, j]) for j in range(Binv.cols)] for i in range(Binv.rows)])
    if Psel * Binv != den * Matrix.eye(v1.PICARD_RANK):
        raise ValueError("actual selected64 inverse reconstruction regression")

    # Every all140 pairing is an exact rational linear form in selected64
    # pairings y.  Multiplying by the same denominator makes all links integer.
    Anum = P * Binv
    if any(sympy.denom(q) != 1 for q in Anum):
        raise ValueError("all140 selected-pairing numerator map became nonintegral")
    Anum = Matrix([[int(Anum[i, j]) for j in range(Anum.cols)] for i in range(Anum.rows)])
    if Anum.extract(selected_indices, list(range(v1.PICARD_RANK))) != den * Matrix.eye(v1.PICARD_RANK):
        raise ValueError("selected64 all140 numerator identity regression")

    normal_mass = 19 * v1.DEGREE - 5 * v1.EXCEPTIONAL_MASS
    if normal_mass != 132:
        raise ValueError("representative normal-mass regression")
    bridge_cert = bridge.certificate
    if bridge_cert.get("mass_identity_exact_on_picard64") is not True:
        raise ValueError("Picard64 mass identity source-lock regression")

    # Bounded pairing-coordinate formulation. y_j are the actual selected64
    # pairings, not Picard basis coordinates. p_i are all140 pairings.  The
    # divisibility conditions Binv*y == 0 mod den are exactly equivalent to
    # existence of an integral retained-Picard64 coordinate vector x=Binv*y/den.
    # No new mathematical filter is introduced over V1.
    y = [Int(f"y_{j}") for j in range(v1.PICARD_RANK)]
    p = [Int(f"p_{i}") for i in range(v1.ALL140_COUNT)]
    solver = SolverFor("QF_LIA")
    solver.set(timeout=args.solver_timeout_ms)

    selected_labels = [int(label) for label in INDLIST]
    for j, label in enumerate(selected_labels):
        ub = v1.EXCEPTIONAL_MASS if label > NORMAL_COUNT else normal_mass
        solver.add(y[j] >= 0, y[j] <= ub)
        solver.add(p[label - 1] == y[j])

    for i in range(v1.ALL140_COUNT):
        ub = normal_mass if i < NORMAL_COUNT else v1.EXCEPTIONAL_MASS
        solver.add(p[i] >= 0, p[i] <= ub)
        solver.add(
            den * p[i] == sum(int(Anum[i, j]) * y[j] for j in range(v1.PICARD_RANK))
        )

    # Exact Picard-lattice membership of selected64 pairing vector.
    for i in range(v1.PICARD_RANK):
        numerator = sum(int(Binv[i, j]) * y[j] for j in range(v1.PICARD_RANK))
        solver.add(numerator % den == 0)

    solver.add(sum(p[:NORMAL_COUNT]) == normal_mass)
    solver.add(sum(p[NORMAL_COUNT:]) == v1.EXCEPTIONAL_MASS)

    terminal_constraints = []
    selected_label_set = set(selected_labels)
    if not set(v1.EXPECTED_ASSIGNMENT_ORDER).issubset(selected_label_set):
        raise ValueError("indexed terminal labels are not all contained in selected64 coordinate set")
    for label, value in zip(v1.EXPECTED_ASSIGNMENT_ORDER, terminal):
        solver.add(p[int(label) - 1] == int(value))
        terminal_constraints.append({
            "known_label_1based": int(label),
            "all140_index_0based": int(label) - 1,
            "pairing": int(value),
        })

    result = solver.check()
    status = "UNKNOWN"
    completion = None
    witness_r_reduced = None
    target = {
        "row_id": v1.ROW_ID,
        "genus": v1.GENUS,
        "degree": v1.DEGREE,
        "e": v1.EXCEPTIONAL_MASS,
        "terminal_rank": v1.TERMINAL_RANK,
        "terminal_pairings": list(terminal),
    }

    if result == sat:
        status = "SAT"
        model = solver.model()
        yv = [int(model.eval(q, model_completion=True).as_long()) for q in y]
        pv = [int(model.eval(q, model_completion=True).as_long()) for q in p]
        xnum = Binv * Matrix(yv)
        if any(int(q) % den for q in xnum):
            raise ValueError("SAT selected pairing vector is not in integral Picard64 image")
        x = Matrix([int(q) // den for q in xnum])
        xv = v1.vector_int(x)
        if v1.vector_int(P * x) != pv:
            raise ValueError("SAT all140 pairing replay from Picard64 regression")
        if min(pv) < 0 or sum(pv[:NORMAL_COUNT]) != normal_mass or sum(pv[NORMAL_COUNT:]) != v1.EXCEPTIONAL_MASS:
            raise ValueError("SAT mass/nonnegativity replay regression")
        for item in terminal_constraints:
            if pv[item["all140_index_0based"]] != item["pairing"]:
                raise ValueError("SAT indexed-terminal replay regression")

        d_actual = v1.evaluate_functional(bridge.degree_functional, xv)
        e_actual = v1.evaluate_functional(bridge.exceptional_mass_functional, xv)
        a_actual = v1.evaluate_functional(bridge.first_normal_half_functional, xv)
        if (d_actual, e_actual) != (v1.DEGREE, v1.EXCEPTIONAL_MASS):
            raise ValueError("SAT exact d/e slice replay regression")

        z = data["C"] * x
        zv = v1.vector_int(z)
        x0 = data["x0_map"] * z
        delta = x - x0
        t, params = data["K"].gauss_jordan_solve(delta)
        if params.rows != 0 or any(sympy.denom(q) != 1 for q in t):
            raise ValueError("SAT Picard64 completion lacks unique integral 59D translation")
        t = Matrix([int(q) for q in t])
        if data["K"] * t != delta:
            raise ValueError("59D translation reconstruction regression")

        M = data["M"]
        pivots = tuple(int(q) for q in data["pivot_rows"])
        selected_M = M.extract(list(pivots), list(range(v1.ANTI_RANK)))
        reduced_rows, Trow = selected_M.T.lll_transform()
        if reduced_rows != Trow * selected_M.T:
            raise ValueError("LLL reduced-coordinate transform regression")
        U = Trow.T
        if abs(int(U.det())) != 1:
            raise ValueError("reduced-coordinate transform is not unimodular")
        r = U.inv() * t
        if any(sympy.denom(q) != 1 for q in r):
            raise ValueError("reduced 59D witness became nonintegral")
        r = Matrix([int(q) for q in r])
        witness_r_reduced = v1.vector_int(r)
        if x0 + data["K"] * U * r != x:
            raise ValueError("reduced 59D witness reconstruction regression")

        gram = Matrix(bundle["picard_gram_64x64"])
        selfsq_q = (x.T * gram * x)[0, 0]
        if sympy.denom(selfsq_q) != 1:
            raise ValueError("Picard self-intersection became nonintegral")
        selfsq = int(selfsq_q)
        lower = -v1.DEGREE - 2 + 2 * v1.GENUS
        support = sum(1 for q in pv[NORMAL_COUNT:] if q > 0)
        support_lower = math.ceil((v1.DEGREE - 16 * v1.GENUS + 16) / 4)
        target.update({"a": a_actual, "z": zv})
        completion = {
            "selected64_pairings": yv,
            "selected64_pairings_sha256": v1.csha(yv),
            "picard_coordinates": xv,
            "picard_coordinates_sha256": v1.csha(xv),
            "all140_pairings": pv,
            "all140_pairings_sha256": v1.csha(pv),
            "all140_nonnegative": True,
            "normal_pairing_sum": sum(pv[:NORMAL_COUNT]),
            "exceptional_pairing_sum": sum(pv[NORMAL_COUNT:]),
            "first_normal_half_a": a_actual,
            "projection_z": zv,
            "projection_z_equals_C_times_picard": True,
            "original_59d_translation_sha256": v1.csha(v1.vector_int(t)),
            "reduced_59d_translation_sha256": v1.csha(witness_r_reduced),
            "reduced_59d_reconstructs_same_picard64": True,
            "self_intersection": selfsq,
            "project_native_self_intersection_lower_formula": "-d-2+2g",
            "project_native_self_intersection_lower_bound": lower,
            "passes_project_native_self_intersection_lower_bound": selfsq >= lower,
            "positive_exceptional_support": support,
            "bijective_node_support_required_lower_bound": support_lower,
            "passes_bijective_node_support_lower_bound": support >= support_lower,
        }
    elif result == unsat:
        status = "UNSAT"
    elif result == unknown:
        status = "UNKNOWN"
    else:
        raise ValueError(f"unexpected solver status: {result}")

    payload = {
        "schema": SCHEMA,
        "stage": "32EX5",
        "leaf": "BC2-02",
        "unit": "BC2_02_ONE_INDEXED_FULL178_TERMINAL_PAIRING_COORDINATE_COMPLETION",
        "status": (
            "PASS_ONE_INDEXED_TERMINAL_EXACT_PICARD64_COMPLETION_AND_59D_PROJECTION"
            if status == "SAT"
            else (
                "PASS_ONE_INDEXED_TERMINAL_EXACT_NO_PICARD64_COMPLETION"
                if status == "UNSAT"
                else "PASS_PAIRING_COORDINATE_PROTOTYPE_UNKNOWN_NO_COMPLETION_CREDIT"
            )
        ),
        "source_locks": {
            "manifest_canonical_sha256": manifest_canonical,
            "prefix_checkpoint_canonical_sha256": checkpoint_canonical,
            "adapter_preflight_canonical_sha256": adapter_preflight_canonical,
            "prior_v1_unknown_canonical_sha256": prior_canonical,
            "retained_bundle_canonical_sha256": bundle.get("canonical_sha256"),
            "retained_marking_canonical_sha256": marking.get("canonical_sha256"),
            "actual_all140_pairing_matrix_sha256": v1.csha(matrix_payload(P)),
            "actual_selected64_pairing_matrix_sha256": v1.csha(matrix_payload(Psel)),
            "actual_selected64_inverse_integer_sha256": v1.csha(matrix_payload(Binv)),
        },
        "indexed_terminal": {
            "row_id": v1.ROW_ID,
            "genus": v1.GENUS,
            "degree": v1.DEGREE,
            "e": v1.EXCEPTIONAL_MASS,
            "terminal_rank": v1.TERMINAL_RANK,
            "terminal_count_in_stratum": int(indexer.terminal_count),
            "rank_unrank_replay_exact": True,
            "assignment_order_known_labels_1based": v1.EXPECTED_ASSIGNMENT_ORDER,
            "pairings": list(terminal),
            "constraints": terminal_constraints,
        },
        "pairing_coordinate_model": {
            "selected64_labels_1based": selected_labels,
            "selected64_matrix_determinant": det,
            "selected64_inverse_denominator": den,
            "selected64_all140_numerator_identity_exact": True,
            "picard_membership_formula": "Binv*y divisible coordinatewise by den",
            "picard_membership_exact": True,
            "all140_formula": "den*p = (P*Binv)*y",
            "all140_formula_exact": True,
            "selected64_pairings_are_bounded_variables": True,
            "normal_pairing_bounds": [0, normal_mass],
            "exceptional_pairing_bounds": [0, v1.EXCEPTIONAL_MASS],
            "all_indexed_terminal_labels_are_selected64_coordinates": True,
            "new_mathematical_condition_added_over_v1": False,
        },
        "exact_completion_problem": {
            "solver": "Z3_QF_LIA",
            "z3_version": get_version_string(),
            "solver_timeout_ms": args.solver_timeout_ms,
            "result": status,
            "reason_unknown": solver.reason_unknown() if status == "UNKNOWN" else None,
            "21az_fixed_projection_prism_imported": False,
            "21bk_21bh_21bi_21bj_chain_bands_imported": False,
            "self_intersection_used_to_authorize_solver_sat": False,
        },
        "target": target,
        "result": {"status": status, "witness_r_reduced": witness_r_reduced, "completion": completion},
        "semantics": {
            "pairing_coordinate_reparameterization_is_exact": True,
            "indexed_terminal_is_not_assumed_to_determine_z": True,
            "z_is_computed_only_after_exact_picard64_completion": True,
            "sat_is_one_exact_integral_numerical_picard_completion_only": True,
            "unsat_is_one_indexed_terminal_only": True,
            "one_terminal_result_is_not_full178_completion": True,
            "sat_is_not_effective_integral_curve_existence": True,
            "prior_timeouts_are_not_unsat": True,
        },
        "firewalls": {
            "heavy_scaleout_authorized": False,
            "FULL178_complete": False,
            "receiver_credit": False,
            "stage32_main_credit": False,
            "Q602_excluded": False,
            "O210_excluded": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
            "merge_authorized": False,
        },
    }
    payload["canonical_sha256_without_this_field"] = v1.csha(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": payload["status"],
        "solver_result": status,
        "selected64_inverse_denominator": den,
        "projection_z": target.get("z"),
        "self_intersection": completion.get("self_intersection") if completion else None,
        "support": completion.get("positive_exceptional_support") if completion else None,
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
