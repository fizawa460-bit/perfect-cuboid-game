from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


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


def is_square(n: int) -> bool:
    if n < 0:
        return False
    r = math.isqrt(n)
    return r * r == n


def raw_data(m: int, n: int, r: int, s: int):
    delta = math.gcd(n, s)
    n0, s0 = n // delta, s // delta
    E = 4 * m * n * r * s
    X = 2 * r * s * (m * m - n * n)
    Y = 2 * m * n * (r * r - s * s)
    Gamma = math.gcd(E, math.gcd(X, Y))
    c0 = math.gcd(m, r)
    cs = math.gcd(m, s0)
    cn = math.gcd(r, n0)
    C = c0 * cs * cn
    epsilon = 2 if all(v % 2 for v in (m, n, r, s)) else 1
    return delta, n0, s0, E, X, Y, Gamma, c0, cs, cn, C, epsilon


checked = 0
for m in range(2, 30):
    for n in range(1, m):
        if math.gcd(m, n) != 1:
            continue
        for r in range(2, 30):
            for s in range(1, r):
                if math.gcd(r, s) != 1:
                    continue
                (
                    delta,
                    n0,
                    s0,
                    E,
                    X,
                    Y,
                    Gamma,
                    c0,
                    cs,
                    cn,
                    C,
                    epsilon,
                ) = raw_data(m, n, r, s)

                assert math.gcd(n0, s0) == 1
                assert math.gcd(c0, cs) == 1
                assert math.gcd(c0, cn) == 1
                assert math.gcd(cs, cn) == 1
                assert Gamma == 2 * delta * epsilon * C

                M = m * m + n * n
                K = r * r - s * s
                h = math.gcd(M, K)
                a, b = M // h, K // h
                assert math.gcd(a, b) == 1
                p = s0 * s0 * a
                q = n0 * n0 * b
                J = a * b * h + delta * delta * (p - q)
                assert J == b * m * m + p * delta * delta
                assert J == a * r * r - q * delta * delta
                assert a * r * r - b * m * m == delta * delta * (p + q)

                assert (p + q) % (c0 * c0) == 0
                assert J % (cs * cs) == 0
                assert J % (cn * cn) == 0

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
                    if epsilon == 2:
                        assert h % 2 == 0
                    assert h % epsilon == 0

                    R2_raw = E * E + X * X + Y * Y
                    assert R2_raw % (Gamma * Gamma) == 0
                    R2 = R2_raw // (Gamma * Gamma)
                    if is_square(R2):
                        R = math.isqrt(R2)
                        assert R == (h // epsilon) * kappa * wp * cp
                        assert R % kappa == 0
                        assert R % (h // epsilon) == 0
                checked += 1

assert checked > 50000, checked

# Explicit exactly-two Stage19 survivor with kappa=1, preventing a fake large-kappa theorem.
m, n, r, s = 7, 4, 5, 3
delta, n0, s0, E, X, Y, Gamma, c0, cs, cn, C, epsilon = raw_data(m, n, r, s)
e, x, y = E // Gamma, X // Gamma, Y // Gamma
R2 = e * e + x * x + y * y
assert is_square(R2)
assert not is_square(x * x + y * y)
R = math.isqrt(R2)
M, K = m * m + n * n, r * r - s * s
h = math.gcd(M, K)
a, b = M // h, K // h
p, q = s0 * s0 * a, n0 * n0 * b
J = a * b * h + delta * delta * (p - q)
assert sf(p + q) == sf(J) == 1
assert R == 1073

contract = json.loads((ROOT / "stages/stage27/27-19-r5ah/route-contract.json").read_text())
assert contract["task_id"] == "Stage27-19-r5ah"
assert contract["status"] == "CLOSED_AUDITED_PASS_MERGED"
assert contract["final_audit"]["pr"] == 1054
assert contract["final_audit"]["merge_commit"] == "38dd56bc3fdcc6830f39340f00bb7bcfc4ad66f9"
assert contract["proved"]["exact_primitive_scale_factorization"] is True
assert contract["proved"]["exact_physical_diagonal_integer_product"] is True
assert contract["not_proved"]["strict_sub_sqrt_upper"] is True

old_contract = json.loads((ROOT / "stages/stage27/27-19-r5af/route-contract.json").read_text())
assert old_contract["status"] == "CLOSED_AUDITED_PASS_MERGED"
assert old_contract["final_audit"]["pr"] == 1051
assert old_contract["final_audit"]["merge_commit"] == "e7e11fd67d147d4f7c78b153e330c6bb6ed0e1a9"

controller = json.loads((ROOT / "stages/stage27/27-controller.json").read_text())
assert controller["state"]["CURRENT_CHECKPOINT"] == 40
assert controller["state"]["AUDIT_STATUS"] == "PENDING"
assert controller["state"]["ADVANCE_ALLOWED"] is False
assert controller["state"]["NEXT_CHECKPOINT"] == 40
assert controller["derived_routes"]["Stage27-19-r5af-r5ag"]["audit_status"] == "PASS"
assert controller["derived_routes"]["Stage27-19-r5af-r5ag"]["merge_commit"] == "e7e11fd67d147d4f7c78b153e330c6bb6ed0e1a9"
assert controller["derived_routes"]["Stage27-19-r5ah-r5ai"]["status"] == "AUDITED_PASS_MERGED"
assert controller["derived_routes"]["Stage27-19-r5ah-r5ai"]["audit_status"] == "PASS"
assert controller["derived_routes"]["Stage27-19-r5ah-r5ai"]["merge_commit"] == "38dd56bc3fdcc6830f39340f00bb7bcfc4ad66f9"

r5ah = (ROOT / "stages/stage27/27-19-r5ah/result.md").read_text()
r5ai = (ROOT / "stages/stage27/27-19-r5ai/result.md").read_text()
for marker in [
    "EXACT_PRIMITIVE_SCALE_FACTORIZATION_PROVED=true",
    "EXACT_PHYSICAL_DIAGONAL_PRODUCT_PROVED=true",
    "H_KAPPA_BOUND_PROVED=true",
    "STRICT_SUB_SQRT_UPPER_PROVED=false",
]:
    assert marker in r5ah
for marker in [
    "THRESHOLD_DICHOTOMY_PROVED=true",
    "HIDDEN_GAMMA_BRANCH_CLOSED=true",
    "LARGE_CROSS_GCD_CANCELLATION_SPARSE_PROVED=false",
]:
    assert marker in r5ai

print(f"Stage27-19-r5ah-r5ai verification PASS; primitive slope tuples checked={checked}")
