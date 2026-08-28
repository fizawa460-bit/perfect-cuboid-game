#!/usr/bin/env python3
"""Materialize an exact five-bit cc/ct decoder for the A2_26 finite-H1 value.

The preceding Stage33-11c profiler proves that the naturality-allowed value
space at A2_26 has dimension five inside H^1(V4,K), and that simultaneous
restriction to <cc> and <ct> is injective on that five-dimensional space.
This script turns that rank statement into a concrete decoder:

* compute the actual cyclic coboundary spaces (g-1)K independently for cc/ct;
* reduce cc and ct values modulo those exact spaces;
* choose five canonical quotient coordinates by left-to-right pivoting;
* record the resulting invertible 5x5 observation matrix and its inverse.

Thus a future explicit Gersten/Galois-difference computation only needs those
five quotient bits to determine the finite-H1 value uniquely.  This script does
not materialize the connecting column and makes no Stage33-11 closure claim.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROFILE_SCRIPT = HERE / "profile_stage33_11_smallest_block_target_images.py"
STAGE07 = HERE.parent / "33-07"
BR2 = STAGE07 / "proper-brauer2-from-discriminant.json"
RECEIVER = STAGE07 / "order2-localization-receiver.json"
OUT = HERE / "stage33-11-a2-26-restriction-decoder.json"

EXPECTED_PROFILE = "45e42d6f3577654df7a4126cad5e2eee651c38fdce3c5cf8289b5f96707f2edc"
EXPECTED_BR2 = "c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf"
EXPECTED_RECEIVER = "9280846c6e7ae8a043e36c7b5498f11476901567b229b94e953b79afab891bda"
KDIM, H1DIM = 14, 16


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


def rref(rows, ncols):
    a = [[int(x) & 1 for x in row] for row in rows if any(int(x) & 1 for x in row)]
    if any(len(row) != ncols for row in a):
        raise SystemExit("GF2 row width regression")
    pivots = []
    r = 0
    for c in range(ncols):
        p = next((i for i in range(r, len(a)) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        for i in range(len(a)):
            if i != r and a[i][c]:
                a[i] = [x ^ y for x, y in zip(a[i], a[r])]
        pivots.append(c)
        r += 1
        if r == len(a):
            break
    return a[:r], pivots


def rank2(rows, ncols):
    return len(rref(rows, ncols)[0])


def reduce_mod(v, rref_basis, pivot_cols):
    out = [int(x) & 1 for x in v]
    for row, p in zip(rref_basis, pivot_cols):
        if out[p]:
            out = [x ^ y for x, y in zip(out, row)]
    if any(out[p] for p in pivot_cols):
        raise SystemExit("quotient reduction failed to clear a pivot")
    return out


def combine(coords, basis):
    out = [0] * len(basis[0])
    for bit, row in zip(coords, basis):
        if int(bit) & 1:
            out = [x ^ (int(y) & 1) for x, y in zip(out, row)]
    return out


def matmul(a, b):
    if not a or not b or len(a[0]) != len(b):
        raise SystemExit("matrix multiplication shape mismatch")
    bt = list(zip(*b))
    return [[sum((x & 1) * (y & 1) for x, y in zip(row, col)) & 1 for col in bt] for row in a]


def invert_square_f2(m):
    n = len(m)
    if n == 0 or any(len(row) != n for row in m):
        raise SystemExit("inverse requires nonempty square matrix")
    aug = [[int(x) & 1 for x in row] + [int(i == j) for j in range(n)] for i, row in enumerate(m)]
    for c in range(n):
        p = next((i for i in range(c, n) if aug[i][c]), None)
        if p is None:
            raise SystemExit("decoder observation matrix is singular")
        aug[c], aug[p] = aug[p], aug[c]
        for i in range(n):
            if i != c and aug[i][c]:
                aug[i] = [x ^ y for x, y in zip(aug[i], aug[c])]
    ident = [[int(i == j) for j in range(n)] for i in range(n)]
    if [row[:n] for row in aug] != ident:
        raise SystemExit("GF2 inversion failed")
    return [row[n:] for row in aug]


# Regenerate and lock the exact Stage33-11c profile in-process.
ns = {"__name__": "__main__", "__file__": str(PROFILE_SCRIPT)}
exec(compile(PROFILE_SCRIPT.read_text(encoding="utf-8"), str(PROFILE_SCRIPT), "exec"), ns)
profile = ns["cert"]
if profile["canonical_sha256"] != EXPECTED_PROFILE:
    raise SystemExit(f"Stage33-11c profile moved: expected {EXPECTED_PROFILE}, got {profile['canonical_sha256']}")
rec26 = next(r for r in profile["smallest_direction_records"] if r["source_basis_name"] == "A2_26")
h1_allowed = [[int(x) & 1 for x in row] for row in rec26["finite_H1_allowed_value_basis_rows_f2_16"]]
if len(h1_allowed) != 5 or any(len(row) != H1DIM for row in h1_allowed):
    raise SystemExit("A2_26 allowed finite-H1 basis is no longer 5x16")
if rec26["finite_H1_allowed_values_joint_restriction_kernel_dimension_f2"] != 0:
    raise SystemExit("A2_26 joint cc/ct restriction is no longer injective")

br2 = load_locked(BR2, EXPECTED_BR2)
receiver = load_locked(RECEIVER, EXPECTED_RECEIVER)
G = [[int(x) & 1 for x in row] for row in br2["proper_Br2_cc_action_f2"]]
H = [[int(x) & 1 for x in row] for row in br2["proper_Br2_ct_action_f2"]]
I = [[int(i == j) for j in range(KDIM)] for i in range(KDIM)]
bcc, pcc = rref([[G[i][j] ^ I[i][j] for j in range(KDIM)] for i in range(KDIM)], KDIM)
bct, pct = rref([[H[i][j] ^ I[i][j] for j in range(KDIM)] for i in range(KDIM)], KDIM)
# Do not infer these ranks from dim B^1(V4,K): each cyclic image (g-1)K is
# computed independently and source-locked by the action matrices above.
free_cc = [j for j in range(KDIM) if j not in pcc]
free_ct = [j for j in range(KDIM) if j not in pct]
if not free_cc or not free_ct:
    raise SystemExit("degenerate cyclic quotient coordinate system")

reps = [[int(x) & 1 for x in row] for row in receiver["finite_receiver_H1_quotient_representatives_f2_28"]]
if len(reps) != H1DIM or any(len(row) != 2 * KDIM for row in reps):
    raise SystemExit("finite receiver H1 representative shape moved")

quotient_rows = []
full_reduced_records = []
for i, h1row in enumerate(h1_allowed):
    cocycle = combine(h1row, reps)
    cc = reduce_mod(cocycle[:KDIM], bcc, pcc)
    ct = reduce_mod(cocycle[KDIM:], bct, pct)
    qcc = [cc[j] for j in free_cc]
    qct = [ct[j] for j in free_ct]
    qrow = qcc + qct
    quotient_rows.append(qrow)
    full_reduced_records.append({
        "allowed_basis_index_0based": i,
        "finite_H1_coordinates_f2_16": h1row,
        "cc_reduced_mod_coboundary_f2_14": cc,
        "ct_reduced_mod_coboundary_f2_14": ct,
        "joint_canonical_quotient_coordinates_f2": qrow,
    })

joint_width = len(free_cc) + len(free_ct)
if rank2(quotient_rows, joint_width) != 5:
    raise SystemExit("joint canonical restriction lost rank five")

# Left-to-right RREF chooses five deterministic observation coordinates.
_, observation_cols = rref(quotient_rows, joint_width)
if len(observation_cols) != 5:
    raise SystemExit(f"expected five canonical observation pivots, got {observation_cols}")
observation_matrix = [[row[j] for j in observation_cols] for row in quotient_rows]
observation_inverse = invert_square_f2(observation_matrix)
ident5 = [[int(i == j) for j in range(5)] for i in range(5)]
if matmul(observation_matrix, observation_inverse) != ident5 or matmul(observation_inverse, observation_matrix) != ident5:
    raise SystemExit("observation decoder inverse verification failed")

coordinate_descriptors = []
for qcol in observation_cols:
    if qcol < len(free_cc):
        coordinate_descriptors.append({
            "generator": "cc",
            "joint_quotient_column_0based": qcol,
            "K_coordinate_0based": free_cc[qcol],
            "K_coordinate_1based": free_cc[qcol] + 1,
        })
    else:
        j = qcol - len(free_cc)
        coordinate_descriptors.append({
            "generator": "ct",
            "joint_quotient_column_0based": qcol,
            "K_coordinate_0based": free_ct[j],
            "K_coordinate_1based": free_ct[j] + 1,
        })

for mask in range(1 << 5):
    coeff = [(mask >> i) & 1 for i in range(5)]
    joint = combine(coeff, quotient_rows)
    observed = [joint[j] for j in observation_cols]
    decoded = [sum((observed[k] & 1) * (observation_inverse[k][j] & 1) for k in range(5)) & 1 for j in range(5)]
    if decoded != coeff:
        raise SystemExit(f"exhaustive decoder regression at mask={mask}: {decoded} != {coeff}")

cert = {
    "schema": "STAGE33_11_A2_26_CC_CT_RESTRICTION_DECODER_V1",
    "stage": "33-11",
    "branch": "33-11c_A2_26_FIVE_BIT_RESTRICTION_DECODER",
    "source_locks": {
        "stage33_11_smallest_block_target_profile_sha256": EXPECTED_PROFILE,
        "proper_brauer2_from_discriminant_sha256": EXPECTED_BR2,
        "order2_localization_receiver_sha256": EXPECTED_RECEIVER,
    },
    "source_direction": {
        "name": "A2_26",
        "source_index_1based": 26,
        "rectangle_edges": ["X_0125", "X_0126", "X_0131", "X_0132"],
        "allowed_finite_H1_value_dimension_f2": 5,
    },
    "cyclic_quotients": {
        "cc_coboundary_rank_f2": len(bcc),
        "ct_coboundary_rank_f2": len(bct),
        "cc_canonical_free_K_coordinates_0based": free_cc,
        "ct_canonical_free_K_coordinates_0based": free_ct,
        "joint_canonical_quotient_width": joint_width,
    },
    "allowed_basis_restriction_records": full_reduced_records,
    "decoder": {
        "joint_restriction_rank_on_allowed_space_f2": 5,
        "canonical_observation_count": 5,
        "canonical_observation_coordinates": coordinate_descriptors,
        "allowed_basis_to_observation_matrix_f2_5x5": observation_matrix,
        "observation_to_allowed_basis_matrix_f2_5x5": observation_inverse,
        "row_vector_convention": "allowed_coefficients * basis_to_observation = observed_bits; observed_bits * observation_to_allowed_basis = allowed_coefficients",
        "all_32_coefficient_vectors_roundtrip_verified": True,
    },
    "exact_consequence": {
        "five_cc_ct_quotient_bits_determine_A2_26_finite_H1_value_uniquely": True,
        "full_absolute_class_materialization_not_needed_for_this_finite_factor": True,
        "explicit_cc_ct_Gersten_Galois_difference_bits_still_required": True,
        "a2_26_connecting_column_materialized": False,
        "connecting_columns_materialized": 0,
        "stage33_11_closed_exact": False,
        "next_branch": "33-11c_A2_26_EXPLICIT_CC_CT_GERSTEN_DIFFERENCE_BITS",
    },
}
cert["canonical_sha256"] = csha(cert)
OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "A2_26_allowed_finite_H1_dimension": 5,
    "cc_coboundary_rank": len(bcc),
    "ct_coboundary_rank": len(bct),
    "canonical_observation_coordinates": coordinate_descriptors,
    "basis_to_observation_matrix": observation_matrix,
    "observation_to_basis_matrix": observation_inverse,
    "all_32_roundtrips_verified": True,
    "connecting_columns_materialized": "0/26",
    "certificate_sha256": cert["canonical_sha256"],
    "next": cert["exact_consequence"]["next_branch"],
}, indent=2, sort_keys=True))
