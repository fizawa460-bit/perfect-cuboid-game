#!/usr/bin/env python3
"""Source-lock the named J2 binary functional under the two Kc swaps."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "j2-order4-swap-functional-source-v21.json"
LOCKS = {
    "v20_quotient": (
        HERE / "j2-order4-named-functional-quotient-v20.json",
        "1b53db254c381721c0c648bab41c276ec79f69f6e1f81235993936df3e25232e",
    ),
    "semantic_orientation": (
        HERE / "j2-cv-d2-semantic-orientation.json",
        "0a5abe419c3bd2e4c523af50fd8f85858af6a0d957dcce1e3bdf2ff1430fed3e",
    ),
    "order4_reduction": (
        HERE / "j2-order4-brauer-lift-reduction.json",
        "a524121930e1c712bd8d8220415ef1836b11cd6eb11f2bb44f70dc844f6d85b0",
    ),
    "kc_isometry_rejection": (
        HERE / "j2-kc-automorphism-mod2-marking-rejection.json",
        "dfbd85c56c3c9c29238e1da633baec2ed2bd8cc58021c8137e95fb1cf9cd74fb",
    ),
    "actual_swap_descent": (
        HERE / "j2-actual-swap-mixed-discriminant-descent.json",
        "93dc99201a04fdec7c8ad8369409e7cb593ae7f8fba44b772df1b2cc1d29cfa3",
    ),
}
UPSTREAM = {
    "repository": "MichaelStollBayreuth/Verification",
    "commit": "51233ed5ef2bf228fac9416c66db9adc0ebcaadd",
    "path": "Cuboids/cuboids.magma",
    "git_blob_sha1": "0422b69847f2afb97cb7b3ed02ebef91279f61b1",
    "raw_sha256": "5dc3ae961d872ff96420385880edf0f4225a12d3f906c614e1ccd2220399ce89",
    "surface_swap_lines_175_177": [
        "[a2,a1,a3,b2,b1,b3,c]",
        "[a3,a2,a1,b3,b2,b1,c]",
    ],
    "kc_swap_lines_487_489": [
        "[A2,A1,A3,B2,B1,B3]",
        "[A3,A2,A1,B3,B2,B1]",
    ],
}


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def locked(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text())
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body), path
    return obj


data = {name: locked(path, digest) for name, (path, digest) in LOCKS.items()}

# Exact substitutions from the pinned source. Coordinates are zero-based here:
# S=(a1,a2,a3,b1,b2,b3,c), Kc=(A1,A2,A3,B1,B2,B3).
s_swaps = {
    "swap12": [1, 0, 2, 4, 3, 5, 6],
    "swap13": [2, 1, 0, 5, 4, 3, 6],
}
kc_swaps = {
    "swap12": [1, 0, 2, 4, 3, 5],
    "swap13": [2, 1, 0, 5, 4, 3],
}
projection = [0, 1, 2, 3, 4, 5]
kc_equations = [((0, 1), 5), ((1, 2), 3), ((0, 2), 4)]


def image_equation(eq, subst):
    pos, neg = eq
    return (tuple(sorted(subst[i] for i in pos)), subst[neg])


equivariance = {}
for name in ("swap12", "swap13"):
    ss, ks = s_swaps[name], kc_swaps[name]
    assert [ss[i] for i in projection] == [projection[ks[i]] for i in range(6)]
    images = [image_equation(eq, ks) for eq in kc_equations]
    assert sorted(images) == sorted(kc_equations)
    equivariance[name] = {
        "surface_substitution_zero_based": ss,
        "kc_substitution_zero_based": ks,
        "projection_commutes_exactly": True,
        "kc_equation_permutation_zero_based": [kc_equations.index(x) for x in images],
        "kc_automorphism_exact": True,
    }

orientation = data["semantic_orientation"]
reduction = data["order4_reduction"]
assert orientation["exact_conclusion"]["named_CV_J2_semantic_discriminant_label"] == "u1"
assert orientation["anti_isometry_check"]["generator"] == "t1/4"
assert reduction["marked_kc_normalization"]["named_functional"] == "beta1=t1/8 mod T*"
assert reduction["marked_kc_normalization"]["binary_evaluations_on_marked_T_basis_f2"] == [1, 0]

iso = data["kc_isometry_rejection"]
assert iso["transcendental_lattice_gram"] == [[4, 0], [0, 8]]
isometries = iso["integral_isometry_group_exact"]
assert len(isometries) == 4
order4_images = []
for m in isometries:
    assert m[0][1] == m[1][0] == 0
    assert abs(m[0][0]) == abs(m[1][1]) == 1
    order4_images.append([m[0][0] % 4, 0])
    assert [m[0][0] % 2, m[0][1] % 2] == [1, 0]
assert sorted(order4_images) == [[1, 0], [1, 0], [3, 0], [3, 0]]

v20 = data["v20_quotient"]
s3 = v20["actual_s3_action_on_two_bit_quotient"]
assert s3["unique_joint_fixed_mask"] == 6
records = v20["exact_quotient"]["affine_plane_records"]
named = next(x for x in records if x["retained10_mask_decimal"] == 6)
assert named["proper14_mask_decimal"] == 25

out = {
    "schema": "STAGE33_12_J2_ORDER4_SWAP_FUNCTIONAL_SOURCE_V21",
    "stage": "33-12",
    "status": "PASS_EXACT_SOURCE_FIRST_NAMED_FUNCTIONAL_MATERIALIZED",
    "source_locks": {name: digest for name, (_, digest) in LOCKS.items()},
    "pinned_upstream": UPSTREAM,
    "exact_geometric_equivariance": {
        "surface_coordinate_order": ["a1", "a2", "a3", "b1", "b2", "b3", "c"],
        "kc_coordinate_order": ["A1", "A2", "A3", "B1", "B2", "B3"],
        "projection": "forget c",
        "kc_equations": ["A1^2+A2^2-B3^2", "A2^2+A3^2-B1^2", "A1^2+A3^2-B2^2"],
        "swaps": equivariance,
        "pullback_naturality_applies": True,
    },
    "named_order4_functional_behavior": {
        "transcendental_gram": [[4, 0], [0, 8]],
        "integral_isometry_group": isometries,
        "semantic_order4_generator": "t1/4",
        "possible_order4_images_mod_T_coordinates_mod4": order4_images,
        "order4_element_itself_claimed_fixed": False,
        "named_binary_functional": "beta1",
        "named_binary_functional_coordinate_f2": [1, 0],
        "named_binary_functional_fixed_under_every_kc_isometry": True,
        "named_binary_functional_fixed_under_swap12": True,
        "named_binary_functional_fixed_under_swap13": True,
        "reason": "the Kc swaps act on t1/4 by sign; sign is invisible in the induced F2-valued beta1 functional",
    },
    "named_full_surface_source": {
        "selection_rule": "source-side Kc functional naturality plus the exact actual full-surface swap action",
        "unique_joint_fixed_candidate_used_after_named_functional_fixedness_proved": True,
        "proper14_f2": named["proper14_f2"],
        "proper14_mask_decimal": named["proper14_mask_decimal"],
        "retained10_f2": named["retained10_f2"],
        "retained10_mask_decimal": named["retained10_mask_decimal"],
        "two_bit_value_a_b": named["quotient_bits_ab"],
        "source_coordinate_materialized": True,
    },
    "anti_inference": {
        "semantic_u1_fixedness_used_to_assert_order4_element_fixed": False,
        "historical_mask6_binding_reused": False,
        "target_compatibility_used_to_select_source": False,
        "picard_adjoint_binding_reused": False,
    },
    "promotion_scope": {
        "source_coordinate_only": True,
        "named_source_target_relation_materialized": False,
        "finite_v4_kummer_columns_materialized": 0,
        "stage33_progress": "6/11",
        "stage33_12_closed_exact": False,
        "stage33_13_released": False,
        "theorem_credit": False,
        "receiver_credit": False,
        "endpoint_credit": False,
    },
}
out["canonical_sha256"] = csha(out)
if "--check" in sys.argv:
    assert locked(OUT, out["canonical_sha256"]) == out
else:
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps({
    "success": True,
    "proper14_mask": named["proper14_mask_decimal"],
    "retained10_mask": named["retained10_mask_decimal"],
    "two_bit_value_a_b": named["quotient_bits_ab"],
    "source_coordinate_materialized": True,
    "relation_materialized": False,
    "canonical_sha256": out["canonical_sha256"],
    "marker": "PROOF_REPLAY_COMPLETE",
}, sort_keys=True))
