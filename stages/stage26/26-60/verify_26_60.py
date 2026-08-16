#!/usr/bin/env python3
from pathlib import Path
from math import gcd, isqrt
import json

ROOT = Path(__file__).resolve().parents[3]

def text(rel):
    p = ROOT / rel
    assert p.exists(), rel
    return p.read_text(encoding='utf-8')

def data(rel):
    return json.loads(text(rel))

def square_root(n):
    q = isqrt(n)
    assert q*q == n, n
    return q

def tau(n):
    out = 1
    p = 2
    while p*p <= n:
        if n % p == 0:
            a = 0
            while n % p == 0:
                n //= p
                a += 1
            out *= a + 1
        p += 1
    if n > 1:
        out *= 2
    return out

res = text('stages/stage26/26-60/result.md')
proof = text('stages/stage26/26-60/general-saunderson-proof.md')
reg = data('stages/stage26/26-60/lower-registry.json')
ctl = data('stages/stage26/26-controller.json')
a50 = text('stages/stage26/26-50/audit.md')

assert 'AUDIT_VERDICT=PASS' in a50
assert reg['upstream']['checkpoint50_pr'] == 1018
assert reg['upstream']['checkpoint50_merge_commit'] == '6775851010af3f7edc47a8383d6c30cb98be43c1'
assert reg['candidate_conclusions']['M3_lower_B_one_third_minus_epsilon'] is True
assert reg['general_saunderson']['global_injectivity_required'] is False
assert reg['firewalls']['M3_lower_B_one_third_without_epsilon_proved'] is False
assert reg['firewalls']['true_M3_exponent_identified'] is False
assert reg['firewalls']['M3_asymptotic_proved'] is False
assert reg['firewalls']['perfect_cuboid_conclusion'] == 'NONE'

outputs = {}
for r in range(2, 35):
    for s in range(1, r):
        if gcd(r, s) != 1 or (r - s) % 2 == 0:
            continue
        u = r*r - s*s
        v = 2*r*s
        w = r*r + s*s
        A = u * abs(4*v*v - w*w)
        B = v * abs(4*u*u - w*w)
        C = 4*u*v*w
        assert min(A, B, C) > 0
        assert gcd(gcd(A, B), C) == 1
        dAB = square_root(A*A + B*B)
        dAC = square_root(A*A + C*C)
        dBC = square_root(B*B + C*C)
        assert dAB == w**3
        assert dAC == u*(4*v*v + w*w)
        assert dBC == v*(4*u*u + w*w)
        assert A*A + B*B + C*C < (9*w**3)**2
        key = tuple(sorted((A, B, C)))
        outputs.setdefault(key, []).append((u, v, w))

for edges, preimages in outputs.items():
    x, y, z = edges
    face_diags = [square_root(x*x+y*y), square_root(x*x+z*z), square_root(y*y+z*z)]
    for _, _, w in preimages:
        assert w**3 in face_diags

for w in range(1, 80):
    n = w*w
    reps = 0
    lim = isqrt(n)
    for a in range(-lim, lim+1):
        b2 = n - a*a
        if b2 < 0:
            continue
        b = isqrt(b2)
        if b*b == b2:
            reps += 1 if b == 0 else 2
    assert reps <= 4*tau(n)

for T in (40, 80, 120):
    cnt = sum(1 for r in range(2, T+1) for s in range(1, r)
              if gcd(r, s) == 1 and (r-s) % 2 == 1)
    assert cnt > T*T/10

for marker in [
    'M_3(B)\\gg_\\epsilon B^{1/3-\\epsilon}',
    'GLOBAL_INJECTIVITY_CLAIMED=false',
    'DIVISOR_FIBER_BOUND_USED=true',
    'M3_LOWER_B_ONE_THIRD_WITHOUT_EPSILON_PROVED=false',
    'TRUE_M3_EXPONENT_IDENTIFIED=false',
    'UPPER_LOWER_MATCH=false',
    'PERFECT_CUBOID_CONCLUSION=NONE',
]:
    assert marker in res, marker

for marker in [
    'w^3',
    'r_2(w^2)',
    'tau(w^2)',
    'no global injectivity is claimed',
]:
    assert marker in proof, marker

assert ctl['checkpoint_status']['50'] == 'PROVED_AUDITED_PASS_MERGED'
assert ctl['checkpoint50']['pr'] == 1018
assert ctl['checkpoint50']['merge_commit'] == '6775851010af3f7edc47a8383d6c30cb98be43c1'
assert ctl['state']['CURRENT_CHECKPOINT'] == 60
assert ctl['state']['NEXT_CHECKPOINT'] == 70
c60 = ctl['checkpoint60']
assert c60['audit_status'] == 'PENDING'
assert ctl['checkpoint_status']['60'] == 'PROVED_SUBMITTED_PENDING_AUDIT'
assert ctl['state']['AUDIT_STATUS'] == 'PENDING'
assert ctl['state']['ADVANCE_ALLOWED'] is False
assert ctl['state']['MERGE_ALLOWED'] is False
assert ctl['next_expected_command'] == 'Stage26-audit'

print('STAGE26_60_GENERAL_SAUNDERSON_ALGEBRA=PASS')
print('STAGE26_60_PRIMITIVITY_HEIGHT=PASS')
print('STAGE26_60_CUBE_DIAGONAL_FIBER=PASS')
print('STAGE26_60_ONE_THIRD_MINUS_EPSILON_CANDIDATE=PASS')
print('STAGE26_60_FIREWALL=PASS')
