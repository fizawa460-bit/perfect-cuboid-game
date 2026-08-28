#!/usr/bin/env python3
"""Refine the Stage33-11c smallest source blocks inside the exact naturality envelope.

This does not choose a Gersten lift.  It computes, for the five smallest named
source directions isolated by the 33-11b profiler, the exact value subspaces
that remain possible under all seven coordinate signs plus the two actual
coordinate swaps.  For the finite H1(V4,K) factor it also restricts those value
subspaces to H1(<cc>,K) x H1(<ct>,K), so the next explicit Gersten calculation
knows the smallest receiver subspace it must distinguish.

A2_26 is source-locked as the four-edge rectangle
  SIDE_021 -- EXC_046
  SIDE_021 -- EXC_047
  SIDE_022 -- EXC_046
  SIDE_022 -- EXC_047.
No connecting column is promoted by this profiler.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "profile_stage33_11_equivariant_forced_zero_blocks.py"
STAGE07 = HERE.parent / "33-07"
BR2 = STAGE07 / "proper-brauer2-from-discriminant.json"
RECEIVER = STAGE07 / "order2-localization-receiver.json"
OUT = HERE / "stage33-11-smallest-block-target-images.json"

EXPECTED_BR2 = "c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf"
EXPECTED_RECEIVER = "9280846c6e7ae8a043e36c7b5498f11476901567b229b94e953b79afab891bda"
QDIM, KDIM, H1DIM = 26, 14, 16
SMALLEST = [2, 3, 24, 25, 26]


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_locked(path: Path, expected: str):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise SystemExit(f"source lock moved for {path.name}: claimed={claimed} actual={actual}")
    return obj


def row_basis(rows, ncols):
    a = [[int(x) & 1 for x in row] for row in rows if any(int(x) & 1 for x in row)]
    if any(len(row) != ncols for row in a):
        raise SystemExit("GF2 row width regression")
    r = 0
    for c in range(ncols):
        p = next((i for i in range(r, len(a)) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        for i in range(len(a)):
            if i != r and a[i][c]:
                a[i] = [x ^ y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return a[:r]


def rank2(rows, ncols):
    return len(row_basis(rows, ncols))


def quotient_image_rank(images, quotient_subspace, ncols):
    base = rank2(quotient_subspace, ncols)
    return rank2(quotient_subspace + images, ncols) - base


def eval_space(hom_basis, source_index0, tdim):
    rows = [
        [int(flat[source_index0 * tdim + j]) & 1 for j in range(tdim)]
        for flat in hom_basis
    ]
    return row_basis(rows, tdim)


def combine(coords, basis):
    out = [0] * len(basis[0])
    for bit, row in zip(coords, basis):
        if int(bit) & 1:
            out = [x ^ (int(y) & 1) for x, y in zip(out, row)]
    return out


# Execute 33-11b once and retain its exact Hom bases and first-residue records.
ns = {"__name__": "__main__", "__file__": str(BASE)}
exec(compile(BASE.read_text(encoding="utf-8"), str(BASE), "exec"), ns)
K_hom_basis = ns["K_hom_basis"]
H1_hom_basis = ns["H1_hom_basis"]
if len(K_hom_basis) != 24 or len(H1_hom_basis) != 33:
    raise SystemExit("33-11a Hom dimensions moved")

# First-residue records are exposed through the nested exact source verifier.
base_ns = ns["base_ns"]
source_records = base_ns["source_records"]
if len(source_records) != QDIM:
    raise SystemExit("source record dimension moved")

a26 = source_records[25]
expected_a26_components = {
    "SIDE_021": ["X_0125", "X_0126"],
    "SIDE_022": ["X_0131", "X_0132"],
    "EXC_046": ["X_0125", "X_0131"],
    "EXC_047": ["X_0126", "X_0132"],
}
actual_a26_components = {
    rec["component_id"]: rec["selected_edge_ids"]
    for rec in a26["component_first_residue_functions"]
}
if a26["source_basis_name"] != "A2_26":
    raise SystemExit("A2_26 source ordering moved")
if int(a26["selected_crossing_count"]) != 4 or int(a26["nontrivial_component_function_count"]) != 4:
    raise SystemExit("A2_26 no longer has the four-edge/four-component shape")
if actual_a26_components != expected_a26_components:
    raise SystemExit(f"A2_26 rectangle incidence moved: {actual_a26_components}")
if not a26["raw_order2_first_residue_function_liftable"]:
    raise SystemExit("A2_26 lost raw order-two liftability")

# Reconstruct finite H1 generator restrictions in exactly the retained basis.
br2 = load_locked(BR2, EXPECTED_BR2)
receiver = load_locked(RECEIVER, EXPECTED_RECEIVER)
G = [[int(x) & 1 for x in row] for row in br2["proper_Br2_cc_action_f2"]]
H = [[int(x) & 1 for x in row] for row in br2["proper_Br2_ct_action_f2"]]
I = [[int(i == j) for j in range(KDIM)] for i in range(KDIM)]
bcc = row_basis([[G[i][j] ^ I[i][j] for j in range(KDIM)] for i in range(KDIM)], KDIM)
bct = row_basis([[H[i][j] ^ I[i][j] for j in range(KDIM)] for i in range(KDIM)], KDIM)
reps = [[int(x) & 1 for x in row] for row in receiver["finite_receiver_H1_quotient_representatives_f2_28"]]
if len(reps) != H1DIM or any(len(row) != 2 * KDIM for row in reps):
    raise SystemExit("finite H1 retained representative shape moved")

joint_coboundaries = [row + [0] * KDIM for row in bcc] + [[0] * KDIM + row for row in bct]

records = []
for idx1 in SMALLEST:
    rec = source_records[idx1 - 1]
    k_space = eval_space(K_hom_basis, idx1 - 1, KDIM)
    h1_space = eval_space(H1_hom_basis, idx1 - 1, H1DIM)
    h1_cocycles = [combine(v, reps) for v in h1_space]
    cc_images = [row[:KDIM] for row in h1_cocycles]
    ct_images = [row[KDIM:] for row in h1_cocycles]
    cc_rank = quotient_image_rank(cc_images, bcc, KDIM)
    ct_rank = quotient_image_rank(ct_images, bct, KDIM)
    joint_rank = quotient_image_rank(h1_cocycles, joint_coboundaries, 2 * KDIM)
    if joint_rank > len(h1_space):
        raise SystemExit(f"restriction rank escaped evaluation space at A2_{idx1:02d}")
    records.append({
        "source_direction_1based": idx1,
        "source_basis_name": rec["source_basis_name"],
        "selected_crossing_count": rec.get("selected_crossing_count"),
        "nontrivial_component_function_count": rec.get("nontrivial_component_function_count"),
        "K_factor_allowed_value_subspace_dimension_f2": len(k_space),
        "finite_H1_factor_allowed_value_subspace_dimension_f2": len(h1_space),
        "finite_H1_allowed_values_cc_restriction_rank_f2": cc_rank,
        "finite_H1_allowed_values_ct_restriction_rank_f2": ct_rank,
        "finite_H1_allowed_values_joint_restriction_rank_f2": joint_rank,
        "finite_H1_allowed_values_joint_restriction_kernel_dimension_f2": len(h1_space) - joint_rank,
        "finite_H1_allowed_value_basis_rows_f2_16": h1_space,
        "K_allowed_value_basis_rows_f2_14": k_space,
    })

# Also quantify the whole symmetric 24/25/26 block as one restriction problem.
def restricted_block_space(hom_basis, indices1, tdim):
    rows = []
    for flat in hom_basis:
        row = []
        for idx1 in indices1:
            row.extend(int(flat[(idx1 - 1) * tdim + j]) & 1 for j in range(tdim))
        rows.append(row)
    return row_basis(rows, len(indices1) * tdim)

block = [24, 25, 26]
block_k = restricted_block_space(K_hom_basis, block, KDIM)
block_h1 = restricted_block_space(H1_hom_basis, block, H1DIM)

a26_record = next(r for r in records if r["source_direction_1based"] == 26)
cert = {
    "schema": "STAGE33_11_SMALLEST_BLOCK_TARGET_IMAGE_PROFILE_V1",
    "stage": "33-11",
    "branch": "33-11c_SMALLEST_BLOCK_TARGET_IMAGE_REDUCTION",
    "source_locks": {
        "stage33_11b_profile_sha256": ns["cert"]["canonical_sha256"],
        "proper_brauer2_from_discriminant_sha256": EXPECTED_BR2,
        "order2_localization_receiver_sha256": EXPECTED_RECEIVER,
        "first_residue_liftability_certificate_sha256": base_ns["cert"]["canonical_sha256"],
    },
    "a2_26_rectangle": {
        "raw_order2_liftable": True,
        "selected_edges": ["X_0125", "X_0126", "X_0131", "X_0132"],
        "component_incidence": expected_a26_components,
        "component_count": 4,
        "edge_count": 4,
        "shape": "K2,2 four-cycle",
    },
    "smallest_direction_records": records,
    "symmetric_block_24_25_26": {
        "source_dimension_f2": 3,
        "Hom_A_to_K_restriction_parameter_dimension_f2": len(block_k),
        "Hom_A_to_finite_H1_restriction_parameter_dimension_f2": len(block_h1),
    },
    "a2_26_exact_target": {
        "K_factor_allowed_dimension_f2": a26_record["K_factor_allowed_value_subspace_dimension_f2"],
        "finite_H1_factor_allowed_dimension_f2": a26_record["finite_H1_factor_allowed_value_subspace_dimension_f2"],
        "finite_H1_joint_restriction_kernel_dimension_f2": a26_record["finite_H1_allowed_values_joint_restriction_kernel_dimension_f2"],
    },
    "exact_consequence": {
        "connecting_columns_materialized": 0,
        "a2_26_connecting_column_materialized": False,
        "a2_26_explicit_middle_gersten_lift_still_required": True,
        "naturality_envelope_refined_to_exact_value_subspaces": True,
        "remote_cas_used": False,
        "stage33_11_closed_exact": False,
        "next_branch": "33-11c_A2_26_EXPLICIT_RECTANGLE_GERSTEN_LIFT",
    },
}
cert["canonical_sha256"] = csha(cert)
OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "A2_26_K_allowed_dim": cert["a2_26_exact_target"]["K_factor_allowed_dimension_f2"],
    "A2_26_finite_H1_allowed_dim": cert["a2_26_exact_target"]["finite_H1_factor_allowed_dimension_f2"],
    "A2_26_finite_H1_joint_restriction_kernel_dim": cert["a2_26_exact_target"]["finite_H1_joint_restriction_kernel_dimension_f2"],
    "block_24_25_26_K_parameter_dim": len(block_k),
    "block_24_25_26_H1_parameter_dim": len(block_h1),
    "connecting_columns_materialized": "0/26",
    "certificate_sha256": cert["canonical_sha256"],
    "next": cert["exact_consequence"]["next_branch"],
}, indent=2, sort_keys=True))
