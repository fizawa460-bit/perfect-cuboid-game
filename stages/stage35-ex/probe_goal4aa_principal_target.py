#!/usr/bin/env python3
from __future__ import annotations
import json,runpy
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
SNAP61=ROOT/'stages/stage35-ex/snapshots/MAIN-STATE-V61-0a8af929e004.json'
GOAL4Z=ROOT/'stages/stage35-ex/35ex-35/goal4z-one-explicit-biquaternion-second-qi-principalization.json'
PERMS=ROOT/'stages/stage33/33-07/galois-known-class-permutations.json'

# Recreate the exact Goal4Y core against its V61 parent without expanding any retained opaque payload.
snaptext=SNAP61.read_text(); orig=Path.read_text; sr=STATE.resolve()
def patched(self:Path,*a,**k):
    if self.resolve()==sr:return snaptext
    return orig(self,*a,**k)
Path.read_text=patched
try:
    core=runpy.run_path(str(ROOT/'stages/stage35-ex/stage35_ex_35_goal4y_core.py'))
finally:
    Path.read_text=orig

f,_=core['h1_generator'](13)
Pact=core['Pact']; Dact=core['Dact']; liftP=core['liftP']; liftD=core['liftD']
S=core['S']; Sinv=core['Sinv']; A2=core['A2']; solve_integral=core['solve_integral']
R=core['R']; NBD=core['NBD']; triples=core['triples']; pairs=core['pairs']
lp={g:liftP(f[g]) for g in range(4)}
d={}
for g in range(4):
    for h in range(4):
        d[(g,h)]=liftD(lp[g]*Pact[h]+lp[h]-lp[g^h])
target=[]
for g,h,k in triples:
    kval=d[(g,h)]*Dact[k]+d[(g^h,k)]-d[(g,h^k)]-d[(h,k)]
    knew=kval*Sinv
    assert knew[:,:R]==sp.zeros(1,R)
    target.extend(int(v) for v in knew[:,R:])
ecoord,_=solve_integral(A2,sp.Matrix(target))
pindex={p:i for i,p in enumerate(pairs)}
e11=sp.Matrix([[int(ecoord[pindex[(1,1)]*3+a,0]) for a in range(3)]])
enew=sp.zeros(1,NBD)
for a in range(3):enew[0,R+a]=e11[0,a]
eold=enew*S
E=d[(1,1)]-eold
Bmat=sp.Matrix(core['ns']['B'])
delta=lp[1]*Pact[1]+lp[1]
assert E*Bmat==delta
bidx=[int(x)+1 for x in core['ns']['bidx']]
E_sparse={str(bidx[j]):int(E[0,j]) for j in range(NBD) if E[0,j]}

# Materialize the formal divisor V = D_B + cc(D_B) - E_B on the 140 retained divisors.
a=json.loads(GOAL4Z.read_text())
perm=json.loads(PERMS.read_text())['cc_permutation_1based']
formal=[0]*140
for k,v in a['class_B']['picard_lift_cc_indlist_coefficients'].items():
    i=int(k); c=int(v); formal[i-1]+=c; formal[int(perm[i-1])-1]+=c
for k,v in E_sparse.items():formal[int(k)-1]-=int(v)
known=[[int(x) for x in r] for r in core['ns']['known']]
cls=[sum(formal[j]*known[j][i] for j in range(140)) for i in range(64)]
assert cls==[0]*64
V_sparse={str(i+1):formal[i] for i in range(140) if formal[i]}

# A small exact library of complete hyperplane sections whose irreducible strict components
# are entirely among Stoll's retained C1/C2/C3 curves.  Add each singular exceptional once.
gram=core['ns']['gram']
def pair(i,j):
    return sum(known[i][u]*gram[u][v]*known[j][v] for u in range(64) for v in range(64))
def total_transform(curves):
    vec=[0]*140
    for i in curves:vec[i-1]+=1
    for j in range(93,141):
        if any(pair(i-1,j-1)!=0 for i in curves):vec[j-1]+=1
    return vec
hyp={
 'a1':list(range(1,9)),'a2':list(range(9,17)),'a3':list(range(17,25)),'c':list(range(25,33)),
 'b1':list(range(33,37)),'b2':list(range(37,41)),'b3':list(range(41,45)),
 'a1+a2':list(range(45,49)),'a1-a2':list(range(49,53)),
 'a2+a3':list(range(53,57)),'a2-a3':list(range(57,61)),
 'a3+a1':list(range(61,65)),'a3-a1':list(range(65,69)),
 'i*a1+c':[69,71,73,75],'i*a1-c':[70,72,74,76],
 'i*a2+c':[77,79,81,83],'i*a2-c':[78,80,82,84],
 'i*a3+c':[85,87,89,91],'i*a3-c':[86,88,90,92],
}
H={name:total_transform(curves) for name,curves in hyp.items()}
# Every listed total transform must have the same Picard class (the hyperplane class).
hclasses=[]
for name,vec in H.items():
    hclasses.append([sum(vec[j]*known[j][i] for j in range(140)) for i in range(64)])
assert all(x==hclasses[0] for x in hclasses)
M=sp.Matrix(140,len(H),lambda i,j:H[list(H)[j]][i])
v=sp.Matrix(formal)
sol=sp.linsolve((M,v))
in_basic_span=sol!=sp.EmptySet
solution=None
if in_basic_span:
    tup=next(iter(sol))
    if not any(x.free_symbols for x in tup):solution={list(H)[j]:str(tup[j]) for j in range(len(H)) if tup[j]}

out={
 'success':True,
 'goal4aa_marker':'SECOND_CLASS_QI_CYCLIC_PRINCIPAL_DIVISOR_EXACT_TARGET',
 'boundary_component_order_known_indices_1based':bidx,
 'unit_corrected_boundary_divisor_E_B':E_sparse,
 'formal_principal_divisor_D_plus_ccD_minus_E':V_sparse,
 'formal_target_support_count':len(V_sparse),
 'formal_target_picard_class_zero':True,
 'basic_complete_hyperplane_library_size':len(H),
 'basic_complete_hyperplane_span_contains_target':in_basic_span,
 'basic_complete_hyperplane_exact_solution':solution,
 'stage33_boundary_function_packages_are_residue_field_functions_not_assumed_global_principal_functions':True,
}
print('GOAL4AA_TARGET '+json.dumps(out,sort_keys=True))
