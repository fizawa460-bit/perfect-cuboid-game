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
ctl = json.loads((root/'stages/stage25/25-60/r505-r506-iteration-controller.json').read_text(encoding='utf-8'))


def sf(n):
    assert n > 0
    out = 1
    p = 2
    while p*p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e ^= 1
        if e:
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

# Exact Stage19 identities and the squarefree-core equivalence.
rows = 0
space_rows = 0
for n in range(1,18):
    for m in range(n+1,31):
        if gcd(m,n) != 1:
            continue
        for s in range(1,14):
            for r in range(s+1,23):
                if gcd(r,s) != 1:
                    continue
                E,X,Y,HX,HY,A,B = toric(m,n,r,s)
                assert E*E + X*X == HX*HX
                assert E*E + Y*Y == HY*HY
                assert E*E + X*X + Y*Y == 4*A*B
                same = sf(A) == sf(B)
                assert same == is_square(A*B)
                if same:
                    k = sf(A)
                    assert A % k == 0 and B % k == 0
                    assert is_square(A//k) and is_square(B//k)
                    P = isqrt(A//k); Q = isqrt(B//k)
                    assert A == k*P*P and B == k*Q*Q
                    space_rows += 1
                rows += 1
assert rows > 10000
assert space_rows > 0

# R506 coordinates are exactly rank-one coordinates for the same A,B.
rank_rows = 0
for n in range(1,13):
    for m in range(n+1,22):
        if gcd(m,n) != 1:
            continue
        for s in range(1,10):
            for r in range(s+1,18):
                if gcd(r,s) != 1:
                    continue
                u = m*r; v = n*s; w = m*s; z = n*r
                assert u*v == w*z
                _,_,_,_,_,A,B = toric(m,n,r,s)
                assert A == u*u + v*v
                assert B == w*w + z*z
                # Projective reconstruction ratios.
                assert Fraction(u,z) == Fraction(m,n)
                assert Fraction(w,v) == Fraction(m,n)
                assert Fraction(u,w) == Fraction(r,s)
                assert Fraction(z,v) == Fraction(r,s)
                rank_rows += 1
assert rank_rows > 3000

# Converse on arbitrary positive rational rank-one data generated without toric labels.
# Choose u,w,z and impose v=w*z/u; then recover the same two projective ratios.
conv_rows = 0
for u0 in range(2,19):
    for w0 in range(1,u0+1):
        for z0 in range(1,16):
            u=Fraction(u0); w=Fraction(w0); z=Fraction(z0)
            v=w*z/u
            assert u*v == w*z
            mn1=u/z; mn2=w/v
            rs1=u/w; rs2=z/v
            assert mn1 == mn2
            assert rs1 == rs2
            conv_rows += 1
assert conv_rows > 1000

# Artifact contracts.
for marker in [
    'R504_ORIGINAL_BASE_STATUS=AUDITED_CLOSED_NO_GLOBAL_UPGRADE',
    'R504_RESIDUAL_STATUS=EXTERNAL_THEOREM_GATE_SUBMITTED_FOR_FRESH_AUDIT',
    'R504_NEW_EXPLICIT_BASE_CHANGE_REOPENS_ROUTE=true',
    'R504_GLOBAL_LOWER_CHANGED=false',
]:
    assert marker in r504, marker

for marker in [
    'R505_EXACT_TARGET_RECEIVER=true',
    'R505_SPACE_CONDITION=sf(A)=sf(B)',
    'R505_COMMON_CORE=A=kP^2,B=kQ^2',
    'R505_RECEIVER_IS_NOT_CONSTRUCTION_BY_ITSELF=true',
    'R505_STAGE15_INTERNAL_ROUTE_SEARCH_REUSED=true',
    'R505_STATUS=EXTERNAL_THEOREM_GATE_SUBMITTED_FOR_FRESH_AUDIT',
    'GLOBAL_STAGE25_LOWER_CHANGED=false',
]:
    assert marker in r505, marker

for marker in [
    'R506_RANK_ONE_IDENTITY=uv=wz',
    'R506_A=u^2+v^2',
    'R506_B=w^2+z^2',
    'R506_TORIC_RECONSTRUCTION_PROJECTIVE_UNIQUE=true',
    'R506_INDEPENDENT_PARAMETER_DIMENSION=false',
    'R506_SUBSUMED_BY_R505_EXACT_TORIC_RECEIVER=true',
    'R506_STATUS=CLOSED_NO_INDEPENDENT_ROUTE_WITH_CERTIFICATE_SUBMITTED_FOR_FRESH_AUDIT',
]:
    assert marker in r506, marker

for marker in [
    'DISCOVERY_CHECKPOINT=Stage25-60-R505-R506',
    'REPO_REUSE_PREFLIGHT=PASS',
    'S1415-ATTACK-0724=',
    'S1415-ATTACK-0746=',
    'S1415-ATTACK-0753=',
    'S1415-ATTACK-0765=',
    'S1415-ATTACK-0770=',
    'S1415-ATTACK-0773=',
    'S1415-ATTACK-0784=',
    'R504_RESIDUAL=EXTERNAL_THEOREM_GATE_SUBMITTED_FOR_FRESH_AUDIT',
    'R505=EXTERNAL_THEOREM_GATE_SUBMITTED_FOR_FRESH_AUDIT',
    'R506=CLOSED_NO_INDEPENDENT_ROUTE_WITH_CERTIFICATE_SUBMITTED_FOR_FRESH_AUDIT',
    'CHECKPOINT60_DEEP_STOP_RULE_CANDIDATE=true',
    'CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false',
    'FINITE_DATA_USED_AS_PROOF=false',
]:
    assert marker in ledger, marker

assert ctl['stage'] == 'Stage25'
assert ctl['checkpoint'] == 60
assert ctl['iteration'] == 'R505_R506_BOUNDARY'
assert ctl['audit_status'] == 'PENDING'
assert ctl['advance_allowed'] is False
assert ctl['next_checkpoint'] == 60
assert ctl['merge_allowed'] is False
assert ctl['stage70_allowed'] is False
assert ctl['persistent_route_ids'] is True
assert ctl['r504_residual']['status'] == 'EXTERNAL_THEOREM_GATE_SUBMITTED_FOR_FRESH_AUDIT'
assert ctl['r505']['status'] == 'EXTERNAL_THEOREM_GATE_SUBMITTED_FOR_FRESH_AUDIT'
assert ctl['r505']['exact_target_receiver'] is True
assert ctl['r506']['status'] == 'CLOSED_NO_INDEPENDENT_ROUTE_WITH_CERTIFICATE_SUBMITTED_FOR_FRESH_AUDIT'
assert ctl['r506']['subsumed_by_r505_exact_toric_receiver'] is True
assert ctl['global_stage25_lower_changed'] is False
assert ctl['deep_stop_rule_candidate'] is True
assert ctl['deep_stop_rule_satisfied'] is False
assert ctl['deep_stop_pending_hostile_audit'] is True
assert ctl['finite_data_used_as_proof'] is False

print(f'R505_TORIC_IDENTITY_ROWS={rows}')
print(f'R505_SPACE_CORE_ROWS={space_rows}')
print('R505_SQUAREFREE_CORE_EQUIVALENCE=PASS')
print(f'R506_RANK_ONE_ROWS={rank_rows}')
print(f'R506_CONVERSE_PROJECTIVE_ROWS={conv_rows}')
print('R506_TORIC_SUBSUMPTION=PASS')
print('R504_RESIDUAL_BOUNDARY_ARTIFACT=PASS')
print('R505_STAGE15_REUSE_LEDGER=PASS')
print('CHECKPOINT60_DEEP_STOP_CANDIDATE_PENDING_AUDIT=PASS')
print('STAGE25_60_R505_R506_AUDIT=PASS')
