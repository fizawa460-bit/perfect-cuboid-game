#!/usr/bin/env python3
"""Stage14-t31: Gaussian cofactor / moving auxiliary correlation audit."""

from collections import Counter
from math import gcd, isqrt
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "stages/stage14/data/14-t31/gaussian_cofactor_sieve.json"
AB_MAX = 40
PQ_MAX = 40
COMPLETE_PRIMES = (3, 5, 7, 11, 13)


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


def cover_value(C, D, p, q):
    return (4 * D * D - 2 * C * C) * p * p * q * q - C * C * (p**4 + q**4)


def gaussian_prime_rep(ell):
    for s in range(1, isqrt(ell) + 1):
        t2 = ell - s * s
        t = isqrt(t2)
        if t > 0 and t * t == t2:
            return s, t
    raise AssertionError(("no sum-of-two-squares representation", ell))


def gaussian_div(x, y, s, t):
    """Return (x+iy)/(s+it) if Gaussian-integral, else None."""
    den = s * s + t * t
    nr = x * s + y * t
    ni = y * s - x * t
    if nr % den or ni % den:
        return None
    return nr // den, ni // den


def root_minus_one_mod_p2(p, cache):
    if p in cache:
        return cache[p]
    r = next(x for x in range(1, p) if (x * x + 1) % p == 0)
    c = (r * r + 1) // p
    k = (-c * pow(2 * r, -1, p)) % p
    rho = r + k * p
    assert (rho * rho + 1) % (p * p) == 0
    cache[p] = rho
    return rho


def universal_form(a, b, p, q):
    return (b * b * p * p - a * a * q * q) * (b * b * q * q - a * a * p * p)


def complete_four_variable_sum(lam):
    total = 0
    for a in range(lam):
        for b in range(lam):
            for p in range(lam):
                for q in range(lam):
                    total += legendre(universal_form(a, b, p, q), lam)
    # A conservative constant-2 version of O(lambda^(7/2)).
    assert total * total <= 4 * lam**7
    return total


def audit():
    totals = Counter()
    matched = Counter()
    eps_counts = Counter()
    delta_counts = Counter()
    canonical_primes = set()
    rho_cache = {}
    max_m = max_n = max_delta = max_m_delta = 0

    for b in range(2, AB_MAX + 1):
        for a in range(1, b):
            if gcd(a, b) != 1:
                continue
            totals["directions"] += 1
            eps, r, u, C, D, L, Delta = ab_direction(a, b)
            ell = max(
                largest_odd_prime_factor(r),
                largest_odd_prime_factor(u),
                largest_odd_prime_factor(C),
                largest_odd_prime_factor(D),
            )
            if ell <= 1:
                continue
            column = direction_column(a, b, ell)

            for q in range(1, PQ_MAX + 1):
                for p in range(1, PQ_MAX + 1):
                    if gcd(p, q) != 1:
                        continue
                    if not (a * q < b * p and a * p < b * q):
                        continue
                    totals["primitive_interval_tuples"] += 1

                    S = p * p + q * q
                    den_q = S // gcd(S, 2 * D)
                    B_min = den_q * D
                    gs = four_factors(a, b, p, q)
                    divinds = tuple(i + 1 for i, z in enumerate(gs) if z % ell == 0)

                    # Kernel-invisible D/sum residual: the t26 Gaussian state is
                    # a local root choice, not a rational p/q congruence.
                    if column == "sum" and not divinds:
                        assert ell % 4 == 1
                        assert S % ell != 0
                        mod = ell * ell
                        F = cover_value(C, D, p, q)
                        assert (F + C * C * S * S) % mod == 0
                        rho = root_minus_one_mod_p2(ell, rho_cache)
                        Wloc = (rho * C * S) % mod
                        assert (Wloc * Wloc - F) % mod == 0
                        totals["invisible_sum_local_root_checks"] += 1

                    if p == q or not divinds:
                        continue
                    if ell * ell <= 4 * B_min:
                        continue

                    # t30 says every such visible non-torsion incidence is sum-column.
                    assert column == "sum"
                    assert divinds in ((1, 4), (2, 3))
                    totals["super_sqrt_visible_incidences"] += 1
                    canonical_primes.add(ell)
                    matched[f"{divinds[0]}{divinds[1]}"] += 1
                    eps_counts[str(eps)] += 1

                    A = a * a + b * b
                    assert A % ell == 0 and S % ell == 0
                    assert ell * ell > A and ell * ell > S
                    m = A // ell
                    n = S // ell
                    assert gcd(m, ell) == 1 and gcd(n, ell) == 1
                    totals["exact_exponent_one_norm_checks"] += 1

                    delta = n // gcd(n, eps * m)
                    assert den_q == delta
                    assert B_min == eps * ell * m * delta // 2
                    assert eps * ell * m * delta <= 2 * B_min
                    totals["scale_cofactor_identity_checks"] += 1
                    if delta == 1:
                        delta_counts["delta_eq_1"] += 1
                    else:
                        delta_counts["delta_gt_1"] += 1

                    max_m = max(max_m, m)
                    max_n = max(max_n, n)
                    max_delta = max(max_delta, delta)
                    max_m_delta = max(max_m_delta, m * delta)

                    # Matched factors have exact ell-adic exponent one because 0<g_i<ell^2.
                    for idx in divinds:
                        z = gs[idx - 1]
                        assert 0 < z < ell * ell
                        assert z % ell == 0 and z % (ell * ell) != 0
                        totals["matched_factor_exact_valuation_checks"] += 1

                    # Gaussian quotient/orientation audit.
                    s, t = gaussian_prime_rep(ell)
                    adivs = {}
                    pdivs = {}
                    for label, (ss, tt) in (("pi", (s, t)), ("bar", (s, -t))):
                        z = gaussian_div(a, b, ss, tt)
                        if z is not None:
                            adivs[label] = z
                        z = gaussian_div(p, q, ss, tt)
                        if z is not None:
                            pdivs[label] = z
                    assert len(adivs) == 1 and len(pdivs) == 1
                    alabel = next(iter(adivs))
                    plabel = next(iter(pdivs))
                    U = adivs[alabel]
                    V = pdivs[plabel]
                    assert U[0] * U[0] + U[1] * U[1] == m
                    assert V[0] * V[0] + V[1] * V[1] == n
                    if divinds == (1, 4):
                        assert alabel == plabel
                        totals["same_gaussian_orientation_checks"] += 1
                    else:
                        assert alabel != plabel
                        totals["opposite_gaussian_orientation_checks"] += 1
                    totals["gaussian_cofactor_norm_checks"] += 1

    assert totals["directions"] == 489
    assert totals["primitive_interval_tuples"] == 239121
    assert totals["super_sqrt_visible_incidences"] == 1018
    assert totals["exact_exponent_one_norm_checks"] == 1018
    assert totals["scale_cofactor_identity_checks"] == 1018
    assert totals["gaussian_cofactor_norm_checks"] == 1018
    assert totals["same_gaussian_orientation_checks"] == 509
    assert totals["opposite_gaussian_orientation_checks"] == 509
    assert totals["matched_factor_exact_valuation_checks"] == 2036
    assert totals["invisible_sum_local_root_checks"] == 211712
    assert dict(matched) == {"14": 509, "23": 509}
    assert dict(eps_counts) == {"2": 594, "1": 424}
    assert dict(delta_counts) == {"delta_eq_1": 676, "delta_gt_1": 342}
    assert len(canonical_primes) == 82
    assert min(canonical_primes) == 5 and max(canonical_primes) == 1373
    assert (max_m, max_n, max_delta, max_m_delta) == (26, 34, 25, 50)

    complete = {str(lam): complete_four_variable_sum(lam) for lam in COMPLETE_PRIMES}
    assert complete == {"3": 0, "5": 384, "7": 0, "11": 0, "13": 12672}

    return {
        "totals": dict(totals),
        "matched_pair_counts": dict(matched),
        "epsilon_counts": dict(eps_counts),
        "delta_counts": dict(delta_counts),
        "canonical_prime_summary": {
            "distinct": len(canonical_primes),
            "min": min(canonical_primes),
            "max": max(canonical_primes),
        },
        "cofactor_maxima": {
            "m": max_m,
            "n": max_n,
            "delta": max_delta,
            "m_times_delta": max_m_delta,
        },
        "sample_complete_four_variable_character_sums": complete,
    }


def main():
    audit_data = audit()
    report = {
        "stage": "14-t31",
        "super_sqrt_visible": {
            "norm_descent": "a^2+b^2=ell*m, p^2+q^2=ell*n with v_ell=1",
            "cofactor_bounds": "m,n<sqrt(B)",
            "scale_identity": "delta=n/gcd(n,epsilon*m), epsilon*ell*m*delta/2<=B",
            "gaussian_orientation_14": "same pi orientation",
            "gaussian_orientation_23": "opposite pi orientation",
            "matched_factor_valuation": "v_ell(g_i)=1",
            "rational_even_invisible": False,
        },
        "moving_auxiliary_correlation": {
            "complete_4d_single_prime": "O(lambda^(7/2))",
            "complete_4d_two_prime": "O((lambda*mu)^(7/2))",
            "box_correlation": "HU^2*HV^2*(L^-1+L^2/HU)*B^o(1)",
            "balanced_L": "HU^(1/3)",
            "square_sieve_saving": "HU^(-1/3+o(1))",
            "shell_bound": "B*X^(5/6)*ell^(-11/6+o(1))",
            "closes_direction_projection": False,
        },
        "invisible_branch": {
            "canonical_prime_role": "local square-root label, not rational p/q incidence",
            "good_auxiliary_object": "chi_lambda(F_ab(p,q)), lambda not dividing Delta",
            "CRT_independent_from_local_root_label": True,
        },
        "finite_audit": audit_data,
        "decision": {
            "STAGE14_T31": "COMPLETE_GAUSSIAN_COFACTOR_AND_MOVING_AUXILIARY_CORRELATION_BOUNDARY",
            "SUPER_SQRT_VISIBLE_NORMS_HAVE_ELL_EXACT_EXPONENT_ONE": True,
            "SUPER_SQRT_VISIBLE_GAUSSIAN_COFACTOR_COMPRESSION": True,
            "SUPER_SQRT_MATCHED_G_FACTORS_HAVE_ELL_EXACT_EXPONENT_ONE": True,
            "SUPER_SQRT_RATIONAL_EVEN_INVISIBLE_BRANCH_EMPTY": True,
            "PHYSICAL_SCALE_COFACTOR_IDENTITY": True,
            "PHYSICAL_SCALE_THIN_NORM_CONDITION": True,
            "GOOD_AUXILIARY_ADMISSIBILITY_SURVIVES_GAUSSIAN_DESCENT": True,
            "FIXED_ELL_MOVING_FAMILY_COMPLETE_CORRELATION_POWER_SAVING": True,
            "FIXED_ELL_COFACTOR_BOX_SQUARE_SIEVE_POWER_SAVING": True,
            "FIXED_ELL_BOX_SIEVE_EXPONENT": "H_U^(-1/3+o(1))",
            "BOX_SIEVE_CLOSES_DIRECTION_PROJECTION": False,
            "INVISIBLE_CANONICAL_PRIME_GIVES_RATIONAL_PQ_INCIDENCE": False,
            "INVISIBLE_GOOD_AUXILIARY_SQUARE_SIEVE_OBJECT_DEFINED": True,
            "VISIBLE_BRANCH_POWER_SAVING_PROVED": False,
            "INVISIBLE_BRANCH_POWER_SAVING_PROVED": False,
            "JOINT_COVER_CONDITIONED_SMOOTH_POWER_SAVING_PROVED": False,
            "A_11_POWER_SAVING_PROVED": False,
            "T_O_SQRT_B_PROVED": False,
            "PERFECT_CUBOID_NONEXISTENCE_PROVED": False,
            "NEXT": "Stage14-t32 auxiliary-character sieve on Gaussian norm circles with n=k*delta, k|epsilon*m and m*delta<<B/ell; compare visible rational and invisible local-root states without enlarging to full cofactor boxes",
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(audit_data, indent=2, sort_keys=True))
    print(json.dumps(report["decision"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
