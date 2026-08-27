#!/usr/bin/env python3
"""Certify an explicit invariant-factor basis for the retained 2-primary
boundary-residue quotient.

The retained presentation uses row relations on the ordered generators

    R01..R17,O01..O12.

For a Smith decomposition D = S*M*T, row coordinates therefore transform as
x |-> x*T.  Conversely, the j-th Smith generator is the j-th row of T^{-1}
in the original generator basis.  This leaf records and verifies both maps.

This is only an exact change of basis for the boundary-residue presentation.
It does not compute the arithmetic localization connecting map, identify the
absolute Galois H1 with the finite V4 diagnostic, or lift a residue direction
to a Q-defined Brauer class.
"""
import hashlib
import json
from pathlib import Path

import sympy as sp
from sympy import ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "br0g-finite-ramified-residue-presentation.json"
OUTPUT = HERE / "two-primary-residue-invariant-basis.json"
EXPECTED_SOURCE_SHA256 = (
    "4ff7731ec06df0fbd676c7c310e29c50ef1898690530d7f7497ce832a1e0d71d"
)


def canonical_sha256(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


src = json.loads(SOURCE.read_text(encoding="utf-8"))
claimed = src["canonical_sha256"]
source_body = dict(src)
source_body.pop("canonical_sha256")
actual = canonical_sha256(source_body)
if claimed != EXPECTED_SOURCE_SHA256 or actual != EXPECTED_SOURCE_SHA256:
    raise SystemExit(
        f"retained BR0G source lock moved claimed={claimed} actual={actual}"
    )
if src["schema"] != "STAGE33_07_BR0G_FINITE_RAMIFIED_RESIDUE_PRESENTATION_RETAINED_V2":
    raise SystemExit("retained BR0G source schema regression")
if not src["relation_matrix_exact_for_boundary_finite_ramified_residue_branch"]:
    raise SystemExit("boundary-residue exactness flag regressed")
if src["relation_matrix_exact_for_full_two_primary_BrU_branch"]:
    raise SystemExit("full Br(U) relation firewall regressed")

rows = [[int(v) for v in row] for row in src[
    "diagnostic_quotient_by_U44_relation_matrix_29x29"
]]
if len(rows) != 29 or any(len(row) != 29 for row in rows):
    raise SystemExit("retained quotient presentation shape regression")

domain_matrix = DomainMatrix.from_list_sympy(29, 29, rows).convert_to(ZZ)
D_dm, S_dm, T_dm = smith_normal_decomp(domain_matrix)
M = sp.Matrix(rows)
D = D_dm.to_Matrix()
S = S_dm.to_Matrix()
T = T_dm.to_Matrix()
I = sp.eye(29)
if S * M * T != D:
    raise SystemExit("Smith decomposition equality failed")
if abs(int(S.det())) != 1 or abs(int(T.det())) != 1:
    raise SystemExit("Smith transformations are not unimodular")

T_inv = T.inv()
S_inv = S.inv()
if any(v.q != 1 for v in T_inv) or any(v.q != 1 for v in S_inv):
    raise SystemExit("unimodular inverse unexpectedly nonintegral")
if T * T_inv != I or T_inv * T != I:
    raise SystemExit("right coordinate maps are not mutual inverses")
if S_inv * D * T_inv != M:
    raise SystemExit("inverse Smith reconstruction failed")

diag = [abs(int(D[i, i])) for i in range(29)]
expected_diag = [1] * 3 + [2] * 23 + [4] * 3
if diag != expected_diag:
    raise SystemExit(f"Smith diagonal regression {diag}")
if diag != src["diagnostic_quotient_smith_nonzero_diagonal"]:
    raise SystemExit("stored Smith diagonal no longer matches")

# Row-relation convention checks.  Original coordinates x map to x*T, so the
# rows of M map to M*T = S^{-1}*D and generate exactly the diagonal row lattice.
if M * T != S_inv * D:
    raise SystemExit("row-relation coordinate convention failed")

generator_names = [f"R{i:02d}" for i in range(1, 18)] + [
    f"O{i:02d}" for i in range(1, 13)
]


def matrix_rows(A):
    return [[int(A[i, j]) for j in range(A.cols)] for i in range(A.rows)]


def sparse_expression(row):
    return [
        {"generator": generator_names[j], "coefficient": int(row[j])}
        for j in range(29)
        if row[j]
    ]


invariant_generators = []
order_counts = {"2": 0, "4": 0}
for j, order in enumerate(diag):
    if order == 1:
        continue
    order_counts[str(order)] += 1
    label = f"I{order:02d}_{order_counts[str(order)]:02d}"
    original_row = [int(T_inv[j, k]) for k in range(29)]
    smith_image = sp.Matrix(1, 29, original_row) * T
    if smith_image != sp.eye(29).row(j):
        raise SystemExit(f"inverse generator image failed at Smith index {j}")
    invariant_generators.append({
        "name": label,
        "order": order,
        "smith_coordinate_index_1based": j + 1,
        "original_R17_O12_coordinates": original_row,
        "original_sparse_expression": sparse_expression(original_row),
    })

if len(invariant_generators) != 26 or order_counts != {"2": 23, "4": 3}:
    raise SystemExit("minimal invariant-factor generator count regression")

cert = {
    "schema": "STAGE33_07_TWO_PRIMARY_RESIDUE_INVARIANT_BASIS_V1",
    "source_locks": {
        "br0g_finite_ramified_residue_presentation_sha256": claimed,
        "full_certificate_original_canonical_sha256": src[
            "full_certificate_original_canonical_sha256"
        ],
    },
    "presentation_scope": "DIAGNOSTIC_BOUNDARY_RESIDUE_QUOTIENT_BY_U44",
    "original_generator_order": "R01..R17,O01..O12",
    "relation_convention": "ROWS_OF_M_GENERATE_THE_RELATION_LATTICE_IN_Z29",
    "smith_identity": "D=S*M*T",
    "original_to_smith_row_coordinate_map": "x_maps_to_x*T",
    "smith_to_original_row_coordinate_map": "y_maps_to_y*T_inverse",
    "smith_diagonal": diag,
    "smith_left_unimodular_S": matrix_rows(S),
    "smith_right_unimodular_T": matrix_rows(T),
    "smith_right_inverse_T_inverse": matrix_rows(T_inv),
    "unimodular_determinants": {"S": int(S.det()), "T": int(T.det())},
    "exact_checks": {
        "D_equals_S_M_T": True,
        "M_equals_S_inverse_D_T_inverse": True,
        "M_T_equals_S_inverse_D": True,
        "T_T_inverse_equals_identity": True,
        "all_transform_entries_integral": True,
        "source_and_stored_smith_diagonal_match": True,
    },
    "trivial_smith_generator_count": 3,
    "minimal_invariant_factor_generator_count": 26,
    "invariant_factor_counts": {"order2": 23, "order4": 3},
    "diagnostic_quotient_exact": "(Z/2)^23 direct_sum (Z/4)^3",
    "invariant_factor_generators": invariant_generators,
    "arithmetic_localization_connecting_map_computed": False,
    "absolute_H1_identified_with_finite_V4_H1": False,
    "boundary_residual_promoted_to_global_q_classes": False,
    "full_two_primary_BrU_relation_matrix_claimed": False,
    "actual_index512_k3_glue_identified": False,
    "arithmetic_HS_closed": False,
    "next_exact_leaf": (
        "L33-07-COMPUTE-ORDER2-LOCALIZATION-EXTENSION-CLASS-IN-EXPLICIT-"
        "RESIDUE-INVARIANT-BASIS"
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
    "certificate_sha256": cert["canonical_sha256"],
    "smith_diagonal_counts": {"1": 3, "2": 23, "4": 3},
    "minimal_invariant_factor_generator_count": 26,
    "coordinate_maps_mutually_inverse": True,
    "arithmetic_HS_closed": False,
    "stage33_progress": "6/11",
}, indent=2, sort_keys=True))
