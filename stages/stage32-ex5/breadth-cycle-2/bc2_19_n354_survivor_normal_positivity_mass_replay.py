#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from sympy import Matrix
from z3 import Int, SolverFor, get_version_string, sat, unknown, unsat

import bc2_18_n354_survivor_exceptional_mod8_decomposition as d18

HERE = Path(__file__).resolve().parent
BC2_17_EVIDENCE = HERE / "bc2-17-n354-authority-picard64-retarget-v2-evidence.json"
BC2_18_CHECKPOINT = HERE / "bc2-18-n354-survivor-selected-exceptional-mod8-checkpoint.json"

SCHEMA = "STAGE32EX5_BC2_19_N354_SURVIVOR_NORMAL_POSITIVITY_MASS_REPLAY_V1"
EXPECTED_BC2_17_CANONICAL = "a8dd000481a39011bd1d9d108d55e38e0420dbc2bb7abf4851595dfdb5da5072"
EXPECTED_BC2_18_CANONICAL = "b789468cb515e9ebff55ca7bbfab98a32b3857137dd0ea534fcfdf20b914f6f8"
EXPECTED_FEASIBLE_STREAM_SHA256 = "752a7618e5a4301aea16a3a4983081e02fb26451a21d84e4b8e60b8d11f84db7"
EXPECTED_PARENT_COUNT = 7336
EXPECTED_ENUMERATED_PARENT_COUNT = 177100
NORMAL_COUNT = 92
PICARD_RANK = 64
ALL140_COUNT = 140
TARGET_D = 8
TARGET_E = 8
NORMAL_MASS = 112
RESIDUAL_EXCEPTIONAL_MASS = 6
X4_LABEL = 49


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--per-parent-timeout-ms", type=int, default=2000)
    ap.add_argument("--max-parents", type=int, default=0,
                    help="0 means all exact mod8-surviving parents")
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if args.per_parent_timeout_ms <= 0:
        raise ValueError("per-parent timeout must be positive")
    if args.max_parents < 0:
        raise ValueError("max-parents must be nonnegative")

    bc217 = json.loads(BC2_17_EVIDENCE.read_text())
    if bc217.get("canonical_sha256_without_this_field") != EXPECTED_BC2_17_CANONICAL:
        raise ValueError("BC2-17 evidence canonical regression")
    bc218 = json.loads(BC2_18_CHECKPOINT.read_text())
    if bc218.get("canonical_sha256_without_this_field") != EXPECTED_BC2_18_CANONICAL:
        raise ValueError("BC2-18 checkpoint canonical regression")
    if bc218["status"] != "PASS_SELECTED_EXCEPTIONAL_MOD8_DECOMPOSITION_NORMAL_POSITIVITY_REMAINS":
        raise ValueError("BC2-18 status regression")
    if bc218["next_exact_unit"]["id"] != "BC2_19_NORMAL_POSITIVITY_MASS_REPLAY_ON_MOD8_SURVIVING_PARENTS":
        raise ValueError("BC2-18 next-route regression")
    if bc218["exact_decomposition"]["mod8_extendable_parent_count"] != EXPECTED_PARENT_COUNT:
        raise ValueError("BC2-18 parent count regression")
    if bc218["exact_decomposition"]["enumerated_parent_count"] != EXPECTED_ENUMERATED_PARENT_COUNT:
        raise ValueError("BC2-18 enumeration count regression")
    if bc218["exact_decomposition"]["feasible_stream_sha256"] != EXPECTED_FEASIBLE_STREAM_SHA256:
        raise ValueError("BC2-18 feasible stream regression")

    fixed = {
        int(k): int(v)
        for k, v in bc217["retarget"]["fixed_exceptional_pairings"].items()
    }
    if len(fixed) != 10 or sum(fixed.values()) != 2:
        raise ValueError("BC2-17 fixed exceptional pairings regression")
    if bc217["retarget"]["residual_exceptional_mass"] != RESIDUAL_EXCEPTIONAL_MASS:
        raise ValueError("BC2-17 residual exceptional mass regression")

    bundle = d18.load_retained(d18.RETAINED, "s32ex5_bc219_bundle")
    marking = d18.load_retained(d18.MARKING, "s32ex5_bc219_marking")
    if bundle.get("canonical_sha256") != d18.EXPECTED_BUNDLE_CANONICAL:
        raise ValueError("retained bundle canonical regression")
    if marking.get("canonical_sha256") != d18.EXPECTED_MARKING_CANONICAL:
        raise ValueError("retained marking canonical regression")

    adapter = d18.HperpIntegralPairingAdapter.from_retained(marking, bundle)
    P = Matrix(adapter.pairing_matrix)
    if P.shape != (ALL140_COUNT, PICARD_RANK):
        raise ValueError("all140 pairing matrix shape regression")

    selected_labels = [int(v) for v in d18.INDLIST]
    selected_indices = [label - 1 for label in selected_labels]
    Psel = P.extract(selected_indices, list(range(PICARD_RANK)))
    if Psel.det() == 0:
        raise ValueError("selected64 pairing matrix singular")
    Pinv = Psel.inv()
    den = d18.lcm_denominator(Pinv)
    if den != 8:
        raise ValueError("selected64 denominator regression")
    Bq = Pinv * den
    if any(q.q != 1 for q in Bq):
        raise ValueError("selected64 inverse scaling regression")
    B = Matrix([[int(Bq[i, j]) for j in range(Bq.cols)] for i in range(Bq.rows)])
    if Psel * B != den * Matrix.eye(PICARD_RANK):
        raise ValueError("selected64 inverse reconstruction regression")

    selected_normal_positions = [
        j for j, label in enumerate(selected_labels) if label <= NORMAL_COUNT
    ]
    selected_exceptional_positions = [
        j for j, label in enumerate(selected_labels) if label > NORMAL_COUNT
    ]
    selected_exceptional_labels = [selected_labels[j] for j in selected_exceptional_positions]
    if any(label not in selected_exceptional_labels for label in fixed):
        raise ValueError("fixed exceptional label left selected64")
    free_selected_exceptional_labels = [
        label for label in selected_exceptional_labels if label not in fixed
    ]
    if len(free_selected_exceptional_labels) != 19:
        raise ValueError("free selected exceptional count regression")

    full_check = d18.build_hnf_extension_check(
        B, den, selected_exceptional_positions, selected_normal_positions
    )
    x4_pos = selected_labels.index(X4_LABEL)
    x4_check = d18.build_hnf_extension_check(
        B,
        den,
        selected_exceptional_positions + [x4_pos],
        [j for j in selected_normal_positions if j != x4_pos],
    )

    def exceptional_values(comp: tuple[int, ...]) -> list[int]:
        by_label = dict(fixed)
        by_label.update(
            {
                label: int(value)
                for label, value in zip(free_selected_exceptional_labels, comp)
            }
        )
        return [int(by_label[label]) for label in selected_exceptional_labels]

    parents: list[tuple[tuple[int, ...], list[int], list[int]]] = []
    stream = hashlib.sha256()
    enumerated = 0
    for comp in d18.weak_compositions_at_most(
        RESIDUAL_EXCEPTIONAL_MASS, len(free_selected_exceptional_labels)
    ):
        enumerated += 1
        yE = exceptional_values(comp)
        allowed = [
            residue
            for residue in range(den)
            if d18.feasible(x4_check, yE + [residue])
        ]
        full_ok = d18.feasible(full_check, yE)
        if full_ok != bool(allowed):
            raise ValueError("HNF parent/x4 extension regression")
        if not full_ok:
            continue
        record = {
            "selected_exceptional_pairings": yE,
            "selected_residual_mass": sum(comp),
            "x4_allowed_residues_mod8": allowed,
        }
        stream.update(
            json.dumps(record, sort_keys=True, separators=(",", ":")).encode() + b"\n"
        )
        parents.append((comp, yE, allowed))
    if enumerated != EXPECTED_ENUMERATED_PARENT_COUNT:
        raise ValueError("parent enumeration coverage regression")
    if len(parents) != EXPECTED_PARENT_COUNT:
        raise ValueError("mod8 surviving parent count regression")
    if stream.hexdigest() != EXPECTED_FEASIBLE_STREAM_SHA256:
        raise ValueError("mod8 surviving parent stream regression")

    limit = len(parents) if args.max_parents == 0 else min(args.max_parents, len(parents))

    x = [Int(f"x_{j}") for j in range(PICARD_RANK)]
    p = [
        sum(int(P[i, j]) * x[j] for j in range(PICARD_RANK))
        for i in range(ALL140_COUNT)
    ]
    solver = SolverFor("QF_LIA")
    solver.set(timeout=args.per_parent_timeout_ms)

    for i in range(NORMAL_COUNT):
        solver.add(p[i] >= 0, p[i] <= NORMAL_MASS)
    for i in range(NORMAL_COUNT, ALL140_COUNT):
        solver.add(p[i] >= 0, p[i] <= TARGET_E)
    solver.add(sum(p[:NORMAL_COUNT]) == NORMAL_MASS)
    solver.add(sum(p[NORMAL_COUNT:]) == TARGET_E)
    for label, value in fixed.items():
        solver.add(p[label - 1] == value)
    solver.add(p[X4_LABEL - 1] >= 0, p[X4_LABEL - 1] <= NORMAL_MASS)

    checked = 0
    unsat_count = 0
    unknown_count = 0
    unknown_parent_indices: list[int] = []
    status_stream = hashlib.sha256()
    sat_witness = None

    for parent_index, (comp, yE, allowed) in enumerate(parents[:limit]):
        solver.push()
        for label, value in zip(selected_exceptional_labels, yE):
            solver.add(p[label - 1] == int(value))
        result = solver.check()
        checked += 1
        if result == sat:
            model = solver.model()
            xv = [int(model.eval(q, model_completion=True).as_long()) for q in x]
            pv = [
                sum(int(P[i, j]) * xv[j] for j in range(PICARD_RANK))
                for i in range(ALL140_COUNT)
            ]
            if min(pv) < 0:
                raise ValueError("SAT witness violates all140 nonnegativity")
            if sum(pv[:NORMAL_COUNT]) != NORMAL_MASS:
                raise ValueError("SAT witness normal mass regression")
            if sum(pv[NORMAL_COUNT:]) != TARGET_E:
                raise ValueError("SAT witness exceptional mass regression")
            if any(pv[label - 1] != value for label, value in fixed.items()):
                raise ValueError("SAT witness terminal fixed-pairing regression")
            if any(
                pv[label - 1] != value
                for label, value in zip(selected_exceptional_labels, yE)
            ):
                raise ValueError("SAT witness parent regression")
            x4 = pv[X4_LABEL - 1]
            if not 0 <= x4 <= NORMAL_MASS or x4 % den not in allowed:
                raise ValueError("SAT witness x4 block/residue regression")
            sat_witness = {
                "parent_index": parent_index,
                "selected_residual_mass": sum(comp),
                "free_selected_exceptional_values": list(comp),
                "selected_exceptional_pairings": yE,
                "x4": x4,
                "x4_mod8": x4 % den,
                "picard64_coordinates": xv,
                "all140_pairings": pv,
                "all140_pairings_sha256": csha(pv),
            }
            status_stream.update(f"{parent_index}:SAT\n".encode())
            solver.pop()
            break
        if result == unsat:
            unsat_count += 1
            status_stream.update(f"{parent_index}:UNSAT\n".encode())
        elif result == unknown:
            unknown_count += 1
            if len(unknown_parent_indices) < 64:
                unknown_parent_indices.append(parent_index)
            status_stream.update(f"{parent_index}:UNKNOWN:{solver.reason_unknown()}\n".encode())
        else:
            raise ValueError(f"unexpected solver result: {result}")
        solver.pop()

    if sat_witness is not None:
        status = "PASS_PICARD64_PAIRING_FEASIBLE_WITNESS_FOUND_NO_CURVE_CREDIT"
        next_id = "BC2_20_ANALYZE_PICARD64_SAT_WITNESS_AND_N355_INTERACTION"
        whole_first_block_unsat = False
    elif checked == len(parents) and unknown_count == 0:
        status = "PASS_N354_SURVIVOR_FIRST_BLOCK_EXACT_UNSAT_AFTER_NORMAL_POSITIVITY_MASS"
        next_id = "BC2_20_UNIFORMIZE_PICARD64_OBSTRUCTION_ACROSS_N354_SURVIVORS"
        whole_first_block_unsat = True
    else:
        status = "BLOCKED_NORMAL_POSITIVITY_PARENT_REPLAY_HAS_UNKNOWN_OR_PARTIAL_COVERAGE"
        next_id = "BC2_20_SLICE_UNKNOWN_NORMAL_POSITIVITY_PARENTS"
        whole_first_block_unsat = False

    body = {
        "schema": SCHEMA,
        "stage": "32EX5",
        "unit": "BC2_19_NORMAL_POSITIVITY_MASS_REPLAY_ON_MOD8_SURVIVING_PARENTS",
        "status": status,
        "source_locks": {
            "bc2_17_evidence_canonical": EXPECTED_BC2_17_CANONICAL,
            "bc2_18_checkpoint_canonical": EXPECTED_BC2_18_CANONICAL,
            "bc2_18_feasible_stream_sha256": EXPECTED_FEASIBLE_STREAM_SHA256,
            "retained_bundle_canonical": d18.EXPECTED_BUNDLE_CANONICAL,
            "retained_marking_canonical": d18.EXPECTED_MARKING_CANONICAL,
        },
        "target": {
            "row_id": "g1-d008",
            "g": 1,
            "d": TARGET_D,
            "e": TARGET_E,
            "first_block": [0, 112],
            "first_block_width": 113,
            "fixed_exceptional_mass": 2,
            "residual_exceptional_mass": RESIDUAL_EXCEPTIONAL_MASS,
        },
        "parent_replay": {
            "input_mod8_parent_count": len(parents),
            "parents_requested": limit,
            "parents_checked": checked,
            "unsat_count": unsat_count,
            "unknown_count": unknown_count,
            "sat_found": sat_witness is not None,
            "unknown_parent_indices_first64": unknown_parent_indices,
            "status_stream_sha256": status_stream.hexdigest(),
            "per_parent_timeout_ms": args.per_parent_timeout_ms,
            "solver": "Z3_QF_LIA_INCREMENTAL",
            "z3_version": get_version_string(),
        },
        "exact_constraints": {
            "picard64_coordinates_integral": True,
            "all140_pairings_from_exact_integer_pairing_matrix": True,
            "all140_nonnegative": True,
            "normal_pairing_mass": NORMAL_MASS,
            "exceptional_pairing_mass": TARGET_E,
            "terminal_fixed_exceptional_pairings": {
                str(k): v for k, v in sorted(fixed.items())
            },
            "selected_exceptional_parent_fixed_per_check": True,
            "x4_symbolic_first_block": [0, 112],
        },
        "sat_witness": sat_witness,
        "credit": {
            "parent_space_coverage_exact": checked == len(parents),
            "whole_first_block_unsat": whole_first_block_unsat,
            "picard64_pairing_feasibility_only_if_sat": sat_witness is not None,
            "effectivity_or_actual_curve_existence_proved": False,
            "whole_stratum_closed": False,
            "full178_complete": False,
            "stage32_main_credit": False,
            "n350_production_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
        },
        "firewalls": {
            "sat_relabelled_actual_curve": False,
            "unknown_relabelled_unsat": False,
            "main_promotion": False,
            "merge_authorized": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
        "next_exact_unit": {
            "id": next_id,
            "heavy_scaleout_authorized": False,
            "main_promotion_authorized": False,
        },
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    args.output.write_text(json.dumps(body, sort_keys=True, indent=2) + "\n")
    print(json.dumps({
        "status": status,
        "parents_checked": checked,
        "unsat": unsat_count,
        "unknown": unknown_count,
        "sat": sat_witness is not None,
        "sat_parent": None if sat_witness is None else sat_witness["parent_index"],
        "sat_x4": None if sat_witness is None else sat_witness["x4"],
        "canonical": body["canonical_sha256_without_this_field"],
        "next": next_id,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
