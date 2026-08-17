from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def pair_count(Y: int, k: int, a: int) -> int:
    return sum(1 for u in range(1, Y + 1) for v in range(1, Y // u + 1) if (u - a * v) % k == 0)


# Hyperbolic pair lemma: finite regression against a generous absolute constant.
for Y in [16, 32, 64, 128]:
    for k in [1, 3, 5, 7, 11, 13]:
        for a in range(1, k + 1):
            if math.gcd(a, k) != 1:
                continue
            lhs = pair_count(Y, k, a)
            rhs = 8 * (Y * math.log(2 * Y) / k + math.sqrt(Y) + 1)
            assert lhs <= rhs

# Residual congruence rewrite: if k is coprime to the physical variables,
# m = c0*cs*mu, n = delta*cn*nu turns m = sign*n mod k
# into a unit relation mu = A*nu mod k, and similarly for rho,sigma.
for k in [5, 13, 17]:
    delta, c0, cs, cn = 2, 3, 7, 1
    if math.gcd(k, delta * c0 * cs * cn) != 1:
        continue
    inv = lambda x: pow(x, -1, k)
    for sign in [-1, 1]:
        A = (sign * delta * cn * inv(c0 * cs)) % k
        for nu in range(1, k):
            mu = A * nu % k
            if mu == 0:
                continue
            m = c0 * cs * mu
            n = delta * cn * nu
            assert (m - sign * n) % k == 0

contract = json.loads((ROOT / "stages/stage27/27-19-r5aq/route-contract.json").read_text())
assert contract["task_id"] == "Stage27-19-r5aq"
assert contract["status"] == "BATCH_SUBMITTED_PENDING_FRESH_AUDIT"
assert contract["proved"]["physical_weighted_fixed_kappa_sieve"] is True
assert contract["proved"]["double_pell_compression"] is True
assert contract["not_proved"]["strict_sub_sqrt_upper"] is True

old = json.loads((ROOT / "stages/stage27/27-19-r5ao/route-contract.json").read_text())
assert old["status"] == "CLOSED_AUDITED_PASS_MERGED"
assert old["final_audit"]["pr"] == 1066
assert old["final_audit"]["merge_commit"] == "f95b259ffcc0c7ab75e9eb8ecaae2c27ceaa6b3a"

texts = {
    "aq": (ROOT / "stages/stage27/27-19-r5aq/result.md").read_text(),
    "ar": (ROOT / "stages/stage27/27-19-r5ar/result.md").read_text(),
    "as": (ROOT / "stages/stage27/27-19-r5as/result.md").read_text(),
}
for marker in [
    "PHYSICAL_WEIGHTED_FIXED_KAPPA_SIEVE_PROVED=true",
    "FIXED_KAPPA_WEIGHTED_BOUND=X^eps*(X/k+sqrt(X))",
]:
    assert marker in texts["aq"]
for marker in [
    "MODULUS_ENTROPY_CANCELS_ONE_OVER_K_SAVING=true",
    "SELF_GENERATED_KAPPA_IDENTITY_PROVED=true",
]:
    assert marker in texts["ar"]
for marker in [
    "DOUBLE_PELL_COMPRESSION_PROVED=true",
    "SMALL_KAPPA_PER_SEVEN_OUTER_CELL_BOUND=K*B^o(1)",
]:
    assert marker in texts["as"]

print("Stage27-19-r5aq-r5as verification PASS")
