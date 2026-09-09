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

SCHEMA = "STAGE32EX5_BC2_02_ONE_INDEXED_FULL178_TERMINAL_TO_PICARD64_COMPLETION_V2"
NORMAL_COUNT = 92
EXCEPTIONAL_COUNT = 48


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--prefix-checkpoint", type=Path, required=True)
    ap.add_argument("--adapter-preflight", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--solver-timeout-ms", type=int, default=120000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if args.solver_timeout_ms <= 0:
        raise ValueError("solver timeout must be positive")

    manifest, manifest_canonical = v1.load_canonical_json(args.manifest)
    rows = v1.parse_manifest_rows(manifest)
    if v1.ROW_ID not in rows or len(rows) != 178:
        raise ValueError("FULL178 manifest row population regression")

    checkpoint, checkpoint_canonical = v1.load_canonical_json(args.prefix_checkpoint)
    indexed = checkpoint["indexed_reparameterization"]
    if indexed["random_access_unrank"] is not True or indexed["inverse_rank"] is not True:
        raise ValueError("compressed terminal random-access contract regression")
    if indexed["full_terminal_materialization_required"] is not False:
        raise ValueError("compressed terminal materialization firewall regression")
    if checkpoint["exact_terminal_family"]["assignment_order_known_labels_1based"] != v1.EXPECTED_ASSIGNMENT_ORDER:
        raise ValueError("compressed terminal label-order regression")
    if list(v1.KNOWN_LABEL_ORDER) != v1.EXPECTED_ASSIGNMENT_ORDER:
        raise ValueError("runtime pairing-prefix label-order regression")

    adapter_preflight, adapter_preflight_canonical = v1.load_canonical_json(args.adapter_preflight)
    if adapter_preflight["next_exact_unit"]["id"] != "BC2_02_ONE_INDEXED_FULL178_TERMINAL_TO_PICARD64_COMPLETION_PROTOTYPE":
        raise ValueError("BC2-02 preflight next-unit regression")
    if adapter_preflight["preflight_findings"]["direct_index_to_z_shortcut_authorized"] is not False:
        raise ValueError("unsafe direct terminal-index to z shortcut became authorized")

    indexer = v1.CompressedTerminalIndexer(v1.EXCEPTIONAL_MASS, v1.DEGREE)
    if indexer.terminal_count <= v1.TERMINAL_RANK:
        raise ValueError("representative compressed terminal rank outside family")
    terminal = tuple(int(x) for x in indexer.unrank(v1.TERMINAL_RANK))
    if indexer.rank(terminal) != v1.TERMINAL_RANK:
        raise ValueError("compressed terminal rank/unrank replay regression")

    bundle = v1.load_retained(args.retained, "s32ex5_bc2_02_indexed_picard_v2")
    marking = v1.load_retained(args.marking, "s32ex5_bc2_02_indexed_marking_v2")
    data = v1.reconstruct_translation_data(marking, bundle)
    adapter = data["adapter"]
    bridge = data["bridge"]
    if adapter.pairing_matrix.shape != (v1.ALL140_COUNT, v1.PICARD_RANK):
        raise ValueError("all140 pairing matrix shape regression")
    if data["C"].shape != (5, v1.PICARD_RANK) or data["K"].shape != (v1.PICARD_RANK, v1.ANTI_RANK):
        raise ValueError("Reynolds projection/kernel shape regression")

    bridge_cert = bridge.certificate
    if bridge_cert.get("mass_identity_exact_on_picard64") is not True:
        raise ValueError("Picard64 mass identity source lock regression")
    if bridge_cert.get("mass_identity") != "normal_total + 5*exceptional_total = 19*degree":
        raise ValueError("Picard64 mass identity formula regression")
    normal_mass = 19 * v1.DEGREE - 5 * v1.EXCEPTIONAL_MASS
    if normal_mass != 132:
        raise ValueError("bounded prototype normal mass regression")

    # V2 is mathematically equivalent to V1 for fixed (d,e): the DirectPicardSliceBridge
    # proves normal_total + 5*exceptional_total = 19*degree identically on Picard64.
    # Therefore normal_total=132 and exceptional_total=4 are redundant exact equalities;
    # with nonnegativity they also justify explicit per-pairing upper bounds.  These are
    # solver-propagation aids only, not new mathematical filters.
    xvars = [Int(f"x_{j}") for j in range(v1.PICARD_RANK)]
    solver = SolverFor("QF_LIA")
    solver.set(timeout=args.solver_timeout_ms)
    pairings = []
    for i in range(v1.ALL140_COUNT):
        expr = v1.linear_expr(adapter.pairing_matrix.row(i), xvars)
        pairings.append(expr)
        if i < NORMAL_COUNT:
            solver.add(expr >= 0, expr <= normal_mass)
        else:
            solver.add(expr >= 0, expr <= v1.EXCEPTIONAL_MASS)

    degree_expr = v1.linear_expr(bridge.degree_functional, xvars)
    exceptional_mass_expr = v1.linear_expr(bridge.exceptional_mass_functional, xvars)
    solver.add(degree_expr == v1.DEGREE)
    solver.add(exceptional_mass_expr == v1.EXCEPTIONAL_MASS)
    solver.add(sum(pairings[:NORMAL_COUNT]) == normal_mass)
    solver.add(sum(pairings[NORMAL_COUNT:]) == v1.EXCEPTIONAL_MASS)

    terminal_constraints = []
    for label, value in zip(v1.EXPECTED_ASSIGNMENT_ORDER, terminal):
        idx = int(label) - 1
        solver.add(pairings[idx] == int(value))
        terminal_constraints.append({
            "known_label_1based": int(label),
            "all140_index_0based": idx,
            "pairing": int(value),
        })

    result = solver.check()
    result_status = "UNKNOWN"
    witness_r_reduced = None
    completion = None
    target = {
        "row_id": v1.ROW_ID,
        "genus": v1.GENUS,
        "degree": v1.DEGREE,
        "e": v1.EXCEPTIONAL_MASS,
        "terminal_rank": v1.TERMINAL_RANK,
        "terminal_pairings": list(terminal),
    }

    if result == sat:
        result_status = "SAT"
        model = solver.model()
        x = Matrix([int(model.eval(var, model_completion=True).as_long()) for var in xvars])
        x_values = v1.vector_int(x)
        exact_pairings = adapter.pairing_matrix * x
        pairing_values = v1.vector_int(exact_pairings)
        if min(pairing_values) < 0:
            raise ValueError("SAT witness violates all140 nonnegativity")
        if sum(pairing_values[:NORMAL_COUNT]) != normal_mass:
            raise ValueError("SAT witness normal-mass replay regression")
        if sum(pairing_values[NORMAL_COUNT:]) != v1.EXCEPTIONAL_MASS:
            raise ValueError("SAT witness exceptional-mass replay regression")
        for item in terminal_constraints:
            if pairing_values[item["all140_index_0based"]] != item["pairing"]:
                raise ValueError("SAT witness violates indexed terminal pairing")

        d_actual = v1.evaluate_functional(bridge.degree_functional, x_values)
        e_actual = v1.evaluate_functional(bridge.exceptional_mass_functional, x_values)
        a_actual = v1.evaluate_functional(bridge.first_normal_half_functional, x_values)
        if (d_actual, e_actual) != (v1.DEGREE, v1.EXCEPTIONAL_MASS):
            raise ValueError("SAT witness violates exact d/e slice")

        z = data["C"] * x
        z_values = v1.vector_int(z)
        x0 = data["x0_map"] * z
        delta = x - x0
        original_t, params = data["K"].gauss_jordan_solve(delta)
        if params.rows != 0:
            raise ValueError("anti-fixed translation unexpectedly non-unique")
        if any(sympy.denom(value) != 1 for value in original_t):
            raise ValueError("Picard64 completion does not have integral 59D translation")
        original_t = Matrix([int(value) for value in original_t])
        if data["K"] * original_t != delta:
            raise ValueError("59D translation reconstruction regression")

        M = data["M"]
        pivots = tuple(int(value) for value in data["pivot_rows"])
        selected_M = M.extract(list(pivots), list(range(v1.ANTI_RANK)))
        reduced_rows, Trow = selected_M.T.lll_transform()
        if reduced_rows != Trow * selected_M.T:
            raise ValueError("LLL reduced-coordinate transform regression")
        U = Trow.T
        if abs(int(U.det())) != 1:
            raise ValueError("reduced-coordinate transform is not unimodular")
        reduced_t = U.inv() * original_t
        if any(sympy.denom(value) != 1 for value in reduced_t):
            raise ValueError("unimodular reduced translation became nonintegral")
        reduced_t = Matrix([int(value) for value in reduced_t])
        witness_r_reduced = v1.vector_int(reduced_t)
        if len(witness_r_reduced) != v1.ANTI_RANK:
            raise ValueError("reduced 59D witness length regression")
        if x0 + data["K"] * U * reduced_t != x:
            raise ValueError("reduced 59D witness does not reconstruct Picard64 completion")

        gram = Matrix(bundle["picard_gram_64x64"])
        raw_selfsq = (x.T * gram * x)[0, 0]
        if sympy.denom(raw_selfsq) != 1:
            raise ValueError("Picard self-intersection became nonintegral")
        selfsq = int(raw_selfsq)
        lower = -v1.DEGREE - 2 + 2 * v1.GENUS
        required_support = math.ceil((v1.DEGREE - 16 * v1.GENUS + 16) / 4)
        exceptional_support = sum(1 for value in pairing_values[NORMAL_COUNT:] if value > 0)

        target.update({"a": a_actual, "z": z_values})
        completion = {
            "picard_coordinates": x_values,
            "picard_coordinates_sha256": v1.csha(x_values),
            "all140_pairings": pairing_values,
            "all140_pairings_sha256": v1.csha(pairing_values),
            "all140_nonnegative": True,
            "normal_mass": normal_mass,
            "exceptional_mass": e_actual,
            "degree": d_actual,
            "first_normal_half_a": a_actual,
            "projection_z": z_values,
            "projection_z_equals_C_times_picard": True,
            "original_59d_translation_sha256": v1.csha(v1.vector_int(original_t)),
            "reduced_59d_translation_sha256": v1.csha(witness_r_reduced),
            "reduced_59d_reconstructs_same_picard64": True,
            "self_intersection": selfsq,
            "project_native_self_intersection_lower_formula": "-d-2+2g",
            "project_native_self_intersection_lower_bound": lower,
            "passes_project_native_self_intersection_lower_bound": selfsq >= lower,
            "positive_exceptional_support": exceptional_support,
            "bijective_node_support_required_lower_bound": required_support,
            "passes_bijective_node_support_lower_bound": exceptional_support >= required_support,
        }
    elif result == unsat:
        result_status = "UNSAT"
    elif result == unknown:
        result_status = "UNKNOWN"
    else:
        raise ValueError(f"unexpected Z3 status: {result}")

    payload = {
        "schema": SCHEMA,
        "stage": "32EX5",
        "leaf": "BC2-02",
        "unit": "BC2_02_ONE_INDEXED_FULL178_TERMINAL_TO_PICARD64_COMPLETION_PROTOTYPE_V2",
        "status": (
            "PASS_ONE_INDEXED_TERMINAL_EXACT_PICARD64_COMPLETION_AND_59D_PROJECTION"
            if result_status == "SAT"
            else f"PASS_BOUNDED_PROTOTYPE_{result_status}_NO_COMPLETION_CREDIT"
        ),
        "source_locks": {
            "manifest": str(args.manifest),
            "manifest_canonical_sha256": manifest_canonical,
            "prefix_checkpoint": str(args.prefix_checkpoint),
            "prefix_checkpoint_canonical_sha256": checkpoint_canonical,
            "adapter_preflight": str(args.adapter_preflight),
            "adapter_preflight_canonical_sha256": adapter_preflight_canonical,
            "retained_bundle_canonical_sha256": bundle.get("canonical_sha256"),
            "retained_marking_canonical_sha256": marking.get("canonical_sha256"),
            "direct_picard_slice_bridge_certificate_sha256": bridge_cert.get("canonical_sha256_without_this_field"),
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
        "exact_completion_problem": {
            "solver": "Z3_QF_LIA",
            "z3_version": get_version_string(),
            "solver_timeout_ms": args.solver_timeout_ms,
            "picard_integer_variable_count": v1.PICARD_RANK,
            "all140_pairing_nonnegativity_enforced": True,
            "degree_equality_enforced": True,
            "exceptional_mass_equality_enforced": True,
            "indexed_11_pairing_equalities_enforced": True,
            "redundant_exact_normal_mass_equality_enforced": True,
            "redundant_exact_exceptional_mass_pairing_sum_enforced": True,
            "normal_pairing_upper_bound": normal_mass,
            "exceptional_pairing_upper_bound": v1.EXCEPTIONAL_MASS,
            "mass_identity_formula": bridge_cert["mass_identity"],
            "mass_identity_exact_on_picard64": True,
            "v2_constraints_semantically_equivalent_to_v1_fixed_d_e_problem": True,
            "21az_fixed_projection_prism_imported": False,
            "21bk_21bh_21bi_21bj_chain_bands_imported": False,
            "self_intersection_used_to_authorize_solver_sat": False,
            "result": result_status,
            "reason_unknown": solver.reason_unknown() if result_status == "UNKNOWN" else None,
        },
        "target": target,
        "result": {
            "status": result_status,
            "witness_r_reduced": witness_r_reduced,
            "completion": completion,
        },
        "semantics": {
            "indexed_terminal_is_not_assumed_to_determine_z": True,
            "z_is_computed_only_after_exact_picard64_completion": True,
            "sat_is_one_exact_integral_numerical_picard_completion_only": True,
            "sat_is_not_effective_integral_curve_existence": True,
            "one_terminal_result_is_not_full178_completion": True,
            "v1_timeout_is_not_unsat": True,
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
        "solver_result": result_status,
        "row_id": v1.ROW_ID,
        "e": v1.EXCEPTIONAL_MASS,
        "terminal_rank": v1.TERMINAL_RANK,
        "terminal_count": int(indexer.terminal_count),
        "normal_mass": normal_mass,
        "projection_z": target.get("z"),
        "self_intersection": completion.get("self_intersection") if completion else None,
        "self_intersection_pass": completion.get("passes_project_native_self_intersection_lower_bound") if completion else None,
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
