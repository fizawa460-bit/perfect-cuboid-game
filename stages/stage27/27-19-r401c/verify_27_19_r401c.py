#!/usr/bin/env python3
from pathlib import Path
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


def add(p, q):
    n = max(len(p), len(q))
    out = [0] * n
    for i in range(n):
        out[i] = (p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0)
    return trim(out)


def scale(p, c):
    return trim([c*x for x in p])


def mul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i+j] += x*y
    return trim(out)


def derivative(p):
    return trim([i*p[i] for i in range(1, len(p))])


def det_bareiss(mat):
    A = [row[:] for row in mat]
    n = len(A)
    if n == 0:
        return 1
    sign = 1
    prev = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            swap = next((i for i in range(k + 1, n) if A[i][k] != 0), None)
            if swap is None:
                return 0
            A[k], A[swap] = A[swap], A[k]
            sign *= -1
        pivot = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j]*pivot - A[i][k]*A[k][j]) // prev
        prev = pivot
        for i in range(k + 1, n):
            A[i][k] = 0
    return sign * A[-1][-1]


def resultant_asc(p, q):
    p, q = trim(p), trim(q)
    f, g = p[::-1], q[::-1]
    m, n = len(f)-1, len(g)-1
    size = m+n
    M = [[0]*size for _ in range(size)]
    for i in range(n):
        for j, c in enumerate(f):
            M[i][i+j] = c
    for i in range(m):
        for j, c in enumerate(g):
            M[n+i][i+j] = c
    return det_bareiss(M)


def disc_asc(p):
    p = trim(p)
    n = len(p)-1
    assert n >= 1
    res = resultant_asc(p, derivative(p))
    sign = -1 if (n*(n-1)//2) % 2 else 1
    return sign * res // p[-1]


def receiver_factors(a, b):
    # ascending coefficients in tau
    u = [b, a]
    u2 = mul(u, u)
    A = add(u2, [1, 1])
    Q = add(add(mul([2, 1], u2), scale(mul([1, 1], u), -4)), [2, 3, 1])
    H = [0] + mul(A, Q)
    return trim(A), trim(Q), trim(H)


def F(a, b):
    return (
        16*a**4 - 32*a**3*b + 20*a*a*b*b - 32*a*a*b + 44*a*a
        - 4*a*b**3 + 32*a*b*b - 44*a*b - b*b + 6*b - 1
    )


def expected_disc(a, b):
    return (
        1024*a**6*(a-b)**6*(b-1)**6*(b*b+1)**2
        *(4*a*a-4*a*b-1)*F(a, b)
    )


parent_audit = text('stages/stage27/27-19-r401b/audit.md')
res = text('stages/stage27/27-19-r401c/result.md')
reg = data('stages/stage27/27-19-r401c/affine-linear-registry.json')
ctl = data('stages/stage27/27-controller.json')
status = text('docs/00_CURRENT_RESEARCH_STATUS.md')

assert 'AUDIT_VERDICT=PASS' in parent_audit
assert 'CONSTANT_U_NONDEGENERATE_GENUS_ONE_ACCEPTED=true' in parent_audit
assert 'NEXT_DERIVED_ROUTE=27-19-r401c' in parent_audit

# The direct sextic discriminant identity has deg_a<=18 and deg_b<=20.
# Checking a 19 x 21 grid of distinct rational/integer values certifies the
# bivariate polynomial identity. We use 19 nonzero a-values so the affine
# polynomial retains degree six.
alist = list(range(-10, 0)) + list(range(1, 10))
blist = list(range(-10, 11))
assert len(alist) == 19 and len(blist) == 21
for a in alist:
    for b in blist:
        A, Q, H = receiver_factors(a, b)
        assert len(H)-1 == 6
        assert H[-1] == a**4
        assert disc_asc(H) == expected_disc(a, b)

# Component identities used in the proof.
for a in range(-12, 13):
    assert F(a, a) == -a*a + 6*a - 1
    assert F(a, 1) == 4*(2*a*a - 2*a + 1)**2

# CA cap CQ resultant in a: 256*(2b-11)^2.  The left side has degree <=2
# in b, so three values suffice; use several for regression margin.
for b in [-4, -1, 0, 2, 7, 11]:
    # CA = 4a^2-4ba-1, ascending in a.
    CA = [-1, -4*b, 4]
    # F as a-polynomial, ascending coefficients.
    CQ = [
        -b*b + 6*b - 1,
        -4*b**3 + 32*b*b - 44*b,
        20*b*b - 32*b + 44,
        -32*b,
        16,
    ]
    assert resultant_asc(CA, CQ) == 256*(2*b-11)**2

# Rational pairwise-intersection firewalls.
# a=b with F=0 gives a^2-6a+1=0, discriminant 32.
assert 32 == 6**2 - 4
assert int(32**0.5)**2 != 32
# b=1 with CA=0 also has discriminant 32.
# b=1 with F=0 gives 2a^2-2a+1=0, discriminant -4.
# CA cap CQ forces b=11/2 and then 4a^2-22a-1=0, discriminant 500.
assert int(500**0.5)**2 != 500

for marker in [
    'AFFINE_LINEAR_RECEIVER_DERIVED=true',
    'AFFINE_LINEAR_GENERIC_GENUS=2',
    'AFFINE_LINEAR_DISCRIMINANT_FACTORIZATION_PROVED=true',
    'AFFINE_LINEAR_SINGLE_DEGENERATION_GENUS=1',
    'ALL_AFFINE_LINEAR_MULTISECTIONS_CLASSIFIED=true',
    'AFFINE_LINEAR_PHYSICAL_GENUS_ZERO_ROUTE_EXISTS=false',
    'LOWER_EXPONENT_ABOVE_ONE_QUARTER_PROVED=false',
    'NEXT_DERIVED_ROUTE=27-19-r401d',
    'NEXT_EXPECTED_COMMAND=Stage27-19-r401-audit',
]:
    assert marker in res, marker

assert reg['generic']['degree'] == 6
assert reg['generic']['genus'] == 2
assert reg['codimension_one']['single_degeneration_genus'] == 1
assert reg['rational_intersections']['only_simultaneous_moving_point'] == [1, 1]
assert reg['rational_intersections']['physical'] is False
assert reg['firewalls']['all_affine_linear_multisections_classified'] is True
assert reg['firewalls']['lower_exponent_above_one_quarter_proved'] is False

pb = ctl['derived_routes']['Stage27-19-r401b']
pc = ctl['derived_routes']['Stage27-19-r401c']
assert pb['status'] == 'INTERMEDIATE_AUDITED_PASS_MERGED'
assert pb['audit_status'] == 'PASS'
assert pb['pr'] == 1033
assert pb['merge_commit'] == 'dcc04e4d778aaaa31f9abb0d39dd98117c33ddb4'
assert pc['status'] == 'SUBMITTED_PENDING_FRESH_AUDIT'
assert pc['all_affine_linear_multisections_classified'] is True
assert pc['affine_linear_physical_genus_zero_route_exists'] is False
assert pc['lower_exponent_above_one_quarter_proved'] is False
assert pc['audit_status'] == 'PENDING'
assert ctl['state']['CURRENT_CHECKPOINT'] == 40
assert ctl['state']['AUDIT_STATUS'] == 'PENDING'
assert ctl['state']['MERGE_ALLOWED'] is False
assert ctl['next_expected_command'] == 'Stage27-19-r401-audit'
assert 'CURRENT_STAGE=Stage27-19-r401c-SUBMITTED-PENDING-FRESH-AUDIT' in status
assert 'STAGE27_19_R401B_STATUS=INTERMEDIATE_AUDITED_PASS_MERGED_PR1033' in status
assert 'STAGE27_19_R401C_STATUS=AFFINE_LINEAR_SUBMITTED_PENDING_FRESH_AUDIT' in status

print('STAGE27_19_R401C_PARENT_SYNC=PASS')
print('STAGE27_19_R401C_SEXTIC_DISCRIMINANT=PASS')
print('STAGE27_19_R401C_COMPONENT_INTERSECTIONS=PASS')
print('STAGE27_19_R401C_PHYSICAL_GENUS_ZERO_FIREWALL=PASS')
print('STAGE27_19_R401C_LIFECYCLE=PASS')
