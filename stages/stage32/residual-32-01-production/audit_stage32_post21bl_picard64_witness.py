#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy
from sympy import Matrix

from diagnose_stage32_21ak_affine_2adic_membership import reconstruct_translation_data
from direct_picard_reynolds_lattice_diagnostic import csha, load_retained
from hperp_integral_adapter import RETAINED_BASIS_KNOWN_LABELS_1BASED

EXPECTED_21BL_CANONICAL = "ac88fb355252750e6afdc10cbb54abec24babbad57c25090c017f9a55ac93a44"
EXPECTED_ADAPTER_CANONICAL = "ef3f21e4166d4bfcacce3503213b0a72afee5f5002ab7145de01fc9c54d47038"
EXPECTED_WITNESS_SHA256 = "1a131595c87cf9c5d54ef97dba62261eeb3dda7bb92a5a9fa62c280f46bc4137"
EXPECTED_PICARD_SHA256 = "0fcbe0c9cdf894a95704bcaf55536290fc2daa736387169c891e8262f2c565a7"
EXPECTED_PAIRINGS_SHA256 = "1968dba54ebe2082c6ed07203ea9e4118460f60c32c60d46292bc73dc6bdf961"
EXPECTED_PICARD_RANK = 64
EXPECTED_AFFINE_RANK = 59
SCHEMA = "STAGE32_POST21BL_FRESH_PICARD64_PAIRING_INVERSION_AUDIT_V1"


def sha256_json(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_canonical(path: Path, expected: str) -> dict:
    payload = json.loads(path.read_text())
    claimed = payload.pop("canonical_sha256_without_this_field")
    if claimed != expected or csha(payload) != expected:
        raise ValueError(f"canonical regression for {path}: {claimed}")
    payload["canonical_sha256_without_this_field"] = claimed
    return payload


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--evidence21bl", type=Path, required=True)
    ap.add_argument("--adapter-evidence", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    source = load_canonical(args.evidence21bl, EXPECTED_21BL_CANONICAL)
    adapted = load_canonical(args.adapter_evidence, EXPECTED_ADAPTER_CANONICAL)
    if source["result"]["witness_sha256"] != EXPECTED_WITNESS_SHA256:
        raise ValueError("21bl witness SHA regression")
    if adapted["status"] != "PASS_POST21BL_EXACT_PICARD64_SLICE_WITNESS":
        raise ValueError("adapter evidence is not PASS")

    bundle = load_retained(args.retained, "s32_post21bl_audit_picard")
    marking = load_retained(args.marking, "s32_post21bl_audit_marking")
    data = reconstruct_translation_data(marking, bundle)
    gram = Matrix(bundle["picard_gram_64x64"])
    if gram.shape != (EXPECTED_PICARD_RANK, EXPECTED_PICARD_RANK):
        raise ValueError("Picard Gram rank regression")

    # Rebuild the exact 21bl pairing vector from its source witness. This audit
    # intentionally does NOT import or call the producing adapter.
    z = Matrix([int(v) for v in source["target"]["z"]])
    r = Matrix([int(v) for v in source["result"]["witness_r_reduced"]])
    M = data["M"]
    pivots = tuple(int(v) for v in data["pivot_rows"])
    selected_M = M.extract(list(pivots), list(range(EXPECTED_AFFINE_RANK)))
    reduced_rows, Trow = selected_M.T.lll_transform()
    if reduced_rows != Trow * selected_M.T:
        raise ValueError("audit LLL transform regression")
    U = Trow.T
    if abs(int(U.det())) != 1:
        raise ValueError("audit reduced transform not unimodular")
    y = data["pairing_x0_map"] * z + M * U * r
    y_values = [int(y[i, 0]) for i in range(y.rows)]

    # Independent reconstruction: select pairings against the retained Picard
    # basis and invert its Gram matrix, rather than using x=x0+KUr.
    retained_idx = [int(v) - 1 for v in RETAINED_BASIS_KNOWN_LABELS_1BASED]
    pairing_matrix = data["adapter"].pairing_matrix
    retained_pairing_block = pairing_matrix.extract(
        retained_idx, list(range(EXPECTED_PICARD_RANK))
    )
    retained_pairing_block_is_gram = retained_pairing_block == gram
    if not retained_pairing_block_is_gram:
        raise ValueError("retained pairing block is not the Picard Gram")
    y_basis = Matrix([y[i, 0] for i in retained_idx])
    xq = gram.inv() * y_basis
    picard_integral = all(sympy.denom(v) == 1 for v in xq)
    if not picard_integral:
        raise ValueError("pairing inversion produced a nonintegral Picard class")
    x = Matrix([int(v) for v in xq])
    x_values = [int(x[i, 0]) for i in range(x.rows)]

    all140_replay_exact = pairing_matrix * x == y
    source_pairings_match_persisted = y_values == [
        int(v) for v in adapted["all140"]["pairings"]
    ]
    picard_matches_persisted = x_values == [
        int(v) for v in adapted["reconstruction"]["picard_coordinates"]
    ]
    picard_sha = sha256_json(x_values)
    pairing_sha = sha256_json(y_values)

    fixed_projection_exact = data["C"] * x == z
    reynolds_numerator_exact = data["N"] * x == data["B"] * z

    bridge = data["bridge"]
    phi = Matrix([
        list(bridge.degree_functional),
        list(bridge.exceptional_mass_functional),
        list(bridge.first_normal_half_functional),
    ])
    actual_slice = [int(v) for v in phi * x]
    expected_slice = [
        int(adapted["target"]["degree"]),
        int(adapted["target"]["e"]),
        int(adapted["target"]["a"]),
    ]
    slice_exact = actual_slice == expected_slice
    target_image_exact = bridge.target_in_image(*expected_slice)

    self_square = int((x.T * gram * x)[0])
    genus = int(adapted["target"]["genus"])
    degree = int(adapted["target"]["degree"])
    required_lower = -degree - 2 + 2 * genus
    self_square_threshold_exact = self_square >= required_lower
    all140_nonnegative = min(y_values) >= 0
    zero_pairing_count = sum(1 for v in y_values if v == 0)

    checks = {
        "retained_pairing_block_is_gram": retained_pairing_block_is_gram,
        "picard_integral": picard_integral,
        "all140_replay_exact": all140_replay_exact,
        "source_pairings_match_persisted": source_pairings_match_persisted,
        "picard_matches_persisted": picard_matches_persisted,
        "picard_sha_matches": picard_sha == EXPECTED_PICARD_SHA256,
        "pairing_sha_matches": pairing_sha == EXPECTED_PAIRINGS_SHA256,
        "fixed_projection_exact": fixed_projection_exact,
        "reynolds_numerator_exact": reynolds_numerator_exact,
        "slice_exact": slice_exact,
        "target_image_exact": target_image_exact,
        "all140_nonnegative": all140_nonnegative,
        "self_square_threshold_exact": self_square_threshold_exact,
        "self_square_matches_persisted": self_square
        == int(adapted["quadratic"]["picard_self_square"]),
    }
    passed = all(checks.values())
    verdict = (
        "PASS_STAGE32_POST21BL_FRESH_PICARD64_PAIRING_INVERSION_AUDIT"
        if passed
        else "FAIL_STAGE32_POST21BL_FRESH_PICARD64_PAIRING_INVERSION_AUDIT"
    )

    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "verdict": verdict,
        "mode": "FRESH_PAIRING_VECTOR_TO_RETAINED_PICARD_BASIS_INVERSION_WITHOUT_CALLING_THE_PRODUCING_ADAPTER",
        "source": {
            "21bl_canonical_sha256": EXPECTED_21BL_CANONICAL,
            "adapter_evidence_canonical_sha256": EXPECTED_ADAPTER_CANONICAL,
            "21bl_witness_sha256": EXPECTED_WITNESS_SHA256,
            "retained_bundle_sha256": bundle["canonical_sha256"],
            "adapter_certificate_sha256": data["adapter"].certificate[
                "canonical_sha256_without_this_field"
            ],
            "bridge_certificate_sha256": bridge.certificate[
                "canonical_sha256_without_this_field"
            ],
        },
        "checks": checks,
        "result": {
            "picard_rank": EXPECTED_PICARD_RANK,
            "picard_coordinates_sha256": picard_sha,
            "all140_pairings_sha256": pairing_sha,
            "minimum_pairing": min(y_values),
            "maximum_pairing": max(y_values),
            "zero_pairing_count": zero_pairing_count,
            "actual_d_e_a": actual_slice,
            "expected_d_e_a": expected_slice,
            "picard_self_square": self_square,
            "required_lower": required_lower,
            "slack": self_square - required_lower,
        },
        "credit_firewalls": {
            "representative_sample_only": True,
            "not_full178_numerical_credit": True,
            "picard_class_is_not_effective_curve_existence": True,
            "receiver_credit": False,
            "theorem_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": verdict,
        "checks": checks,
        "self_square": self_square,
        "required_lower": required_lower,
        "slack": self_square - required_lower,
        "actual_d_e_a": actual_slice,
        "minimum_pairing": min(y_values),
        "zero_pairing_count": zero_pairing_count,
        "picard_sha256": picard_sha,
        "pairings_sha256": pairing_sha,
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
