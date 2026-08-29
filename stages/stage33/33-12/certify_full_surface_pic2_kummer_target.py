#!/usr/bin/env python3
"""Linearize the full-surface finite-V4 Kummer-defect target.

The actual Kummer extension class is not present in the retained interface.
This verifier nevertheless computes, from the exact integral Picard actions,
the complete finite-V4 target in which its restriction must live.  It also
materializes an explicit basis of the ten invariant proper Br[2] directions.

This is only the V4 restriction.  It is not identified with absolute G_Q
cohomology and it does not compute any Hochschild--Serre d2 value.
"""

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
STAGE33 = HERE.parent
PIC = STAGE33 / "33-07" / "retained-picard-base-sparse.json"
BR2 = STAGE33 / "33-07" / "proper-brauer2-from-discriminant.json"
ADJUST = HERE / "full-surface-hs-adjustment-contract.json"
OUT = HERE / "full-surface-pic2-kummer-target.json"

EXPECTED_PIC = "e41df3f84760b941440035a388baac88602126c80140139ddf9c187bedf0bb49"
EXPECTED_BR2 = "c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf"
EXPECTED_ADJUST = "f1b34a61119da7bbf2ee47ccf457a962e1e127ab5464082426f1948ce7321c43"


def csha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_locked(path, expected):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256", None)
    if claimed != expected or csha(body) != expected:
        raise SystemExit(f"canonical source lock moved: {path}")
    return obj


def expand_sparse(obj, n):
    rows = obj["matrix_64x64_sparse_rows_1based"]
    if len(rows) != n:
        raise SystemExit("sparse matrix row count regression")
    out = []
    for row in rows:
        dense = [0] * n
        for j, value in row:
            if not 1 <= int(j) <= n or dense[int(j) - 1] != 0:
                raise SystemExit("invalid sparse row")
            dense[int(j) - 1] = int(value)
        out.append(dense)
    return out


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def matmul(a, b):
    bt = list(zip(*b))
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def transpose(a):
    return [list(row) for row in zip(*a)]


def xor(a, b):
    return [int(x) ^ int(y) for x, y in zip(a, b)]


def rref(rows, ncols):
    a = [[int(x) & 1 for x in row] for row in rows if any(int(x) & 1 for x in row)]
    if any(len(row) != ncols for row in a):
        raise SystemExit("GF2 row width regression")
    pivots = []
    r = 0
    for c in range(ncols):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        for i in range(len(a)):
            if i != r and a[i][c]:
                a[i] = xor(a[i], a[r])
        pivots.append(c)
        r += 1
        if r == len(a):
            break
    return a[:r], pivots


def rank(rows, ncols):
    return len(rref(rows, ncols)[0])


def nullspace(rows, ncols):
    reduced, pivots = rref(rows, ncols)
    free = [c for c in range(ncols) if c not in pivots]
    basis = []
    for f in free:
        v = [0] * ncols
        v[f] = 1
        for i, p in enumerate(pivots):
            v[p] = reduced[i][f]
        basis.append(v)
    return basis


pic = load_locked(PIC, EXPECTED_PIC)
br2 = load_locked(BR2, EXPECTED_BR2)
adjust = load_locked(ADJUST, EXPECTED_ADJUST)

n = 64
cc_z = expand_sparse(pic["objects"]["cc"], n)
ct_z = expand_sparse(pic["objects"]["ct"], n)
gram = expand_sparse(pic["objects"]["gram"], n)
i64 = identity(n)
if matmul(cc_z, cc_z) != i64 or matmul(ct_z, ct_z) != i64:
    raise SystemExit("integral Picard involution regression")
if matmul(cc_z, ct_z) != matmul(ct_z, cc_z):
    raise SystemExit("integral Picard V4 commutation regression")
if matmul(matmul(cc_z, gram), transpose(cc_z)) != gram:
    raise SystemExit("cc Picard Gram isometry regression")
if matmul(matmul(ct_z, gram), transpose(ct_z)) != gram:
    raise SystemExit("ct Picard Gram isometry regression")

cc = [[x & 1 for x in row] for row in cc_z]
ct = [[x & 1 for x in row] for row in ct_z]
i2 = identity(n)
nc = [xor(row, eye) for row, eye in zip(cc, i2)]
nt = [xor(row, eye) for row, eye in zip(ct, i2)]

# Row-vector cocycle pair (a,b): a(1+cc)=0, b(1+ct)=0,
# a(ct-1)=b(cc-1).  In characteristic two, +/- coincide.
equations = []
for col in transpose(nc):
    equations.append(col + [0] * n)
for col in transpose(nt):
    equations.append([0] * n + col)
for c_nt, c_nc in zip(transpose(nt), transpose(nc)):
    equations.append(c_nt + c_nc)
cocycle_dimension = 2 * n - rank(equations, 2 * n)
coboundaries = [nc[i] + nt[i] for i in range(n)]
coboundary_basis = rref(coboundaries, 2 * n)[0]
coboundary_dimension = len(coboundary_basis)
h1_dimension = cocycle_dimension - coboundary_dimension
cocycle_basis = nullspace(equations, 2 * n)
if len(cocycle_basis) != cocycle_dimension:
    raise SystemExit("cocycle nullspace dimension regression")
if rank(coboundary_basis + cocycle_basis, 2 * n) != cocycle_dimension:
    raise SystemExit("coboundaries escaped the cocycle space")
span = list(coboundary_basis)
h1_representatives = []
current_rank = len(span)
for vector in cocycle_basis:
    new_rank = rank(span + [vector], 2 * n)
    if new_rank > current_rank:
        h1_representatives.append(vector)
        span.append(vector)
        current_rank = new_rank
if current_rank != cocycle_dimension or len(h1_representatives) != h1_dimension:
    raise SystemExit("failed to construct an explicit H1 quotient basis")

pic2_fixed_dimension = n - rank(transpose(nc) + transpose(nt), n)

kcc = br2["proper_Br2_cc_action_f2"]
kct = br2["proper_Br2_ct_action_f2"]
kdim = 14
ki = identity(kdim)
knc = [xor(row, eye) for row, eye in zip(kcc, ki)]
knt = [xor(row, eye) for row, eye in zip(kct, ki)]
proper_invariant_basis = nullspace(transpose(knc) + transpose(knt), kdim)
if len(proper_invariant_basis) != 10:
    raise SystemExit("proper invariant basis dimension regression")

if adjust["full_surface_proper_adjustment_module"]["dimension_f2"] != 10:
    raise SystemExit("HS adjustment contract regression")

certificate = {
    "schema": "STAGE33_12_FULL_SURFACE_PIC2_KUMMER_TARGET_V1",
    "source_locks": {
        "retained_picard_base_sparse_sha256": EXPECTED_PIC,
        "proper_brauer2_from_discriminant_sha256": EXPECTED_BR2,
        "full_surface_hs_adjustment_contract_sha256": EXPECTED_ADJUST,
    },
    "integral_picard_interface": {
        "rank": 64,
        "cc_ct_integral_involutions_commuting": True,
        "cc_ct_preserve_picard_gram": True,
        "pic_mod2_joint_fixed_dimension_f2": pic2_fixed_dimension,
    },
    "finite_v4_pic2_cohomology": {
        "group": "V4=<cc,ct>",
        "module": "Pic(Sbar)/2",
        "normalized_cocycle_pair_ambient_dimension_f2": 128,
        "cocycle_dimension_f2": cocycle_dimension,
        "coboundary_dimension_f2": coboundary_dimension,
        "H1_dimension_f2": h1_dimension,
        "H1_quotient_basis_cc_ct_pairs_original_pic2_coordinates_f2": [
            {"cc": vector[:n], "ct": vector[n:]} for vector in h1_representatives
        ],
        "H1_quotient_basis_sha256": csha(h1_representatives),
        "absolute_H1_identified_with_finite_V4_H1": False,
    },
    "proper_invariant_domain": {
        "module": "P=Br(Sbar)[2]^{V4}=Br(Sbar)[2]^{G_Q}",
        "dimension_f2": 10,
        "basis_rows_original_proper_br2_coordinates_f2": proper_invariant_basis,
        "basis_sha256": csha(proper_invariant_basis),
    },
    "kummer_defect_map_contract": {
        "finite_restriction": "delta_Kum,V4: P -> H^1(V4,Pic(Sbar)/2)",
        "source_dimension_f2": 10,
        "target_dimension_f2": h1_dimension,
        "matrix_shape_target_by_source": [h1_dimension, 10],
        "matrix_entries_materialized": 0,
        "columns_materialized": 0,
        "known_full_surface_J2_kernel_dimension_lower_bound": 1,
        "therefore_rank_upper_bound": 9,
        "finite_V4_d2_is_integral_bockstein_after_delta_Kum": True,
    },
    "exact_information_boundary": {
        "picard_action_missing": False,
        "proper_invariant_basis_missing": False,
        "kummer_extension_class_missing": True,
        "integral_bockstein_target_quotient_materialized": False,
        "finite_V4_zero_would_imply_absolute_zero": False,
        "finite_V4_nonzero_would_certify_absolute_nonzero_by_restriction": True,
    },
    "next_exact_leaf": "MATERIALIZE_ONE_COLUMN_OF_DELTA_KUM_V4_FROM_A_FULL_SURFACE_MU2_LIFT_OR_EQUIVALENT_UNIMODULAR_GLUE_DATUM",
    "promotion_firewall": {
        "proper_d2_map_computed": False,
        "finite_obstruction_cosets_materialized": 0,
        "arithmetic_hs_d2_computed": False,
        "global_q_residue_lifts_complete": False,
        "stage33_12_closed": False,
        "stage33_progress": "6/11",
    },
}
certificate["canonical_sha256"] = csha(certificate)
OUT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "pic2_fixed_dimension_f2": pic2_fixed_dimension,
    "pic2_H1_V4_dimension_f2": h1_dimension,
    "proper_invariant_dimension_f2": len(proper_invariant_basis),
    "kummer_defect_columns_materialized": 0,
    "certificate_sha256": certificate["canonical_sha256"],
}, indent=2, sort_keys=True))
