from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def factor(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def tau(n: int) -> int:
    ans = 1
    for e in factor(n).values():
        ans *= e + 1
    return ans


def admissible_kappa(k: int) -> bool:
    if k < 1 or k % 2 == 0:
        return False
    ff = factor(k)
    return all(e == 1 and p % 4 == 1 for p, e in ff.items())


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


# Fixed-R entropy collapse: admissible kernels are a subset of divisors of R.
for R in range(1, 401):
    admissible = [d for d in divisors(R) if admissible_kappa(d)]
    assert len(admissible) <= tau(R)
    for K in [1, 2, 4, 8, 16, 32, 64, 128, 256]:
        block = [d for d in admissible if K <= d < 2 * K]
        assert len(block) <= tau(R)

# Grouping coefficient cells by t=delta*c0*cs*cn is exact before the
# project-specific coprimality restrictions are imposed.
for R in [12, 20, 36]:
    direct: dict[int, int] = {}
    for delta in range(1, R + 1):
        for c0 in range(1, R // delta + 1):
            for cs in range(1, R // (delta * c0) + 1):
                max_cn = R // (delta * c0 * cs)
                for cn in range(1, max_cn + 1):
                    t = delta * c0 * cs * cn
                    direct[t] = direct.get(t, 0) + 1
    for t, multiplicity in direct.items():
        # ordered four-factor divisor function d_4(t)
        d4 = 0
        for a in range(1, t + 1):
            if t % a:
                continue
            q1 = t // a
            for b in range(1, q1 + 1):
                if q1 % b:
                    continue
                q2 = q1 // b
                for c in range(1, q2 + 1):
                    if q2 % c == 0:
                        d4 += 1
        assert multiplicity == d4

contract = json.loads((ROOT / "stages/stage27/27-19-r5at/route-contract.json").read_text())
assert contract["task_id"] == "Stage27-19-r5at"
assert contract["status"] == "BATCH_SUBMITTED_PENDING_FRESH_AUDIT"
assert contract["proved"]["fixed_R_kappa_entropy_collapse"] is True
assert contract["proved"]["fixed_R_dyadic_weighted_host"] is True
assert contract["proved"]["hyperbolic_boundary_accumulation_barrier"] is True
assert contract["not_proved"]["strict_sub_sqrt_upper"] is True

old = json.loads((ROOT / "stages/stage27/27-19-r5aq/route-contract.json").read_text())
assert old["status"] in {"BATCH_SUBMITTED_PENDING_FRESH_AUDIT", "CLOSED_AUDITED_PASS_MERGED"}
if old["status"] == "CLOSED_AUDITED_PASS_MERGED":
    assert old["final_audit"]["pr"] == 1068
    assert old["final_audit"]["merge_commit"] == "fbae8c1bde526a82bbcfc11eed8f86ac5dda5351"
    assert (ROOT / "stages/stage27/27-19-r5aq/audit-final.md").exists()

texts = {
    "at": (ROOT / "stages/stage27/27-19-r5at/result.md").read_text(),
    "au": (ROOT / "stages/stage27/27-19-r5au/result.md").read_text(),
    "av": (ROOT / "stages/stage27/27-19-r5av/result.md").read_text(),
}
for marker in [
    "FIXED_R_KAPPA_ENTROPY_COLLAPSE_PROVED=true",
    "FIXED_SEVEN_OUTER_PLUS_R_COMPLETIONS=B^o(1)",
]:
    assert marker in texts["at"]
for marker in [
    "FIXED_R_DYADIC_WEIGHTED_HOST_PROVED=true",
    "FIXED_R_DYADIC_BOUND=R^eps*(X_R/K+sqrt(X_R))",
]:
    assert marker in texts["au"]
for marker in [
    "FIXED_R_ALL_CELL_BOUND=R^eps*(R/K+R)",
    "HYPERBOLIC_BOUNDARY_IS_CURRENT_PRIMARY_BARRIER=true",
    "STRICT_SUB_SQRT_UPPER_PROVED=false",
]:
    assert marker in texts["av"]

print("Stage27-19-r5at-r5av verification PASS")
