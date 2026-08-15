#!/usr/bin/env python3
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import json

root=Path(__file__).resolve().parents[3]
r504=(root/'stages/stage25/25-60/r504-base-change-boundary.md').read_text()
policy=(root/'stages/stage25/25-60/continuation-policy.md').read_text()
reaudit=(root/'stages/stage25/25-60/r505-r506-audit-recheck.md').read_text()
ctl=json.loads((root/'stages/stage25/25-60/r505-r506-iteration-controller.json').read_text())

def sf(n):
    out=1; p=2
    while p*p<=n:
        odd=0
        while n%p==0: n//=p; odd^=1
        if odd: out*=p
        p=3 if p==2 else p+2
    return out*n

def sq(n):
    r=isqrt(n); return r*r==n

# Retain accepted R505/R506 identity regression.
rows=0
for n in range(1,12):
  for m in range(n+1,22):
    if gcd(m,n)!=1: continue
    for s in range(1,9):
      for r in range(s+1,16):
        if gcd(r,s)!=1: continue
        A=m*m*r*r+n*n*s*s; B=m*m*s*s+n*n*r*r
        assert (sf(A)==sf(B)) == sq(A*B)
        u=m*r; v=n*s; w=m*s; z=n*r
        assert u*v==w*z and A==u*u+v*v and B==w*w+z*z
        rows+=1
assert rows>3000

# BC1/BC2 accepted certificates stay bound.
for marker in ['R504_BC1_STATUS=CLOSED_NO_RANK_JUMP','R504_BC2_STATUS=CLOSED_NO_RANK_JUMP']:
    assert marker in r504

# Exact-Q Kummer overclaim is removed and safe class is explicit.
for marker in [
 'R504_STANDARD_Q_KUMMER_IDENTIFICATION=false',
 'R504_SAFE_KUMMER_CLASS=Q_FORM_OR_TWIST_OF_PRODUCT_KUMMER',
 'R504_KUMMER_MODEL_EXACT_OVER_Q=false']:
    assert marker in r504
assert 'R504_KUMMER_MODEL=Km(E0xE0)' not in r504

# Materialized real-component parity lemma: direct numerical range regression.
for F in [1,2,5,17]:
  for t in [Fraction(0),Fraction(1,3),Fraction(1),Fraction(3,2),Fraction(4)]:
    X=Fraction(-4*F)*t*t/(t**4+1)
    assert Fraction(-2*F)<=X<=0
for marker in [
 'R504_QUARTIC_REAL_X_RANGE=[-2F,0]',
 'R504_REAL_COMPONENT_GROUP=Z/2',
 'R504_GENERATOR_COMPONENT=NONIDENTITY',
 'R504_EVEN_MULTIPLES_COMPONENT=IDENTITY',
 'R504_EVEN_MULTIPLES_ARE_QUARTIC_IMAGES=false',
 'R504_ALL_PHYSICAL_MULTIPLES_ODD_LEMMA_MATERIALIZED=true',
 'R504_FIRST_NONDEGENERATE_PHYSICAL_MULTIPLE_INDEX=3',
 'R504_ALL_MULTIPLES_COUNT_UPPER=O(B^(1/9)*sqrt(log B))']:
    assert marker in r504, marker

# Normative policy is restored exactly on the rejected dimensions.
for marker in [
 'STATUS=NORMATIVE_FOR_STAGE25_60_CONTINUATION',
 'remaining open items require genuinely new external mathematics, not another unexecuted repo-native mutation.',
 'R504_EXCEPTIONAL_BASE_CHANGE_RESIDUAL=LIVE_EXPLICIT_CURVE_SEARCH',
 'CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false',
 'STAGE70_ALLOWED=false']:
    assert marker in policy, marker
assert 'reduced to an exact external/new-parametric theorem gate' not in policy

# Prior hostile FAIL is durable.
for marker in ['AUDIT_VERDICT=FAIL','R504_STANDARD_Q_KUMMER_IDENTIFICATION_ACCEPTED=false','CONTINUATION_POLICY_SELF_RELAXATION_ACCEPTED=false']:
    assert marker in reaudit

assert ctl['iteration']=='R504_RESIDUAL_REAUDIT_REPAIR_2'
assert ctl['status']=='REPAIR_SUBMITTED_FOR_FRESH_AUDIT'
assert ctl['audit_status']=='PENDING'
assert ctl['advance_allowed'] is False and ctl['next_checkpoint']==60
assert ctl['merge_allowed'] is False and ctl['stage70_allowed'] is False
assert ctl['repair_2']['normative_stop_rule_restored'] is True
assert ctl['repair_2']['policy_change_submitted'] is False
assert ctl['repair_2']['standard_q_kummer_identification_asserted'] is False
assert ctl['repair_2']['all_physical_multiples_odd_lemma_materialized'] is True
assert ctl['repair_2']['exceptional_base_change_residual']=='LIVE_EXPLICIT_CURVE_SEARCH'
assert ctl['deep_stop_rule_satisfied'] is False
assert ctl['next_expected_command']=='Stage25-audit'

print(f'R505_R506_IDENTITY_ROWS={rows}')
print('R504_SAFE_Q_KUMMER_CLASS=PASS')
print('R504_REAL_COMPONENT_PARITY_LEMMA=PASS')
print('R504_GROWING_MULTIPLE_REPAIR=PASS')
print('NORMATIVE_STOP_RULE_RESTORED=PASS')
print('R504_EXCEPTIONAL_BASE_CHANGE_RESIDUAL=LIVE')
print('STAGE25_60_REPAIR_2=SUBMITTED_FOR_FRESH_AUDIT')
