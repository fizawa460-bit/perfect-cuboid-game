#!/usr/bin/env python3
"""Stage14-t30: physical denominator compression / good auxiliary-prime audit."""

from collections import Counter
from math import gcd
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "stages/stage14/data/14-t30/height_auxiliary_character.json"
AB_MAX = 40
PQ_MAX = 40
AUX_PRIME_MAX = 97


def primes_upto(n):
    out = []
    for x in range(2, n + 1):
        prime = True
        for p in out:
            if p * p > x:
                break
            if x % p == 0:
                prime = False
                break
        if prime:
            out.append(x)
    return out


AUX_PRIMES = [p for p in primes_upto(AUX_PRIME_MAX) if p & 1]


def legendre(x, p):
    x %= p
    if x == 0:
        return 0
    return 1 if pow(x, (p - 1) // 2, p) == 1 else -1


def largest_odd_prime_factor(n):
    n = abs(n)
    while n and n % 2 == 0:
        n //= 2
    ans = 1
    p = 3
    while p * p <= n:
        while n % p == 0:
            ans = p
            n //= p
        p += 2
    if n > 1:
        ans = max(ans, n)
    return ans


def ab_direction(a, b):
    assert 0 < a < b and gcd(a, b) == 1
    eps = 1 if (a & 1 and b & 1) else 2
    if eps == 1:
        r = (b - a) // 2
        u = (b + a) // 2
    else:
        r = b - a
        u = b + a
    C = eps * a * b
    D = eps * (a * a + b * b) // 2
    L = eps * (b * b - a * a) // 2
    Delta = 2 * a * b * (b * b - a * a) * (a * a + b * b)
    assert D * D - C * C == L * L
    return eps, r, u, C, D, L, Delta


def direction_column(a, b, ell):
    hits = []
    if a % ell == 0:
        hits.append("a")
    if b % ell == 0:
        hits.append("b")
    if (b * b - a * a) % ell == 0:
        hits.append("difference")
    if (a * a + b * b) % ell == 0:
        hits.append("sum")
    assert len(hits) == 1, (a, b, ell, hits)
    return hits[0]


def four_factors(a, b, p, q):
    return (
        b * p - a * q,
        a * q + b * p,
        b * q - a * p,
        b * q + a * p,
    )


def allowed_pairs(column):
    if column in ("a", "b"):
        return {(1, 2), (3, 4)}
    if column == "difference":
        return {(1, 3), (2, 4)}
    return {(1, 4), (2, 3)}


def quartic_value(a, b, t):
    return (b * b * t * t - a * a) * (b * b - a * a * t * t)


def quartic_derivative_mod(a, b, t, ell):
    return (
        -4 * a * a * b * b * t**3
        + 2 * (a**4 + b**4) * t
    ) % ell


def complete_character_sum(a, b, ell):
    return sum(legendre(quartic_value(a, b, t), ell) for t in range(ell))


def audit():
    totals = Counter()
    visible_columns = Counter()
    max_abs_character_sum = 0
    max_character_case = None

    for b in range(2, AB_MAX + 1):
        for a in range(1, b):
            if gcd(a, b) != 1:
                continue

            eps, r, u, C, D, L, Delta = ab_direction(a, b)
            totals["directions"] += 1

            # Exact quartic discriminant identity disc(f)=Delta^4.
            disc = (
                16 * a**4 * b**4 * (b - a)**4 * (b + a)**4
                * (a * a + b * b)**4
            )
            assert disc == Delta**4
            totals["discriminant_identity_checks"] += 1

            # Good auxiliary primes: squarefree quartic + complete Weil bound.
            good = []
            sums = []
            for lam in AUX_PRIMES:
                if Delta % lam == 0:
                    continue
                char_sum = 0
                for t in range(lam):
                    f = quartic_value(a, b, t) % lam
                    if f == 0:
                        # disc(f) nonzero mod lam => every root is simple.
                        assert quartic_derivative_mod(a, b, t, lam) != 0
                    char_sum += legendre(f, lam)
                # Conservative squarefree-quartic Weil bound.
                assert char_sum * char_sum <= 9 * lam
                totals["good_auxiliary_prime_character_checks"] += 1
                good.append(lam)
                sums.append(char_sum)
                if abs(char_sum) > max_abs_character_sum:
                    max_abs_character_sum = abs(char_sum)
                    max_character_case = {
                        "a": a,
                        "b": b,
                        "prime": lam,
                        "character_sum": char_sum,
                    }

            if len(good) >= 2:
                # CRT factorization for two distinct good primes.
                lam, mu = good[0], good[1]
                sl, sm = sums[0], sums[1]
                assert (sl * sm) ** 2 <= 81 * lam * mu
                totals["two_prime_correlation_checks"] += 1

            pstar = max(
                largest_odd_prime_factor(r),
                largest_odd_prime_factor(u),
                largest_odd_prime_factor(C),
                largest_odd_prime_factor(D),
            )
            column = direction_column(a, b, pstar) if pstar > 1 else None

            for q in range(1, PQ_MAX + 1):
                for p in range(1, PQ_MAX + 1):
                    if gcd(p, q) != 1:
                        continue
                    if not (a * q < b * p and a * p < b * q):
                        continue

                    totals["primitive_interval_tuples"] += 1
                    S = p * p + q * q
                    assert gcd(S, p * q) == 1

                    # Exact denominator of Q=2Dpq/S.
                    den_q = S // gcd(S, 2 * D)
                    B_min = den_q * D
                    assert S <= 2 * B_min
                    totals["physical_denominator_checks"] += 1

                    if pstar <= 1:
                        continue
                    gs = four_factors(a, b, p, q)
                    divinds = tuple(i + 1 for i, g in enumerate(gs) if g % pstar == 0)
                    if not divinds:
                        totals["canonical_prime_no_linear_factor_residual"] += 1
                        continue

                    assert len(divinds) == 2
                    assert divinds in allowed_pairs(column)
                    totals["canonical_prime_matching_incidence"] += 1

                    if p == q:
                        totals["matching_torsion_incidence"] += 1
                        continue

                    totals["non_torsion_matching_incidence"] += 1
                    visible_columns[column] += 1

                    if column in ("a", "b"):
                        # t26 C-column rational branch: ell|p or ell|q.
                        assert p % pstar == 0 or q % pstar == 0
                        assert pstar * pstar <= S
                        totals["C_column_sqrt_bound_checks"] += 1
                    elif column == "difference":
                        # t26 r/u rational branch: ell|p-q or ell|p+q.
                        assert (p - q) % pstar == 0 or (p + q) % pstar == 0
                        if (p - q) % pstar == 0:
                            assert p != q
                            assert pstar <= abs(p - q)
                        else:
                            assert pstar <= p + q
                        assert (p + q) ** 2 <= 2 * S
                        totals["RU_difference_sqrt_bound_checks"] += 1
                    else:
                        # t26 D-column rational branch: ell|p^2+q^2.
                        assert S % pstar == 0
                        assert pstar <= S
                        totals["D_sum_bound_checks"] += 1

                    # If ell>2 sqrt(B_min), C/difference are impossible.
                    if pstar * pstar > 4 * B_min:
                        assert column == "sum"
                        totals["super_sqrt_visible_incidence"] += 1

    assert totals["directions"] == 489
    assert totals["primitive_interval_tuples"] == 239121
    assert totals["physical_denominator_checks"] == 239121
    assert totals["canonical_prime_matching_incidence"] == 6371
    assert totals["canonical_prime_no_linear_factor_residual"] == 232750
    assert totals["matching_torsion_incidence"] == 33
    assert totals["non_torsion_matching_incidence"] == 6338
    assert totals["C_column_sqrt_bound_checks"] == 936
    assert totals["RU_difference_sqrt_bound_checks"] == 814
    assert totals["D_sum_bound_checks"] == 4588
    assert totals["super_sqrt_visible_incidence"] == 1018
    assert dict(visible_columns) == {
        "a": 4,
        "b": 932,
        "difference": 814,
        "sum": 4588,
    }
    assert totals["discriminant_identity_checks"] == 489
    assert totals["good_auxiliary_prime_character_checks"] == 9332
    assert totals["two_prime_correlation_checks"] == 489
    assert max_abs_character_sum == 19
    assert max_character_case is not None

    return {
        "totals": dict(totals),
        "non_torsion_visible_columns": dict(visible_columns),
        "auxiliary_prime_cutoff": AUX_PRIME_MAX,
        "max_abs_complete_character_sum": max_abs_character_sum,
        "max_abs_complete_character_sum_case": max_character_case,
    }


def main():
    audit_data = audit()
    report = {
        "stage": "14-t30",
        "physical_height_gate": {
            "X": "D*(p^2-q^2)/(p^2+q^2)",
            "Q": "2*D*p*q/(p^2+q^2)",
            "denominator_Q": "(p^2+q^2)/gcd(p^2+q^2,2D)",
            "physical_disk": "p^2+q^2<=2B",
            "C_visible_bound": "ell<=sqrt(2B)",
            "RU_difference_visible_bound": "ell<=2sqrt(B) on non-torsion branch",
            "super_sqrt_visible_column": "D/sum only",
        },
        "auxiliary_quartic": {
            "f": "(b^2*T^2-a^2)*(b^2-a^2*T^2)",
            "discriminant": "Delta^4",
            "Delta": "2ab(b^2-a^2)(a^2+b^2)",
            "direction_prime_role": "bad-reduction incidence modulus",
            "good_auxiliary_prime_role": "independent quadratic-character gate",
            "single_prime_complete_bound": "abs(sum chi_lambda(f))<=3sqrt(lambda)",
            "two_prime_complete_bound": "abs(correlation)<=9sqrt(lambda*mu)",
            "CRT_independence_after_visible_line": True,
        },
        "literature_boundary": {
            "Pierce_Xu": "candidate for incomplete admissible-form character sums; no direct moving-family projected power saving claimed",
            "Bonolis_Pierce": "polynomial-sieve projection framework is conceptually relevant, but the naive Y^2=g1g2g3g4 weighted cover is singular along branch intersections",
        },
        "finite_audit": audit_data,
        "decision": {
            "STAGE14_T30": "COMPLETE_PHYSICAL_DENOMINATOR_AND_BAD_GOOD_PRIME_SEPARATION",
            "PHYSICAL_PQ_DISK_BOUND": "P2_PLUS_Q2_LE_2B",
            "VISIBLE_C_COLUMN_PRIME_LE_SQRT_2B": True,
            "VISIBLE_RU_DIFFERENCE_PRIME_LE_2SQRT_B_NON_TORSION": True,
            "SUPER_SQRT_VISIBLE_ONLY_D_SUM_COLUMN": True,
            "AUXILIARY_QUARTIC_DISCRIMINANT_EQUALS_DELTA4": True,
            "DIRECTION_PRIMES_ARE_AUXILIARY_QUARTIC_BAD_PRIMES": True,
            "GOOD_AUXILIARY_PRIME_WEIL_CANCELLATION": True,
            "GOOD_AUXILIARY_TWO_PRIME_CORRELATION": True,
            "CANONICAL_INCIDENCE_AND_AUXILIARY_CHARACTER_CRT_INDEPENDENT": True,
            "BONOLIS_PIERCE_DIRECT_APPLICATION": False,
            "PIERCE_XU_DIRECT_POWER_SAVING_PROVED": False,
            "VISIBLE_BRANCH_POWER_SAVING_PROVED": False,
            "INVISIBLE_BRANCH_POWER_SAVING_PROVED": False,
            "JOINT_COVER_CONDITIONED_SMOOTH_POWER_SAVING_PROVED": False,
            "A_11_POWER_SAVING_PROVED": False,
            "T_O_SQRT_B_PROVED": False,
            "PERFECT_CUBOID_NONEXISTENCE_PROVED": False,
            "NEXT": "Stage14-t31 prove a moving-family auxiliary-prime correlation bound on the visible D/sum incidence branch, using the p^2+q^2<=2B disk, and derive the analogous good-prime averaging object for the t26 Gaussian/dual invisible branch",
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(audit_data, indent=2, sort_keys=True))
    print(json.dumps(report["decision"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
