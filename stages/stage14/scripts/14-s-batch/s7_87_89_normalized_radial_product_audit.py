#!/usr/bin/env python3
from fractions import Fraction
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def factorint(n):
    out = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def val(n, p):
    e = 0
    while n % p == 0:
        e += 1
        n //= p
    return e


def is_squarefree(n):
    return all(e == 1 for e in factorint(n).values())


def allocate_c0(c0, J, a, b):
    cJ = ca = cb = 1
    for p, e in factorint(c0).items():
        vJ, va, vb = val(J, p), val(a, p), val(b, p)
        assert vJ + va + vb >= e
        eJ = min(vJ, e)
        rem = e - eJ
        ea = min(va, rem)
        eb = rem - ea
        assert eb <= vb
        cJ *= p ** eJ
        ca *= p ** ea
        cb *= p ** eb
    assert cJ * ca * cb == c0
    assert J % cJ == 0 and a % ca == 0 and b % cb == 0
    return cJ, ca, cb

# Lock merged theorem sources and new boundaries.
checks = {
    'stages/stage14/14-s7-86/result.md': [
        'ROOT_OVERLAP_SQUAREPART_RADIAL_EQUATION=d0_J_a_b_equals_c0_h',
        'FIXED_H_ROOT_OVERLAP_SQUAREPART_FIBER=Bo1',
    ],
    'stages/stage14/14-4fd/result.md': [
        'SURVIVING_HEAVY_RAY_RADIAL_SUPPORT_LOWER_BOUND=B^(mu-o(1))',
        'SURVIVING_HEAVY_RAY_MU_RANGE=0<mu<=1/4-phi',
    ],
    'stages/stage14/14-Work-bqX29/result.md': [
        'S_HEAVY_CAPACITY_GAP_SUPERSEDED_BY_MERGED_4FD=true',
        'GLOBAL_S_COMMON_RADIAL_OUTER_COORDINATE_PROVED=true',
    ],
    'stages/stage14/14-s7-87/result.md': [
        'FIXED_DENOMINATOR_DIVIDES_EVERY_ACCEPTED_H=true',
        'NORMALIZED_RADIAL_COORDINATE_N_DEFINED=true',
        'SURVIVAL_REQUIRES_lambda_LE_sigma_MINUS_mu=true',
    ],
    'stages/stage14/14-s7-88/result.md': [
        'COEFFICIENT_FREE_NORMALIZED_PRODUCT=n_equals_J1_a1_b1',
        'FIXED_N_NORMALIZED_TRIPLE_FIBER=Bo1',
    ],
    'stages/stage14/14-s7-89/result.md': [
        'PEELED_ROOT_PAIR_NORMAL_FORM=true',
        'SHARED_SQUAREFREE_FACTOR_CANCELS_FROM_ROOT_RATIO=true',
        'RECEIVER_MATERIALLY_CHANGED=true',
    ],
}
for rel, needles in checks.items():
    text = (ROOT / rel).read_text()
    for needle in needles:
        assert needle in text, (rel, needle)

cases = 0
allocation_cases = 0
ratio_cases = 0
for c0 in range(1, 21):
    for d0 in range(1, 13):
        if gcd(c0, d0) != 1:
            continue
        for J in range(1, 31):
            if not is_squarefree(J):
                continue
            for a in range(1, 14):
                for b in range(1, 14):
                    Jab = J * a * b
                    if Jab % c0:
                        continue
                    n = Jab // c0
                    h = d0 * n
                    assert d0 * J * a * b == c0 * h
                    assert h % d0 == 0
                    assert Jab % c0 == 0
                    assert h // d0 == n
                    cases += 1

                    cJ, ca, cb = allocate_c0(c0, J, a, b)
                    J1, a1, b1 = J // cJ, a // ca, b // cb
                    assert J1 * a1 * b1 == n
                    assert is_squarefree(J1)
                    allocation_cases += 1

                    # Check the peeled root pair and projective-ratio identity
                    # for a fixed coprime noncommon kernel split A*B.
                    A, B = 1, 5
                    alpha = cJ * A * ca * ca
                    beta = cJ * B * cb * cb
                    X = J * A * a * a
                    Y = J * B * b * b
                    assert X == alpha * J1 * a1 * a1
                    assert Y == beta * J1 * b1 * b1
                    assert Fraction(X, Y) == Fraction(alpha * a1 * a1, beta * b1 * b1)
                    ratio_cases += 1

assert cases > 1000
assert allocation_cases == cases
assert ratio_cases == cases
print(f'radial_normalization_cases={cases}')
print(f'coefficient_allocation_cases={allocation_cases}')
print(f'peeled_ratio_cases={ratio_cases}')
print('STAGE14_S_BATCH_AUDIT=PASS')
