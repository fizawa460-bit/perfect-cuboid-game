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

SCHEMA = "STAGE32EX5_BC2_03_GENERIC_INDEXED_TERMINAL_ADAPTIVE_EXCEPTIONAL_PARTITION_V1"
RANK0_CHECKPOINT_CANONICAL = "02f50ea59027f340baedbdcb0a712b02b71a316c6cc87ab8e7be905317eb0f8b"
NORMAL_COUNT = 92
EXCEPTIONAL_COUNT = 48
EXPECTED_SELECTED_EXCEPTIONAL_COUNT = 29
EXPECTED_UNSELECTED_EXCEPTIONAL_COUNT = 19


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def vector_int(v: Matrix) -> list[int]:
    if v.cols != 1:
        raise ValueError("expected column vector")
    return [int(v[i, 0]) for i in range(v.rows)]


def lcm_denominator(m: Matrix) -> int:
    den = 1
    for q in m:
        den = math.lcm(den, int(sympy.denom(q)))
    return den


def exact_weak_compositions(total: int, parts: int):
    total = int(total)
    parts = int(parts)
    if total < 0 or parts <= 0:
        return
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in exact_weak_compositions(total - first, parts - 1):
            yield (first,) + tail


def at_most_weak_compositions(limit: int, parts: int):
    for total in range(int(limit) + 1):
        yield from exact_weak_compositions(total, parts)


def sparse_labels(labels: list[int], values: tuple[int, ...]) -> list[list[int]]:
    return [[int(label), int(value)] for label, value in zip(labels, values) if value]


def reconstruct_sat(
    *,
    model,
    y,
    p,
    Binv: Matrix,
    den: int,
    P: Matrix,
    normal_mass: int,
    bridge,
    data: dict,
    bundle: dict,
) -> tuple[dict, list[int], dict]:
    yv = [int(model.eval(q, model_completion=True).as_long()) for q in y]
    pv = [int(model.eval(q, model_completion=True).as_long()) for q in p]
    xnum = Binv * Matrix(yv)
    if any(int(q) % den for q in xnum):
        raise ValueError("SAT selected64 vector left integral Picard64 image")
    x = Matrix([int(q) // den for q in xnum])
    xv = vector_int(x)
    if vector_int(P * x) != pv:
        raise ValueError("SAT all140 replay regression")
    if min(pv) < 0:
        raise ValueError("SAT all140 nonnegativity regression")
    if sum(pv[:NORMAL_COUNT]) != normal_mass:
        raise ValueError("SAT normal mass replay regression")
    if sum(pv[NORMAL_COUNT:]) != v1.EXCEPTIONAL_MASS:
        raise ValueError("SAT exceptional mass replay regression")

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
    rv = vector_int(r)
    if x0 + data["K"] * U * r != x:
        raise ValueError("reduced 59D witness reconstruction regression")

    gram = Matrix(bundle["picard_gram_64x64"])
    selfsq_q = (x.T * gram * x)[0, 0]
    if sympy.denom(selfsq_q) != 1:
        raise ValueError("Picard self-intersection became nonintegral")

    target_extra = {"a": int(a_actual), "z": zv}
    completion = {
        "selected64_pairings": yv,
        "selected64_pairings_sha256": csha(yv),
        "picard_coordinates": xv,
        "picard_coordinates_sha256": csha(xv),
        "all140_pairings": pv,
        "all140_pairings_sha256": csha(pv),
        "all140_nonnegative": True,
        "normal_pairing_sum": sum(pv[:NORMAL_COUNT]),
        "exceptional_pairing_sum": sum(pv[NORMAL_COUNT:]),
        "first_normal_half_a": int(a_actual),
        "projection_z": zv,
        "positive_exceptional_support": sum(1 for q in pv[NORMAL_COUNT:] if q > 0),
        "self_intersection": int(selfsq_q),
        "full_exceptional_pairing_vector_fixed_in_sat_subcase": True,
    }
    return target_extra, rv, completion


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--prefix-checkpoint", type=Path, required=True)
    ap.add_argument("--adapter-preflight", type=Path, required=True)
    ap.add_argument("--rank0-checkpoint", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--terminal-rank", type=int, required=True)
    ap.add_argument("--parent-timeout-ms", type=int, default=1500)
    ap.add_argument("--refine-timeout-ms", type=int, default=1000)
    ap.add_argument("--max-parent-branches", type=int, default=1000)
    ap.add_argument("--max-refined-subcases", type=int, default=5000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if args.parent_timeout_ms <= 0 or args.refine_timeout_ms <= 0:
        raise ValueError("solver timeouts must be positive")

    manifest, manifest_canonical = v1.load_canonical_json(args.manifest)
    prefix, prefix_canonical = v1.load_canonical_json(args.prefix_checkpoint)
    preflight, preflight_canonical = v1.load_canonical_json(args.adapter_preflight)
    rank0, rank0_canonical = v1.load_canonical_json(args.rank0_checkpoint)
    if rank0_canonical != RANK0_CHECKPOINT_CANONICAL:
        raise ValueError("rank0 exact checkpoint canonical regression")
    locks = rank0["source_locks"]
    for got, expected, name in (
        (manifest_canonical, locks["manifest_canonical_sha256"], "manifest"),
        (prefix_canonical, locks["prefix_checkpoint_canonical_sha256"], "prefix"),
        (preflight_canonical, locks["adapter_preflight_canonical_sha256"], "adapter preflight"),
    ):
        if got != expected:
            raise ValueError(f"{name} source-lock regression")
    if rank0["exact_result"]["rank0_terminal_exact_unsat_authorized"] is not True:
        raise ValueError("rank0 predecessor exact-UNSAT authority regression")
    if preflight["preflight_findings"]["direct_index_to_z_shortcut_authorized"] is not False:
        raise ValueError("unsafe direct terminal-index to z shortcut became authorized")

    rows = v1.parse_manifest_rows(manifest)
    if len(rows) != 178 or v1.ROW_ID not in rows:
        raise ValueError("FULL178 manifest row population regression")
    if prefix["exact_terminal_family"]["assignment_order_known_labels_1based"] != v1.EXPECTED_ASSIGNMENT_ORDER:
        raise ValueError("terminal assignment-order regression")

    indexer = v1.CompressedTerminalIndexer(v1.EXCEPTIONAL_MASS, v1.DEGREE)
    if not 0 <= args.terminal_rank < indexer.terminal_count:
        raise ValueError("requested terminal rank outside indexed stratum")
    terminal = tuple(int(q) for q in indexer.unrank(args.terminal_rank))
    if indexer.rank(terminal) != args.terminal_rank:
        raise ValueError("terminal rank/unrank regression")

    bundle = v1.load_retained(args.retained, "s32ex5_bc2_03_generic_picard")
    marking = v1.load_retained(args.marking, "s32ex5_bc2_03_generic_marking")
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
    den = lcm_denominator(Pinv)
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

    terminal_by_label = {
        int(label): int(value)
        for label, value in zip(v1.EXPECTED_ASSIGNMENT_ORDER, terminal)
    }
    selected_exceptional_labels = [label for label in selected_labels if label > NORMAL_COUNT]
    if len(selected_exceptional_labels) != EXPECTED_SELECTED_EXCEPTIONAL_COUNT:
        raise ValueError("selected exceptional count regression")
    terminal_exceptional_labels = sorted(label for label in terminal_by_label if label > NORMAL_COUNT)
    if any(label not in selected_exceptional_labels for label in terminal_exceptional_labels):
        raise ValueError("terminal exceptional label left selected64 set")
    fixed_exceptional_mass = sum(terminal_by_label[label] for label in terminal_exceptional_labels)
    residual_exceptional_mass = v1.EXCEPTIONAL_MASS - fixed_exceptional_mass
    if residual_exceptional_mass < 0:
        raise ValueError("terminal fixed exceptional mass exceeds stratum mass")

    remaining_selected_exceptional_labels = [
        label for label in selected_exceptional_labels if label not in terminal_by_label
    ]
    selected_pos = {label: selected_labels.index(label) for label in selected_labels}
    remaining_selected_positions = [
        selected_pos[label] for label in remaining_selected_exceptional_labels
    ]
    unselected_exceptional_labels = [
        label
        for label in range(NORMAL_COUNT + 1, NORMAL_COUNT + EXCEPTIONAL_COUNT + 1)
        if label not in selected_exceptional_labels
    ]
    if len(unselected_exceptional_labels) != EXPECTED_UNSELECTED_EXCEPTIONAL_COUNT:
        raise ValueError("unselected exceptional count regression")

    expected_parent_branch_count = math.comb(
        residual_exceptional_mass + len(remaining_selected_exceptional_labels),
        len(remaining_selected_exceptional_labels),
    )
    if expected_parent_branch_count > args.max_parent_branches:
        raise ValueError(
            f"parent branch resource gate: {expected_parent_branch_count}>{args.max_parent_branches}"
        )
    parent_assignments = list(
        at_most_weak_compositions(
            residual_exceptional_mass, len(remaining_selected_exceptional_labels)
        )
    )
    if len(parent_assignments) != expected_parent_branch_count:
        raise ValueError("parent weak-composition coverage regression")

    normal_mass = 19 * v1.DEGREE - 5 * v1.EXCEPTIONAL_MASS
    y = [Int(f"y_{j}") for j in range(v1.PICARD_RANK)]
    p = [Int(f"p_{i}") for i in range(v1.ALL140_COUNT)]
    solver = SolverFor("QF_LIA")

    for j, label in enumerate(selected_labels):
        ub = v1.EXCEPTIONAL_MASS if label > NORMAL_COUNT else normal_mass
        solver.add(y[j] >= 0, y[j] <= ub)
        solver.add(p[label - 1] == y[j])
    for i in range(v1.ALL140_COUNT):
        ub = normal_mass if i < NORMAL_COUNT else v1.EXCEPTIONAL_MASS
        solver.add(p[i] >= 0, p[i] <= ub)
        solver.add(
            den * p[i]
            == sum(int(Anum[i, j]) * y[j] for j in range(v1.PICARD_RANK))
        )
    for i in range(v1.PICARD_RANK):
        numerator = sum(int(Binv[i, j]) * y[j] for j in range(v1.PICARD_RANK))
        solver.add(numerator % den == 0)
    solver.add(sum(p[:NORMAL_COUNT]) == normal_mass)
    solver.add(sum(p[NORMAL_COUNT:]) == v1.EXCEPTIONAL_MASS)
    for label, value in terminal_by_label.items():
        solver.add(p[label - 1] == value)
    solver.add(
        sum(y[pos] for pos in remaining_selected_positions)
        <= residual_exceptional_mass
    )

    parent_records: list[dict] = []
    parent_exact_unsat = 0
    parent_unknown: list[tuple[int, tuple[int, ...]]] = []
    sat_record = None
    sat_model = None

    solver.set(timeout=args.parent_timeout_ms)
    for parent_id, assignment in enumerate(parent_assignments):
        solver.push()
        try:
            for pos, value in zip(remaining_selected_positions, assignment):
                solver.add(y[pos] == int(value))
            result = solver.check()
            record = {
                "parent_branch_id": int(parent_id),
                "selected_residual_mass": int(sum(assignment)),
                "selected_assignment_sparse_labels_1based": sparse_labels(
                    remaining_selected_exceptional_labels, assignment
                ),
            }
            if result == sat:
                record["status"] = "SAT"
                sat_record = record
                sat_model = solver.model()
                parent_records.append(record)
                break
            if result == unsat:
                record["status"] = "UNSAT"
                parent_exact_unsat += 1
            elif result == unknown:
                record["status"] = "UNKNOWN"
                record["reason_unknown"] = solver.reason_unknown()
                parent_unknown.append((parent_id, assignment))
            else:
                raise ValueError(f"unexpected parent solver result: {result}")
            parent_records.append(record)
        finally:
            solver.pop()

    refined_records: list[dict] = []
    refined_exact_unsat = 0
    refined_unknown = 0
    expected_refined_subcases = 0

    if sat_record is None:
        for parent_id, assignment in parent_unknown:
            selected_mass = int(sum(assignment))
            unselected_mass = residual_exceptional_mass - selected_mass
            subcase_count = math.comb(
                unselected_mass + len(unselected_exceptional_labels) - 1,
                len(unselected_exceptional_labels) - 1,
            )
            expected_refined_subcases += subcase_count
        if expected_refined_subcases > args.max_refined_subcases:
            raise ValueError(
                f"refinement resource gate: {expected_refined_subcases}>{args.max_refined_subcases}"
            )

        solver.set(timeout=args.refine_timeout_ms)
        for parent_id, assignment in parent_unknown:
            selected_mass = int(sum(assignment))
            unselected_mass = residual_exceptional_mass - selected_mass
            solver.push()
            try:
                for pos, value in zip(remaining_selected_positions, assignment):
                    solver.add(y[pos] == int(value))
                for subcase_id, unselected_assignment in enumerate(
                    exact_weak_compositions(
                        unselected_mass, len(unselected_exceptional_labels)
                    )
                ):
                    solver.push()
                    try:
                        for label, value in zip(
                            unselected_exceptional_labels, unselected_assignment
                        ):
                            solver.add(p[label - 1] == int(value))
                        result = solver.check()
                        record = {
                            "parent_branch_id": int(parent_id),
                            "parent_selected_residual_mass": selected_mass,
                            "subcase_id": int(subcase_id),
                            "unselected_exceptional_residual_mass": unselected_mass,
                            "unselected_assignment_sparse_labels_1based": sparse_labels(
                                unselected_exceptional_labels, unselected_assignment
                            ),
                        }
                        if result == sat:
                            record["status"] = "SAT"
                            sat_record = record
                            sat_model = solver.model()
                            refined_records.append(record)
                            break
                        if result == unsat:
                            record["status"] = "UNSAT"
                            refined_exact_unsat += 1
                        elif result == unknown:
                            record["status"] = "UNKNOWN"
                            record["reason_unknown"] = solver.reason_unknown()
                            refined_unknown += 1
                        else:
                            raise ValueError(
                                f"unexpected refinement solver result: {result}"
                            )
                        refined_records.append(record)
                    finally:
                        solver.pop()
                if sat_record is not None:
                    break
            finally:
                solver.pop()

    if sat_record is not None:
        aggregate = "SAT"
    elif not parent_unknown:
        aggregate = (
            "UNSAT"
            if parent_exact_unsat == expected_parent_branch_count
            else "UNKNOWN"
        )
    else:
        aggregate = (
            "UNSAT"
            if refined_unknown == 0
            and len(refined_records) == expected_refined_subcases
            and refined_exact_unsat == expected_refined_subcases
            else "UNKNOWN"
        )

    if aggregate == "UNSAT":
        if parent_exact_unsat + len(parent_unknown) != expected_parent_branch_count:
            raise ValueError("terminal UNSAT parent coverage regression")
        if parent_unknown and (
            len(refined_records) != expected_refined_subcases
            or refined_exact_unsat != expected_refined_subcases
            or refined_unknown != 0
        ):
            raise ValueError("terminal UNSAT refinement coverage regression")
    if aggregate == "UNKNOWN" and sat_record is not None:
        raise ValueError("UNKNOWN/SAT accounting regression")

    target = {
        "row_id": v1.ROW_ID,
        "genus": v1.GENUS,
        "degree": v1.DEGREE,
        "e": v1.EXCEPTIONAL_MASS,
        "terminal_rank": int(args.terminal_rank),
        "terminal_pairings": list(terminal),
    }
    witness_r_reduced = None
    completion = None
    if aggregate == "SAT":
        if sat_model is None:
            raise ValueError("SAT aggregate missing model")
        target_extra, witness_r_reduced, completion = reconstruct_sat(
            model=sat_model,
            y=y,
            p=p,
            Binv=Binv,
            den=den,
            P=P,
            normal_mass=normal_mass,
            bridge=bridge,
            data=data,
            bundle=bundle,
        )
        target.update(target_extra)

    status = (
        "PASS_GENERIC_INDEXED_TERMINAL_EXACT_PICARD64_COMPLETION"
        if aggregate == "SAT"
        else "PASS_GENERIC_INDEXED_TERMINAL_EXACT_UNSAT"
        if aggregate == "UNSAT"
        else "PASS_GENERIC_INDEXED_TERMINAL_UNKNOWN_NO_TERMINAL_CREDIT"
    )
    payload = {
        "schema": SCHEMA,
        "stage": "32EX5",
        "leaf": "BC2-03",
        "unit": "BC2_03_GENERIC_INDEXED_TERMINAL_ADAPTIVE_EXCEPTIONAL_PARTITION",
        "status": status,
        "source_locks": {
            "rank0_checkpoint_canonical_sha256": rank0_canonical,
            "manifest_canonical_sha256": manifest_canonical,
            "prefix_checkpoint_canonical_sha256": prefix_canonical,
            "adapter_preflight_canonical_sha256": preflight_canonical,
            "retained_bundle_canonical_sha256": bundle["canonical_sha256"],
            "retained_marking_canonical_sha256": marking["canonical_sha256"],
            "selected64_inverse_denominator": den,
        },
        "indexed_terminal": {
            "row_id": v1.ROW_ID,
            "degree": v1.DEGREE,
            "e": v1.EXCEPTIONAL_MASS,
            "terminal_rank": int(args.terminal_rank),
            "terminal_count_in_stratum": int(indexer.terminal_count),
            "terminal_pairings": list(terminal),
            "rank_roundtrip_exact": True,
            "canonical_index_order": indexer.certificate()["canonical_index_order"],
        },
        "adaptive_partition": {
            "fixed_terminal_exceptional_mass": int(fixed_exceptional_mass),
            "residual_exceptional_mass": int(residual_exceptional_mass),
            "selected_exceptional_count": len(selected_exceptional_labels),
            "remaining_selected_exceptional_count": len(
                remaining_selected_exceptional_labels
            ),
            "unselected_exceptional_count": len(unselected_exceptional_labels),
            "parent_partition_semantics": (
                "all nonnegative weak compositions of mass <= residual across "
                "remaining selected exceptional pairings"
            ),
            "parent_branch_count": expected_parent_branch_count,
            "parent_assignment_stream_sha256": csha(
                [sparse_labels(remaining_selected_exceptional_labels, a) for a in parent_assignments]
            ),
            "parent_partition_complete": True,
            "refinement_semantics": (
                "UNKNOWN parent only: exact weak compositions of the remaining "
                "exceptional mass across all unselected exceptional pairings"
            ),
            "all_48_exceptional_pairings_fixed_in_each_refined_subcase": True,
            "new_mathematical_condition_added": False,
            "resource_gates_are_execution_only_not_mathematical_conditions": True,
        },
        "parent_result": {
            "tested_parent_branches": len(parent_records),
            "exact_unsat_parent_branches": parent_exact_unsat,
            "unknown_parent_branches": len(parent_unknown),
            "sat_parent_or_refined_record": sat_record,
            "parent_timeout_ms": args.parent_timeout_ms,
            "parent_status_stream_sha256": csha(
                [[r["parent_branch_id"], r["status"]] for r in parent_records]
            ),
        },
        "refinement_result": {
            "expected_refined_subcases": expected_refined_subcases,
            "tested_refined_subcases": len(refined_records),
            "exact_unsat_refined_subcases": refined_exact_unsat,
            "unknown_refined_subcases": refined_unknown,
            "refine_timeout_ms": args.refine_timeout_ms,
            "refined_status_stream_sha256": csha(
                [
                    [r["parent_branch_id"], r["subcase_id"], r["status"]]
                    for r in refined_records
                ]
            ),
        },
        "exact_result": {
            "aggregate_result": aggregate,
            "terminal_exact_unsat_authorized": aggregate == "UNSAT",
            "terminal_exact_sat_completion_found": aggregate == "SAT",
            "z3_version": get_version_string(),
        },
        "target": target,
        "result": {
            "status": aggregate,
            "completion": completion,
            "witness_r_reduced": witness_r_reduced,
        },
        "semantics": {
            "rank0_algorithm_genericized_by_terminal_rank": True,
            "random_access_rank_unrank_replayed": True,
            "selected_exceptional_partition_first": True,
            "only_unknown_parents_refined": True,
            "one_terminal_result_is_not_whole_stratum_completion": True,
            "one_terminal_result_is_not_FULL178_completion": True,
            "sat_is_not_effective_integral_curve_existence": True,
            "unknown_prevents_terminal_unsat_credit": True,
        },
        "firewalls": {
            "whole_g1_d008_e4_stratum_closed": False,
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
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "terminal_rank": args.terminal_rank,
                "terminal_pairings": list(terminal),
                "residual_exceptional_mass": residual_exceptional_mass,
                "parent_branches": expected_parent_branch_count,
                "parent_unsat": parent_exact_unsat,
                "parent_unknown": len(parent_unknown),
                "refined_expected": expected_refined_subcases,
                "refined_tested": len(refined_records),
                "refined_unsat": refined_exact_unsat,
                "refined_unknown": refined_unknown,
                "aggregate_result": aggregate,
                "canonical_sha256": payload["canonical_sha256_without_this_field"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
