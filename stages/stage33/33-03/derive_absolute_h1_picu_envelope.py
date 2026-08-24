#!/usr/bin/env python3
"""Reduce H^1(G_Q,Pic(Ubar)) to one finite inflation bit.

Let T=Pic(Ubar)_tors=(Z/2)^2 and F=Pic(Ubar)/T=Z^6.  The full action factors
through V4.  Since N=Gal(Qbar/L) acts trivially and Hom_cont(N,F)=0,
inflation-restriction gives H^1(G_Q,F)=H^1(V4,F).  We compute the latter
exactly from the integral free quotient action.

The exact sequence 0->T->Pic(Ubar)->F->0 then compares finite and absolute
H^1.  Finite Stage33-03 already gives H^1(V4,PicU)=(Z/2)^9, while
H^1(V4,T)=Hom(V4,T)=(Z/2)^4.  The finite liftable subspace in H^1(V4,F)
has dimension 5.  The only possible enlargement over G_Q comes from the
unique one-dimensional image of the finite connecting map becoming zero
after inflation H^2(V4,T)->H^2(G_Q,T).  Thus the entire remaining H^1 wall
is one explicit F2 obstruction class.
"""
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
finite_env = json.loads((ROOT / "finite-transgression-envelope.json").read_text())
h3 = json.loads((ROOT / "absolute-h3-tate-vanishing.json").read_text())

if picu["pic_u_group"] != {"free_rank": 6, "torsion": [2, 2]}:
    raise SystemExit("Pic(Ubar) structure regression")
if picu["torsion_joint_fixed_dimension_f2"] != 2:
    raise SystemExit("torsion is no longer jointly fixed")
if finite_env["H1_V4_PicU"]["torsion_invariants"] != [2] * 9:
    raise SystemExit("finite H1(PicU) regression")
if not h3["absolute_d2_11_zero"]:
    raise SystemExit("absolute d2_11 is not closed")

Ga = sp.Matrix([row[2:] for row in picu["cc_mixed_action"][2:]])
Gb = sp.Matrix([row[2:] for row in picu["ct_mixed_action"][2:]])
if Ga.shape != (6, 6) or Gb.shape != (6, 6):
    raise SystemExit("free quotient action shape regression")
I = sp.eye(6)
if Ga * Ga != I or Gb * Gb != I or Ga * Gb != Gb * Ga:
    raise SystemExit("free quotient action is not V4")
if (int(sp.trace(Ga)), int(sp.trace(Gb)), int(sp.trace(Ga * Gb))) != (0, -2, -4):
    raise SystemExit("free quotient trace regression")


def resop(G, k):
    return G - I if k % 2 else G + I


def group_cob(Ga, Gb, r):
    n = Ga.rows
    D = sp.zeros((r + 1) * n, (r + 2) * n)
    for p in range(r + 1):
        q = r - p
        D[p*n:(p+1)*n, p*n:(p+1)*n] += ((-1) ** p) * resop(Gb, q + 1)
        D[p*n:(p+1)*n, (p+1)*n:(p+2)*n] += resop(Ga, p + 1)
    return D


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
    raise SystemExit("free quotient cochain differential regression")

# Saturated integral left kernel of D1.
Sdm, Udm, _ = smith_normal_decomp(DomainMatrix.from_Matrix(D1).convert_to(ZZ))
S = Sdm.to_Matrix()
U = Udm.to_Matrix()
rankD1 = sum(1 for i in range(min(S.shape)) if S[i, i] != 0)
left_kernel = U[rankD1:, :]
if left_kernel * D1 != sp.zeros(left_kernel.rows, D1.cols):
    raise SystemExit("free H1 saturated kernel reconstruction failed")
H = hermite_normal_form(left_kernel.T).T
if H.rank() != H.rows:
    raise SystemExit("free H1 kernel basis dependent")

coords = []
for i in range(D0.rows):
    c = row_coefficients(D0.row(i), H)
    if c is None:
        raise SystemExit("free coboundary escaped cocycle lattice")
    coords.append(c)
C = sp.Matrix(coords)
SN = smith_normal_form(C, domain=ZZ)
rankC = C.rank()
diag = [abs(int(SN[i, i])) for i in range(min(SN.shape)) if SN[i, i] != 0]
h1_free = H.rows - rankC
h1_torsion = [d for d in diag if d != 1]
if h1_free != 0 or h1_torsion != [2] * 6:
    raise SystemExit(f"unexpected H1(V4,F): free={h1_free}, torsion={h1_torsion}")

h1_v4_F_dim = 6
h1_v4_T_dim = 4  # Hom(V4,(Z/2)^2)
h1_v4_P_dim = 9
finite_liftable_F_dim = h1_v4_P_dim - h1_v4_T_dim
finite_connecting_image_dim = h1_v4_F_dim - finite_liftable_F_dim
if finite_liftable_F_dim != 5 or finite_connecting_image_dim != 1:
    raise SystemExit("finite PicU extension dimension bookkeeping regression")

cert = {
    "schema": "STAGE33_03_ABSOLUTE_H1_PICU_ENVELOPE_V1",
    "source_locks": {
        "picu_integral_action_sha256": picu["canonical_sha256"],
        "finite_transgression_envelope_sha256": finite_env["canonical_sha256"],
        "absolute_h3_tate_vanishing_sha256": h3["canonical_sha256"],
    },
    "T": "(Z/2)^2 with trivial absolute G_Q action",
    "F": "Z^6 with action factoring through V4 and F^V4=0",
    "H1_V4_F": "(Z/2)^6",
    "H1_V4_T": "(Z/2)^4",
    "H1_V4_PicU": "(Z/2)^9",
    "finite_liftable_F_subspace_dimension_f2": 5,
    "finite_connecting_image_dimension_f2": 1,
    "H1_GQ_F_equals_H1_V4_F": True,
    "absolute_character_subspace": "H^1(G_Q,T)=Hom_cont(G_Q,(Z/2)^2)",
    "absolute_H1_PicU_lower_presentation": (
        "generated by Hom_cont(G_Q,(Z/2)^2) plus a 5-dimensional finite V4 complement"
    ),
    "absolute_H1_PicU_only_remaining_ambiguity": (
        "whether the unique nonzero finite connecting class in H^2(V4,T) inflates to zero in H^2(G_Q,T)"
    ),
    "remaining_ambiguity_dimension_f2": 1,
    "if_obstruction_inflates_nonzero_finite_complement_dimension": 5,
    "if_obstruction_inflates_zero_finite_complement_dimension": 6,
    "remaining_wall": "R33-BR0B-UNIQUE-PICU-EXTENSION-OBSTRUCTION-INFLATION",
    "next_exact_leaf": "L33-03-MATERIALIZE-UNIQUE-PICU-EXTENSION-OBSTRUCTION-AND-INFLATE",
    "br0b_all_primary_classes_accounted": False,
    "unit_closed": False,
    "new_theorem_required": False,
    "theorem_credit": False,
    "endpoint_credit": False,
    "perfect_cuboid_nonexistence_claim": False,
}
canonical = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
cert["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
(ROOT / "absolute-h1-picu-envelope.json").write_text(
    json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps({
    "success": True,
    "H1_V4_F": "(Z/2)^6",
    "finite_connecting_image_dimension_f2": 1,
    "remaining_ambiguity_dimension_f2": 1,
    "next_exact_leaf": cert["next_exact_leaf"],
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
