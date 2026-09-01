#!/usr/bin/env python3
"""Exact local diagnostic for the Kc->S Picard pullback and its mod-2 kernel.

Use only already-locked repository certificates.  No remote CAS is needed.

The exact integral pullback P: Pic(Kc)->Pic(S) and the locked integral V4 actions
on Pic(S) determine, when the pullback image is stable, unique induced integral
actions K_g by

    K_g P = P S_g.

We verify that identity over Z for cc and ct.  We then inspect P modulo 2.  The
current J2 raw ct divisor support is transported through P before being projected
to H^1(V4,Pic(S)/2).  If P mod 2 has a kernel, Kc-side Galois defects can be
invisible after transport.  This diagnostic records that exact information
without changing the named J2 source, target, or any Kummer relation credit.
"""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
ADJOINT = HERE / "j2-picard-adjoint-proper-br2.json"
PIC = S33 / "33-07" / "retained-picard-base-sparse.json"
CT = HERE / "j2-ct-six-kc-support-fullpic64-pullbacks.json"
J2_TARGET = HERE / "j2-named-v4-h1-target-before-source-orientation.json"

ADJOINT_SHA = "066e6b039eb7b67c6dfc44a7af1459254c190ebfa5376e89b8e97fad1c8cb9f8"
PIC_SHA = "e41df3f84760b941440035a388baac88602126c80140139ddf9c187bedf0bb49"
CT_SHA = "592704594d6d26f9e0b0b2ba529d50c34fd801cede779b4e42b1cf775b63a96d"
J2_TARGET_SHA = "4625b6d3ea19ec0e4d8a51471c7f60c0c1219de4672d84c64779c4213306f3b3"
NK = 20
NS = 64


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def locked(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body), path
    return obj


def expand_sparse_integer(obj: dict) -> list[list[int]]:
    out: list[list[int]] = []
    for sparse in obj["matrix_64x64_sparse_rows_1based"]:
        row = [0] * NS
        for column, value in sparse:
            row[int(column) - 1] = int(value)
        out.append(row)
    assert len(out) == NS
    return out


def matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def matmul_q(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), Fraction(0)) for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*a)]


def pivot_columns(a: list[list[int]]) -> list[int]:
    m = [[Fraction(x) for x in row] for row in a]
    rows = len(m)
    cols = len(m[0])
    r = 0
    pivots: list[int] = []
    for c in range(cols):
        p = next((i for i in range(r, rows) if m[i][c]), None)
        if p is None:
            continue
        m[r], m[p] = m[p], m[r]
        q = m[r][c]
        m[r] = [x / q for x in m[r]]
        for i in range(rows):
            if i != r and m[i][c]:
                q = m[i][c]
                m[i] = [m[i][j] - q * m[r][j] for j in range(cols)]
        pivots.append(c)
        r += 1
        if r == rows:
            break
    return pivots


def invert_q(a: list[list[int]]) -> list[list[Fraction]]:
    n = len(a)
    m = [[Fraction(a[i][j]) for j in range(n)] + [Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        p = next((r for r in range(c, n) if m[r][c]), None)
        assert p is not None
        m[c], m[p] = m[p], m[c]
        q = m[c][c]
        m[c] = [x / q for x in m[c]]
        for r in range(n):
            if r != c and m[r][c]:
                q = m[r][c]
                m[r] = [m[r][j] - q * m[c][j] for j in range(2 * n)]
    return [row[n:] for row in m]


def induced_action(P: list[list[int]], S: list[list[int]], pivots: list[int]) -> list[list[int]]:
    PS = matmul(P, S)
    Q = [[P[i][j] for j in pivots] for i in range(NK)]
    R = [[PS[i][j] for j in pivots] for i in range(NK)]
    Kq = matmul_q([[Fraction(x) for x in row] for row in R], invert_q(Q))
    assert all(x.denominator == 1 for row in Kq for x in row)
    K = [[int(x) for x in row] for row in Kq]
    assert matmul(K, P) == PS
    return K


def rowmul_f2(v: list[int], m: list[list[int]]) -> list[int]:
    return [sum((v[i] & 1) * (m[i][j] & 1) for i in range(len(v))) & 1 for j in range(len(m[0]))]


def xor(a: list[int], b: list[int]) -> list[int]:
    return [x ^ y for x, y in zip(a, b)]


def identity(n: int) -> list[list[int]]:
    return [[int(i == j) for j in range(n)] for i in range(n)]


def homogeneous_nullspace_f2(equations: list[int], nvars: int) -> tuple[int, list[int]]:
    pivots: dict[int, int] = {}
    for eq in equations:
        x = eq
        while x:
            p = x.bit_length() - 1
            if p in pivots:
                x ^= pivots[p]
            else:
                pivots[p] = x
                break
    free = [i for i in range(nvars) if i not in pivots]
    basis: list[int] = []
    for f in free:
        x = 1 << f
        for p in sorted(pivots):
            lower = pivots[p] & ((1 << p) - 1)
            if (lower & x).bit_count() & 1:
                x |= 1 << p
        basis.append(x)
    return len(pivots), basis


def bits(mask: int, n: int) -> list[int]:
    return [(mask >> i) & 1 for i in range(n)]


def support(v: list[int]) -> list[int]:
    return [i + 1 for i, x in enumerate(v) if x & 1]


def coordinates_in_basis(v: list[int], basis_masks: list[int]) -> list[int] | None:
    target = sum((x & 1) << i for i, x in enumerate(v))
    # Kernel dimension is expected to be small.  Use labelled elimination rather
    # than exponential enumeration so the routine remains exact if it is not.
    echelon: dict[int, tuple[int, int]] = {}
    for i, vec in enumerate(basis_masks):
        x = vec
        lab = 1 << i
        while x:
            p = x.bit_length() - 1
            if p in echelon:
                x ^= echelon[p][0]
                lab ^= echelon[p][1]
            else:
                echelon[p] = (x, lab)
                break
    lab = 0
    x = target
    while x:
        p = x.bit_length() - 1
        if p not in echelon:
            return None
        x ^= echelon[p][0]
        lab ^= echelon[p][1]
    return bits(lab, len(basis_masks))


adj = locked(ADJOINT, ADJOINT_SHA)
pic = locked(PIC, PIC_SHA)
ct = locked(CT, CT_SHA)
j2_target = locked(J2_TARGET, J2_TARGET_SHA)

P = [[int(x) for x in row] for row in adj["degree2_picard_adjoint"]["picard_pullback_matrix_P_20x64"]]
indlistK = [int(x) for x in adj["degree2_picard_adjoint"]["semantic_Kc_basis_BigK_indices_1based"]]
assert len(P) == NK and all(len(row) == NS for row in P)
assert len(indlistK) == NK

Scc = expand_sparse_integer(pic["objects"]["cc"])
Sct = expand_sparse_integer(pic["objects"]["ct"])
I64 = identity(NS)
assert matmul(Scc, Scc) == I64
assert matmul(Sct, Sct) == I64
assert matmul(Scc, Sct) == matmul(Sct, Scc)

pivots = pivot_columns(P)
assert len(pivots) == NK
Kcc = induced_action(P, Scc, pivots)
Kct = induced_action(P, Sct, pivots)
I20 = identity(NK)
assert matmul(Kcc, Kcc) == I20
assert matmul(Kct, Kct) == I20
assert matmul(Kcc, Kct) == matmul(Kct, Kcc)

# F2 kernel of x -> xP, with x in F2^20.
equations = []
for j in range(NS):
    mask = 0
    for i in range(NK):
        if P[i][j] & 1:
            mask |= 1 << i
    equations.append(mask)
rank_mod2, kernel_masks = homogeneous_nullspace_f2(equations, NK)
kernel_basis = [bits(mask, NK) for mask in kernel_masks]
for v in kernel_basis:
    assert rowmul_f2(v, P) == [0] * NS

raw_support_bigk = [int(row["BigK_index_1based"]) for row in ct["pullbacks"]]
assert len(raw_support_bigk) == 6
position = {bigk: i for i, bigk in enumerate(indlistK)}
assert all(bigk in position for bigk in raw_support_bigk)
r = [0] * NK
for bigk in raw_support_bigk:
    r[position[bigk]] ^= 1
raw_ct = [int(x) & 1 for x in ct["ct_sum_fullPic64_historical_Magma_coordinates_mod2"]]
assert rowmul_f2(r, P) == raw_ct
assert raw_ct == [int(x) & 1 for x in j2_target["raw_named_J2_cocycle_historical_Magma_Pic64_mod2"]["ct"]]

Kcc2 = [[x & 1 for x in row] for row in Kcc]
Kct2 = [[x & 1 for x in row] for row in Kct]
defect_cc = xor(rowmul_f2(r, Kcc2), r)
defect_ct = xor(rowmul_f2(r, Kct2), r)
assert rowmul_f2(defect_cc, P) == [0] * NS
assert rowmul_f2(defect_ct, P) == [0] * NS
coord_cc = coordinates_in_basis(defect_cc, kernel_masks)
coord_ct = coordinates_in_basis(defect_ct, kernel_masks)
assert coord_cc is not None and coord_ct is not None

result = {
    "success": True,
    "schema": "STAGE33_12_J2_PICARD_PULLBACK_MOD2_KERNEL_DIAGNOSTIC_V1",
    "source_locks": {
        "j2_picard_adjoint_canonical_sha256": ADJOINT_SHA,
        "retained_picard_base_sparse_canonical_sha256": PIC_SHA,
        "j2_ct_pullbacks_canonical_sha256": CT_SHA,
        "j2_named_75D_target_canonical_sha256": J2_TARGET_SHA,
    },
    "integral_naturality": {
        "pullback_shape": [NK, NS],
        "pullback_rank_over_Q": len(pivots),
        "pivot_columns_1based": [j + 1 for j in pivots],
        "unique_induced_cc_integral": True,
        "unique_induced_ct_integral": True,
        "cc_equation_KP_equals_PS": True,
        "ct_equation_KP_equals_PS": True,
        "induced_actions_are_commuting_involutions": True,
    },
    "mod2_pullback": {
        "rank_f2": rank_mod2,
        "kernel_dimension_f2": NK - rank_mod2,
        "kernel_basis_supports_1based_in_semantic_Kc20": [support(v) for v in kernel_basis],
    },
    "j2_raw_ct_support": {
        "BigK_indices_1based": raw_support_bigk,
        "semantic_Kc20_support_1based": support(r),
        "pullback_equals_locked_raw_ct": True,
        "cc_action_defect_support_1based": support(defect_cc),
        "ct_action_defect_support_1based": support(defect_ct),
        "cc_action_defect_kernel_coordinates_f2": coord_cc,
        "ct_action_defect_kernel_coordinates_f2": coord_ct,
        "Kc_support_cc_fixed_mod2": not any(defect_cc),
        "Kc_support_ct_fixed_mod2": not any(defect_ct),
        "both_action_defects_die_under_pullback_mod2": True,
    },
    "interpretation": (
        "RAW_CT_KC_SUPPORT_HAS_NONZERO_GALOIS_DEFECT_HIDDEN_BY_MOD2_PULLBACK_KERNEL"
        if any(defect_cc) or any(defect_ct)
        else "RAW_CT_KC_SUPPORT_IS_ALREADY_V4_FIXED_MOD2_UNDER_THE_UNIQUE_INDUCED_ACTION"
    ),
    "firewall": {
        "diagnostic_only": True,
        "named_j2_source_coordinate_changed": False,
        "named_j2_target_coordinate_changed": False,
        "named_kummer_relation_restored": False,
        "standard_kummer_column_materialized": False,
        "actual_geometric_extension_identified": False,
        "stage33_12_closed_exact": False,
        "stage33_13_released": False,
        "theorem_credit": False,
        "receiver_credit": False,
        "endpoint_credit": False,
    },
}
print(json.dumps(result, sort_keys=True))
