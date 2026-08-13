from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def divisors(n: int):
    out = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


def unitary_divisors(n: int):
    return [d for d in divisors(n) if gcd(d, n // d) == 1]


def rad(n: int):
    r = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            r *= p
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        r *= n
    return r


def sqf_kernel(n: int):
    k = 1
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e % 2:
            k *= p
        p += 1
    if n > 1:
        k *= n
    return k


# s7-105/s7-107: every unitary witness is an ordinary-divisor witness.
for m in range(1, 220):
    ds = divisors(m)
    uds = unitary_divisors(m)
    assert set(uds).issubset(ds)

    # Test several moving intervals, including ones depending on the outer pair.
    for E in (1, 2, 5, 11):
        lo = 1 + ((E + m) % max(1, isqrt(m)))
        hi = min(m, lo + 1 + (E * 3 + m) % 9)
        unit_hit = any(lo <= u <= hi for u in uds)
        ord_hit = any(lo <= d <= hi for d in ds)
        assert (not unit_hit) or ord_hit

# s7-106: the coprime-to-rad(K) subset is safely inside the named kernel-gcd mask.
for K in (1, 6, 10, 15, 42, 210):
    Q = rad(K)
    for E in range(1, 500):
        if gcd(E, Q) == 1:
            assert gcd(sqf_kernel(E), K) == 1


def require(path: str, token: str):
    text = (ROOT / path).read_text()
    assert token in text, (path, token)


# Merged theorem-source locks.
require("stages/stage14/14-s7-93/result.md", "w_ratio(n,u,v,E)")
require("stages/stage14/14-s7-93/result.md", "gcd(sqf(E),K_Z)=1")
require("stages/stage14/14-s7-104/result.md", "KNOWN_SQUAREFREE_KERNEL_MASK_FIXED_POWER_DEFICIT=0")
require("stages/stage14/14-4fv/result.md", "Q14_UNITARY_UPPER_BOUND_ADAPTER_COMPLETE=true")
require("stages/stage14/14-Work-bwX35/result.md", "COMMON_ABSOLUTE_CAPACITY_FIRST_PRINCIPLE_PROVED=true")
require("stages/stage14/archive/docs/q-research/stage14-q15-summary.md", "Q15_LOCALIZED_DIVISOR_WIDTH_COMPATIBILITY_TEST")

# New-stage locks.
require("stages/stage14/14-s7-105/result.md", "FIXED_E_TWO_SIDED_ABSOLUTE_CAPACITY_FIRST_CLOSURE=true")
require("stages/stage14/14-s7-106/result.md", "NAMED_PROVED_E_ONLY_MASK_COUNT=1")
require("stages/stage14/14-s7-106/result.md", "FIXED_PRODUCT_SINGLE_RESIDUAL_PHYSICAL_BOOLEAN_DEFINED=true")
require("stages/stage14/14-s7-107/result.md", "POLYNOMIAL_PAIR_UNITARY_TO_ORDINARY_POINTWISE_ENVELOPE_PROVED=true")
require("stages/stage14/14-s7-107/result.md", "WORK_BWX35_REVISIT_TRIGGER_S7_107_REACHED=true")
require("stages/stage14/14-s-batch/s7-105-107-report.md", "BATCH_STOP_REASON=receiver_change")
require("stages/stage14/14-s-batch/s7-105-107-report.md", "NEXT=Stage14-s7-108")

print("STAGE14_S_BATCH_S7_105_107_AUDIT=PASS")
