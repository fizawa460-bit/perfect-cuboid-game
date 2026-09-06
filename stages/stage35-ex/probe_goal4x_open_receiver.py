#!/usr/bin/env python3
from __future__ import annotations
import json, runpy
from pathlib import Path
import sympy as sp
from sympy import ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

ROOT=Path(__file__).resolve().parents[2]
GAL=ROOT/'stages/stage33/33-07/certify_actual_galois_at2_actions.py'
gal=runpy.run_path(str(GAL))
known=[[int(x) for x in r] for r in gal['known']]
gram=[[int(x) for x in r] for r in gal['gram']]
cc=[[int(x) for x in r] for r in gal['cc_pic']]
ct=[[int(x) for x in r] for r in gal['ct_pic']]
assert len(known)==140 and len(known[0])==64

def pair(u,v):
    return sum(u[i]*gram[i][j]*v[j] for i in range(64) for j in range(64))

# Goal4U source-lock: known classes 1..8 are the a1=0 = h=0 C1 strict transforms.
strict=list(range(8))
exc=[]
incidence={}
for j in range(92,140):
    hits=[i for i in strict if pair(known[i],known[j])!=0]
    if hits:
        exc.append(j)
        incidence[j+1]=[i+1 for i in hits]
assert len(exc)==24, len(exc)
assert all(len(v)==2 for v in incidence.values()), incidence
assert all(pair(known[i],known[j])==1 for j in exc for i in strict if pair(known[i],known[j])!=0)
bidx=strict+exc
B=[known[i] for i in bidx]
assert len(B)==32

# Smith decomposition of boundary class map Z^32 -> Pic(Sbar)=Z^64.
def dm(a):
    return DomainMatrix([[ZZ(int(x)) for x in row] for row in a], (len(a),len(a[0])), ZZ)
D,S,T=smith_normal_decomp(dm(B))
Dl=D.to_Matrix()
diag=[int(Dl[i,i]) for i in range(min(Dl.rows,Dl.cols)) if Dl[i,i]!=0]
r=len(diag)
assert r==sp.Matrix(B).rank()
primitive=all(abs(x)==1 for x in diag)

res={
 'boundary_known_indices_1based':[i+1 for i in bidx],
 'boundary_strict_indices_1based':[i+1 for i in strict],
 'boundary_exceptional_indices_1based':[i+1 for i in exc],
 'boundary_component_count':32,
 'boundary_class_rank':r,
 'boundary_smith_nonzero':diag,
 'boundary_sublattice_primitive':primitive,
 'pic_U_free_rank':64-r if primitive else None,
 'incidence':incidence,
}

if primitive:
    Tm=sp.Matrix(T.to_Matrix())
    Tinv=Tm.inv()
    assert all(x.q==1 for x in Tinv)
    def induced(A):
        Ap=Tinv*sp.Matrix(A)*Tm
        assert all(x.q==1 for x in Ap)
        # killed coordinates 0..r-1; lower-right block is quotient action.
        Q=Ap[r:,r:]
        return [[int(x) for x in row] for row in Q.tolist()]
    Ac=induced(cc); At=induced(ct); q=len(Ac)
    I=sp.eye(q)
    Acm=sp.Matrix(Ac); Atm=sp.Matrix(At)
    assert Acm*Acm==I and Atm*Atm==I and Acm*Atm==Atm*Acm

    # Z^1(V4,M): x(1+cc)=0, y(1+ct)=0, x(1-ct)=y(1-cc).
    K=sp.zeros(2*q,3*q)
    K[:q,:q]=I+Acm
    K[q:,q:2*q]=I+Atm
    K[:q,2*q:]=I-Atm
    K[q:,2*q:]=-(I-Acm)
    M=K.T
    Dk,Sk,Tk=smith_normal_decomp(dm([[int(x) for x in row] for row in M.tolist()]))
    Dkm=Dk.to_Matrix(); rk=sum(1 for i in range(min(Dkm.rows,Dkm.cols)) if Dkm[i,i]!=0)
    Tkm=sp.Matrix(Tk.to_Matrix()); Tkinv=Tkm.inv()
    assert all(x.q==1 for x in Tkinv)
    k=2*q-rk
    # Coboundaries m -> (m(cc-1),m(ct-1)), expressed in the integral kernel basis.
    C=(Acm-I).row_join(Atm-I)
    coords=[]
    for row in C.tolist():
        z=Tkinv*sp.Matrix(row).T
        assert all(z[i]==0 for i in range(rk))
        coords.append([int(z[i]) for i in range(rk,2*q)])
    if k:
        Dc,Sc,Tc=smith_normal_decomp(dm(coords))
        Dcm=Dc.to_Matrix()
        cdiag=[abs(int(Dcm[i,i])) for i in range(min(Dcm.rows,Dcm.cols)) if Dcm[i,i]!=0]
        crank=len(cdiag)
        free_h1=k-crank
        tors=[d for d in cdiag if d>1]
    else:
        cdiag=[]; free_h1=0; tors=[]; crank=0
    res.update({
      'pic_U_cc_action_rank':q,
      'pic_U_ct_action_rank':q,
      'z1_rank':k,
      'b1_rank':crank,
      'H1_free_rank':free_h1,
      'H1_torsion_invariants':tors,
      'H1_trivial':free_h1==0 and not tors,
    })

print('GOAL4X_PROBE '+json.dumps(res,sort_keys=True))
