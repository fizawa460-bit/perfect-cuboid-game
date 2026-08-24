#!/usr/bin/env python3
"""Materialize the unique Pic(Ubar) extension obstruction and inflate it to Q.

For 0 -> T -> P -> F -> 0 with P=Pic(Ubar), T=(Z/2)^2 and F=Z^6,
Stage33-03 has reduced the finite connecting image
  H^1(V4,F) -> H^2(V4,T)
to a one-dimensional F2 subspace.  This script constructs that actual class
from the exact mixed integral V4 action on P, expresses it in the standard
H^2(V4,F2) basis (cc^2, cc*ct, ct^2) for each torsion coordinate, and then
inflates it to G_Q.

The quotient characters are cc=chi_{-1} and ct=chi_2.  Under Kummer/Brauer
identification the three basis classes inflate to quaternion symbols
(-1,-1), (-1,2), (2,2).  Here (-1,2)=0 because 2=N_{Q(i)/Q}(1+i), and
(2,2)=(2,-1)=(-1,2)=0, while (-1,-1) is nonzero already at the real place.
Thus absolute inflation is detected exactly by the cc^2 coefficient in each
of the two T coordinates.
"""
import hashlib
import json
from pathlib import Path

import sympy as sp
from sympy import ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

ROOT = Path(__file__).resolve().parent
picu = json.loads((ROOT / "picu-integral-action.json").read_text())
envelope = json.loads((ROOT / "absolute-h1-picu-envelope.json").read_text())
h3 = json.loads((ROOT / "absolute-h3-tate-vanishing.json").read_text())

if envelope["remaining_ambiguity_dimension_f2"] != 1:
    raise SystemExit("absolute H1 envelope is not one-dimensional")
if not h3["absolute_d2_11_zero"]:
    raise SystemExit("absolute d2_11 regression")
if picu["pic_u_group"] != {"free_rank": 6, "torsion": [2, 2]}:
    raise SystemExit("Pic(Ubar) structure regression")

PA = [[int(x) for x in row] for row in picu["cc_mixed_action"]]
PB = [[int(x) for x in row] for row in picu["ct_mixed_action"]]
FA = sp.Matrix([row[2:] for row in PA[2:]])
FB = sp.Matrix([row[2:] for row in PB[2:]])
I6 = sp.eye(6)
if FA * FA != I6 or FB * FB != I6 or FA * FB != FB * FA:
    raise SystemExit("free V4 action regression")

# Direct normalized inhomogeneous 1-cocycle equations for right actions.
# A cocycle is determined by x=z(cc), y=z(ct):
# x(A+1)=0, y(B+1)=0, x(B-1)-y(A-1)=0.
C = sp.zeros(12, 18)
C[0:6, 0:6] = FA + I6
C[6:12, 6:12] = FB + I6
C[0:6, 12:18] = FB - I6
C[6:12, 12:18] = -(FA - I6)
Sdm, Udm, _ = smith_normal_decomp(DomainMatrix.from_Matrix(C).convert_to(ZZ))
S = Sdm.to_Matrix()
U = Udm.to_Matrix()
rankC = sum(1 for i in range(min(S.shape)) if S[i, i] != 0)
Z1 = U[rankC:, :]
if Z1.rows != 6 or Z1 * C != sp.zeros(Z1.rows, C.cols):
    raise SystemExit("unexpected saturated Z1(V4,F) lattice")

# Coboundaries m -> (m(A-1),m(B-1)); they must lie in Z1.
B1 = (FA - I6).row_join(FB - I6)
if B1 * C != sp.zeros(B1.rows, C.cols):
    raise SystemExit("direct cocycle convention mismatch")

# Confirm the quotient Z1/B1 is exactly (Z/2)^6 by expressing B1 in Z1.
def row_coefficients(v, basis):
    piv = list(basis.rref()[1])
    if len(piv) != basis.rows:
        raise SystemExit("dependent cocycle basis")
    minor = basis[:, piv]
    coeff = sp.Matrix(1, basis.rows, [v[j] for j in piv]) * minor.inv()
    if coeff * basis != v or any(sp.Rational(x).q != 1 for x in coeff):
        raise SystemExit("coboundary not integral in cocycle lattice")
    return [int(x) for x in coeff]

Bcoords = sp.Matrix([row_coefficients(B1.row(i), Z1) for i in range(B1.rows)])
Sbc, _, _ = smith_normal_decomp(DomainMatrix.from_Matrix(Bcoords).convert_to(ZZ))
SbcM = Sbc.to_Matrix()
diag = [abs(int(SbcM[i, i])) for i in range(min(SbcM.shape)) if SbcM[i, i] != 0]
if diag != [2] * 6:
    raise SystemExit(f"H1(V4,F) is not (Z/2)^6: {diag}")

# V4 bookkeeping.
G = ("id", "cc", "ct", "cct")
bits = {"id": (0, 0), "cc": (1, 0), "ct": (0, 1), "cct": (1, 1)}
bybits = {v: k for k, v in bits.items()}
def mul(g, h):
    return bybits[(bits[g][0] ^ bits[h][0], bits[g][1] ^ bits[h][1])]

FI = sp.eye(6)
Factions = {"id": FI, "cc": FA, "ct": FB, "cct": FA * FB}
PI = [[1 if i == j else 0 for j in range(8)] for i in range(8)]

def compose_p(A, B):
    rows = []
    for r in A:
        rows.append(p_apply(r, B))
    return rows


def p_apply(row, A):
    out = [sum(int(row[i]) * int(A[i][j]) for i in range(8)) for j in range(8)]
    out[0] %= 2
    out[1] %= 2
    return out

Pactions = {"id": PI, "cc": PA, "ct": PB, "cct": compose_p(PA, PB)}

def f_apply(row, A):
    v = sp.Matrix([row]) * A
    return [int(v[0, j]) for j in range(6)]

def add(a, b):
    return [x + y for x, y in zip(a, b)]

def sub(a, b):
    return [x - y for x, y in zip(a, b)]

def p_add(a, b):
    out = add(a, b)
    out[0] %= 2
    out[1] %= 2
    return out

def p_sub(a, b):
    out = sub(a, b)
    out[0] %= 2
    out[1] %= 2
    return out

def lift_f(v):
    return [0, 0] + [int(x) for x in v]


def obstruction_from_z1(row):
    x = [int(row[j]) for j in range(6)]
    y = [int(row[6 + j]) for j in range(6)]
    zf = {
        "id": [0] * 6,
        "cc": x,
        "ct": y,
        "cct": add(f_apply(x, FB), y),
    }
    # Exact F-valued 1-cocycle check.
    for g in G:
        for h in G:
            lhs = add(f_apply(zf[g], Factions[h]), zf[h])
            if lhs != zf[mul(g, h)]:
                raise SystemExit(f"F cocycle identity failed for {g},{h}")
    zp = {g: lift_f(zf[g]) for g in G}
    coc = {}
    for g in G:
        for h in G:
            val = p_sub(p_add(p_apply(zp[g], Pactions[h]), zp[h]), zp[mul(g, h)])
            if val[2:] != [0] * 6:
                raise SystemExit("connecting cocycle escaped T")
            coc[(g, h)] = val[:2]
    # For trivial T, H^2(V4,F2) coordinates are q(cc), comm(cc,ct), q(ct).
    triples = []
    for t in range(2):
        qcc = coc[("cc", "cc")][t] & 1
        cross = (coc[("cc", "ct")][t] ^ coc[("ct", "cc")][t]) & 1
        qct = coc[("ct", "ct")][t] & 1
        triples.append([qcc, cross, qct])
    return triples


def flat(triples):
    return [x for tri in triples for x in tri]

def rank_f2(rows):
    if not rows:
        return 0
    a = [[x & 1 for x in row] for row in rows]
    rank = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(rank, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        for i in range(len(a)):
            if i != rank and a[i][col]:
                a[i] = [x ^ y for x, y in zip(a[i], a[rank])]
        rank += 1
    return rank

# Connecting classes on a saturated Z1 basis span the full connecting image.
raw_images = [obstruction_from_z1(Z1.row(i)) for i in range(Z1.rows)]
flat_images = [flat(x) for x in raw_images]
if rank_f2(flat_images) != 1:
    raise SystemExit(f"connecting image rank is not one: {flat_images}")
nonzero = next((v for v in flat_images if any(v)), None)
if nonzero is None:
    raise SystemExit("connecting image unexpectedly zero")
unique = [nonzero[0:3], nonzero[3:6]]

# Coboundaries must map to the zero H^2 class under the same triple invariant.
for i in range(B1.rows):
    if any(flat(obstruction_from_z1(B1.row(i)))):
        raise SystemExit("connecting invariant does not kill a coboundary")

# Inflate cc=chi_-1, ct=chi_2 to G_Q.  In each T coordinate:
# cc^2 -> (-1,-1) != 0; cc*ct -> (-1,2)=0; ct^2 -> (2,2)=0.
inflated_T_coordinates = [tri[0] & 1 for tri in unique]
inflation_zero = not any(inflated_T_coordinates)
finite_complement_dim = 6 if inflation_zero else 5

cert = {
    "schema": "STAGE33_03_PICU_EXTENSION_OBSTRUCTION_INFLATION_V1",
    "source_locks": {
        "picu_integral_action_sha256": picu["canonical_sha256"],
        "absolute_h1_picu_envelope_sha256": envelope["canonical_sha256"],
        "absolute_h3_tate_vanishing_sha256": h3["canonical_sha256"],
    },
    "quotient_character_dictionary": {
        "cc": "chi_{-1}, cutting out Q(i)",
        "ct": "chi_2, cutting out Q(sqrt(2))",
    },
    "H2_V4_T_basis_per_torsion_coordinate": ["cc^2", "cc*ct", "ct^2"],
    "unique_finite_connecting_obstruction": unique,
    "global_quaternion_dictionary": {
        "cc^2": "(-1,-1), nonzero at the real place",
        "cc*ct": "(-1,2)=0 because 2=N_{Q(i)/Q}(1+i)",
        "ct^2": "(2,2)=(2,-1)=(-1,2)=0",
    },
    "inflated_obstruction_T_coordinates_f2": inflated_T_coordinates,
    "unique_obstruction_inflates_to_zero": inflation_zero,
    "absolute_H1_PicU_finite_complement_dimension_f2": finite_complement_dim,
    "absolute_H1_PicU_abstract_inventory": (
        f"Hom_cont(G_Q,(Z/2)^2) direct-sum (Z/2)^{finite_complement_dim} (noncanonical splitting)"
    ),
    "absolute_H1_PicU_all_classes_accounted": True,
    "remaining_H1_PicU_ambiguity_dimension_f2": 0,
    "next_exact_leaf": "L33-03-ASSEMBLE-ALL-PRIMARY-BR0B-FILTRATION",
    "br0b_all_primary_classes_accounted": False,
    "unit_closed": False,
    "new_theorem_required": False,
    "theorem_credit": False,
    "endpoint_credit": False,
    "perfect_cuboid_nonexistence_claim": False,
}
canonical = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
cert["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
(ROOT / "picu-extension-obstruction-inflation.json").write_text(
    json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps({
    "success": True,
    "unique_finite_connecting_obstruction": unique,
    "unique_obstruction_inflates_to_zero": inflation_zero,
    "absolute_H1_PicU_finite_complement_dimension_f2": finite_complement_dim,
    "next_exact_leaf": cert["next_exact_leaf"],
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
