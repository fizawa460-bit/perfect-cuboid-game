#!/usr/bin/env python3
"""Descend the exact local Picard coordinate swaps to intrinsic A_Pic[2].

For an integral lattice (L,G), an order-two discriminant class can be written
as y/2 mod L with y in F2^rank and G y^T = 0 mod 2. Thus
A_L[2] is canonically ker(G mod 2), with no Smith basis required.

We reuse the passing local Picard recovery leaf, derive this 14-dimensional
kernel, descend all nine source-locked geometric automorphisms, and certify
that the first two are the actual S3 coordinate swaps on A_L[2].
"""
from __future__ import annotations

import hashlib
import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
PICARD_SCRIPT = HERE / "certify_two_coordinate_swap_picard_rows.py"
OUT = HERE / "actual-coordinate-swap-at2-actions.json"
RANK = 64
AT2_DIM = 14


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def masks_from_rows(rows: list[list[int]]) -> list[int]:
    return [sum((int(x) & 1) << j for j, x in enumerate(row)) for row in rows]


def null_basis_masks(rows: list[int], ncols: int) -> list[int]:
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
    free = [j for j in range(ncols) if j not in piv]
    out = []
    for f in free:
        v = 1 << f
        for p in sorted(piv):
            if (piv[p] & v).bit_count() & 1:
                v ^= 1 << p
        if any((r & v).bit_count() & 1 for r in rows):
            raise SystemExit("GF2 null-basis verification failed")
        out.append(v)
    return out


def row_from_mask(mask: int, n: int) -> list[int]:
    return [(mask >> j) & 1 for j in range(n)]


def span_solver(basis_masks: list[int]):
    piv: dict[int, tuple[int, int]] = {}
    for i, raw in enumerate(basis_masks):
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
        if not x:
            raise SystemExit("AT2 basis unexpectedly dependent")

    def solve(raw: int) -> int:
        x, tag = int(raw), 0
        while x:
            p = x.bit_length() - 1
            if p not in piv:
                raise SystemExit("automorphism escaped intrinsic A[2] kernel")
            y, t = piv[p]
            x ^= y
            tag ^= t
        return tag

    return solve


def row_action_mask(mask: int, matrix: list[list[int]]) -> int:
    out = 0
    for j in range(len(matrix[0])):
        bit = 0
        for k in range(len(matrix)):
            if ((mask >> k) & 1) and (int(matrix[k][j]) & 1):
                bit ^= 1
        out |= bit << j
    return out


def mm2(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    bt = list(zip(*b))
    return [
        [sum((x & 1) * (y & 1) for x, y in zip(row, col)) & 1 for col in bt]
        for row in a
    ]


def pow2(a: list[list[int]], n: int) -> list[list[int]]:
    out = [[int(i == j) for j in range(len(a))] for i in range(len(a))]
    x = a
    while n:
        if n & 1:
            out = mm2(out, x)
        x = mm2(x, x)
        n >>= 1
    return out


def product2(mats: list[list[list[int]]]) -> list[list[int]]:
    n = len(mats[0])
    out = [[int(i == j) for j in range(n)] for i in range(n)]
    for m in mats:
        out = mm2(out, m)
    return out


ns = runpy.run_path(str(PICARD_SCRIPT))
gram = [[int(x) for x in row] for row in ns["gram"]]
known = ns["known"]
perms = ns["perms"]
indlist = ns["INDLIST"]
marking = ns["marking"]
parsed = ns["parsed"]
base = ns["base"]

if len(gram) != RANK or any(len(row) != RANK for row in gram):
    raise SystemExit("Picard Gram shape regression")

# y/2 lies in L^* iff G y^T is even. Since G is symmetric, this is the
# nullspace of G modulo 2. Its dimension must equal the number of nontrivial
# Smith factors: 4+6+4=14.
gram_masks = masks_from_rows(gram)
kernel_masks = null_basis_masks(gram_masks, RANK)
if len(kernel_masks) != AT2_DIM:
    raise SystemExit(f"intrinsic discriminant 2-torsion dimension regression: {len(kernel_masks)}")
solve_kernel = span_solver(kernel_masks)

all_picard = []
all_at2 = []
for idx, perm in enumerate(perms, start=1):
    action = [known[int(perm[j - 1]) - 1] for j in indlist]
    # Full known-class transport is the strongest marking check available.
    for j in range(len(known)):
        got = ns["row_times_matrix"](known[j], action)
        if got != known[int(perm[j]) - 1]:
            raise SystemExit(f"automorphism {idx} failed class transport at {j+1}")
    if ns["mm"](ns["mm"](action, gram), ns["transpose"](action)) != gram:
        raise SystemExit(f"automorphism {idx} failed Picard isometry check")
    rows = []
    for mask in kernel_masks:
        image = row_action_mask(mask, action)
        coords = solve_kernel(image)
        rows.append(row_from_mask(coords, AT2_DIM))
    all_picard.append(action)
    all_at2.append(rows)

I14 = [[int(i == j) for j in range(AT2_DIM)] for i in range(AT2_DIM)]
A12, A13 = all_at2[0], all_at2[1]
if mm2(A12, A12) != I14 or mm2(A13, A13) != I14:
    raise SystemExit("actual coordinate swap lost involutivity on A[2]")
if mm2(mm2(A12, A13), A12) != mm2(mm2(A13, A12), A13):
    raise SystemExit("actual coordinate swaps lost S3 braid relation on A[2]")

# Upstream generators 4..9 are the six coordinate signs a1,a2,a3,b1,b2,b3.
# Projectively the c-sign equals their product (simultaneous sign on all seven
# coordinates is scalar -1), so obtain all seven sign actions intrinsically.
six_signs = all_at2[3:9]
for i, a in enumerate(six_signs):
    if mm2(a, a) != I14:
        raise SystemExit(f"sign generator {i+1} is not involutive on A[2]")
for i in range(6):
    for j in range(i + 1, 6):
        if mm2(six_signs[i], six_signs[j]) != mm2(six_signs[j], six_signs[i]):
            raise SystemExit("coordinate sign actions stopped commuting")
Ac = product2(six_signs)
signs7 = six_signs + [Ac]

# Exact conjugation of coordinate signs by the two actual coordinate swaps.
perm12 = [1, 0, 2, 4, 3, 5, 6]
perm13 = [2, 1, 0, 5, 4, 3, 6]
for swap, perm, name in ((A12, perm12, "swap12"), (A13, perm13, "swap13")):
    for i in range(7):
        got = mm2(mm2(swap, signs7[i]), swap)
        if got != signs7[perm[i]]:
            raise SystemExit(f"{name} failed exact sign conjugation at sign {i+1}")

# The discriminant quadratic value on y/2 is (y G y)/4 mod 2. For this even
# lattice it is integral on the entire A[2] kernel. Record the intrinsic form
# and verify all actual automorphisms preserve it.
def qbit(mask: int) -> int:
    y = row_from_mask(mask, RANK)
    val = sum(y[i] * gram[i][j] * y[j] for i in range(RANK) for j in range(RANK))
    if val % 4:
        raise SystemExit("intrinsic A[2] quadratic value is not integral")
    return (val // 4) & 1

qdiag = [qbit(m) for m in kernel_masks]
polar = [[0] * AT2_DIM for _ in range(AT2_DIM)]
for i in range(AT2_DIM):
    for j in range(AT2_DIM):
        polar[i][j] = qbit(kernel_masks[i] ^ kernel_masks[j]) ^ qdiag[i] ^ qdiag[j]

def qcoords(row: list[int]) -> int:
    mask = 0
    for i, bit in enumerate(row):
        if bit & 1:
            mask ^= kernel_masks[i]
    return qbit(mask)

for idx, action in enumerate(all_at2, start=1):
    for i in range(AT2_DIM):
        if qcoords(action[i]) != qdiag[i]:
            raise SystemExit(f"automorphism {idx} failed intrinsic quadratic preservation")

out = {
    "schema": "STAGE33_07_ACTUAL_COORDINATE_SWAP_AT2_ACTIONS_V1",
    "intrinsic_discriminant_two_torsion": {
        "model": "ker(Picard_Gram_mod_2) represented by y/2 modulo Picard",
        "dimension_f2": AT2_DIM,
        "kernel_basis_rows_as_bitints_in_indlist_picard_basis": kernel_masks,
        "quadratic_diagonal_f2": qdiag,
        "quadratic_polar_matrix_f2": polar,
    },
    "actual_coordinate_swaps": {
        "swap12_at2_action_14x14": A12,
        "swap13_at2_action_14x14": A13,
        "identified_with_actual_integral_picard_swaps": True,
        "s3_relations_exact": True,
        "seven_coordinate_sign_conjugations_exact": True,
        "quadratic_form_preserved": True,
    },
    "all_nine_source_locked_geometric_at2_actions_14x14": all_at2,
    "seven_coordinate_sign_at2_actions_14x14": signs7,
    "source_locks": {
        "retained_stage32_marking_bundle_sha256": marking["canonical_sha256"],
        "stage32_picard_core_sha256": marking["stage32_picard_core_sha256"],
        "stage32_aut_action_sha256": marking["stage32_aut_action_sha256"],
        "prepared_hperp_input_sha256": parsed["prepared_sha"],
        "retained_picard_base_bundle_sha256": base["canonical_sha256"],
    },
    "execution": {
        "smith_form_used": False,
        "remote_cas_used": False,
        "method": "intrinsic discriminant two-torsion kernel over F2",
    },
    "exact_consequence": {
        "actual_geometric_swap_pair_identified_intrinsically_on_at2": True,
        "previous_finite_candidate_envelope_no_longer_needed_to_identify_swap_pair": True,
        "retained_smith_basis_transport_not_yet_materialized": True,
        "connecting_matrix_columns_explicitly_materialized": 0,
        "middle_gersten_module_action_materialized": False,
        "absolute_delta_loc_computed": False,
        "arithmetic_hs_closed": False,
    },
    "next_exact_leaf": "identify the intrinsic A_T[2] basis with the retained finite receiver basis using the seven sign actions and quadratic form, then impose actual swap naturality on the 26x16 extension map",
    "stage33_progress": "6/11",
    "stage33_08_released": False,
    "theorem_credit": False,
    "endpoint_credit": False,
}
out["canonical_sha256"] = csha(out)
OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "intrinsic_at2_dimension": AT2_DIM,
    "actual_swap_pair_identified": True,
    "s3_relations_exact": True,
    "seven_sign_conjugations_exact": True,
    "certificate_sha256": out["canonical_sha256"],
}, indent=2, sort_keys=True))
