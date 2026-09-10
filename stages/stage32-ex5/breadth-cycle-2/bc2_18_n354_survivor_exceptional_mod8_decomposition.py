#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import sys
from collections import Counter
from pathlib import Path

import sympy
from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
RETAINED = ROOT / "stages/stage33/33-07/picard_base_rows_retained.py"
MARKING = ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py"
BC2_17_EVIDENCE = HERE / "bc2-17-n354-authority-picard64-retarget-v2-evidence.json"
sys.path.insert(0, str(RESIDUAL))

from hperp_integral_adapter import HperpIntegralPairingAdapter
from pairing_prefix_engine import INDLIST

SCHEMA = "STAGE32EX5_BC2_18_N354_SURVIVOR_EXCEPTIONAL_MOD8_DECOMPOSITION_V2"
EXPECTED_BC2_17_CANONICAL = "a8dd000481a39011bd1d9d108d55e38e0420dbc2bb7abf4851595dfdb5da5072"
EXPECTED_BUNDLE_CANONICAL = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
EXPECTED_MARKING_CANONICAL = "e06291dddfc529fca2c0b0fe58dd43151faccd3d7997d9aa5797e1978227bb7c"
NORMAL_COUNT = 92
X4_LABEL = 49
TARGET_E = 8
TARGET_D = 8
RESIDUAL_EXCEPTIONAL_MASS = 6
EXPECTED_DEN = 8
EXPECTED_SELECTED_NORMAL = 35
EXPECTED_SELECTED_EXCEPTIONAL = 29
EXPECTED_FIXED_EXCEPTIONAL = 10
EXPECTED_FREE_SELECTED_EXCEPTIONAL = 19
EXPECTED_ENUM = 177100


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_retained(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import retained payload: {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    payload = mod.load()
    if not isinstance(payload, dict):
        raise ValueError(f"retained payload is not dict: {path}")
    return payload


def lcm_denominator(m: Matrix) -> int:
    den = 1
    for q in m:
        den = math.lcm(den, int(sympy.denom(q)))
    return den


def weak_compositions_at_most(total: int, parts: int):
    buf = [0] * parts
    def rec(i: int, rem: int):
        if i == parts:
            yield tuple(buf)
            return
        for v in range(rem + 1):
            buf[i] = v
            yield from rec(i + 1, rem - v)
        buf[i] = 0
    yield from rec(0, total)


def matrix_list(m: Matrix) -> list[list[int]]:
    return [[int(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]


def build_hnf_extension_check(B: Matrix, den: int, assigned: list[int], unassigned: list[int]) -> dict:
    if set(assigned) & set(unassigned) or sorted(assigned + unassigned) != list(range(B.cols)):
        raise ValueError("assigned/unassigned coordinate partition regression")
    suffix = B[:, unassigned] if unassigned else Matrix.zeros(B.rows, 0)
    lattice = suffix.row_join(den * Matrix.eye(B.rows))
    hnf = hermite_normal_form(lattice)
    if hnf.shape != (B.rows, B.rows) or hnf.det() == 0:
        raise ValueError("HNF extension lattice regression")
    inv = hnf.inv()
    modulus = lcm_denominator(inv)
    inv_int_q = inv * modulus
    if any(sympy.denom(v) != 1 for v in inv_int_q):
        raise ValueError("HNF inverse scaling regression")
    inv_int = Matrix([[int(inv_int_q[i, j]) for j in range(inv_int_q.cols)] for i in range(inv_int_q.rows)])
    coeff = inv_int * B[:, assigned]
    active_rows = []
    if modulus != 1:
        for i in range(coeff.rows):
            row = [int(coeff[i, j]) % modulus for j in range(coeff.cols)]
            if any(row):
                active_rows.append(row)
    return {
        "assigned": assigned,
        "unassigned": unassigned,
        "modulus": modulus,
        "coefficients": active_rows,
        "active_congruence_rows": len(active_rows),
        "quotient_index": abs(int(hnf.det())),
        "hnf_sha256": csha(matrix_list(hnf)),
        "coefficients_sha256": csha(active_rows),
    }


def feasible(check: dict, values: list[int]) -> bool:
    if len(values) != len(check["assigned"]):
        raise ValueError("HNF feasibility value-width regression")
    q = int(check["modulus"])
    if q == 1:
        return True
    return all(sum(int(a) * int(v) for a, v in zip(row, values)) % q == 0 for row in check["coefficients"])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    bc217 = json.loads(BC2_17_EVIDENCE.read_text())
    if bc217.get("canonical_sha256_without_this_field") != EXPECTED_BC2_17_CANONICAL:
        raise ValueError("BC2-17 evidence canonical regression")
    probe = bc217["picard64_probe"]
    if probe["result"] != "UNKNOWN" or probe["reason_unknown"] != "timeout":
        raise ValueError("BC2-17 solver-wall status regression")
    target = bc217["retarget"]["selected_target"]
    if target != {"row_id":"g1-d008","g":1,"d":8,"e":8,"survives_n354":True}:
        raise ValueError("BC2-17 target regression")
    fixed = {int(k): int(v) for k, v in bc217["retarget"]["fixed_exceptional_pairings"].items()}
    if len(fixed) != EXPECTED_FIXED_EXCEPTIONAL or sum(fixed.values()) != 2:
        raise ValueError("BC2-17 fixed exceptional data regression")
    if bc217["retarget"]["residual_exceptional_mass"] != RESIDUAL_EXCEPTIONAL_MASS:
        raise ValueError("BC2-17 residual exceptional mass regression")

    bundle = load_retained(RETAINED, "s32ex5_bc218_bundle")
    marking = load_retained(MARKING, "s32ex5_bc218_marking")
    if bundle.get("canonical_sha256") != EXPECTED_BUNDLE_CANONICAL:
        raise ValueError("retained bundle canonical regression")
    if marking.get("canonical_sha256") != EXPECTED_MARKING_CANONICAL:
        raise ValueError("retained marking canonical regression")

    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    P = Matrix(adapter.pairing_matrix)
    if P.shape != (140, 64):
        raise ValueError("all140 pairing matrix shape regression")

    selected_labels = [int(v) for v in INDLIST]
    selected_indices = [label - 1 for label in selected_labels]
    Psel = P.extract(selected_indices, list(range(64)))
    if Psel.det() == 0:
        raise ValueError("actual INDLIST selected64 pairing matrix singular")
    Pinv = Psel.inv()
    den = lcm_denominator(Pinv)
    if den != EXPECTED_DEN:
        raise ValueError(f"actual INDLIST selected64 denominator regression: {den}")
    Bq = Pinv * den
    if any(sympy.denom(v) != 1 for v in Bq):
        raise ValueError("actual selected64 inverse scaling regression")
    B = Matrix([[int(Bq[i, j]) for j in range(Bq.cols)] for i in range(Bq.rows)])
    if Psel * B != den * Matrix.eye(64):
        raise ValueError("actual selected64 inverse reconstruction regression")
    Anum_q = P * B
    if any(sympy.denom(v) != 1 for v in Anum_q):
        raise ValueError("all140 selected-coordinate numerator map nonintegral")
    Anum = Matrix([[int(Anum_q[i, j]) for j in range(Anum_q.cols)] for i in range(Anum_q.rows)])
    for j, label in enumerate(selected_labels):
        expected = [0] * 64
        expected[j] = den
        got = [int(Anum[label - 1, k]) for k in range(64)]
        if got != expected:
            raise ValueError(f"actual selected64 row replay regression at label {label}")

    selected_normal_positions = [j for j, label in enumerate(selected_labels) if label <= NORMAL_COUNT]
    selected_exceptional_positions = [j for j, label in enumerate(selected_labels) if label > NORMAL_COUNT]
    selected_normal_labels = [selected_labels[j] for j in selected_normal_positions]
    selected_exceptional_labels = [selected_labels[j] for j in selected_exceptional_positions]
    if len(selected_normal_positions) != EXPECTED_SELECTED_NORMAL or len(selected_exceptional_positions) != EXPECTED_SELECTED_EXCEPTIONAL:
        raise ValueError("actual INDLIST normal/exceptional partition regression")
    if X4_LABEL not in selected_normal_labels:
        raise ValueError("x4 label left actual selected64")
    if any(label not in selected_exceptional_labels for label in fixed):
        raise ValueError("terminal fixed exceptional label left actual selected64")

    pos_by_label = {label: j for j, label in enumerate(selected_labels)}
    free_selected_exceptional_labels = [label for label in selected_exceptional_labels if label not in fixed]
    if len(free_selected_exceptional_labels) != EXPECTED_FREE_SELECTED_EXCEPTIONAL:
        raise ValueError("free selected exceptional count regression")
    expected_enum = math.comb(RESIDUAL_EXCEPTIONAL_MASS + len(free_selected_exceptional_labels), len(free_selected_exceptional_labels))
    if expected_enum != EXPECTED_ENUM:
        raise ValueError(f"parent enumeration size regression: {expected_enum}")

    full_assigned = list(selected_exceptional_positions)
    full_unassigned = list(selected_normal_positions)
    full_check = build_hnf_extension_check(B, den, full_assigned, full_unassigned)
    x4_pos = pos_by_label[X4_LABEL]
    x4_assigned = list(selected_exceptional_positions) + [x4_pos]
    x4_unassigned = [j for j in selected_normal_positions if j != x4_pos]
    x4_check = build_hnf_extension_check(B, den, x4_assigned, x4_unassigned)

    def exceptional_values(comp: tuple[int, ...]) -> list[int]:
        by_label = dict(fixed)
        by_label.update({label: int(value) for label, value in zip(free_selected_exceptional_labels, comp)})
        return [int(by_label[label]) for label in selected_exceptional_labels]

    enumerated = 0
    modular_feasible = 0
    residue_union: set[int] = set()
    residue_mask_hist = Counter()
    selected_residual_mass_hist = Counter()
    feasible_residual_mass_hist = Counter()
    feasible_stream = hashlib.sha256()
    first_feasible = []

    for comp in weak_compositions_at_most(RESIDUAL_EXCEPTIONAL_MASS, len(free_selected_exceptional_labels)):
        enumerated += 1
        yE = exceptional_values(comp)
        selected_residual_mass_hist[sum(comp)] += 1
        is_full_feasible = feasible(full_check, yE)
        allowed = []
        mask = 0
        for residue in range(den):
            if feasible(x4_check, yE + [residue]):
                allowed.append(residue)
                mask |= 1 << residue
        if is_full_feasible != bool(allowed):
            raise ValueError("full HNF extension vs x4-residue extension regression")
        if not is_full_feasible:
            continue
        modular_feasible += 1
        feasible_residual_mass_hist[sum(comp)] += 1
        residue_union.update(allowed)
        residue_mask_hist[mask] += 1
        record = {"selected_exceptional_pairings": yE, "selected_residual_mass": sum(comp), "x4_allowed_residues_mod8": allowed}
        feasible_stream.update(json.dumps(record, sort_keys=True, separators=(",", ":")).encode() + b"\n")
        if len(first_feasible) < 16:
            first_feasible.append(record)

    if enumerated != expected_enum:
        raise ValueError(f"weak-composition coverage regression: {enumerated} != {expected_enum}")

    x4_values_union = [x for x in range(113) if x % den in residue_union]
    fixed_n355_diagonal_ok = all(v <= TARGET_D // 2 for v in fixed.values())
    if modular_feasible == 0:
        status = "PASS_N354_SURVIVOR_FIRST_BLOCK_EXACT_UNSAT_BY_SELECTED_EXCEPTIONAL_MOD8_EXTENSION"
        next_id = "BC2_19_UNIFORMIZE_SELECTED_EXCEPTIONAL_MOD8_OBSTRUCTION_ACROSS_N354_SURVIVORS"
    else:
        status = "PASS_SELECTED_EXCEPTIONAL_MOD8_DECOMPOSITION_NORMAL_POSITIVITY_REMAINS"
        next_id = "BC2_19_NORMAL_POSITIVITY_MASS_REPLAY_ON_MOD8_SURVIVING_PARENTS"

    body = {
        "schema": SCHEMA,
        "stage": "32EX5",
        "unit": "BC2_18_DECOMPOSE_N354_SURVIVOR_PICARD64_PROBE",
        "status": status,
        "source_locks": {"bc2_17_evidence_canonical": EXPECTED_BC2_17_CANONICAL, "retained_bundle_canonical": EXPECTED_BUNDLE_CANONICAL, "retained_marking_canonical": EXPECTED_MARKING_CANONICAL},
        "target": {"row_id":"g1-d008","g":1,"d":TARGET_D,"e":TARGET_E,"first_block":[0,112],"first_block_width":113,"fixed_exceptional_mass":2,"residual_exceptional_mass":RESIDUAL_EXCEPTIONAL_MASS},
        "actual_selected64": {
            "coordinate_source": "all140 pairing rows at pairing_prefix_engine.INDLIST",
            "selected_labels_1based": selected_labels,
            "selected_normal_labels": selected_normal_labels,
            "selected_exceptional_labels": selected_exceptional_labels,
            "selected_normal_count": len(selected_normal_labels),
            "selected_exceptional_count": len(selected_exceptional_labels),
            "inverse_denominator": den,
            "inverse_integer_sha256": csha(matrix_list(B)),
            "all140_numerator_map_sha256": csha(matrix_list(Anum)),
            "selected_row_identity_replay": True
        },
        "parent_space": {
            "fixed_terminal_exceptional_pairings": {str(k): v for k, v in sorted(fixed.items())},
            "free_selected_exceptional_labels": free_selected_exceptional_labels,
            "free_selected_exceptional_count": len(free_selected_exceptional_labels),
            "selected_residual_mass_cap": RESIDUAL_EXCEPTIONAL_MASS,
            "coverage_reason": "all48 exceptional pairings are nonnegative and sum to 8, while fixed selected terminal exceptional mass is 2; therefore every integral completion has total remaining selected exceptional mass at most 6",
            "enumerated_parent_count": enumerated,
            "expected_parent_count": expected_enum,
            "selected_residual_mass_histogram": {str(k): v for k, v in sorted(selected_residual_mass_hist.items())}
        },
        "picard_integrality_extension": {
            "method": "exact HNF membership in columns(B_unassigned) + 8*Z^64",
            "meaning": "a fixed selected-exceptional pairing vector extends to some integer selected-normal pairings whose reconstructed Picard64 coordinates are integral",
            "full_check": {k: full_check[k] for k in ("modulus","active_congruence_rows","quotient_index","hnf_sha256","coefficients_sha256")},
            "x4_residue_check": {k: x4_check[k] for k in ("modulus","active_congruence_rows","quotient_index","hnf_sha256","coefficients_sha256")},
            "mod8_extendable_parent_count": modular_feasible,
            "rejected_by_integrality_extension_count": enumerated - modular_feasible,
            "feasible_selected_residual_mass_histogram": {str(k): v for k, v in sorted(feasible_residual_mass_hist.items())},
            "x4_allowed_residues_mod8_union": sorted(residue_union),
            "x4_allowed_values_0_112_union": x4_values_union,
            "x4_residue_mask_histogram": {str(k): v for k, v in sorted(residue_mask_hist.items())},
            "feasible_stream_sha256": feasible_stream.hexdigest(),
            "first_feasible_parents": first_feasible
        },
        "n355_candidate_interaction": {"n355_is_consumed_as_authority":False,"known10_diagonal_bound":"pairing <= floor(d/2)=4","fixed_terminal_known10_satisfy_diagonal_bound":fixed_n355_diagonal_ok,"current_first_block_pruned_by_this_known10_diagonal_test":False},
        "credit": {"solver_used":False,"heavy_compute":False,"parent_space_coverage_exact":True,"picard_integrality_extension_filter_exact":True,"normal_nonnegativity_and_normal_mass_solved":False,"unselected_exceptional_nonnegativity_and_total_mass_solved":False,"whole_first_block_unsat":modular_feasible==0,"whole_stratum_closed":False,"full178_complete":False,"stage32_main_credit":False,"n350_production_credit":False,"theorem_credit":False,"endpoint_credit":False},
        "next_exact_unit": {"id":next_id,"heavy_scaleout_authorized":False,"main_promotion_authorized":False},
        "firewalls": {"bc2_17_unknown_relabelled_unsat_without_new_proof":False,"n355_audit_candidate_self_promoted":False,"main_promotion":False,"perfect_cuboid_existence_claim":False,"perfect_cuboid_nonexistence_claim":False,"merge_authorized":False}
    }
    out = {**body, "canonical_sha256_without_this_field": csha(body)}
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status":status,"enumerated":enumerated,"mod8_extendable":modular_feasible,"rejected_by_mod8":enumerated-modular_feasible,"x4_residues":sorted(residue_union),"next":next_id,"canonical":out["canonical_sha256_without_this_field"]}, sort_keys=True))


if __name__ == "__main__":
    main()
