#!/usr/bin/env python3
from fractions import Fraction
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]

def text(path):
    return (ROOT / path).read_text(encoding='utf-8')

def data(path):
    return json.loads(text(path))

res = text('stages/stage27/27-19-r402/result.md')
reg = data('stages/stage27/27-19-r402/tau-pushforward-registry.json')

for marker in [
    'TASK_ID=Stage27-19-r402',
    'ROUTE_KIND=UPPER_REENTRY',
    'TAU_SURVIVOR_IDENTITY_PROVED=true',
    'TAU_TORIC_FORMULA_PROVED=true',
    'TAU_DEFINED_BEFORE_SPACE_FILTER=true',
    'TAU_COLLISION_RECEIVER_DERIVED=true',
    'TAU_SUPPORT_POLYNOMIAL_LOWER_PROVED=true',
    'TAU_MAX_FIBER_UPPER_GATE=sigma+phi<1/2',
    'TAU_SECOND_MOMENT_UPPER_GATE=sigma+eta<1',
    'STRICT_SUB_SQRT_UPPER_PROVED=false',
    'ADVANCE_TO_CHECKPOINT50=false',
    'NEXT_EXPECTED_COMMAND=Stage27-19-r402-audit',
]:
    assert marker in res, marker

# Exact rational checks of the algebraic identity.  z2 is defined from the
# master receiver, so no square-root choice is needed.
for x in [Fraction(3,2), Fraction(5,3), Fraction(7,4), Fraction(9,5)]:
    for y in [Fraction(4,3), Fraction(5,2), Fraction(7,3), Fraction(8,5)]:
        x2, y2 = x*x, y*y
        z2 = (x2*y2 + 1) / (x2 + y2)
        assert z2 != 1
        tau_fibration = (x2 - z2) / (z2 - 1)
        tau_host = (x2 + 1) / (y2 - 1)
        assert tau_fibration == tau_host

# Exact check of toric substitution and homogeneous invariance.
for m,n,r,s in [(3,2,5,3), (5,2,7,4), (7,3,8,5), (9,4,11,6)]:
    x = Fraction(m,n)
    y = Fraction(r,s)
    tau_xy = (x*x + 1) / (y*y - 1)
    tau_toric = Fraction(s*s*(m*m+n*n), n*n*(r*r-s*s))
    assert tau_xy == tau_toric
    lam, mu = 3, 5
    tau_scaled = Fraction((mu*s)**2*((lam*m)**2+(lam*n)**2),
                          (lam*n)**2*((mu*r)**2-(mu*s)**2))
    assert tau_scaled == tau_toric
    assert tau_toric > 0

# Collision receiver: cross multiplication is exactly equality of reduced
# rational tau values.
def tau(t):
    m,n,r,s = t
    return Fraction(s*s*(m*m+n*n), n*n*(r*r-s*s))

def collision_lhs(a,b):
    m1,n1,r1,s1 = a
    m2,n2,r2,s2 = b
    return s1*s1*(m1*m1+n1*n1)*n2*n2*(r2*r2-s2*s2)

def collision_rhs(a,b):
    m1,n1,r1,s1 = a
    m2,n2,r2,s2 = b
    return s2*s2*(m2*m2+n2*n2)*n1*n1*(r1*r1-s1*s1)

pts = [(3,2,5,3), (5,2,7,4), (7,3,8,5), (9,4,11,6)]
for a in pts:
    for b in pts:
        assert (tau(a) == tau(b)) == (collision_lhs(a,b) == collision_rhs(a,b))

assert reg['task_id'] == 'Stage27-19-r402'
assert reg['tau']['host_identity'] == '(x^2+1)/(y^2-1)'
assert reg['tau']['defined_before_space_filter'] is True
assert reg['known_family_calibration']['R501_tau_projection_degree'] == 8
assert reg['known_family_calibration']['R502_tau_projection_degree'] == 8
assert reg['known_family_calibration']['tau_support_polynomial_lower_proved'] is True
assert reg['upper_gates']['support_max_fiber']['strict_subhalf_gate'] == 'sigma+phi<1/2'
assert reg['upper_gates']['support_second_moment']['strict_subhalf_gate'] == 'sigma+eta<1'
assert reg['proved']['strict_sub_sqrt_upper'] is False
assert reg['firewalls']['tau_cardinality_alone_promoted_to_power_saving'] is False
assert reg['firewalls']['known_lower_support_promoted_to_upper_support_bound'] is False

# Canonical lifecycle: r401d is accepted+merged; r402 is the active pending
# upper reentry at checkpoint40.
ctl = data('stages/stage27/27-controller.json')
status = text('docs/00_CURRENT_RESEARCH_STATUS.md')
pd = ctl['derived_routes']['Stage27-19-r401d']
p2 = ctl['derived_routes']['Stage27-19-r402']
assert pd['status'] == 'INTERMEDIATE_AUDITED_PASS_MERGED'
assert pd['audit_status'] == 'PASS'
assert pd['pr'] == 1036
assert pd['merge_commit'] == 'b37bc86e045175238bf2520518b059574addc52b'
assert p2['status'] == 'SUBMITTED_PENDING_FRESH_AUDIT'
assert p2['trigger_checkpoint'] == 40
assert p2['route_kind'] == 'UPPER_REENTRY'
assert p2['tau_defined_before_space_filter'] is True
assert p2['tau_support_polynomial_lower_proved'] is True
assert p2['tau_support_lower_exponent'] == '1/4'
assert p2['tau_max_fiber_upper_gate'] == 'sigma+phi<1/2'
assert p2['tau_second_moment_upper_gate'] == 'sigma+eta<1'
assert p2['strict_sub_sqrt_upper_proved'] is False
assert p2['audit_status'] == 'PENDING'
assert p2['merge_allowed'] is False
assert ctl['state']['CURRENT_CHECKPOINT'] == 40
assert ctl['state']['AUDIT_STATUS'] == 'PENDING'
assert ctl['state']['MERGE_ALLOWED'] is False
assert ctl['next_expected_command'] == 'Stage27-19-r402-audit'
assert 'CURRENT_STAGE=Stage27-19-r402-SUBMITTED-PENDING-FRESH-AUDIT' in status
assert 'STAGE27_19_R401D_STATUS=INTERMEDIATE_AUDITED_PASS_MERGED_PR1036' in status
assert 'STAGE27_19_R402_STATUS=TAU_PUSHFORWARD_UPPER_SUBMITTED_PENDING_FRESH_AUDIT' in status
assert 'STAGE27_TAU_DEFINED_BEFORE_SPACE_FILTER=true' in status
assert 'STAGE27_TAU_SUPPORT_POLYNOMIAL_LOWER_PROVED=true' in status
assert 'NEXT_EXPECTED_COMMAND=Stage27-19-r402-audit' in status

print('STAGE27_19_R402_TAU_IDENTITY=PASS')
print('STAGE27_19_R402_TORIC_FORMULA=PASS')
print('STAGE27_19_R402_COLLISION_RECEIVER=PASS')
print('STAGE27_19_R402_UPPER_GATES=PASS')
print('STAGE27_19_R402_LIFECYCLE=PASS')
