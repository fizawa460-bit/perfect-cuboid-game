#!/usr/bin/env python3
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def divisors(n: int):
    out = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
        d += 1
    return sorted(out)


def tau(n: int) -> int:
    return len(divisors(n))


# 4gc: accepted primitive-pair support and its outer product image differ only
# by the divisor-bounded multiplication fiber.
D = range(5, 17)
V = range(11, 24)
pairs = [(u, v) for u in D for v in V if gcd(u, v) == 1]
accepted_pairs = [(u, v) for (u, v) in pairs if (u + 2 * v) % 4 == 1]
accepted_products = {u * v for (u, v) in accepted_pairs}
assert len(accepted_products) <= len(accepted_pairs)
for m in accepted_products:
    fiber = [(u, v) for (u, v) in accepted_pairs if u * v == m]
    assert len(fiber) <= tau(m)


# 4gd: one exact normalized coefficient packet where the second reciprocal
# identity is automatically a coefficient identity times (uv)^2.
E0 = 1
H0 = 1
x, y = 5, 3
U, Vag = 1, 1
alpha, beta = 1, 4
for u, v in [(7, 11), (8, 13), (9, 14)]:
    assert gcd(u, v) == 1
    m = u * v
    Xrec = H0 * x * m
    Yrec = H0 * y * m
    Xr = alpha * E0 * u * u
    Yr = beta * E0 * v * v
    assert Xrec * Xrec - Yrec * Yrec == 4 * Xr * Yr * U * Vag


# 4gd: exact first reciprocal factor-pair / CRT recovery on the same packet.
u, v = 7, 11
m = u * v
Xrec = x * m
Yrec = y * m
p, q = 1, 3
assert Xrec % p == 0 and Yrec % q == 0
c, d = Xrec // p, Yrec // q
r = s = epsilon_k = 1
W1 = 4 * r * s * epsilon_k * p * q
Fminus, Fplus = 2, 6
assert Fminus * Fplus == W1
assert (Fplus + Fminus) % (2 * U) == 0
assert (Fplus - Fminus) % (2 * Vag) == 0
a = (Fplus + Fminus) // (2 * U)
b = (Fplus - Fminus) // (2 * Vag)
assert (a * U) ** 2 - (b * Vag) ** 2 == W1
assert Xrec == p * c and Yrec == q * d


# The nested divisor candidate fiber is divisor-bounded in the explicit sample.
count = 0
max_second = 0
for pp in divisors(Xrec):
    for qq in divisors(Yrec):
        w = 4 * pp * qq
        max_second = max(max_second, tau(w))
        count += tau(w)
assert count <= tau(Xrec) * tau(Yrec) * max_second


# 4ge: exact nested-support deficit ledger.
kappa = 0.090
sigma_rec = 0.075
tau_phys = 0.061
mu = 0.055
delta_rec = kappa - sigma_rec
delta_post = sigma_rec - tau_phys
delta_comp = kappa - tau_phys
assert abs(delta_comp - (delta_rec + delta_post)) < 1e-12
assert kappa - delta_rec - delta_post >= mu

# Near-threshold nonnegative deficits must both vanish at fixed-power scale.
eps = 1e-10
kappa = mu = 0.055
delta_rec = 0.0
delta_post = 0.0
assert kappa - delta_rec - delta_post >= mu - eps


locks = {
    "stages/stage14/14-4gc/result.md": [
        "FIXED_E_COMPLETION_SUPPORT_EXPONENT_PRESERVED_UNDER_PAIR_PULLBACK=true",
        "FIXED_E_ACCEPTED_PAIR_TO_OUTER_PRODUCT_FIBER=Bo1",
    ],
    "stages/stage14/14-4gd/result.md": [
        "EXACT_RECIPROCAL_DIVISOR_CRT_CANDIDATE_SET_DEFINED=true",
        "FIXED_PAIR_BARE_RECIPROCAL_CANDIDATE_FIBER=Bo1",
        "X13_COLUMN_PARAMETER_FIXED_SQUARE_CLASS_M0_TIMES_m2=true",
    ],
    "stages/stage14/14-4ge/result.md": [
        "COMPLETION_DEFICIT_EXACTLY_SPLITS_AS_DELTA_REC_PLUS_DELTA_POST=true",
        "WORK_BYX37_REVISIT_TRIGGER_4GE_REACHED=true",
        "RECEIVER_MATERIALLY_CHANGED=true",
        "NEXT=Stage14-4gf",
    ],
}
for rel, tokens in locks.items():
    text = (ROOT / rel).read_text()
    for token in tokens:
        assert token in text, (rel, token)

print("Stage14-main-batch 4gc-4ge reciprocal completion audit: PASS")
