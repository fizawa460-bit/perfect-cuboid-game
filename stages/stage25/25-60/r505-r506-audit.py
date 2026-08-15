#!/usr/bin/env python3
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import json

root = Path(__file__).resolve().parents[3]
r504 = (root/'stages/stage25/25-60/r504-base-change-boundary.md').read_text(encoding='utf-8')
r505 = (root/'stages/stage25/25-60/r505-common-core-gate.md').read_text(encoding='utf-8')
r506 = (root/'stages/stage25/25-60/r506-common-leg-subsumption.md').read_text(encoding='utf-8')
ledger = (root/'stages/stage25/25-60/r505-r506-discovery-ledger.md').read_text(encoding='utf-8')
audit = (root/'stages/stage25/25-60/r505-r506-audit.md').read_text(encoding='utf-8')
reaudit = (root/'stages/stage25/25-60/r505-r506-audit-recheck.md').read_text(encoding='utf-8')
ctl = json.loads((root/'stages/stage25/25-60/r505-r506-iteration-controller.json').read_text(encoding='utf-8'))


def sf(n):
    assert n > 0
    out = 1
    p = 2
    while p*p <= n:
        parity = 0
        while n % p == 0:
            n //= p
            parity ^= 1
        if parity:
            out *= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out *= n
    return out


def is_square(n):
    r = isqrt(n)
    return r*r == n


def toric(m,n,r,s):
    E = 4*m*n*r*s
    X = 2*r*s*(m*m-n*n)
    Y = 2*m*n*(r*r-s*s)
    HX = 2*r*s*(m*m+n*n)
    HY = 2*m*n*(r*r+s*s)
    A = m*m*r*r + n*n*s*s
    B = m*m*s*s + n*n*r*r
    return E,X,Y,HX,HY,A,B

# Previously hostile-audit accepted R505/R506 mathematics stays live.
rows = 0
space_rows = 0
for n in range(1,18):
    for m in range(n+1,31):
        if gcd(m,n) != 1: continue
        for s in range(1,14):
            for r in range(s+1,23):
                if gcd(r,s) != 1: continue
                E,X,Y,HX,HY,A,B = toric(m,n,r,s)
                assert E*E + X*X == HX*HX
                assert E*E + Y*Y == HY*HY
                assert E*E + X*X + Y*Y == 4*A*B
                same = sf(A) == sf(B)
                assert same == is_square(A*B)
                if same:
                    k=sf(A)
                    assert is_square(A//k) and is_square(B//k)
                    space_rows += 1
                u=m*r; v=n*s; w=m*s; z=n*r
                assert u*v == w*z
                assert A == u*u+v*v and B == w*w+z*z
                assert Fraction(u,z)==Fraction(w,v)==Fraction(m,n)
                assert Fraction(u,w)==Fraction(z,v)==Fraction(r,s)
                rows += 1
assert rows > 10000 and space_rows > 0

# Binary quartic invariants / j.
def quartic_IJ(a,b,c,d,e):
    I = 12*a*e - 3*b*d + c*c
    J = 72*a*c*e + 9*b*c*d - 27*a*d*d - 27*b*b*e - 2*c**3
    return I,J

def quartic_j(a,b,c,d,e):
    I,J=quartic_IJ(a,b,c,d,e)
    Delta=Fraction(4*I**3-J**2,27)
    assert Delta != 0
    return Fraction(256*I**3,Delta)

assert quartic_j(1,0,0,0,1) == 1728
assert quartic_j(1,0,-4,0,2) == 8000
assert quartic_j(1,0,4,0,2) == 8000
assert quartic_j(1,-4,22,-4,1) == 10976
assert quartic_j(1,0,-8,0,32) == 10976
assert quartic_j(1,0,0,0,16) == 1728

# finite-field traces for the submitted BC1/BC2 non-isogeny certificates.
def count_poly_curve_mod_p(coeffs,p):
    total=2
    for x in range(p):
        rhs=0
        for a in coeffs:
            rhs=(rhs*x+a)%p
        total += sum((y*y-rhs)%p==0 for y in range(p))
    return total

def count_E0(p):
    total=1
    for x in range(p):
        rhs=(x**3-4*x)%p
        total += sum((y*y-rhs)%p==0 for y in range(p))
    return total

assert count_E0(3) == 4
assert count_poly_curve_mod_p([1,0,-4,0,2],3) == 2
assert count_poly_curve_mod_p([1,0,4,0,2],3) == 6
assert count_poly_curve_mod_p([1,-4,22,-4,1],3) == 6
assert count_poly_curve_mod_p([1,0,-8,0,32],3) == 6

# BC1 quotient identities.
for u in [Fraction(2),Fraction(3,2),Fraction(5,3),Fraction(7,4)]:
    f=u**8+1
    xp=u+1/u
    xm=u-1/u
    lhs=f/u**4
    assert lhs == xp**4-4*xp**2+2
    assert lhs == xm**4+4*xm**2+2

# BC2 Cayley identities.
for u in [Fraction(2),Fraction(3,2),Fraction(5,3),Fraction(7,4)]:
    k=(u*u-1)/(2*u)
    N=u**8-4*u**6+22*u**4-4*u**2+1
    assert 16*u**4*(k**4+1) == N
    lhs=N/u**4
    xp=u+1/u
    xm=u-1/u
    assert lhs == xp**4-8*xp**2+32
    assert lhs == xm**4+16

# Physical-height identities used in the submitted growing-multiple argument.
for p in range(2,9):
    for q in range(1,p):
        for kn,kd in [(2,1),(3,2),(5,3)]:
            k=Fraction(kn,kd); t=Fraction(q,p)
            HX=k*k*p*p+q*q
            X=k*k*p*p-q*q
            HY=k*k*q*q+p*p
            Y=k*k*q*q-p*p
            assert (HX-X)/(HX+X) == (t/k)**2
            assert (HY+Y)/(HY-Y) == (k*t)**2

# Mandatory reuse/discovery handoff repair is present.
for marker in [
    'REPO_REUSE_PREFLIGHT=PASS',
    'REUSE_SEARCH_SCOPE=',
    'REUSED_RESULTS=',
    'REUSE_MATCH_STATUS=MIXED',
    'STRONGEST_KNOWN_CHECK=PASS',
    'STRONGER_PRIOR_RESULT_FOUND=false',
    'NEW_RESEARCH_JUSTIFIED=',
    'POPULATION_ADAPTERS_PROVED=',
    'DISCOVERY_LEDGER_STATUS=COMPLETE_REPAIRED_FOR_FRESH_AUDIT',
    'R504_DEGREE2_GENERAL_GATE=EXTRA_E0_FACTOR_IN_JACOBIAN_OF_C_phi',
    'R505_EXACT_TARGET_RECEIVER_ACCEPTED=true',
    'R506_TORIC_SUBSUMPTION_ACCEPTED=true',
]: assert marker in ledger, marker

# Submission claims remain mechanically bound even where re-audit rejects scope/wording.
for marker in [
    'R504_KUMMER_MODEL=Km(E0xE0)',
    'R504_BC1_STATUS=CLOSED_NO_RANK_JUMP',
    'R504_BC2_STATUS=CLOSED_NO_RANK_JUMP',
    'R504_RATIONAL_BASE_CHANGE_EQUIVALENT_TO_RATIONAL_MULTISECTION=true',
    'R504_GROWING_MULTIPLE_LATTES_DEGREE=n^2',
    'R504_ALL_MULTIPLES_COUNT_UPPER=O(B^(1/9)*sqrt(log B))',
    'R504_RESIDUAL_STATUS=EXTERNAL_OR_NEW_EXPLICIT_CURVE_GATE_SUBMITTED_FOR_FRESH_AUDIT',
]: assert marker in r504, marker

# Historical FAIL remains durable.
for marker in [
    'AUDIT_VERDICT=FAIL',
    'R505_EXACT_TARGET_RECEIVER_ACCEPTED=true',
    'R506_TORIC_SUBSUMPTION_ACCEPTED=true',
]: assert marker in audit, marker

# Re-audit rejection is explicit and narrow.
for marker in [
    'AUDIT_VERDICT=FAIL',
    'DISCOVERY_AUDIT_VERDICT=PASS',
    'REPO_REUSE_HANDOFF_COMPLETE=true',
    'R504_BC1_NO_RANK_JUMP_ACCEPTED=true',
    'R504_BC2_NO_RANK_JUMP_ACCEPTED=true',
    'R504_STANDARD_Q_KUMMER_IDENTIFICATION_ACCEPTED=false',
    'R504_ALL_PHYSICAL_MULTIPLES_ODD_LEMMA_MATERIALIZED=false',
    'R504_ALL_MULTIPLES_COUNT_UPPER_ACCEPTED=false',
    'CONTINUATION_POLICY_SELF_RELAXATION_ACCEPTED=false',
    'CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false',
    'STAGE70_ALLOWED=false',
]: assert marker in reaudit, marker

assert ctl['stage']=='Stage25' and ctl['checkpoint']==60
assert ctl['iteration']=='R504_RESIDUAL_R505_R506_BOUNDARY_REAUDIT'
assert ctl['status']=='AUDIT_FAIL_REPAIR_REQUIRED'
assert ctl['audit_status']=='FAIL'
assert ctl['advance_allowed'] is False
assert ctl['next_checkpoint']==60
assert ctl['merge_allowed'] is False
assert ctl['stage70_allowed'] is False
assert ctl['previous_hostile_audit_acceptance']['r505_exact_target_receiver'] is True
assert ctl['previous_hostile_audit_acceptance']['r506_toric_subsumption'] is True
assert ctl['repair_handoff']['reuse_handoff_materialized'] is True
assert ctl['repair_handoff']['discovery_evidence_block_complete'] is True
assert ctl['reaudit_acceptance']['r504_bc1_no_rank_jump'] is True
assert ctl['reaudit_acceptance']['r504_bc2_no_rank_jump'] is True
assert ctl['reaudit_acceptance']['r504_standard_q_kummer_identification'] is False
assert ctl['reaudit_acceptance']['r504_all_physical_multiples_odd_lemma_materialized'] is False
assert ctl['reaudit_acceptance']['r504_all_multiples_count_upper'] is False
assert ctl['reaudit_acceptance']['continuation_policy_self_relaxation'] is False
assert ctl['r504_residual']['deep_stop_class_accepted'] is False
assert ctl['deep_stop_rule_satisfied'] is False
assert ctl['continuation_policy_self_relaxation_accepted'] is False
assert ctl['next_expected_command']=='Stage25-main-batch'

print(f'R505_TORIC_IDENTITY_ROWS={rows}')
print(f'R505_SPACE_CORE_ROWS={space_rows}')
print('R505_R506_PREVIOUS_AUDIT_ACCEPTED_MATH=PASS')
print('R504_BC1_JACOBIAN_QUOTIENT_CERTIFICATE=PASS')
print('R504_BC2_JACOBIAN_QUOTIENT_CERTIFICATE=PASS')
print('R504_GROWING_MULTIPLE_PHYSICAL_HEIGHT_IDENTITY=PASS')
print('REPO_REUSE_HANDOFF_REPAIR=PASS')
print('STAGE25_60_HOSTILE_REAUDIT_STATE=FAIL_REPAIR_REQUIRED')
