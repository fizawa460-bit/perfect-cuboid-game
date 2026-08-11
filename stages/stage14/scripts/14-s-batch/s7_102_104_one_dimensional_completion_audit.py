from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def divisors(n: int):
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    p = 2
    x = n
    count = 0
    while p * p <= x:
        if x % p == 0:
            x //= p
            count += 1
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        count += 1
    return -1 if count % 2 else 1


def phi(n: int) -> int:
    return sum(1 for a in range(1, n + 1) if gcd(a, n) == 1)


def squarefree_kernel(n: int) -> int:
    out = 1
    p = 2
    x = n
    while p * p <= x:
        e = 0
        while x % p == 0:
            x //= p
            e += 1
        if e % 2:
            out *= p
        p += 1
    if x > 1:
        out *= x
    return out


def rad(n: int) -> int:
    out = 1
    p = 2
    x = n
    while p * p <= x:
        if x % p == 0:
            out *= p
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        out *= x
    return out


# s7-103: once the small primitive side r is frozen, gcd(r,s)=1 is exactly
# the unitary condition for the factor r in m=r*s.
for r in range(1, 25):
    for s in range(1, 80):
        m = r * s
        unitary_r = (m % r == 0 and gcd(r, m // r) == 1)
        assert unitary_r == (gcd(r, s) == 1)

# Möbius interval count has an error bounded by the number of divisors.
for r in range(1, 35):
    ds = divisors(r)
    ph = phi(r)
    for lo in range(0, 20, 4):
        for length in (1, 3, 9, 25, 60):
            hi = lo + length
            actual = sum(1 for s in range(lo + 1, hi + 1) if gcd(s, r) == 1)
            main = length * ph / r
            assert abs(actual - main) <= len(ds) + 1e-9
            mobius_count = sum(
                mobius(d) * ((hi // d) - (lo // d)) for d in ds
            )
            assert mobius_count == actual

# s7-104: gcd(E,rad(KZ))=1 is a subset of the known squarefree-kernel mask.
for kz in range(1, 80):
    q = rad(kz)
    for E in range(1, 160):
        m_k = gcd(squarefree_kernel(E), kz) == 1
        if gcd(E, q) == 1:
            assert m_k


def require(path: str, token: str):
    text = (ROOT / path).read_text()
    assert token in text, (path, token)


# Merged source locks.
require("stages/stage14/14-s7-101/result.md", "WORK_BUX33_REVISIT_TRIGGER_S7_101_REACHED=true")
require("stages/stage14/14-4fs/result.md", "CURRENT_HEAVY_RECEIVER=ComplementaryDilationBareShortUnitaryShadowExponentVersusConditionalCanonicalReverseCompletionDeficitBudget")
require("stages/stage14/14-Work-bvX34/result.md", "PRINCIPAL_SCALE_THEOREM_COVERAGE_COMPLETENESS_LEMMA_PROVED=true")
require("stages/stage14/14-4fk/result.md", "COMPLEMENTARY_E_LOCAL_MASK_EXPLICIT=true")

# New stage locks.
require("stages/stage14/14-s7-102/result.md", "S_FOUR_REALIZATION_NESTED_SUPPORT_LEDGERS_DEFINED=true")
require("stages/stage14/14-s7-103/result.md", "FIXED_E_ENDPOINT_UNITARY_CONDITION_REDUCES_TO_COPRIMALITY=true")
require("stages/stage14/14-s7-103/result.md", "FIXED_E_ENDPOINT_BARE_UNITARY_FIXED_POWER_SAVING=false")
require("stages/stage14/14-s7-104/result.md", "KNOWN_SQUAREFREE_KERNEL_MASK_FIXED_POWER_DEFICIT=0")
require("stages/stage14/14-s7-104/result.md", "WORK_BVX34_REVISIT_TRIGGER_S7_104_REACHED=true")
require("stages/stage14/14-s7-104/result.md", "RECEIVER_MATERIALLY_CHANGED=true")
require("stages/stage14/14-s-batch/s7-102-104-report.md", "BATCH_STOP_REASON=receiver_change")

print("STAGE14_S_BATCH_S7_102_104_AUDIT=PASS")
