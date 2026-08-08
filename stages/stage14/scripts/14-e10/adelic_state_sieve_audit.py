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
AUDITED_PRIMES = [2, 3, 5, 7, 11, 13]


def frac_obj(x: Fraction) -> dict:
    return {'fraction': f'{x.numerator}/{x.denominator}', 'decimal': float(x)}


def state_masses(p: int) -> dict[str, Fraction]:
    """Normalized local Tamagawa masses of the six e9 support states."""
    if p == 2:
        return {
            'none': Fraction(1, 9),
            'G': Fraction(2, 9),
            'U': Fraction(1, 9),
            'V': Fraction(1, 9),
            'GU': Fraction(2, 9),
            'GV': Fraction(2, 9),
        }
    D = p * p + 6 * p + 1
    return {
        'none': Fraction((p - 1) ** 2, D),
        'G': Fraction(4 * (p - 1), D),
        'U': Fraction(2 * (p - 1), D),
        'V': Fraction(2 * (p - 1), D),
        'GU': Fraction(4, D),
        'GV': Fraction(4, D),
    }


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    v = pow(a, (p - 1) // 2, p)
    return -1 if v == p - 1 else 1


def chi4(p: int) -> int:
    assert p % 2 == 1
    return 1 if p % 4 == 1 else -1


def g_conditional_nonsquare_fraction(p: int) -> Fraction:
    """Within odd-p state G, ratio of unit pairs with x^2+y^2 nonsquare mod p."""
    assert p % 2 == 1
    return Fraction(p - chi4(p), 2 * (p - 1))


def blocker_mass(p: int) -> Fraction:
    """Local Tamagawa mass of the rigorous residue blocker B_p."""
    if p == 2:
        # Entire p=2 state G is blocked by x^2+y^2 == 2 mod 4.
        return Fraction(2, 9)
    D = p * p + 6 * p + 1
    return Fraction(2 * (p - chi4(p)), D)


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


def finite_field_check(p: int) -> dict:
    assert p % 2 == 1
    plus = minus = zero = 0
    for r in range(1, p):
        c = legendre(r * r + 1, p)
        if c == 1:
            plus += 1
        elif c == -1:
            minus += 1
        else:
            zero += 1
    expected_minus = (p - chi4(p)) // 2
    expected_zero = 2 if p % 4 == 1 else 0
    assert minus == expected_minus
    assert zero == expected_zero
    return {
        'p': p,
        'square_ratios': plus,
        'nonsquare_ratios': minus,
        'zero_ratios': zero,
        'conditional_nonsquare_fraction': frac_obj(Fraction(minus, p - 1)),
    }


def survivor_product(primes: list[int]) -> Fraction:
    ans = Fraction(1, 1)
    for p in primes:
        ans *= 1 - blocker_mass(p)
    return ans


def main() -> None:
    e8 = json.loads(E8_PATH.read_text())
    e9 = json.loads(E9_PATH.read_text())
    assert e8['status']['EULER_BRICK_K3_MODEL_LOCKED'] is True
    assert e9['status']['STAGE14_E9'] == 'COMPLETE_GCD_LCM_LOCAL_CONTROL_AND_2_3_BLOCKERS'

    local_laws = {}
    for p in AUDITED_PRIMES:
        masses = state_masses(p)
        assert sum(masses.values(), Fraction(0, 1)) == 1
        local_laws[str(p)] = {
            'state_masses': {s: frac_obj(masses[s]) for s in STATES},
            'blocker_mass': frac_obj(blocker_mass(p)),
        }
        if p % 2 == 1:
            local_laws[str(p)]['G_conditional_nonsquare_fraction'] = frac_obj(
                g_conditional_nonsquare_fraction(p)
            )

    # Verify the closed finite-field formula well past the displayed audit primes.
    ff_checks = [finite_field_check(p) for p in primes_upto(199) if p != 2]

    # Compare the proved asymptotic state law with the deliberately pre-asymptotic e9 ceiling.
    ceiling = e9['cutoffs'][-1]
    assert ceiling['B'] == 200000
    raw_total = ceiling['raw_total']
    finite_comparison = {}
    for p in AUDITED_PRIMES:
        exact = ceiling['local_prime_support_exact'][str(p)]
        third = ceiling['local_prime_support_third_square'][str(p)]
        raw = {s: exact[s] + third[s] for s in STATES}
        theory = state_masses(p)
        finite_comparison[str(p)] = {
            'raw_counts': raw,
            'raw_fractions': {s: raw[s] / raw_total for s in STATES},
            'theory_fractions': {s: float(theory[s]) for s in STATES},
            'max_abs_state_gap': max(abs(raw[s] / raw_total - float(theory[s])) for s in STATES),
            'classification': 'finite_preasymptotic_diagnostic_only',
        }

    p23_survival = survivor_product([2, 3])
    p23_blocked = 1 - p23_survival
    assert p23_survival == Fraction(5, 9)
    assert p23_blocked == Fraction(4, 9)

    six_prime_survival = survivor_product(AUDITED_PRIMES)
    assert six_prime_survival == Fraction(31160, 100533)

    # Mertens-scale diagnostic only. The theorem proof uses
    # delta_p = 2/p + O(1/p^2), hence P(z) ~ C/(log z)^2.
    mertens_diag = []
    for limit in [13, 31, 97, 997, 10000, 100000, 1000000]:
        ps = primes_upto(limit)
        z = ps[-1]
        logP = sum(math.log1p(-float(blocker_mass(p))) for p in ps)
        P = math.exp(logP)
        mertens_diag.append({
            'limit': limit,
            'largest_prime': z,
            'survivor_product_float': P,
            'product_times_log_z_squared': P * math.log(z) ** 2,
            'classification': 'numerical_check_of_proved_log_minus_2_product_shape',
        })

    observed_p23_union = ceiling['rigorous_local_blockers']['p2_or_p3_state_G_union'] / raw_total

    report = {
        'metadata': {
            'stage': '14-e10',
            'track': 'adelic six-state law and residue completion sieve',
            'height': 'physical Euclidean D_R, adelically equivalent to the e3/e6 anticanonical metric',
            'finite_comparison_B': ceiling['B'],
        },
        'local_coordinate_dictionary': {
            'odd_p': 'a=vp(S1)=|vp(q1)|, b=vp(S2)=|vp(q2)|',
            'p2': 'a=0 if vp(q1)=0, otherwise a=|vp(q1)|+1; likewise for b',
            'states': {
                'none': 'a=b=0',
                'G': 'a=b>0',
                'U': 'b>a=0',
                'V': 'a>b=0',
                'GU': 'b>a>0',
                'GV': 'a>b>0',
            },
        },
        'adelic_state_law': {
            'odd_prime_closed_form': {
                'denominator': 'D_p=p^2+6p+1',
                'none': '(p-1)^2/D_p',
                'G': '4(p-1)/D_p',
                'U': '2(p-1)/D_p',
                'V': '2(p-1)/D_p',
                'GU': '4/D_p',
                'GV': '4/D_p',
            },
            'p2_closed_form': {
                'none': '1/9', 'G': '2/9', 'U': '1/9', 'V': '1/9', 'GU': '2/9', 'GV': '2/9'
            },
            'displayed_primes': local_laws,
            'finite_set_joint_law': 'for every fixed finite set of primes, state events are asymptotically independent with product Tamagawa mass; the same finite-place law holds in each real direction chamber',
            'direction_independence': True,
        },
        'residue_blocker': {
            'definition': 'B_p is p=2 state G, or for odd p state G with x^2+y^2 a nonzero quadratic nonsquare mod p',
            'odd_p_conditional_formula': '(p-chi_4(p))/(2(p-1)) inside state G',
            'odd_p_total_mass_formula': 'delta_p=2(p-chi_4(p))/(p^2+6p+1)',
            'p2_total_mass': frac_obj(Fraction(2, 9)),
            'delta_asymptotic': 'delta_p=2/p+O(1/p^2)',
            'finite_field_checks': ff_checks,
            'p2_p3': {
                'theoretical_survival': frac_obj(p23_survival),
                'theoretical_blocked': frac_obj(p23_blocked),
                'finite_e9_blocked_fraction_at_B200000': observed_p23_union,
            },
            'primes_2_3_5_7_11_13': {
                'theoretical_survival': frac_obj(six_prime_survival),
                'theoretical_blocked': frac_obj(1 - six_prime_survival),
            },
            'global_square_implication': 'every Euler-brick completion avoids B_p at every prime p',
        },
        'local_sieve': {
            'fixed_z_survivor_product': 'P(z)=prod_{p<=z}(1-delta_p)',
            'mertens_shape': 'P(z)~C_sieve/(log z)^2 for some C_sieve>0',
            'proof_input': 'delta_p=2/p+O(1/p^2) plus Mertens prime product theorem',
            'two_limit_zero_density': 'choose fixed z with P(z)<epsilon, apply fixed-adelic equidistribution as B->infinity, then let z->infinity',
            'independent_zero_density_reproof': 'R_EB(B)=o(B(log B)^5)',
            'growing_z_uniformity_used': False,
            'log_minus_2_global_count_bound_from_this_elementary_sieve_alone': False,
            'diagnostics': mertens_diag,
        },
        'huang_thin_cover_upgrade': {
            'cover': 'minimal resolution of the Euler-brick double cover -> Y=Bl_4(P1xP1)',
            'generic_degree': 2,
            'domain': 'smooth proper geometrically integral K3 surface',
            'rational_image_contained_in_adelic_image': True,
            'theorem_level_conclusion': 'there exists eta_EB>0 such that R_EB(B) << B(log B)^(5-eta_EB)',
            'physical_metric_transfer': 'fixed multiplicative comparability of anticanonical heights preserves the log-power saving',
            'eta_EB_explicitly_evaluated': False,
        },
        'finite_e9_comparison': finite_comparison,
        'theorem_boundary': {
            'explicit_six_state_adelic_law_proved': True,
            'fixed_finite_prime_independence_proved': True,
            'directionwise_same_local_law_proved': True,
            'local_sieve_reproves_zero_density': True,
            'quantitative_relative_log_saving_proved_via_Huang': True,
            'explicit_eta_EB_proved': False,
            'elementary_growing_prime_uniformity_proved': False,
            'sqrt_B_asymptotic_proved': False,
        },
        'status': {
            'STAGE14_E10': 'COMPLETE_ADELIC_STATE_LAW_LOCAL_SIEVE_AND_THIN_COVER_LOG_SAVING',
            'SIX_STATE_ADELIC_LAW_PROVED': True,
            'FIXED_FINITE_PRIME_PRODUCT_LAW_PROVED': True,
            'LOCAL_BLOCKER_MASS_FORMULA_PROVED': True,
            'P2_P3_ASYMPTOTIC_BLOCKED_MASS': '4/9',
            'LOCAL_SIEVE_ZERO_DENSITY_REPROVED': True,
            'HUANG_GENERIC_FINITE_LOG_SAVING_APPLIES': True,
            'QUANTITATIVE_RELATIVE_SAVING_PROVED': True,
            'EXPLICIT_ETA_EB_EVALUATED': False,
            'NEXT_E_SUPPLEMENT': 'Stage14-e11 explicit thin-cover exponent / growing-prime uniformity',
        },
        'pass': True,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + '\n')
    print(json.dumps(report['status'], indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
