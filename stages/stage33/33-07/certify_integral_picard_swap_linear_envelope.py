#!/usr/bin/env python3
"""Certify the exact Picard-level linear envelope for two coordinate swaps.

This uses only the retained integral 64 x 64 Picard Gram, cc/ct actions, and
seven coordinate-sign actions.  It does not call the public Magma calculator.
The two desired swaps must commute with cc/ct and conjugate the sign actions as
(a1 a2)(b1 b2) and (a1 a3)(b1 b3).  Over Q, simultaneous eigenspaces make the
dimension of each corresponding intertwiner space completely explicit.

This is a necessary-condition envelope, not an integral-isometry
classification: integrality, Gram preservation, involutivity and the S3 braid
relation are deliberately not inferred from the linear Hom-space dimension.
"""
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from picard_base_rows_retained import load as load_base  # noqa: E402
from picard_coordinate_sign_rows_retained import load as load_signs  # noqa: E402

OUT = HERE / "integral-picard-swap-linear-envelope.json"
BASE_LOCK = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
SIGN_LOCK = "5cd64ca89ee9f3ec76d275bc4082349764ac8a5cb4647a9bb9a4eaf267b76ab9"


def canonical_sha256(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


base = load_base()
sign = load_signs()
if base["canonical_sha256"] != BASE_LOCK or sign["canonical_sha256"] != SIGN_LOCK:
    raise SystemExit("retained integral Picard lock moved")

Q = sp.Matrix(base["picard_gram_64x64"])
names = ["cc", "ct"] + list(sign["coordinate_order"])
rows = [
    base["picard_action_cc_64x64"],
    base["picard_action_ct_64x64"],
] + [sign["picard_actions_64x64"][name] for name in sign["coordinate_order"]]
actions = [sp.Matrix(x) for x in rows]
I = sp.eye(64)

if Q.shape != (64, 64) or Q != Q.T or Q.det() != -268435456:
    raise SystemExit("retained Picard Gram regression")
if any(A * A != I or A * Q * A.T != Q for A in actions):
    raise SystemExit("retained action ceased to be an involutive Picard isometry")
if any(actions[i] * actions[j] != actions[j] * actions[i]
       for i in range(len(actions)) for j in range(len(actions))):
    raise SystemExit("retained cc/ct/sign actions ceased to commute")
prod = I
for A in actions[2:]:
    prod *= A
if prod != I:
    raise SystemExit("seven-sign projective product relation moved")

# Coordinate columns transform by A^T because retained action rows are the
# images of the Picard basis.  Split Q^64 successively into exact joint
# eigenspaces.  Keys are the nine eigenvalues in names order.
spaces = {(): I}
for A in actions:
    nxt = {}
    AT = A.T
    for character, V in spaces.items():
        for eigenvalue in (1, -1):
            kernel = ((AT - eigenvalue * I) * V).nullspace()
            if kernel:
                nxt[character + (eigenvalue,)] = V * sp.Matrix.hstack(*kernel)
    spaces = nxt

if sum(V.cols for V in spaces.values()) != 64:
    raise SystemExit("joint eigenspaces do not span Picard_Q")

# Distinct joint characters must be Q-orthogonal.  This independently checks
# that the simultaneous decomposition and row/column convention agree.
items = sorted(spaces.items())
for i, (chi, V) in enumerate(items):
    if V.rank() != V.cols or (V.T * Q * V).det() == 0:
        raise SystemExit(f"degenerate joint character block {chi}")
    for psi, W in items[i + 1:]:
        if V.T * Q * W != sp.zeros(V.cols, W.cols):
            raise SystemExit(f"nonorthogonal distinct characters {chi} {psi}")

# Indices: cc,ct,a1,a2,a3,b1,b2,b3,c.  For an involutive label
# permutation, precomposition and postcomposition induce the same character
# permutation.
swap_permutations = {
    "swap12": [0, 1, 3, 2, 4, 6, 5, 7, 8],
    "swap13": [0, 1, 4, 3, 2, 7, 6, 5, 8],
}
dims = {chi: V.cols for chi, V in spaces.items()}
hom_dimensions = {}
for swap_name, perm in swap_permutations.items():
    total = 0
    for chi, dim in dims.items():
        image = tuple(chi[perm[j]] for j in range(len(names)))
        if image not in dims or dims[image] != dim:
            raise SystemExit(f"{swap_name} does not preserve character multiplicities")
        total += dim * dims[image]
    hom_dimensions[swap_name] = total

hist = Counter(dims.values())
if len(spaces) != 40 or hist != Counter({1: 21, 2: 18, 7: 1}):
    raise SystemExit(f"joint character multiplicity regression: {hist}")
if hom_dimensions != {"swap12": 142, "swap13": 142}:
    raise SystemExit(f"Picard swap Hom dimension regression: {hom_dimensions}")

records = []
for chi, V in items:
    records.append({
        "eigenvalues_in_generator_order": list(chi),
        "multiplicity": V.cols,
        "restricted_gram_rank": (V.T * Q * V).rank(),
    })

cert = {
    "schema": "STAGE33_07_INTEGRAL_PICARD_SWAP_LINEAR_ENVELOPE_V1",
    "source_locks": {
        "retained_picard_base_bundle_sha256": BASE_LOCK,
        "retained_seven_sign_picard_bundle_sha256": SIGN_LOCK,
        "upstream_git_blob_sha1": base["upstream_git_blob_sha1"],
    },
    "generator_order": names,
    "exact_joint_character_decomposition": {
        "character_count": len(spaces),
        "multiplicity_histogram": {str(k): hist[k] for k in sorted(hist)},
        "maximum_multiplicity": max(hist),
        "total_dimension": sum(dims.values()),
        "distinct_character_blocks_pairwise_gram_orthogonal": True,
        "all_character_blocks_gram_nondegenerate": True,
        "records": records,
    },
    "coordinate_swap_linear_envelope_over_Q": {
        "swap12_intertwiner_dimension": hom_dimensions["swap12"],
        "swap13_intertwiner_dimension": hom_dimensions["swap13"],
        "swap12_preserves_character_multiplicities": True,
        "swap13_preserves_character_multiplicities": True,
        "actual_integral_picard_swap_identified": False,
        "gram_isometry_imposed_on_unknown_swap": False,
        "integrality_imposed_on_unknown_swap": False,
        "involutions_and_S3_braid_imposed_on_unknown_swaps": False,
    },
    "exact_information_boundary": {
        "public_magma_required_for_this_certificate": False,
        "linear_conjugacy_conditions_alone_determine_actual_swaps": False,
        "required_new_geometric_distinguisher": (
            "an exact integral curve-class or ample-cone marking, an equivalent "
            "integral Picard quotient transport, or genuine middle-Gersten lift data"
        ),
        "connecting_matrix_columns_materialized": 0,
        "middle_gersten_module_action_materialized": False,
        "project_14x26_L_squareclass_tensor_materialized": False,
        "absolute_delta_loc_computed": False,
    },
    "project_status": {
        "actual_index512_glue_identified": False,
        "arithmetic_HS_closed": False,
        "stage33_progress": "6/11",
        "stage33_08_released": False,
        "theorem_credit": False,
        "endpoint_credit": False,
        "perfect_cuboid_existence_claim": False,
        "perfect_cuboid_nonexistence_claim": False,
    },
    "next_exact_leaf": (
        "L33-07-MATERIALIZE-INTEGRAL-CURVE-CLASS-OR-AMPLE-CONE-SWAP-DISTINGUISHER-"
        "OR-GENUINE-MIDDLE-GERSTEN-LIFT-DATA"
    ),
}
cert["canonical_sha256"] = canonical_sha256(cert)
OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "joint_character_count": len(spaces),
    "multiplicity_histogram": cert["exact_joint_character_decomposition"]["multiplicity_histogram"],
    "swap12_intertwiner_dimension": hom_dimensions["swap12"],
    "swap13_intertwiner_dimension": hom_dimensions["swap13"],
    "actual_integral_picard_swap_identified": False,
    "certificate_sha256": cert["canonical_sha256"],
    "next_exact_leaf": cert["next_exact_leaf"],
}, indent=2, sort_keys=True))
