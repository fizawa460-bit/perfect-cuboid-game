#!/usr/bin/env python3
from pathlib import Path
from math import gcd, isqrt
import json

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / 'stages/stage27/27-19-r402a/result.md'
REGISTRY = ROOT / 'stages/stage27/27-19-r402a/tau-height-registry.json'
PARENT_AUDIT = ROOT / 'stages/stage27/27-19-r402/audit.md'
CONTROLLER = ROOT / 'stages/stage27/27-controller.json'
STATUS = ROOT / 'docs/00_CURRENT_RESEARCH_STATUS.md'

result = RESULT.read_text(encoding='utf-8')
registry = json.loads(REGISTRY.read_text(encoding='utf-8'))
parent_audit = PARENT_AUDIT.read_text(encoding='utf-8')
controller = json.loads(CONTROLLER.read_text(encoding='utf-8'))
status = STATUS.read_text(encoding='utf-8')

# Parent route must be hostile-audited PASS and merged before r402a opens.
assert 'AUDIT_VERDICT=PASS' in parent_audit
assert registry['parent_pr'] == 1037
assert registry['parent_merge_commit'] == '77dc7bc7eb29f4113d59c8255ab4b2148bd52690'

# Exact elementary gcd lemma used in the proof.
for m in range(2, 50):
    for n in range(1, m):
        if gcd(m, n) != 1:
            continue
        assert gcd(2*m*n, m*m - n*n) <= 2

# Check the toric face identities, G bounds, and reduced tau-height inequality
# on a broad deterministic reduced-positive sample. The proof in result.md is
# algebraic; these checks guard transcription/sign/scaling mistakes.
checked = 0
for m in range(2, 18):
    for n in range(1, m):
        if gcd(m, n) != 1:
            continue
        for r in range(2, 18):
            for s in range(1, r):
                if gcd(r, s) != 1:
                    continue
                E = 4*m*n*r*s
                X = 2*r*s*(m*m - n*n)
                Y = 2*m*n*(r*r - s*s)
                G = gcd(gcd(E, X), Y)
                assert G <= 4*r*s
                assert G <= 4*m*n
                e, x, y = E//G, X//G, Y//G
                FXraw = 2*r*s*(m*m+n*n)
                FYraw = 2*m*n*(r*r+s*s)
                assert FXraw % G == 0
                assert FYraw % G == 0
                FX, FY = FXraw//G, FYraw//G
                assert FX*FX == e*e + x*x
                assert FY*FY == e*e + y*y
                R2 = e*e + x*x + y*y
                Rfloor = isqrt(R2)
                B = Rfloor if Rfloor*Rfloor == R2 else Rfloor + 1
                assert m*m + n*n < 2*B
                assert r*r + s*s < 2*B
                assert n*n < B
                assert s*s < B
                N0 = s*s*(m*m+n*n)
                D0 = n*n*(r*r-s*s)
                gt = gcd(N0, D0)
                p, q = N0//gt, D0//gt
                assert gcd(p, q) == 1
                assert max(p, q) < 2*B*B
                checked += 1
assert checked > 1000

required_result_markers = [
    'TAU_REDUCED_HEIGHT_BOUND_PROVED=true',
    'TAU_REDUCED_HEIGHT_BOUND=H(tau)<2B^2',
    'TAU_BEST_CERTIFIED_SUPPORT_UPPER=1/2_PLUS_EPSILON',
    'TAU_SUPPORT_STRICT_SUBHALF_PROVED=false',
    'HEIGHT_ONLY_SUPPORT_ROUTE_CLOSED=true',
    'STRICT_SUB_SQRT_UPPER_PROVED=false',
    'TRUE_N2_EXPONENT_IDENTIFIED=false',
    'NEXT_DERIVED_ROUTE=27-19-r402b',
    'AUDIT_STATUS=PENDING',
    'MERGE_ALLOWED=false',
]
for marker in required_result_markers:
    assert marker in result, marker

assert registry['tau']['reduced_height_bound'] == 'H(tau)<2B^2'
assert registry['support']['audited_lower_exponent'] == '1/4'
assert registry['support']['best_certified_upper'] == '1/2+epsilon'
assert registry['support']['strict_subhalf_proved'] is False
assert registry['support']['height_only_support_route_closed'] is True
assert registry['upper']['strict_sub_sqrt_upper_proved'] is False

r402 = controller['derived_routes']['Stage27-19-r402']
assert r402['audit_status'] == 'PASS'
assert r402['pr'] == 1037
assert r402['merge_commit'] == '77dc7bc7eb29f4113d59c8255ab4b2148bd52690'
r402a = controller['derived_routes']['Stage27-19-r402a']
assert r402a['status'] == 'SUBMITTED_PENDING_FRESH_AUDIT'
assert r402a['tau_reduced_height_bound_proved'] is True
assert r402a['tau_support_strict_subhalf_proved'] is False
assert r402a['height_only_support_route_closed'] is True
assert r402a['next_derived_route'] == '27-19-r402b'
assert r402a['audit_status'] == 'PENDING'
assert r402a['merge_allowed'] is False
assert controller['state']['CURRENT_CHECKPOINT'] == 40
assert controller['state']['ADVANCE_ALLOWED'] is False
assert controller['next_expected_command'] == 'Stage27-19-r402-audit'

for marker in [
    'STAGE27_19_R402_STATUS=INTERMEDIATE_AUDITED_PASS_MERGED_PR1037',
    'STAGE27_19_R402A_STATUS=TAU_HEIGHT_SUPPORT_SUBMITTED_PENDING_FRESH_AUDIT',
    'STAGE27_TAU_REDUCED_HEIGHT_BOUND=H_LT_2B2',
    'STAGE27_TAU_SUPPORT_STRICT_SUBHALF_PROVED=false',
    'STAGE27_HEIGHT_ONLY_SUPPORT_ROUTE_CLOSED=true',
    'NEXT_EXPECTED_COMMAND=Stage27-19-r402-audit',
]:
    assert marker in status, marker

print(f'Stage27-19-r402a verifier PASS ({checked} deterministic toric checks)')
