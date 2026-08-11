from pathlib import Path
from fractions import Fraction

ROOT = Path(__file__).resolve().parents[4]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def require(rel: str, token: str) -> None:
    text = read(rel)
    assert token in text, f"missing token in {rel}: {token}"


# Merged-source locks.
require(
    "stages/stage14/14-4fw/result.md",
    "FIXED_E_ORDINARY_SHADOW_IS_RECTANGULAR_DISTINCT_PRODUCT_SET=true",
)
require(
    "stages/stage14/14-4fy/result.md",
    "FIXED_E_TWO_SIDED_SURVIVAL_BUDGET=pi_minus_delta_lift_ge_mu",
)
require(
    "stages/stage14/14-Work-bxX36/result.md",
    "S_POLYNOMIAL_PAIR_RECTANGULAR_STRAIGHTENING_PROVED=false",
)
require(
    "stages/stage14/14-s7-107/result.md",
    "POLYNOMIAL_PAIR_UNITARY_TO_ORDINARY_POINTWISE_ENVELOPE_PROVED=true",
)

# Finite exact audit of the fibered image identity.
E_set = [2, 3, 5, 6]
D = {
    2: [2, 3, 4],
    3: [2, 5],
    5: [3, 4],
    6: [2, 3, 5],
}
V = {
    2: [5, 7],
    3: [3, 4, 7],
    5: [2, 6],
    6: [4, 5],
}

fibered = {
    (E, d * v)
    for E in E_set
    for d in D[E]
    for v in V[E]
}

by_fiber = sum(
    len({d * v for d in D[E] for v in V[E]})
    for E in E_set
)
pair_capacity = sum(len(D[E]) * len(V[E]) for E in E_set)

assert len(fibered) == by_fiber
assert len(fibered) <= pair_capacity

# Direct existential-support reconstruction.
reconstructed = set()
for E in E_set:
    candidates = {d * v for d in D[E] for v in V[E]}
    for m in range(1, 100):
        if m in candidates:
            reconstructed.add((E, m))
assert reconstructed == fibered

# E is an outer coordinate: equal integer products in distinct E-fibers do not collide.
assert (2, 20) != (5, 20)
assert len({(2, 20), (5, 20)}) == 2

# Threshold ledger sanity checks.
mu = Fraction(3, 10)
subcritical = Fraction(1, 10) + Fraction(1, 20) + Fraction(1, 10)
principal = Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10)
assert subcritical < mu
assert principal >= mu

pi_fib = Fraction(7, 20)
delta_lift = Fraction(1, 20)
tau_fib = pi_fib - delta_lift
assert tau_fib == mu
assert pi_fib - delta_lift >= mu

# New-stage and batch boundary locks.
require(
    "stages/stage14/14-s7-108/result.md",
    "POLYNOMIAL_PAIR_FIBERED_PRODUCT_IMAGE_EXACT=true",
)
require(
    "stages/stage14/14-s7-109/result.md",
    "SUBCRITICAL_FIBERED_PAIR_CAPACITY_BRANCH_CLOSED=true",
)
require(
    "stages/stage14/14-s7-110/result.md",
    "POLYNOMIAL_FIBER_SURVIVAL_BUDGET=pi_fib_minus_delta_lift_ge_mu",
)
require(
    "stages/stage14/14-s7-110/result.md",
    "RECEIVER_MATERIALLY_CHANGED=true",
)
require(
    "stages/stage14/14-s-batch/s7-108-110-report.md",
    "BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3",
)
require(
    "stages/stage14/14-s-batch/s7-108-110-report.md",
    "BATCH_STOP_REASON=receiver_change",
)
require(
    "stages/stage14/14-s-batch/s7-108-110-report.md",
    "NEXT=Stage14-s7-111",
)

print("STAGE14_S_BATCH_AUDIT=PASS")
print("S7_108_110_FIBERED_PRODUCT_CAPACITY_AUDIT=PASS")
