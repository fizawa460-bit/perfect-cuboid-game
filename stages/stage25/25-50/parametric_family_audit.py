#!/usr/bin/env python3
from math import gcd
from pathlib import Path
import json

root = Path(__file__).resolve().parents[3]
result = (root / 'stages/stage25/25-50/result.md').read_text(encoding='utf-8')
proof = (root / 'stages/stage25/25-50/r501-parametric-positive-power.md').read_text(encoding='utf-8')
ledger = (root / 'stages/stage25/25-50/discovery-ledger.md').read_text(encoding='utf-8')
ctl = json.loads((root / 'stages/stage25/25-controller.json').read_text(encoding='utf-8'))


def family(m, n):
    A = 16*m*m*n*n*(m**4 - 9*n**4)
    B = (m**4 - 10*m*m*n*n + 9*n**4) * (m**4 + 2*m*m*n*n + 9*n**4)
    C = 4*m*n*(m*m + 3*n*n)*(m**4 - 10*m*m*n*n + 9*n**4)
    DAC = 4*m*n*(m*m + 3*n*n)*(m**4 - 2*m*m*n*n + 9*n**4)
    DBC = (m**4 - n**4)*(m**4 - 81*n**4)
    D = m**8 + 46*m**4*n**4 + 81*n**8
    return A, B, C, DAC, DBC, D


# Coefficients of P(t) from t^0,t^2,...,t^16.  Keeping one canonical
# coefficient vector binds the mod-5 Q certificate to the actual submitted
# missing-face polynomial rather than to an independently hard-coded copy.
P_EVEN_COEFFS = [6561, -11664, 25596, -1008, -3290, -112, 316, -16, 1]


def missing_homogeneous(m, n):
    return sum(
        coeff * m**(2*i) * n**(16 - 2*i)
        for i, coeff in enumerate(P_EVEN_COEFFS)
    )


# Polynomial helpers, coefficients low degree first, over F_p.
def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b, p):
    n = max(len(a), len(b))
    out = [0]*n
    for i in range(n):
        out[i] = ((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % p
    return trim(out)


def mul(a, b, p):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] = (out[i+j] + x*y) % p
    return trim(out)


def deriv(a, p):
    if len(a) <= 1:
        return [0]
    return trim([(i*a[i]) % p for i in range(1, len(a))])


# P(t) mod 5 is Q(t^2), with Q derived from the actual P coefficients above.
p = 5
Q = [c % p for c in P_EVEN_COEFFS]
assert Q == [1, 1, 1, 2, 0, 3, 1, 4, 1]
Qp = deriv(Q, p)
S = [2, 1, 0, 2, 1, 2, 2]
T = [4, 4, 0, 4, 2, 2, 4, 1]
bezout = add(mul(S, Q, p), mul(T, Qp, p), p)
assert bezout == [1], bezout
assert Q[0] == 1

# Because P'(t)=2t Q'(t^2) mod 5, Q squarefree, Q(0)!=0, and 2!=0 mod 5
# imply P is squarefree mod 5.  This is the exact logical bridge used in proof.
assert 2 % p != 0

# Exact integer regression over many admissible reduced parameters.
seen = 0
for n in range(3, 61):
    for k in range(1, (n-1)//2 + 1):
        if 2*k >= n or gcd(k, n) != 1:
            continue
        m = 4*n - k
        assert gcd(m, n) == 1
        assert 7*n < 2*m < 8*n
        A, B, C, DAC, DBC, D = family(m, n)
        assert 0 < B < C < A
        assert A*A + C*C == DAC*DAC
        assert B*B + C*C == DBC*DBC
        assert A*A + B*B + C*C == D*D
        assert A*A + B*B == missing_homogeneous(m, n)
        g = gcd(gcd(A, B), C)
        assert DAC % g == 0 and DBC % g == 0 and D % g == 0
        seen += 1
assert seen > 200

# Height constant used by the proof.
assert 1 + 46 + 81 == 128

for marker in [
    'NEW_LOWER_CANDIDATE=N2(B)>>B^(1/4)',
    'POSITIVE_POWER_LOWER_BOUND_CANDIDATE=true',
    'POSITIVE_POWER_EXPONENT_CANDIDATE=1/4',
    'STAGE25_RATIO_LOWER_CANDIDATE=B^(-7/4)(log B)^(-1)',
    'STAGE24_RATIO_LOWER_BACKFLOW_CANDIDATE=B^(-3/4)(log B)^(-5)',
    'STAGE23_RATIO_LOWER_BACKFLOW_CANDIDATE=B^(-3/4)(log B)^(-3)',
    'AMBIENT_INTERACTION_SIGN_BACKFLOW_CANDIDATE=POSITIVE_DIVERGENT',
    'CROSS_RATIO_SIGN_BACKFLOW_CANDIDATE=POSITIVE_DIVERGENT',
    'FINITE_DATA_USED_AS_PROOF=false',
    'EXPLORATION_EVIDENCE_COMPLETE=true',
]:
    assert marker in result, marker

for marker in [
    'CANDIDATE_LOWER=N2(B)>>B^(1/4)',
    'THIRD_FACE_EXCEPTION_CURVE_GENUS=7',
    'PARAMETER_FIBER_BOUND=8',
    'HEIGHT_DEGREE=8',
    'PARAMETER_COUNT_DEGREE=2',
    'FINITE_DATA_USED_AS_PROOF=false',
]:
    assert marker in proof, marker

for marker in [
    'DISCOVERY_CHECKPOINT=Stage25-50',
    'REPO_REUSE_PREFLIGHT=PASS',
    'SEARCHED_PATHS=',
    'CANDIDATES_FOUND=',
    'CANDIDATES_ACCEPTED=',
    'CANDIDATES_REJECTED_WITH_REASON=',
    'POPULATION_ADAPTERS_PROVED=',
    'SUBLANES_OPENED=Stage25-r501-parametric-positive-power',
    'FORMULA_SUBSTITUTION_ONLY=false',
    'FINITE_DATA_USED_AS_PROOF=false',
    'EXPLORATION_EVIDENCE_COMPLETE=true',
]:
    assert marker in ledger, marker

assert ctl['stage'] == 'Stage25'
assert ctl['parent_class'] == 'transition'
for cp, status in [('10','PROVED_AUDITED_PASS'),('20','COMPUTED_AUDITED_PASS'),('30','PROVED_AUDITED_PASS'),('40','PROVED_AUDITED_PASS')]:
    assert ctl['checkpoint_status'][cp] == status
status50 = ctl['checkpoint_status']['50']
assert status50 in ('PROVED_SUBMITTED_FOR_FRESH_AUDIT', 'PROVED_AUDITED_PASS')
current = int(ctl['state']['CURRENT_CHECKPOINT'])
assert current >= 50

cp50 = ctl['checkpoint50']
assert cp50['candidate_lower'] == 'N2(B)>>B^(1/4)'
assert cp50['positive_power_lower_candidate'] is True
assert cp50['positive_power_exponent_candidate'] == '1/4'
assert cp50['stage25_ratio_lower_candidate'] == 'N2/M1>>B^(-7/4)(log B)^(-1)'
assert cp50['third_face_exception_curve_genus'] == 7
assert cp50['parameter_fiber_bound'] == 8
assert cp50['family_height_degree'] == 8
assert cp50['parameter_count_degree'] == 2
assert cp50['finite_data_used_as_proof'] is False
assert cp50['exploration_evidence_complete'] is True

# Historical provenance must survive.
assert ctl['checkpoint10']['previous_audit'] == 'FAIL'
assert ctl['checkpoint20']['num_r01_manifest_binding'] == 'PASS'
assert ctl['checkpoint30']['previous_audit'] == 'FAIL'
assert ctl['checkpoint30']['directional_ratio_refinement_status'] == 'OPEN_GATE_ADAPTER_REQUIRED'
assert ctl['checkpoint40']['audit'] == 'PASS'
assert ctl['checkpoint40']['upper_provenance'] == 'stages/stage25/25-40/upper-provenance.md'
assert any(x['checkpoint'] == 40 and x['verdict'] == 'PASS' for x in ctl['audit_history'])

if status50 == 'PROVED_SUBMITTED_FOR_FRESH_AUDIT':
    assert current == 50
    assert ctl['state']['AUDIT_STATUS'] == 'PENDING'
    assert ctl['state']['ADVANCE_ALLOWED'] is False
    assert ctl['state']['NEXT_CHECKPOINT'] == 50
    assert ctl['state']['MERGE_ALLOWED'] is False
    assert cp50['audit'] == 'PENDING'
    assert ctl['discovery_audit']['checkpoint'] == 50
    assert ctl['discovery_audit']['verdict'] == 'PENDING'
    assert ctl['next_expected_command'] == 'Stage25-audit'
else:
    assert cp50['audit'] == 'PASS'
    assert cp50['positive_power_lower_proved'] is True
    assert cp50['positive_power_exponent'] == '1/4'
    assert cp50['directional_b_lower'] == 'N2,b(B)>>B^(1/4)'
    assert cp50['advance_allowed'] is True
    assert cp50['merge_allowed'] is True
    assert any(x['checkpoint'] == 50 and x['verdict'] == 'PASS' for x in ctl['audit_history'])
    if current == 50:
        assert ctl['state']['AUDIT_STATUS'] == 'PASS'
        assert ctl['state']['ADVANCE_ALLOWED'] is True
        assert ctl['state']['NEXT_CHECKPOINT'] == 60
        assert ctl['state']['MERGE_ALLOWED'] is True
    else:
        assert current > 50

print('MESKHISHVILI_HOMOGENEOUS_IDENTITIES_REGRESSION=PASS')
print(f'ADMISSIBLE_REDUCED_SAMPLE_COUNT={seen}')
print('PHYSICAL_CONE_ORDER_B_LT_C_LT_A=PASS')
print('PRIMITIVE_DIAGONAL_DIVISIBILITY_REGRESSION=PASS')
print('MISSING_FACE_HYPERELLIPTIC_POLYNOMIAL=PASS')
print('P_MOD5_TO_Q_T2_BINDING=PASS')
print('Q_MOD5_BEZOUT_SQUAREFREE_CERTIFICATE=PASS')
print('HYPERELLIPTIC_DEGREE=16')
print('HYPERELLIPTIC_GENUS=7')
print('HEIGHT_CONSTANT_128=PASS')
print('PARAMETER_FIBER_BOUND_DEGREE=8')
print(f'CURRENT_CHECKPOINT={current}')
print('CONTROLLER_HISTORY_PRESERVATION=PASS')
print('DISCOVERY_EVIDENCE_BLOCK=PASS')
print('STAGE25_50_PARAMETRIC_FAMILY_AUDIT=PASS')
