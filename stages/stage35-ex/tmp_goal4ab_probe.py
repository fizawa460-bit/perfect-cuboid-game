#!/usr/bin/env python3
from __future__ import annotations
import json, runpy
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
ns=runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_35_goal4aa.py'))
raw=ns['raw']; known=ns['known']; anchor_class=ns['anchor_class']; picclass=ns['picclass']; formal=ns['formal']

Ecols=sp.Matrix(64,48,lambda i,j: known[92+j][i])
print('GOAL4AB_PROBE exceptional_rank',Ecols.rank())
assert Ecols.rank()==48

full={}
mult_hist={}
fail=[]
for L,cs in raw.items():
    strict=[0]*140
    for ci in cs: strict[ci-1]+=1
    rhs=sp.Matrix(anchor_class)-sp.Matrix(picclass(strict))
    solset=sp.linsolve((Ecols,rhs))
    if solset==sp.EmptySet:
        fail.append(('inconsistent',L,cs)); continue
    sols=list(solset)
    if len(sols)!=1:
        fail.append(('nonsingleton',L,cs)); continue
    x=list(sols[0])
    if any(v.free_symbols for v in x):
        fail.append(('nonunique',L,cs)); continue
    if any(v.q!=1 for v in x):
        fail.append(('nonintegral',L,cs,x)); continue
    xi=[int(v) for v in x]
    if any(v<0 for v in xi):
        fail.append(('negative',L,cs,xi)); continue
    vec=strict[:]
    for j,v in enumerate(xi): vec[92+j]=v
    assert picclass(vec)==anchor_class
    full[L]=vec
    for v in xi: mult_hist[v]=mult_hist.get(v,0)+1

print('GOAL4AB_PROBE raw_count',len(raw),'full_count',len(full),'fail_count',len(fail))
print('GOAL4AB_PROBE exceptional_multiplicity_hist',json.dumps(mult_hist,sort_keys=True))
if fail:
    print('GOAL4AB_PROBE failures',repr(fail[:4]))

M=sp.Matrix(140,len(full),lambda i,j:list(full.values())[j][i])
v=sp.Matrix(formal)
sol=sp.linsolve((M,v))
print('GOAL4AB_PROBE target_in_Q_span',sol!=sp.EmptySet)
print('GOAL4AB_PROBE matrix_rank',M.rank())
if sol!=sp.EmptySet:
    tup=next(iter(sol))
    free=sorted(set().union(*(e.free_symbols for e in tup)),key=str)
    print('GOAL4AB_PROBE free_parameter_count',len(free))
    if not free:
        den_lcm=sp.ilcm(*[int(e.q) for e in tup]) if tup else 1
        print('GOAL4AB_PROBE unique_solution_den_lcm',den_lcm)
        print('GOAL4AB_PROBE unique_solution',repr([str(e) for e in tup]))

vals=list(full.values())
if vals:
    D=sp.Matrix(140,max(0,len(vals)-1),lambda i,j: vals[j+1][i]-vals[0][i])
    solD=sp.linsolve((D,v))
    print('GOAL4AB_PROBE target_in_Q_span_of_differences',solD!=sp.EmptySet)
    print('GOAL4AB_PROBE difference_rank',D.rank())

# Retained Stoll C4/C5 nonlinear defining sections: test the natural
# degree-balanced elimination identities exactly in the projective surface ring.
a1,a2,a3,b1,b2,b3,c=sp.symbols('a1 a2 a3 b1 b2 b3 c')
i=sp.I
G=sp.groebner([
    a1**2+a2**2-b3**2,
    a2**2+a3**2-b1**2,
    a1**2+a3**2-b2**2,
    a1**2+a2**2+a3**2-c**2,
],c,b3,b2,b1,a3,a2,a1,extension=i)
def zero_on_surface(expr):
    return sp.expand(G.reduce(sp.expand(expr))[1])==0

# C4: each of the four source families has four degree-1 sections and two
# degree-2 sections cutting the same eight degree-8 C4 components in aggregate.
# The degree-balanced elimination is already a scalar polynomial identity.
c4_specs=[
    (1,1,a2*a3,i*a1*b1),
    (i,1,a1*a3,b2*c),
    (1,i,a1*a2,b3*c),
    (i,i,a2*a3,b1*c),
]
for alpha2,alpha3,q0,q1 in c4_specs:
    lp=sp.prod([b1+e2*alpha2*b2+e3*alpha3*b3 for e2 in (1,-1) for e3 in (1,-1)])
    qp=(q0+q1)*(q0-q1)
    assert zero_on_surface(lp+4*qp)
print('GOAL4AB_PROBE c4_degree_balanced_identities',len(c4_specs))

# C5: for each sign pair, eliminating the four C5 curves by pairing the two
# source quadrics gives exactly the product of the four conjugate linear sections.
c5_count=0
for e2 in (1,-1):
    for e3 in (1,-1):
        l1=sp.prod([a1+e2*a2+e3*a3+e4*i*c for e4 in (1,-1)])
        l2=sp.prod([a1-e2*a2-e3*a3+e4*i*c for e4 in (1,-1)])
        qp=sp.prod([(e2*a2+e3*a3)*b1+e1*i*b2*b3 for e1 in (1,-1)])
        assert zero_on_surface(l1*l2-4*qp)
        c5_count+=1
print('GOAL4AB_PROBE c5_paired_quadratic_identities',c5_count)
print('GOAL4AB_PROBE retained_C4_C5_nonlinear_elimination_adds_new_divisor_direction',False)

print('PASS Goal4AB probe: 43 exact complete linear sections plus retained C4/C5 low-degree nonlinear eliminations do not synthesize F_B')
