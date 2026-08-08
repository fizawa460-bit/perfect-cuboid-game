#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path

E8_PATH = Path('stages/stage14/data/14-e8/euler_brick_thin_count_audit.json')
E9_PATH = Path('stages/stage14/data/14-e9/gcd_lcm_local_statistics.json')
OUT = Path('stages/stage14/data/14-e10/adelic_state_sieve_audit.json')
STATES = ['none', 'G', 'U', 'V', 'GU', 'GV']
DISPLAY_PRIMES = [2, 3, 5, 7, 11, 13]


def F(x: Fraction) -> dict:
    return {'fraction': f'{x.numerator}/{x.denominator}', 'decimal': float(x)}


def chi4(p: int) -> int:
    assert p % 2
    return 1 if p % 4 == 1 else -1


def state_masses(p: int) -> dict[str, Fraction]:
    if p == 2:
        return {'none':Fraction(1,9),'G':Fraction(2,9),'U':Fraction(1,9),'V':Fraction(1,9),'GU':Fraction(2,9),'GV':Fraction(2,9)}
    D = p*p + 6*p + 1
    return {
        'none': Fraction((p-1)**2, D), 'G': Fraction(4*(p-1), D),
        'U': Fraction(2*(p-1), D), 'V': Fraction(2*(p-1), D),
        'GU': Fraction(4, D), 'GV': Fraction(4, D),
    }


def blocker_mass(p: int) -> Fraction:
    if p == 2:
        return Fraction(2, 9)
    return Fraction(2*(p-chi4(p)), p*p+6*p+1)


def legendre(a: int, p: int) -> int:
    a %= p
    if not a:
        return 0
    z = pow(a, (p-1)//2, p)
    return -1 if z == p-1 else 1


def primes_upto(n: int) -> list[int]:
    s = bytearray(b'\x01')*(n+1)
    s[0:2] = b'\x00\x00'
    for p in range(2, math.isqrt(n)+1):
        if s[p]:
            s[p*p:n+1:p] = b'\x00'*(((n-p*p)//p)+1)
    return [p for p in range(2, n+1) if s[p]]


def verify_finite_field_formula(p: int) -> None:
    vals = [legendre(r*r+1, p) for r in range(1, p)]
    minus = vals.count(-1)
    zero = vals.count(0)
    assert minus == (p-chi4(p))//2
    assert zero == (2 if p % 4 == 1 else 0)


def survivor(ps: list[int]) -> Fraction:
    ans = Fraction(1)
    for p in ps:
        ans *= 1-blocker_mass(p)
    return ans


def main() -> None:
    e8 = json.loads(E8_PATH.read_text())
    e9 = json.loads(E9_PATH.read_text())
    assert e8['status']['EULER_BRICK_K3_MODEL_LOCKED'] is True
    assert e9['status']['STAGE14_E9'] == 'COMPLETE_GCD_LCM_LOCAL_CONTROL_AND_2_3_BLOCKERS'

    laws = {}
    for p in DISPLAY_PRIMES:
        m = state_masses(p)
        assert sum(m.values(), Fraction()) == 1
        laws[str(p)] = {
            'state_masses': {s: F(m[s]) for s in STATES},
            'blocker_mass': F(blocker_mass(p)),
        }
        if p > 2:
            laws[str(p)]['G_conditional_nonsquare_fraction'] = F(Fraction(p-chi4(p), 2*(p-1)))

    odd_test_primes = [p for p in primes_upto(199) if p > 2]
    for p in odd_test_primes:
        verify_finite_field_formula(p)

    p23_surv = survivor([2, 3])
    six_surv = survivor(DISPLAY_PRIMES)
    assert p23_surv == Fraction(5, 9)
    assert six_surv == Fraction(31160, 100533)

    ceiling = e9['cutoffs'][-1]
    assert ceiling['B'] == 200000 and ceiling['raw_total'] == 1896751
    finite_block = ceiling['rigorous_local_blockers']
    assert finite_block['third_square_incidence_in_union'] == 0

    diag = []
    for limit in [13, 31, 97, 997, 10000, 100000, 1000000]:
        ps = primes_upto(limit)
        z = ps[-1]
        P = math.exp(sum(math.log1p(-float(blocker_mass(p))) for p in ps))
        diag.append({'largest_prime': z, 'P': P, 'P_log2': P*math.log(z)**2})

    report = {
        'metadata': {
            'stage': '14-e10',
            'track': 'adelic six-state law and residue completion sieve',
            'height': 'physical Euclidean D_R / e6 physical anticanonical adelic metric',
        },
        'local_coordinates': {
            'odd_p': 'a=vp(S1)=|vp(q1)|, b=vp(S2)=|vp(q2)|',
            'p2': 'a=0 on vp(q1)=0 and a=|vp(q1)|+1 otherwise; likewise b',
            'state_partition': {'none':'a=b=0','G':'a=b>0','U':'b>a=0','V':'a>b=0','GU':'b>a>0','GV':'a>b>0'},
        },
        'adelic_state_law': {
            'odd_prime_denominator': 'D_p=p^2+6p+1',
            'odd_prime_formula': {'none':'(p-1)^2/D_p','G':'4(p-1)/D_p','U':'2(p-1)/D_p','V':'2(p-1)/D_p','GU':'4/D_p','GV':'4/D_p'},
            'p2_formula': {'none':'1/9','G':'2/9','U':'1/9','V':'1/9','GU':'2/9','GV':'2/9'},
            'displayed_primes': laws,
            'fixed_finite_prime_joint_law': 'product Tamagawa mass after truncating valuation tails; same finite-place law in each real direction chamber',
            'direction_independence': True,
        },
        'residue_completion_sieve': {
            'B2': 'state G at p=2; x^2+y^2=2 mod 4',
            'odd_Bp': 'state G and x^2+y^2 is a nonzero quadratic nonsquare mod p',
            'odd_G_conditional_nonsquare': '(p-chi_4(p))/(2(p-1))',
            'odd_blocker_mass': 'delta_p=2(p-chi_4(p))/(p^2+6p+1)',
            'delta_2': F(Fraction(2,9)),
            'delta_asymptotic': '2/p+O(1/p^2)',
            'finite_field_formula_verified': {'odd_primes_tested': len(odd_test_primes), 'largest_prime': odd_test_primes[-1]},
            'p2_p3': {'survival':F(p23_surv),'blocked':F(1-p23_surv)},
            'primes_2_3_5_7_11_13': {'survival':F(six_surv),'blocked':F(1-six_surv)},
            'every_Euler_brick_avoids_every_Bp': True,
        },
        'finite_e9_crosscheck': {
            'B': ceiling['B'], 'raw_total': ceiling['raw_total'],
            'p2_or_p3_G_union': finite_block['p2_or_p3_state_G_union'],
            'finite_blocked_fraction': finite_block['p2_or_p3_state_G_union']/ceiling['raw_total'],
            'asymptotic_blocked_fraction': float(Fraction(4,9)),
            'third_square_incidence_in_union': 0,
            'classification': 'finite_preasymptotic_diagnostic_only',
        },
        'local_sieve': {
            'survivor_product': 'P(z)=prod_{p<=z}(1-delta_p)',
            'mertens_shape': 'P(z)~C_sieve/(log z)^2 for some C_sieve>0',
            'two_limit_argument': 'fix z, apply adelic equidistribution, then z->infinity',
            'zero_density_reproof': 'R_EB(B)=o(B(log B)^5)',
            'growing_z_uniformity_used': False,
            'B_log3_upper_bound_from_elementary_sieve_alone': False,
            'numerical_product_diagnostic': diag,
        },
        'huang_thin_cover_upgrade': {
            'map': 'minimal resolution of Euler-brick degree-2 cover -> Y=Bl_4(P1xP1)',
            'generic_degree': 2,
            'domain': 'proper smooth geometrically integral K3',
            'application': 'Huang v3 Theorem 1.6(1) bounds the larger adelic image, hence also rational Euler-brick images',
            'conclusion': 'exists eta_EB in (0,1): R_EB(B) << B(log B)^(5-eta_EB)',
            'physical_height_transfer': 'fixed multiplicative comparison with toric anticanonical height',
            'eta_EB_explicitly_evaluated': False,
        },
        'theorem_boundary': {
            'six_state_adelic_law_proved': True,
            'fixed_finite_prime_independence_proved': True,
            'directionwise_same_local_law_proved': True,
            'local_sieve_zero_density_reproved': True,
            'quantitative_relative_log_saving_proved_via_Huang': True,
            'explicit_eta_EB_proved': False,
            'elementary_growing_prime_uniformity_proved': False,
            'sqrt_B_asymptotic_proved': False,
        },
        'status': {
            'STAGE14_E10':'COMPLETE_ADELIC_STATE_LAW_LOCAL_SIEVE_AND_THIN_COVER_LOG_SAVING',
            'SIX_STATE_ADELIC_LAW_PROVED':True,
            'FIXED_FINITE_PRIME_PRODUCT_LAW_PROVED':True,
            'LOCAL_BLOCKER_MASS_FORMULA_PROVED':True,
            'P2_P3_ASYMPTOTIC_BLOCKED_MASS':'4/9',
            'LOCAL_SIEVE_ZERO_DENSITY_REPROVED':True,
            'HUANG_GENERIC_FINITE_LOG_SAVING_APPLIES':True,
            'QUANTITATIVE_RELATIVE_SAVING_PROVED':True,
            'EXPLICIT_ETA_EB_EVALUATED':False,
            'NEXT_E_SUPPLEMENT':'Stage14-e11 explicit thin-cover exponent / growing-prime uniformity',
        },
        'pass': True,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True)+'\n')
    print(json.dumps(report['status'], indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
