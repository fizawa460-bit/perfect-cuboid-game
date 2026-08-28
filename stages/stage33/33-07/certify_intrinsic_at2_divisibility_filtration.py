#!/usr/bin/env python3
"""Certify the canonical 4A[8] subset 2A[4] subset A[2] filtration intrinsically.

For an order-two discriminant class y/2 in A_L[2]=ker(G mod 2):
- y/2 lies in 2A_L[4] iff y has a mod-4 lift z with Gz=0 mod 4;
- y/2 lies in 4A_L[8] iff y has a mod-8 lift z with Gz=0 mod 8.

This gives a basis-independent marking of the mixed (2,4,8) discriminant group.
The retained Smith model has dimensions 10 and 4 respectively.  We derive the
same subspaces from the integral Picard Gram without Smith form or remote CAS.
"""
from __future__ import annotations

import hashlib
import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
INTRINSIC_SCRIPT = HERE / "certify_actual_coordinate_swap_at2_actions.py"
GALOIS_SCRIPT = HERE / "certify_actual_galois_at2_actions.py"
OUT = HERE / "intrinsic-at2-divisibility-filtration.json"


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def bitrow(row: list[int]) -> int:
    return sum((int(x) & 1) << j for j, x in enumerate(row))


def row_from_mask(mask: int, n: int) -> list[int]:
    return [(int(mask) >> j) & 1 for j in range(n)]


def xor_basis(rows: list[int]) -> dict[int, int]:
    piv: dict[int, int] = {}
    for raw in rows:
        x = int(raw)
        while x:
            p = x.bit_length() - 1
            if p in piv:
                x ^= piv[p]
            else:
                for q in list(piv):
                    if (piv[q] >> p) & 1:
                        piv[q] ^= x
                piv[p] = x
                break
    return piv


def reduce_by(piv: dict[int, int], raw: int) -> int:
    x = int(raw)
    for p in sorted(piv, reverse=True):
        if (x >> p) & 1:
            x ^= piv[p]
    return x


def tagged_span_solver(rows: list[int]):
    piv: dict[int, tuple[int, int]] = {}
    for i, raw in enumerate(rows):
        x, tag = int(raw), 1 << i
        while x:
            p = x.bit_length() - 1
            if p in piv:
                y, t = piv[p]
                x ^= y
                tag ^= t
            else:
                piv[p] = (x, tag)
                break

    def solve(raw: int) -> int | None:
        x, tag = int(raw), 0
        while x:
            p = x.bit_length() - 1
            if p not in piv:
                return None
            y, t = piv[p]
            x ^= y
            tag ^= t
        return tag

    return solve


def greedy_basis(rows: list[int]) -> list[int]:
    piv: dict[int, int] = {}
    out: list[int] = []
    for raw in rows:
        x = int(raw)
        while x:
            p = x.bit_length() - 1
            if p in piv:
                x ^= piv[p]
            else:
                piv[p] = x
                out.append(int(raw))
                break
    return out


def row_action_mask(mask: int, matrix: list[list[int]]) -> int:
    out = 0
    for j in range(len(matrix[0])):
        bit = 0
        for i in range(len(matrix)):
            if ((mask >> i) & 1) and (int(matrix[i][j]) & 1):
                bit ^= 1
        out |= bit << j
    return out


intr = runpy.run_path(str(INTRINSIC_SCRIPT))
gal = runpy.run_path(str(GALOIS_SCRIPT))
gram = [[int(x) for x in row] for row in intr["gram"]]
kernel_masks = [int(x) for x in intr["kernel_masks"]]
if len(gram) != 64 or len(kernel_masks) != 14:
    raise SystemExit("intrinsic Picard/A[2] shape regression")

G2_rows = [bitrow(row) for row in gram]
image_piv = xor_basis(G2_rows)
solve_image = tagged_span_solver(G2_rows)


def matvec(mask: int) -> list[int]:
    return [sum(gram[i][j] for j in range(64) if (mask >> j) & 1) for i in range(64)]


def vals_to_mask(vals: list[int]) -> int:
    return sum((int(v) & 1) << i for i, v in enumerate(vals))

# Quotient classes of Gk/2 mod 2 for k in ker(G mod 2).  Their span is exactly
# the ambiguity in the second Hensel step when changing a mod-4 lift.
h_classes: list[int] = []
for k in kernel_masks:
    gk = matvec(k)
    if any(v % 2 for v in gk):
        raise SystemExit("kernel vector ceased to pair evenly")
    h_classes.append(reduce_by(image_piv, vals_to_mask([v // 2 for v in gk])))
h_piv = xor_basis(h_classes)
if len(h_piv) != 4:
    raise SystemExit(f"second Hensel ambiguity dimension regression: {len(h_piv)}")

D2: list[int] = []
D4: list[int] = []
for coords in range(1 << 14):
    y = 0
    for i, k in enumerate(kernel_masks):
        if (coords >> i) & 1:
            y ^= k
    gy = matvec(y)
    if any(v % 2 for v in gy):
        raise SystemExit("A[2] representative ceased to be dual")

    # First Hensel step: z=y+2u and Gz=0 mod 4.
    rhs = vals_to_mask([(-v // 2) & 1 for v in gy])
    u = solve_image(rhs)
    if u is None:
        continue
    gu = matvec(u)
    if vals_to_mask(gu) != rhs:
        raise SystemExit("mod-4 lift solver regression")
    D2.append(coords)

    # Second Hensel step: changing u by k in ker(G mod2) changes the obstruction
    # by Gk/2 modulo Im(G mod2).  Hence membership in span(h_classes) is the
    # exact existence criterion for a mod-8 lift.
    zpair = [gy[i] + 2 * gu[i] for i in range(64)]
    if any(v % 4 for v in zpair):
        raise SystemExit("chosen mod-4 lift is not divisible by four")
    obstruction = reduce_by(image_piv, vals_to_mask([v // 4 for v in zpair]))
    if reduce_by(h_piv, obstruction) == 0:
        D4.append(coords)

if len(D2) != (1 << 10) or len(D4) != (1 << 4):
    raise SystemExit(f"divisibility filtration size regression: {len(D2)}, {len(D4)}")
D2_basis_masks = greedy_basis(D2)
D4_basis_masks = greedy_basis(D4)
if len(D2_basis_masks) != 10 or len(D4_basis_masks) != 4:
    raise SystemExit("divisibility filtration dimension regression")
D2_set, D4_set = set(D2), set(D4)

# All actual geometric and named Galois actions must preserve this canonical
# filtration.  This also checks the row-coordinate convention used below.
actions = list(intr["all_at2"]) + [gal["A_cc"], gal["A_ct"]]
for ai, action in enumerate(actions, start=1):
    for x in D2_basis_masks:
        if row_action_mask(x, action) not in D2_set:
            raise SystemExit(f"action {ai} escaped 2A[4]")
    for x in D4_basis_masks:
        if row_action_mask(x, action) not in D4_set:
            raise SystemExit(f"action {ai} escaped 4A[8]")

out = {
    "schema": "STAGE33_07_INTRINSIC_AT2_DIVISIBILITY_FILTRATION_V1",
    "intrinsic_model": "A_Pic[2]=ker(Picard_Gram mod 2), represented by y/2",
    "filtration": {
        "A2_dimension_f2": 14,
        "two_A4_dimension_f2": 10,
        "four_A8_dimension_f2": 4,
        "two_A4_basis_rows_as_bitints_in_intrinsic_at2_basis": D2_basis_masks,
        "four_A8_basis_rows_as_bitints_in_intrinsic_at2_basis": D4_basis_masks,
        "retained_smith_model_two_A4_coordinate_span": "coordinates 5..14 for moduli [4^6,8^4]",
        "retained_smith_model_four_A8_coordinate_span": "coordinates 11..14 for moduli [8^4]",
    },
    "hensel_certificate": {
        "mod4_liftable_element_count": len(D2),
        "mod8_liftable_element_count": len(D4),
        "second_hensel_ambiguity_dimension_f2": len(h_piv),
    },
    "invariance": {
        "all_nine_geometric_actions_preserve_filtration": True,
        "named_cc_ct_preserve_filtration": True,
    },
    "execution": {
        "smith_form_used": False,
        "remote_cas_used": False,
        "enumerated_intrinsic_A2_elements": 1 << 14,
    },
    "exact_consequence": {
        "basis_independent_mixed_order_marking_materialized": True,
        "connecting_matrix_columns_explicitly_materialized": 0,
        "middle_gersten_module_action_materialized": False,
        "absolute_delta_loc_computed": False,
        "arithmetic_hs_closed": False,
    },
    "next_exact_leaf": "require intrinsic-to-retained A[2] transport to preserve 4A[8] subset 2A[4] subset A[2] and retest actual swap-pair uniqueness",
    "stage33_progress": "6/11",
    "stage33_08_released": False,
    "theorem_credit": False,
    "endpoint_credit": False,
}
out["canonical_sha256"] = csha(out)
OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "two_A4_dimension_f2": 10,
    "four_A8_dimension_f2": 4,
    "all_actions_preserve_filtration": True,
    "certificate_sha256": out["canonical_sha256"],
}, indent=2, sort_keys=True))
