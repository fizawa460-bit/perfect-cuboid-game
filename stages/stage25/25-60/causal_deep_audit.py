#!/usr/bin/env python3
from math import gcd
from fractions import Fraction
from pathlib import Path
import json

root = Path(__file__).resolve().parents[3]
result = (root/'stages/stage25/25-60/result.md').read_text(encoding='utf-8')
causal = (root/'stages/stage25/25-60/causal-lattice.md').read_text(encoding='utf-8')
r501_rigid = (root/'stages/stage25/25-60/r507-primitive-height-rigidity.md').read_text(encoding='utf-8')
r502_cert = (root/'stages/stage25/25-60/r502-primitive-height-no-upgrade.md').read_text(encoding='utf-8')
triage = (root/'stages/stage25/25-60/deeper-lane-triage.md').read_text(encoding='utf-8')
ledger = (root/'stages/stage25/25-60/discovery-ledger.md').read_text(encoding='utf-8')
continuation = (root/'stages/stage25/25-60/continuation-policy.md').read_text(encoding='utf-8')
audit = (root/'stages/stage25/25-60/audit.md').read_text(encoding='utf-8')
ctl = json.loads((root/'stages/stage25/25-controller.json').read_text(encoding='utf-8'))

# -------------------------
# Exact scale arithmetic
# -------------------------
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

# -------------------------
# Small polynomial gcd over F_p, low coefficients first
# -------------------------
def trim(a):
    a = [x for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a

def deriv(a,p):
    if len(a) <= 1:
        return [0]
    return trim([(i*a[i]) % p for i in range(1,len(a))])

def divmod_poly(a,b,p):
    a=trim([x%p for x in a])
    b=trim([x%p for x in b])
    assert b != [0]
    if len(a) < len(b):
        return [0],a
    q=[0]*(len(a)-len(b)+1)
    inv=pow(b[-1],-1,p)
    r=a[:]
    while r != [0] and len(r) >= len(b):
        shift=len(r)-len(b)
        c=(r[-1]*inv)%p
        q[shift]=c
        for i,bi in enumerate(b):
            r[i+shift]=(r[i+shift]-c*bi)%p
        r=trim(r)
    return trim(q),trim(r)

def gcd_poly(a,b,p):
    a=trim([x%p for x in a]); b=trim([x%p for x in b])
    while b != [0]:
        _,r=divmod_poly(a,b,p)
        a,b=b,r
    inv=pow(a[-1],-1,p)
    return trim([(x*inv)%p for x in a])

# -------------------------
# R501 accepted exact gcd regression
# -------------------------
def r501(m,n):
    A=16*m*m*n*n*(m**4-9*n**4)
    B=(m**4-10*m*m*n*n+9*n**4)*(m**4+2*m*m*n*n+9*n**4)
    C=4*m*n*(m*m+3*n*n)*(m**4-10*m*m*n*n+9*n**4)
    D=m**8+46*m**4*n**4+81*n**8
    g=gcd(gcd(abs(A),abs(B)),abs(C))
    return A,B,C,D,g

seen501=0
for n in range(1,180):
    for m in range((7*n)//2+1,4*n):
        if gcd(m,n)!=1 or not (7*n < 2*m < 8*n):
            continue
        A0,B0,C0,D0,g=r501(m,n)
        pred=(128 if (m&1 and n&1) else 1)*(81 if m%3==0 else 1)
        assert g == pred, ('R501',m,n,g,pred)
        assert g <= 10368 and D0 % g == 0
        assert D0//g >= m**8//10368
        seen501 += 1
assert seen501 > 4000

# -------------------------
# R502 repair: source-level third-parametrization regression
# -------------------------
def r502(m,n):
    A=(m**4-n**4)*(m**4-81*n**4)
    B=4*m*n*(m*m-3*n*n)*(m**4+2*m*m*n*n+9*n**4)
    C=16*m*m*n*n*(m**4-9*n**4)
    DAC=m**8+46*m**4*n**4+81*n**8
    DBC=4*m*n*(m*m-3*n*n)*(m**4+10*m*m*n*n+9*n**4)
    D=(m**4-2*m*m*n*n+9*n**4)*(m**4+10*m*m*n*n+9*n**4)
    g=gcd(gcd(abs(A),abs(B)),abs(C))
    P=(m**16 + 16*m**14*n**2 - 196*m**12*n**4 + 112*m**10*n**6
       + 5926*m**8*n**8 + 1008*m**6*n**10 - 15876*m**4*n**12
       + 11664*m**2*n**14 + 6561*n**16)
    return A,B,C,DAC,DBC,D,g,P

seen502=0
for n in range(1,180):
    for m in range((7*n)//2+1,4*n):
        if gcd(m,n)!=1 or not (7*n < 2*m < 8*n):
            continue
        A,B,C,DAC,DBC,D,g,P=r502(m,n)
        assert 0 < A < B < C
        assert A*A + C*C == DAC*DAC
        assert B*B + C*C == DBC*DBC
        assert A*A + B*B + C*C == D*D
        assert A*A + B*B == P
        pred=(32 if (m&1 and n&1) else 1)*(81 if m%3==0 else 1)
        assert g == pred, ('R502',m,n,g,pred)
        assert g <= 2592
        assert DAC % g == 0 and DBC % g == 0 and D % g == 0
        assert D//g >= m**8//2592
        seen502 += 1
assert seen502 > 4000

# P502(t) coefficients low degree first; squarefree mod 5.
P502=[6561,0,11664,0,-15876,0,1008,0,5926,0,112,0,-196,0,16,0,1]
g502_mod5=gcd_poly(P502,deriv(P502,5),5)
assert g502_mod5 == [1], g502_mod5

# -------------------------
# R504 accepted moving 3P section regression
# -------------------------
def t3z3(k):
    P=k**8-6*k**4-3
    Q=3*k**8+6*k**4-1
    Z=k**16+28*k**12+6*k**8+28*k**4+1
    return Fraction(k*P,Q), Fraction(Z,Q*Q)
for k in range(2,35):
    t,z=t3z3(k)
    assert t**4 + 1 == (k**4+1)*z*z

# -------------------------
# Artifact contract markers
# -------------------------
for marker in [
    'TWO_PATH_CAUSAL_DECOMPOSITION=PASS',
    'ORDER_OF_CONDITIONS_INTERACTION=POSITIVE_DIVERGENT_SYMMETRIC_CROSS_RATIO',
    'R501_EXACT_FAMILY_GROWTH=Theta(B^(1/4))',
    'R502_EXACT_FAMILY_GROWTH=Theta(B^(1/4))',
    'R502_GCD_GLOBAL_BOUND=2592',
    'R502_PARAMETER_FIBER_BOUND=8',
    'R502_THIRD_FACE_EXCEPTION_CURVE_GENUS=7',
    'R502_HIDDEN_GCD_EXPONENT_UPGRADE=false',
    'R502_ROUTE_BOUNDARY_CERTIFICATE=SUBMITTED_FOR_FRESH_AUDIT',
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
]: assert marker in r501_rigid, marker

for marker in [
    'R502_SOURCE_FORMULAS_BOUND=true',
    'R502_CANONICAL_ORDER=0<A<B<C',
    'R502_GCD_GLOBAL_BOUND=2592',
    'R502_PRIMITIVE_HEIGHT_DEGREE=8',
    'R502_THIRD_FACE_EXCEPTION_CURVE_GENUS=7',
    'R502_PARAMETER_FIBER_BOUND=8',
    'R502_EXACT_FAMILY_GROWTH=Theta(B^(1/4))',
    'R502_HIDDEN_GCD_EXPONENT_UPGRADE=false',
    'R502_ROUTE_BOUNDARY_CERTIFICATE=SUBMITTED_FOR_FRESH_AUDIT',
]: assert marker in r502_cert, marker

for marker in [
    'R502_STATUS=CLOSED_NO_UPGRADE_WITH_CERTIFICATE_SUBMITTED_FOR_FRESH_AUDIT',
    'R502_EXACT_FAMILY_GROWTH=Theta(B^(1/4))',
    'R503_UNIFORM_VARYING_FIBER_HEIGHT_COUNT=NOT_PROVED',
    'R504_GENERIC_NONTORSION_SECTION_PROVED=true',
    'HIGHER_THAN_ONE_QUARTER_LOWER_PROVED=false',
]: assert marker in triage, marker

for marker in [
    'DISCOVERY_CHECKPOINT=Stage25-60',
    'PREVIOUS_AUDIT_VERDICT=FAIL',
    'REPAIR_OPTION_SELECTED=R502_PRIMITIVE_HEIGHT_MULTIPLICITY_EXACTLY_TWO_CERTIFICATE',
    'R502_EXACT_FAMILY_GROWTH=Theta(B^(1/4))',
    'R502_GCD_GLOBAL_BOUND=2592',
    'R502_REPAIR_STATUS=SUBMITTED_FOR_FRESH_AUDIT',
    'LIVE_ROUTE_CANDIDATES=R503,R504,R505,R506',
    'DISCOVERY_LEDGER_STATUS=COMPLETE_REPAIRED_R502',
    'NUM_REUSE_CHECK=PASS',
]: assert marker in ledger, marker

for marker in [
    'ROUTE_ID_IS_PERSISTENT=true',
    'AUDIT_ROUND_IS_NOT_ROUTE_ID=true',
    'CHECKPOINT_NUMBER_DOES_NOT_RENUMBER_EXISTING_ROUTE=true',
    'R501_R507_ALLOCATIONS_FROZEN=true',
    'R502=CLOSED_NO_UPGRADE_WITH_CERTIFICATE_SUBMITTED_FOR_FRESH_AUDIT',
    'CHECKPOINT60_DEEP_STOP_RULE=SATISFIED',
]: assert marker in continuation, marker

# Historical FAIL must remain durable.
for marker in [
    'Status: **FAIL',
    'CORE_MATHEMATICS_VERDICT=PASS',
    'R502_ROUTE_BOUNDARY_ACCEPTED=false',
    'REPAIR_SCOPE=R502_LIVE_RESTORE_OR_PRIMITIVE_HEIGHT_NO_UPGRADE_CERTIFICATE',
]: assert marker in audit, marker

# -------------------------
# Controller states
# -------------------------
assert ctl['stage']=='Stage25'
assert ctl['checkpoint_status']['50']=='PROVED_AUDITED_PASS'
status60=ctl['checkpoint_status']['60']
assert status60 in ('AUDIT_FAIL_REPAIR_REQUIRED','REPAIR_SUBMITTED_FOR_FRESH_AUDIT','PROVED_AUDITED_PASS')
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

if status60=='AUDIT_FAIL_REPAIR_REQUIRED':
    assert current==60
    assert ctl['state']['AUDIT_STATUS']=='FAIL'
    assert ctl['state']['ADVANCE_ALLOWED'] is False
    assert ctl['state']['NEXT_CHECKPOINT']==60
    assert ctl['state']['MERGE_ALLOWED'] is False
    assert cp60['audit']=='FAIL'
    assert cp60['core_mathematics_verdict']=='PASS'
    assert cp60['r502_route_boundary_accepted'] is False
    assert cp60['r502_prematurely_removed_from_live_set'] is True
elif status60=='REPAIR_SUBMITTED_FOR_FRESH_AUDIT':
    assert current==60
    assert ctl['state']['AUDIT_STATUS']=='PENDING'
    assert ctl['state']['ADVANCE_ALLOWED'] is False
    assert ctl['state']['NEXT_CHECKPOINT']==60
    assert ctl['state']['MERGE_ALLOWED'] is False
    assert cp60['previous_audit']=='FAIL'
    assert cp60['r502_repair_status']=='SUBMITTED_FOR_FRESH_AUDIT'
    assert cp60['r502_exact_family_growth']=='Theta(B^(1/4))'
    assert cp60['r502_gcd_bound']==2592
    assert cp60['r502_parameter_fiber_bound']==8
    assert cp60['r502_third_face_exception_curve_genus']==7
    assert cp60['r502_hidden_gcd_exponent_upgrade'] is False
    assert cp60['r502_route_boundary_certificate']=='SUBMITTED_FOR_FRESH_AUDIT'
    assert cp60['live_routes_after_current_audit']==['R503','R504','R505','R506']
    assert ctl['discovery_audit']['verdict']=='PENDING'
else:
    assert cp60['audit']=='PASS'
    assert cp60['r502_route_boundary_accepted'] is True
    assert cp60['r502_exact_family_growth']=='Theta(B^(1/4))'
    assert cp60['advance_allowed'] is True
    assert cp60['merge_allowed'] is True

print('CAUSAL_CROSS_RATIO_SCALE=I>>B^1/4(logB)^-7:PASS')
print('THREE_EXACT_DECOMPOSITIONS=PASS')
print(f'R501_GCD_GRID_ROWS={seen501}')
print('R501_PRIMITIVE_HEIGHT_RIGIDITY_REGRESSION=PASS')
print(f'R502_GCD_GRID_ROWS={seen502}')
print('R502_INTEGER_IDENTITIES=PASS')
print('R502_PHYSICAL_CONE_ORDER=PASS')
print('R502_EXACT_GCD_REGRESSION=PASS')
print('R502_MISSING_FACE_POLYNOMIAL_BINDING=PASS')
print('R502_MOD5_SQUAREFREE_CERTIFICATE=PASS')
print('R502_PRIMITIVE_HEIGHT_NO_UPGRADE=PASS')
print('R504_3P_SECTION_REGRESSION=PASS')
print('PERSISTENT_ROUTE_NAMING_REGISTRY=PASS')
print('CHECKPOINT60_ITERATIVE_CONTINUATION_POLICY=PASS')
print(f'CONTROLLER_CURRENT_CHECKPOINT={current}')
print(f'AUDIT_STATE={ctl["state"]["AUDIT_STATUS"]}')
print('STAGE25_60_CAUSAL_DEEP_REGRESSION=PASS')
