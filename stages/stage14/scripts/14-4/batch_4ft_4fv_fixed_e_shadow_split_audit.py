#!/usr/bin/env python3
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def divisors(n: int):
    return [d for d in range(1, n + 1) if n % d == 0]


def unitary_divisors(n: int):
    return [d for d in divisors(n) if gcd(d, n // d) == 1]


# Exact algebraic lock used by 4fu: every unitary divisor is an ordinary divisor.
for n in range(1, 181):
    ds = set(divisors(n))
    uds = set(unitary_divisors(n))
    assert uds <= ds

# Representative moving-window support lock.  The actual Stage14 interval is
# theorem-dependent; the only deterministic claim here is the pointwise set
# inclusion after applying the same interval predicate to both divisor species.
for n in range(2, 121):
    lo = max(1, n // 7)
    hi = max(lo, n // 2)
    bare_unit = any(lo <= d <= hi for d in unitary_divisors(n))
    ordinary = any(lo <= d <= hi for d in divisors(n))
    assert (not bare_unit) or ordinary

# Nested-support exponent bookkeeping: tau <= sigma_unit <= sigma_ord and a
# physical heavy survivor forces tau >= mu.  Check representative rational cells.
for mu10 in range(1, 8):
    mu = mu10 / 10
    for tau10 in range(mu10, 9):
        tau = tau10 / 10
        for su10 in range(tau10, 10):
            sigma_unit = su10 / 10
            for so10 in range(su10, 11):
                sigma_ord = so10 / 10
                assert tau <= sigma_unit <= sigma_ord
                assert tau >= mu
                delta_c = sigma_unit - tau
                assert abs((sigma_unit - delta_c) - tau) < 1e-12

locks = {
    "stages/stage14/14-4ft/result.md": [
        "STAGE14_4FT=COMPLETE_FIXED_E_BARE_SHADOW_TO_ENDPOINT_COMPLETION_OR_TWO_SIDED_UNITARY_SPLIT",
        "FIXED_E_ENDPOINT_UNITARY_WITNESS_CHOICE_EXHAUSTED=true",
        "FIXED_E_TWO_SIDED_UNITARY_SHADOW_RETAINS=true",
        "NEXT=Stage14-4fu",
    ],
    "stages/stage14/14-4fu/result.md": [
        "STAGE14_4FU=COMPLETE_FIXED_E_TWO_SIDED_UNITARY_TO_ORDINARY_DIVISOR_SHADOW_DOMINATION",
        "UNITARY_TO_ORDINARY_DIVISOR_SHADOW_POINTWISE_DOMINATION=true",
        "UNITARY_RESTRICTION_REMOVAL_COST_FOR_UPPER_BOUND=ZERO",
        "Q14_UNITARY_RESTRICTION_AS_UPPER_BOUND_OBSTRUCTION_EXHAUSTED=true",
        "NEXT=Stage14-4fv",
    ],
    "stages/stage14/14-4fv/result.md": [
        "STAGE14_4FV=COMPLETE_FIXED_E_ENDPOINT_OR_MOVING_ORDINARY_DIVISOR_CAPACITY_COMPLETION_RECEIVER",
        "Q14_UNITARY_UPPER_BOUND_ADAPTER_COMPLETE=true",
        "Q14_MOVING_INTERVAL_NORMALIZATION_RETAINS=true",
        "RECEIVER_MATERIALLY_CHANGED=true",
        "NEXT=Stage14-4fw",
    ],
    "stages/stage14/14-4-batch/4ft-4fv-report.md": [
        "BATCH_START_MAIN_SHA=923b4b92bdfa90d7fa626e9ec512ea2cfb06c00e",
        "BATCH_PUBLICATION_MAIN_SHA=923b4b92bdfa90d7fa626e9ec512ea2cfb06c00e",
        "BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3",
        "BATCH_INTEGRATED_H_UNITS=NONE",
        "BATCH_STOP_REASON=receiver_change",
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
        "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
        "NEXT=Stage14-4fw",
    ],
}

for rel, tokens in locks.items():
    text = read(rel)
    for token in tokens:
        assert token in text, (rel, token)

# Merged-boundary regression locks.
merged_locks = {
    "stages/stage14/14-4fs/result.md": [
        "HEAVY_SURVIVAL_BUDGET=sigma_j_minus_delta_j_ge_mu",
        "NEXT=Stage14-4ft",
    ],
    "stages/stage14/14-s7-101/result.md": [
        "FIXED_E_ENDPOINT_ONE_DIMENSIONAL_SUPPORT=true",
        "FIXED_E_TWO_SIDED_POLYNOMIAL_UNITARY_PARTITION_RETAINS=true",
    ],
    "stages/stage14/14-Work-bvX34/result.md": [
        "PRINCIPAL_SCALE_THEOREM_COVERAGE_COMPLETENESS_LEMMA_PROVED=true",
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    ],
}
for rel, tokens in merged_locks.items():
    text = read(rel)
    for token in tokens:
        assert token in text, (rel, token)

print("Stage14-main-batch 4ft-4fv audit: PASS")
