#!/usr/bin/env python3
"""Verify 35EX-33 pairwise Gaussian gcd/support blocker and all credit firewalls."""
from __future__ import annotations
import hashlib, json
from math import gcd, isqrt
from pathlib import Path
from sympy import I, symbols, simplify

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
ART=ROOT/'stages/stage35-ex/35ex-33/pairwise-gaussian-gcd-support-route-blocker.json'
SCHEMA='STAGE35_EX_PESCH_E1_STATE_V32_POST_35EX32_USER_APPROVED_MERGE_ROUTE_SELECTION'
BASE_MAIN='3b4b5969330ae89a41899598fbdf17e76be76f72'

def git_blob_sha(path:Path)->str:
    data=path.read_bytes()
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

state=json.loads(STATE.read_text())
art=json.loads(ART.read_text())
assert state['schema']==SCHEMA and state['base_main_sha']==BASE_MAIN
assert art['schema']=='STAGE35_EX_33_PAIRWISE_GAUSSIAN_GCD_SUPPORT_ROUTE_BLOCKER_V1'
assert art['stage']=='35-EX'
assert art['unit']=='35EX-33_GAUSSIAN_THREE_FACE_COMPATIBILITY_PREFLIGHT'
assert art['small_goals_closed']==[3,4,5]
assert art['status']=='PROVISIONAL_EXACT_ROUTE_BLOCKER_PENDING_HOSTILE_AUDIT_NO_E1_CREDIT'

for key,lock in art['source_locks'].items():
    p=ROOT/lock['path']
    actual=git_blob_sha(p)
    assert actual==lock['blob_sha'], (key,actual,lock['blob_sha'])

fac=art['individual_face_factorization']
assert fac['pairwise_coprime_edge_gcds']=='gcd(g_AB,g_AC)=gcd(g_AB,g_BC)=gcd(g_AC,g_BC)=1'
assert fac['exact_factorizations']==[
    'F_AB=epsilon_AB*g_AB*Z_AB^2',
    'F_AC=epsilon_AC*g_AC*Z_AC^2',
    'F_BC=epsilon_BC*g_BC*Z_BC^2',
]
assert fac['self_conjugate_gcd_ideals']==[
    '(F_AB,conj(F_AB))=(g_AB)',
    '(F_AC,conj(F_AC))=(g_AC)',
    '(F_BC,conj(F_BC))=(g_BC)',
]
assert art['two_adic_bookkeeping']['exact_parity']=='exactly one of A,B,C is odd'
assert 'absent from every gcd between two distinct face Gaussians' in art['two_adic_bookkeeping']['consequence']
assert 'every Gaussian prime dividing g_AB is absent' in art['private_edge_gcd_support']['statement']

locators=art['exact_distinct_face_gcd_locator_ideals']
assert locators==[
    '(F_AB,F_AC)=(F_AB,B-C)',
    '(F_AB,conj(F_AC))=(F_AB,B+C)',
    '(F_AB,F_BC)=(F_AB,A+C)',
    '(F_AB,conj(F_BC))=(F_AB,A-C)',
    '(F_AC,F_BC)=(F_AC,A-B)',
    '(F_AC,conj(F_BC))=(F_AC,A+B)',
]
A,B,C=symbols('A B C', integer=True, real=True)
FAB=A+I*B; FAC=A+I*C; FBC=B+I*C
barFAC=A-I*C; barFBC=B-I*C
assert simplify(FAB-FAC-I*(B-C))==0
assert simplify(FAB-barFAC-I*(B+C))==0
assert simplify(FAB-I*FBC-(A+C))==0
assert simplify(FAB-I*barFBC-(A-C))==0
assert simplify(FAC-FBC-(A-B))==0
assert simplify(FAC+barFBC-(A+B))==0

cross=art['cross_face_square_gcd_theorem']
assert 'gcd ideal in Z[i] is a square ideal' in cross['statement']
assert '1+i does not divide that gcd' in cross['statement']
assert 'unit times H^2' in cross['generator_form']
assert 'every shared Gaussian-prime exponent in the gcd is even' in cross['odd_shared_prime_locator']

sq=art['squareclass_output']
assert sq['cross_face_shared_squareclass'].startswith('trivial: every distinct-face gcd is square')
assert sq['finite_receiver_obtained'] is False
assert 'pairwise coprime, private to their own faces' in sq['remaining_support']

hist=art['historical_no_recharge_comparison']
assert hist['old_credit_recharged'] is False
assert hist['35EX13'].startswith('DISTINCT_BLOCKER')
assert hist['35EX17B'].startswith('DISTINCT_BLOCKER')
assert hist['35EX18'].startswith('DISTINCT_BLOCKER')
ars=art['arsenal_comparison']
assert ars['S34_W01_classification']=='PARTIAL_ROUTER_MATCH_THEN_BLOCKED_BEFORE_FINITE_BRANCH_TRIGGER'
assert ars['S34_W01_receiver_credit'] is False
assert 'private moving rational squareclasses' in ars['blocking_reason']
route=art['route_decision']
assert route['cycle_route_status']=='BLOCKED_NEW_PATTERN_ISOLATED'
assert route['exact_blocker']=='DISTINCT_FACE_GAUSSIAN_GCDS_ARE_SQUARE_AND_ONLY_PRIVATE_MOVING_EDGE_GCD_SQUARECLASSES_REMAIN'
assert route['selected_gaussian_three_face_shared_support_route_live'] is False
assert route['all_deeper_gaussian_or_reciprocity_arguments_ruled_out'] is False
assert route['E1_route_impossible'] is False
assert route['next_if_hostile_audit_pass']=='35EX-34_POST_GAUSSIAN_BLOCK_FRESH_BREADTH_AUDIT'
exit_=art['cycle_exit']
assert exit_['CYCLE_ROUTE_STATUS']=='BLOCKED_NEW_PATTERN_ISOLATED'
assert exit_['CYCLE_LIVE_CANDIDATES']==0 and exit_['CYCLE_UNTESTED_CANDIDATES']==8
assert exit_['CYCLE_EXHAUSTIVE_VIEW_AUDIT'] is False and exit_['CYCLE_BLIND_REDISCOVERY'] is False
assert exit_['CYCLE_NEW_VIEW_SOURCE']=='INTERNAL_DERIVATION'

u33=state['completed_units_delta']['35EX-33']
assert u33['status']=='PROVISIONAL_EXACT_ROUTE_BLOCKER_PENDING_HOSTILE_AUDIT_NO_E1_CREDIT'
assert u33['completed_small_goals']==[1,2,3,4,5]
assert u33['distinct_face_gaussian_gcds_square_ideals'] is True
assert u33['private_moving_edge_gcd_squareclasses_only'] is True
assert u33['finite_squareclass_receiver_credit'] is False
assert u33['route_status']=='BLOCKED_NEW_PATTERN_ISOLATED'
cur=state['current']
assert cur['unit']=='35EX-33_GAUSSIAN_THREE_FACE_COMPATIBILITY_PREFLIGHT'
assert cur['status']=='PROVISIONAL_EXACT_ROUTE_BLOCKER_PENDING_HOSTILE_AUDIT_NO_E1_CREDIT'
assert cur['completed_small_goals']==[1,2,3,4,5]
assert cur['next_if_hostile_audit_pass']=='RUN_35EX34_POST_GAUSSIAN_BLOCK_EXHAUSTIVE_VIEW_AUDIT_PLUS_BLIND_REDISCOVERY'
assert state['candidate_ledger']['untested_count']==8
assert state['candidate_ledger']['next_selection_requires_fresh_breadth_audit'] is True

# Regression helpers over Gaussian integers; these are checks, not the proof.
UNITS=((1,0),(-1,0),(0,1),(0,-1))
def gmul(z,w): return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
def gnorm(z): return z[0]*z[0]+z[1]*z[1]
def gsquare(z): return gmul(z,z)
def is_unit_square(z):
    n=gnorm(z)
    h=isqrt(n)
    if h*h!=n: return False
    bound=isqrt(h)+2
    for a in range(-bound,bound+1):
        for b in range(-bound,bound+1):
            s=gsquare((a,b))
            for u in UNITS:
                if gmul(u,s)==z:
                    return True
    return False

def gdivmod(z,w):
    a,b=z; c,d=w; n=c*c+d*d
    from math import floor, ceil
    xr=(a*c+b*d)/n; yi=(b*c-a*d)/n
    best=None
    for r in {floor(xr),ceil(xr)}:
        for s in {floor(yi),ceil(yi)}:
            rem=(a-(r*c-s*d), b-(r*d+s*c))
            item=(gnorm(rem),rem)
            if best is None or item[0]<best[0]: best=item
    return best[1]
def ggcd(z,w):
    while w!=(0,0): z,w=w,gdivmod(z,w)
    return z

for x,y in ((3,4),(5,12),(7,24),(20,21),(9,40),(11,60)):
    for g in (1,2,3,5,6):
        F=(g*x,g*y)
        assert is_unit_square((F[0]//g,F[1]//g))

fixtures=((44,117,240),(85,132,720),(140,480,693),(160,231,792),(240,252,275))
for a,b,c in fixtures:
    assert gcd(gcd(a,b),c)==1
    assert sum(x%2 for x in (a,b,c))==1
    gs=(gcd(a,b),gcd(a,c),gcd(b,c))
    assert gcd(gs[0],gs[1])==gcd(gs[0],gs[2])==gcd(gs[1],gs[2])==1
    faces=((a,b),(a,c),(b,c))
    for (x,y),g in zip(faces,gs):
        assert is_unit_square((x//g,y//g))
        selfg=ggcd((x,y),(x,-y))
        assert gnorm(selfg)==g*g
    for i in range(3):
        for j in range(i+1,3):
            for conj in (False,True):
                w=faces[j] if not conj else (faces[j][0],-faces[j][1])
                d=ggcd(faces[i],w)
                assert is_unit_square(d)
                assert not ((d[0]-d[1])%2==0 and gnorm(d)>1), (a,b,c,i,j,conj,d)

cf=art['credit_firewall']
assert cf['pairwise_gaussian_gcd_support_exact'] is True
for key in ('finite_squareclass_receiver_obtained','gaussian_compatibility_theorem_proved','E1_proved','R29_PESCH_E1_closed','R29_FIB2_closed','J12_PARAMETRIC_closed','stage35_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim'):
    assert cf[key] is False, key
claims=state['claims']
for key in ('finite_squareclass_receiver_obtained','gaussian_compatibility_theorem_proved','E1_proved','R29_PESCH_E1_closed','R29_FIB2_closed','J12_PARAMETRIC_closed','stage35_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim'):
    assert claims[key] is False, key

print('PASS STAGE35_EX_33_PAIRWISE_GAUSSIAN_GCD_SUPPORT_ROUTE_BLOCKER')
