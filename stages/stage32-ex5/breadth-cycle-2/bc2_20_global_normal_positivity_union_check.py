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
BC2_19_CHECKPOINT = HERE / "bc2-19-n354-survivor-normal-positivity-mass-checkpoint.json"

SCHEMA = "STAGE32EX5_BC2_20_GLOBAL_NORMAL_POSITIVITY_UNION_CHECK_V1"
EXPECTED_BC2_17 = "a8dd000481a39011bd1d9d108d55e38e0420dbc2bb7abf4851595dfdb5da5072"
EXPECTED_BC2_18 = "b789468cb515e9ebff55ca7bbfab98a32b3857137dd0ea534fcfdf20b914f6f8"
EXPECTED_BC2_18_BLOB = "0e269d5ec6da24b9b887b6dd40f4b4f33242e154"
EXPECTED_BC2_18_RAW_OUTPUT = "ca53c910b70cb41dd628cd1d428227b4aa91523ed49b74b0e669e89e7e88fe2e"
EXPECTED_BC2_18_SOURCE_COMMIT = "d095336aceae65d5f56cdbfaa88ef6e1ad705b82"
EXPECTED_FEASIBLE_STREAM = "752a7618e5a4301aea16a3a4983081e02fb26451a21d84e4b8e60b8d11f84db7"
EXPECTED_BC2_19 = "62e97cdb8bd6a8d14c0ac176576bd2cf2ec51020295f8703cbefc3bc85f001eb"
EXPECTED_PARENT_COUNT = 7336
EXPECTED_ENUMERATED_PARENT_COUNT = 177100
NORMAL_COUNT = 92
ALL140_COUNT = 140
PICARD_RANK = 64
TARGET_E = 8
NORMAL_MASS = 112
X4_LABEL = 49


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def git_blob_sha(raw: bytes) -> str:
    header = f"blob {len(raw)}\0".encode()
    return hashlib.sha1(header + raw).hexdigest()


def load_self_canonical(path: Path, expected: str, label: str) -> dict:
    obj = json.loads(path.read_text())
    if obj.get("canonical_sha256_without_this_field") != expected:
        raise ValueError(f"{label} canonical field regression")
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    if csha(cp) != expected:
        raise ValueError(f"{label} canonical replay regression")
    return obj


def load_bc2_18_pinned() -> dict:
    raw = BC2_18_CHECKPOINT.read_bytes()
    if git_blob_sha(raw) != EXPECTED_BC2_18_BLOB:
        raise ValueError("BC2-18 checkpoint Git blob regression")
    obj = json.loads(raw)
    if obj.get("canonical_sha256_without_this_field") != EXPECTED_BC2_18:
        raise ValueError("BC2-18 embedded canonical regression")
    if obj.get("schema") != "STAGE32EX5_BC2_18_N354_SURVIVOR_SELECTED_EXCEPTIONAL_MOD8_CHECKPOINT_V1":
        raise ValueError("BC2-18 checkpoint schema regression")
    if obj.get("status") != "PASS_SELECTED_EXCEPTIONAL_MOD8_DECOMPOSITION_NORMAL_POSITIVITY_REMAINS":
        raise ValueError("BC2-18 checkpoint status regression")
    dec = obj.get("exact_decomposition", {})
    if dec.get("mod8_extendable_parent_count") != EXPECTED_PARENT_COUNT:
        raise ValueError("BC2-18 parent-count regression")
    if dec.get("enumerated_parent_count") != EXPECTED_ENUMERATED_PARENT_COUNT:
        raise ValueError("BC2-18 enumeration-count regression")
    if dec.get("feasible_stream_sha256") != EXPECTED_FEASIBLE_STREAM:
        raise ValueError("BC2-18 feasible-stream regression")
    locks = obj.get("source_locks", {})
    if locks.get("bc2_17_evidence_canonical") != EXPECTED_BC2_17:
        raise ValueError("BC2-18 BC2-17 source-lock regression")
    if locks.get("exact_output_canonical") != EXPECTED_BC2_18_RAW_OUTPUT:
        raise ValueError("BC2-18 raw-output source-lock regression")
    if locks.get("source_commit") != EXPECTED_BC2_18_SOURCE_COMMIT:
        raise ValueError("BC2-18 source-commit regression")
    nxt = obj.get("next_exact_unit", {})
    if nxt.get("id") != "BC2_19_NORMAL_POSITIVITY_MASS_REPLAY_ON_MOD8_SURVIVING_PARENTS":
        raise ValueError("BC2-18 next-unit regression")
    if nxt.get("input_parent_count") != EXPECTED_PARENT_COUNT:
        raise ValueError("BC2-18 next-unit parent-count regression")
    return obj


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--solver-timeout-ms", type=int, default=300000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if args.solver_timeout_ms <= 0:
        raise ValueError("solver timeout must be positive")

    bc217 = load_self_canonical(BC2_17_EVIDENCE, EXPECTED_BC2_17, "BC2-17")
    bc218 = load_bc2_18_pinned()
    bc219 = load_self_canonical(BC2_19_CHECKPOINT, EXPECTED_BC2_19, "BC2-19")
    if bc218["exact_decomposition"]["mod8_extendable_parent_count"] != EXPECTED_PARENT_COUNT:
        raise ValueError("BC2-18 parent-count regression")
    if bc219["result"]["input_mod8_parent_count"] != EXPECTED_PARENT_COUNT:
        raise ValueError("BC2-19 parent-count regression")
    if (bc219["result"]["unsat_count"], bc219["result"]["unknown_count"], bc219["result"]["sat_count"]) != (7100, 236, 0):
        raise ValueError("BC2-19 partition regression")

    fixed = {int(k): int(v) for k, v in bc217["retarget"]["fixed_exceptional_pairings"].items()}
    if len(fixed) != 10 or sum(fixed.values()) != 2:
        raise ValueError("fixed exceptional pairing regression")

    bundle = d18.load_retained(d18.RETAINED, "s32ex5_bc220_bundle")
    marking = d18.load_retained(d18.MARKING, "s32ex5_bc220_marking")
    if bundle.get("canonical_sha256") != d18.EXPECTED_BUNDLE_CANONICAL:
        raise ValueError("retained bundle canonical regression")
    if marking.get("canonical_sha256") != d18.EXPECTED_MARKING_CANONICAL:
        raise ValueError("retained marking canonical regression")

    adapter = d18.HperpIntegralPairingAdapter.from_retained(marking, bundle)
    P = Matrix(adapter.pairing_matrix)
    if P.shape != (ALL140_COUNT, PICARD_RANK):
        raise ValueError("pairing matrix shape regression")

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
        raise ValueError("scaled selected64 inverse nonintegral")
    B = Matrix([[int(Bq[i, j]) for j in range(Bq.cols)] for i in range(Bq.rows)])
    if Psel * B != den * Matrix.eye(PICARD_RANK):
        raise ValueError("selected64 inverse reconstruction regression")

    selected_normal_positions = [j for j, label in enumerate(selected_labels) if label <= NORMAL_COUNT]
    selected_exceptional_positions = [j for j, label in enumerate(selected_labels) if label > NORMAL_COUNT]
    selected_exceptional_labels = [selected_labels[j] for j in selected_exceptional_positions]
    if any(label not in selected_exceptional_labels for label in fixed):
        raise ValueError("fixed exceptional label left selected64")
    free_selected_exceptional_labels = [label for label in selected_exceptional_labels if label not in fixed]
    if len(free_selected_exceptional_labels) != 19:
        raise ValueError("free selected exceptional count regression")

    # Exact union compression: every BC2-19 SAT parent is a solution below;
    # conversely, every solution below has nonnegative integral exceptional
    # pairings of total mass 8. The ten fixed selected exceptional pairings have
    # mass 2, so the 19 free selected values form one of BC2-18's weak
    # compositions of mass <=6. Integral Picard coordinates themselves witness
    # the selected64/HNF extension.
    x = [Int(f"x_{j}") for j in range(PICARD_RANK)]
    p = [
        sum(int(P[i, j]) * x[j] for j in range(PICARD_RANK))
        for i in range(ALL140_COUNT)
    ]
    solver = SolverFor("QF_LIA")
    solver.set(timeout=args.solver_timeout_ms)
    for i in range(NORMAL_COUNT):
        solver.add(p[i] >= 0, p[i] <= NORMAL_MASS)
    for i in range(NORMAL_COUNT, ALL140_COUNT):
        solver.add(p[i] >= 0, p[i] <= TARGET_E)
    solver.add(sum(p[:NORMAL_COUNT]) == NORMAL_MASS)
    solver.add(sum(p[NORMAL_COUNT:]) == TARGET_E)
    for label, value in fixed.items():
        solver.add(p[label - 1] == value)

    result = solver.check()
    witness = None
    reason_unknown = None

    if result == sat:
        model = solver.model()
        xv = [int(model.eval(q, model_completion=True).as_long()) for q in x]
        pv = [
            sum(int(P[i, j]) * xv[j] for j in range(PICARD_RANK))
            for i in range(ALL140_COUNT)
        ]
        if min(pv) < 0 or sum(pv[:NORMAL_COUNT]) != NORMAL_MASS or sum(pv[NORMAL_COUNT:]) != TARGET_E:
            raise ValueError("SAT witness violates global mass/nonnegativity")
        if any(pv[label - 1] != value for label, value in fixed.items()):
            raise ValueError("SAT witness violates fixed terminal pairings")
        free_comp = [pv[label - 1] for label in free_selected_exceptional_labels]
        if any(v < 0 for v in free_comp) or sum(free_comp) > 6:
            raise ValueError("SAT witness does not induce BC2-18 weak composition")

        yE = [pv[label - 1] for label in selected_exceptional_labels]
        full_check = d18.build_hnf_extension_check(
            B, den, selected_exceptional_positions, selected_normal_positions
        )
        if not d18.feasible(full_check, yE):
            raise ValueError("SAT witness fails BC2-18 selected64 HNF parent condition")
        x4_pos = selected_labels.index(X4_LABEL)
        x4_check = d18.build_hnf_extension_check(
            B,
            den,
            selected_exceptional_positions + [x4_pos],
            [j for j in selected_normal_positions if j != x4_pos],
        )
        allowed = [r for r in range(den) if d18.feasible(x4_check, yE + [r])]
        x4 = pv[X4_LABEL - 1]
        if x4 % den not in allowed:
            raise ValueError("SAT witness fails BC2-18 x4 residue condition")
        witness = {
            "picard64_coordinates": xv,
            "all140_pairings": pv,
            "all140_pairings_sha256": csha(pv),
            "induced_bc2_18_parent": {
                "free_selected_exceptional_values": free_comp,
                "free_selected_exceptional_mass": sum(free_comp),
                "selected_exceptional_pairings": yE,
                "x4": x4,
                "x4_mod8": x4 % den,
                "allowed_x4_residues_mod8": allowed,
                "bc2_18_hnf_parent_extendable": True,
            },
        }
        status = "PASS_GLOBAL_PICARD64_PAIRING_FEASIBLE_WITNESS_FOUND_NO_CURVE_CREDIT"
        next_id = "BC2_21_ANALYZE_GLOBAL_PICARD64_WITNESS_AND_FULL_SPECIAL_FIBRE_INEQUALITIES"
        whole_unsat = False
    elif result == unsat:
        status = "PASS_N354_SURVIVOR_FIRST_BLOCK_EXACT_UNSAT_AFTER_GLOBAL_NORMAL_POSITIVITY_UNION_COMPRESSION"
        next_id = "BC2_21_RETAIN_FIRST_BLOCK_UNSAT_AND_ASSESS_STRATUM_COVERAGE"
        whole_unsat = True
    elif result == unknown:
        reason_unknown = solver.reason_unknown()
        status = "BLOCKED_GLOBAL_NORMAL_POSITIVITY_UNION_CHECK_UNKNOWN"
        next_id = "BC2_21_SLICE_BC2_19_UNKNOWN_PARENTS"
        whole_unsat = False
    else:
        raise ValueError(f"unexpected solver result: {result}")

    body = {
        "schema": SCHEMA,
        "stage": "32EX5",
        "unit": "BC2_20_GLOBAL_NORMAL_POSITIVITY_UNION_CHECK",
        "status": status,
        "source_locks": {
            "bc2_17_evidence_canonical": EXPECTED_BC2_17,
            "bc2_18_checkpoint_canonical": EXPECTED_BC2_18,
            "bc2_18_checkpoint_git_blob": EXPECTED_BC2_18_BLOB,
            "bc2_18_raw_output_canonical": EXPECTED_BC2_18_RAW_OUTPUT,
            "bc2_18_source_commit": EXPECTED_BC2_18_SOURCE_COMMIT,
            "bc2_19_checkpoint_canonical": EXPECTED_BC2_19,
            "retained_bundle_canonical": d18.EXPECTED_BUNDLE_CANONICAL,
            "retained_marking_canonical": d18.EXPECTED_MARKING_CANONICAL,
        },
        "target": {"row_id": "g1-d008", "g": 1, "d": 8, "e": 8, "first_block": [0, 112]},
        "solver": {
            "kind": "Z3_QF_LIA_SINGLE_GLOBAL_CHECK",
            "z3_version": get_version_string(),
            "timeout_ms": args.solver_timeout_ms,
            "result": str(result),
            "reason_unknown": reason_unknown,
        },
        "union_equivalence": {
            "bc2_18_mod8_parent_count": EXPECTED_PARENT_COUNT,
            "bc2_19_unsat_parent_count": 7100,
            "bc2_19_unknown_parent_count": 236,
            "fixed_selected_exceptional_mass": 2,
            "total_exceptional_mass": TARGET_E,
            "free_selected_exceptional_mass_at_most": 6,
            "every_global_solution_induces_bc2_18_enumerated_parent": True,
            "integral_picard_solution_implies_selected64_hnf_extension": True,
            "every_bc2_19_parent_sat_solution_satisfies_global_system": True,
            "global_sat_iff_some_bc2_18_parent_sat": True,
        },
        "sat_witness": witness,
        "credit": {
            "whole_first_block_unsat": whole_unsat,
            "picard64_pairing_feasibility_only_if_sat": witness is not None,
            "whole_stratum_closed": False,
            "full178_complete": False,
            "stage32_main_credit": False,
            "n350_production_credit": False,
            "effectivity_or_actual_curve_existence_proved": False,
            "theorem_credit": False,
            "endpoint_credit": False,
        },
        "firewalls": {
            "unknown_relabelled_unsat": False,
            "sat_relabelled_actual_curve": False,
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
    args.output.write_text(json.dumps(body, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "canonical": body["canonical_sha256_without_this_field"],
        "status": status,
        "solver_result": str(result),
        "next": next_id,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
