#!/usr/bin/env python3
"""Materialize the exact finite source/receiver coordinates for delta_loc.

This is a preparatory exact leaf only.  It does not compute the localization
extension class and does not identify the finite V4 H1 diagnostic with the
absolute Galois H1.

Source side:
  the order-two subgroup of the retained boundary-residue diagnostic quotient
      (Z/2)^23 direct_sum (Z/4)^3,
  written in the explicit Smith basis already certified in
  two-primary-residue-invariant-basis.json.

Receiver side:
  an explicit deterministic basis for
      H^1(V4, Br(Sbar)[2])
  for the exact proper Br2 V4 module certified in
  proper-brauer2-from-discriminant.json.

The resulting certificate is the finite coordinate frame in which the next
leaf must compute the actual order-two localization extension-class matrix.
"""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
IB_PATH = HERE / "two-primary-residue-invariant-basis.json"
BR2_PATH = HERE / "proper-brauer2-from-discriminant.json"
OUTPUT = HERE / "order2-localization-receiver.json"

EXPECTED_IB_SHA256 = "f18a54717b2327f7abc8ee87859b5c0537bffc062a1d5c1e36a5763c46faa939"
EXPECTED_BR2_SHA256 = "c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf"


def canonical_sha256(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_locked(path, expected, schema):
    obj = json.loads(path.read_text(encoding="utf-8"))
    claimed = obj["canonical_sha256"]
    body = dict(obj)
    body.pop("canonical_sha256")
    actual = canonical_sha256(body)
    if claimed != expected or actual != expected:
        raise SystemExit(
            f"source lock moved for {path.name}: claimed={claimed} actual={actual}"
        )
    if obj["schema"] != schema:
        raise SystemExit(f"schema regression for {path.name}: {obj['schema']}")
    return obj


def xor(a, b):
    return [x ^ y for x, y in zip(a, b)]


def dot2(a, b):
    return sum(x & y for x, y in zip(a, b)) & 1


def row_basis(rows, ncols):
    """Deterministic reduced row basis over F2, pivots increasing."""
    a = [[int(x) & 1 for x in row] for row in rows if any(int(x) & 1 for x in row)]
    if any(len(row) != ncols for row in a):
        raise SystemExit("GF2 row width regression")
    r = 0
    pivots = []
    for c in range(ncols):
        p = next((i for i in range(r, len(a)) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        for i in range(len(a)):
            if i != r and a[i][c]:
                a[i] = xor(a[i], a[r])
        pivots.append(c)
        r += 1
        if r == len(a):
            break
    return a[:r], pivots


def rank2(rows, ncols):
    return len(row_basis(rows, ncols)[0])


def nullspace_basis(equations, ncols):
    """Deterministic basis of the right nullspace of row equations over F2."""
    rref, pivots = row_basis(equations, ncols)
    free = [j for j in range(ncols) if j not in set(pivots)]
    out = []
    for f in free:
        v = [0] * ncols
        v[f] = 1
        # In RREF each pivot equation is x_p + sum_f a_pf x_f = 0.
        for row, p in zip(rref, pivots):
            if row[f]:
                v[p] = 1
        if any(dot2(eq, v) for eq in equations):
            raise SystemExit("nullspace reconstruction failed")
        out.append(v)
    if len(out) != ncols - len(pivots):
        raise SystemExit("nullspace dimension regression")
    return out


def matmul(A, B):
    if not A or not B:
        return []
    m, k, n = len(A), len(B), len(B[0])
    if any(len(r) != k for r in A) or any(len(r) != n for r in B):
        raise SystemExit("matrix shape regression")
    return [
        [sum(A[i][t] * B[t][j] for t in range(k)) for j in range(n)]
        for i in range(m)
    ]


ib = load_locked(
    IB_PATH,
    EXPECTED_IB_SHA256,
    "STAGE33_07_TWO_PRIMARY_RESIDUE_INVARIANT_BASIS_V1",
)
br2 = load_locked(
    BR2_PATH,
    EXPECTED_BR2_SHA256,
    "STAGE33_07_PROPER_BRAUER2_FROM_DISCRIMINANT_V1",
)

if ib["diagnostic_quotient_exact"] != "(Z/2)^23 direct_sum (Z/4)^3":
    raise SystemExit("two-primary diagnostic quotient regression")
if ib["invariant_factor_counts"] != {"order2": 23, "order4": 3}:
    raise SystemExit("two-primary invariant-factor count regression")
if ib["arithmetic_localization_connecting_map_computed"]:
    raise SystemExit("unexpected localization promotion in source certificate")

# ---------------------------------------------------------------------------
# Source: A[2] for A=(Z/2)^23 direct_sum (Z/4)^3.
# A Smith generator of order 2 is used once; an order-4 generator is doubled.
# ---------------------------------------------------------------------------
T = [[int(x) for x in row] for row in ib["smith_right_unimodular_T"]]
diag = [int(x) for x in ib["smith_diagonal"]]
if len(T) != 29 or any(len(row) != 29 for row in T):
    raise SystemExit("stored Smith T shape regression")
if diag != [1] * 3 + [2] * 23 + [4] * 3:
    raise SystemExit("stored Smith diagonal regression")

source_basis = []
for g in ib["invariant_factor_generators"]:
    order = int(g["order"])
    if order not in (2, 4):
        raise SystemExit("unexpected invariant factor order")
    j = int(g["smith_coordinate_index_1based"]) - 1
    multiplier = 1 if order == 2 else 2
    original = [multiplier * int(x) for x in g["original_R17_O12_coordinates"]]
    smith = matmul([original], T)[0]
    expected_smith = [0] * 29
    expected_smith[j] = multiplier
    if smith != expected_smith:
        raise SystemExit(f"Smith source-basis image failed for {g['name']}")
    # Exact order-two check in Smith coordinates: 2*y is divisible by D.
    twice = [2 * x for x in smith]
    if any(twice[k] % diag[k] for k in range(29)):
        raise SystemExit(f"order-two source check failed for {g['name']}")
    source_basis.append({
        "name": f"A2_{len(source_basis)+1:02d}",
        "from_invariant_factor": g["name"],
        "parent_order": order,
        "parent_multiplier": multiplier,
        "smith_coordinates_Z29": smith,
        "original_R17_O12_coordinates_Z29": original,
    })

if len(source_basis) != 26:
    raise SystemExit("order-two source basis dimension regression")
# Distinct nontrivial Smith factors give an exact independent F2 basis of A[2].
source_supports = [
    next(i for i, x in enumerate(v["smith_coordinates_Z29"]) if x)
    for v in source_basis
]
if len(set(source_supports)) != 26:
    raise SystemExit("order-two source Smith supports are not independent")

# ---------------------------------------------------------------------------
# Receiver: explicit Z1, B1 and H1 bases for V4 acting on proper Br2.
# Preserve the exact row-action convention used by the source certificate:
# cocycle pair (a,b): a*(g-I)=0, b*(h-I)=0, a*(h-I)=b*(g-I).
# ---------------------------------------------------------------------------
N = int(br2["proper_geometric_Br2_dimension_f2"])
if N != 14:
    raise SystemExit("proper Br2 dimension regression")
G = [[int(x) & 1 for x in row] for row in br2["proper_Br2_cc_action_f2"]]
H = [[int(x) & 1 for x in row] for row in br2["proper_Br2_ct_action_f2"]]
if len(G) != N or len(H) != N or any(len(r) != N for r in G + H):
    raise SystemExit("proper Br2 action shape regression")
I = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
Ng = [[G[i][j] ^ I[i][j] for j in range(N)] for i in range(N)]
Nh = [[H[i][j] ^ I[i][j] for j in range(N)] for i in range(N)]

eq = []
for j in range(N):
    eq.append([Ng[i][j] for i in range(N)] + [0] * N)
for j in range(N):
    eq.append([0] * N + [Nh[i][j] for i in range(N)])
for j in range(N):
    eq.append([Nh[i][j] for i in range(N)] + [Ng[i][j] for i in range(N)])

z1_basis = nullspace_basis(eq, 2 * N)
b1_generators = [Ng[i] + Nh[i] for i in range(N)]
b1_basis, _ = row_basis(b1_generators, 2 * N)
if len(z1_basis) != 20 or len(b1_basis) != 4:
    raise SystemExit(
        f"finite V4 Z1/B1 regression Z1={len(z1_basis)} B1={len(b1_basis)}"
    )
if any(any(dot2(eqrow, b) for eqrow in eq) for b in b1_basis):
    raise SystemExit("coboundary basis is not contained in cocycles")

# Deterministic quotient representatives: extend the reduced B1 basis using
# the deterministic nullspace basis in free-coordinate order.
span = list(b1_basis)
span_rank = rank2(span, 2 * N)
h1_basis = []
for z in z1_basis:
    r = rank2(span + [z], 2 * N)
    if r > span_rank:
        h1_basis.append(z)
        span.append(z)
        span_rank = r
if len(h1_basis) != 16 or span_rank != 20:
    raise SystemExit("finite V4 H1 quotient-basis regression")

claimed_h1 = br2["finite_v4_H1_proper_Br2"]
if claimed_h1["cocycle_dimension_f2"] != 20:
    raise SystemExit("proper Br2 stored cocycle dimension regression")
if claimed_h1["coboundary_dimension_f2"] != 4:
    raise SystemExit("proper Br2 stored coboundary dimension regression")
if claimed_h1["H1_dimension_f2"] != 16:
    raise SystemExit("proper Br2 stored H1 dimension regression")
if claimed_h1["absolute_H1_identified_with_finite_H1"]:
    raise SystemExit("absolute H1 firewall regressed")

cert = {
    "schema": "STAGE33_07_ORDER2_LOCALIZATION_RECEIVER_V1",
    "source_locks": {
        "two_primary_residue_invariant_basis_sha256": EXPECTED_IB_SHA256,
        "proper_brauer2_from_discriminant_sha256": EXPECTED_BR2_SHA256,
    },
    "finite_source_role": "ORDER2_SUBGROUP_OF_DIAGNOSTIC_BOUNDARY_RESIDUE_QUOTIENT",
    "finite_source_parent_group": "(Z/2)^23 direct_sum (Z/4)^3",
    "finite_source_order2_dimension_f2": 26,
    "finite_source_basis": source_basis,
    "finite_receiver_role": "FINITE_V4_LOCALIZATION_OBSTRUCTION_TARGET_DIAGNOSTIC",
    "finite_receiver_module": "proper geometric Br(Sbar)[2]",
    "finite_receiver_module_dimension_f2": 14,
    "finite_receiver_cocycle_pair_coordinate_order": "cc_value_14_then_ct_value_14",
    "finite_receiver_Z1_dimension_f2": 20,
    "finite_receiver_B1_dimension_f2": 4,
    "finite_receiver_H1_dimension_f2": 16,
    "finite_receiver_Z1_basis_f2_28": z1_basis,
    "finite_receiver_B1_basis_f2_28": b1_basis,
    "finite_receiver_H1_quotient_representatives_f2_28": h1_basis,
    "exact_checks": {
        "source_order2_basis_has_26_independent_smith_supports": True,
        "source_basis_elements_have_exact_order_dividing_2": True,
        "receiver_Z1_dimension_is_20": True,
        "receiver_B1_dimension_is_4": True,
        "receiver_H1_dimension_is_16": True,
        "receiver_B1_contained_in_Z1": True,
        "receiver_H1_representatives_extend_B1_to_Z1": True,
    },
    "localization_extension_class_computed": False,
    "localization_connecting_map_delta_loc_evaluated": False,
    "absolute_H1_identified_with_finite_V4_H1": False,
    "boundary_residual_promoted_to_global_q_classes": False,
    "constant_cokernel_HS_d2_computed": False,
    "actual_index512_k3_glue_identified": False,
    "arithmetic_HS_closed": False,
    "next_exact_leaf": (
        "L33-07-COMPUTE-ORDER2-LOCALIZATION-EXTENSION-CLASS-MATRIX-"
        "FROM-BOUNDARY-KUMMER-COMPLEX-IN-26x16-COORDINATES"
    ),
    "unit_status": "RUNNING_REPAIR",
    "stage33_progress": "6/11",
    "stage33_08_released": False,
    "theorem_credit": False,
    "endpoint_credit": False,
    "perfect_cuboid_nonexistence_claim": False,
}
cert["canonical_sha256"] = canonical_sha256(cert)
OUTPUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "finite_source_order2_dimension_f2": 26,
    "finite_receiver_Z1_dimension_f2": 20,
    "finite_receiver_B1_dimension_f2": 4,
    "finite_receiver_H1_dimension_f2": 16,
    "localization_extension_class_computed": False,
    "certificate_sha256": cert["canonical_sha256"],
    "stage33_progress": "6/11",
}, indent=2, sort_keys=True))
