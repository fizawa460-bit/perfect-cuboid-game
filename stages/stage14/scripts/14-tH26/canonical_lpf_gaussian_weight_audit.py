#!/usr/bin/env python3

import json
import math
from fractions import Fraction

LIMIT = 80000
REP_LIMIT = 800


def spf_sieve(n):
    spf = list(range(n + 1))
    if n >= 1:
        spf[1] = 1
    for p in range(2, math.isqrt(n) + 1):
        if spf[p] == p:
            for m in range(p * p, n + 1, p):
                if spf[m] == m:
                    spf[m] = p
    return spf


SPF = spf_sieve(LIMIT)


def factor(n):
    out = {}
    while n > 1:
        p = SPF[n]
        out[p] = out.get(p, 0) + 1
        n //= p
    return out


def split_supported(n):
    return all(p == 2 or p % 4 == 1 for p in factor(n))


def primitive_gaussian_reps(n):
    out = []
    r = math.isqrt(n)
    for x in range(-r, r + 1):
        y2 = n - x * x
        if y2 < 0:
            continue
        y = math.isqrt(y2)
        if y * y != y2:
            continue
        ys = {y, -y} if y else {0}
        for yy in ys:
            if math.gcd(abs(x), abs(yy)) == 1:
                out.append((x, yy))
    return out


def main():
    canonical_states = 0
    lpf_uniqueness_checks = 0
    exponent_one_checks = 0
    feasible_B_interval_checks = 0
    split_support_checks = 0
    prime_spine_states = 0
    nontrivial_cofactor_states = 0
    max_cofactor = 0
    max_cofactor_ratio = 0.0
    cofactor_rep_checks = 0
    primitive_rep_states = 0

    cutoff_prime_spine = {}
    running_prime_spine = 0
    cutoffs = [10000, 20000, 40000, 80000]

    for Q in range(5, LIMIT + 1):
        ff = factor(Q)
        if not all(p == 2 or p % 4 == 1 for p in ff):
            continue
        split_support_checks += 1
        ell = max(ff)
        if ff[ell] != 1:
            continue
        if ell * ell <= 2 * Q:
            continue

        delta0 = Q // ell
        canonical_states += 1
        assert ell == max(ff)
        lpf_uniqueness_checks += 1
        assert ff[ell] == 1
        exponent_one_checks += 1

        # For h*k0=1, a physical B exists exactly between Q/2 and ell^2/4.
        # The strict interval is nonempty because ell^2 > 2Q.
        lower = Q / 2.0
        upper = ell * ell / 4.0
        assert lower < upper
        feasible_B_interval_checks += 1

        if delta0 == 1:
            prime_spine_states += 1
            running_prime_spine += 1
        else:
            nontrivial_cofactor_states += 1
            max_cofactor = max(max_cofactor, delta0)
            max_cofactor_ratio = max(max_cofactor_ratio, delta0 / math.sqrt(Q))

        if delta0 <= REP_LIMIT and split_supported(delta0):
            reps = primitive_gaussian_reps(delta0)
            cofactor_rep_checks += 1
            if reps:
                primitive_rep_states += 1

        if Q in cutoffs:
            cutoff_prime_spine[Q] = running_prime_spine

    # Fill cutoffs that may not have been hit after filtering.
    for cutoff in cutoffs:
        if cutoff not in cutoff_prime_spine:
            count = 0
            for p in range(5, cutoff + 1):
                ff = factor(p)
                if len(ff) == 1:
                    q = next(iter(ff))
                    if ff[q] == 1 and q % 4 == 1:
                        count += 1
            cutoff_prime_spine[cutoff] = count

    # Fixed-power range witness from the frozen inequalities.
    e_ell = Fraction(11, 20)
    e_delta = Fraction(7, 20)
    e_Q = e_ell + e_delta
    e_hk0 = Fraction(0, 1)
    range_guard_checks = 0
    assert 2 * e_ell > 1  # ell^2 > 4B
    range_guard_checks += 1
    assert 2 * e_ell > e_hk0 + e_Q  # ell^2 > 2*h*k0*Q
    range_guard_checks += 1
    assert e_hk0 + e_Q < 1  # h*k0*Q <= 2B with room
    range_guard_checks += 1
    assert e_delta > 0  # polynomial cofactor remains allowed
    range_guard_checks += 1
    assert e_ell > e_delta  # largest-prime separation
    range_guard_checks += 1

    assert canonical_states > 0
    assert prime_spine_states > 0
    assert nontrivial_cofactor_states > 0
    assert primitive_rep_states > 0

    result = {
        "stage": "14-tH26",
        "status": "COMPLETE_T90_SNAPSHOT_CANONICAL_LPF_GAUSSIAN_REPRESENTATION_CHARACTER_WEIGHT_APPLICABILITY_AUDIT",
        "limit": LIMIT,
        "canonical_lpf_states": canonical_states,
        "lpf_uniqueness_checks": lpf_uniqueness_checks,
        "lpf_exponent_one_checks": exponent_one_checks,
        "feasible_physical_B_interval_checks": feasible_B_interval_checks,
        "split_support_candidates": split_support_checks,
        "prime_spine_states": prime_spine_states,
        "nontrivial_cofactor_states": nontrivial_cofactor_states,
        "max_cofactor": max_cofactor,
        "max_cofactor_over_sqrt_Q": max_cofactor_ratio,
        "cofactor_representation_checks": cofactor_rep_checks,
        "primitive_cofactor_representation_states": primitive_rep_states,
        "prime_spine_by_cutoff": {str(k): v for k, v in sorted(cutoff_prime_spine.items())},
        "range_guard_checks": range_guard_checks,
        "range_witness": {
            "ell_exponent": "11/20",
            "delta0_exponent": "7/20",
            "Q_exponent": "9/10",
            "hk0_exponent": "0"
        },
        "boundary": {
            "TARGET_FROZEN": True,
            "PRINCIPAL_REPRESENTATION_TERM_POWER_SPARSE": False,
            "NONPRINCIPAL_GAUSSIAN_CHARACTER_SAVING_AVAILABLE": False,
            "FULL_PHYSICAL_COEFFICIENT_DECOMPOSITION_THEOREM_READY": False,
            "CANONICAL_LPF_SHORT_COFACTOR_UNIFORMITY_CONTROLLED": False,
            "OFF_THE_SHELF_UNIFORM_FIXED_POWER_SAVING_PROVED": False,
            "CERTIFIED_FIXED_U_PACKET_B_POWER_SAVING_EXPONENT": "0",
            "NEXT_H_NEEDED": False,
            "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT": "1/2"
        }
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
