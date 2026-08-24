#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

import sympy as sp
from sympy import ZZ
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

ROOT = Path(__file__).resolve().parent
picu = json.loads((ROOT / "picu-integral-action.json").read_text())
finite = json.loads((ROOT / "finite-v4-hypercohomology.json").read_text())
shape = json.loads((ROOT / "absolute-two-primary-shape.json").read_text())

Ga = sp.Matrix(picu["cc_mixed_action"])
Gb = sp.Matrix(picu["ct_mixed_action"])
if Ga.shape != (8, 8) or Gb.shape != (8, 8):
    raise SystemExit("unexpected Pic(Ubar) mixed-action shape")
if Ga * Ga != sp.eye(8) or Gb * Gb != sp.eye(8) or Ga * Gb != Gb * Ga:
    raise SystemExit("mixed V4 action regression")
if picu["pic_u_group"] != {"free_rank": 6, "torsion": [2, 2]}:
    raise SystemExit("Pic(Ubar) structure regression")
if finite["finite_v4_h2_free_rank"] != 0 or finite["finite_v4_h2_torsion_invariants"] != [2] * 33:
    raise SystemExit("finite UPic H2 regression")
if shape["pic_u_invariants"]["group"] != "(Z/2)^2":
    raise SystemExit("Pic(Ubar)^V4 invariant regression")

n = 8
I = sp.eye(n)


def resop(G, k):
    return G - I if k % 2 else G + I


def group_cob(Ga, Gb, r):
    D = sp.zeros((r + 1) * n, (r + 2) * n)
    for p in range(r + 1):
        q = r - p
        D[p*n:(p+1)*n, p*n:(p+1)*n] += ((-1) ** p) * resop(Gb, q + 1)
        D[p*n:(p+1)*n, (p+1)*n:(p+2)*n] += resop(Ga, p + 1)
    return D


def relation_matrix(copies):
    # Pic(Ubar)=Z^8/<2e1,2e2>; each cochain copy carries the same two relations.
    R = sp.zeros(2 * copies, n * copies)
    for c in range(copies):
        R[2*c, c*n] = 2
        R[2*c + 1, c*n + 1] = 2
    return R


def row_coefficients(v, B):
    piv = list(B.rref()[1])
    if len(piv) != B.rows:
        return None
    minor = B[:, piv]
    coeff = sp.Matrix(1, B.rows, [v[j] for j in piv]) * minor.inv()
    if coeff * B != v:
        return None
    if any(sp.Rational(x).q != 1 for x in coeff):
        return None
    return [int(x) for x in coeff]


D0 = group_cob(Ga, Gb, 0)
D1 = group_cob(Ga, Gb, 1)
if D0 * D1 != sp.zeros(D0.rows, D1.cols):
    raise SystemExit("V4 Pic(Ubar) cochain differential regression")
R0, R1, R2 = relation_matrix(1), relation_matrix(2), relation_matrix(3)
for i in range(R0.rows):
    if row_coefficients(R0.row(i) * D0, R1) is None:
        raise SystemExit("degree-zero torsion relation not respected")
for i in range(R1.rows):
    if row_coefficients(R1.row(i) * D1, R2) is None:
        raise SystemExit("degree-one torsion relation not respected")

# Kernel in the quotient: x is a cocycle iff x*D1 lies in the relation lattice R2.
# Solve (x,z) [D1; -R2] = 0 over Z.  Smith decomposition gives a saturated
# integral left-kernel basis; project it to the x coordinates and HNF the image.
A = D1.col_join(-R2)
Sdm, Udm, _ = smith_normal_decomp(DomainMatrix.from_Matrix(A).convert_to(ZZ))
S = Sdm.to_Matrix()
U = Udm.to_Matrix()
rankA = sum(1 for i in range(min(S.shape)) if S[i, i] != 0)
left_kernel = U[rankA:, :]
if left_kernel * A != sp.zeros(left_kernel.rows, A.cols):
    raise SystemExit("saturated left-kernel reconstruction failed")
projected = left_kernel[:, :D1.rows]
H = hermite_normal_form(projected.T).T
if H.rank() != H.rows:
    raise SystemExit("kernel row basis is not independent")

# Quotient by intrinsic presentation relations in C1 and by coboundaries im D0.
Q = R1.col_join(D0)
coords = []
for i in range(Q.rows):
    c = row_coefficients(Q.row(i), H)
    if c is None:
        raise SystemExit("coboundary/relation escaped the cocycle lattice")
    coords.append(c)
C = sp.Matrix(coords)
SN = smith_normal_form(C, domain=ZZ)
rankC = C.rank()
diag = [abs(int(SN[i, i])) for i in range(min(SN.shape)) if SN[i, i] != 0]
h1_free = H.rows - rankC
h1_torsion = [d for d in diag if d != 1]
if h1_free != 0 or h1_torsion != [2] * 9:
    raise SystemExit(f"unexpected H1(V4,PicU): free={h1_free}, torsion={h1_torsion}")

# Spectral-sequence bookkeeping for the exact two-term complex.
# U_D=Z^14 is trivial, so H2(V4,U_D)=(Z/2)^28.
# Pic(Ubar)^V4=(Z/2)^2, so r01=rank d2^{0,1} is 0,1,2.
# With total H2 dimension 33, the right-filtration kernel has dimension
# 33-(28-r01)=5+r01.  Since H1(V4,PicU) has dimension 9, the finite d2^{1,1}
# rank is 9-(5+r01)=4-r01.  Thus only three exact rank pairs remain.
possible = []
for r01 in (0, 1, 2):
    right_kernel = 5 + r01
    r11 = 9 - right_kernel
    possible.append({
        "rank_d2_01": r01,
        "left_H2U_quotient_dimension": 28 - r01,
        "right_kernel_dimension": right_kernel,
        "rank_d2_11": r11,
    })
if [(x["rank_d2_01"], x["rank_d2_11"]) for x in possible] != [(0,4),(1,3),(2,2)]:
    raise SystemExit("finite transgression envelope arithmetic regression")

cert = {
    "schema": "STAGE33_03_FINITE_V4_TRANSGRESSION_ENVELOPE_V1",
    "source_locks": {
        "picu_integral_action_sha256": picu["canonical_sha256"],
        "finite_v4_hypercohomology_sha256": finite["canonical_sha256"],
        "absolute_two_primary_shape_sha256": shape["canonical_sha256"],
    },
    "H1_V4_PicU": {
        "free_rank": 0,
        "torsion_invariants": [2] * 9,
        "f2_dimension": 9,
        "mixed_integral_torsion_action_included": True,
    },
    "H2_V4_unit_lattice": {
        "unit_rank": 14,
        "action": "trivial",
        "f2_dimension": 28,
    },
    "PicU_V4_invariants": {
        "group": "(Z/2)^2",
        "f2_dimension": 2,
    },
    "total_H2_V4_UPic": {
        "group": "(Z/2)^33",
        "f2_dimension": 33,
    },
    "possible_finite_transgression_rank_pairs": possible,
    "finite_rank_pair_ambiguity_count": 3,
    "finite_transgression_unknown_reduced_to_rank_d2_01_in_0_1_2": True,
    "absolute_kernel_character_terms_still_open": True,
    "next_exact_leaf": "L33-03-COMPUTE-FINITE-d2_01-RANK-THEN-ABSOLUTE-N-CHARACTER-d2_11",
    "br0b_all_primary_classes_accounted": False,
    "theorem_credit": False,
    "endpoint_credit": False,
}
canonical = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
cert["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
(ROOT / "finite-transgression-envelope.json").write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
print(json.dumps({
    "success": True,
    "H1_V4_PicU": "(Z/2)^9",
    "possible_rank_pairs": [[x["rank_d2_01"], x["rank_d2_11"]] for x in possible],
    "next_exact_leaf": cert["next_exact_leaf"],
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
