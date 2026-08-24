#!/usr/bin/env python3
"""Exact absolute H^1 inventory for Pic(Ubar)."""
import hashlib, json
from pathlib import Path
import sympy as sp
from sympy import ZZ
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

ROOT=Path(__file__).resolve().parent
picu=json.loads((ROOT/"picu-integral-action.json").read_text())
finite=json.loads((ROOT/"finite-transgression-envelope.json").read_text())
h3=json.loads((ROOT/"absolute-h3-tate-vanishing.json").read_text())
if picu["pic_u_group"]!={"free_rank":6,"torsion":[2,2]}: raise SystemExit("PicU shape regression")
if finite["H1_V4_PicU"]["torsion_invariants"]!=[2]*9: raise SystemExit("finite PicU H1 regression")
if not h3["absolute_d2_11_zero"]: raise SystemExit("absolute d2_11 not closed")

cc=[[int(x) for x in r] for r in picu["cc_mixed_action"]]
ct=[[int(x) for x in r] for r in picu["ct_mixed_action"]]
for name,A in (("cc",cc),("ct",ct)):
    if any(A[i][j] for i in range(2) for j in range(2,8)): raise SystemExit(f"{name}: T->F mixing")
    if any(A[i][j] for i in range(2,8) for j in range(2)): raise SystemExit(f"{name}: F->T mixing")
Ga=sp.Matrix([r[2:] for r in cc[2:]]); Gb=sp.Matrix([r[2:] for r in ct[2:]])
I=sp.eye(6)
if Ga*Ga!=I or Gb*Gb!=I or Ga*Gb!=Gb*Ga: raise SystemExit("free action not V4")
if (int(sp.trace(Ga)),int(sp.trace(Gb)),int(sp.trace(Ga*Gb)))!=(0,-2,-4): raise SystemExit("free trace regression")

def rop(G,k): return G-I if k%2 else G+I
def cob(r):
    D=sp.zeros((r+1)*6,(r+2)*6)
    for p in range(r+1):
        q=r-p
        D[p*6:(p+1)*6,p*6:(p+1)*6]+=((-1)**p)*rop(Gb,q+1)
        D[p*6:(p+1)*6,(p+1)*6:(p+2)*6]+=rop(Ga,p+1)
    return D
D0,D1=cob(0),cob(1)
if D0*D1!=sp.zeros(D0.rows,D1.cols): raise SystemExit("free complex regression")
Sdm,Udm,_=smith_normal_decomp(DomainMatrix.from_Matrix(D1).convert_to(ZZ))
S,U=Sdm.to_Matrix(),Udm.to_Matrix(); rank=sum(S[i,i]!=0 for i in range(min(S.shape)))
K=hermite_normal_form(U[rank:,:].T).T
if K*D1!=sp.zeros(K.rows,D1.cols) or K.rows!=6: raise SystemExit("bad saturated H1 kernel")
piv=list(K.rref()[1]); minor=K[:,piv]; rows=[]
for i in range(D0.rows):
    c=sp.Matrix(1,K.rows,[D0[i,j] for j in piv])*minor.inv()
    if c*K!=D0.row(i) or any(sp.Rational(x).q!=1 for x in c): raise SystemExit("coboundary escaped kernel")
    rows.append([int(x) for x in c])
C=sp.Matrix(rows); SN=smith_normal_form(C,domain=ZZ)
diag=[abs(int(SN[i,i])) for i in range(min(SN.shape)) if SN[i,i]!=0]
tors=[d for d in diag if d!=1]
if K.rows-C.rank()!=0 or tors!=[2]*5: raise SystemExit(f"H1(V4,F) regression: diag={diag}")
# Block diagonal action is an actual G_Q-module split P=T direct-sum F.
# N acts trivially on F and Hom_cont(N,Z^6)=0, hence H1(G_Q,F)=H1(V4,F).
cert={
 "schema":"STAGE33_03_ABSOLUTE_H1_PICU_EXACT_V1",
 "source_locks":{"picu_integral_action_sha256":picu["canonical_sha256"],"finite_transgression_envelope_sha256":finite["canonical_sha256"],"absolute_h3_tate_vanishing_sha256":h3["canonical_sha256"]},
 "PicU_absolute_module_split":"(Z/2)^2 direct-sum Z^6","PicU_absolute_module_split_exact":True,
 "H1_V4_free_quotient":"(Z/2)^5","H1_GQ_free_quotient":"(Z/2)^5",
 "H1_GQ_torsion":"Hom_cont(G_Q,(Z/2)^2)",
 "H1_GQ_PicU":"Hom_cont(G_Q,(Z/2)^2) direct-sum (Z/2)^5",
 "absolute_H1_PicU_all_classes_accounted":True,"remaining_H1_PicU_ambiguity_dimension_f2":0,
 "next_exact_leaf":"L33-03-ASSEMBLE-ALL-PRIMARY-BR0B-FILTRATION",
 "br0b_all_primary_classes_accounted":False,"unit_closed":False,"new_theorem_required":False,"theorem_credit":False,"endpoint_credit":False,"perfect_cuboid_nonexistence_claim":False}
raw=json.dumps(cert,sort_keys=True,separators=(",",":")).encode(); cert["canonical_sha256"]=hashlib.sha256(raw).hexdigest()
(ROOT/"absolute-h1-picu-exact.json").write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n")
print(json.dumps({"success":True,"H1_GQ_PicU":cert["H1_GQ_PicU"],"next_exact_leaf":cert["next_exact_leaf"],"certificate_sha256":cert["canonical_sha256"]},indent=2,sort_keys=True))
