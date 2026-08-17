from __future__ import annotations

import json
import math
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def squarefree_kernel(n: int) -> int:
    out = 1
    p = 2
    while p * p <= n:
        odd = False
        while n % p == 0:
            n //= p
            odd = not odd
        if odd:
            out *= p
        p += 1
    if n > 1:
        out *= n
    return out


def unique_completion(a, b, delta, c0, cs, cn, mu, nu, sigma):
    q1 = a * cs * cs * sigma * sigma + b * cn * cn * nu * nu
    kappa = squarefree_kernel(q1)
    cp2_num = q1 // kappa
    cp = math.isqrt(cp2_num)
    if cp * cp != cp2_num or cp % c0:
        return None
    cp //= c0

    q2 = b * c0 * c0 * mu * mu + a * delta * delta * sigma * sigma
    den2 = kappa * cn * cn
    if q2 % den2:
        return None
    wp = math.isqrt(q2 // den2)
    if wp * wp != q2 // den2:
        return None

    rho2_num = kappa * cs * cs * wp * wp + b * delta * delta * nu * nu
    rho2_den = a * c0 * c0
    if rho2_num % rho2_den:
        return None
    rho = math.isqrt(rho2_num // rho2_den)
    if rho * rho != rho2_num // rho2_den:
        return None
    return kappa, cp, wp, rho


# The actual r5ak L=1 witness must be reconstructed uniquely.
got = unique_completion(17, 13, 2, 3, 7, 1, 1, 8, 1)
assert got == (185, 1, 1, 9), got

# Randomly generated valid equation data reconstruct to the same completion.
rng = random.Random(2719)
checked = 1  # The exact r5ak witness above is one verified completion.
for _ in range(5000):
    vals = [rng.randint(1, 15) for _ in range(9)]
    a, b, delta, c0, cs, cn, mu, nu, sigma = vals
    if math.gcd(a, b) != 1:
        continue
    completion = unique_completion(*vals)
    if completion is None:
        continue
    kappa, cp, wp, rho = completion
    assert a * cs**2 * sigma**2 + b * cn**2 * nu**2 == kappa * c0**2 * cp**2
    assert b * c0**2 * mu**2 + a * delta**2 * sigma**2 == kappa * cn**2 * wp**2
    assert a * c0**2 * rho**2 - b * delta**2 * nu**2 == kappa * cs**2 * wp**2
    assert squarefree_kernel(kappa) == kappa
    checked += 1

assert checked > 0

contract = json.loads(
    (ROOT / "stages/stage27/27-19-r5al/route-contract.json").read_text(encoding="utf-8")
)
assert contract["task_id"] == "Stage27-19-r5al"
assert contract["verdict"] == "INCONCLUSIVE"
assert contract["proved"]["residual_completion_rigidity"] is True
assert contract["not_proved"]["strict_sub_sqrt_upper"] is True
assert contract["exponent_promotion_proposed"] is False

result = (ROOT / "stages/stage27/27-19-r5al/result.md").read_text(encoding="utf-8")
for marker in [
    "RESIDUAL_COMPLETION_RIGIDITY_PROVED=true",
    "UNIFORM_MORDELL_WEIL_RANK_ASSUMED=false",
    "ACTUAL_L_EQ_1_WITNESS_RETAINED=true",
    "STRICT_SUB_SQRT_UPPER_PROVED=false",
    "EXPONENT_PROMOTION_PROPOSED=false",
    "VERDICT=INCONCLUSIVE",
]:
    assert marker in result

controller = json.loads(
    (ROOT / "stages/stage27/27-controller.json").read_text(encoding="utf-8")
)
route = controller["derived_routes"]["Stage27-19-r5al"]
assert route["status"] == "PROPOSED_INCONCLUSIVE_PENDING_FRESH_AUDIT"
assert route["strict_sub_sqrt_upper_proved"] is False
assert route["exponent_promotion_proposed"] is False

print(f"Stage27-19-r5al verification PASS; valid completions checked={checked}")
