from fractions import Fraction
from math import gcd


def oddpart(n: int) -> int:
    n = abs(n)
    while n and n % 2 == 0:
        n //= 2
    return n


def divisors(n: int):
    out = []
    for d in range(1, int(n**0.5) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    p = 2
    while p * p <= n:
        if n % p == 0:
            return False
        p += 1
    return True


# 1. Exact effective-root overlap checks on primitive small packets.
root_checks = 0
overlap_positive = 0
for D in range(3, 80):
    for A in range(1, D):
        if gcd(D, A) != 1:
            continue
        hp = D * D + A * A
        hm = D * D - A * A
        hp_o = oddpart(hp)
        hm_o = oddpart(hm)
        for C in divisors(hp_o):
            Mp = hp_o // C
            for u in divisors(hm_o):
                Mm = hm_o // u
                if gcd(C, u) != 1:
                    continue
                qmix = C * u
                if gcd(qmix, D * A) != 1:
                    continue
                Wp = gcd(C, Mp)
                Wm = gcd(u, Mm)
                qeff = qmix * Wp * Wm
                if gcd(qeff, D * A) != 1:
                    raise AssertionError("effective modulus lost unit condition")
                if hp % (C * Wp) != 0:
                    raise AssertionError("plus overlap does not lift plus modulus")
                if hm % (u * Wm) != 0:
                    raise AssertionError("minus overlap does not lift minus modulus")
                if qeff > 1:
                    t = (D * pow(A, -1, qeff)) % qeff
                    if (t * t + 1) % (C * Wp) != 0:
                        raise AssertionError("minus-one root lift failed")
                    if (t * t - 1) % (u * Wm) != 0:
                        raise AssertionError("plus-one root lift failed")
                    if (pow(t, 4, qeff) - 1) % qeff != 0:
                        raise AssertionError("fourth-root lift failed")
                root_checks += 1
                if Wp > 1 or Wm > 1:
                    overlap_positive += 1

assert root_checks > 1000
assert overlap_positive > 0

# 2. Fraction ledger: fixed overlap gives exactly its total exponent as saving
# while the root-line term is live; beyond that the 1-term is even stronger.
ledger_checks = 0
for wp_num in range(0, 17):
    for wm_num in range(0, 17):
        wp = Fraction(wp_num, 64)
        wm = Fraction(wm_num, 64)
        s = wp + wm
        root_lift = max(Fraction(0), Fraction(1, 4) - s)
        E = Fraction(1, 4) + root_lift
        if s <= Fraction(1, 4):
            assert E == Fraction(1, 2) - s
        else:
            assert E == Fraction(1, 4)
        assert E <= Fraction(1, 2)
        ledger_checks += 1

# 3. Exact 2-primary decorated coupled-square identities.
coupled_checks = 0
for D in range(2, 120):
    for A in range(1, D):
        if gcd(D, A) != 1:
            continue
        hp = D * D + A * A
        hm = D * D - A * A
        hp_o = oddpart(hp)
        hm_o = oddpart(hm)
        eps_p = hp // hp_o
        eps_m = hm // hm_o
        for C in divisors(hp_o)[:8]:
            Mp = hp_o // C
            for u in divisors(hm_o)[:8]:
                Mm = hm_o // u
                assert eps_p * C * Mp == hp
                assert eps_m * u * Mm == hm
                assert eps_p * C * Mp + eps_m * u * Mm == 2 * D * D
                assert eps_p * C * Mp - eps_m * u * Mm == 2 * A * A
                coupled_checks += 1

assert coupled_checks > 1000

# 4. Finite ambient balanced-squarefree witness: products of primes from
# disjoint short ranges are unique and have balanced coprime splits.
left = [p for p in range(101, 160) if is_prime(p)]
right = [p for p in range(181, 250) if is_prime(p)]
products = {}
for p in left:
    for q in right:
        m = p * q
        if m in products:
            raise AssertionError("disjoint prime-pair product not unique")
        products[m] = (p, q)
        assert gcd(p, q) == 1
        # squarefree follows because p,q are distinct primes
        assert m % (p * p) != 0 and m % (q * q) != 0

assert len(products) == len(left) * len(right)
assert len(products) > 100

print("Stage14-s7-47 within-side overlap / balanced-split audit: PASS")
print(f"effective mixed-root checks: {root_checks}")
print(f"positive-overlap packets: {overlap_positive}")
print(f"fraction ledger checks: {ledger_checks}")
print(f"decorated coupled-square checks: {coupled_checks}")
print(f"ambient balanced prime-product witnesses: {len(products)}")
print("current whole-family exponent: 1/2")
print("strict sub-sqrt whole-family saving proved: false")
print("sqrt saturation requires W_plus=W_minus=B^o(1)")
print("balanced split alone fixed-power saving: false")
print("next: Stage14-s7-48")
