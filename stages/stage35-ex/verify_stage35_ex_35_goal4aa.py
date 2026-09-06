#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,runpy
from fractions import Fraction
from pathlib import Path
from collections import defaultdict
import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
ART=ROOT/'stages/stage35-ex/35ex-35/goal4aa-second-class-qi-cyclic-linear-hyperplane-blocker.json'
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
SNAP61=ROOT/'stages/stage35-ex/snapshots/MAIN-STATE-V61-0a8af929e004.json'
GOAL4Z=ROOT/'stages/stage35-ex/35ex-35/goal4z-one-explicit-biquaternion-second-qi-principalization.json'
PERMS=ROOT/'stages/stage33/33-07/galois-known-class-permutations.json'

def blob(path:str)->str:
    b=(ROOT/path).read_bytes()
    return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

a=json.loads(ART.read_text()); state=json.loads(STATE.read_text())
assert a['schema']=='STAGE35_EX_35_GOAL4AA_QI_CYCLIC_LINEAR_HYPERPLANE_BLOCKER_V1'
assert blob(a['parent']['snapshot_path'])==a['parent']['snapshot_blob_sha']
for v in a['source_locks'].values():
    if 'path' in v and 'blob_sha' in v: assert blob(v['path'])==v['blob_sha']
perm_obj=json.loads(PERMS.read_text())
assert perm_obj['canonical_sha256']==a['source_locks']['stage33_galois_permutations']['canonical_sha256']
assert a['source_locks']['upstream_stoll']['commit']=='51233ed5ef2bf228fac9416c66db9adc0ebcaadd'
assert a['source_locks']['upstream_stoll']['git_blob_sha1']=='0422b69847f2afb97cb7b3ed02ebef91279f61b1'

# Recreate Goal4Y exact lattice core against its immutable V61 parent.
snaptext=SNAP61.read_text(); orig=Path.read_text; sr=STATE.resolve()
def patched(self:Path,*args,**kwargs):
    if self.resolve()==sr:return snaptext
    return orig(self,*args,**kwargs)
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
    for h in range(4): d[(g,h)]=liftD(lp[g]*Pact[h]+lp[h]-lp[g^h])
target=[]
for g,h,k in triples:
    kval=d[(g,h)]*Dact[k]+d[(g^h,k)]-d[(g,h^k)]-d[(h,k)]
    knew=kval*Sinv; assert knew[:,:R]==sp.zeros(1,R)
    target.extend(int(v) for v in knew[:,R:])
ecoord,_=solve_integral(A2,sp.Matrix(target)); pindex={p:i for i,p in enumerate(pairs)}
e11=sp.Matrix([[int(ecoord[pindex[(1,1)]*3+j,0]) for j in range(3)]])
enew=sp.zeros(1,NBD)
for j in range(3): enew[0,R+j]=e11[0,j]
E=d[(1,1)]-enew*S
Bmat=sp.Matrix(core['ns']['B']); delta=lp[1]*Pact[1]+lp[1]
assert E*Bmat==delta
assert max(abs(int(x)) for x in E)==a['class_B_principalization_target']['raw_boundary_solution_max_abs']==683

# Exact rank-three unit-kernel simplification; Picard image and residue parity stay fixed.
K=sp.Matrix(core['kernel_basis_old']); assert K*Bmat==sp.zeros(3,64)
adjust=a['class_B_principalization_target']['unit_kernel_adjustment_coefficients']; assert adjust==[4,218,-12]
Es=E+sp.Matrix([adjust])*K
assert Es*Bmat==delta
assert max(abs(int(x)) for x in Es)==a['class_B_principalization_target']['simplified_boundary_solution_max_abs']==36
assert all((int(Es[0,j])-int(E[0,j]))%2==0 for j in range(NBD))
bidx=[int(x)+1 for x in core['ns']['bidx']]
E_sparse={str(bidx[j]):int(Es[0,j]) for j in range(NBD) if Es[0,j]}
assert E_sparse==a['class_B_principalization_target']['simplified_boundary_divisor_E_B']

# Materialize V_B=D_B+cc(D_B)-E_B on the exact 140 retained divisor classes.
z=json.loads(GOAL4Z.read_text()); perm=perm_obj['cc_permutation_1based']
formal=[0]*140
for key,val in z['class_B']['picard_lift_cc_indlist_coefficients'].items():
    i=int(key); c=int(val); formal[i-1]+=c; formal[int(perm[i-1])-1]+=c
for key,val in E_sparse.items(): formal[int(key)-1]-=int(val)
known=[[int(x) for x in r] for r in core['ns']['known']]
cls=[sum(formal[j]*known[j][i] for j in range(140)) for i in range(64)]
assert cls==[0]*64
assert sum(x!=0 for x in formal)==a['class_B_principalization_target']['formal_target_support_count']==69

# Exact total transforms on the smooth resolution.
gram=core['ns']['gram']
def pair(i,j):
    return sum(known[i][u]*gram[u][v]*known[j][v] for u in range(64) for v in range(64))
def total_transform(curves):
    vec=[0]*140
    for i in curves: vec[i-1]+=1
    for j in range(93,141):
        if any(pair(i-1,j-1)!=0 for i in curves): vec[j-1]+=1
    return vec
def picclass(vec):
    return [sum(vec[j]*known[j][i] for j in range(140)) for i in range(64)]

# Tiny exact Q(i,sqrt(2)) arithmetic used only to identify scalar-equivalent source linear forms.
Z=(Fraction(0),)*4; ONE=(Fraction(1),Fraction(0),Fraction(0),Fraction(0))
II=(Fraction(0),Fraction(1),Fraction(0),Fraction(0)); SS=(Fraction(0),Fraction(0),Fraction(1),Fraction(0))
def add(x,y): return tuple(x[i]+y[i] for i in range(4))
def neg(x): return tuple(-t for t in x)
def mul(x,y):
    out=[Fraction(0)]*4; mons=[(0,0),(1,0),(0,1),(1,1)]
    for r,(ai,as_) in enumerate(mons):
      for t,(bi,bs) in enumerate(mons):
        ci=ai+bi; cs=as_+bs; c=x[r]*y[t]
        if ci>=2: c=-c; ci-=2
        if cs>=2: c*=2; cs-=2
        out[mons.index((ci,cs))]+=c
    return tuple(out)
IS=mul(II,SS)
def inv_pivot(x):
    cand=[ONE,neg(ONE),II,neg(II),SS,neg(SS),IS,neg(IS)]
    halfS=tuple(t/Fraction(2) for t in SS); minusHalfIS=tuple(-t/Fraction(2) for t in IS)
    inv=[ONE,neg(ONE),neg(II),II,halfS,neg(halfS),minusHalfIS,neg(minusHalfIS)]
    return inv[cand.index(x)]
def coeff(unit,sign=1):
    q={'1':ONE,'i':II,'s':SS}[unit]; return q if sign==1 else neg(q)
def form(*terms):
    v=[Z]*7
    for j,c in terms: v[j]=add(v[j],c)
    p=next(x for x in v if x!=Z); pinv=inv_pivot(p)
    return tuple(tuple((q.numerator,q.denominator) for q in mul(x,pinv)) for x in v)
def f1(j,u='1',sgn=1): return form((j,coeff(u,sgn)))
def f2(j,u,j2,u2='1',sgn2=1): return form((j,coeff(u)),(j2,coeff(u2,sgn2)))

# Reconstruct the pinned Stoll C1/C2/C3 defining linear-form incidence.
curve_forms={}; degrees={}
def addcurve(idx,deg,forms): curve_forms[idx]=forms; degrees[idx]=deg
idx=1
for base,specs in [(0,[(1,5),(2,4),(3,6)]),(1,[(2,3),(0,5),(4,6)]),(2,[(0,4),(1,3),(5,6)])]:
  for e1 in [1,-1]:
   for e2 in [1,-1]:
    for e3 in [1,-1]:
     es=[e1,e2,e3]; addcurve(idx,2,[f1(base)]+[f2(x,'1',y,'1',es[t]) for t,(x,y) in enumerate(specs)]); idx+=1
for e3 in [1,-1]:
 for e2 in [1,-1]:
  for e1 in [1,-1]:
   addcurve(idx,2,[f1(6),f2(0,'i',3,'1',e1),f2(1,'i',4,'1',e2),f2(2,'i',5,'1',e3)]); idx+=1
assert idx==33
for b,(x,y,c0) in [(3,(1,2,0)),(4,(2,0,1)),(5,(0,1,2))]:
 for e1 in [1,-1]:
  for e2 in [1,-1]:
   addcurve(idx,4,[f1(b),f2(x,'i',y,'1',e1),f2(c0,'1',6,'1',e2)]); idx+=1
assert idx==45
for x,y,b3,b1,b2 in [(0,1,5,3,4),(1,2,3,4,5),(2,0,4,5,3)]:
 for e1 in [1,-1]:
  for e2 in [1,-1]:
   for e3 in [1,-1]:
    addcurve(idx,4,[f2(x,'1',y,'1',e1),f2(x,'s',b3,'1',e2),f2(b1,'1',b2,'1',e3)]); idx+=1
for x,b2,b3,b1 in [(0,4,5,3),(1,5,3,4),(2,3,4,5)]:
 for e3 in [1,-1]:
  for e2 in [1,-1]:
   for e1 in [1,-1]:
    addcurve(idx,4,[f2(x,'i',6,'1',e1),f2(b2,'i',b3,'1',e2),form((x,IS),(b1,coeff('1',e3)))]); idx+=1
assert idx==93

groups=defaultdict(set)
for ci,forms in curve_forms.items():
    for L in forms: groups[L].add(ci)
raw={L:sorted(cs) for L,cs in groups.items() if sum(degrees[i] for i in cs)==16}
anchor_class=picclass(total_transform(list(range(1,9))))
H={}
for L,cs in raw.items():
    vec=total_transform(cs)
    if picclass(vec)==anchor_class: H[L]=vec
route=a['bounded_linear_hyperplane_route']
assert len(groups)==route['retained_distinct_linear_form_count']==79
assert len(raw)==route['raw_degree16_candidate_count']==43
assert len(H)==route['picard_certified_complete_linear_hyperplane_count']==31
M=sp.Matrix(140,len(H),lambda i,j:list(H.values())[j][i]); v=sp.Matrix(formal)
assert sp.linsolve((M,v))==sp.EmptySet
assert route['formal_target_in_Q_span_of_certified_complete_hyperplane_divisors'] is False
assert route['retained_linear_hyperplane_product_route_blocked'] is True

# Fail-close semantic and authority boundary.
fw=a['semantic_firewall']
for key in ['global_F_B_nonexistence_proved','formal_target_nonprincipal_proved','nonlinear_or_higher_degree_principalization_excluded','both_goal4y_explicit_symbols_materialized','full_Br_a_U_computed','local_evaluations_computed','verticality_proved','brauer_manin_obstruction_obtained','E1_proved','R29_PESCH_E1_closed','R29_FIB2_closed','stage35_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
    assert fw[key] is False,key
assert state['schema']=='STAGE35_EX_PESCH_E1_STATE_V64_GOAL4AA_LINEAR_HYPERPLANE_PRODUCT_ROUTE_BLOCKED_GENERAL_QI_PRINCIPAL_FUNCTION_PENDING_AUDIT'
assert state['current']['unit']==a['unit']
assert state['claims']['goal4aa_executed'] is True
assert state['claims']['open_receiver_second_class_linear_hyperplane_product_route_blocked'] is True
assert state['claims']['open_receiver_second_class_explicit_F_B_computed'] is False
assert state['claims']['brauer_manin_obstruction_obtained'] is False
assert state['claims']['E1_proved'] is False and state['claims']['stage35_closed'] is False
print('PASS Stage35-EX Goal4AA: exact 69-support Q(i) principal-divisor target fixed; retained 31 complete linear-hyperplane product route blocked; general F_B remains open')
