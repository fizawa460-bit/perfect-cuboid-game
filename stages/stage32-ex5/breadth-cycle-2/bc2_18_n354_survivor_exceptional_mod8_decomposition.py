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

from sympy import Matrix
from sympy.polys.domains import ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
RETAINED = ROOT / "stages/stage33/33-07/picard_base_rows_retained.py"
MARKING = ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py"
BC2_17_EVIDENCE = HERE / "bc2-17-n354-authority-picard64-retarget-v2-evidence.json"
sys.path.insert(0, str(RESIDUAL))

from hperp_integral_adapter import HperpIntegralPairingAdapter
from pairing_prefix_engine import RetainedBasisPairingTransform

SCHEMA = "STAGE32EX5_BC2_18_N354_SURVIVOR_EXCEPTIONAL_MOD8_DECOMPOSITION_V1"
EXPECTED_BC2_17_CANONICAL = "a8dd000481a39011bd1d9d108d55e38e0420dbc2bb7abf4851595dfdb5da5072"
EXPECTED_BUNDLE_CANONICAL = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
EXPECTED_MARKING_CANONICAL = "e06291dddfc529fca2c0b0fe58dd43151faccd3d7997d9aa5797e1978227bb7c"
NORMAL_LABELS = list(range(1, 93))
EXCEPTIONAL_LABELS = list(range(93, 141))
X4_LABEL = 49
TARGET_E = 8
TARGET_D = 8
RESIDUAL_EXCEPTIONAL_MASS = 6
DEN = 8


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


def snf_constraints(A: Matrix, rhs_E: Matrix, rhs_x4: Matrix | None = None):
    dm = DomainMatrix.from_Matrix(A).convert_to(ZZ)
    Ddm, Sdm, _ = smith_normal_decomp(dm)
    D = Ddm.to_Matrix()
    S = Sdm.to_Matrix()
    CE = -S * rhs_E
    CX = -S * rhs_x4 if rhs_x4 is not None else None
    constraints = []
    diag_len = min(D.rows, D.cols)
    rank = 0
    invariant_factors = []
    for i in range(D.rows):
        d = int(D[i, i]) if i < diag_len else 0
        if d:
            rank += 1
            invariant_factors.append(abs(d))
            modulus = math.gcd(abs(d), DEN)
        else:
            modulus = DEN
        if modulus == 1:
            continue
        e_coeffs = [int(CE[i, j]) % modulus for j in range(CE.cols)]
        x_coeff = int(CX[i, 0]) % modulus if CX is not None else None
        constraints.append((modulus, e_coeffs, x_coeff))
    return {
        "rank": rank,
        "invariant_factors": invariant_factors,
        "constraints": constraints,
        "constraint_moduli": Counter(m for m, _, _ in constraints),
    }


def constraints_ok(constraints, yE, x4_residue=None) -> bool:
    for modulus, coeffs, xcoeff in constraints:
        v = sum(a * b for a, b in zip(coeffs, yE))
        if xcoeff is not None:
            if x4_residue is None:
                raise ValueError("x4 residue required")
            v += xcoeff * int(x4_residue)
        if v % modulus:
            return False
    return True


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    bc217 = json.loads(BC2_17_EVIDENCE.read_text())
    if bc217.get("canonical_sha256_without_this_field") != EXPECTED_BC2_17_CANONICAL:
        raise ValueError("BC2-17 evidence canonical regression")
    if bc217["picard64_probe"]["result"] != "UNKNOWN" or bc217["picard64_probe"]["reason_unknown"] != "timeout":
        raise ValueError("BC2-17 solver-wall status regression")
    if bc217["retarget"]["selected_target"] != {"row_id": "g1-d008", "g": 1, "d": 8, "e": 8, "survives_n354": True}:
        raise ValueError("BC2-17 retarget regression")
    fixed = {int(k): int(v) for k, v in bc217["retarget"]["fixed_exceptional_pairings"].items()}
    if sum(fixed.values()) != 2 or bc217["retarget"]["residual_exceptional_mass"] != RESIDUAL_EXCEPTIONAL_MASS:
        raise ValueError("BC2-17 exceptional-mass regression")

    bundle = load_retained(RETAINED, "s32ex5_bc218_bundle")
    marking = load_retained(MARKING, "s32ex5_bc218_marking")
    if bundle.get("canonical_sha256") != EXPECTED_BUNDLE_CANONICAL:
        raise ValueError("retained bundle canonical regression")
    if marking.get("canonical_sha256") != EXPECTED_MARKING_CANONICAL:
        raise ValueError("retained marking canonical regression")

    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    transform = RetainedBasisPairingTransform.from_bundle(bundle)
    if transform.den != DEN:
        raise ValueError("selected64 denominator regression")
    selected_labels = [int(v) for v in transform.certificate["selected_known_indices_1based"]]
    if len(selected_labels) != 64:
        raise ValueError("selected64 size regression")
    selected_exceptional = selected_labels[:29]
    selected_normal = selected_labels[29:]
    if len(selected_exceptional) != 29 or any(v <= 92 for v in selected_exceptional):
        raise ValueError("selected exceptional partition regression")
    if len(selected_normal) != 35 or any(v > 92 for v in selected_normal):
        raise ValueError("selected normal partition regression")
    if X4_LABEL not in selected_normal:
        raise ValueError("x4 label left selected normal coordinates")

    B = Matrix(transform.inverse_integer)
    P = Matrix(adapter.pairing_matrix)
    if B.shape != (64, 64) or P.shape != (140, 64):
        raise ValueError("retained matrix shape regression")
    M = P * B

    for j, label in enumerate(selected_labels):
        row = [int(M[label - 1, k]) for k in range(64)]
        expected = [0] * 64
        expected[j] = DEN
        if row != expected:
            raise ValueError(f"selected64 row replay regression at label {label}")

    exceptional_normal_cross_nonzero = []
    for label in EXCEPTIONAL_LABELS:
        for j in range(29, 64):
            q = int(M[label - 1, j])
            if q:
                exceptional_normal_cross_nonzero.append([label, selected_labels[j], q])
    exceptional_decoupled = not exceptional_normal_cross_nonzero
    if not exceptional_decoupled:
        raise ValueError("exceptional pairings do not decouple from selected normal coordinates")

    selected_exc_pos = {label: j for j, label in enumerate(selected_exceptional)}
    fixed_selected = {label: value for label, value in fixed.items() if label in selected_exc_pos}
    fixed_unselected = {label: value for label, value in fixed.items() if label not in selected_exc_pos}
    free_selected = [label for label in selected_exceptional if label not in fixed]
    if sum(fixed.values()) != TARGET_E - RESIDUAL_EXCEPTIONAL_MASS:
        raise ValueError("fixed exceptional total regression")

    BE = B[:, :29]
    BN = B[:, 29:]
    full_snf = snf_constraints(BN, BE)
    x4_global_col = selected_labels.index(X4_LABEL)
    x4_normal_col = x4_global_col - 29
    BN_rest = BN[:, [j for j in range(BN.cols) if j != x4_normal_col]]
    BX = BN[:, x4_normal_col]
    rest_snf = snf_constraints(BN_rest, BE, BX)

    def build_yE(comp):
        y = [0] * 29
        for label, value in fixed_selected.items():
            y[selected_exc_pos[label]] = value
        for label, value in zip(free_selected, comp):
            y[selected_exc_pos[label]] = int(value)
        return y

    unselected_exceptional = [label for label in EXCEPTIONAL_LABELS if label not in selected_exc_pos]
    expected_enum = math.comb(RESIDUAL_EXCEPTIONAL_MASS + len(free_selected), len(free_selected))
    enum_count = 0
    exceptional_feasible = 0
    mod8_compatible = 0
    residue_mask_hist = Counter()
    residue_union = set()
    exc_stream = hashlib.sha256()
    mod_stream = hashlib.sha256()
    first_exceptional = []
    first_modular = []
    support_hist = Counter()
    per_label_min = {label: None for label in EXCEPTIONAL_LABELS}
    per_label_max = {label: None for label in EXCEPTIONAL_LABELS}

    for comp in weak_compositions_at_most(RESIDUAL_EXCEPTIONAL_MASS, len(free_selected)):
        enum_count += 1
        yE = build_yE(comp)
        p = {label: yE[selected_exc_pos[label]] for label in selected_exceptional}
        ok = True
        for label in unselected_exceptional:
            num = sum(int(M[label - 1, j]) * yE[j] for j in range(29))
            if num % DEN:
                ok = False
                break
            val = num // DEN
            if val < 0:
                ok = False
                break
            p[label] = val
        if not ok:
            continue
        if any(p.get(label) != value for label, value in fixed_unselected.items()):
            continue
        if any(p.get(label) != value for label, value in fixed.items()):
            continue
        if sum(p[label] for label in EXCEPTIONAL_LABELS) != TARGET_E:
            continue

        exceptional_feasible += 1
        vec48 = [p[label] for label in EXCEPTIONAL_LABELS]
        rec = {"selected29": yE, "exceptional48": vec48}
        exc_stream.update(json.dumps(rec, sort_keys=True, separators=(",", ":")).encode() + b"\n")
        support_hist[sum(1 for v in vec48 if v)] += 1
        for label, value in p.items():
            lo = per_label_min[label]
            hi = per_label_max[label]
            per_label_min[label] = value if lo is None else min(lo, value)
            per_label_max[label] = value if hi is None else max(hi, value)
        if len(first_exceptional) < 12:
            first_exceptional.append(rec)

        full_ok = constraints_ok(full_snf["constraints"], yE)
        mask = 0
        allowed = []
        for r in range(DEN):
            if constraints_ok(rest_snf["constraints"], yE, r):
                mask |= 1 << r
                allowed.append(r)
        if full_ok != bool(mask):
            raise ValueError("full-vs-x4-residue SNF solvability regression")
        if not full_ok:
            continue

        mod8_compatible += 1
        residue_mask_hist[mask] += 1
        residue_union.update(allowed)
        mrec = {"selected29": yE, "exceptional48": vec48, "x4_residues_mod8": allowed}
        mod_stream.update(json.dumps(mrec, sort_keys=True, separators=(",", ":")).encode() + b"\n")
        if len(first_modular) < 12:
            first_modular.append(mrec)

    if enum_count != expected_enum:
        raise ValueError(f"composition enumeration regression: {enum_count} != {expected_enum}")

    x4_values = [x for x in range(113) if x % DEN in residue_union]
    n355_diagonal_redundant = all(value <= TARGET_D // 2 for value in fixed.values())

    if exceptional_feasible == 0:
        status = "PASS_FIRST_BLOCK_UNSAT_AT_EXCEPTIONAL_PAIRING_RECONSTRUCTION"
        next_id = "BC2_19_RETARGET_UNIFORM_EXCEPTIONAL_RECONSTRUCTION_ACROSS_N354"
    elif mod8_compatible == 0:
        status = "PASS_FIRST_BLOCK_UNSAT_AT_PICARD64_MOD8_INTEGRALITY"
        next_id = "BC2_19_RETARGET_MOD8_OBSTRUCTION_ACROSS_N354"
    else:
        status = "PASS_EXCEPTIONAL_DECOUPLING_AND_MOD8_FILTER_RETAINED_NORMAL_POSITIVITY_REMAINS"
        next_id = "BC2_19_NORMAL_POSITIVITY_MASS_REPLAY_ON_MODULAR_EXCEPTIONAL_CLASSES"

    body = {
        "schema": SCHEMA,
        "stage": "32EX5",
        "unit": "BC2_18_DECOMPOSE_N354_SURVIVOR_PICARD64_PROBE",
        "status": status,
        "source_lock": {
            "bc2_17_evidence_canonical": EXPECTED_BC2_17_CANONICAL,
            "retained_bundle_canonical": EXPECTED_BUNDLE_CANONICAL,
            "retained_marking_canonical": EXPECTED_MARKING_CANONICAL,
            "selected64_denominator": DEN,
        },
        "target": {
            "row_id": "g1-d008", "g": 1, "d": TARGET_D, "e": TARGET_E,
            "first_block": [0, 112], "fixed_exceptional_mass": 2,
            "residual_exceptional_mass": RESIDUAL_EXCEPTIONAL_MASS,
        },
        "selected64_decomposition": {
            "selected_labels_1based": selected_labels,
            "selected_exceptional_labels": selected_exceptional,
            "selected_normal_labels": selected_normal,
            "x4_selected64_index_0based": x4_global_col,
            "exceptional_rows_depend_on_selected_normal_coordinates": False,
            "exceptional_normal_cross_nonzero_count": len(exceptional_normal_cross_nonzero),
            "exceptional_pairing_rank": int(M[92:140, :29].rank()),
        },
        "finite_exceptional_enumeration": {
            "fixed_terminal_exceptional_pairings": {str(k): v for k, v in sorted(fixed.items())},
            "fixed_selected_exceptional_count": len(fixed_selected),
            "fixed_unselected_exceptional_count": len(fixed_unselected),
            "free_selected_exceptional_count": len(free_selected),
            "free_selected_exceptional_labels": free_selected,
            "composition_mass_cap": RESIDUAL_EXCEPTIONAL_MASS,
            "enumerated_selected_assignments": enum_count,
            "exceptional_reconstruction_feasible_count": exceptional_feasible,
            "exceptional_reconstruction_stream_sha256": exc_stream.hexdigest(),
            "support_size_histogram": {str(k): v for k, v in sorted(support_hist.items())},
            "per_exceptional_label_minmax": {str(k): [per_label_min[k], per_label_max[k]] for k in EXCEPTIONAL_LABELS},
            "first_feasible_completions": first_exceptional,
        },
        "picard_integrality_mod8": {
            "meaning": "there exists a selected-normal residue vector modulo 8 making all 64 reconstructed Picard coordinates integral",
            "full_normal_snf_rank": full_snf["rank"],
            "full_normal_nontrivial_constraint_moduli": {str(k): v for k, v in sorted(full_snf["constraint_moduli"].items())},
            "without_x4_snf_rank": rest_snf["rank"],
            "without_x4_nontrivial_constraint_moduli": {str(k): v for k, v in sorted(rest_snf["constraint_moduli"].items())},
            "compatible_exceptional_completion_count": mod8_compatible,
            "compatible_stream_sha256": mod_stream.hexdigest(),
            "x4_allowed_residues_mod8_union": sorted(residue_union),
            "x4_allowed_values_0_112_union": x4_values,
            "x4_residue_mask_histogram": {str(mask): count for mask, count in sorted(residue_mask_hist.items())},
            "first_compatible_completions": first_modular,
        },
        "n355_diagnostic_interaction": {
            "n355_is_not_consumed_as_authority_here": True,
            "known10_diagonal_bound_floor_d_over_2": TARGET_D // 2,
            "fixed_terminal_known10_all_satisfy_bound": n355_diagonal_redundant,
            "therefore_current_n355_prefix_diagonal_cut_prunes_this_first_block_signature": False,
        },
        "credit": {
            "solver_used": False,
            "heavy_compute": False,
            "exceptional_decoupling_exact": True,
            "finite_exceptional_reconstruction_exact": True,
            "picard_integrality_mod8_filter_exact": True,
            "normal_nonnegativity_and_mass_solved": False,
            "whole_first_block_unsat": mod8_compatible == 0,
            "whole_stratum_closed": False,
            "full178_complete": False,
            "stage32_main_credit": False,
            "n350_production_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
        },
        "next_exact_unit": {
            "id": next_id,
            "heavy_scaleout_authorized": False,
            "main_promotion_authorized": False,
        },
        "firewalls": {
            "bc2_17_unknown_relabelled_unsat": False,
            "n355_audit_candidate_self_promoted": False,
            "main_promotion": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
            "merge_authorized": False,
        },
    }
    out = {**body, "canonical_sha256_without_this_field": csha(body)}
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": status,
        "enumerated": enum_count,
        "exceptional_feasible": exceptional_feasible,
        "mod8_compatible": mod8_compatible,
        "x4_residues": sorted(residue_union),
        "next": next_id,
        "canonical": out["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
