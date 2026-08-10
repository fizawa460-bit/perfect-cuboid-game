#!/usr/bin/env python3
from fractions import Fraction as F
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def r2(n: int) -> int:
    out = 1
    p = 2
    m = n
    while p * p <= m:
        if m % p:
            p += 1
            continue
        e = 0
        while m % p == 0:
            m //= p
            e += 1
        out *= p ** ((e + 1) // 2)
        p += 1
    if m > 1:
        out *= m
    return out


def divisors(n: int):
    return [d for d in range(1, n + 1) if n % d == 0]


def check_divisor_intersection_lemma():
    checks = 0
    for C in range(1, 121):
        for A in divisors(C):
            for G in divisors(C):
                B = C // G
                lhs = A // gcd(A, B)
                rhs = gcd(A, G)
                assert rhs % lhs == 0
                checks += 1
    return checks


def check_square_root_lost_core():
    checks = 0
    for H in range(1, 181):
        for D0 in divisors(H * H):
            R = r2(D0)
            assert H % R == 0, (H, D0, R)
            assert R * R >= D0
            checks += 1
    return checks


def check_column_transfer():
    checks = 0
    for R in range(1, 40):
        for jm in range(1, 35):
            for jp in range(1, 35):
                if gcd(jm, jp) != 1:
                    continue
                Lm = (R * jm // gcd(R, jm)) * 3
                Lp = (R * jp // gcd(R, jp)) * 5
                assert Lm % jm == 0 and Lp % jp == 0
                assert Lm % R == 0 and Lp % R == 0
                hm, hp = Lm // jm, Lp // jp
                assert (hm * hp) % R == 0, (R, jm, jp, hm, hp)
                checks += 1
    return checks


def strip_ok(theta, phi):
    return (
        F(3, 16) <= theta <= F(5, 16)
        and F(1, 8) <= phi <= F(1, 4)
        and F(0) <= theta - phi <= F(1, 8)
        and theta + phi >= F(3, 8)
    )


def block_bounds(theta, phi, sH):
    chi = 2 * theta + 2 * phi - F(3, 4)
    d = chi - F(1, 4)
    EH = 3 * phi - F(1, 8) - 3 * sH
    ESRC = 2 * phi + max(F(0), sH - d) + max(F(0), 2 * sH - d)
    Es = max(2 * theta, 1 - 2 * theta)
    Ek = 3 * theta - F(1, 4)
    return chi, d, EH, ESRC, Es, Ek, min(EH, ESRC, Es, Ek)


def candidate_s(theta, phi):
    chi = 2 * theta + 2 * phi - F(3, 4)
    d = chi - F(1, 4)
    lo = max(F(0), d / 2)
    cands = {
        lo,
        max(F(0), d),
        F(0),
        F(1, 8),
        (phi - F(1, 8) + d) / 5,
        (phi - F(1, 8) + 2 * d) / 6,
    }
    return [s for s in cands if lo <= s <= F(1, 8)]


def check_symbolic_equality():
    theta, phi, sH = F(17, 64), F(1, 4), F(1, 32)
    chi, d, EH, ESRC, Es, Ek, E = block_bounds(theta, phi, sH)
    assert chi == F(9, 32)
    assert d == F(1, 32)
    assert EH == ESRC == Es == E == F(17, 32)
    assert Ek == F(35, 64)
    j = chi - 2 * sH
    lost = chi - j
    raw_col = F(1, 4) - j
    forced = lost / 2
    eff_col = raw_col - forced
    row = F(1, 4) - j
    assert j == F(7, 32)
    assert lost == F(1, 16)
    assert raw_col == forced == row == F(1, 32)
    assert eff_col == 0
    assert F(61, 112) - F(17, 32) == F(3, 224)
    assert F(17, 32) - F(1, 2) == F(1, 32)


def check_whole_strip_mesh():
    D = 3200
    best = F(-1)
    equality = set()
    points = 0
    for it in range(int(F(3, 16) * D), int(F(5, 16) * D) + 1):
        theta = F(it, D)
        for ip in range(int(F(1, 8) * D), int(F(1, 4) * D) + 1):
            phi = F(ip, D)
            if not strip_ok(theta, phi):
                continue
            points += 1
            local = F(-1)
            local_s = []
            for sH in candidate_s(theta, phi):
                val = block_bounds(theta, phi, sH)[-1]
                if val > local:
                    local = val
                    local_s = [sH]
                elif val == local:
                    local_s.append(sH)
            if local > best:
                best = local
                equality = {(theta, phi, s) for s in local_s}
            elif local == best:
                equality |= {(theta, phi, s) for s in local_s}
    assert best == F(17, 32), (best, equality)
    assert equality == {(F(17, 64), F(1, 4), F(1, 32))}, equality
    return points


def check_predecessor_text():
    cr = (ROOT / 'stages/stage14/14-4cr/result.md').read_text()
    cs = (ROOT / 'stages/stage14/14-4cs/result.md').read_text()
    s35 = (ROOT / 'stages/stage14/14-s7-35/result.md').read_text()
    s38 = (ROOT / 'stages/stage14/14-s7-38/result.md').read_text()
    cw = (ROOT / 'stages/stage14/14-4cw/result.md').read_text()
    assert 'gcd(C_*,M*N)=1' in cr
    assert 'oddpart(h)' in cs and 'oddpart(gcd(X,Y))' in cs
    assert 'omega_1*omega_2' in s35 and 'H_star' in s35
    assert 'CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=61/112' in s38
    assert 'CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=61/112' in cw


def check_boundary():
    out = (ROOT / 'stages/stage14/14-s7-39/result.md').read_text()
    for tok in [
        'STAGE14_S7_39=COMPLETE_CAYLEY_RESIDUAL_DISJOINTNESS_SQUARE_ROOT_LOST_CORE_AND_17_32_PROMOTION',
        'CAYLEY_GOOD_CORE_COPRIME_TO_COMMON_ROOT_GCD=true',
        'CAYLEY_RESIDUAL_FIXED_POWER_INTERSECTION_TRIVIAL=true',
        'CAYLEY_ONLY_ANNULUS_FIXED_POWER_EXPONENT=0',
        'JOINT_CORE_EQUALS_CAYLEY_GOOD_CORE_AT_FIXED_POWER=true',
        'LOST_CORE_SQUARE_ROOT_DIVISOR_PROVED=true',
        'LOST_CORE_SQUARE_ROOT_DIVISOR_DIVIDES_COLUMN_COFACTOR_PRODUCT=true',
        'CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=17/32',
        'IMPROVEMENT_OVER_PREVIOUS_61_112=3/224',
        'CURRENT_GAP_TO_SQRT=1/32',
        'SEVENTEEN_32_EFFECTIVE_COLUMN_SUPPORT_EXPONENT=0',
        'SEVENTEEN_32_ROW_CRT_LIFT_EXPONENT=1/32',
        'S7_39_AUXILIARY_H_NEEDED=false',
        'NEXT=Stage14-s7-40',
    ]:
        assert tok in out, tok


def main():
    dchecks = check_divisor_intersection_lemma()
    rchecks = check_square_root_lost_core()
    cchecks = check_column_transfer()
    check_symbolic_equality()
    points = check_whole_strip_mesh()
    check_predecessor_text()
    check_boundary()
    print('Stage14-s7-39 Cayley/residual disjointness audit: PASS')
    print('divisor intersection checks:', dchecks)
    print('square-root lost-core checks:', rchecks)
    print('column transfer checks:', cchecks)
    print('balanced mesh points:', points)
    print('current whole-family exponent: 17/32')
    print('saving over 61/112: 3/224')
    print('gap to sqrt: 1/32')
    print('unique equality: theta=17/64 phi=1/4 s_H=1/32')
    print('equality ledger: chi=9/32 j=7/32 lost=1/16 forced_sqrt=1/32 effective_column=0 row=1/32')


if __name__ == '__main__':
    main()
