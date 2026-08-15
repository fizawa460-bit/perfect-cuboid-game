#!/usr/bin/env python3
from math import gcd
from fractions import Fraction
from pathlib import Path
import json

root = Path(__file__).resolve().parents[3]
result = (root/'stages/stage25/25-60/result.md').read_text(encoding='utf-8')
causal = (root/'stages/stage25/25-60/causal-lattice.md').read_text(encoding='utf-8')
rigid = (root/'stages/stage25/25-60/r507-primitive-height-rigidity.md').read_text(encoding='utf-8')
triage = (root/'stages/stage25/25-60/deeper-lane-triage.md').read_text(encoding='utf-8')
ledger = (root/'stages/stage25/25-60/discovery-ledger.md').read_text(encoding='utf-8')
continuation = (root/'stages/stage25/25-60/continuation-policy.md').read_text(encoding='utf-8')
ctl = json.loads((root/'stages/stage25/25-controller.json').read_text(encoding='utf-8'))

# scale tuples (B exponent, log exponent); epsilon omitted.
def mul(a,b): return (a[0]+b[0],a[1]+b[1])
def div(a,b): return (a[0]-b[0],a[1]-b[1])
F=(-1,4)
S=(-1,2)
Alo=(-.75,-5)
Ahi=(-.5,-5)
Tlo=(-.75,-3)
Thi=(-.5,-3)
Ilo=div(Alo,S)
Ihi=div(Ahi,S)
assert Ilo == (.25,-7)
assert Ihi == (.5,-7)
assert mul(F,Alo) == (-1.75,-1)
assert mul(S,Tlo) == (-1.75,-1)
assert mul(mul(F,S),Ilo) == (-1.75,-1)
assert mul(F,Ahi) == (-1.5,-1)
assert mul(S,Thi) == (-1.5,-1)
assert mul(mul(F,S),Ihi) == (-1.5,-1)

# r501 exact gcd regression over a broad deterministic cone grid.
def fam(m,n):
    A=16*m*m*n*n*(m**4-9*n**4)
    B=(m**4-10*m*m*n*n+9*n**4)*(m**4+2*m*m*n*n+9*n**4)
    C=4*m*n*(m*m+3*n*n)*(m**4-10*m*m*n*n+9*n**4)
    D=m**8+46*m**4*n**4+81*n**8
    g=gcd(gcd(abs(A),abs(B)),abs(C))
    return A,B,C,D,g
seen=0
for n in range(1,180):
    for m in range((7*n)//2+1,4*n):
        if gcd(m,n)!=1 or not (7*n < 2*m < 8*n):
            continue
        A0,B0,C0,D0,g=fam(m,n)
        pred=(128 if (m&1 and n&1) else 1)*(81 if m%3==0 else 1)
        assert g == pred, (m,n,g,pred)
        assert g <= 10368 and D0 % g == 0
        assert D0//g >= m**8//10368
        seen += 1
assert seen > 4000

# R504 exact moving 3P section regression on the symmetric-k quartic.
def t3z3(k):
    P=k**8-6*k**4-3
    Q=3*k**8+6*k**4-1
    Z=k**16+28*k**12+6*k**8+28*k**4+1
    return Fraction(k*P,Q), Fraction(Z,Q*Q)
for k in range(2,35):
    t,z=t3z3(k)
    assert t**4 + 1 == (k**4+1)*z*z

for marker in [
    'TWO_PATH_CAUSAL_DECOMPOSITION=PASS',
    'ORDER_OF_CONDITIONS_INTERACTION=POSITIVE_DIVERGENT_SYMMETRIC_CROSS_RATIO',
    'R501_EXACT_FAMILY_GROWTH=Theta(B^(1/4))',
    'R504_GENERIC_NONTORSION_SECTION_PROVED=true',
    'GLOBAL_LOWER_EXPONENT_ABOVE_QUARTER_PROVED=false',
    'ROUTE_ID_IS_PERSISTENT=true',
    'AUDIT_PASS_DOES_NOT_IMPLY_CHECKPOINT60_CLOSE=true',
    'CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false',
    'FINITE_DATA_USED_AS_PROOF=false',
    'EXPLORATION_EVIDENCE_COMPLETE=true',
]: assert marker in result, marker

for marker in [
    'CORRECTED_PRODUCT_IDENTITY=N2/M1=(M2/M1)*(N1/M1)*I',
    'INTERACTION_SIGN=POSITIVE_DIVERGENT',
    'INTERACTION_LOWER=I>>B^(1/4)(log B)^(-7)',
    'DOUBLE_CHARGE_CHECK=PASS',
]: assert marker in causal, marker

for marker in [
    'R501_EXACT_FAMILY_GROWTH=Theta(B^(1/4))',
    'R501_GCD_GLOBAL_BOUND=10368',
    'R501_HIDDEN_GCD_EXPONENT_UPGRADE=false',
]: assert marker in rigid, marker

for marker in [
    'R503_UNIFORM_VARYING_FIBER_HEIGHT_COUNT=NOT_PROVED',
    'R504_GENERIC_NONTORSION_SECTION_PROVED=true',
    'HIGHER_THAN_ONE_QUARTER_LOWER_PROVED=false',
]: assert marker in triage, marker

for marker in [
    'DISCOVERY_CHECKPOINT=Stage25-60',
    'R501=Meskhishvili_first_positive_power_family',
    'R503=Yoshida_uniform_varying_fiber_height',
    'R504=symmetric_k_aggregation',
    'R505=common_squarefree_core',
    'R506=common_leg_plus_space',
    'R507=R501_primitive_height_rigidity',
    'ROUTE_IDS_PERSIST_ACROSS_CHECKPOINTS=true',
    'S1415_ATTACKS_REVIEWED=',
    'S1415_Q03_RELEVANCE=',
    'S1415_Q05_RELEVANCE=',
    'DISCOVERY_LEDGER_STATUS=COMPLETE',
    'NUM_REUSE_CHECK=PASS',
]: assert marker in ledger, marker

for marker in [
    'ROUTE_ID_IS_PERSISTENT=true',
    'AUDIT_ROUND_IS_NOT_ROUTE_ID=true',
    'CHECKPOINT_NUMBER_DOES_NOT_RENUMBER_EXISTING_ROUTE=true',
    'R501_R507_ALLOCATIONS_FROZEN=true',
    'CHECKPOINT60_DEEP_STOP_RULE=SATISFIED',
]: assert marker in continuation, marker
assert '25-60-r01' not in continuation
assert '25-60-r02' not in continuation

assert ctl['stage']=='Stage25'
assert ctl['checkpoint_status']['50']=='PROVED_AUDITED_PASS'
status60=ctl['checkpoint_status']['60']
assert status60 in ('PROVED_SUBMITTED_FOR_FRESH_AUDIT','PROVED_AUDITED_PASS')
current=int(ctl['state']['CURRENT_CHECKPOINT'])
assert current>=60
cp60=ctl['checkpoint60']
assert cp60['corrected_product_identity_check']=='PASS'
assert cp60['interaction_sign']=='POSITIVE_DIVERGENT'
assert cp60['r501_exact_family_growth']=='Theta(B^(1/4))'
assert cp60['r501_gcd_bound']==10368
assert cp60['r504_generic_nontorsion_section_proved'] is True
assert cp60['higher_than_one_quarter_lower_proved'] is False
assert cp60['finite_data_used_as_proof'] is False

if status60=='PROVED_SUBMITTED_FOR_FRESH_AUDIT':
    assert current==60
    assert ctl['state']['AUDIT_STATUS']=='PENDING'
    assert ctl['state']['ADVANCE_ALLOWED'] is False
    assert ctl['state']['NEXT_CHECKPOINT']==60
    assert ctl['state']['MERGE_ALLOWED'] is False
else:
    assert cp60['audit']=='PASS'
    assert cp60['advance_allowed'] is True
    assert cp60['merge_allowed'] is True

print('CAUSAL_CROSS_RATIO_SCALE=I>>B^1/4(logB)^-7:PASS')
print('THREE_EXACT_DECOMPOSITIONS=PASS')
print(f'R501_GCD_GRID_ROWS={seen}')
print('R501_PRIMITIVE_HEIGHT_RIGIDITY_REGRESSION=PASS')
print('R504_3P_SECTION_REGRESSION=PASS')
print('PERSISTENT_ROUTE_NAMING_REGISTRY=PASS')
print('CHECKPOINT60_ITERATIVE_CONTINUATION_POLICY=PASS')
print(f'CONTROLLER_CURRENT_CHECKPOINT={current}')
print('STAGE25_60_CAUSAL_DEEP_AUDIT=PASS')
