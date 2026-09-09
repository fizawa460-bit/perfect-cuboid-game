#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import sympy
from sympy import Matrix
from z3 import Int, SolverFor, get_version_string, sat, unknown, unsat

import bc2_02_one_indexed_full178_terminal_to_picard64_completion as v1
import bc2_02_one_indexed_full178_terminal_exceptional_mass2_branched_exact as parent
from pairing_prefix_engine import INDLIST

SCHEMA = "STAGE32EX5_BC2_02_RANK0_UNKNOWN53_FULL_EXCEPTIONAL_PARTITION_EXACT_V1"
EXPECTED_CHECKPOINT_CANONICAL = "2467b5479881c10a2e28c3d822787acefabef867540a3544d46026655ae81ed7"
NORMAL_COUNT = 92
EXCEPTIONAL_COUNT = 48
EXPECTED_SELECTED_EXCEPTIONAL_COUNT = 29
EXPECTED_UNSELECTED_EXCEPTIONAL_COUNT = 19
EXPECTED_UNKNOWN_PARENT_COUNT = 53
EXPECTED_REFINED_SUBCASE_COUNT = 377


def vector_int(v: Matrix) -> list[int]:
    if v.cols != 1:
        raise ValueError("expected column vector")
    return [int(v[i, 0]) for i in range(v.rows)]


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def one_hot(n: int) -> list[tuple[int, ...]]:
    out = []
    for i in range(n):
        row = [0] * n
        row[i] = 1
        out.append(tuple(row))
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--prefix-checkpoint", type=Path, required=True)
    ap.add_argument("--adapter-preflight", type=Path, required=True)
    ap.add_argument("--prior-v1", type=Path, required=True)
    ap.add_argument("--branched-checkpoint", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--subcase-timeout-ms", type=int, default=1000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if args.subcase_timeout_ms <= 0:
        raise ValueError("subcase timeout must be positive")

    manifest, manifest_canonical = v1.load_canonical_json(args.manifest)
    prefix, prefix_canonical = v1.load_canonical_json(args.prefix_checkpoint)
    preflight, preflight_canonical = v1.load_canonical_json(args.adapter_preflight)
    prior, prior_canonical = v1.load_canonical_json(args.prior_v1)
    checkpoint, checkpoint_canonical = v1.load_canonical_json(args.branched_checkpoint)
    if checkpoint_canonical != EXPECTED_CHECKPOINT_CANONICAL:
        raise ValueError("branched exact checkpoint canonical regression")
    locks = checkpoint["source_locks"]
    for got, expected, name in (
        (manifest_canonical, locks["manifest_canonical_sha256"], "manifest"),
        (prefix_canonical, locks["prefix_checkpoint_canonical_sha256"], "prefix"),
        (preflight_canonical, locks["adapter_preflight_canonical_sha256"], "adapter preflight"),
        (prior_canonical, locks["prior_v1_unknown_canonical_sha256"], "prior V1"),
    ):
        if got != expected:
            raise ValueError(f"{name} source-lock regression")
    if checkpoint["result"]["aggregate_result"] != "UNKNOWN":
        raise ValueError("expected retained branched UNKNOWN checkpoint")
    unknown_parent_ids = [int(q) for q in checkpoint["result"]["unknown_branch_ids"]]
    if len(unknown_parent_ids) != EXPECTED_UNKNOWN_PARENT_COUNT or len(set(unknown_parent_ids)) != EXPECTED_UNKNOWN_PARENT_COUNT:
        raise ValueError("unknown parent branch-id regression")
    if checkpoint["result"]["exact_unsat_branch_count"] != 157:
        raise ValueError("retained parent exact-UNSAT count regression")

    rows = v1.parse_manifest_rows(manifest)
    if len(rows) != 178 or v1.ROW_ID not in rows:
        raise ValueError("FULL178 manifest row population regression")
    if prefix["exact_terminal_family"]["assignment_order_known_labels_1based"] != v1.EXPECTED_ASSIGNMENT_ORDER:
        raise ValueError("terminal assignment-order regression")
    if preflight["preflight_findings"]["direct_index_to_z_shortcut_authorized"] is not False:
        raise ValueError("unsafe terminal-index to z shortcut became authorized")
    if prior["result"]["status"] != "UNKNOWN":
        raise ValueError("prior V1 is not UNKNOWN")

    indexer = v1.CompressedTerminalIndexer(v1.EXCEPTIONAL_MASS, v1.DEGREE)
    terminal = tuple(int(q) for q in indexer.unrank(v1.TERMINAL_RANK))
    if indexer.rank(terminal) != v1.TERMINAL_RANK:
        raise ValueError("terminal rank/unrank regression")
    if list(terminal) != checkpoint["indexed_terminal"]["terminal_pairings"]:
        raise ValueError("rank0 terminal pairing regression")

    bundle = v1.load_retained(args.retained, "s32ex5_bc2_02_unknown53_full_exceptional_picard")
    marking = v1.load_retained(args.marking, "s32ex5_bc2_02_unknown53_full_exceptional_marking")
    if bundle["canonical_sha256"] != locks["retained_bundle_canonical_sha256"]:
        raise ValueError("retained bundle source-lock regression")
    if marking["canonical_sha256"] != locks["retained_marking_canonical_sha256"]:
        raise ValueError("retained marking source-lock regression")
    data = v1.reconstruct_translation_data(marking, bundle)
    adapter = data["adapter"]
    bridge = data["bridge"]
    P = adapter.pairing_matrix
    if P.shape != (v1.ALL140_COUNT, v1.PICARD_RANK):
        raise ValueError("all140 pairing matrix shape regression")

    selected_labels = [int(label) for label in INDLIST]
    selected_indices = [label - 1 for label in selected_labels]
    Psel = P.extract(selected_indices, list(range(v1.PICARD_RANK)))
    if Psel.det() == 0:
        raise ValueError("selected64 pairing matrix singular")
    Pinv = Psel.inv()
    den = parent.lcm_denominator(Pinv)
    if den != locks["selected64_inverse_denominator"]:
        raise ValueError("selected64 inverse denominator regression")
    Binv_q = Pinv * den
    if any(sympy.denom(q) != 1 for q in Binv_q):
        raise ValueError("selected64 inverse scaling regression")
    Binv = Matrix([[int(Binv_q[i, j]) for j in range(Binv_q.cols)] for i in range(Binv_q.rows)])
    if Psel * Binv != den * Matrix.eye(v1.PICARD_RANK):
        raise ValueError("selected64 inverse exact reconstruction regression")
    Anum_q = P * Binv
    if any(sympy.denom(q) != 1 for q in Anum_q):
        raise ValueError("all140 selected-coordinate map became nonintegral")
    Anum = Matrix([[int(Anum_q[i, j]) for j in range(Anum_q.cols)] for i in range(Anum_q.rows)])

    terminal_by_label = {int(label): int(value) for label, value in zip(v1.EXPECTED_ASSIGNMENT_ORDER, terminal)}
    selected_exceptional_labels = [label for label in selected_labels if label > NORMAL_COUNT]
    if len(selected_exceptional_labels) != EXPECTED_SELECTED_EXCEPTIONAL_COUNT:
        raise ValueError("selected exceptional count regression")
    remaining_selected_exceptional_labels = [
        label for label in selected_exceptional_labels if label not in terminal_by_label
    ]
    if remaining_selected_exceptional_labels != checkpoint["branch_partition"]["remaining_selected_exceptional_labels_1based"]:
        raise ValueError("remaining selected exceptional label regression")
    unselected_exceptional_labels = [
        label for label in range(NORMAL_COUNT + 1, NORMAL_COUNT + EXCEPTIONAL_COUNT + 1)
        if label not in selected_exceptional_labels
    ]
    if len(unselected_exceptional_labels) != EXPECTED_UNSELECTED_EXCEPTIONAL_COUNT:
        raise ValueError("unselected exceptional count regression")

    assignments = parent.enumerate_residual_mass_le2(len(remaining_selected_exceptional_labels))
    if len(assignments) != parent.EXPECTED_BRANCH_COUNT:
        raise ValueError("parent assignment enumeration regression")
    if csha([parent.sparse_assignment(a) for a in assignments]) != checkpoint["branch_partition"]["assignment_stream_sha256"]:
        raise ValueError("parent assignment stream regression")
    parent_mass_counts = {1: 0, 2: 0}
    for branch_id in unknown_parent_ids:
        m = sum(assignments[branch_id])
        if m not in parent_mass_counts:
            raise ValueError("unknown parent mass outside expected 1/2 layers")
        parent_mass_counts[m] += 1
    if parent_mass_counts != {1: 18, 2: 35}:
        raise ValueError(f"unknown parent mass-layer regression: {parent_mass_counts}")

    selected_pos = {label: selected_labels.index(label) for label in selected_labels}
    remaining_selected_positions = [selected_pos[label] for label in remaining_selected_exceptional_labels]
    normal_mass = 19 * v1.DEGREE - 5 * v1.EXCEPTIONAL_MASS
    if normal_mass != 132:
        raise ValueError("normal mass regression")

    y = [Int(f"y_{j}") for j in range(v1.PICARD_RANK)]
    p = [Int(f"p_{i}") for i in range(v1.ALL140_COUNT)]
    solver = SolverFor("QF_LIA")
    solver.set(timeout=args.subcase_timeout_ms)
    for j, label in enumerate(selected_labels):
        ub = v1.EXCEPTIONAL_MASS if label > NORMAL_COUNT else normal_mass
        solver.add(y[j] >= 0, y[j] <= ub)
        solver.add(p[label - 1] == y[j])
    for i in range(v1.ALL140_COUNT):
        ub = normal_mass if i < NORMAL_COUNT else v1.EXCEPTIONAL_MASS
        solver.add(p[i] >= 0, p[i] <= ub)
        solver.add(den * p[i] == sum(int(Anum[i, j]) * y[j] for j in range(v1.PICARD_RANK)))
    for i in range(v1.PICARD_RANK):
        numerator = sum(int(Binv[i, j]) * y[j] for j in range(v1.PICARD_RANK))
        solver.add(numerator % den == 0)
    solver.add(sum(p[:NORMAL_COUNT]) == normal_mass)
    solver.add(sum(p[NORMAL_COUNT:]) == v1.EXCEPTIONAL_MASS)
    for label, value in terminal_by_label.items():
        solver.add(p[label - 1] == value)
    solver.add(sum(y[pos] for pos in remaining_selected_positions) <= 2)

    subcase_records: list[dict] = []
    unsat_count = 0
    unknown_count = 0
    sat_record = None
    sat_model = None
    expected_subcases = 0

    for parent_id in unknown_parent_ids:
        assignment = assignments[parent_id]
        selected_mass = int(sum(assignment))
        unselected_mass = 2 - selected_mass
        if unselected_mass == 0:
            subassignments = [tuple(0 for _ in unselected_exceptional_labels)]
        elif unselected_mass == 1:
            subassignments = one_hot(len(unselected_exceptional_labels))
        else:
            raise ValueError("unexpected unselected exceptional residual mass")
        expected_subcases += len(subassignments)

        solver.push()
        try:
            for pos, value in zip(remaining_selected_positions, assignment):
                solver.add(y[pos] == int(value))
            for sub_id, unselected_assignment in enumerate(subassignments):
                solver.push()
                try:
                    for label, value in zip(unselected_exceptional_labels, unselected_assignment):
                        solver.add(p[label - 1] == int(value))
                    result = solver.check()
                    record = {
                        "parent_branch_id": int(parent_id),
                        "parent_selected_residual_mass": selected_mass,
                        "parent_assignment_sparse": parent.sparse_assignment(assignment),
                        "unselected_exceptional_residual_mass": unselected_mass,
                        "subcase_id": int(sub_id),
                        "unselected_assignment_sparse_labels_1based": [
                            [int(label), int(value)] for label, value in zip(unselected_exceptional_labels, unselected_assignment) if value
                        ],
                    }
                    if result == sat:
                        record["status"] = "SAT"
                        sat_record = record
                        sat_model = solver.model()
                        subcase_records.append(record)
                        break
                    if result == unsat:
                        record["status"] = "UNSAT"
                        unsat_count += 1
                    elif result == unknown:
                        record["status"] = "UNKNOWN"
                        record["reason_unknown"] = solver.reason_unknown()
                        unknown_count += 1
                    else:
                        raise ValueError(f"unexpected solver result: {result}")
                    subcase_records.append(record)
                finally:
                    solver.pop()
            if sat_record is not None:
                break
        finally:
            solver.pop()

    if expected_subcases != EXPECTED_REFINED_SUBCASE_COUNT:
        raise ValueError(f"refined subcase count regression: {expected_subcases}")
    aggregate = "SAT" if sat_record is not None else (
        "UNSAT" if unsat_count == EXPECTED_REFINED_SUBCASE_COUNT and unknown_count == 0 else "UNKNOWN"
    )
    if aggregate == "UNSAT" and len(subcase_records) != EXPECTED_REFINED_SUBCASE_COUNT:
        raise ValueError("rank0 UNSAT requires all 377 refinement subcases exact UNSAT")
    if aggregate == "UNKNOWN" and (len(subcase_records) != EXPECTED_REFINED_SUBCASE_COUNT or unknown_count == 0):
        raise ValueError("refinement UNKNOWN accounting regression")

    target = {
        "row_id": v1.ROW_ID,
        "genus": v1.GENUS,
        "degree": v1.DEGREE,
        "e": v1.EXCEPTIONAL_MASS,
        "terminal_rank": v1.TERMINAL_RANK,
        "terminal_pairings": list(terminal),
    }
    witness_r_reduced = None
    completion = None
    if aggregate == "SAT":
        if sat_model is None:
            raise ValueError("SAT refinement missing model")
        yv = [int(sat_model.eval(q, model_completion=True).as_long()) for q in y]
        pv = [int(sat_model.eval(q, model_completion=True).as_long()) for q in p]
        xnum = Binv * Matrix(yv)
        if any(int(q) % den for q in xnum):
            raise ValueError("SAT selected64 vector left integral Picard64 image")
        x = Matrix([int(q) // den for q in xnum])
        xv = vector_int(x)
        if vector_int(P * x) != pv:
            raise ValueError("SAT all140 replay regression")
        if min(pv) < 0 or sum(pv[:NORMAL_COUNT]) != normal_mass or sum(pv[NORMAL_COUNT:]) != v1.EXCEPTIONAL_MASS:
            raise ValueError("SAT mass/nonnegativity replay regression")
        d_actual = v1.evaluate_functional(bridge.degree_functional, xv)
        e_actual = v1.evaluate_functional(bridge.exceptional_mass_functional, xv)
        a_actual = v1.evaluate_functional(bridge.first_normal_half_functional, xv)
        if (d_actual, e_actual) != (v1.DEGREE, v1.EXCEPTIONAL_MASS):
            raise ValueError("SAT d/e slice replay regression")
        z = data["C"] * x
        zv = vector_int(z)
        x0 = data["x0_map"] * z
        delta = x - x0
        t, params = data["K"].gauss_jordan_solve(delta)
        if params.rows != 0 or any(sympy.denom(q) != 1 for q in t):
            raise ValueError("SAT Picard64 completion lacks integral 59D translation")
        t = Matrix([int(q) for q in t])
        M = data["M"]
        pivots = tuple(int(q) for q in data["pivot_rows"])
        selected_M = M.extract(list(pivots), list(range(v1.ANTI_RANK)))
        reduced_rows, Trow = selected_M.T.lll_transform()
        if reduced_rows != Trow * selected_M.T:
            raise ValueError("LLL transform regression")
        U = Trow.T
        if abs(int(U.det())) != 1:
            raise ValueError("reduced-coordinate transform non-unimodular")
        r = U.inv() * t
        if any(sympy.denom(q) != 1 for q in r):
            raise ValueError("reduced 59D witness nonintegral")
        r = Matrix([int(q) for q in r])
        witness_r_reduced = vector_int(r)
        if x0 + data["K"] * U * r != x:
            raise ValueError("reduced 59D witness reconstruction regression")
        target.update({"a": int(a_actual), "z": zv})
        completion = {
            "selected64_pairings": yv,
            "picard_coordinates": xv,
            "all140_pairings": pv,
            "all140_nonnegative": True,
            "first_normal_half_a": int(a_actual),
            "projection_z": zv,
            "positive_exceptional_support": sum(1 for q in pv[NORMAL_COUNT:] if q > 0),
            "full_exceptional_pairing_vector_fixed_in_sat_subcase": True,
        }

    status = (
        "PASS_RANK0_EXACT_PICARD64_COMPLETION_AFTER_FULL_EXCEPTIONAL_PARTITION" if aggregate == "SAT" else
        "PASS_RANK0_TERMINAL_EXACT_UNSAT_AFTER_157_PLUS_377_PARTITION" if aggregate == "UNSAT" else
        "PASS_RANK0_FULL_EXCEPTIONAL_PARTITION_UNKNOWN_NO_TERMINAL_CREDIT"
    )
    payload = {
        "schema": SCHEMA,
        "stage": "32EX5",
        "leaf": "BC2-02",
        "unit": "BC2_02_RANK0_UNKNOWN53_FULL_EXCEPTIONAL_PARTITION_EXACT",
        "status": status,
        "source_locks": {
            "branched_checkpoint_canonical_sha256": checkpoint_canonical,
            "manifest_canonical_sha256": manifest_canonical,
            "prefix_checkpoint_canonical_sha256": prefix_canonical,
            "adapter_preflight_canonical_sha256": preflight_canonical,
            "prior_v1_unknown_canonical_sha256": prior_canonical,
            "retained_bundle_canonical_sha256": bundle["canonical_sha256"],
            "retained_marking_canonical_sha256": marking["canonical_sha256"],
            "selected64_inverse_denominator": den,
        },
        "indexed_terminal": checkpoint["indexed_terminal"],
        "partition": {
            "retained_parent_exact_unsat_count": 157,
            "retained_parent_unknown_count": 53,
            "unknown_parent_branch_ids": unknown_parent_ids,
            "selected_exceptional_count": len(selected_exceptional_labels),
            "unselected_exceptional_count": len(unselected_exceptional_labels),
            "unselected_exceptional_labels_1based": unselected_exceptional_labels,
            "mass2_unknown_parent_count": 35,
            "mass2_refinement_semantics": "remaining unselected exceptional mass=0; all 19 unselected exceptional pairings fixed to zero",
            "mass1_unknown_parent_count": 18,
            "mass1_refinement_semantics": "remaining unselected exceptional mass=1; exactly one of 19 unselected exceptional pairings equals one",
            "expected_refined_subcase_count_formula": "35 + 18*19 = 377",
            "expected_refined_subcase_count": EXPECTED_REFINED_SUBCASE_COUNT,
            "partition_complete_for_all_53_parent_unknown_solution_sets": True,
            "new_mathematical_condition_added": False,
        },
        "subcase_records": subcase_records,
        "exact_result": {
            "aggregate_result": aggregate,
            "tested_refined_subcase_count": len(subcase_records),
            "exact_unsat_refined_subcase_count": unsat_count,
            "unknown_refined_subcase_count": unknown_count,
            "sat_subcase": sat_record,
            "z3_version": get_version_string(),
            "subcase_timeout_ms": args.subcase_timeout_ms,
            "rank0_terminal_exact_unsat_authorized": aggregate == "UNSAT",
            "rank0_terminal_exact_sat_completion_found": aggregate == "SAT",
        },
        "target": target,
        "result": {
            "status": aggregate,
            "completion": completion,
            "witness_r_reduced": witness_r_reduced,
        },
        "semantics": {
            "157_parent_exact_unsat_branches_not_rerun": True,
            "all_48_exceptional_pairings_fixed_in_every_refined_subcase": True,
            "unknown_refined_subcase_prevents_rank0_unsat_credit": True,
            "rank0_unsat_is_one_indexed_terminal_only": True,
            "rank0_sat_is_one_exact_integral_numerical_picard_completion_only": True,
            "sat_is_not_effective_integral_curve_existence": True,
            "one_terminal_result_is_not_FULL178_completion": True,
        },
        "firewalls": {
            "FULL178_complete": False,
            "stage32_main_credit": False,
            "receiver_credit": False,
            "Q602_excluded": False,
            "O210_excluded": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
            "merge_authorized": False,
        },
    }
    payload["exact_result"]["subcase_status_stream_sha256"] = csha([
        [r["parent_branch_id"], r["subcase_id"], r["status"]] for r in subcase_records
    ])
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "aggregate_result": aggregate,
        "tested_refined_subcases": len(subcase_records),
        "exact_unsat_refined_subcases": unsat_count,
        "unknown_refined_subcases": unknown_count,
        "sat_parent_branch": None if sat_record is None else sat_record["parent_branch_id"],
        "sat_subcase_id": None if sat_record is None else sat_record["subcase_id"],
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
