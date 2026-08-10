#!/usr/bin/env python3
from fractions import Fraction as F
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def oddpart(n: int) -> int:
    while n % 2 == 0 and n:
        n //= 2
    return n


def divisors(n: int):
    out = []
    for d in range(1, n + 1):
        if n % d == 0:
            out.append(d)
    return out


def check_endpoint_ledger():
    theta = F(23, 88)
    phi = F(19, 88)
    chi = 2 * theta + 2 * phi - F(3, 4)
    mu = 2 * theta - 2 * phi
    nu = F(1, 4) + 2 * phi - 2 * theta
    base = 2 * phi
    short = F(1, 4) - chi

    assert chi == F(9, 44)
    assert mu == F(1, 11)
    assert nu == F(7, 44)
    assert nu - chi == -F(1, 22)
    assert base == F(19, 44)
    assert short == F(1, 22)
    assert 2 * short == mu
    assert base + mu == F(23, 44)
    assert base + 2 * short == F(23, 44)
    assert F(23, 44) - F(1, 2) == F(1, 44)


def check_first_reciprocal_reconstruction():
    # Algebraic guard for
    # (aU)^2-(bV)^2 = 4*r*s*eps_k*p*q
    # followed by the second reciprocal reconstruction of XY.
    checks = 0
    for U in range(1, 17):
        for V in range(1, 17):
            if gcd(U, V) != 1:
                continue
            for a in range(1, 8):
                for b in range(1, 8):
                    au, bv = a * U, b * V
                    if au <= bv:
                        continue
                    diff = au * au - bv * bv
                    if diff % 4:
                        continue
                    Nk = diff // 4
                    if Nk <= 0:
                        continue
                    for p in divisors(Nk):
                        q = Nk // p
                        if gcd(p, q) != 1:
                            continue
                        assert 4 * p * q == diff
                        # Search small second signed quotients.  These are
                        # synthetic algebra checks, not a physical census.
                        for c in range(1, 7):
                            for d in range(1, 7):
                                cp, dq = c * p, d * q
                                if cp <= dq or (cp + dq) % 2:
                                    continue
                                Q = (cp + dq) // 2
                                P = (cp - dq) // 2
                                num = cp * cp - dq * dq
                                den = 4 * U * V
                                if num <= 0 or num % den:
                                    continue
                                XY = num // den
                                assert Q * Q - P * P == cp * dq
                                assert 4 * XY * U * V == num
                                checks += 1
    assert checks >= 100, checks
    return checks


def check_fixed_N_factorization_fiber():
    # Fixed N has only divisor-type ordered quadruple factorizations.
    # We audit the finite-to-one map quadruple -> oddpart(a*b).
    tuples_checked = 0
    residual_values = 0
    for N in range(1, 161):
        quads = []
        uvals = set()
        for a in divisors(N):
            N1 = N // a
            for b in divisors(N1):
                N2 = N1 // b
                for c in divisors(N2):
                    d = N2 // c
                    quads.append((a, b, c, d))
                    uvals.add(oddpart(a * b))
        assert len(uvals) <= len(quads)
        # elementary tau_4 upper envelope, deliberately loose
        assert len(quads) <= len(divisors(N)) ** 3
        tuples_checked += len(quads)
        residual_values += len(uvals)
    assert tuples_checked > 1000
    return tuples_checked, residual_values


def crt_two(a1: int, m1: int, a2: int, m2: int) -> int:
    assert gcd(m1, m2) == 1
    M = m1 * m2
    for x in range(M):
        if x % m1 == a1 % m1 and x % m2 == a2 % m2:
            return x
    raise AssertionError('CRT failure')


def check_twin_short_roundtrip():
    # Abstract exact row/column reconstruction guard.
    # One already-charged modulus is viewed through coprime row/column splits.
    checks = 0
    for jm in range(1, 10):
        for jp in range(1, 10):
            if gcd(jm, jp) != 1:
                continue
            J = jm * jp
            for hm in range(1, 6):
                for hp in range(1, 6):
                    Lm = jm * hm
                    Lp = jp * hp
                    if (Lm + Lp) % 2:
                        continue
                    zA = (Lp + Lm) // 2
                    zB = (Lp - Lm) // 2
                    assert zA + zB == Lp
                    assert zA - zB == Lm
                    for M in range(1, 3 * J + 1):
                        N0 = crt_two(M, jm, -M, jp)
                        for hN in range(0, 4):
                            N = N0 + J * hN
                            assert N % jm == M % jm
                            assert N % jp == (-M) % jp
                            assert (N - N0) // J == hN
                            checks += 1
    assert checks > 10000
    return checks


def check_no_double_charge_guard():
    # The endpoint residual and twin-short ledgers are equal coordinate costs.
    base = F(19, 44)
    residual = F(1, 11)
    col = row = F(1, 22)
    assert residual == col + row
    assert base + residual == base + col + row == F(23, 44)
    # A hypothetical additional subtraction would assert information not
    # supplied by finite-fiber reparameterization alone.
    assert base + residual - col < F(23, 44)


def check_predecessor_text():
    s40 = (ROOT / 'stages/stage14/14-s7-40/result.md').read_text()
    cy = (ROOT / 'stages/stage14/14-4cy/result.md').read_text()
    s31 = (ROOT / 'stages/stage14/14-s7-31/result.md').read_text()
    s28 = (ROOT / 'stages/stage14/14-s7-28/result.md').read_text()
    cv = (ROOT / 'stages/stage14/14-4cv/result.md').read_text()

    assert 'TWENTYTHREE_44_SATURATION_POINT_UNIQUE=true' in s40
    assert 'TWENTYTHREE_44_U_RESIDUAL_CAP_EXPONENT=1/11' in s40
    assert 'TWENTYTHREE_44_SATURATION_SEGMENT_COLLAPSED_TO_POINT=true' in cy
    assert 'FIXED_OUTER_NONPRIMITIVE_ROOT_PAIR_LEMMA_PROVED=true' in s31
    assert 'OPPOSITE_AGREEMENT_PRODUCT_RECONSTRUCTED_FROM_PRIMITIVE_X_PAIR=true' in s28
    assert 'FIXED_N_SIGNED_QUOTIENT_QUADRUPLE_MULTIPLICITY=Bo1' in cv


def check_boundary():
    out = (ROOT / 'stages/stage14/14-s7-41/result.md').read_text()
    tokens = [
        'STAGE14_S7_41=COMPLETE_FIRST_RESIDUAL_TWIN_SHORT_FINITE_FIBER_IDENTIFICATION_AND_H_GATE',
        'FIRST_SIGNED_QUOTIENT_FULL_PRODUCT_CAP_EXPONENT=1/11',
        'OPPOSITE_SIGNED_QUOTIENT_MINUS_COMMON_CORE_EXPONENT=-1/22',
        'RESIDUAL_TO_TWIN_SHORT_FIBER_MULTIPLICITY=Bo1',
        'TWIN_SHORT_TO_FIRST_RESIDUAL_FIBER_MULTIPLICITY=Bo1',
        'FIRST_RESIDUAL_AND_TWIN_SHORT_PARAMETRIZATIONS_POWER_EQUIVALENT=true',
        'TWIN_SHORT_DOUBLE_SAVING_ALLOWED=false',
        'REVERSE_ROOT_LINE_REUSE_WITHOUT_QUANTIFIER_BRIDGE_ALLOWED=false',
        'CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=23/44',
        'NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false',
        'CURRENT_GAP_TO_SQRT=1/44',
        'S7_41_AUXILIARY_H_NEEDED=true',
        'S7_41_AUXILIARY_H_REQUIRED_SAVING=delta>0',
        'S7_41_AUXILIARY_H_SQRT_THRESHOLD_SAVING=1/44',
        'S_ROUTE_BLOCKED_WAITING_FOR_H=true',
        'TH22_CROSS_PROMOTED_TO_S7_41=false',
        'NEXT=Stage14-s7-42_AFTER_AUXILIARY_H',
    ]
    for tok in tokens:
        assert tok in out, tok


def main():
    check_endpoint_ledger()
    reciprocal_checks = check_first_reciprocal_reconstruction()
    tuple_checks, residual_values = check_fixed_N_factorization_fiber()
    twin_checks = check_twin_short_roundtrip()
    check_no_double_charge_guard()
    check_predecessor_text()
    check_boundary()

    print('Stage14-s7-41 residual/twin finite-fiber audit: PASS')
    print('reciprocal reconstruction checks:', reciprocal_checks)
    print('fixed-N quadruple checks:', tuple_checks)
    print('fixed-N residual images:', residual_values)
    print('twin-short row/column roundtrip checks:', twin_checks)
    print('endpoint base exponent: 19/44')
    print('first residual exponent: 1/11')
    print('twin short exponents: 1/22 + 1/22 = 1/11')
    print('current whole-family exponent: 23/44')
    print('gap to sqrt: 1/44')
    print('auxiliary H needed: true')
    print('H saving needed for any improvement: delta>0')
    print('H saving needed to reach sqrt in one step: 1/44')


if __name__ == '__main__':
    main()
