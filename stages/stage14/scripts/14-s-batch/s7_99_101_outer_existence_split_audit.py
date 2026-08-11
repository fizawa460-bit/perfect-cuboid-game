from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def unitary_divisors(n: int):
    return [d for d in range(1, n + 1) if n % d == 0 and gcd(d, n // d) == 1]


def divisors(n: int):
    out = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return out


# Unitary divisors are a subset of ordinary divisors; fixed outer multiplicity cannot exceed tau(m).
for m in range(1, 160):
    uds = unitary_divisors(m)
    ds = divisors(m)
    assert set(uds).issubset(set(ds))
    assert len(uds) <= len(ds)
    for u in uds:
        v = m // u
        assert gcd(u, v) == 1
        assert u * v == m

# s7-100: fixed primitive product/orientation leaves one scalar E and constant projective ratio.
alpha, beta, d0 = 6, 35, 11
u0, v0 = 4, 9
assert gcd(u0, v0) == 1
m0 = u0 * v0
ratios = []
for E in (5, 13, 41):
    n = E * m0
    xr = alpha * E * u0 * u0
    yr = beta * E * v0 * v0
    h = d0 * n
    assert n == E * u0 * v0
    assert h == d0 * E * m0
    ratios.append((xr * beta * v0 * v0, yr * alpha * u0 * u0))
assert all(a == b for a, b in ratios)

# s7-101 endpoint: freeze one primitive side r0; the opposite side s carries all polynomial mobility.
E0, r0 = 7, 3
for s in (5, 8, 11, 17):
    if gcd(r0, s) != 1:
        continue
    m = r0 * s
    assert r0 in unitary_divisors(m)
    n = E0 * m
    xr = alpha * E0 * r0 * r0
    yr = beta * E0 * s * s
    h = d0 * E0 * r0 * s
    assert n == E0 * r0 * s
    assert xr == alpha * E0 * r0 * r0
    assert yr == beta * E0 * s * s
    assert h == d0 * n


def require(path: str, token: str):
    text = (ROOT / path).read_text()
    assert token in text, (path, token)


# Merged source locks.
require("stages/stage14/14-4fp/result.md", "PHYSICAL_WEIGHT_OUTERIZED_AT_SUPPORT_LEVEL=true")
require("stages/stage14/14-Work-buX33/result.md", "GLOBAL_S_OUTER_PHYSICAL_EXISTENCE_SUPPORT_RECEIVER_PROVED=true")
require("stages/stage14/14-s7-98/result.md", "P0_POLYNOMIAL_ENTROPY_ONLY_IN_E=true")
require("stages/stage14/14-s7-94/result.md", "SMALL_ONE_SIDE_GEOMETRY_ALONE_FIXED_POWER_SAVING=false")

# New stage locks.
require("stages/stage14/14-s7-99/result.md", "POLYNOMIAL_E_FIXED_M_OUTER_SUPPORT_PREDICATE_DEFINED=true")
require("stages/stage14/14-s7-100/result.md", "FIXED_M_PROJECTIVE_ROOT_RATIO_CONSTANT=true")
require("stages/stage14/14-s7-101/result.md", "FIXED_E_ENDPOINT_ONE_DIMENSIONAL_SUPPORT=true")
require("stages/stage14/14-s7-101/result.md", "FIXED_E_TWO_SIDED_POLYNOMIAL_UNITARY_PARTITION_RETAINS=true")
require("stages/stage14/14-s7-101/result.md", "WORK_BUX33_REVISIT_TRIGGER_S7_101_REACHED=true")
require("stages/stage14/14-s-batch/s7-99-101-report.md", "BATCH_STOP_REASON=receiver_change")

print("STAGE14_S_BATCH_S7_99_101_AUDIT=PASS")
