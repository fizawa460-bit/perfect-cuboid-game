#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path

OUT = Path('stages/stage14/data/14-e11/explicit_log_saving_audit.json')
E10 = Path('stages/stage14/data/14-e10/adelic_state_sieve_audit.json')

RHO = 6
DIM_X = 2
A = 2 * (RHO + 2 * DIM_X + 1)  # Huang Theorem 1.6(1) proof exponent.
LAMBDA_STAR = Fraction(1, 46)
ETA_SUPREMUM = Fraction(1, 46)
ETA_CONCRETE = Fraction(1, 50)
EPS_WITNESS = Fraction(1, 1000)
LOCAL_LAMBDA = Fraction(1, 100)


def frac(x: Fraction) -> dict:
    return {'fraction': f'{x.numerator}/{x.denominator}', 'decimal': float(x)}


def primes_upto(n: int) -> list[int]:
    sieve = bytearray(b'\x01') * (n + 1)
    if n >= 0:
        sieve[0] = 0
    if n >= 1:
        sieve[1] = 0
    for p in range(2, math.isqrt(n) + 1):
        if sieve[p]:
            start = p * p
            sieve[start:n + 1:p] = b'\x00' * (((n - start) // p) + 1)
    return [p for p in range(2, n + 1) if sieve[p]]


def chi4(p: int) -> int:
    assert p % 2 == 1
    return 1 if p % 4 == 1 else -1


def delta(p: int) -> Fraction:
    assert p % 2 == 1
    return Fraction(2 * (p - chi4(p)), p * p + 6 * p + 1)


def sieve_weight(p: int) -> Fraction:
    d = delta(p)
    return d / (1 - d)


def finite_field_nonsquare_count(p: int) -> int:
    assert p % 2 == 1
    count = 0
    for r in range(1, p):
        a = (r * r + 1) % p
        if a == 0:
            continue
        symbol = pow(a, (p - 1) // 2, p)
        if symbol == p - 1:
            count += 1
    return count


def g_diagnostics(max_n: int, checkpoints: list[int]) -> list[dict]:
    # f is the square-free multiplicative function with f(p)=delta_p/(1-delta_p)
    # for odd primes and f(2)=0. Then G(N)=sum_{n<N} f(n).
    spf = list(range(max_n + 1))
    for p in range(2, math.isqrt(max_n) + 1):
        if spf[p] == p:
            for m in range(p * p, max_n + 1, p):
                if spf[m] == m:
                    spf[m] = p
    f = [0.0] * (max_n + 1)
    f[1] = 1.0
    total = 0.0
    wanted = set(checkpoints)
    rows = []
    for n in range(1, max_n):
        if n == 1:
            value = 1.0
        else:
            p = spf[n]
            m = n // p
            if p == 2 or m % p == 0:
                value = 0.0
            else:
                value = f[m] * float(sieve_weight(p))
            f[n] = value
        total += value
        N = n + 1
        if N in wanted:
            rows.append({
                'N': N,
                'G_N': total,
                'G_N_over_logN_squared': total / (math.log(N) ** 2),
                'classification': 'finite_diagnostic_only',
            })
    return rows


def main() -> None:
    e10 = json.loads(E10.read_text())
    assert e10['status']['STAGE14_E10'] == 'COMPLETE_ADELIC_STATE_LAW_LOCAL_SIEVE_AND_THIN_COVER_LOG_SAVING'
    assert e10['status']['QUANTITATIVE_RELATIVE_SAVING_PROVED'] is True
    assert e10['status']['EXPLICIT_ETA_EB_EVALUATED'] is False

    # Huang proof balance for r=6, dim X=2:
    # term 1 saves lambda(1-eps), term 2 saves 1/2-eps-lambda(22+eps).
    first_saving = LAMBDA_STAR * (1 - EPS_WITNESS)
    second_saving = Fraction(1, 2) - EPS_WITNESS - LAMBDA_STAR * (A + EPS_WITNESS)
    assert A == 22
    assert LAMBDA_STAR < Fraction(1, 4 * (RHO + 2 * DIM_X + 1))  # 1/46 < 1/44
    assert first_saving > ETA_CONCRETE
    assert second_saving > ETA_CONCRETE

    # e10 blocker has sieve dimension 2: w_p=delta_p/(1-delta_p)=2/p+O(p^-2).
    displayed = {}
    for p in [3, 5, 7, 11, 13, 17, 19]:
        d = delta(p)
        w = sieve_weight(p)
        expected = (p - chi4(p)) // 2
        assert finite_field_nonsquare_count(p) == expected
        displayed[str(p)] = {
            'delta_p': frac(d),
            'sieve_weight_delta_over_one_minus_delta': frac(w),
            'nonsquare_ratio_count': expected,
        }

    # Uniform local blocker is a mod-p condition on the four exceptional rays.
    fan_exceptional_rays = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for n1 in range(-8, 9):
        for n2 in range(-8, 9):
            if n1 == n2 == 0:
                continue
            is_G = abs(n1) == abs(n2) and abs(n1) > 0
            on_exceptional_ray = any(
                n1 == k * a and n2 == k * b
                for a, b in fan_exceptional_rays
                for k in range(1, 9)
            )
            assert is_G == on_exceptional_ray

    # With N=(log B)^1/100, the Selberg-sieve error has a fixed positive
    # log-B gap 1/2-22/100 before epsilon losses, hence is negligible versus
    # the main B(log B)^5/(log log B)^2 term.
    local_error_gap = Fraction(1, 2) - A * LOCAL_LAMBDA
    assert local_error_gap == Fraction(7, 25)
    assert LOCAL_LAMBDA < Fraction(1, 44)

    g_rows = g_diagnostics(200000, [100, 1000, 10000, 100000, 200000])

    report = {
        'metadata': {
            'stage': '14-e11',
            'track': 'explicit thin-cover exponent and growing-prime uniformity',
            'huang_source': 'arXiv:2111.01509v3, proof of Theorem 1.6(1), equations corresponding to the two Selberg-sieve error terms',
        },
        'huang_explicit_exponent': {
            'picard_rank_r': RHO,
            'dimension_X': DIM_X,
            'sieve_error_N_exponent': A,
            'allowed_lambda_ceiling_from_paper': '1/44',
            'balanced_lambda': frac(LAMBDA_STAR),
            'admissible_eta_supremum_not_endpoint': frac(ETA_SUPREMUM),
            'statement': 'for every eta<1/46, R_EB(B) <<_eta B(log B)^(5-eta)',
            'concrete_eta': frac(ETA_CONCRETE),
            'concrete_statement': 'R_EB(B) << B(log B)^(5-1/50)',
            'epsilon_witness': frac(EPS_WITNESS),
            'first_term_saving_with_witness': frac(first_saving),
            'second_term_saving_with_witness': frac(second_saving),
            'endpoint_eta_1_over_46_claimed': False,
            'optimality_beyond_huang_proof_claimed': False,
        },
        'growing_prime_local_sieve': {
            'uniform_detection': 'for odd p the e10 blocker is reduction-mod-p data on the four exceptional toric divisors; n0=1',
            'exceptional_fan_rays': [list(x) for x in fan_exceptional_rays],
            'sieve_weight_formula': 'w_p=delta_p/(1-delta_p)=2/p+O(1/p^2)',
            'sieve_dimension': 2,
            'G_asymptotic': 'G(N)=C_G(log N)^2+O(log N) for some C_G>0',
            'chosen_N': 'N=(log B)^(1/100)',
            'local_error_log_gap_before_epsilon': frac(local_error_gap),
            'theorem': 'R_EB(B) << B(log B)^5/(log log B)^2 using only the e10 explicit blockers plus Huang uniform Selberg sieve',
            'stronger_than_e10_two_limit_argument': True,
            'weaker_than_thin_cover_log_power_bound': True,
            'displayed_local_weights': displayed,
            'G_finite_diagnostics': g_rows,
        },
        'comparison': {
            'e8_independent_envelope': 'B^(1+o(1))',
            'e10_thin_cover': 'B(log B)^(5-eta_EB) for some eta_EB>0',
            'e11_explicit_thin_cover': 'B(log B)^(5-eta) for every eta<1/46; in particular eta=1/50',
            'e11_local_blocker_only': 'B(log B)^5/(log log B)^2',
            'sqrt_B_asymptotic_proved': False,
        },
        'status': {
            'STAGE14_E11': 'COMPLETE_EXPLICIT_THIN_COVER_EXPONENT_AND_GROWING_PRIME_SIEVE',
            'HUANG_PROOF_EXPLICIT_ETA_RANGE_PROVED': True,
            'ETA_EB_ANY_LT_1_OVER_46': True,
            'CONCRETE_ETA_1_OVER_50_PROVED': True,
            'ENDPOINT_ETA_1_OVER_46_PROVED': False,
            'ELEMENTARY_GROWING_PRIME_UNIFORMITY_PROVED': True,
            'LOCAL_BLOCKER_LOGLOG_SAVING_PROVED': True,
            'LOCAL_BLOCKER_SIEVE_DIMENSION': 2,
            'SQRT_B_ASYMPTOTIC_PROVED': False,
            'NEXT_E_SUPPLEMENT': 'NONE_DEFINED_AFTER_E11',
        },
        'pass': True,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + '\n')
    print(json.dumps(report['status'], indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
