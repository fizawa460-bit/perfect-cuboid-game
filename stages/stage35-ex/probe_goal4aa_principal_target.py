#!/usr/bin/env python3
from __future__ import annotations
import json,runpy
from fractions import Fraction
from pathlib import Path
from collections import defaultdict
import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
SNAP61=ROOT/'stages/stage35-ex/snapshots/MAIN-STATE-V61-0a8af929e004.json'
GOAL4Z=ROOT/'stages/stage35-ex/35ex-35/goal4z-one-explicit-biquaternion-second-qi-principalization.json'
PERMS=ROOT/'stages/stage33/33-07/galois-known-class-permutations.json'

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
    for h in range(4):d[(g,h)]=liftD(lp[g]*Pact[h]+lp[h]-lp[g^h])
target=[]
for g,h,k in triples:
    kval=d[(g,h)]*Dact[k]+d[(g^h,k)]-d[(g,h^k)]-d[(h,k)]
    knew=kval*Sinv; assert knew[:,:R]==sp.zeros(1,R)
    target.extend(int(v) for v in knew[:,R:])
ecoord,_=solve_integral(A2,sp.Matrix(target)); pindex={p:i for i,p in enumerate(pairs)}
e11=sp.Matrix([[int(ecoord[pindex[(1,1)]*3+a,0]) for a in range(3)]])
enew=sp.zeros(1,NBD)
for a in range(3):enew[0,R+a]=e11[0,a]
E=d[(1,1)]-enew*S
Bmat=sp.Matrix(core['ns']['B']); delta=lp[1]*Pact[1]+lp[1]
assert E*Bmat==delta
bidx=[int(x)+1 for x in core['ns']['bidx']]

K=sp.Matrix(core['kernel_basis_old'])
assert K*Bmat==sp.zeros(3,64)
unit_adjust=[4,218,-12]
Es=E+sp.Matrix([unit_adjust])*K
assert Es*Bmat==delta
assert max(abs(int(x)) for x in Es)<=36
assert all((int(Es[0,j])-int(E[0,j]))%2==0 for j in range(NBD))
E_sparse={str(bidx[j]):int(Es[0,j]) for j in range(NBD) if Es[0,j]}

a=json.loads(GOAL4Z.read_text()); perm=json.loads(PERMS.read_text())['cc_permutation_1based']
formal=[0]*140
for k,v in a['class_B']['picard_lift_cc_indlist_coefficients'].items():
    i=int(k); c=int(v); formal[i-1]+=c; formal[int(perm[i-1])-1]+=c
for k,v in E_sparse.items():formal[int(k)-1]-=int(v)
known=[[int(x) for x in r] for r in core['ns']['known']]
cls=[sum(formal[j]*known[j][i] for j in range(140)) for i in range(64)]
assert cls==[0]*64
V_sparse={str(i+1):formal[i] for i in range(140) if formal[i]}

gram=core['ns']['gram']
def pair(i,j):
    return sum(known[i][u]*gram[u][v]*known[j][v] for u in range(64) for v in range(64))
def total_transform(curves):
    vec=[0]*140
    for i in curves:vec[i-1]+=1
    for j in range(93,141):
        if any(pair(i-1,j-1)!=0 for i in curves):vec[j-1]+=1
    return vec

Z=(Fraction(0),)*4; ONE=(Fraction(1),Fraction(0),Fraction(0),Fraction(0))
II=(Fraction(0),Fraction(1),Fraction(0),Fraction(0)); SS=(Fraction(0),Fraction(0),Fraction(1),Fraction(0))
def add(x,y):return tuple(x[i]+y[i] for i in range(4))
def neg(x):return tuple(-z for z in x)
def mul(x,y):
    out=[Fraction(0)]*4; mons=[(0,0),(1,0),(0,1),(1,1)]
    for r,(ai,as_) in enumerate(mons):
      for t,(bi,bs) in enumerate(mons):
        ci=ai+bi; cs=as_+bs; c=x[r]*y[t]
        if ci>=2:c=-c; ci-=2
        if cs>=2:c*=2; cs-=2
        out[mons.index((ci,cs))]+=c
    return tuple(out)
IS=mul(II,SS)
def inv_pivot(x):
    candidates=[ONE,neg(ONE),II,neg(II),SS,neg(SS),IS,neg(IS)]
    halfS=tuple(z/Fraction(2) for z in SS); minusHalfIS=tuple(-z/Fraction(2) for z in IS)
    inverses=[ONE,neg(ONE),neg(II),II,halfS,neg(halfS),minusHalfIS,neg(minusHalfIS)]
    for q,r in zip(candidates,inverses):
        if x==q:return r
    raise AssertionError(('unexpected pivot',x))
def coeff(unit,sign=1):
    q={'1':ONE,'i':II,'s':SS}[unit]
    return q if sign==1 else neg(q)
def form(*terms):
    v=[Z]*7
    for j,c in terms:v[j]=add(v[j],c)
    p=next(x for x in v if x!=Z); pinv=inv_pivot(p)
    n=[mul(x,pinv) for x in v]
    return tuple(tuple((z.numerator,z.denominator) for z in x) for x in n)
def f1(j,u='1',sgn=1):return form((j,coeff(u,sgn)))
def f2(j,u,j2,u2='1',sgn2=1):return form((j,coeff(u)),(j2,coeff(u2,sgn2)))

curve_forms={}; degrees={}
def addcurve(idx,deg,forms):curve_forms[idx]=forms;degrees[idx]=deg
idx=1
for base,specs in [(0,[(1,5),(2,4),(3,6)]),(1,[(2,3),(0,5),(4,6)]),(2,[(0,4),(1,3),(5,6)])]:
  for e1 in [1,-1]:
   for e2 in [1,-1]:
    for e3 in [1,-1]:
     es=[e1,e2,e3]; addcurve(idx,2,[f1(base)]+[f2(x,'1',y,'1',es[t]) for t,(x,y) in enumerate(specs)]);idx+=1
for e3 in [1,-1]:
 for e2 in [1,-1]:
  for e1 in [1,-1]:
   addcurve(idx,2,[f1(6),f2(0,'i',3,'1',e1),f2(1,'i',4,'1',e2),f2(2,'i',5,'1',e3)]);idx+=1
assert idx==33
for b,(x,y,c0) in [(3,(1,2,0)),(4,(2,0,1)),(5,(0,1,2))]:
 for e1 in [1,-1]:
  for e2 in [1,-1]:
   addcurve(idx,4,[f1(b),f2(x,'i',y,'1',e1),f2(c0,'1',6,'1',e2)]);idx+=1
assert idx==45
for x,y,b3,b1,b2 in [(0,1,5,3,4),(1,2,3,4,5),(2,0,4,5,3)]:
 for e1 in [1,-1]:
  for e2 in [1,-1]:
   for e3 in [1,-1]:
    addcurve(idx,4,[f2(x,'1',y,'1',e1),f2(x,'s',b3,'1',e2),f2(b1,'1',b2,'1',e3)]);idx+=1
for x,b2,b3,b1 in [(0,4,5,3),(1,5,3,4),(2,3,4,5)]:
 for e3 in [1,-1]:
  for e2 in [1,-1]:
   for e1 in [1,-1]:
    addcurve(idx,4,[f2(x,'i',6,'1',e1),f2(b2,'i',b3,'1',e2),form((x,IS),(b1,coeff('1',e3)))]);idx+=1
assert idx==93

groups=defaultdict(set)
for ci,fs in curve_forms.items():
    for L in fs:groups[L].add(ci)
complete={L:sorted(cs) for L,cs in groups.items() if sum(degrees[i] for i in cs)==16}
H={L:total_transform(cs) for L,cs in complete.items()}
hclasses=[]
for L,vec in H.items():hclasses.append([sum(vec[j]*known[j][i] for j in range(140)) for i in range(64)])
assert H and all(x==hclasses[0] for x in hclasses)

names=list(H); M=sp.Matrix(140,len(names),lambda i,j:H[names[j]][i]); v=sp.Matrix(formal)
sol=sp.linsolve((M,v)); in_span=sol!=sp.EmptySet
solution=None; solution_rational=None
if in_span:
    tup=next(iter(sol)); subs={s:0 for x in tup for s in x.free_symbols}; cand=[sp.simplify(x.subs(subs)) for x in tup]
    solution_rational={str(j):str(x) for j,x in enumerate(cand) if x}
    if all(x.q==1 for x in cand):
        ivec=[int(x) for x in cand]; assert M*sp.Matrix(ivec)==v
        solution={str(j):ivec[j] for j in range(len(ivec)) if ivec[j]}
def enc_form(L):return [[[aa,bb] for aa,bb in slot] for slot in L]
solution_forms=None
if solution is not None:
    solution_forms=[{'exponent':e,'coefficients_QiS2':enc_form(names[int(j)]),'curve_components_1based':complete[names[int(j)]]} for j,e in solution.items()]

out={
 'success':True,
 'goal4aa_marker':'SECOND_CLASS_QI_CYCLIC_PRINCIPAL_DIVISOR_EXACT_TARGET',
 'boundary_component_order_known_indices_1based':bidx,
 'raw_unit_corrected_boundary_max_abs':max(abs(int(x)) for x in E),
 'unit_kernel_adjustment_coefficients':unit_adjust,
 'simplified_boundary_max_abs':max(abs(int(x)) for x in Es),
 'simplified_boundary_divisor_E_B':E_sparse,
 'formal_principal_divisor_D_plus_ccD_minus_E':V_sparse,
 'formal_target_support_count':len(V_sparse),
 'formal_target_picard_class_zero':True,
 'retained_curve_linear_form_count':len(groups),
 'degree16_complete_hyperplane_library_size':len(H),
 'complete_hyperplane_span_contains_target':in_span,
 'complete_hyperplane_rational_solution_at_zero_parameters':solution_rational,
 'complete_hyperplane_integer_solution':solution,
 'complete_hyperplane_integer_solution_forms':solution_forms,
 'stage33_boundary_function_packages_are_residue_field_functions_not_assumed_global_principal_functions':True,
}
print('GOAL4AA_TARGET '+json.dumps(out,sort_keys=True))
