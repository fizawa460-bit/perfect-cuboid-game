#!/usr/bin/env python3
"""Verify Goal4E: all-odd-prime universal edge-zero classification and finite forced-prime receiver."""
from __future__ import annotations
import itertools, json, math
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / 'stages/stage35-ex/MAIN-STATE.json'
ART = ROOT / 'stages/stage35-ex/35ex-35/goal4e-all-odd-prime-zero-support-classification.json'
state = json.loads(STATE.read_text())
art = json.loads(ART.read_text())

LIVE_BASE = 'b6b538b4c8838e24ddf99eb05fc022fe50056af4'
G4D_MERGE = '2949391d032a9014b0e9ffebce78be84a93d1d8a'
HEAD4D = '6684b731fcca201bee1af96d868eaf74a0b62574'
REVIEW4D = 5123225301
assert state['schema'] == 'STAGE35_EX_PESCH_E1_STATE_V42_GOAL4E_ALL_ODD_PRIME_ZERO_SUPPORT_CLASSIFICATION_PENDING_AUDIT'
assert state['base_main_sha'] == LIVE_BASE
assert state['parent_authority']['pr'] == 1631
assert state['parent_authority']['hostile_review_id'] == REVIEW4D
assert state['parent_authority']['exact_head_sha'] == HEAD4D
assert state['parent_authority']['exact_head_ci_run'] == 33995239057
assert state['parent_authority']['exact_head_ci_job'] == 101384520908
assert state['parent_authority']['merge_sha'] == G4D_MERGE
assert art['base_main_sha'] == LIVE_BASE
assert art['parent_goal4d_authority']['hostile_review_id'] == REVIEW4D
assert art['parent_goal4d_authority']['exact_head_sha'] == HEAD4D
assert art['parent_goal4d_authority']['merge_sha'] == G4D_MERGE

def qset(p:int)->set[int]: return {x*x%p for x in range(p)}
def nonzero_projective_counts(p:int)->tuple[int,int]:
    Q=qset(p); face=full=0
    for B,C in itertools.product(range(1,p),repeat=2):
        vals=((1+B*B)%p,(1+C*C)%p,(B*B+C*C)%p)
        if not all(v in Q for v in vals): continue
        face+=1
        if (1+B*B+C*C)%p in Q: full+=1
    return face,full
small_primes=list(sp.primerange(3,97))
rows=[(p,*nonzero_projective_counts(p)) for p in small_primes]
assert rows==[tuple(r) for r in art['small_prime_exact_census']['rows']]
forced=[p for p,face,full in rows if full==0]
face_forced=[p for p,face,full in rows if face==0]
fourth_new=[p for p,face,full in rows if face>0 and full==0]
assert forced==[3,5,7,11,19]
assert face_forced==[3,5,11]
assert fourth_new==[7,19]

def normalize_projective(v,p):
    for x in v:
        if x%p:
            inv=pow(x,-1,p); return tuple(t*inv%p for t in v)
    raise AssertionError('zero vector')
def full_projective_classes(p):
    Q=qset(p); classes=set()
    for A,B,C in itertools.product(range(p),repeat=3):
        if A==B==C==0: continue
        vals=((A*A+B*B)%p,(A*A+C*C)%p,(B*B+C*C)%p,(A*A+B*B+C*C)%p)
        if all(v in Q for v in vals): classes.add(normalize_projective((A,B,C),p))
    return classes
expected={3:3,5:9,7:9,11:15,19:27}
for p in forced:
    cls=full_projective_classes(p)
    assert len(cls)==expected[p]
    zs={sum(x==0 for x in v) for v in cls}
    assert zs==({2} if p==3 else {1,2})
    assert all(any(x==0 for x in v) for v in cls)

s=sp.symbols('s')
a=6*s**5-20*s**3+6*s
b=-s**6+15*s**4-15*s**2+1
c=8*s**5-8*s
F=s**8+68*s**6-122*s**4+68*s**2+1
assert sp.expand(a*a+b*b-(s*s+1)**6)==0
assert sp.expand(a*a+c*c-4*(5*s**5-6*s**3+5*s)**2)==0
assert sp.expand(b*b+c*c-(s**6+17*s**4-17*s**2-1)**2)==0
assert sp.expand(a*a+b*b+c*c-(s*s+1)**2*F)==0
assert sp.factorint(int(sp.discriminant(F,s)))=={2:72,5:4}
assert sp.degree(F,s)==8
assert art['large_prime_completion']['smooth_genus']==3
assert sp.degree(a,s)+sp.degree(b,s)+sp.degree(c,s)==16
assert art['large_prime_completion']['bad_affine_points_upper_bound']==32
assert art['large_prime_completion']['points_at_infinity']==2
def lower(p): return p+1-6*math.sqrt(p)
assert lower(89)<=34<lower(97)
assert all(lower(p)>34 for p in sp.primerange(97,1000))
assert all(full>0 for p,face,full in rows if p not in forced)

assert art['global_integer_consequence']['combined_divisor']==65835
assert 3**2*5*7*11*19==65835
edges=(0,1,2)
single=[frozenset([i]) for i in edges]
double=[frozenset(set(edges)-{i}) for i in edges]
assignments=list(itertools.product(double,single+double,single+double,single+double,single+double))
assert len(assignments)==3888
perms=list(itertools.permutations(edges))
def act(S,p): return frozenset(p[i] for i in S)
def canon(asg): return min(tuple(tuple(sorted(act(S,p))) for S in asg) for p in perms)
orbits={canon(a0) for a0 in assignments}
assert len(orbits)==656
assert art['finite_global_forced_prime_support_receiver']['S3_orbits']==656
boundary=art['exact_boundary']
assert boundary['all_odd_primes_classified_for_universal_edge_zero_obstruction'] is True
assert boundary['all_odd_prime_Qp_local_conditions_classified'] is False
assert boundary['finite_exhaustive_global_squareclass_family_obtained'] is False
assert state['current']['unit']=='35EX-35_GOAL4E_ODD_PRIME_LOCAL_BREADTH_AND_FINITE_GLOBAL_RECEIVER_TEST'
assert state['current']['status']=='PROVISIONAL_PENDING_HOSTILE_AUDIT_NO_E1_CREDIT'
assert state['claims']['forced_odd_prime_set']==[3,5,7,11,19]
assert state['claims']['forced_ABC_divisor']==65835
assert state['claims']['finite_global_forced_prime_support_S3_orbits']==656
assert state['claims']['all_odd_prime_Qp_local_conditions_classified'] is False
assert state['claims']['finite_squareclass_receiver_obtained'] is False
assert state['claims']['E1_proved'] is False and state['claims']['stage35_closed'] is False
print('PASS STAGE35_EX_35_GOAL4E_ALL_ODD_PRIME_ZERO_SUPPORT_EXACT_FORCED_SET_3_5_7_11_19_GLOBAL_656_ORBITS')
