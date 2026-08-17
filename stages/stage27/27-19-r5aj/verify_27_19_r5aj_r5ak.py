from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def is_square(n: int) -> bool:
    if n < 0:
        return False
    r = math.isqrt(n)
    return r * r == n


def sf(n: int) -> int:
    out = 1
    d = 2
    while d * d <= n:
        parity = 0
        while n % d == 0:
            n //= d
            parity ^= 1
        if parity:
            out *= d
        d += 1
    if n > 1:
        out *= n
    return out


checked = 0
survivor_squareclass_checked = 0
for m in range(2, 36):
    for n in range(1, m):
        if math.gcd(m, n) != 1:
            continue
        for r in range(2, 36):
            for s in range(1, r):
                if math.gcd(r, s) != 1:
                    continue

                delta = math.gcd(n, s)
                n0, s0 = n // delta, s // delta
                c0 = math.gcd(m, r)
                cs = math.gcd(m, s0)
                cn = math.gcd(r, n0)
                C = c0 * cs * cn
                epsilon = 2 if all(v % 2 for v in (m, n, r, s)) else 1

                assert math.gcd(c0, cs) == 1
                assert math.gcd(c0, cn) == 1
                assert math.gcd(cs, cn) == 1

                assert m % (c0 * cs) == 0
                assert r % (c0 * cn) == 0
                assert s0 % cs == 0
                assert n0 % cn == 0
                mu = m // (c0 * cs)
                rho = r // (c0 * cn)
                sigma = s0 // cs
                nu = n0 // cn

                E = 4 * m * n * r * s
                X = 2 * r * s * (m * m - n * n)
                Y = 2 * m * n * (r * r - s * s)
                Gamma = math.gcd(E, math.gcd(X, Y))
                assert Gamma == 2 * delta * epsilon * C
                e, x, y = E // Gamma, X // Gamma, Y // Gamma

                edge_num = 2 * delta * C * mu * rho * nu * sigma
                x_num = rho * sigma * (m * m - n * n)
                y_num = mu * nu * (r * r - s * s)
                assert edge_num % epsilon == 0
                assert x_num % epsilon == 0
                assert y_num % epsilon == 0
                assert e == edge_num // epsilon
                assert x == x_num // epsilon
                assert y == y_num // epsilon

                M = m * m + n * n
                K = r * r - s * s
                h = math.gcd(M, K)
                a, b = M // h, K // h
                dex_num = rho * sigma * h * a
                dey_num = mu * nu * (r * r + s * s)
                assert dex_num % epsilon == 0
                assert dey_num % epsilon == 0
                dex = dex_num // epsilon
                dey = dey_num // epsilon
                assert dex * dex == e * e + x * x
                assert dey * dey == e * e + y * y

                # The r5aj physical edge budget is the direct consequence e <= R.
                assert 2 * delta * C * mu * rho * nu * sigma == epsilon * e

                p = s0 * s0 * a
                q = n0 * n0 * b
                J = a * b * h + delta * delta * (p - q)
                if is_square(J * (p + q)):
                    kappa = sf(p + q)
                    assert sf(J) == kappa
                    c2 = (p + q) // kappa
                    w2 = J // kappa
                    assert is_square(c2) and is_square(w2)
                    c = math.isqrt(c2)
                    w = math.isqrt(w2)
                    assert c % c0 == 0
                    assert w % (cs * cn) == 0
                    cp = c // c0
                    wp = w // (cs * cn)

                    assert a * cs * cs * sigma * sigma + b * cn * cn * nu * nu == kappa * c0 * c0 * cp * cp
                    assert b * c0 * c0 * mu * mu + a * delta * delta * sigma * sigma == kappa * cn * cn * wp * wp
                    assert a * c0 * c0 * rho * rho - b * delta * delta * nu * nu == kappa * cs * cs * wp * wp
                    survivor_squareclass_checked += 1

                checked += 1

assert checked > 100000, checked
assert survivor_squareclass_checked > 100, survivor_squareclass_checked

# Actual exactly-two Stage19 survivor with residual factor L=1.
m, n, r, s = 21, 16, 27, 14
delta = math.gcd(n, s)
n0, s0 = n // delta, s // delta
c0, cs, cn = math.gcd(m, r), math.gcd(m, s0), math.gcd(r, n0)
C = c0 * cs * cn
epsilon = 2 if all(v % 2 for v in (m, n, r, s)) else 1
E = 4 * m * n * r * s
X = 2 * r * s * (m * m - n * n)
Y = 2 * m * n * (r * r - s * s)
Gamma = math.gcd(E, math.gcd(X, Y))
e, x, y = E // Gamma, X // Gamma, Y // Gamma
M, K = m * m + n * n, r * r - s * s
h = math.gcd(M, K)
a, b = M // h, K // h
p, q = s0 * s0 * a, n0 * n0 * b
J = a * b * h + delta * delta * (p - q)
kappa = sf(p + q)
c = math.isqrt((p + q) // kappa)
w = math.isqrt(J // kappa)
assert (delta, n0, s0) == (2, 8, 7)
assert (c0, cs, cn, C, epsilon) == (3, 7, 1, 21, 1)
assert (h, a, b, p, q, J, kappa, c, w) == (41, 17, 13, 833, 832, 9065, 185, 3, 7)
assert w * c // C == 1
assert Gamma == 84
assert (e, x, y) == (6048, 1665, 4264)
assert is_square(e * e + x * x)
assert is_square(e * e + y * y)
assert not is_square(x * x + y * y)
assert math.isqrt(e * e + x * x) == 6273
assert math.isqrt(e * e + y * y) == 7400
assert math.isqrt(e * e + x * x + y * y) == 7585
assert 7585 * 7585 == e * e + x * x + y * y

contract = json.loads((ROOT / "stages/stage27/27-19-r5aj/route-contract.json").read_text())
assert contract["task_id"] == "Stage27-19-r5aj"
assert contract["status"] in {"SUBMITTED_PENDING_FRESH_AUDIT", "CLOSED_AUDITED_PASS_MERGED"}
assert contract["proved"]["cross_gcd_residual_chart"] is True
assert contract["proved"]["residual_squareclass_system"] is True
assert contract["proved"]["actual_stage19_L_eq_1_witness"] is True
assert contract["not_proved"]["strict_sub_sqrt_upper"] is True

# Historical r5ah-r5ai must be canonical PASS once this successor branch is active.
old_contract = json.loads((ROOT / "stages/stage27/27-19-r5ah/route-contract.json").read_text())
assert old_contract["status"] == "CLOSED_AUDITED_PASS_MERGED"
assert old_contract["final_audit"]["pr"] == 1054
assert old_contract["final_audit"]["merge_commit"] == "38dd56bc3fdcc6830f39340f00bb7bcfc4ad66f9"

controller = json.loads((ROOT / "stages/stage27/27-controller.json").read_text())
assert controller["state"]["CURRENT_CHECKPOINT"] == 40
old = controller["derived_routes"]["Stage27-19-r5ah-r5ai"]
assert old["audit_status"] == "PASS"
assert old["merge_commit"] == "38dd56bc3fdcc6830f39340f00bb7bcfc4ad66f9"
cur = controller["derived_routes"]["Stage27-19-r5aj-r5ak"]
assert cur["status"] in {"BATCH_SUBMITTED_PENDING_FRESH_AUDIT", "AUDITED_PASS_MERGED"}
assert cur["strict_sub_sqrt_upper_proved"] is False

r5aj = (ROOT / "stages/stage27/27-19-r5aj/result.md").read_text()
r5ak = (ROOT / "stages/stage27/27-19-r5ak/result.md").read_text()
for marker in [
    "CROSS_GCD_RESIDUAL_CHART_PROVED=true",
    "INTEGRAL_FACE_DIAGONAL_RESIDUAL_FORMULAS_PROVED=true",
    "LARGE_C_POPULATION_FIXED_POWER_SPARSE_PROVED=false",
    "STRICT_SUB_SQRT_UPPER_PROVED=false",
]:
    assert marker in r5aj
for marker in [
    "RESIDUAL_SQUARECLASS_SYSTEM_PROVED=true",
    "ACTUAL_STAGE19_L_EQ_1_WITNESS_PROVED=true",
    "HEIGHT_DEPENDENT_L_LOWER_BOUND_DISPROVED=false",
    "SMALL_L_SURVIVOR_COUNT_FIXED_POWER_BOUND_PROVED=false",
]:
    assert marker in r5ak

print(
    "Stage27-19-r5aj-r5ak verification PASS; "
    f"primitive tuples={checked}; squareclass incidences={survivor_squareclass_checked}"
)
