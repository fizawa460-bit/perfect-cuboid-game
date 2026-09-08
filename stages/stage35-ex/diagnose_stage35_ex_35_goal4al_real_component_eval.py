#!/usr/bin/env python3
"""Exact Goal4AL diagnostic: class-B real evaluation on the positive receiver component."""
from __future__ import annotations

import hashlib
import json
import math
import runpy
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
LOADER=ROOT/'stages/stage35-ex/35ex-35/goal4ak_explicit_fb.py'
ZERO=(Fraction(0),Fraction(0),Fraction(0),Fraction(0))
ONE=(Fraction(1),Fraction(0),Fraction(0),Fraction(0))

ns=runpy.run_path(str(LOADER))
num_terms,den_terms=ns['load_terms']()
assert len(num_terms)==5924 and len(den_terms)==1542

def q(x):
    return (Fraction(x),Fraction(0),Fraction(0),Fraction(0))

def ra(x):
    return (Fraction(0),Fraction(x),Fraction(0),Fraction(0))

def rb(x):
    return (Fraction(0),Fraction(0),Fraction(x),Fraction(0))

def add(u,v):
    return tuple(a+b for a,b in zip(u,v))

def mul(u,v,A,B):
    a,b,c,d=u; e,f,g,h=v
    return (
        a*e+A*b*f+B*c*g+A*B*d*h,
        a*f+b*e+B*(c*h+d*g),
        a*g+c*e+A*(b*h+d*f),
        a*h+d*e+b*g+c*f,
    )

def sq(u,A,B):
    return mul(u,u,A,B)

def powers(u,A,B,n=31):
    out=[ONE]
    for _ in range(n): out.append(mul(out[-1],u,A,B))
    return out

def evaluate(terms,coords,A,B):
    pp=[powers(u,A,B) for u in coords]
    total=ZERO
    for coeff,ex in terms:
        t=q(coeff)
        for i,e in enumerate(ex):
            if e: t=mul(t,pp[i][e],A,B)
        total=add(total,t)
    return total

def enc(u):
    return [[x.numerator,x.denominator] for x in u]

def vec_sha(u):
    return hashlib.sha256(json.dumps(enc(u),separators=(',',':')).encode()).hexdigest()

def sqrt_bounds(n,digits):
    scale10=10**digits
    target=n*scale10*scale10
    m=math.isqrt(target)
    lo=Fraction(m,scale10)
    if m*m==target:
        return lo,lo
    return lo,Fraction(m+1,scale10)

def exact_sign(u,A,B):
    if u==ZERO:return 0
    for digits in (8,16,32,64,128,256,512):
        roots=[(Fraction(1),Fraction(1)),sqrt_bounds(A,digits),sqrt_bounds(B,digits),sqrt_bounds(A*B,digits)]
        lo=Fraction(0); hi=Fraction(0)
        for coeff,(rlo,rhi) in zip(u,roots):
            if coeff>=0:
                lo+=coeff*rlo; hi+=coeff*rhi
            else:
                lo+=coeff*rhi; hi+=coeff*rlo
        if lo>0:return 1
        if hi<0:return -1
    raise AssertionError(('sign interval unresolved',A,B,vec_sha(u)))

def check_surface(coords,A,B):
    h,x,y,z,qv,p,w=coords
    assert h==ONE
    assert sq(p,A,B)==add(ONE,sq(x,A,B))
    assert sq(qv,A,B)==add(ONE,sq(y,A,B))
    assert sq(z,A,B)==add(sq(x,A,B),sq(y,A,B))
    assert sq(w,A,B)==add(ONE,add(sq(x,A,B),sq(y,A,B)))

# The first-generation diagonal probes x=y were all nonregular for the fixed
# A31/B31 presentation (run 34236284901, job 102096461707).  Use six
# non-diagonal positive-component points, in swap pairs, with rational p and q.
samples=[
    ('x3over4_y4over3',337,481,[q(1),q(Fraction(3,4)),q(Fraction(4,3)),ra(Fraction(1,12)),q(Fraction(5,3)),q(Fraction(5,4)),rb(Fraction(1,12))]),
    ('x4over3_y3over4',337,481,[q(1),q(Fraction(4,3)),q(Fraction(3,4)),ra(Fraction(1,12)),q(Fraction(5,4)),q(Fraction(5,3)),rb(Fraction(1,12))]),
    ('x3over4_y5over12',106,10,[q(1),q(Fraction(3,4)),q(Fraction(5,12)),ra(Fraction(1,12)),q(Fraction(13,12)),q(Fraction(5,4)),rb(Fraction(5,12))]),
    ('x5over12_y3over4',106,10,[q(1),q(Fraction(5,12)),q(Fraction(3,4)),ra(Fraction(1,12)),q(Fraction(5,4)),q(Fraction(13,12)),rb(Fraction(5,12))]),
    ('x5over12_y4over3',281,17,[q(1),q(Fraction(5,12)),q(Fraction(4,3)),ra(Fraction(1,12)),q(Fraction(5,3)),q(Fraction(13,12)),rb(Fraction(5,12))]),
    ('x4over3_y5over12',281,17,[q(1),q(Fraction(4,3)),q(Fraction(5,12)),ra(Fraction(1,12)),q(Fraction(13,12)),q(Fraction(5,3)),rb(Fraction(5,12))]),
]
rows=[]
regular_signs=[]
for name,A,B,coords in samples:
    check_surface(coords,A,B)
    nv=evaluate(num_terms,coords,A,B)
    dv=evaluate(den_terms,coords,A,B)
    nsig=exact_sign(nv,A,B)
    dsig=exact_sign(dv,A,B)
    regular=nsig!=0 and dsig!=0
    fsign=(nsig*dsig) if regular else None
    if regular: regular_signs.append(fsign)
    rows.append({
        'name':name,'field':f'Q(sqrt({A}),sqrt({B}))','surface_equations_exact':True,
        'numerator_vector_sha256':vec_sha(nv),'denominator_vector_sha256':vec_sha(dv),
        'numerator_sign':nsig,'denominator_sign':dsig,'regular_for_fixed_FB':regular,
        'F_B_sign':fsign,'class_B_real_invariant':'0' if fsign==1 else ('1/2' if fsign==-1 else None),
    })
probe={
    'schema':'STAGE35_EX_GOAL4AL_CLASS_B_POSITIVE_REAL_COMPONENT_PROBES_V2',
    'sample_count':len(rows),'regular_sample_count':sum(r['regular_for_fixed_FB'] for r in rows),
    'samples':rows,
}
print('GOAL4AL_REAL_PROBES_JSON='+json.dumps(probe,sort_keys=True,separators=(',',':')))
assert regular_signs, 'no regular non-diagonal positive-component sample'
assert len(set(regular_signs))==1,('inconsistent regular sample signs',regular_signs)
common=regular_signs[0]
result={
    'schema':'STAGE35_EX_GOAL4AL_CLASS_B_POSITIVE_REAL_COMPONENT_DIAGNOSTIC_V2',
    'stage':'35-EX','unit':'35EX-35_GOAL4AL_CLASS_B_LOCAL_EVALUATION_PREFLIGHT',
    'status':'PROVISIONAL_EXACT_REAL_COMPONENT_ONLY_NO_BM_NO_E1_CREDIT',
    'positive_component':'U(R)^+ = {x,y,p,q,z,w>0 on the normalized receiver surface}',
    'positive_component_connected_by_xy_graph':True,
    'initial_diagonal_probe_run':34236284901,'initial_diagonal_probe_job':102096461707,
    'initial_diagonal_regular_sample_count':0,
    'sample_count':len(rows),'regular_sample_count':sum(r['regular_for_fixed_FB'] for r in rows),
    'samples':rows,'common_F_B_sign_on_regular_samples':common,
    'class_B_positive_real_component_invariant':'0' if common==1 else '1/2',
    'population_firewall':{
        'e1_counterexample_maps_into_positive_real_component':True,
        'finite_places_not_computed':True,'primitive_reverse_adapter_not_required_for_enlarged_local_population':True,
    },
    'credit_firewall':{
        'all_local_evaluations_computed':False,'brauer_manin_obstruction_obtained':False,
        'E1_proved':False,'R29_PESCH_E1_closed':False,'stage35_closed':False,
        'perfect_cuboid_existence_claim':False,'perfect_cuboid_nonexistence_claim':False,
    },
}
print('GOAL4AL_REAL_EVAL_JSON='+json.dumps(result,sort_keys=True,separators=(',',':')))
