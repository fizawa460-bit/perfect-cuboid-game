#!/usr/bin/env python3
"""Independent hostile replay of Stage33-05 zero K3 Br[2] Q-survival.

Uses two ct-fixed Picard test curves, CsK[2] and CsK[5]. Their mod-2 pairing
functionals on the two restricted HS d2 images give an invertible 2x2 matrix:
    J2 -> (1,1)
    q1 -> (1,0)
so every nonzero element of <J2,q1> has nonzero restricted d2.
"""
from __future__ import annotations
import hashlib, json
from pathlib import Path
import sympy as sp

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
CAND = HERE / "stage33-05-br2-zero-q-survival-after-j2-nogo.json"
J2 = HERE / "j2-r5e-pic2-r5f-ct-hs-d2-nonzero.json"
J2_AUDIT = HERE / "j2-r5f-hs-d2-nonzero-hostile-replay.json"
SEM = S33 / "33-12" / "j2-semantic-kc-picard-basis.json"
Q1_NS = HERE / "q1_ns_lift_parity.py"
Q1_D2 = HERE / "q1_hs_d2_bockstein.py"
CONTRACT = S33 / "33-00" / "unit-closure-contract.md"
OUT = HERE / "stage33-05-br2-zero-q-survival-hostile-replay.json"

EXPECTED_CANON = {
    CAND: "a48386c523e8c98b1d2b22a7dc3d789e4cea1bfa4557e658fb150e3c6b85a585",
    J2: "8e384501db1cb3aa3f73358b0c3612a85e4012c5041fda60d3be7aeddc7c4c55",
    J2_AUDIT: "6535f3190daab8c20ba5ddb3409675f20ac35dc4ee319e3be7af056baa4ce20d",
    SEM: "c17439c877de3d1cdebd716f4ba2571fb67ec9f07e30d944eafc39ae534380c0",
}
EXPECTED_BLOB = {
    Q1_NS: "6526a8cbc50e5e683e5385fd38e208703b724ff3",
    Q1_D2: "9b38833b58c548a539648cc803ee1f451ece5434",
    CONTRACT: "b7036a9901304340361f68a9fc845770fb51cb4b",
}

def csha(obj):
    body=dict(obj); body.pop("canonical_sha256",None)
    return hashlib.sha256(json.dumps(body,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def blobsha(path):
    b=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()

def locked(path, sha):
    o=json.loads(path.read_text())
    assert o["canonical_sha256"]==sha==csha(o)
    return o

for p,s in EXPECTED_BLOB.items():
    assert blobsha(p)==s, (p,blobsha(p))
cand=locked(CAND,EXPECTED_CANON[CAND])
j2=locked(J2,EXPECTED_CANON[J2])
j2audit=locked(J2_AUDIT,EXPECTED_CANON[J2_AUDIT])
sem=locked(SEM,EXPECTED_CANON[SEM])
assert cand["restricted_d2_rank_f2"]==2
assert j2audit["hostile_checks"]["restricted_class_nonzero"] is True
contract=CONTRACT.read_text()
assert "OR EXACT_ZERO_SURVIVAL_CERTIFICATE=true" in contract
assert "Zero surviving classes is a valid exact closure" in contract
q1src=Q1_D2.read_text()
assert '"HS_d2_q1_global_nonzero": True' in q1src
assert '"q1_Q_descent": False' in q1src

# Exact marked Gram.
g17=sem["gram17"]; inc=sem["incidence17x12"]; tri=sem["semantic_exceptional_indices_0based"]
G=[r[:] + [inc[i][c] for c in tri] for i,r in enumerate(g17)]
for a,c in enumerate(tri):
    r=[inc[i][c] for i in range(17)] + [0,0,0]
    r[17+a]=-2; G.append(r)
Z=j2["r5f_integral_lift_and_restricted_d2"]["restricted_normalized_2cocycle"]["beta(ct,ct)=Z=(B+ct(B))/2"]
def pair(x,k): return sum(x[j]*G[j][k] for j in range(20))
j2_sig=(pair(Z,0)&1,pair(Z,2)&1)
assert j2_sig==(1,1)

# ct fixes both tests.
M=j2["semantic_ct_action"]["matrix"]
assert M[0]==[1 if k==0 else 0 for k in range(20)]
assert M[2]==[1 if k==2 else 0 for k in range(20)]

# Recompute q1 D=Cb+E_P0 pairings with CsK[2], CsK[5].
A1,A2,A3,B1,B2,B3=sp.symbols("A1 A2 A3 B1 B2 B3")
V=(A1,A2,A3,B1,B2,B3); I=sp.I
K=[A1**2+A2**2-B3**2,A2**2+A3**2-B1**2,A1**2+A3**2-B2**2]
Cb=[I*A1+B1,I*A2+B2,I*A3+B3]
T2=[A1,A2+B3,A3-B2]
T5=[A2,A3+B1,A1+B3]
P0=[0,1,0,-1,0,1]
def mat(fs): return sp.Matrix([[sp.expand(f).coeff(v) for v in V] for f in fs])
m2=mat(Cb+T2)
assert m2.rank()==5 and len(m2.nullspace())==1
P=m2.nullspace()[0]; sub=dict(zip(V,P))
assert all(sp.simplify(f.subs(sub))==0 for f in K+Cb+T2)
JK=sp.Matrix([[sp.diff(f,v).subs(sub) for v in V] for f in K])
JC=sp.Matrix([[sp.diff(f,v).subs(sub) for v in V] for f in Cb])
JT=sp.Matrix([[sp.diff(f,v).subs(sub) for v in V] for f in T2])
assert JK.rank()==3 and JK.col_join(JC).rank()==4 and JK.col_join(JT).rank()==4
assert JK.col_join(JC).col_join(JT).rank()==5
sub0=dict(zip(V,P0))
assert any(sp.simplify(f.subs(sub0))!=0 for f in T2)
assert any(sp.simplify(f.subs(sub0))!=0 for f in T5)
assert mat(Cb+T5).rank()==6
q1_sig=(1,0)

# Pairing signature matrix rows are tests [CsK2,CsK5], columns [J2,q1].
sig=[[j2_sig[0],q1_sig[0]],[j2_sig[1],q1_sig[1]]]
det=(sig[0][0]*sig[1][1]-sig[0][1]*sig[1][0])&1
assert sig==[[1,1],[1,0]] and det==1
images={}
for a,b in ((1,0),(0,1),(1,1)):
    images[f"{a}*J2+{b}*q1"]=((a*j2_sig[0]+b*q1_sig[0])&1,
                              (a*j2_sig[1]+b*q1_sig[1])&1)
assert all(v!=(0,0) for v in images.values())

out=json.loads(OUT.read_text())
assert out["hostile_checks"]["all_three_nonzero_domain_elements_have_nonzero_restricted_d2"] is True
assert out["hostile_checks"]["restricted_kernel_dimension_f2"]==0
assert out["hostile_checks"]["global_kernel_dimension_f2"]==0
assert out["unit_closure_adapter"]["Q_RELEVANT_SURVIVING_DIM"]==0
assert out["unit_closure_adapter"]["HOSTILE_AUDIT"]=="PASS"
assert out["canonical_sha256"]==csha(out)
print(json.dumps({"status":out["status"],"canonical_sha256":out["canonical_sha256"],
                  "pairing_signature_matrix":sig,"det_mod2":det,
                  "nonzero_images":images},sort_keys=True))
