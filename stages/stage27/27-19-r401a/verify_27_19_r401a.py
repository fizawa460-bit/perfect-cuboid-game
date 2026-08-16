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


def det_bareiss(mat):
    a = [row[:] for row in mat]
    n = len(a)
    if n == 0:
        return 1
    sign = 1
    prev = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            swap = next((i for i in range(k + 1, n) if a[i][k] != 0), None)
            assert swap is not None
            a[k], a[swap] = a[swap], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * pivot - a[i][k] * a[k][j]) // prev
        prev = pivot
        for i in range(k + 1, n):
            a[i][k] = 0
        for j in range(k + 1, n):
            a[k][j] = a[k][j]
    return sign * a[-1][-1]


def resultant(f, g):
    # coefficients highest degree first
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


def quartic_coeffs(t):
    # G_t(u)=(u^2+t+1)*((t+2)u^2-4(t+1)u+(t+1)(t+2))
    return [
        t + 2,
        -4 * (t + 1),
        2 * t * t + 6 * t + 4,
        -4 * (t + 1) * (t + 1),
        (t + 1) * (t + 1) * (t + 2),
    ]


def quartic_disc(t):
    f = quartic_coeffs(t)
    a, b, c, d, e = f
    fp = [4*a, 3*b, 2*c, d]
    return resultant(f, fp) // a


parent_audit = text('stages/stage27/27-19-r401/audit.md')
res = text('stages/stage27/27-19-r401a/result.md')
reg = data('stages/stage27/27-19-r401a/torsor-registry.json')
ctl = data('stages/stage27/27-controller.json')
status = text('docs/00_CURRENT_RESEARCH_STATUS.md')

assert 'AUDIT_VERDICT=PASS' in parent_audit
assert 'LOWER_PROGRESS_GATE=kappa/h>1/4' in parent_audit

# Master split identity.
for x, y, z in [(2, 3, 5), (7, 4, 3), (Fraction(5, 2), Fraction(7, 3), Fraction(11, 5))]:
    lhs = (x*x-z*z)*(y*y-z*z)
    rhs = x*x*y*y + 1 - z*z*(x*x+y*y) + (z**4 - 1)
    assert lhs == rhs

# First-conic parameterization and induced y^2 identity on exact rational samples.
for tau, u in [(Fraction(3, 2), Fraction(7, 3)), (Fraction(5, 3), Fraction(11, 4)), (Fraction(-2, 3), Fraction(5, 2))]:
    assert tau not in (0, -1)
    D = u*u - tau - 1
    assert D != 0
    z = (tau + (u-1)*(u-1)) / D
    x = (2*tau*u - tau - u*u + 2*u - 1) / D
    assert x*x == (tau+1)*z*z - tau
    y2_from_split = z*z + (z*z+1)/tau
    q = (tau+2)*u*u - 4*(tau+1)*u + (tau+1)*(tau+2)
    y2_from_quartic = (u*u+tau+1)*q / (tau*D*D)
    assert y2_from_split == y2_from_quartic

# Exact quartic discriminant on several nonsingular and singular fibers.
for tau in [-5, -3, -2, 1, 2, 3, 7]:
    assert quartic_disc(tau) == 4096 * tau*tau * (tau+1)**8
assert quartic_disc(0) == 0
assert quartic_disc(-1) == 0

# Binary-quartic invariant formulas, checked numerically.
for tau in [-3, -2, 1, 2, 5]:
    a,b,c,d,e = quartic_coeffs(tau)
    I = 12*a*e - 3*b*d + c*c
    J = 72*a*c*e + 9*b*c*d - 27*a*d*d - 27*b*b*e - 2*c*c*c
    assert I == 16*(tau+1)**2*(tau*tau+tau+1)
    assert J == 64*(tau-1)*(tau+1)**3*(tau+2)*(2*tau+1)

# Tau-adic parity skeleton used by the proof.
# At tau=0, G_0(u)=2(u^2+1)(u-1)^2.
for u in [-4, -1, 0, 1, 2, 5]:
    a,b,c,d,e = quartic_coeffs(0)
    G0 = a*u**4+b*u**3+c*u*u+d*u+e
    assert G0 == 2*(u*u+1)*(u-1)**2
# For u=1+a*tau, the tau^2 coefficient of the second factor is positive over Q.
for a in [Fraction(-3,2), Fraction(-1,1), Fraction(0,1), Fraction(1,2), Fraction(2,1), Fraction(7,3)]:
    lead = 1 - 2*a + 2*a*a
    assert lead == ((2*a-1)**2 + 1) / 2
    assert lead > 0

for marker in [
    'MASTER_SPLIT_FACTORIZATION_PROVED=true',
    'PHYSICAL_GENERIC_FIBER_GENUS=1',
    'TAU_ADIC_LOCAL_OBSTRUCTION_PROVED=true',
    'GENERIC_FIBER_QTAU_POINT_EXISTS=false',
    'GENERIC_RATIONAL_SECTION_EXISTS=false',
    'DEGREE1_SECTION_ROUTE_CLOSED=true',
    'GENERIC_DEGREE2_CLOSED_POINT_EXHIBITED=true',
    'LOWER_EXPONENT_ABOVE_ONE_QUARTER_PROVED=false',
    'NEXT_DERIVED_ROUTE=27-19-r401b',
    'NEXT_EXPECTED_COMMAND=Stage27-19-r401-audit',
]:
    assert marker in res, marker

assert reg['generic_fiber']['genus'] == 1
assert reg['generic_fiber']['smooth_on_physical_chart'] is True
assert reg['local_obstruction']['Q_tau_rational_point_exists'] is False
assert reg['local_obstruction']['rational_section_exists'] is False
assert reg['degree_two_escape']['generic_degree2_closed_point_exhibited'] is True
assert reg['firewalls']['master_surface_rationality_disproved'] is False
assert reg['firewalls']['lower_exponent_above_one_quarter_proved'] is False

parent = ctl['derived_routes']['Stage27-19-r401']
child = ctl['derived_routes']['Stage27-19-r401a']
assert parent['status'] == 'INTERMEDIATE_AUDITED_PASS_MERGED'
assert parent['audit_status'] == 'PASS'
assert parent['pr'] == 1031
assert parent['merge_commit'] == '05e8768872d69770bc02f42f3324039dab8f5e9b'
assert child['status'] == 'SUBMITTED_PENDING_FRESH_AUDIT'
assert child['generic_rational_section_exists'] is False
assert child['lower_exponent_above_one_quarter_proved'] is False
assert child['audit_status'] == 'PENDING'
assert ctl['state']['CURRENT_CHECKPOINT'] == 40
assert ctl['state']['AUDIT_STATUS'] == 'PENDING'
assert ctl['state']['MERGE_ALLOWED'] is False
assert ctl['next_expected_command'] == 'Stage27-19-r401-audit'
assert 'CURRENT_STAGE=Stage27-19-r401a-SUBMITTED-PENDING-FRESH-AUDIT' in status
assert 'STAGE27_19_R401_STATUS=INTERMEDIATE_AUDITED_PASS_MERGED_PR1031' in status
assert 'STAGE27_19_R401A_STATUS=GENUS_ONE_TORSOR_SUBMITTED_PENDING_FRESH_AUDIT' in status

print('STAGE27_19_R401A_SPLIT_FACTOR=PASS')
print('STAGE27_19_R401A_GENUS_ONE=PASS')
print('STAGE27_19_R401A_LOCAL_OBSTRUCTION=PASS')
print('STAGE27_19_R401A_NO_SECTION=PASS')
print('STAGE27_19_R401A_LIFECYCLE=PASS')
