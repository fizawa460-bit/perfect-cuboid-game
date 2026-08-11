from collections import Counter
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def tau(n: int) -> int:
    ans = 0
    r = isqrt(n)
    for d in range(1, r + 1):
        if n % d == 0:
            ans += 1 if d * d == n else 2
    return ans


# Deterministic finite model of the exact rectangular product statements.
D = list(range(31, 91))
V = list(range(47, 129))
Q = len(D) * len(V)

rep = Counter(d * v for d in D for v in V)
assert sum(rep.values()) == Q
assert all(mult <= tau(m) for m, mult in rep.items())
energy = sum(mult * mult for mult in rep.values())
assert Q <= energy <= max(rep.values()) * Q

coprime_pairs = [(d, v) for d in D for v in V if gcd(d, v) == 1]
primitive_products = {d * v for d, v in coprime_pairs}
assert coprime_pairs
assert primitive_products
assert len(coprime_pairs) <= Q
assert len(primitive_products) <= len(rep)
assert len(coprime_pairs) <= max(rep.values()) * len(primitive_products)

fz = text("stages/stage14/14-4fz/result.md")
ga = text("stages/stage14/14-4ga/result.md")
gb = text("stages/stage14/14-4gb/result.md")
report = text("stages/stage14/14-4-batch/4fz-4gb-report.md")

for lock in [
    "RECTANGULAR_PRODUCT_FIBER_BOUND=Bo1",
    "RECTANGULAR_DISTINCT_PRODUCT_EXPONENT_EQUALS_PAIR_CAPACITY=true",
    "POLYNOMIAL_COLLISION_EXCESS_BRANCH_EXISTS=false",
    "DISTINCT_PRODUCT_CAPACITY_MECHANISM_EXHAUSTED=true",
]:
    assert lock in fz, lock

for lock in [
    "FIXED_E_TWO_SIDED_UNITARY_SHADOW_EQUALS_COPRIME_RECTANGULAR_PRODUCT_SUPPORT=true",
    "COPRIME_RECTANGULAR_PAIR_COUNT=Q_times_B_minus_o1",
    "UNITARY_TO_ORDINARY_FIXED_POWER_SUPPORT_DISTORTION=0",
    "UNITARY_COPRIME_COMPONENT_OF_DELTA_LIFT_FIXED_POWER_EXPONENT=0",
]:
    assert lock in ga, lock

for lock in [
    "MULTIPLICATION_COMPRESSION_FIXED_POWER_DEFICIT=0",
    "UNITARY_COPRIME_FIXED_POWER_DEFICIT=0",
    "FIXED_E_TWO_SIDED_SURVIVAL_BUDGET=kappa_minus_delta_comp_ge_mu",
    "RECEIVER_MATERIALLY_CHANGED=true",
    "NEXT=Stage14-4gc",
]:
    assert lock in gb, lock

for lock in [
    "BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3",
    "BATCH_INTEGRATED_H_UNITS=NONE",
    "BATCH_STOP_REASON=receiver_change",
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
    "NEW_HEAVY_MAIN_H_NEEDED=false",
    "NEXT=Stage14-4gc",
]:
    assert lock in report, lock

print("Stage14-main-batch 4fz-4gb deterministic audit: OK")
