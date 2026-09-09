#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import sympy
from sympy import Matrix
from z3 import Int, SolverFor, get_version_string, sat, unknown, unsat

ROOT = Path(__file__).resolve().parents[3]
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
sys.path.insert(0, str(RESIDUAL))

import bc2_02_one_indexed_full178_terminal_to_picard64_completion as v1
from compressed_terminal_indexer import CompressedTerminalIndexer
from diagnose_stage32_21ak_affine_2adic_membership import reconstruct_translation_data
from direct_picard_reynolds_lattice_diagnostic import csha, load_retained
from pairing_prefix_engine import RetainedBasisPairingTransform
from run_full178_prefix_work_unit import KNOWN_LABEL_ORDER

SCHEMA = "STAGE32EX5_BC2_02_ONE_INDEXED_FULL178_TERMINAL_PICARD64_BOX_BOUNDED_V2"


def ceil_div(a: int, b: int) -> int:
    return -((-int(a)) // int(b))


def linear_expr(coeffs, variables):
    return sum(int(coeffs[j]) * variables[j] for j in range(len(variables)))


def vector_int(v: Matrix) -> list[int]:
    if v.cols != 1:
        raise ValueError("expected column vector")
    return [int(v[i, 0]) for i in range(v.rows)]


def functional_value(coeffs, values: list[int]) -> int:
    return sum(int(coeffs[j]) * int(values[j]) for j in range(len(values)))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--prefix-checkpoint", type=Path, required=True)
    ap.add_argument("--adapter-preflight", type=Path, required=True)
    ap.add_argument("--prior-prototype", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--solver-timeout-ms", type=int, default=60000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if args.solver_timeout_ms <= 0:
        raise ValueError("solver timeout must be positive")

    manifest, manifest_canonical = v1.load_canonical_json(args.manifest)
    rows = v1.parse_manifest_rows(manifest)
    if v1.ROW_ID not in rows or len(rows) != 178:
        raise ValueError("FULL178 manifest row population regression")

    checkpoint, checkpoint_canonical = v1.load_canonical_json(args.prefix_checkpoint)
    if checkpoint["indexed_reparameterization"]["random_access_unrank"] is not True:
        raise ValueError("compressed terminal random-access regression")
    if checkpoint["indexed_reparameterization"]["full_terminal_materialization_required"] is not False:
        raise ValueError("materialization firewall regression")
    if checkpoint["exact_terminal_family"]["assignment_order_known_labels_1based"] != v1.EXPECTED_ASSIGNMENT_ORDER:
        raise ValueError("compressed terminal label-order regression")
    if list(KNOWN_LABEL_ORDER) != v1.EXPECTED_ASSIGNMENT_ORDER:
        raise ValueError("runtime label-order regression")

    adapter_preflight, adapter_preflight_canonical = v1.load_canonical_json(args.adapter_preflight)
    if adapter_preflight["preflight_findings"]["direct_index_to_z_shortcut_authorized"] is not False:
        raise ValueError("unsafe direct index-to-z shortcut authorized")

    prior, prior_canonical = v1.load_canonical_json(args.prior_prototype)
    if prior["schema"] != v1.SCHEMA or prior["result"]["status"] != "UNKNOWN":
        raise ValueError("expected exact prior bounded UNKNOWN prototype")
    if prior["exact_completion_problem"]["reason_unknown"] != "timeout":
        raise ValueError("prior UNKNOWN was not a timeout")
    if prior["indexed_terminal"]["row_id"] != v1.ROW_ID or prior["indexed_terminal"]["terminal_rank"] != v1.TERMINAL_RANK:
        raise ValueError("prior prototype target regression")

    indexer = CompressedTerminalIndexer(v1.EXCEPTIONAL_MASS, v1.DEGREE)
    terminal = tuple(int(x) for x in indexer.unrank(v1.TERMINAL_RANK))
    if indexer.rank(terminal) != v1.TERMINAL_RANK:
        raise ValueError("rank/unrank replay regression")
    if list(terminal) != prior["indexed_terminal"]["pairings"]:
        raise ValueError("prior terminal pairing replay regression")

    bundle = load_retained(args.retained, "s32ex5_bc2_02_box_picard")
    marking = load_retained(args.marking, "s32ex5_bc2_02_box_marking")
    data = reconstruct_translation_data(marking, bundle)
    adapter = data["adapter"]
    bridge = data["bridge"]
    transform = RetainedBasisPairingTransform.from_bundle(bundle)

    normal_mass = 19 * v1.DEGREE - 5 * v1.EXCEPTIONAL_MASS
    if normal_mass != 132:
        raise ValueError("representative normal mass regression")

    # Source-locked redundant finite box.  With all 140 pairings nonnegative,
    # exceptional_total=e and normal_total=19d-5e imply each exceptional
    # pairing lies in [0,e] and each normal pairing lies in [0,normal_mass].
    # The selected 64 pairing coordinates therefore lie in an explicit box.
    # x = inverse_integer*y/den then gives exact redundant bounds on every
    # Picard-basis coordinate.  No mathematical condition is added.
    selected_labels = [int(x) for x in transform.certificate["selected_known_indices_1based"]]
    selected_ubs = [v1.EXCEPTIONAL_MASS if label > 92 else normal_mass for label in selected_labels]
    B = transform.inverse_integer
    den = int(transform.den)
    x_bounds: list[tuple[int, int]] = []
    for i in range(v1.PICARD_RANK):
        nlo = 0
        nhi = 0
        for j, ub in enumerate(selected_ubs):
            a = int(B[i, j])
            if a < 0:
                nlo += a * ub
            elif a > 0:
                nhi += a * ub
        lo = ceil_div(nlo, den)
        hi = nhi // den
        if lo > hi:
            raise ValueError("derived Picard coordinate box is empty")
        x_bounds.append((lo, hi))

    xvars = [Int(f"x_{j}") for j in range(v1.PICARD_RANK)]
    solver = SolverFor("QF_LIA")
    solver.set(timeout=args.solver_timeout_ms)
    for j, (lo, hi) in enumerate(x_bounds):
        solver.add(xvars[j] >= lo, xvars[j] <= hi)

    pairing_exprs = []
    for i in range(v1.ALL140_COUNT):
        expr = linear_expr(adapter.pairing_matrix.row(i), xvars)
        pairing_exprs.append(expr)
        if i < 92:
            solver.add(expr >= 0, expr <= normal_mass)
        else:
            solver.add(expr >= 0, expr <= v1.EXCEPTIONAL_MASS)

    # Redundant exact mass equations are made explicit for the Presburger solver.
    solver.add(sum(pairing_exprs[:92]) == normal_mass)
    solver.add(sum(pairing_exprs[92:140]) == v1.EXCEPTIONAL_MASS)
    solver.add(linear_expr(bridge.degree_functional, xvars) == v1.DEGREE)
    solver.add(linear_expr(bridge.exceptional_mass_functional, xvars) == v1.EXCEPTIONAL_MASS)

    terminal_constraints = []
    for label, value in zip(v1.EXPECTED_ASSIGNMENT_ORDER, terminal):
        idx = int(label) - 1
        solver.add(pairing_exprs[idx] == int(value))
        terminal_constraints.append({"known_label_1based": int(label), "all140_index_0based": idx, "pairing": int(value)})

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
        x = Matrix([int(model.eval(q, model_completion=True).as_long()) for q in xvars])
        xv = vector_int(x)
        pairings = adapter.pairing_matrix * x
        pv = vector_int(pairings)
        if min(pv) < 0 or sum(pv[:92]) != normal_mass or sum(pv[92:]) != v1.EXCEPTIONAL_MASS:
            raise ValueError("SAT witness mass/nonnegativity replay regression")
        for item in terminal_constraints:
            if pv[item["all140_index_0based"]] != item["pairing"]:
                raise ValueError("SAT witness terminal replay regression")
        d_actual = functional_value(bridge.degree_functional, xv)
        e_actual = functional_value(bridge.exceptional_mass_functional, xv)
        a_actual = functional_value(bridge.first_normal_half_functional, xv)
        if (d_actual, e_actual) != (v1.DEGREE, v1.EXCEPTIONAL_MASS):
            raise ValueError("SAT witness slice replay regression")

        z = data["C"] * x
        zv = vector_int(z)
        x0 = data["x0_map"] * z
        delta = x - x0
        t, params = data["K"].gauss_jordan_solve(delta)
        if params.rows != 0 or any(sympy.denom(q) != 1 for q in t):
            raise ValueError("SAT completion lacks unique integral 59D translation")
        t = Matrix([int(q) for q in t])
        if data["K"] * t != delta:
            raise ValueError("59D translation reconstruction regression")

        M = data["M"]
        pivots = tuple(int(q) for q in data["pivot_rows"])
        selected_M = M.extract(list(pivots), list(range(v1.ANTI_RANK)))
        reduced_rows, Trow = selected_M.T.lll_transform()
        if reduced_rows != Trow * selected_M.T:
            raise ValueError("LLL transform reconstruction regression")
        U = Trow.T
        if abs(int(U.det())) != 1:
            raise ValueError("LLL transform is not unimodular")
        r = U.inv() * t
        if any(sympy.denom(q) != 1 for q in r):
            raise ValueError("reduced 59D witness became nonintegral")
        r = Matrix([int(q) for q in r])
        witness_r_reduced = vector_int(r)
        if x0 + data["K"] * U * r != x:
            raise ValueError("reduced witness reconstruction regression")

        gram = Matrix(bundle["picard_gram_64x64"])
        selfsq_q = (x.T * gram * x)[0, 0]
        if sympy.denom(selfsq_q) != 1:
            raise ValueError("self-intersection nonintegral regression")
        selfsq = int(selfsq_q)
        lower = -v1.DEGREE - 2 + 2 * v1.GENUS
        support = sum(1 for q in pv[92:] if q > 0)
        support_lower = math.ceil((v1.DEGREE - 16 * v1.GENUS + 16) / 4)
        target.update({"a": a_actual, "z": zv})
        completion = {
            "picard_coordinates": xv,
            "picard_coordinates_sha256": csha(xv),
            "all140_pairings": pv,
            "all140_pairings_sha256": csha(pv),
            "all140_nonnegative": True,
            "normal_pairing_sum": sum(pv[:92]),
            "exceptional_pairing_sum": sum(pv[92:]),
            "first_normal_half_a": a_actual,
            "projection_z": zv,
            "projection_z_equals_C_times_picard": True,
            "original_59d_translation_sha256": csha(vector_int(t)),
            "reduced_59d_translation_sha256": csha(witness_r_reduced),
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
        "unit": "BC2_02_ONE_INDEXED_FULL178_TERMINAL_TO_PICARD64_COMPLETION_PROTOTYPE_V2_BOX_BOUNDED",
        "status": (
            "PASS_ONE_INDEXED_TERMINAL_EXACT_PICARD64_COMPLETION_AND_59D_PROJECTION"
            if status == "SAT"
            else f"PASS_BOX_BOUNDED_PROTOTYPE_{status}_NO_COMPLETION_CREDIT"
        ),
        "source_locks": {
            "manifest_canonical_sha256": manifest_canonical,
            "prefix_checkpoint_canonical_sha256": checkpoint_canonical,
            "adapter_preflight_canonical_sha256": adapter_preflight_canonical,
            "prior_unknown_prototype_canonical_sha256": prior_canonical,
            "retained_bundle_canonical_sha256": bundle.get("canonical_sha256"),
            "retained_marking_canonical_sha256": marking.get("canonical_sha256"),
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
        "exact_redundant_box": {
            "normal_mass_identity": "normal_total=19*d-5*e",
            "normal_mass": normal_mass,
            "exceptional_mass": v1.EXCEPTIONAL_MASS,
            "selected_pairing_count": len(selected_labels),
            "selected_pairing_labels_1based": selected_labels,
            "selected_pairing_upper_bounds": selected_ubs,
            "picard_inverse_denominator": den,
            "picard_coordinate_bounds": [[lo, hi] for lo, hi in x_bounds],
            "picard_coordinate_box_is_logically_redundant": True,
            "all140_individual_upper_bounds_are_logically_redundant": True,
            "explicit_normal_and_exceptional_sum_equations_are_logically_redundant": True,
        },
        "exact_completion_problem": {
            "solver": "Z3_QF_LIA",
            "z3_version": get_version_string(),
            "solver_timeout_ms": args.solver_timeout_ms,
            "result": status,
            "reason_unknown": solver.reason_unknown() if status == "UNKNOWN" else None,
            "all140_pairing_nonnegativity_enforced": True,
            "degree_equality_enforced": True,
            "exceptional_mass_equality_enforced": True,
            "indexed_11_pairing_equalities_enforced": True,
            "21az_fixed_projection_prism_imported": False,
            "21bk_21bh_21bi_21bj_chain_bands_imported": False,
            "new_mathematical_condition_added_over_v1": False,
        },
        "target": target,
        "result": {"status": status, "witness_r_reduced": witness_r_reduced, "completion": completion},
        "semantics": {
            "v1_unknown_timeout_is_not_unsat": True,
            "box_bounds_are_exact_consequences_of_existing_mass_and_nonnegativity_constraints": True,
            "z_is_computed_only_after_exact_picard64_completion": True,
            "sat_is_one_exact_integral_numerical_picard_completion_only": True,
            "sat_is_not_effective_integral_curve_existence": True,
            "one_terminal_result_is_not_full178_completion": True,
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
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": payload["status"],
        "solver_result": status,
        "row_id": v1.ROW_ID,
        "terminal_rank": v1.TERMINAL_RANK,
        "projection_z": target.get("z"),
        "self_intersection": completion.get("self_intersection") if completion else None,
        "self_intersection_pass": completion.get("passes_project_native_self_intersection_lower_bound") if completion else None,
        "support": completion.get("positive_exceptional_support") if completion else None,
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
