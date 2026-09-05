#!/usr/bin/env python3
"""Verify 35EX-35 goals 1-3: private edge-gcd six-variable exact decomposition."""
from __future__ import annotations
import hashlib, json
from itertools import permutations
from math import gcd, isqrt
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
ART=ROOT/'stages/stage35-ex/35ex-35/private-edge-gcd-six-variable-decomposition.json'
ARS=ROOT/'docs/arsenal/cards/formal/S34-W01.md'
SCHEMA='STAGE35_EX_PESCH_E1_STATE_V34_POST_35EX34_HOSTILE_AUDITED_PRIVATE_GCD_PREFLIGHT'
BASE='605ef83aae1ba2804537eb6dc36695ca80ade412'
PARENT_MERGE='c8a876838882c91c078c85da5c88d131b151ac40'
PARENT_REVIEW=5120821124
PARENT_HEAD='f381177b10f709dccfb9628e56d2dbdf5d811e3d'
PARENT_RUN=33960030022
PARENT_JOB=101290193422
ARS_BLOB='01a8e90e34b4aa46edbfa825803d488e5230e9d0'

def git_blob_sha(path:Path)->str:
    data=path.read_bytes()
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

def is_square(n:int)->bool:
    r=isqrt(n)
    return r*r==n

def v2(n:int)->int:
    k=0
    while n%2==0:
        n//=2; k+=1
    return k

state=json.loads(STATE.read_text())
art=json.loads(ART.read_text())
assert state['schema']==SCHEMA and state['stage']=='35-EX' and state['status']=='ACTIVE_RESEARCH_NO_CREDIT'
assert state['base_main_sha']==BASE
assert state['history_snapshot']['commit_sha']==PARENT_MERGE
pa=state['parent_authority']
assert pa['unit']=='35EX-34' and pa['audit_verdict']=='HOSTILE_AUDIT_PASS'
assert pa['hostile_review_id']==PARENT_REVIEW and pa['exact_head_sha']==PARENT_HEAD
assert pa['exact_head_ci_run']==PARENT_RUN and pa['exact_head_ci_job']==PARENT_JOB
assert pa['merged_main_sha']==PARENT_MERGE
assert pa['route_status']=='PASS_NEW_GATE_FROM_STRONGER_VIEW'
assert state['current']['unit']=='35EX-35_PRIVATE_EDGE_GCD_SIX_VARIABLE_DECOMPOSITION_PREFLIGHT'
assert state['current']['status']=='PROVISIONAL_EXACT_GOALS_1_TO_3_PENDING_HOSTILE_AUDIT_NO_E1_CREDIT'
ri=state['resolved_investigations']
assert ri['CURRENT_PRIMITIVE_SOURCE_MARKING']['status']=='AUDITED_EXACT_REVERSE_ADAPTER_AND_ENDPOINT_POPULATION_EQUIVALENCE_NO_E1_CREDIT'
assert ri['SOURCE_MARKING_AS_STRICT_ENDPOINT_RESTRICTION']['status']=='BLOCKED_EQUIVALENT_TO_GAUGE'
assert ri['HISTORICAL_GAUSSIAN_ORIENTATION_ROUTE_35EX13_17B_18']['status']=='FROZEN_NO_RECHARGE'
assert ri['ENDPOINT_THREE_FACE_SHARED_GAUSSIAN_SUPPORT_35EX33']['all_deeper_gaussian_arguments_ruled_out'] is False
ledger=state['candidate_ledger']
assert ledger['untested_count']==8 and ledger['split_triggered'] is False
assert 'E1-GAUSSIAN-THREE-FACE-COMPATIBILITY-DESCENT' in ledger['blocked']
assert 'E1-S3-SYMMETRIC-ENDPOINT-INVARIANTS_WITHOUT_STRICT_ARITHMETIC_REDUCTION' in ledger['blocked']

assert art['schema']=='STAGE35_EX_35_PRIVATE_EDGE_GCD_SIX_VARIABLE_DECOMPOSITION_V1'
assert art['status']=='PROVISIONAL_EXACT_GOALS_1_TO_3_NO_E1_CREDIT'
assert art['base_main_sha']==BASE
assert art['parent_35ex34']['hostile_review_id']==PARENT_REVIEW
assert art['parent_35ex34']['merge_sha']==PARENT_MERGE
assert git_blob_sha(ARS)==ARS_BLOB==art['arsenal']['S34_W01_blob']
assert art['arsenal']['status']=='PREFLIGHT_ONLY_NOT_TRIGGERED'
assert art['goal4_boundary']['status']=='NOT_EXECUTED_IN_THIS_LEAF'
assert art['goal4_boundary']['finite_squareclass_receiver_obtained'] is False
assert art['goal4_boundary']['new_valuation_restriction_from_space_square_claimed'] is False

# Goal 1/2 exact integer gcd identities: exhaustive regression over primitive triples.
for A in range(1,42):
  for B in range(1,42):
    for C in range(1,42):
      if gcd(gcd(A,B),C)!=1:
        continue
      x,y,z=gcd(A,B),gcd(A,C),gcd(B,C)
      assert gcd(x,y)==gcd(x,z)==gcd(y,z)==1
      assert A%(x*y)==B%(x*z)==C%(y*z)==0
      a,b,c=A//(x*y),B//(x*z),C//(y*z)
      assert (A,B,C)==(x*y*a,x*z*b,y*z*c)
      assert gcd(y*a,z*b)==1
      assert gcd(x*a,z*c)==1
      assert gcd(x*b,y*c)==1
      assert gcd(a,b)==gcd(a,c)==gcd(b,c)==1
      assert gcd(a,z)==gcd(b,y)==gcd(c,x)==1

# Exact parity lemmas used in the proof.
SQ4={i*i%4 for i in range(4)}
SQ8={i*i%8 for i in range(8)}
assert 2 not in SQ4                     # two odd legs cannot have square hypotenuse
assert 5 not in SQ8                     # primitive odd leg + v2(even leg)=1 is impossible

# Non-vacuous regression on primitive Euler bricks, including all edge placements.
for A,B,C in set(permutations((44,117,240))) | set(permutations((85,132,720))):
    assert gcd(gcd(A,B),C)==1
    assert is_square(A*A+B*B) and is_square(A*A+C*C) and is_square(B*B+C*C)
    odds=[A%2,B%2,C%2]
    assert sum(odds)==1
    evens=[q for q in (A,B,C) if q%2==0]
    assert all(q%4==0 for q in evens)
    assert v2(evens[0])!=v2(evens[1])
    x,y,z=gcd(A,B),gcd(A,C),gcd(B,C)
    a,b,c=A//(x*y),B//(x*z),C//(y*z)
    if A%2:
        assert x%2 and y%2 and a%2 and z%4==0 and (b%2)!=(c%2)
    elif B%2:
        assert x%2 and z%2 and b%2 and y%4==0 and (a%2)!=(c%2)
    else:
        assert y%2 and z%2 and c%2 and x%4==0 and (a%2)!=(b%2)

# Goal 3 symbolic identities.
x,y,z,a,b,c,rab,rac,rbc,W=sp.symbols('x y z a b c r_AB r_AC r_BC W')
A=x*y*a; B=x*z*b; C=y*z*c
assert sp.expand(A**2+B**2-x**2*((y*a)**2+(z*b)**2))==0
assert sp.expand(A**2+C**2-y**2*((x*a)**2+(z*c)**2))==0
assert sp.expand(B**2+C**2-z**2*((x*b)**2+(y*c)**2))==0
space=sp.expand(A**2+B**2+C**2)
# Each space/face coupling differs from zero by the corresponding primitive
# face relation multiplied by the exact edge gcd squared.
assert sp.expand(space-((x*rab)**2+C**2)-x**2*((y*a)**2+(z*b)**2-rab**2))==0
assert sp.expand(space-((y*rac)**2+B**2)-y**2*((x*a)**2+(z*c)**2-rac**2))==0
assert sp.expand(space-((z*rbc)**2+A**2)-z**2*((x*b)**2+(y*c)**2-rbc**2))==0

cf=art['credit_firewall']
assert cf['six_variable_exact_decomposition'] is True
assert cf['primitive_face_dictionary'] is True
assert cf['three_face_and_space_exact_rewrite'] is True
for key in ('universal_torsor_constructed','finite_squareclass_receiver_obtained','E1_proved','R29_PESCH_E1_closed','R29_FIB2_closed','J12_PARAMETRIC_closed','stage35_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim'):
    assert cf[key] is False, key
claims=state['claims']
for key in ('universal_torsor_constructed','finite_squareclass_receiver_obtained','E1_proved','R29_PESCH_E1_closed','R29_FIB2_closed','J12_PARAMETRIC_closed','stage35_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim'):
    assert claims[key] is False, key

print('PASS STAGE35_EX_35_PRIVATE_EDGE_GCD_SIX_VARIABLE_EXACT_DECOMPOSITION_GOALS_1_TO_3')
