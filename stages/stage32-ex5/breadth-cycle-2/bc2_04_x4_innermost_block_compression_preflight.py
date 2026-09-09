#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import sympy
from sympy import Matrix
from z3 import Int, SolverFor, get_version_string, sat, unknown, unsat

import bc2_03_generic_indexed_terminal_adaptive_exceptional_partition as g

SCHEMA = "STAGE32EX5_BC2_04_X4_INNERMOST_BLOCK_COMPRESSION_PREFLIGHT_V1"
NORMAL_COUNT = 92
EXCEPTIONAL_COUNT = 48
BLOCK_EXCEPTIONAL_RANK = 0
EXPECTED_NORMAL_BUDGET = 132
EXPECTED_BLOCK_WIDTH = 133
EXPECTED_LABEL49 = 49
EXPECTED_SELECTED_EXCEPTIONAL_COUNT = 29
EXPECTED_UNSELECTED_EXCEPTIONAL_COUNT = 19
EXPECTED_RANK1_EVIDENCE = "447e8f99748f72b1ab741ddc1b675be5f59109a972e598b2d624c48d93432432"
EXPECTED_RANK1_SOURCE_HEAD = "31c4b1f1808dcd415768888a226f62e7213d42d7"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--prefix-checkpoint", type=Path, required=True)
    ap.add_argument("--adapter-preflight", type=Path, required=True)
    ap.add_argument("--rank0-checkpoint", type=Path, required=True)
    ap.add_argument("--rank1-checkpoint", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--parent-timeout-ms", type=int, default=1500)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if args.parent_timeout_ms <= 0:
        raise ValueError("parent timeout must be positive")

    v1 = g.v1
    manifest, manifest_canonical = v1.load_canonical_json(args.manifest)
    prefix, prefix_canonical = v1.load_canonical_json(args.prefix_checkpoint)
    preflight, preflight_canonical = v1.load_canonical_json(args.adapter_preflight)
    rank0, rank0_canonical = v1.load_canonical_json(args.rank0_checkpoint)
    rank1 = load_json(args.rank1_checkpoint)

    if rank0_canonical != g.RANK0_CHECKPOINT_CANONICAL:
        raise ValueError("rank0 checkpoint canonical regression")
    if rank1.get("source_exact_head") != EXPECTED_RANK1_SOURCE_HEAD:
        raise ValueError("rank1 source head regression")
    if rank1.get("exact_result", {}).get("evidence_canonical_sha256") != EXPECTED_RANK1_EVIDENCE:
        raise ValueError("rank1 evidence canonical regression")
    if rank1.get("exact_result", {}).get("rank1_terminal_exact_unsat_authorized") is not True:
        raise ValueError("rank1 predecessor exact-UNSAT authority regression")
    if rank1.get("next_exact_unit", {}).get("id") != "BC2_04_X4_INNERMOST_BLOCK_COMPRESSION_PREFLIGHT":
        raise ValueError("rank1 next-unit routing regression")

    locks = rank0["source_locks"]
    for got, expected, name in (
        (manifest_canonical, locks["manifest_canonical_sha256"], "manifest"),
        (prefix_canonical, locks["prefix_checkpoint_canonical_sha256"], "prefix"),
        (preflight_canonical, locks["adapter_preflight_canonical_sha256"], "adapter preflight"),
    ):
        if got != expected:
            raise ValueError(f"{name} source-lock regression")

    rows = v1.parse_manifest_rows(manifest)
    if len(rows) != 178 or v1.ROW_ID not in rows:
        raise ValueError("FULL178 manifest row population regression")
    if prefix["exact_terminal_family"]["assignment_order_known_labels_1based"] != v1.EXPECTED_ASSIGNMENT_ORDER:
        raise ValueError("terminal assignment-order regression")
    if v1.EXPECTED_ASSIGNMENT_ORDER[4] != EXPECTED_LABEL49:
        raise ValueError("x4/known-label-49 position regression")

    indexer = v1.CompressedTerminalIndexer(v1.EXCEPTIONAL_MASS, v1.DEGREE)
    if indexer.normal_budget != EXPECTED_NORMAL_BUDGET:
        raise ValueError("normal budget regression")
    block_width = indexer.normal_budget + 1
    if block_width != EXPECTED_BLOCK_WIDTH:
        raise ValueError("x4 block width regression")
    block_start = BLOCK_EXCEPTIONAL_RANK * block_width
    block_end = block_start + block_width - 1

    base_terminal = tuple(int(q) for q in indexer.unrank(block_start))
    base_exceptional_signature = base_terminal[:4] + base_terminal[5:]
    block_terminal_stream = []
    for x4 in range(block_width):
        rank = block_start + x4
        terminal = tuple(int(q) for q in indexer.unrank(rank))
        if terminal[4] != x4:
            raise ValueError("canonical x4 innermost order regression")
        if terminal[:4] + terminal[5:] != base_exceptional_signature:
            raise ValueError("exceptional signature changed inside x4 block")
        if indexer.rank(terminal) != rank:
            raise ValueError("x4 block rank/unrank regression")
        block_terminal_stream.append([rank, list(terminal)])
    if base_terminal != (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1):
        raise ValueError("block exceptional terminal regression")

    bundle = v1.load_retained(args.retained, "s32ex5_bc2_04_x4_block_picard")
    marking = v1.load_retained(args.marking, "s32ex5_bc2_04_x4_block_marking")
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

    selected_labels = [int(label) for label in g.INDLIST]
    if EXPECTED_LABEL49 not in selected_labels:
        raise ValueError("known-label-49 left selected64 basis")
    selected_indices = [label - 1 for label in selected_labels]
    Psel = P.extract(selected_indices, list(range(v1.PICARD_RANK)))
    if Psel.det() == 0:
        raise ValueError("selected64 pairing matrix singular")
    Pinv = Psel.inv()
    den = g.lcm_denominator(Pinv)
    if den != locks["selected64_inverse_denominator"]:
        raise ValueError("selected64 inverse denominator regression")
    Binv_q = Pinv * den
    if any(sympy.denom(q) != 1 for q in Binv_q):
        raise ValueError("selected64 inverse scaling regression")
    Binv = Matrix([[int(Binv_q[i, j]) for j in range(Binv_q.cols)] for i in range(Binv_q.rows)])
    if Psel * Binv != den * Matrix.eye(v1.PICARD_RANK):
        raise ValueError("selected64 inverse reconstruction regression")
    Anum_q = P * Binv
    if any(sympy.denom(q) != 1 for q in Anum_q):
        raise ValueError("all140 selected-coordinate map became nonintegral")
    Anum = Matrix([[int(Anum_q[i, j]) for j in range(Anum_q.cols)] for i in range(Anum_q.rows)])

    terminal_by_label = {
        int(label): int(value)
        for label, value in zip(v1.EXPECTED_ASSIGNMENT_ORDER, base_terminal)
    }
    if terminal_by_label[EXPECTED_LABEL49] != 0:
        raise ValueError("base x4 is not zero")
    selected_exceptional_labels = [label for label in selected_labels if label > NORMAL_COUNT]
    if len(selected_exceptional_labels) != EXPECTED_SELECTED_EXCEPTIONAL_COUNT:
        raise ValueError("selected exceptional count regression")
    terminal_exceptional_labels = sorted(label for label in terminal_by_label if label > NORMAL_COUNT)
    if any(label not in selected_exceptional_labels for label in terminal_exceptional_labels):
        raise ValueError("terminal exceptional label left selected64 set")
    fixed_exceptional_mass = sum(terminal_by_label[label] for label in terminal_exceptional_labels)
    residual_exceptional_mass = v1.EXCEPTIONAL_MASS - fixed_exceptional_mass
    if residual_exceptional_mass != 2:
        raise ValueError("block residual exceptional mass regression")

    remaining_selected_exceptional_labels = [
        label for label in selected_exceptional_labels if label not in terminal_by_label
    ]
    selected_pos = {label: selected_labels.index(label) for label in selected_labels}
    remaining_selected_positions = [selected_pos[label] for label in remaining_selected_exceptional_labels]
    unselected_exceptional_labels = [
        label
        for label in range(NORMAL_COUNT + 1, NORMAL_COUNT + EXCEPTIONAL_COUNT + 1)
        if label not in selected_exceptional_labels
    ]
    if len(unselected_exceptional_labels) != EXPECTED_UNSELECTED_EXCEPTIONAL_COUNT:
        raise ValueError("unselected exceptional count regression")

    parent_assignments = list(
        g.at_most_weak_compositions(residual_exceptional_mass, len(remaining_selected_exceptional_labels))
    )
    expected_parent_count = math.comb(
        residual_exceptional_mass + len(remaining_selected_exceptional_labels),
        len(remaining_selected_exceptional_labels),
    )
    if len(parent_assignments) != expected_parent_count or expected_parent_count != 210:
        raise ValueError("selected exceptional parent partition regression")

    normal_mass = 19 * v1.DEGREE - 5 * v1.EXCEPTIONAL_MASS
    if normal_mass != EXPECTED_NORMAL_BUDGET:
        raise ValueError("normal mass regression")
    y = [Int(f"y_{j}") for j in range(v1.PICARD_RANK)]
    p = [Int(f"p_{i}") for i in range(v1.ALL140_COUNT)]
    solver = SolverFor("QF_LIA")
    solver.set(timeout=args.parent_timeout_ms)

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
        if label == EXPECTED_LABEL49:
            continue
        solver.add(p[label - 1] == value)
    x4 = p[EXPECTED_LABEL49 - 1]
    solver.add(x4 >= 0, x4 <= normal_mass)
    solver.add(sum(y[pos] for pos in remaining_selected_positions) <= residual_exceptional_mass)

    parent_records = []
    unknown_parents = []
    exact_unsat_count = 0
    sat_record = None
    sat_model = None
    for parent_id, assignment in enumerate(parent_assignments):
        solver.push()
        try:
            for pos, value in zip(remaining_selected_positions, assignment):
                solver.add(y[pos] == int(value))
            result = solver.check()
            selected_mass = int(sum(assignment))
            record = [int(parent_id), selected_mass]
            if result == sat:
                record.append("SAT")
                sat_model = solver.model()
                sat_x4 = int(sat_model.eval(x4, model_completion=True).as_long())
                sat_record = {
                    "parent_branch_id": int(parent_id),
                    "selected_residual_mass": selected_mass,
                    "selected_assignment_sparse_labels_1based": g.sparse_labels(
                        remaining_selected_exceptional_labels, assignment
                    ),
                    "x4": sat_x4,
                    "terminal_rank": block_start + sat_x4,
                }
                parent_records.append(record)
                break
            if result == unsat:
                record.append("UNSAT")
                exact_unsat_count += 1
            elif result == unknown:
                record.append("UNKNOWN")
                unselected_mass = residual_exceptional_mass - selected_mass
                if unselected_mass < 0:
                    raise ValueError("negative unselected residual mass")
                refinement_count = math.comb(
                    unselected_mass + len(unselected_exceptional_labels) - 1,
                    len(unselected_exceptional_labels) - 1,
                )
                unknown_parents.append({
                    "parent_branch_id": int(parent_id),
                    "selected_residual_mass": selected_mass,
                    "selected_assignment_sparse_labels_1based": g.sparse_labels(
                        remaining_selected_exceptional_labels, assignment
                    ),
                    "unselected_residual_mass": int(unselected_mass),
                    "exact_full_exceptional_refinement_subcase_count": int(refinement_count),
                    "reason_unknown": solver.reason_unknown(),
                })
            else:
                raise ValueError(f"unexpected solver result: {result}")
            parent_records.append(record)
        finally:
            solver.pop()

    if sat_record is not None:
        aggregate = "SAT"
    elif exact_unsat_count == len(parent_assignments) and not unknown_parents:
        aggregate = "UNSAT"
    else:
        aggregate = "UNKNOWN"

    completion = None
    witness_r_reduced = None
    target = {
        "row_id": v1.ROW_ID,
        "genus": v1.GENUS,
        "degree": v1.DEGREE,
        "e": v1.EXCEPTIONAL_MASS,
        "terminal_rank_block": [block_start, block_end],
        "x4_range": [0, normal_mass],
    }
    if aggregate == "SAT":
        if sat_model is None or sat_record is None:
            raise ValueError("SAT block missing model")
        target_extra, witness_r_reduced, completion = g.reconstruct_sat(
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
        target["terminal_rank"] = int(sat_record["terminal_rank"])
        target["terminal_pairings"] = list(indexer.unrank(target["terminal_rank"]))
        if target["terminal_pairings"][4] != sat_record["x4"]:
            raise ValueError("SAT x4/terminal-rank replay regression")

    refinement_total = sum(
        int(q["exact_full_exceptional_refinement_subcase_count"])
        for q in unknown_parents
    )
    unknown_mass_counts = {}
    for q in unknown_parents:
        m = str(q["unselected_residual_mass"])
        unknown_mass_counts[m] = unknown_mass_counts.get(m, 0) + 1

    payload = {
        "schema": SCHEMA,
        "stage": "32EX5",
        "leaf": "BC2-04",
        "unit": "BC2_04_X4_INNERMOST_BLOCK_COMPRESSION_PREFLIGHT",
        "status": (
            "PASS_SYMBOLIC_X4_BLOCK_HAS_EXACT_PICARD64_COMPLETION" if aggregate == "SAT" else
            "PASS_SYMBOLIC_X4_BLOCK_EXACT_UNSAT" if aggregate == "UNSAT" else
            "PASS_SYMBOLIC_X4_BLOCK_COMPRESSION_REFINED_UNIT_REQUIRED"
        ),
        "source_locks": {
            "manifest_canonical_sha256": manifest_canonical,
            "prefix_checkpoint_canonical_sha256": prefix_canonical,
            "adapter_preflight_canonical_sha256": preflight_canonical,
            "rank0_checkpoint_canonical_sha256": rank0_canonical,
            "rank1_checkpoint_source_head": rank1["source_exact_head"],
            "rank1_evidence_canonical_sha256": rank1["exact_result"]["evidence_canonical_sha256"],
            "retained_bundle_canonical_sha256": bundle["canonical_sha256"],
            "retained_marking_canonical_sha256": marking["canonical_sha256"],
            "selected64_inverse_denominator": den,
        },
        "x4_block_semantics": {
            "exceptional_rank": BLOCK_EXCEPTIONAL_RANK,
            "rank_start": block_start,
            "rank_end": block_end,
            "block_width": block_width,
            "known_label_49_is_x4": True,
            "x4_is_only_normal_terminal_variable": True,
            "x4_is_independent_of_exceptional_terminal_predicate_conditions": True,
            "x4_range": [0, normal_mass],
            "all_133_rank_unrank_replays_exact": True,
            "exceptional_signature_constant_across_block": True,
            "block_terminal_stream_sha256": g.csha(block_terminal_stream),
            "exact_disjunction_replaced_by_single_bounded_integer_x4": True,
            "new_mathematical_condition_added": False,
        },
        "adaptive_exceptional_partition": {
            "fixed_exceptional_mass": fixed_exceptional_mass,
            "residual_exceptional_mass": residual_exceptional_mass,
            "remaining_selected_exceptional_count": len(remaining_selected_exceptional_labels),
            "unselected_exceptional_count": len(unselected_exceptional_labels),
            "parent_branch_count": len(parent_assignments),
            "parent_assignment_stream_sha256": g.csha([
                g.sparse_labels(remaining_selected_exceptional_labels, a)
                for a in parent_assignments
            ]),
            "parent_partition_complete_for_symbolic_x4_block": True,
        },
        "parent_result": {
            "aggregate_result": aggregate,
            "tested_parent_branches": len(parent_records),
            "exact_unsat_parent_branches": exact_unsat_count,
            "unknown_parent_branches": len(unknown_parents),
            "sat_parent": sat_record,
            "parent_status_stream_sha256": g.csha(parent_records),
            "unknown_parent_unselected_mass_counts": unknown_mass_counts,
            "exact_full_exceptional_refinement_subcase_count_if_needed": refinement_total,
            "parent_timeout_ms": args.parent_timeout_ms,
            "z3_version": get_version_string(),
        },
        "unknown_parents": unknown_parents,
        "target": target,
        "result": {
            "status": aggregate,
            "completion": completion,
            "witness_r_reduced": witness_r_reduced,
            "whole_rank_0_to_132_block_exact_unsat_authorized": aggregate == "UNSAT",
            "symbolic_block_sat_completion_found": aggregate == "SAT",
        },
        "next_exact_unit": {
            "id": (
                "BC2_04_SYMBOLIC_X4_BLOCK_SAT_CONSUMER" if aggregate == "SAT" else
                "BC2_04_BLOCK_CLOSED_CHECKPOINT" if aggregate == "UNSAT" else
                "BC2_05_SYMBOLIC_X4_UNKNOWN_PARENT_FULL_EXCEPTIONAL_REFINEMENT"
            ),
            "required_refined_subcases": refinement_total,
            "heavy_scaleout_authorized": False,
            "new_parallel_lane_required": False,
        },
        "firewalls": {
            "closed_indexed_terminals_before_this_unit": [0, 1],
            "whole_rank_0_to_132_block_closed": aggregate == "UNSAT",
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
    payload["canonical_sha256_without_this_field"] = g.csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "aggregate_result": aggregate,
        "block": [block_start, block_end],
        "parent_branches": len(parent_assignments),
        "tested_parent": len(parent_records),
        "parent_unsat": exact_unsat_count,
        "parent_unknown": len(unknown_parents),
        "unknown_mass_counts": unknown_mass_counts,
        "refined_subcases_if_needed": refinement_total,
        "sat_x4": None if sat_record is None else sat_record["x4"],
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
