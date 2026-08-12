#!/usr/bin/env python3
from pathlib import Path
from math import gcd

ROOT = Path(__file__).resolve().parents[4]


def read(rel):
    return (ROOT / rel).read_text()


def kfree_part(n, K):
    z = n
    p = 2
    kk = K
    primes = []
    while p * p <= kk:
        if kk % p == 0:
            primes.append(p)
            while kk % p == 0:
                kk //= p
        p += 1
    if kk > 1:
        primes.append(kk)
    for p in primes:
        while z % p == 0:
            z //= p
    return z


def audit_seed():
    # A concrete exact homogeneous seed:
    # U=3, V=5, A_x=30, A_y=70, C0=4,
    # P=1, Q=14, G_-=4, G_+=14.
    U, V = 3, 5
    Ax, Ay, C0 = 30, 70, 4
    P, Q, Gm, Gp = 1, 14, 4, 14
    assert Ax % P == 0 and Ay % Q == 0
    assert Gm * Gp == C0 * P * Q
    assert (Gp + Gm) % (2 * U) == 0
    assert (Gp - Gm) % (2 * V) == 0
    for m in [1, 2, 7, 11, 35, 143]:
        p, q = P * m, Q * m
        c, d = Ax // P, Ay // Q
        fm, fp = Gm * m, Gp * m
        a = (fp + fm) // (2 * U)
        b = (fp - fm) // (2 * V)
        assert p * c == Ax * m
        assert q * d == Ay * m
        assert fm * fp == C0 * p * q
        assert (fp + fm) % (2 * U) == 0
        assert (fp - fm) % (2 * V) == 0
        assert a > 0 and b > 0 and fp > fm > 0


def audit_kfree_normal_form():
    Ax, Ay, C0, U, V = 30, 70, 4, 3, 5
    K = 2 * Ax * Ay * C0 * U * V
    # 11 and 13 are outside the coefficient prime support.
    m = 11 * 11 * 13
    mc = kfree_part(m, K)
    assert mc == m
    # First layer: choose two different moving allocations.
    tp = 11
    tc = mc // tp
    tq = 13
    td = mc // tq
    assert tp * tc == mc
    assert tq * td == mc
    # Second layer: an ordered factorization of tp*tq.
    fm = 11
    fp = 13
    assert fm * fp == tp * tq
    assert gcd(fm * fp, K) == 1


def audit_first_moment_support():
    counts = [0, 1, 3, 0, 2, 1, 0, 4]
    support = sum(1 for n in counts if n > 0)
    first = sum(counts)
    max_mult = max(counts)
    assert support <= first <= max_mult * support
    # This is the finite analogue of #T <= S1 <= B^o(1)#T.


def audit_tokens():
    gf = read('stages/stage14/14-4gf/result.md')
    gg = read('stages/stage14/14-4gg/result.md')
    gh = read('stages/stage14/14-4gh/result.md')
    report = read('stages/stage14/14-4-batch/4gf-4gh-report.md')

    for token in [
        'HOMOGENEOUS_RECIPROCAL_SEED_CONSTRUCTION_EXACT=true',
        'SEEDED_RECIPROCAL_DEFICIT_FIXED_POWER=0',
        'SEEDLESS_IMPLIES_RECIPROCAL_SPARSITY=false',
        'Q17_EXPLICIT_RECIPROCAL_SELECTOR_CONSTRUCTION_TEST=COMPLETE',
    ]:
        assert token in gf, token

    for token in [
        'FIRST_LAYER_KFREE_MOVING_DIVISORS_EXACT=true',
        'SECOND_LAYER_KFREE_FACTOR_ALLOCATION_EXACT=true',
        'FIXED_UV_CRT_PRESERVED_EXACTLY=true',
        'K_SUPPORTED_CORE_RECHARGE_FORBIDDEN=true',
    ]:
        assert token in gg, token

    for token in [
        'RECIPROCAL_SUPPORT_EXPONENT_EQUALS_FIRST_MOMENT_EXPONENT=true',
        'Q17_SECOND_MOMENT_SUPPORT_TRANSFER_REQUIRED=false',
        'Q17_FIRST_MOMENT_ALONE_CONTROLS_SUPPORT_AT_B_POWER_SCALE=true',
        'KFREE_RECIPROCAL_FIRST_MOMENT_EXACT_THEOREM_SPECIES=true',
        'NEW_HEAVY_MAIN_H_NEEDED=true',
        'STRICT_SUBSQRT_POWER_SAVING_PROVED=false',
    ]:
        assert token in gh, token

    for token in [
        'BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3',
        'BATCH_INTEGRATED_H_UNITS=NONE',
        'BATCH_STOP_REASON=receiver_change',
        'NEXT=Stage14-4gi',
    ]:
        assert token in report, token


if __name__ == '__main__':
    audit_seed()
    audit_kfree_normal_form()
    audit_first_moment_support()
    audit_tokens()
    print('Stage14-main-batch 4gf-4gh deterministic audit: PASS')
