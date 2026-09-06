#!/usr/bin/env python3
import itertools,json,math
from pathlib import Path
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

ROOT=Path(__file__).resolve().parents[2]
ART=ROOT/'stages/stage35-ex/35ex-35/goal4s-picard-overlattice-discriminant-2primary.json'
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
a=json.loads(ART.read_text())
assert a['schema']=='STAGE35_EX_35_GOAL4S_PICARD_OVERLATTICE_DISCRIMINANT_2PRIMARY_V1'
assert a['visible_numerical_lattice']['rank']==53
assert a['smith_normal_form']['discriminant_absolute']=='2^45'
assert a['same_rank_integral_overlattice_gate']['index_must_be_power_of_two'] is True
assert a['same_rank_integral_overlattice_gate']['unimodular_same_rank_overlattice_exists'] is False
assert a['credit_boundary']['E1_proved'] is False

verts=list(itertools.product([0,1],repeat=3));vi={v:i for i,v in enumerate(verts)}
edges=[]
for v in verts:
    for c in range(3):
        if v[c]==0:
            u=list(v);u[c]=1;u=tuple(u)
            edges.extend([(vi[v],vi[u],c,0),(vi[v],vi[u],c,1)])
M=sp.zeros(32)
for i in range(8):M[i,i]=-4
for j,(u,v,_,_) in enumerate(edges):
    t=8+j;M[t,t]=-2;M[u,t]=M[t,u]=1;M[v,t]=M[t,v]=1
Mall=sp.diag(M,*([-2]*24))
assert Mall.rank()==53

# Exact inertia: M32 spectrum plus 24 extra -2 eigenvalues.
ev=M.eigenvals()
assert ev[sp.Integer(0)]==3
pos=sum(mult for lam,mult in ev.items() if lam.is_positive)
neg=sum(mult for lam,mult in ev.items() if lam.is_negative)+24
zero=ev[sp.Integer(0)]
assert (pos,neg,zero)==(1,52,3)
assert a['visible_numerical_lattice']['signature']==[1,52]

D=smith_normal_form(Mall,domain=ZZ)
diag=[abs(int(D[i,i])) for i in range(56)]
non=[x for x in diag if x]
from collections import Counter
cnt=Counter(non)
assert cnt==Counter({1:14,2:34,4:4,8:1})
assert len(non)==53 and diag.count(0)==3
assert math.prod(non)==2**45
assert a['smith_normal_form']['nonzero_invariants']=={'1':14,'2':34,'4':4,'8':1}
assert a['smith_normal_form']['discriminant_group']=='(Z/2)^34 x (Z/4)^4 x Z/8'
assert a['smith_normal_form']['minimal_generator_count']==39

# For any same-rank integral overlattice L', disc scales by index squared.
# Since disc(L_num)=2^45, every possible finite index is 2-primary and 2k<=45.
possible_k=list(range(23))
assert possible_k[0]==0 and possible_k[-1]==22
assert all(45-2*k>=1 and (45-2*k)%2==1 for k in possible_k)
assert a['same_rank_integral_overlattice_gate']['index_exponent_bound']=='0<=k<=22'
assert a['same_rank_integral_overlattice_gate']['odd_index_overlattice_exists'] is False

s=json.loads(STATE.read_text())
assert s['schema'].startswith('STAGE35_EX_PESCH_E1_STATE_V56_')
assert s['current']['unit']=='35EX-35_GOAL4S_PICARD_OVERLATTICE_DISCRIMINANT_AND_2PRIMARY_SATURATION_PREFLIGHT'
assert s['claims']['same_rank_odd_primary_saturation_eliminated'] is True
assert s['claims']['algebraic_brauer_group_computed'] is False
print('PASS Stage35-EX Goal4S: A(L_num)=(Z/2)^34 x (Z/4)^4 x Z/8, pure 2-primary')
