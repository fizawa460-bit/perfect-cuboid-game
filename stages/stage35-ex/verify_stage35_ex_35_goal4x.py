#!/usr/bin/env python3
"""Verify Goal4X: boundary quotient Pic(Ubar)=Z^35 and H1(V4,Pic(Ubar))=(Z/2)^2."""
from __future__ import annotations
import json, runpy, subprocess, sys
from pathlib import Path
import sympy as sp
from sympy import ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

ROOT=Path(__file__).resolve().parents[2]
ART=ROOT/'stages/stage35-ex/35ex-35/goal4x-open-receiver-boundary-picard-galois-h1.json'
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
a=json.loads(ART.read_text())
st=json.loads(STATE.read_text())
assert a['schema']=='STAGE35_EX_35_GOAL4X_OPEN_RECEIVER_BOUNDARY_PICARD_GALOIS_H1_V1'
assert a['base_main_sha']=='87a1c4e6268f76c642964dbcb5d0cd4be4e7c425'
assert a['parent']['source_head_sha']=='87a1c4e6268f76c642964dbcb5d0cd4be4e7c425'
assert a['parent']['snapshot_blob_sha']=='9a071c9d3c5436831550502091b677601dce0650'

def blob(path:str)->str:
    return subprocess.check_output(['git','hash-object',str(ROOT/path)],text=True).strip()
for k in ['goal4x_source_lock','goal4q_boundary_geometry','goal4u_surface_adapter','goal4v_full_picard','stage33_exact_galois_adapter']:
    x=a['source_locks'][k]
    assert blob(x['path'])==x['blob_sha'], k

GAL_DIR=ROOT/'stages/stage33/33-07'
sys.path.insert(0,str(GAL_DIR))
gal=runpy.run_path(str(GAL_DIR/'certify_actual_galois_at2_actions.py'))
known=[[int(x) for x in r] for r in gal['known']]
gram=[[int(x) for x in r] for r in gal['gram']]
cc=[[int(x) for x in r] for r in gal['cc_pic']]
ct=[[int(x) for x in r] for r in gal['ct_pic']]
assert len(known)==140 and all(len(r)==64 for r in known)

def pair(u,v):
    return sum(u[i]*gram[i][j]*v[j] for i in range(64) for j in range(64))
strict=list(range(8))
exc=[]
incidence={}
for j in range(92,140):
    hits=[i for i in strict if pair(known[i],known[j])!=0]
    if hits:
        exc.append(j); incidence[j+1]=[i+1 for i in hits]
expected_exc=[x-1 for x in a['open_receiver']['boundary_exceptional_known_indices_1based']]
assert exc==expected_exc
assert len(exc)==24 and all(len(v)==2 for v in incidence.values())
assert all(pair(known[i],known[j])==1 for j in exc for i in strict if pair(known[i],known[j])!=0)
bidx=strict+exc
assert [i+1 for i in bidx]==a['open_receiver']['boundary_known_indices_1based']
B=[known[i] for i in bidx]

def dm(m):
    return DomainMatrix([[ZZ(int(x)) for x in row] for row in m],(len(m),len(m[0])),ZZ)
D,S,T=smith_normal_decomp(dm(B))
Dm=D.to_Matrix()
diag=[int(Dm[i,i]) for i in range(min(Dm.rows,Dm.cols)) if Dm[i,i]!=0]
assert diag==[1]*29
assert a['open_receiver']['boundary_class_rank_in_Pic_Sbar']==29
assert a['open_receiver']['boundary_image_primitive'] is True
assert a['picard_Ubar']['structure']=='Z^35'

r=29; q=35
Tm=sp.Matrix(T.to_Matrix()); Tinv=Tm.inv()
assert all(x.q==1 for x in Tinv)
def induced(A):
    Ap=Tinv*sp.Matrix(A)*Tm
    assert all(x.q==1 for x in Ap)
    # Boundary image is the killed first-rank summand and must be Galois-stable.
    assert Ap[:r,r:]==sp.zeros(r,q)
    Q=Ap[r:,r:]
    return Q
Ac=induced(cc); At=induced(ct); I=sp.eye(q)
assert Ac*Ac==I and At*At==I and Ac*At==At*Ac
assert a['galois_module']['boundary_image_stable'] is True
assert a['galois_module']['induced_action_dimension']==35

# Exact integral group cohomology for V4=<cc,ct> in row-action convention.
K=sp.zeros(2*q,3*q)
K[:q,:q]=I+Ac
K[q:,q:2*q]=I+At
K[:q,2*q:]=I-At
K[q:,2*q:]=-(I-Ac)
M=K.T
Dk,Sk,Tk=smith_normal_decomp(dm([[int(x) for x in row] for row in M.tolist()]))
Dkm=Dk.to_Matrix(); rk=sum(1 for i in range(min(Dkm.rows,Dkm.cols)) if Dkm[i,i]!=0)
Tkm=sp.Matrix(Tk.to_Matrix()); Tkinv=Tkm.inv()
assert all(x.q==1 for x in Tkinv)
z1rank=2*q-rk
C=(Ac-I).row_join(At-I)
coords=[]
for row in C.tolist():
    z=Tkinv*sp.Matrix(row)
    assert all(z[i]==0 for i in range(rk))
    coords.append([int(z[i]) for i in range(rk,2*q)])
Dc,Sc,Tc=smith_normal_decomp(dm(coords))
Dcm=Dc.to_Matrix()
cdiag=[abs(int(Dcm[i,i])) for i in range(min(Dcm.rows,Dcm.cols)) if Dcm[i,i]!=0]
b1rank=len(cdiag); free=z1rank-b1rank; tors=[d for d in cdiag if d>1]
assert z1rank==14 and b1rank==14 and free==0 and tors==[2,2]
assert a['cohomology']['z1_rank']==14
assert a['cohomology']['b1_rank']==14
assert a['cohomology']['torsion_invariants']==[2,2]
assert a['cohomology']['structure']=='Z/2 x Z/2'
assert a['cohomology']['trivial'] is False

# Deliberate firewall: this leaf computes geometric Picard H1 but not the explicit Brauer lift/residue/evaluation layer.
br=a['brauer_route']
assert br['open_receiver_H1_Pic_nontrivial'] is True
assert br['open_receiver_Br1_mod_Br0_fully_materialized'] is False
assert br['explicit_brauer_class_constructed'] is False
assert br['purity_localization_residue_representatives_computed'] is False
assert br['brauer_manin_obstruction_obtained'] is False
assert st['schema']=='STAGE35_EX_PESCH_E1_STATE_V61_GOAL4X_OPEN_PICARD_H1_Z2_SQUARED_PENDING_BRAUER_LIFT_AND_AUDIT'
assert st['current']['unit']=='35EX-35_GOAL4X_OPEN_RECEIVER_BOUNDARY_PICARD_GALOIS_AND_ALGEBRAIC_BRAUER_PREFLIGHT'
assert st['claims']['open_receiver_Picard_rank']==35
assert st['claims']['open_receiver_H1_Pic_structure']=='Z/2 x Z/2'
assert st['claims']['open_receiver_algebraic_brauer_group_computed'] is False
assert st['claims']['brauer_manin_obstruction_obtained'] is False
assert st['claims']['E1_proved'] is False
print('PASS Stage35-EX Goal4X: boundary rank29 primitive, Pic(Ubar)=Z^35, H1(V4,Pic(Ubar))=(Z/2)^2; Brauer lift remains pending')
