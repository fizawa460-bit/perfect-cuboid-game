#!/usr/bin/env python3
from fractions import Fraction
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]

# Exact fixed-tau conic identity on arbitrary positive reduced toric samples.
samples = [
    (5, 2, 7, 3),
    (7, 3, 11, 4),
    (8, 3, 13, 5),
    (9, 4, 14, 5),
]
for m, n, r, s in samples:
    x = Fraction(m, n)
    y = Fraction(r, s)
    tau = Fraction(s*s*(m*m+n*n), n*n*(r*r-s*s))
    p, q = tau.numerator, tau.denominator
    assert Fraction(p)*y*y - Fraction(q)*x*x == p + q
    assert p*n*n*(r*r-s*s) == q*s*s*(m*m+n*n)

# Recheck the parent r401a first-conic parametrization for rational values.
for t, u in [(Fraction(2, 3), Fraction(5, 2)),
             (Fraction(3, 2), Fraction(7, 3)),
             (Fraction(5, 4), Fraction(9, 5))]:
    D = u*u - t - 1
    assert D != 0
    z = (t + (u-1)*(u-1)) / D
    x = (2*t*u - t - u*u + 2*u - 1) / D
    assert x*x == (t+1)*z*z - t

reg = json.loads((ROOT / 'stages/stage27/27-19-r402b/fixed-tau-fiber-registry.json').read_text())
assert reg['fixed_tau']['ambient_conic'] == 'p*y^2-q*x^2=p+q'
assert reg['fixed_tau']['stage19_fiber_genus'] == 1
assert reg['physical_height_transfer']['z_height_bound'] == 'H(z)<3B'
assert reg['physical_height_transfer']['u_height_bound'] == 'H(u)<5B^(3/2)'
assert reg['pointwise_fiber']['subpower_proved'] is True
assert reg['pointwise_fiber']['uniform_in_t'] is False
assert reg['pointwise_fiber']['uniform_max_fiber_subpower_proved'] is False
assert reg['upper_route']['fiber_alone_strict_subhalf_route_closed'] is True
assert reg['upper_route']['strict_sub_sqrt_upper_proved'] is False
assert reg['next']['derived_route'] == '27-19-r402c'

result = (ROOT / 'stages/stage27/27-19-r402b/result.md').read_text()
for marker in [
    'POINTWISE_FIXED_TAU_SUBPOWER_PROVED=true',
    'UNIFORM_IN_T=false',
    'TAU_UNIFORM_FIBER_SUBPOWER_PROVED=false',
    'POINTWISE_TO_UNIFORM_PROMOTION_FORBIDDEN=true',
    'FIBER_ALONE_STRICT_SUBHALF_ROUTE_CLOSED=true',
    'STRICT_SUB_SQRT_UPPER_PROVED=false',
    'NEXT_DERIVED_ROUTE=27-19-r402c',
]:
    assert marker in result, marker

ctl = json.loads((ROOT / 'stages/stage27/27-controller.json').read_text())
r402a = ctl['derived_routes']['Stage27-19-r402a']
assert r402a['status'] == 'INTERMEDIATE_AUDITED_PASS_MERGED'
assert r402a['audit_status'] == 'PASS'
assert r402a['pr'] == 1038
assert r402a['merge_commit'] == 'e94dd7652c1c60cc32617ff00240f67734d39bed'

r402b = ctl['derived_routes']['Stage27-19-r402b']
assert r402b['status'] == 'SUBMITTED_PENDING_FRESH_AUDIT'
assert r402b['route_kind'] == 'UPPER_REENTRY'
assert r402b['parent_route'] == 'Stage27-19-r402a'
assert r402b['fixed_tau_ambient_conic_derived'] is True
assert r402b['fixed_tau_stage19_fiber_genus'] == 1
assert r402b['pointwise_fixed_tau_subpower_proved'] is True
assert r402b['tau_uniform_fiber_subpower_proved'] is False
assert r402b['fiber_alone_strict_subhalf_route_closed'] is True
assert r402b['strict_sub_sqrt_upper_proved'] is False
assert r402b['audit_status'] == 'PENDING'
assert r402b['merge_allowed'] is False
assert r402b['next_derived_route'] == '27-19-r402c'

state = ctl['state']
assert state['CURRENT_CHECKPOINT'] == 40
assert state['AUDIT_STATUS'] == 'PENDING'
assert state['ADVANCE_ALLOWED'] is False
assert state['NEXT_CHECKPOINT'] == 40
assert state['MERGE_ALLOWED'] is False
assert ctl['next_expected_command'] == 'Stage27-19-r402-audit'

status = (ROOT / 'docs/00_CURRENT_RESEARCH_STATUS.md').read_text()
for marker in [
    'STAGE27_19_R402A_STATUS=INTERMEDIATE_AUDITED_PASS_MERGED_PR1038',
    'STAGE27_19_R402B_STATUS=FIXED_TAU_FIBER_SUBMITTED_PENDING_FRESH_AUDIT',
    'STAGE27_POINTWISE_FIXED_TAU_SUBPOWER_PROVED=true',
    'STAGE27_TAU_UNIFORM_FIBER_SUBPOWER_PROVED=false',
    'STAGE27_FIBER_ALONE_STRICT_SUBHALF_ROUTE_CLOSED=true',
    'STAGE27_STRICT_SUB_SQRT_UPPER_PROVED=false',
    'NEXT_EXPECTED_COMMAND=Stage27-19-r402-audit',
]:
    assert marker in status, marker

print('Stage27-19-r402b verifier: PASS')
