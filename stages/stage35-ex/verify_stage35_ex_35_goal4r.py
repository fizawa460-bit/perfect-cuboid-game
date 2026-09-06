#!/usr/bin/env python3
import itertools,json,math
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
ART=ROOT/'stages/stage35-ex/35ex-35/goal4r-visible-numerical-configuration-c2-cohomology.json'
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
a=json.loads(ART.read_text())
assert a['schema']=='STAGE35_EX_35_GOAL4R_VISIBLE_NUMERICAL_CONFIGURATION_C2_COHOMOLOGY_V1'
assert a['configuration_module']['intersection_matrix_rank']==53
assert a['configuration_module']['radical_rank']==3
assert a['configuration_module']['radical_is_primitive_in_P'] is True
assert a['cohomology_computation']['H1_C2_P']==0
assert a['cohomology_computation']['K_mod2_to_fixed_coordinates_rank']==3
assert a['cohomology_computation']['H2_K_to_H2_P_injective'] is True
assert a['interpretation']['full_Picard_H1_computed'] is False
assert a['credit_boundary']['E1_proved'] is False

# Rebuild Goal4Q doubled-cube intersection configuration exactly.
verts=list(itertools.product([0,1],repeat=3)); vi={v:i for i,v in enumerate(verts)}
edges=[]
for v in verts:
    for c in range(3):
        if v[c]==0:
            u=list(v);u[c]=1;u=tuple(u)
            edges.extend([(vi[v],vi[u],c,0),(vi[v],vi[u],c,1)])
M=sp.zeros(32)
for i in range(8):M[i,i]=-4
for j,(u,v,c,k) in enumerate(edges):
    t=8+j;M[t,t]=-2;M[u,t]=M[t,u]=1;M[v,t]=M[t,v]=1
Mall=sp.diag(M,*([-2]*24))
assert M.rank()==29 and Mall.rank()==53

# Integral radical. Start from rational nullspace, primitive-normalize columns.
raw=[]
for v in M.nullspace():
    den=sp.ilcm(*[x.q for x in v]); z=v*den
    g=0
    for x in z:g=math.gcd(g,abs(int(x)))
    raw.append((z/g).applyfunc(int))
Kraw=sp.Matrix.hstack(*raw)
assert Kraw.shape==(32,3)

def gcd_max_minors(B):
    g=0
    for rows in itertools.combinations(range(B.rows),B.cols):
        d=abs(int(B[list(rows),:].det()))
        g=math.gcd(g,d)
        if g==1:return 1
    return g
assert gcd_max_minors(Kraw)==2
# Find the unique nonzero F2 combination divisible by 2 and adjoin its half.
even=[]
for bits in itertools.product([0,1],repeat=3):
    if bits==(0,0,0):continue
    v=sum((bits[j]*Kraw[:,j] for j in range(3)),sp.zeros(32,1))
    if all(int(x)%2==0 for x in v):even.append((bits,v/2))
assert len(even)==1
bits,half=even[0]
# Replace one participating raw column while keeping three independent columns.
candidates=[]
for drop in range(3):
    cols=[Kraw[:,j] for j in range(3) if j!=drop]+[half]
    B=sp.Matrix.hstack(*cols)
    if B.rank()==3 and gcd_max_minors(B)==1:candidates.append(B)
assert candidates
K=candidates[0]
assert gcd_max_minors(K)==1  # primitive/saturated kernel in the free curve module
assert M*K==sp.zeros(32,3)

# Exact C2 action: boundary fixed; doubled edges in the eta/c=2 direction are conjugate pairs;
# epsilon/delta edge exceptionals are Q-rational. Affine: 8 rational fixed + 8 Q(i)-pairs.
G=sp.zeros(56)
for i in range(8):G[i,i]=1
for j,(u,v,c,k) in enumerate(edges):
    src=8+j
    if c==2:
        jj=edges.index((u,v,c,1-k));dst=8+jj
    else:dst=src
    G[dst,src]=1
for i in range(32,40):G[i,i]=1
for t in range(8):
    i=40+2*t;j=i+1;G[j,i]=1;G[i,j]=1
assert G*G==sp.eye(56)
fixed=[i for i in range(56) if G[:,i]==sp.eye(56)[:,i]]
assert len(fixed)==32
# Extend K by the affine zero block and verify pointwise invariance.
K56=K.col_join(sp.zeros(24,3))
assert G*K56==K56

# F2 rank of K -> the 32 fixed-coordinate H2(P) summands.
def rank2(rows):
    A=[[int(x)%2 for x in r] for r in rows];m=len(A);n=len(A[0]);r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None:continue
        A[r],A[p]=A[p],A[r]
        for i in range(m):
            if i!=r and A[i][c]:A[i]=[(u^v) for u,v in zip(A[i],A[r])]
        r+=1
    return r
fixed_rows=[[K56[i,j] for j in range(3)] for i in fixed]
assert rank2(fixed_rows)==3
# Since P=Z^32(trivial) plus 12 Z[C2], H1(C2,P)=0.
# K is trivial rank3, so H2(K)=(F2)^3. Its map to H2(P)=(F2)^32 has rank3,
# hence is injective. The long exact sequence for 0->K->P->L_num->0 gives H1(C2,L_num)=0.
assert a['cohomology_computation']['long_exact_sequence_conclusion']=='H1(C2,L_num)=0'

s=json.loads(STATE.read_text())
assert s['schema'].startswith('STAGE35_EX_PESCH_E1_STATE_V55_')
assert s['current']['unit']=='35EX-35_GOAL4R_VISIBLE_DIVISOR_LATTICE_SATURATION_AND_C2_COHOMOLOGY_PREFLIGHT'
assert s['claims']['visible_numerical_C2_H1_zero_obtained'] is True
assert s['claims']['algebraic_brauer_group_computed'] is False
print('PASS Stage35-EX Goal4R: primitive rank-3 numerical radical and H1(C2,L_num)=0')
