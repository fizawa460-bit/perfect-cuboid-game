#!/usr/bin/env python3
"""Stage14-t25: odd local minimality and large-prime routing on the rank [-1] cover."""

from collections import Counter
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
GRAPH = ROOT / 'stages/stage14/scripts/14-4/rank_jump_graph_audit.py'
T21 = ROOT / 'stages/stage14/scripts/14-t/t21_direction_scale_reduction_audit.py'
OUT = ROOT / 'stages/stage14/data/14-t25/local_minimality_large_prime.json'
MAX_B = 2_000_000
CUTS = (1000,2000,5000,10000,20000,50000,100000,200000,500000,1000000,2000000)
EXPECTED_RAW = {1000:2,2000:5,5000:15,10000:25,20000:42,50000:62,100000:89,200000:116,500000:188,1000000:255,2000000:356}


def factorint(n):
    n = abs(int(n))
    out = {}
    while n % 2 == 0 and n:
        out[2] = out.get(2, 0) + 1
        n //= 2
    p = 3
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def vp(n, p):
    n = abs(int(n))
    e = 0
    while n and n % p == 0:
        e += 1
        n //= p
    return e


def three_part(n):
    out = 1
    for p, e in factorint(n).items():
        if p % 4 == 3:
            out *= p ** e
    return out


def largest_three_prime(n):
    z = [p for p in factorint(n) if p % 4 == 3]
    return max(z, default=1)


def edge_records(a, b, c, d, mask, direction_data):
    sides = (a, b, c)
    specs = ((0,1,0), (0,2,1), (1,2,2))
    out = []
    for i, j, shared_idx in specs:
        if not ((mask & (1 << i)) and (mask & (1 << j))):
            continue
        s = sides[shared_idx]
        others = [sides[k] for k in range(3) if k != shared_idx]
        zdir = direction_data(d, s)
        g, D, C = zdir['g'], zdir['D'], zdir['C']
        alpha, beta, r, u, h = (zdir[k] for k in ('alpha','beta','r','u','h'))
        assert gcd(D, C) == 1 and d == g * D and s == g * C
        assert D - C == h * alpha * r * r
        assert D + C == h * beta * u * u

        # Integral 4-torsion model from t24:
        # Y^2 = X(X^2 + (4D^2-2C^2)X + C^4).
        # c4=16(16D^4-16D^2C^2+C^4), Delta=256 C^8 D^2(D^2-C^2).
        c4 = 16 * (16 * D**4 - 16 * D*D*C*C + C**4)
        disc = 256 * C**8 * D**2 * (D*D - C*C)

        # The odd bad-prime support is exactly C*D*(D^2-C^2).  Use the
        # t21 factorization for D^2-C^2 to avoid factoring a 4e12-size integer.
        support = set()
        for n in (C, D, alpha, beta, r, u):
            support.update(p for p in factorint(n) if p != 2)
        local_checks = 0
        mult_primes = []
        for ell in sorted(support):
            assert c4 % ell != 0
            assert disc % ell == 0
            # Since c4 is an ell-adic unit, the displayed integral model is
            # minimal at odd ell and has multiplicative reduction.
            if C % ell == 0:
                expected_v = 8 * vp(C, ell)
            elif D % ell == 0:
                expected_v = 2 * vp(D, ell)
            else:
                expected_v = vp(alpha, ell) + vp(beta, ell) + 2*vp(r, ell) + 2*vp(u, ell)
            assert vp(disc, ell) == expected_v
            local_checks += 1
            mult_primes.append(ell)

        # t20 kernel support: no odd 3 mod 4 prime occurs in alpha*beta.
        assert all(p % 4 == 1 for p in factorint(alpha) if p != 2)
        assert all(p % 4 == 1 for p in factorint(beta) if p != 2)

        # A physical [-1]-cover point forces every odd prime divisor of D to
        # split in Q(i), hence ell=1 mod 4.  Verify this exact consequence.
        odd_D_primes = [p for p in factorint(D) if p != 2]
        assert all(p % 4 == 1 for p in odd_D_primes)

        ru3 = three_part(r * u)
        lp3 = largest_three_prime(r * u)
        cover_checks = 0
        forced_orientation_checks = 0
        for xx, yy in (others, others[::-1]):
            hy = isqrt(s*s + yy*yy)
            assert hy*hy == s*s + yy*yy

            # Physical square parameter z=-((d+x)/H_y)^2.  Reduce it to p/q.
            rat = Fraction(d + xx, hy)
            p, q = rat.numerator, rat.denominator
            assert p > q > 0 and gcd(p, q) == 1

            # Cleared [-1] cover, homogeneous in p,q.
            rhs = (4*D*D - 2*C*C) * p*p*q*q - C*C * (p**4 + q**4)
            assert rhs >= 0
            W = isqrt(rhs)
            assert W*W == rhs

            # Two exact sum-of-two-squares identities.
            assert W*W + C*C*(p*p + q*q)**2 == (2*D*p*q)**2
            assert W*W + C*C*(p*p - q*q)**2 == 4*(D*D-C*C)*p*p*q*q

            # The first identity excludes odd ell=3 mod 4 from D.
            for ell in odd_D_primes:
                if ell % 4 == 3:
                    raise AssertionError('3 mod 4 prime divides D on a physical cover')

            # For ell=3 mod 4 in D^2-C^2, valuation of a sum of two squares
            # is even.  Since alpha*beta contains no such ell, these primes
            # come from r*u with even exponent; exactly half of that exponent
            # is forced into W and p^2-q^2.
            for ell, e_ru in factorint(r*u).items():
                if ell % 4 != 3:
                    continue
                e = vp(D*D-C*C, ell)
                assert e == 2 * e_ru
                forced = ell ** e_ru
                assert W % forced == 0
                assert (p*p - q*q) % forced == 0
                assert (p-q) % ell == 0 or (p+q) % ell == 0

            assert W % ru3 == 0
            assert (p*p - q*q) % ru3 == 0
            if ru3 > 1:
                forced_orientation_checks += 1
            cover_checks += 1

        out.append({
            'd': d, 'D': D, 'C': C,
            'alpha': alpha, 'beta': beta, 'r': r, 'u': u,
            'odd_local_minimality_checks': local_checks,
            'odd_multiplicative_primes': mult_primes,
            'odd_D_primes': odd_D_primes,
            'ru_3mod4_part': ru3,
            'largest_3mod4_prime_in_ru': lp3,
            'minus_one_cover_checks': cover_checks,
            'forced_orientation_checks': forced_orientation_checks,
            'is_triple_edge': mask.bit_count() == 3,
        })
    return out


def main():
    t21 = runpy.run_path(str(T21))
    direction_data = t21['direction_data']
    graph = runpy.run_path(str(GRAPH))
    keep, _ = graph['enumerate_multi'](MAX_B)

    records = []
    for (a,b,c,d),(mask,ds) in keep.items():
        records.extend(edge_records(a,b,c,d,mask,direction_data))
    records.sort(key=lambda z:(z['d'],z['D'],z['C']))
    assert len(records) == 356
    assert not any(z['is_triple_edge'] for z in records)
    assert sum(z['minus_one_cover_checks'] for z in records) == 712

    rows = []
    for B in CUTS:
        z = [r for r in records if r['d'] <= B]
        assert len(z) == EXPECTED_RAW[B]
        ru3_nontriv = [r for r in z if r['ru_3mod4_part'] > 1]
        hist = Counter(r['largest_3mod4_prime_in_ru'] for r in z if r['largest_3mod4_prime_in_ru'] > 1)
        rows.append({
            'B': B,
            'rank_active_raw_edges': len(z),
            'odd_local_minimality_checks': sum(r['odd_local_minimality_checks'] for r in z),
            'minus_one_cover_orientation_checks': sum(r['minus_one_cover_checks'] for r in z),
            'edges_with_nontrivial_3mod4_ru_part': len(ru3_nontriv),
            'edges_with_trivial_3mod4_ru_part': len(z)-len(ru3_nontriv),
            'forced_orientation_checks': sum(r['forced_orientation_checks'] for r in z),
            'max_3mod4_ru_part': max((r['ru_3mod4_part'] for r in z), default=1),
            'max_3mod4_prime_in_ru': max((r['largest_3mod4_prime_in_ru'] for r in z), default=1),
            'largest_3mod4_prime_histogram': {str(k):v for k,v in sorted(hist.items())},
        })

    final = rows[-1]
    report = {
        'stage':'14-t25',
        'odd_local_model':{
            'curve':'E_{D,C}: Y^2=X(X^2+(4D^2-2C^2)X+C^4)',
            'c4':'16(16D^4-16D^2C^2+C^4)',
            'displayed_discriminant':'256 C^8 D^2(D^2-C^2)',
            'odd_minimality':'for every odd ell|C D(D^2-C^2), c4 is an ell-adic unit; displayed model is minimal with multiplicative reduction',
            'odd_conductor':'N_odd=rad(C D(D^2-C^2))',
            'prime_2_status':'not resolved in t25',
        },
        'large_prime_routing':{
            'cover':'W^2=(4D^2-2C^2)p^2q^2-C^2(p^4+q^4), gcd(p,q)=1',
            'D_identity':'W^2+C^2(p^2+q^2)^2=(2Dpq)^2',
            'difference_identity':'W^2+C^2(p^2-q^2)^2=4(D^2-C^2)p^2q^2',
            'D_3mod4_exclusion':'every odd prime divisor of D on a physical rank-active direction is 1 mod 4',
            'kernel_3mod4_exclusion':'odd primes in alpha*beta are 1 mod 4',
            'ru_3mod4_forcing':'R3(ru)=prod_{ell=3 mod4} ell^v_ell(ru) divides both W and p^2-q^2 for every physical orientation',
            'large_prime_transfer':'if ell=3 mod4 divides r or u, then ell^v_ell(ru) divides exactly one of p-q or p+q at the ell-adic level',
            'gaussian_factorizations':[
                '(W+iC(p^2+q^2))(W-iC(p^2+q^2))=(2Dpq)^2',
                '(W+iC(p^2-q^2))(W-iC(p^2-q^2))=4(D^2-C^2)p^2q^2',
            ],
        },
        'transfer_boundary':{
            'Le_Boudec_2018_architecture':'large-prime factor plus complete 2-descent is structurally applicable, but the elementary integer forcing only captures 3 mod 4 primes in the square parts r,u',
            'unrouted_columns':['1 mod 4 primes in D','1 mod 4 primes in r,u','odd primes in C'],
            'reason_power_saving_not_closed':'the remaining large primes split in Z[i] or are invisible on this one isogeny cover; a Gaussian gcd/allocation audit and dual-isogeny descent are still required before a complete counting argument',
            'rank_second_moment_power_saving_proved':False,
        },
        'finite':{
            'max_B':MAX_B,
            **{k:v for k,v in final.items() if k != 'B'},
        },
        'rows':rows,
        'decision':{
            'STAGE14_T25':'COMPLETE_ODD_LOCAL_MINIMALITY_AND_PARTIAL_LARGE_PRIME_ROUTING',
            'ODD_DISPLAYED_MODEL_MINIMAL_MULTIPLICATIVE':True,
            'ODD_CONDUCTOR_RADICAL_EXPLICIT':True,
            'ALL_ODD_D_PRIMES_1MOD4_ON_PHYSICAL_RANK_BRANCH':True,
            'RU_3MOD4_PART_FORCED_INTO_P2_MINUS_Q2':True,
            'LE_BOUDEC_LARGE_PRIME_TRANSFER_PARTIAL':True,
            'LE_BOUDEC_TRANSFER_FULL_POWER_SAVING_PROVED':False,
            'GAUSSIAN_OR_DUAL_DESCENT_REQUIRED':True,
            'RANK_ACTIVE_SECOND_MOMENT_POWER_SAVING_PROVED':False,
            'Q_ACTIVE_DIRECTION_POWER_SAVING_PROVED':False,
            'Q_SPLIT_POWER_SAVING_PROVED':False,
            'Q_EDGE_O_B_PROVED':False,
            'T_O_SQRT_B_PROVED':False,
            'PERFECT_CUBOID_NONEXISTENCE_PROVED':False,
            'NEXT':'Stage14-t26 complete the large-prime routing: Gaussian gcd/allocation for 1 mod 4 primes and dual-isogeny descent for the C-column, then formulate the same-partition pair count',
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report['finite'], indent=2))
    print(json.dumps(report['decision'], indent=2))


if __name__ == '__main__':
    main()
