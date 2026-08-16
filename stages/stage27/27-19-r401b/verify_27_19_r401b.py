#!/usr/bin/env python3
from pathlib import Path
from fractions import Fraction
from math import isqrt
import json

ROOT = Path(__file__).resolve().parents[3]


def text(rel):
    p = ROOT / rel
    assert p.exists(), rel
    return p.read_text(encoding='utf-8')


def data(rel):
    return json.loads(text(rel))


def det_bareiss(mat):
    a = [row[:] for row in mat]
    n = len(a)
    sign = 1
    prev = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            swap = next((i for i in range(k + 1, n) if a[i][k] != 0), None)
            if swap is None:
                return 0
            a[k], a[swap] = a[swap], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * pivot - a[i][k] * a[k][j]) // prev
        prev = pivot
        for i in range(k + 1, n):
            a[i][k] = 0
    return sign * a[-1][-1]


def resultant(f, g):
    m, n = len(f) - 1, len(g) - 1
    size = m + n
    M = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(n):
        for j, c in enumerate(f):
            M[i][i + j] = c
    for i in range(m):
        for j, c in enumerate(g):
            M[n + i][i + j] = c
    return det_bareiss(M)


def H_coeffs(c):
    A = c*c + 1
    B = (c - 1) * (c - 3)
    C = 2 * (c - 1) * (c - 1)
    return [1, A + B, C + A*B, A*C, 0]


def quartic_disc(c):
    f = H_coeffs(c)
    a,b,d,e,f0 = f
    fp = [4*a, 3*b, 2*d, e]
    return resultant(f, fp)


parent_audit = text('stages/stage27/27-19-r401a/audit.md')
res = text('stages/stage27/27-19-r401b/result.md')
reg = data('stages/stage27/27-19-r401b/bisection-registry.json')
ctl = data('stages/stage27/27-controller.json')
status = text('docs/00_CURRENT_RESEARCH_STATUS.md')

assert 'AUDIT_VERDICT=PASS' in parent_audit
assert 'GENERIC_DEGREE2_CLOSED_POINT_EXHIBITED=true' in parent_audit
assert 'LOWER_EXPONENT_ABOVE_ONE_QUARTER_PROVED=false' in parent_audit

for c in range(-12, 13):
    got = quartic_disc(c)
    want = 64*c**6*(c-1)**6*(c*c+1)**2*(c*c-6*c+1)
    assert got == want, (c, got, want)

assert isqrt(32)**2 != 32
assert quartic_disc(0) == 0
assert quartic_disc(1) == 0
for c in [-9,-3,-1,2,3,4,7,11]:
    assert quartic_disc(c) != 0


def reconstruct(tau, u):
    D = u*u - tau - 1
    assert D != 0
    z = (tau + (u-1)*(u-1)) / D
    x = (2*tau*u - tau - u*u + 2*u - 1) / D
    return x, z, D


for tau in [Fraction(-5,2), Fraction(-3,2), Fraction(1,2), Fraction(2), Fraction(7,3)]:
    if tau != -1:
        x,z,_ = reconstruct(tau, Fraction(0))
        assert x == 1 and z == -1
    if tau != 0:
        x,z,_ = reconstruct(tau, Fraction(1))
        assert x == -1 and z == -1

for tau in [Fraction(-5,2), Fraction(-3,2), Fraction(1,2), Fraction(2), Fraction(7,3)]:
    u = tau + 1
    D = u*u - tau - 1
    if D == 0:
        continue
    x,z,_ = reconstruct(tau, u)
    assert z == 1
    G = (u*u+tau+1)*((tau+2)*u*u-4*(tau+1)*u+(tau+1)*(tau+2))
    assert tau*G == tau**3*(tau+1)**2*(tau+2)

for marker in [
    'R401A_U0_DEGREE2_POINT_PHYSICAL=false',
    'CONSTANT_U_BISECTION_RECEIVER_DERIVED=true',
    'CONSTANT_U_BISECTION_DISCRIMINANT_PROVED=true',
    'CONSTANT_U_NONDEGENERATE_GENUS_ONE=true',
    'CONSTANT_U_RATIONAL_GENUS_ZERO_PHYSICAL_ROUTE_EXISTS=false',
    'BOUNDARY_LINE_U_EQ_TAU_PLUS_1_PHYSICAL=false',
    'ALL_AFFINE_LINEAR_MULTISECTIONS_CLASSIFIED=false',
    'LOWER_EXPONENT_ABOVE_ONE_QUARTER_PROVED=false',
    'NEXT_DERIVED_ROUTE=27-19-r401c',
    'NEXT_EXPECTED_COMMAND=Stage27-19-r401-audit',
]:
    assert marker in res, marker

assert reg['constant_u_classification']['rational_degenerate_c'] == [0, 1]
assert reg['constant_u_classification']['c0_physical'] is False
assert reg['constant_u_classification']['c1_physical'] is False
assert reg['constant_u_classification']['all_rational_c_not_0_1_genus'] == 1
assert reg['parent_degree_two_point']['physical'] is False
assert reg['boundary_lines']['u_tau_plus_1_physical'] is False
assert reg['firewalls']['all_affine_linear_multisections_classified'] is False
assert reg['firewalls']['lower_exponent_above_one_quarter_proved'] is False

pa = ctl['derived_routes']['Stage27-19-r401a']
pb = ctl['derived_routes']['Stage27-19-r401b']
pc = ctl['derived_routes']['Stage27-19-r401c']
assert pa['status'] == 'INTERMEDIATE_AUDITED_PASS_MERGED'
assert pa['audit_status'] == 'PASS'
assert pa['pr'] == 1032
assert pa['merge_commit'] == '86b5428d42f7f4c7344bace93b067d580391d7ac'
assert pb['status'] == 'INTERMEDIATE_AUDITED_PASS_MERGED'
assert pb['audit_status'] == 'PASS'
assert pb['pr'] == 1033
assert pb['merge_commit'] == 'dcc04e4d778aaaa31f9abb0d39dd98117c33ddb4'
assert pb['r401a_u0_degree2_point_physical'] is False
assert pb['constant_u_nondegenerate_genus_one'] is True
assert pc['status'] == 'SUBMITTED_PENDING_FRESH_AUDIT'
assert pc['all_affine_linear_multisections_classified'] is True
assert pc['audit_status'] == 'PENDING'
assert ctl['state']['CURRENT_CHECKPOINT'] == 40
assert ctl['state']['AUDIT_STATUS'] == 'PENDING'
assert ctl['state']['MERGE_ALLOWED'] is False
assert ctl['next_expected_command'] == 'Stage27-19-r401-audit'
assert 'CURRENT_STAGE=Stage27-19-r401c-SUBMITTED-PENDING-FRESH-AUDIT' in status
assert 'STAGE27_19_R401B_STATUS=INTERMEDIATE_AUDITED_PASS_MERGED_PR1033' in status
assert 'STAGE27_19_R401C_STATUS=AFFINE_LINEAR_SUBMITTED_PENDING_FRESH_AUDIT' in status

print('STAGE27_19_R401B_PARENT_SYNC=PASS')
print('STAGE27_19_R401B_DISCRIMINANT=PASS')
print('STAGE27_19_R401B_PHYSICAL_DEGENERACY=PASS')
print('STAGE27_19_R401B_CONSTANT_U_GENUS=PASS')
print('STAGE27_19_R401B_SUCCESSOR_LIFECYCLE=PASS')
