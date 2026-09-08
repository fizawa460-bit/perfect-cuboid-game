#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ART = HERE / "ex3-04c-bolza-h4-plane-coordinate-closure.json"

def add(x,y): return (x[0]+y[0], x[1]+y[1])
def mul(x,y): return (x[0]*y[0]-2*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def conj(x): return (x[0], -x[1])

M = [[(2,0),(1,1)],[(1,-1),(2,0)]]

def herm(v,w):
    out=(0,0)
    for i in range(2):
        for j in range(2):
            out=add(out,mul(conj(v[i]),mul(M[i][j],w[j])))
    return out

def act_mod2(P, x):
    z=[(x[0]&1,x[1]&1),(x[2]&1,x[3]&1)]
    out=[]
    for i in range(2):
        zz=(0,0)
        for j in range(2):
            zz=add(zz,mul(P[j][i],z[j]))
        out.extend([zz[0]&1,zz[1]&1])
    return tuple(out)

def action_matrix(P):
    cols=[]
    for k in range(4):
        e=[0,0,0,0]
        e[k]=1
        cols.append(act_mod2(P,e))
    return tuple(tuple(cols[j][i] for j in range(4)) for i in range(4))

def mv(A,v):
    return tuple(sum(A[i][j]*v[j] for j in range(4)) & 1 for i in range(4))

def xor(u,v): return tuple(a^b for a,b in zip(u,v))
def span2(u,v): return frozenset(((0,0,0,0),u,v,xor(u,v)))
def compose(p,q,labels): return {x:p[q[x]] for x in labels}

with ART.open("r", encoding="utf-8") as f:
    art=json.load(f)

expected=art["canonical_sha256_without_this_field"]
tmp=dict(art)
tmp.pop("canonical_sha256_without_this_field")
got=hashlib.sha256(json.dumps(tmp,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
assert got == expected

# lambda_min(M)=2-sqrt(3).  If h(v,v)=2 then
# |z1|^2+|z2|^2 <= 2/(2-sqrt(3))=4+2sqrt(3)<8.
# Thus each a^2+2b^2<8, so |a|<=2 and |b|<=1.
vals=[(a,b) for a in range(-2,3) for b in range(-1,2)]
norm2=[(z1,z2) for z1 in vals for z2 in vals if herm((z1,z2),(z1,z2))==(2,0)]
assert len(norm2)==24

auts=[]
for v1 in norm2:
    for v2 in norm2:
        if herm(v1,v2)==(1,1) and herm(v2,v1)==(1,-1):
            auts.append((v1,v2))
assert len(auts)==48

actions={action_matrix(P) for P in auts}
assert len(actions)==24

vecs=[tuple((n>>i)&1 for i in range(4)) for n in range(16)]
nz=[v for v in vecs if any(v)]
subs=set()
for i,u in enumerate(nz):
    for v in nz[i+1:]:
        S=span2(u,v)
        if len(S)==4:
            subs.add(S)
assert len(subs)==35

invariant=[]
for S in subs:
    if all(frozenset(mv(A,v) for v in S)==S for A in actions):
        invariant.append(S)
assert len(invariant)==1
U0=frozenset(((0,0,0,0),(0,1,0,0),(0,0,0,1),(0,1,0,1)))
assert invariant[0]==U0

# Product elliptic alternating form twisted by M.
def multmat(z):
    a,b=z
    return ((a,-2*b),(b,a))
M4=[[0]*4 for _ in range(4)]
for bi in range(2):
    for bj in range(2):
        B=multmat(M[bi][bj])
        for i in range(2):
            for j in range(2):
                M4[2*bi+i][2*bj+j]=B[i][j]
J0=((0,1,0,0),(-1,0,0,0),(0,0,0,1),(0,0,-1,0))
K=[[sum(J0[i][k]*M4[k][j] for k in range(4)) & 1 for j in range(4)] for i in range(4)]
def pairing(u,v):
    return sum(u[i]*K[i][j]*v[j] for i in range(4) for j in range(4)) & 1
assert all(pairing(u,v)==0 for u in U0 for v in U0)

# Möbius generators on {0,inf,+/-1,+/-i}.
labels=("0","inf","1","-1","i","-i")
r={"0":"0","inf":"inf","1":"i","i":"-1","-1":"-i","-i":"1"}
t={"0":"-1","inf":"1","1":"inf","-1":"0","i":"-i","-i":"i"}
identity={x:x for x in labels}
group={tuple(identity[x] for x in labels):identity}
front=[identity]
for cur in front:
    for gen in (r,t):
        nxt=compose(gen,cur,labels)
        key=tuple(nxt[x] for x in labels)
        if key not in group:
            group[key]=nxt
            front.append(nxt)
assert len(group)==24
matching=frozenset((frozenset(("0","inf")),frozenset(("1","-1")),frozenset(("i","-i"))))
for p in group.values():
    image=frozenset(frozenset(p[x] for x in pair) for pair in matching)
    assert image==matching

assert art["diagonal_H4_label_sharpening"]["basis_change_A"]=="I"
assert art["diagonal_H4_label_sharpening"]["exact_mod2_action"]=="T|U = I"
assert art["E2_coordinate_filter"]["T_restrict_U0_identity_iff"] == [
    "a11 == 1 mod 2",
    "a22 == 1 mod 2",
    "a12 == 0 mod 2",
    "a21 == 0 mod 2",
]

# Nonpruning witness T=I satisfies T^dagger T=I <= 8505 I.
assert 1 <= 8505
assert art["nonpruning_witness"]["T"]=="I_2"
assert art["diagnostic_verdict"]["EX3_04_exclusion_obtained"] is False
assert art["firewalls"]["O210_excluded"] is False
assert art["firewalls"]["stage32_main_credit"] is False
assert art["firewalls"]["claim_dag_sync_triggered_by_this_scratch"] is False
assert art["firewalls"]["merge_authorized"] is False

print(json.dumps({
    "status":"PASS",
    "norm2_vector_count":len(norm2),
    "M_unitary_matrix_count":len(auts),
    "distinct_mod2_action_count":len(actions),
    "rank2_subspace_count":len(subs),
    "invariant_rank2_plane_count":len(invariant),
    "unique_plane":"s*F2^2",
    "branch_permutation_group_order":len(group),
    "T_on_U":"identity",
    "EX3_04_exclusion_obtained":False
}, sort_keys=True))
