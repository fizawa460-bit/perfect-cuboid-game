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
from pairing_prefix_engine import INDLIST

SCHEMA = "STAGE32EX5_BC2_02_ONE_INDEXED_FULL178_TERMINAL_EXCEPTIONAL_MASS2_BRANCHED_EXACT_V1"
NORMAL_COUNT = 92
EXCEPTIONAL_COUNT = 48
EXPECTED_RESIDUAL_EXCEPTIONAL_MASS = 2
EXPECTED_REMAINING_SELECTED_EXCEPTIONAL_COUNT = 19
EXPECTED_BRANCH_COUNT = 210


def lcm_denominator(m: Matrix) -> int:
    den = 1
    for value in m:
        den = math.lcm(den, int(sympy.denom(value)))
    return den


def vector_int(v: Matrix) -> list[int]:
    if v.cols != 1:
        raise ValueError("expected column vector")
    return [int(v[i, 0]) for i in range(v.rows)]


def sparse_assignment(values: tuple[int, ...]) -> list[list[int]]:
    return [[i, int(v)] for i, v in enumerate(values) if v]


def enumerate_residual_mass_le2(n: int) -> list[tuple[int, ...]]:
    out: list[tuple[int, ...]] = [tuple(0 for _ in range(n))]
    for i in range(n):
        row = [0] * n
        row[i] = 1
        out.append(tuple(row))
    for i in range(n):
        row = [0] * n
        row[i] = 2
        out.append(tuple(row))
        for j in range(i + 1, n):
            row = [0] * n
            row[i] = 1
            row[j] = 1
            out.append(tuple(row))
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--prefix-checkpoint", type=Path, required=True)
    ap.add_argument("--adapter-preflight", type=Path, required=True)
    ap.add_argument("--prior-v1", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--branch-timeout-ms", type=int, default=1500)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if args.branch_timeout_ms <= 0:
        raise ValueError("branch timeout must be positive")

    manifest, manifest_canonical = v1.load_canonical_json(args.manifest)
    rows = v1.parse_manifest_rows(manifest)
    if v1.ROW_ID not in rows or len(rows) != 178:
        raise ValueError("FULL178 manifest row population regression")
    checkpoint, checkpoint_canonical = v1.load_canonical_json(args.prefix_checkpoint)
    adapter_preflight, adapter_preflight_canonical = v1.load_canonical_json(args.adapter_preflight)
    prior, prior_canonical = v1.load_canonical_json(args.prior_v1)
    if prior["schema"] != v1.SCHEMA or prior["result"]["status"] != "UNKNOWN":
        raise ValueError("expected retained V1 UNKNOWN prototype")
    if prior["exact_completion_problem"]["reason_unknown"] != "timeout":
        raise ValueError("retained V1 UNKNOWN is not timeout")
    if adapter_preflight["preflight_findings"]["direct_index_to_z_shortcut_authorized"] is not False:
        raise ValueError("unsafe direct terminal-index to z shortcut became authorized")
    if checkpoint["exact_terminal_family"]["assignment_order_known_labels_1based"] != v1.EXPECTED_ASSIGNMENT_ORDER:
        raise ValueError("compressed terminal label-order regression")

    indexer = v1.CompressedTerminalIndexer(v1.EXCEPTIONAL_MASS, v1.DEGREE)
    terminal = tuple(int(q) for q in indexer.unrank(v1.TERMINAL_RANK))
    if indexer.rank(terminal) != v1.TERMINAL_RANK:
        raise ValueError("compressed terminal rank/unrank regression")
    if list(terminal) != prior["indexed_terminal"]["pairings"]:
        raise ValueError("retained V1 terminal pairing regression")

    bundle = v1.load_retained(args.retained, "s32ex5_bc2_02_branch_picard")
    marking = v1.load_retained(args.marking, "s32ex5_bc2_02_branch_marking")
    data = v1.reconstruct_translation_data(marking, bundle)
    adapter = data["adapter"]
    bridge = data["bridge"]
    P = adapter.pairing_matrix
    if P.shape != (v1.ALL140_COUNT, v1.PICARD_RANK):
        raise ValueError("all140 pairing matrix shape regression")

    selected_labels = [int(label) for label in INDLIST]
    selected_indices = [label - 1 for label in selected_labels]
    if len(selected_labels) != v1.PICARD_RANK or len(set(selected_labels)) != v1.PICARD_RANK:
        raise ValueError("selected64 label-set regression")
    Psel = P.extract(selected_indices, list(range(v1.PICARD_RANK)))
    if int(Psel.det()) == 0:
        raise ValueError("actual selected64 pairing matrix is singular")
    Pinv = Psel.inv()
    den = lcm_denominator(Pinv)
    Binv_q = Pinv * den
    if any(sympy.denom(q) != 1 for q in Binv_q):
        raise ValueError("selected64 inverse scaling regression")
    Binv = Matrix([[int(Binv_q[i, j]) for j in range(Binv_q.cols)] for i in range(Binv_q.rows)])
    if Psel * Binv != den * Matrix.eye(v1.PICARD_RANK):
        raise ValueError("actual selected64 inverse reconstruction regression")
    Anum_q = P * Binv
    if any(sympy.denom(q) != 1 for q in Anum_q):
        raise ValueError("all140 selected-pairing map became nonintegral")
    Anum = Matrix([[int(Anum_q[i, j]) for j in range(Anum_q.cols)] for i in range(Anum_q.rows)])
    if Anum.extract(selected_indices, list(range(v1.PICARD_RANK))) != den * Matrix.eye(v1.PICARD_RANK):
        raise ValueError("selected64 numerator identity regression")

    normal_mass = 19 * v1.DEGREE - 5 * v1.EXCEPTIONAL_MASS
    if normal_mass != 132:
        raise ValueError("representative normal-mass regression")
    bridge_cert = bridge.certificate
    if bridge_cert.get("mass_identity_exact_on_picard64") is not True:
        raise ValueError("Picard64 mass identity source-lock regression")

    terminal_by_label = {int(label): int(value) for label, value in zip(v1.EXPECTED_ASSIGNMENT_ORDER, terminal)}
    terminal_exceptional_labels = sorted(label for label in terminal_by_label if label > NORMAL_COUNT)
    fixed_exceptional_mass = sum(terminal_by_label[label] for label in terminal_exceptional_labels)
    residual_exceptional_mass = v1.EXCEPTIONAL_MASS - fixed_exceptional_mass
    if residual_exceptional_mass != EXPECTED_RESIDUAL_EXCEPTIONAL_MASS:
        raise ValueError("residual exceptional mass regression")

    selected_exceptional_labels = [label for label in selected_labels if label > NORMAL_COUNT]
    remaining_selected_exceptional_labels = [
        label for label in selected_exceptional_labels if label not in terminal_by_label
    ]
    if len(remaining_selected_exceptional_labels) != EXPECTED_REMAINING_SELECTED_EXCEPTIONAL_COUNT:
        raise ValueError(
            f"remaining selected exceptional count regression: {len(remaining_selected_exceptional_labels)}"
        )
    selected_pos = {label: selected_labels.index(label) for label in selected_labels}
    remaining_selected_positions = [selected_pos[label] for label in remaining_selected_exceptional_labels]

    assignments = enumerate_residual_mass_le2(len(remaining_selected_exceptional_labels))
    if len(assignments) != EXPECTED_BRANCH_COUNT:
        raise ValueError(f"branch count regression: {len(assignments)}")
    if sorted(sum(a) for a in assignments).count(0) != 1:
        raise ValueError("zero-mass branch coverage regression")
    if sum(sum(a) == 1 for a in assignments) != 19:
        raise ValueError("unit-mass branch coverage regression")
    if sum(sum(a) == 2 for a in assignments) != 190:
        raise ValueError("double-mass branch coverage regression")
    assignment_stream = [sparse_assignment(a) for a in assignments]
    assignment_sha256 = hashlib.sha256(
        json.dumps(assignment_stream, separators=(",", ":")).encode()
    ).hexdigest()

    y = [Int(f"y_{j}") for j in range(v1.PICARD_RANK)]
    p = [Int(f"p_{i}") for i in range(v1.ALL140_COUNT)]
    solver = SolverFor("QF_LIA")
    solver.set(timeout=args.branch_timeout_ms)

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
    for i in range(v1.PICARD_RANK):
        numerator = sum(int(Binv[i, j]) * y[j] for j in range(v1.PICARD_RANK))
        solver.add(numerator % den == 0)
    solver.add(sum(p[:NORMAL_COUNT]) == normal_mass)
    solver.add(sum(p[NORMAL_COUNT:]) == v1.EXCEPTIONAL_MASS)
    for label, value in terminal_by_label.items():
        solver.add(p[label - 1] == value)

    # This inequality is derivable from global exceptional mass=4,
    # nonnegativity, and the terminal exceptional contribution=2. It is only
    # a propagation aid and does not alter the V1 solution set.
    solver.add(sum(y[pos] for pos in remaining_selected_positions) <= residual_exceptional_mass)

    branch_records: list[dict] = []
    unsat_count = 0
    unknown_count = 0
    sat_branch = None
    sat_model = None

    for branch_id, assignment in enumerate(assignments):
        solver.push()
        try:
            for pos, value in zip(remaining_selected_positions, assignment):
                solver.add(y[pos] == int(value))
            result = solver.check()
            record = {
                "branch_id": branch_id,
                "selected_residual_mass": int(sum(assignment)),
                "assignment_sparse": sparse_assignment(assignment),
            }
            if result == sat:
                record["status"] = "SAT"
                sat_branch = record
                sat_model = solver.model()
                branch_records.append(record)
                break
            if result == unsat:
                record["status"] = "UNSAT"
                unsat_count += 1
            elif result == unknown:
                record["status"] = "UNKNOWN"
                record["reason_unknown"] = solver.reason_unknown()
                unknown_count += 1
            else:
                raise ValueError(f"unexpected solver status: {result}")
            branch_records.append(record)
        finally:
            solver.pop()

    aggregate_status = "SAT" if sat_branch is not None else (
        "UNSAT" if unsat_count == EXPECTED_BRANCH_COUNT else "UNKNOWN"
    )
    if aggregate_status == "UNSAT":
        if len(branch_records) != EXPECTED_BRANCH_COUNT or unknown_count != 0:
            raise ValueError("aggregate UNSAT requires all 210 branches exact UNSAT")
    if aggregate_status == "UNKNOWN":
        if len(branch_records) != EXPECTED_BRANCH_COUNT or unknown_count == 0:
            raise ValueError("aggregate UNKNOWN accounting regression")

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

    if aggregate_status == "SAT":
        if sat_model is None:
            raise ValueError("SAT branch missing model")
        # The model object remains valid after pop. Reconstruct selected64,
        # Picard64, all140, z and the integral 59D reduced witness exactly.
        yv = [int(sat_model.eval(q, model_completion=True).as_long()) for q in y]
        pv = [int(sat_model.eval(q, model_completion=True).as_long()) for q in p]
        xnum = Binv * Matrix(yv)
        if any(int(q) % den for q in xnum):
            raise ValueError("SAT selected64 pairing vector left integral Picard64 image")
        x = Matrix([int(q) // den for q in xnum])
        xv = vector_int(x)
        exact_pv = vector_int(P * x)
        if exact_pv != pv:
            raise ValueError("SAT all140 replay from Picard64 regression")
        if min(pv) < 0 or sum(pv[:NORMAL_COUNT]) != normal_mass or sum(pv[NORMAL_COUNT:]) != v1.EXCEPTIONAL_MASS:
            raise ValueError("SAT mass/nonnegativity replay regression")
        for label, value in terminal_by_label.items():
            if pv[label - 1] != value:
                raise ValueError("SAT terminal replay regression")
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
        witness_r_reduced = vector_int(r)
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
            "original_59d_translation_sha256": v1.csha(vector_int(t)),
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

    status_text = (
        "PASS_ONE_INDEXED_TERMINAL_EXACT_PICARD64_COMPLETION_AND_59D_PROJECTION"
        if aggregate_status == "SAT"
        else (
            "PASS_ONE_INDEXED_TERMINAL_EXACT_NO_PICARD64_COMPLETION"
            if aggregate_status == "UNSAT"
            else "PASS_RESIDUAL_MASS2_BRANCHED_EXACT_UNKNOWN_NO_COMPLETION_CREDIT"
        )
    )
    branch_status_stream_sha256 = hashlib.sha256(
        "\n".join(f"{r['branch_id']}|{r['status']}|{r['selected_residual_mass']}|{r['assignment_sparse']}" for r in branch_records).encode()
    ).hexdigest()

    payload = {
        "schema": SCHEMA,
        "stage": "32EX5",
        "leaf": "BC2-02",
        "unit": "BC2_02_ONE_INDEXED_FULL178_TERMINAL_EXCEPTIONAL_MASS2_BRANCHED_EXACT",
        "status": status_text,
        "source_locks": {
            "manifest_canonical_sha256": manifest_canonical,
            "prefix_checkpoint_canonical_sha256": checkpoint_canonical,
            "adapter_preflight_canonical_sha256": adapter_preflight_canonical,
            "prior_v1_unknown_canonical_sha256": prior_canonical,
            "retained_bundle_canonical_sha256": bundle.get("canonical_sha256"),
            "retained_marking_canonical_sha256": marking.get("canonical_sha256"),
            "selected64_inverse_denominator": den,
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
            "terminal_exceptional_labels_1based": terminal_exceptional_labels,
            "fixed_exceptional_mass": fixed_exceptional_mass,
            "residual_exceptional_mass": residual_exceptional_mass,
        },
        "branch_partition": {
            "selected64_labels_1based": selected_labels,
            "selected_exceptional_labels_1based": selected_exceptional_labels,
            "remaining_selected_exceptional_labels_1based": remaining_selected_exceptional_labels,
            "remaining_selected_exceptional_count": len(remaining_selected_exceptional_labels),
            "residual_mass_upper_bound": residual_exceptional_mass,
            "partition_formula": "all nonnegative assignments on 19 remaining selected exceptional pairings with total <= 2",
            "branch_count": len(assignments),
            "expected_branch_count_formula": "1 + 19 + C(20,2) = 210",
            "assignment_stream_sha256": assignment_sha256,
            "partition_complete_for_every_V1_solution": True,
            "new_mathematical_condition_added_over_v1": False,
        },
        "exact_completion_problem": {
            "solver": "Z3_QF_LIA_INCREMENTAL_210_BRANCH_PARTITION",
            "z3_version": get_version_string(),
            "branch_timeout_ms": args.branch_timeout_ms,
            "tested_branch_count": len(branch_records),
            "unsat_branch_count": unsat_count,
            "unknown_branch_count": unknown_count,
            "sat_branch": sat_branch,
            "aggregate_result": aggregate_status,
            "aggregate_unsat_requires_all_210_exact_unsat": True,
            "branch_status_stream_sha256": branch_status_stream_sha256,
            "21az_fixed_projection_prism_imported": False,
            "21bk_21bh_21bi_21bj_chain_bands_imported": False,
            "self_intersection_used_to_authorize_solver_sat": False,
        },
        "branch_records": branch_records,
        "target": target,
        "result": {
            "status": aggregate_status,
            "witness_r_reduced": witness_r_reduced,
            "completion": completion,
        },
        "semantics": {
            "pairing_coordinate_reparameterization_is_exact": True,
            "branch_partition_is_exhaustive_for_V1_solution_set": True,
            "unknown_branch_prevents_unsat_credit": True,
            "indexed_terminal_is_not_assumed_to_determine_z": True,
            "z_is_computed_only_after_exact_picard64_completion": True,
            "sat_is_one_exact_integral_numerical_picard_completion_only": True,
            "unsat_is_one_indexed_terminal_only": True,
            "one_terminal_result_is_not_full178_completion": True,
            "sat_is_not_effective_integral_curve_existence": True,
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
        "status": status_text,
        "aggregate_result": aggregate_status,
        "tested_branches": len(branch_records),
        "unsat_branches": unsat_count,
        "unknown_branches": unknown_count,
        "sat_branch_id": sat_branch["branch_id"] if sat_branch else None,
        "projection_z": target.get("z"),
        "self_intersection": completion.get("self_intersection") if completion else None,
        "support": completion.get("positive_exceptional_support") if completion else None,
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
