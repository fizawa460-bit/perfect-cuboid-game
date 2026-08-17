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


def squarefree_odd_1mod4(n: int) -> bool:
    if n < 1 or n % 2 == 0:
        return False
    ff = factor(n)
    return all(e == 1 and p % 4 == 1 for p, e in ff.items())


def omega(n: int) -> int:
    return len(factor(n))


def tau(n: int) -> int:
    ans = 1
    for e in factor(n).values():
        ans *= e + 1
    return ans


def roots_mod(k: int, sign: int) -> list[int]:
    return [x for x in range(k) if math.gcd(x, k) == 1 and (x * x - sign) % k == 0]


# CRT root multiplicities used in the proof.
for k in range(1, 180):
    if not squarefree_odd_1mod4(k):
        continue
    expected = 2 ** omega(k)
    assert len(roots_mod(k, 1)) == expected
    assert len(roots_mod(k, -1)) == expected

# Fixed-modulus box estimates and dyadic divisor-switch ingredients.
H = 18
primitive_pairs = [(m, n) for m in range(2, H + 1) for n in range(1, m) if math.gcd(m, n) == 1]

for k in range(1, H * H + 1):
    if not squarefree_odd_1mod4(k):
        continue
    rc = 2 ** omega(k)
    first = sum(1 for m, n in primitive_pairs if math.gcd(k, m * n) == 1 and (m * m - n * n) % k == 0)
    second = sum(1 for r, s in primitive_pairs if math.gcd(k, r * s) == 1 and (r * r + s * s) % k == 0)
    coarse = rc * (H * H / k + H + 1)
    assert first <= coarse + 1e-9
    assert second <= coarse + 1e-9

# Every admissible large modulus is a divisor of the first quadratic value;
# this is the divisor-switch step for K>H.
for m, n in primitive_pairs:
    q = m * m - n * n
    admissible = [
        k for k in range(H + 1, H * H + 1)
        if squarefree_odd_1mod4(k) and q % k == 0 and math.gcd(k, m * n) == 1
    ]
    assert len(admissible) <= tau(q)

# Small exact dyadic census is contained in the multiplicity sum over k.
for K in [1, 2, 4, 8, 16, 32, 64, 128]:
    actual: set[tuple[int, int, int, int]] = set()
    multiplicity_sum = 0
    for k in range(K, min(2 * K, H * H + 1)):
        if not squarefree_odd_1mod4(k):
            continue
        local = []
        for m, n in primitive_pairs:
            if math.gcd(k, m * n) != 1 or (m * m - n * n) % k:
                continue
            for r, s in primitive_pairs:
                if math.gcd(k, r * s) != 1 or (r * r + s * s) % k:
                    continue
                local.append((m, n, r, s))
                actual.add((m, n, r, s))
        multiplicity_sum += len(local)
    assert len(actual) <= multiplicity_sum

contract = json.loads((ROOT / "stages/stage27/27-19-r5ao/route-contract.json").read_text())
assert contract["task_id"] == "Stage27-19-r5ao"
assert contract["status"] == "BATCH_SUBMITTED_PENDING_FRESH_AUDIT"
assert contract["proved"]["dyadic_kappa_raw_slope_sieve"] is True
assert contract["not_proved"]["strict_sub_sqrt_upper"] is True

old = json.loads((ROOT / "stages/stage27/27-19-r5am/route-contract.json").read_text())
assert old["status"] == "CLOSED_AUDITED_PASS_MERGED"
assert old["final_audit"]["pr"] == 1061
assert old["final_audit"]["merge_commit"] == "366548fbc2d41536cd0d0e285784e932ec27bad7"
assert (ROOT / "stages/stage27/27-19-r5am/audit-final.md").exists()

controller = json.loads((ROOT / "stages/stage27/27-controller.json").read_text())
hist = controller["derived_routes"]["Stage27-19-r5am-r5an"]
cur = controller["derived_routes"]["Stage27-19-r5ao-r5ap"]
assert hist["status"] == "AUDITED_PASS_MERGED"
assert hist["audit_status"] == "PASS"
assert hist["pr"] == 1061
assert hist["merge_commit"] == "366548fbc2d41536cd0d0e285784e932ec27bad7"
assert cur["status"] == "BATCH_SUBMITTED_PENDING_FRESH_AUDIT"
assert cur["audit_status"] == "PENDING"
assert cur["strict_sub_sqrt_upper_proved"] is False
assert controller["state"]["CURRENT_CHECKPOINT"] == 40
assert controller["state"]["MAIN_STATUS"] == "UPPER_REENTRY_STAGE27_19_R5AO_R5AP_SUBMITTED_PENDING_FRESH_AUDIT"
assert controller["state"]["MERGE_ALLOWED"] is False
assert controller["next_expected_command"] == "Stage27-19-r5-audit"

status_doc = (ROOT / "docs/00_CURRENT_RESEARCH_STATUS.md").read_text()
for marker in [
    "CURRENT_STAGE=Stage27-19-r5ao-r5ap-BATCH-SUBMITTED-PENDING-FRESH-AUDIT",
    "STAGE27_19_R5AM_R5AN_STATUS=AUDITED_PASS_MERGED_PR1061",
    "STAGE27_19_R5AO_R5AP_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT",
    "STAGE27_ACTIVE_UPPER_REENTRY=27-19-r5ao-r5ap",
]:
    assert marker in status_doc

r5ao = (ROOT / "stages/stage27/27-19-r5ao/result.md").read_text()
r5ap = (ROOT / "stages/stage27/27-19-r5ap/result.md").read_text()
for marker in [
    "DYADIC_KAPPA_RAW_SLOPE_SIEVE_PROVED=true",
    "DYADIC_KAPPA_RAW_SLOPE_BOUND=H^eps*(H^4/K+H^3)",
    "DIVISOR_SWITCH_FOR_K_GT_H_PROVED=true",
    "STRICT_SUB_SQRT_UPPER_PROVED=false",
]:
    assert marker in r5ao
for marker in [
    "RAW_KAPPA_SIEVE_COMPOSITION_TO_SUBHALF_PROVED=false",
    "RAW_KAPPA_SIEVE_TOO_EARLY_IN_COUNTING_PIPELINE_PROVED=true",
    "PHYSICAL_WEIGHTED_KAPPA_SIEVE_IDENTIFIED_AS_NEXT_TARGET=true",
    "STRICT_SUB_SQRT_UPPER_PROVED=false",
]:
    assert marker in r5ap

print("Stage27-19-r5ao-r5ap verification PASS")
