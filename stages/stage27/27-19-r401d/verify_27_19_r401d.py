#!/usr/bin/env python3
from pathlib import Path
from fractions import Fraction
import json

ROOT = Path(__file__).resolve().parents[3]


def text(rel):
    p = ROOT / rel
    assert p.exists(), rel
    return p.read_text(encoding='utf-8')


def data(rel):
    return json.loads(text(rel))


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def pdeg(p):
    return len(trim(p)) - 1


def pdivmod(a, b):
    a = [Fraction(x) for x in trim(a)]
    b = [Fraction(x) for x in trim(b)]
    assert b != [0]
    q = [Fraction(0)] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and a != [0]:
        k = len(a) - len(b)
        c = a[-1] / b[-1]
        q[k] = c
        for j in range(len(b)):
            a[k+j] -= c * b[j]
        a = trim(a)
    return trim(q), trim(a)


def pgcd(a, b):
    a = [Fraction(x) for x in trim(a)]
    b = [Fraction(x) for x in trim(b)]
    while b != [0]:
        _, r = pdivmod(a, b)
        a, b = b, r
    lead = a[-1]
    return trim([x/lead for x in a])


def r501_edges(t):
    A = 16*t*t*(t**4-9)
    B = (t**4-10*t*t+9)*(t**4+2*t*t+9)
    C = 4*t*(t*t+3)*(t**4-10*t*t+9)
    return A, B, C


def r502_edges(t):
    A = (t**4-1)*(t**4-81)
    B = 4*t*(t*t-3)*(t**4+2*t*t+9)
    C = 16*t*t*(t**4-9)
    return A, B, C


def master(x, y, z):
    return x*x*y*y + 1 == z*z*(x*x+y*y)


def split_coords(x, z):
    tau = (x*x-z*z)/(z*z-1)
    u = (x-1)/(z-1)
    return tau, u


parent_audit = text('stages/stage27/27-19-r401c/audit.md')
res = text('stages/stage27/27-19-r401d/result.md')
reg = data('stages/stage27/27-19-r401d/calibration-registry.json')
assert 'AUDIT_VERDICT=PASS' in parent_audit
assert 'AFFINE_LINEAR_PHYSICAL_GENUS_ZERO_ROUTE_EXISTS=false' in parent_audit

# Universal toric identities on exact rational samples.
for P,Q,R,S in [(5,2,7,3),(11,4,13,5),(17,6,19,7)]:
    E = 4*P*Q*R*S
    X = 2*R*S*(P*P-Q*Q)
    Y = 2*P*Q*(R*R-S*S)
    assert E*E + X*X == (2*R*S*(P*P+Q*Q))**2
    assert E*E + Y*Y == (2*P*Q*(R*R+S*S))**2

# R501 exact embedding and toric reconstruction.
for t in [Fraction(7,2)+Fraction(1,10), Fraction(15,4), Fraction(39,10), Fraction(31,8)]:
    x = (t-1)*(t+3)/((t-3)*(t+1))
    y = (t*t+3)/(2*t)
    z = (t**4+2*t**3+2*t*t-6*t+9)/(t**4-2*t**3+2*t*t+6*t+9)
    assert master(x,y,z)
    tau,u = split_coords(x,z)
    tau_expected = 8*t*t*(t**4-2*t*t+9)/((t-3)**2*(t+1)**2*(t*t-2*t+3)*(t*t+2*t+3))
    u_expected = (t**4-2*t**3+2*t*t+6*t+9)/((t-3)*(t+1)*(t*t-3))
    assert tau == tau_expected
    assert u == u_expected

for m in range(4, 15):
    n = 1
    P=(m-n)*(m+3*n); Q=(m-3*n)*(m+n)
    R=m*m+3*n*n; S=2*m*n
    E=4*P*Q*R*S
    X=2*R*S*(P*P-Q*Q)
    Y=2*P*Q*(R*R-S*S)
    A=16*m*m*n*n*(m**4-9*n**4)
    B=(m**4-10*m*m*n*n+9*n**4)*(m**4+2*m*m*n*n+9*n**4)
    C=4*m*n*(m*m+3*n*n)*(m**4-10*m*m*n*n+9*n**4)
    assert (E,X,Y) == (2*C,2*A,2*B)

# R502 exact embedding and degree-12 -> degree-8 polynomial cancellation.
for t in [Fraction(18,5), Fraction(15,4), Fraction(39,10), Fraction(31,8)]:
    x = (t*t-3)*(t*t+3)/(8*t*t)
    y = (t*t+3)/(2*t)
    z = (t**4-2*t*t+9)/(2*t*(t*t+3))
    assert master(x,y,z)
    tau,u = split_coords(x,z)
    tau_expected = ((t**4-2*t**3+2*t*t+6*t+9)*(t**4+2*t**3+2*t*t-6*t+9))/(16*t*t*(t*t-2*t+3)*(t*t+2*t+3))
    u_expected = ((t+3)*(t*t+1)*(t*t+3))/(4*t*(t-1)*(t*t+2*t+3))
    assert tau == tau_expected
    assert u == u_expected

for m in range(4, 17):
    n = 1
    P=m**4-9*n**4; Q=8*m*m*n*n
    R=m*m+3*n*n; S=2*m*n
    E=4*P*Q*R*S
    X=2*R*S*(P*P-Q*Q)
    Y=2*P*Q*(R*R-S*S)
    A=(m**4-n**4)*(m**4-81*n**4)
    B=4*m*n*(m*m-3*n*n)*(m**4+2*m*m*n*n+9*n**4)
    C=16*m*m*n*n*(m**4-9*n**4)
    G=4*m*n*(m*m+3*n*n)
    assert (E,X,Y) == (G*C,G*A,G*B)

# Tau projection degrees and coprimality.
# ascending coefficient lists
r501_tau_num = [0,0,72,0,-16,0,8]
# denominator expanded mechanically from the displayed factorization
# use direct coefficient construction helper below instead of a hard-coded expansion.
def pmul(a,b):
    out=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=Fraction(x)*Fraction(y)
    return trim(out)

def ppow(a,k):
    out=[Fraction(1)]
    for _ in range(k): out=pmul(out,a)
    return out

r501_tau_den = pmul(pmul(ppow([-3,1],2),ppow([1,1],2)), pmul([3,-2,1],[3,2,1]))
r502_tau_num = pmul([9,6,2,-2,1],[9,-6,2,2,1])
r502_tau_den = [Fraction(16)*x for x in pmul([0,0,1],pmul([3,-2,1],[3,2,1]))]
assert pdeg(r501_tau_num) == 6 and pdeg(r501_tau_den) == 8
assert pdeg(r502_tau_num) == 8 and pdeg(r502_tau_den) == 6
assert pgcd(r501_tau_num,r501_tau_den) == [Fraction(1)]
assert pgcd(r502_tau_num,r502_tau_den) == [Fraction(1)]

for marker in [
    'R501_TAU_EMBEDDING_PROVED=true',
    'R502_TAU_EMBEDDING_PROVED=true',
    'R501_TAU_PROJECTION_DEGREE=8',
    'R502_TAU_PROJECTION_DEGREE=8',
    'R501_TORIC_DEGREE_LEDGER=dx2_dy2_g0_h8',
    'R502_TORIC_DEGREE_LEDGER=dx4_dy2_g4_h8',
    'R502_DEGREE12_TO_8_POLYNOMIAL_CANCELLATION_PROVED=true',
    'ONE_PARAMETER_ALGEBRAIC_PROGRESS_GATE=2dx+2dy-g<8',
    'LOWER_EXPONENT_ABOVE_ONE_QUARTER_PROVED=false',
    'LOWER_BOUNDED_REENTRY_STOP_CANDIDATE=true',
    'PREFERRED_POST_AUDIT_LANE=UPPER_REENTRY',
    'NEXT_UPPER_ROUTE=27-40af',
    'NEXT_EXPECTED_COMMAND=Stage27-19-r401-audit',
]:
    assert marker in res, marker

assert reg['R501']['tau_projection_degree'] == 8
assert reg['R501']['h_alg'] == 8
assert reg['R502']['tau_projection_degree'] == 8
assert reg['R502']['h_alg'] == 8
assert reg['R502']['common_polynomial_factor_degree'] == 4
assert reg['lower_stop_boundary']['bounded_reentry_stop_candidate'] is True
assert reg['lower_stop_boundary']['preferred_post_audit_lane'] == 'UPPER_REENTRY'
assert reg['lower_stop_boundary']['lower_exponent_above_one_quarter_proved'] is False



# Canonical lifecycle synchronization after first hostile audit.
ctl = data('stages/stage27/27-controller.json')
status = text('docs/00_CURRENT_RESEARCH_STATUS.md')
self_audit = text('stages/stage27/27-19-r401d/audit.md')
assert 'MATHEMATICAL_AUDIT=PASS' in self_audit
assert 'FAIL_REASON=STALE_R401C_PENDING_STATE_AND_MISSING_R401D_CANONICAL_REGISTRATION' in self_audit

pc = ctl['derived_routes']['Stage27-19-r401c']
pd = ctl['derived_routes']['Stage27-19-r401d']
assert pc['status'] == 'INTERMEDIATE_AUDITED_PASS_MERGED'
assert pc['audit_status'] == 'PASS'
assert pc['pr'] == 1035
assert pc['merge_commit'] == '4ca03c43f4ff2c858c51ac8959d6e75f077c6de7'
assert pd['status'] == 'REPAIR_SUBMITTED_PENDING_FRESH_AUDIT'
assert pd['r501_tau_projection_degree'] == 8
assert pd['r502_tau_projection_degree'] == 8
assert pd['r501_toric_degree_ledger'] == 'dx2_dy2_g0_h8'
assert pd['r502_toric_degree_ledger'] == 'dx4_dy2_g4_h8'
assert pd['r502_degree12_to_8_polynomial_cancellation_proved'] is True
assert pd['one_parameter_algebraic_progress_gate'] == '2dx+2dy-g<8'
assert pd['lower_bounded_reentry_stop_candidate'] is True
assert pd['previous_audit_verdict'] == 'FAIL'
assert pd['mathematical_audit_status'] == 'PASS'
assert pd['audit_status'] == 'PENDING'
assert pd['advance_to_checkpoint50'] is False
assert pd['merge_allowed'] is False
assert ctl['state']['CURRENT_CHECKPOINT'] == 40
assert ctl['state']['AUDIT_STATUS'] == 'PENDING'
assert ctl['state']['MERGE_ALLOWED'] is False
assert ctl['next_expected_command'] == 'Stage27-19-r401-audit'
assert 'CURRENT_STAGE=Stage27-19-r401d-REPAIR-SUBMITTED-PENDING-FRESH-AUDIT' in status
assert 'STAGE27_19_R401C_STATUS=INTERMEDIATE_AUDITED_PASS_MERGED_PR1035' in status
assert 'STAGE27_19_R401D_STATUS=R501_R502_CALIBRATION_REPAIR_SUBMITTED_PENDING_FRESH_AUDIT' in status
assert 'STAGE27_NEXT_UPPER_ROUTE=27-40af' in status

print('STAGE27_19_R401D_PARENT_AUDIT=PASS')
print('STAGE27_19_R401D_R501_EMBEDDING=PASS')
print('STAGE27_19_R401D_R502_EMBEDDING=PASS')
print('STAGE27_19_R401D_TAU_DEGREE=PASS')
print('STAGE27_19_R401D_HEIGHT_CALIBRATION=PASS')
print('STAGE27_19_R401D_LOWER_STOP_BOUNDARY=PASS')
