#!/usr/bin/env python3
from pathlib import Path
from fractions import Fraction
from math import gcd, isqrt
import json

ROOT = Path(__file__).resolve().parents[3]


def must(path, *needles):
    text = (ROOT / path).read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, (path, needle)


def squarefree_kernel(n):
    n = abs(n)
    out = 1
    p = 2
    while p * p <= n:
        exponent = 0
        while n % p == 0:
            n //= p
            exponent += 1
        if exponent % 2:
            out *= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out *= n
    return out


def prime_divisors(n):
    n = abs(n)
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out.append(n)
    return out


# Route locks.
must(
    "stages/stage27/27-20-r301g/result.md",
    "INTEGRAL_F_G_RECEIVER_PROVED=true",
    "COMMON_SQUARECLASS_EQUALS_SQFREE_GCD_KERNEL=true",
    "ODD_COMMON_PRIME_ONE_MOD_FOUR=true",
    "ODD_COMMON_PRIME_CROSS_GCD_LOCALIZATION_PROVED=true",
    "GLOBAL_SQUARECLASS_FIXED_POWER_SUPPORT_BOUND_PROVED=false",
    "STRICT_SUB_SQRT_UPPER_PROVED=false",
)
must(
    "stages/stage27/27-20-r301h/result.md",
    "DELTA_ODD_DIVIDES_RAD_A4_MINUS_B4=true",
    "DELTA_ODD_DIVIDES_RAD_C4_MINUS_E4=true",
    "PHYSICAL_Q_HEIGHT_LE_2B=true",
    "FIXED_Q1_SQUARECLASS_SUPPORT_SUBPOLYNOMIAL=true",
    "FIXED_Q1_DELTA_FIBER_UNIFORM_SUBPOWER_PROVED=false",
    "STRICT_SUB_SQRT_UPPER_PROVED=false",
)
must(
    "stages/stage27/27-20-r301i/result.md",
    "FIXED_Q1_DELTA_COMPLETE_INTERSECTION_TWO_QUADRICS=true",
    "FIXED_Q1_DELTA_PHYSICAL_FIBER_GENUS=1",
    "FIXED_Q1_DELTA_QUARTIC_MODEL_PROVED=true",
    "QUARTIC_BRANCH_DISCRIMINANT=4096*delta^6*x^8*(x^4-1)^2",
    "MOVING_Q1_FAMILY_NONISOTRIVIAL=true",
    "POINTWISE_FIXED_FIBER_SUBPOWER_PROVED=true",
    "UNIFORM_MOVING_FIBER_SUBPOWER_PROVED=false",
    "POINTWISE_TO_UNIFORM_PROMOTION_FORBIDDEN=true",
)
must(
    "stages/stage27/27-20-r301j/result.md",
    "SQUARECLASS_INDEX_FIXED_POWER_COST_ZERO_AFTER_FIXED_Q1=true",
    "MAX_FIBER_PROGRESS_GATE=sigma+phi<1/2",
    "SECOND_MOMENT_PROGRESS_GATE=sigma+eta<1",
    "POINTWISE_FIXED_FIBER_BOUND_USED_AS_UNIFORM=false",
    "TAUTOLOGICAL_Q1_SUPPORT_USED_AS_INDEPENDENT_BOUND=false",
    "FULL_SECOND_MOMENT_DIAGONAL_IGNORED=false",
    "STRICT_SUB_SQRT_UPPER_PROVED=false",
    "NEW_MU_LT_HALF_PROVED=false",
)

# Exact denominator-cleared receiver and common-prime localization.
# Enumerate a deterministic small box and only inspect genuine FG-square points.
survivors = []
for b in range(1, 10):
    for a in range(b + 1, 20):
        if gcd(a, b) != 1:
            continue
        for e in range(1, 10):
            for c in range(e + 1, 20):
                if gcd(c, e) != 1:
                    continue
                F = a * a * e * e + b * b * c * c
                G = a * a * c * c + b * b * e * e
                if isqrt(F * G) ** 2 != F * G:
                    continue
                h = gcd(F, G)
                delta = squarefree_kernel(h)
                assert isqrt(F // delta) ** 2 == F // delta
                assert isqrt(G // delta) ** 2 == G // delta
                delta_odd = delta // 2 if delta % 2 == 0 else delta
                assert (a**4 - b**4) % delta_odd == 0
                assert (c**4 - e**4) % delta_odd == 0
                for p in prime_divisors(h):
                    assert a % p and b % p and c % p and e % p
                    if p == 2:
                        continue
                    assert p % 4 == 1
                    channel_1 = (a * a - b * b) % p == 0 and (c * c + e * e) % p == 0
                    channel_2 = (a * a + b * b) % p == 0 and (c * c - e * e) % p == 0
                    assert channel_1 ^ channel_2
                survivors.append((a, b, c, e, F, G, h, delta))

assert len(survivors) >= 10, len(survivors)
assert any(delta == 10 for *_, delta in survivors)
assert any(delta == 17 for *_, delta in survivors)
assert any(delta == 85 for *_, delta in survivors)

# Explicit physical genus-one witness from q1=9, q2=13, delta=10.
x = Fraction(9, 1)
y = Fraction(13, 1)
delta = Fraction(10, 1)
r = Fraction(5, 1)
s = Fraction(37, 1)
assert x * x + y * y == delta * r * r
assert x * x * y * y + 1 == delta * s * s
z = s + x * r
V = 2 * x * z * y
lhs = delta * V * V
rhs = (delta * z * z - (x * x + 1) ** 2) * (delta * z * z - (x * x - 1) ** 2)
assert lhs == rhs

# The branch cross-ratio is x^-4, hence varies with x.
A = x * x + 1
B = x * x - 1
cross_ratio = ((A - B) / (A + B)) ** 2
assert cross_ratio == x ** -4

# Generic support/fiber inequalities on a deterministic toy fiber distribution.
weights = [1, 1, 2, 4, 7]
N = sum(weights)
classes = len(weights)
max_fiber = max(weights)
energy = sum(w * w for w in weights)
assert N <= classes * max_fiber
assert N * N <= classes * energy
assert energy >= N

# This verifier now runs after the hostile audit and merge closeout of r301g-j.
# Do not freeze the historical pre-audit PENDING lifecycle here.
reg = json.loads((ROOT / "stages/stage27/27-20-r301g-j/batch-registry.json").read_text())
assert reg["routes"] == [
    "Stage27-20-r301g",
    "Stage27-20-r301h",
    "Stage27-20-r301i",
    "Stage27-20-r301j",
]
assert reg["status"] == "AUDITED_PASS_MERGED"
assert reg["audit_status"] == "PASS"
assert reg["merge_allowed"] is True
assert reg["advance_allowed"] is True
assert reg["fresh_reaudit_required"] is False
assert reg["final_audit_verdict"] == "PASS"
assert reg["merged"] is True
assert reg["merge_commit"] == "d53f4a4bb74e86c9e0ea38a0e12124c9b3bab30c"
assert reg["claims"]["fixed_q1_squareclass_support_subpolynomial"] is True
assert reg["claims"]["fixed_q1_delta_fiber_genus"] == 1
assert reg["claims"]["uniform_moving_fiber_subpower"] is False
assert reg["claims"]["strict_sub_sqrt_upper_proved"] is False

# Controller checks are intentionally narrow: g-j are final-audited/merged while checkpoint40 stays active.
ctl = json.loads((ROOT / "stages/stage27/27-controller.json").read_text())
for key in [
    "Stage27-20-r301g",
    "Stage27-20-r301h",
    "Stage27-20-r301i",
    "Stage27-20-r301j",
]:
    assert key in ctl["derived_routes"], key
    route = ctl["derived_routes"][key]
    assert route["status"] == "AUDITED_PASS_MERGED"
    assert route["audit_status"] == "PASS"
    assert route["merge_allowed"] is True
    assert route["advance_allowed"] is True
    assert route["audit_verdict"] == "PASS"
    assert route["merged"] is True
    assert route["merge_commit"] == "d53f4a4bb74e86c9e0ea38a0e12124c9b3bab30c"
    assert route["strict_sub_sqrt_upper_proved"] is False
assert ctl["state"]["CURRENT_CHECKPOINT"] == 40
assert ctl["state"]["NEXT_CHECKPOINT"] == 40

print("Stage27-20-r301g-j verifier: PASS")
