#!/usr/bin/env python3
"""Verify that all seven safe geometric signs fix the four J2 row candidates.

The raw 75D target and V4-extension compatibility are intentionally absent.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
LEGACY = HERE.parent / "33-07"
CERT = HERE / "j2-marked-order4-geometric-sign-indistinguishability.json"
LABEL_GAP = HERE / "j2-marked-order4-lift-label-gap.json"
U1 = HERE / "j2-semantic-u1-full-surface-smith-source.json"
PROPER = LEGACY / "proper-brauer2-from-discriminant.json"
SIGNS = LEGACY / "retained-q256-geometric-sign-endpoint.json"
KC_AUT = HERE / "j2-kc-automorphism-mod2-marking-rejection.json"
GLUE_GAP = HERE / "j2-marked-glue-geometric-sign-route-gap.json"

LOCKS = {
    LABEL_GAP: "4ca10da7ea214258dd57d1e42c2dc7ea7b66ae29c8cfd5b75ecd6a3eb0fd0101",
    U1: "ae5a9b45e4e4d9b50d8685d1c4649725dadf4956f246e18b33cb601aef94a2ec",
    PROPER: "c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf",
    SIGNS: "19d59e89b87d49681ae8b1b165085d529bef64b40c2d5ab6fe692a6b899fb061",
    KC_AUT: "dfbd85c56c3c9c29238e1da633baec2ed2bd8cc58021c8137e95fb1cf9cd74fb",
    GLUE_GAP: "23b6fc3e9cf666e81f0c11c4c57c7070a1cc4c459c35515a6d934db3a84f3ee9",
}


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def locked(path: Path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == LOCKS[path] == csha(body), path
    return obj


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def rowmul(vector, matrix):
    return [sum((int(vector[i]) & 1) * (int(matrix[i][j]) & 1) for i in range(len(vector))) & 1 for j in range(len(matrix[0]))]


def restrict_two(matrix, moduli):
    scales = [modulus // 2 for modulus in moduli]
    out = []
    for i in range(14):
        row = []
        for j in range(14):
            numerator = scales[i] * int(matrix[i][j])
            assert numerator % scales[j] == 0
            row.append((numerator // scales[j]) & 1)
        out.append(row)
    return out


def rank_f2(rows):
    work = [[int(value) & 1 for value in row] for row in rows]
    rank = 0
    for column in range(len(work[0]) if work else 0):
        pivot = next((i for i in range(rank, len(work)) if work[i][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        for i in range(len(work)):
            if i != rank and work[i][column]:
                work[i] = [a ^ b for a, b in zip(work[i], work[rank])]
        rank += 1
    return rank


cert = json.loads(CERT.read_text(encoding="utf-8"))
body = dict(cert)
claimed = body.pop("canonical_sha256")
assert claimed == csha(body)
gap = locked(LABEL_GAP)
u1 = locked(U1)
proper = locked(PROPER)
signs = locked(SIGNS)
kc_aut = locked(KC_AUT)
glue_gap = locked(GLUE_GAP)

assert cert["source_locks"] == {
    "kc_automorphism_mod2_rejection_sha256": LOCKS[KC_AUT],
    "marked_glue_geometric_sign_route_gap_sha256": LOCKS[GLUE_GAP],
    "order4_lift_label_gap_sha256": LOCKS[LABEL_GAP],
    "proper_brauer2_sha256": LOCKS[PROPER],
    "retained_q256_geometric_sign_endpoint_sha256": LOCKS[SIGNS],
    "semantic_u1_full_surface_smith_source_sha256": LOCKS[U1],
}
assert glue_gap["exact_findings"]["seven_geometric_coordinate_sign_involutions_are_safe_inputs"] is True
assert kc_aut["all_integral_isometries_reduce_to_identity_mod2"] is True
assert signs["coordinate_order"] == ["a1", "a2", "a3", "b1", "b2", "b3", "c"]
assert signs["seven_sign_involutions_commute"] is True
assert signs["seven_sign_product_identity"] is True

moduli = signs["discriminant_moduli"]
a_signs = [restrict_two(matrix, moduli) for matrix in signs["sign_actions_mixed_moduli"]]
b_signs = [transpose(matrix) for matrix in a_signs]
assert transpose(restrict_two(signs["cc_action_mixed_moduli"], moduli)) == proper["proper_Br2_cc_action_f2"]
assert transpose(restrict_two(signs["ct_action_mixed_moduli"], moduli)) == proper["proper_Br2_ct_action_f2"]

u1_row = u1["exact_normalization"]["full_surface_A_T_2_coordinates_f2"]
assert all(rowmul(u1_row, matrix) == u1_row for matrix in a_signs)

candidates = gap["exact_enumeration"]["joint_v4_fixed_functionals"]
assert [row["retained10_mask_decimal"] for row in candidates] == [4, 5, 6, 7]
for candidate in candidates:
    row = candidate["proper14_f2"]
    assert all(rowmul(row, matrix) == row for matrix in b_signs)

base_proper = candidates[0]["proper14_f2"]
base_retained = candidates[0]["retained10_f2"]
directions_proper = [
    [a ^ b for a, b in zip(base_proper, candidates[1]["proper14_f2"])],
    [a ^ b for a, b in zip(base_proper, candidates[2]["proper14_f2"])],
]
directions_retained = [
    [a ^ b for a, b in zip(base_retained, candidates[1]["retained10_f2"])],
    [a ^ b for a, b in zip(base_retained, candidates[2]["retained10_f2"])],
]
assert rank_f2(directions_proper) == rank_f2(directions_retained) == 2
assert [a ^ b ^ c for a, b, c in zip(base_proper, *directions_proper)] == candidates[3]["proper14_f2"]

affine = cert["exact_affine_ambiguity"]
assert affine["affine_base_proper14_f2"] == base_proper
assert affine["affine_base_retained10_f2"] == base_retained
assert affine["direction_proper14_f2"] == directions_proper
assert affine["direction_retained10_f2"] == directions_retained
assert affine["affine_dimension_f2"] == 2

result = cert["exact_geometric_sign_result"]
assert result["candidate_count_before_seven_sign_fixedness"] == 4
assert result["candidate_count_after_seven_sign_fixedness"] == 4
assert result["geometric_sign_constraint_rank_on_candidate_affine_plane_f2"] == 0
assert result["safe_geometric_signs_distinguish_named_j2_row"] is False
assert cert["minimal_missing_information"]["minimum_independent_binary_constraints_on_current_affine_slice"] == 2

fw = cert["promotion_firewall"]
assert fw["candidate_masks_4_5_6_7_promoted"] is False
assert fw["geometric_sign_fixedness_used_as_label_selection"] is False
assert fw["raw_75D_target_used"] is False
assert fw["historical_mask6_restored"] is False
assert fw["marked_adapter_materialized"] is False

print(json.dumps({
    "success": True,
    "status": cert["status"],
    "candidate_masks_before_signs": [4, 5, 6, 7],
    "candidate_masks_after_signs": [4, 5, 6, 7],
    "geometric_sign_constraint_rank_f2": 0,
    "remaining_affine_dimension_f2": 2,
    "minimum_cross_marking_bits_needed": 2,
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
