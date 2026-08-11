#!/usr/bin/env python3
from pathlib import Path
from math import gcd

ROOT = Path(__file__).resolve().parents[4]


def require(path: str, needle: str) -> None:
    text = (ROOT / path).read_text()
    assert needle in text, (path, needle)


def unitary_divisors(n: int):
    return [d for d in range(1, n + 1) if n % d == 0 and gcd(d, n // d) == 1]


def omega(n: int) -> int:
    p = 2
    out = 0
    while p * p <= n:
        if n % p == 0:
            out += 1
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        out += 1
    return out


# Boundary locks.
require("stages/stage14/14-4fq/result.md", "FIXED_E_BARE_UNITARY_SHADOW_DEFINED=true")
require("stages/stage14/14-4fq/result.md", "FIXED_E_SURVIVAL_BUDGET=sigma_minus_delta_c_ge_mu")
require("stages/stage14/14-4fq/result.md", "EXPONENT_ZERO_COMPLETION_DENSITY_FORCED=false")
require("stages/stage14/14-4fr/result.md", "POLYNOMIAL_E_BARE_SHADOW_DEFINED=true")
require("stages/stage14/14-4fr/result.md", "POLYNOMIAL_E_P0_SURVIVAL_BUDGET=sigma_0_minus_delta_0_ge_mu")
require("stages/stage14/14-4fr/result.md", "POLYNOMIAL_E_PPLUS_SURVIVAL_BUDGET=sigma_plus_minus_delta_plus_ge_mu")
require("stages/stage14/14-4fs/result.md", "HEAVY_SURVIVAL_BUDGET=sigma_j_minus_delta_j_ge_mu")
require("stages/stage14/14-4fs/result.md", "BARE_SHADOW_SAVING_MECHANISM_SEPARATED=true")
require("stages/stage14/14-4fs/result.md", "CONDITIONAL_COMPLETION_SAVING_MECHANISM_SEPARATED=true")
require("stages/stage14/14-4fs/result.md", "RECEIVER_MATERIALLY_CHANGED=true")
require("stages/stage14/14-4-batch/4fq-4fs-report.md", "BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3")
require("stages/stage14/14-4-batch/4fq-4fs-report.md", "BATCH_STOP_REASON=receiver_change")
require("stages/stage14/14-4-batch/4fq-4fs-report.md", "NEXT=Stage14-4ft")

# Exact elementary unitary-divisor identity used only as a regression lock for
# the already-charged B^o(1) inner fiber: # {d || n} = 2^omega(n).
for n in range(1, 301):
    assert len(unitary_divisors(n)) == 2 ** omega(n), n

# Nested-support ledger sanity checks.  If physical support is a subset of the
# bare shadow, tau<=sigma and delta=sigma-tau>=0; survival means tau>=mu.
samples = [
    (0.20, 0.18, 0.10),
    (0.12, 0.08, 0.07),
    (1 / 24, 1 / 30, 1 / 40),
]
for sigma, tau, mu in samples:
    assert tau <= sigma
    delta = sigma - tau
    assert delta >= -1e-12
    assert abs((sigma - delta) - tau) < 1e-12
    assert tau >= mu

print("Stage14-main-batch 4fq-4fs bare-shadow/completion audit: PASS")
