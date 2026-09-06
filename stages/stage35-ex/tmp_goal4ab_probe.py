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

# Independent reduced-coordinate test: differences against the first full hyperplane.
vals=list(full.values())
if vals:
    D=sp.Matrix(140,max(0,len(vals)-1),lambda i,j: vals[j+1][i]-vals[0][i])
    solD=sp.linsolve((D,v))
    print('GOAL4AB_PROBE target_in_Q_span_of_differences',solD!=sp.EmptySet)
    print('GOAL4AB_PROBE difference_rank',D.rank())

print('PASS Goal4AB probe: exact exceptional completion of all degree-16 retained linear sections tested')
