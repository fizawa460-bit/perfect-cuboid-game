#!/usr/bin/env python3
"""Stage14-s4c: collective activation / higher-degree reverse-count audit.

This stage is theorem-boundary bookkeeping after Stage14-4ak eliminated every
fixed physical Q-rational M-degree-4 curve mechanism.

It has two roles:
1. regenerate the exact finite active-base first-hit count V(B) and eligible
   primitive oriented Pythagorean-base count A(B) at frozen cutoffs;
2. lock the conditional exponent arithmetic for any explanation by a growing
   collection of fixed rational curves of M-degree d.

If one fixed M-degree-d rational curve contributes at most B^(2/d+o(1))
physical points, then N_d(B) such strata contribute at most
N_d(B) B^(2/d+o(1)). Hence an eventual V(B) ~ c B^(1/2) would require

    N_d(B) >= B^(1/2 - 2/d - o(1)).

This is a necessary reverse-count relation, not an existence theorem for such
strata and not a proof of the sqrt(B) law.
"""
from math import gcd, sqrt
from pathlib import Path
import json, runpy

ROOT=Path(__file__).resolve().parents[4]
GRAPH=ROOT/'stages/stage14/scripts/14-4/rank_jump_graph_audit.py'
OUTPUT=ROOT/'stages/stage14/data/14-s4c/collective_activation_reverse_count.json'
MAX_B=2_000_000
CUTOFFS=(100_000,200_000,500_000,1_000_000,2_000_000)
DEGREES=(4,6,8,10,12,16,20)


def primitive_oriented_base_count(B):
    c=0
    m=2
    while m*m+1<=B:
        for n in range(1,m):
            if ((m-n)&1)==0 or gcd(m,n)!=1: continue
            h=m*m+n*n
            if h<=B:
                c+=2  # oriented legs (S,X) and (X,S)
        m+=1
    return c


def first_hits():
    mod=runpy.run_path(str(GRAPH))
    keep,_=mod['enumerate_multi'](MAX_B)
    object_edges=mod['object_edges']
    first={}
    for (a,b,c,d),(mask,ds) in keep.items():
        if d>MAX_B or mask.bit_count()<2: continue
        for f1,f2 in object_edges(a,b,c,mask,ds):
            for f in (f1,f2):
                old=first.get(f)
                if old is None or d<old: first[f]=d
    assert len(first)==490
    return first


def exponent_requirement(d):
    return 0.5-2.0/d


def main():
    first=first_hits()
    finite=[]
    for B in CUTOFFS:
        A=primitive_oriented_base_count(B)
        V=sum(mu<=B for mu in first.values())
        finite.append({
            'B':B,'A_eligible_bases':A,'V_active_first_hit':V,
            'activation_density':V/A,
            'sqrtB_scaled_activation_density':sqrt(B)*V/A,
            'V_over_sqrtB':V/sqrt(B),
        })
    reverse=[]
    for d in DEGREES:
        e=exponent_requirement(d)
        reverse.append({
            'M_degree':d,
            'single_fixed_curve_height_exponent':2.0/d,
            'required_stratum_count_exponent_for_sqrtB':e,
            'interpretation':('fixed finite number could match sqrt(B) exponent' if e<=0 else f'N_d(B) must be at least B^({e:g}-o(1)) if this degree alone explains a sqrt(B) law')
        })
    report={
      'metadata':{'stage':'14-s4c','max_B':MAX_B,'cutoffs':list(CUTOFFS)},
      'finite_activation':finite,
      'reverse_count':{
        'general_rule':'if each fixed M-degree-d rational stratum contributes at most B^(2/d+o(1)), then V(B)~c*B^(1/2) requires N_d(B)>=B^(1/2-2/d-o(1))',
        'degrees':reverse,
        'degree4_status':'eliminated geometrically/arithmetic-lattice-wise by merged Stage14-4ak; exponent zero here is only arithmetic bookkeeping, not a surviving mechanism',
        'mixed_degree_status':'for a mixture, sum_d N_d(B) B^(2/d+o(1)) must reach the target scale; this stage does not optimize an unknown degree distribution.'
      },
      's4b_handoff':{
        'active_vertices':490,
        'exact_kummer_class_triples':483,
        'coarse_signatures':393,
        'largest_coarse_cluster':4,
        'singleton_coarse_signatures':326,
        'interpretation':'finite active arithmetic is highly dispersed, so a collective explanation should not assume a few repeated exact/coarse descent classes.'
      },
      'decision':{
        'STAGE14_S4C':'COMPLETE_COLLECTIVE_ACTIVATION_REVERSE_COUNT_BOUNDARY',
        'FIXED_M4_MECHANISM_CLOSED_BY_4AK':True,
        'COLLECTIVE_PROLIFERATION_NECESSITY_FORMULA_LOCKED':True,
        'DEGREE8_REQUIRED_COUNT_EXPONENT':'1/4',
        'DEGREE12_REQUIRED_COUNT_EXPONENT':'1/3',
        'FINITE_S4B_DISPERSION_IMPORTED':True,
        'SQRT_B_ASYMPTOTIC_PROVED':False,
        'HIGHER_DEGREE_STRATA_EXISTENCE_PROVED':False,
        'NEXT':'Stage14-s5 seek a uniform arithmetic small-point/rank-jump counting theorem compatible with the collective activation measure'
      }
    }
    OUTPUT.parent.mkdir(parents=True,exist_ok=True)
    OUTPUT.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__': main()
