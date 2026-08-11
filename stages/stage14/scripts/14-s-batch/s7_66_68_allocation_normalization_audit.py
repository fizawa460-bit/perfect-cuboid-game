#!/usr/bin/env python3
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

# Primitive binary-form arithmetic used by s7-66/67.
checked_pairs = 0
checked_plus_primes = 0
for a in range(1, 80):
    for b in range(a + 1, 100):
        if gcd(a, b) != 1:
            continue
        checked_pairs += 1
        n = a*a + b*b
        assert gcd(n, a*b) == 1

        # Exact signed-factor identities after clearing the factor 2:
        # 2D=g(a+b), 2A=g(b-a), hence D-A=ga and D+A=gb.
        g = 2
        D = g*(a+b)//2
        A = g*(b-a)//2
        assert D-A == g*a
        assert D+A == g*b

        # Every divisor of ab decomposes uniquely across coprime a,b.
        for d in range(1, a*b + 1):
            if (a*b) % d:
                continue
            da = gcd(d, a)
            db = gcd(d, b)
            assert gcd(da, db) == 1
            assert da * db == d

        # Every odd prime divisor of primitive a^2+b^2 is 1 mod 4.
        m = n
        p = 3
        while p*p <= m:
            if m % p == 0:
                checked_plus_primes += 1
                assert p % 4 == 1
                while m % p == 0:
                    m //= p
            p += 2
        if m > 1 and m % 2:
            checked_plus_primes += 1
            assert m % 4 == 1

assert checked_pairs > 1000
assert checked_plus_primes > 100

locks = {
    'stages/stage14/14-s7-65/result.md': [
        'PRIMITIVE_BINARY_FORM_CORE_GCD_ONE=true',
        'JOINT_BALANCED_RECIPROCAL_SELECTOR_REMAINS=true',
    ],
    'stages/stage14/14-4dz/result.md': [
        'GLOBAL_ACCEPTANCE_DENSITY_CHAIN_RULE_EXACT=true',
        'INDEPENDENCE_ASSUMED=false',
    ],
    'stages/stage14/14-s7-66/result.md': [
        'PRIMITIVE_SIGNED_FACTORS_EQUAL_GA_AND_GB=true',
        'MINUS_ALLOCATION_LOCALIZES_TO_DIVISORS_OF_A_AND_B=true',
        'RECEIVER_MATERIALLY_CHANGED=false',
        'NEXT=Stage14-s7-67',
    ],
    'stages/stage14/14-s7-67/result.md': [
        'PRIMITIVE_PLUS_CORE_ODD_PRIMES_ALL_SPLIT_MOD4=true',
        'PLUS_ALLOCATION_IS_SPLIT_PRIME_SUBSET_DIVISOR_PROBLEM=true',
        'RECEIVER_MATERIALLY_CHANGED=false',
        'NEXT=Stage14-s7-68',
    ],
    'stages/stage14/14-s7-68/result.md': [
        'CANONICAL_ALLOCATION_RECIPROCAL_DENSITY_CHAIN_EXACT=true',
        'RECEIVER_MATERIALLY_CHANGED=true',
        'S7_68_NEW_AUXILIARY_H_NEEDED=false',
        'NEXT=Stage14-s7-69',
    ],
}
for rel, needles in locks.items():
    text = (ROOT / rel).read_text()
    for needle in needles:
        assert needle in text, (rel, needle)

print({
    'batch': 'Stage14-s-batch',
    'stages': 's7-66..s7-68',
    'primitive_pairs_checked': checked_pairs,
    'plus_prime_factors_checked': checked_plus_primes,
    'stop_reason': 'receiver_change',
    'current_exponent': '1/2',
    'next': 'Stage14-s7-69',
})
