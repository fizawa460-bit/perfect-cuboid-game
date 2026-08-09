#!/usr/bin/env python3
"""Stage14-t32: unified super-sqrt norm skeleton / split-torus audit."""

from collections import Counter, defaultdict
from math import gcd
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "stages/stage14/data/14-t32/split_torus_norm_sieve.json"
AB_MAX = 40
PQ_MAX = 40
SPLIT_AUX = (13, 17, 29, 37, 41)
INERT_RESONANCE = 11
PI = (1, 2)  # norm 5


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
    eps = 1 if (a & 1 and b & 1) else 2
    if eps == 1:
        r = (b - a) // 2
        u = (b + a) // 2
    else:
        r = b - a
        u = b + a
    C = eps * a * b
    D = eps * (a * a + b * b) // 2
    return eps, r, u, C, D


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
    assert len(hits) == 1
    return hits[0]


def four_factors(a, b, p, q):
    return (
        b * p - a * q,
        a * q + b * p,
        b * q - a * p,
        b * q + a * p,
    )


def unified_norm_skeleton_audit():
    totals = Counter()
    visible_delta = Counter()
    invisible_delta = Counter()
    maxima = Counter()

    for b in range(2, AB_MAX + 1):
        for a in range(1, b):
            if gcd(a, b) != 1:
                continue
            eps, r, u, C, D = ab_direction(a, b)
            ell = max(
                largest_odd_prime_factor(r),
                largest_odd_prime_factor(u),
                largest_odd_prime_factor(C),
                largest_odd_prime_factor(D),
            )
            if ell <= 1 or direction_column(a, b, ell) != "sum":
                continue

            A = a * a + b * b
            for q in range(1, PQ_MAX + 1):
                for p in range(1, PQ_MAX + 1):
                    if gcd(p, q) != 1:
                        continue
                    if not (a * q < b * p and a * p < b * q):
                        continue
                    if p == q:
                        continue

                    S = p * p + q * q
                    den = S // gcd(S, 2 * D)
                    B_min = den * D
                    if ell * ell <= 4 * B_min:
                        continue

                    # Super-sqrt D/sum: a^2+b^2=ell*m with exponent one.
                    assert A % ell == 0 and A < ell * ell
                    m = A // ell
                    assert gcd(m, ell) == 1

                    gs = four_factors(a, b, p, q)
                    divinds = tuple(i + 1 for i, z in enumerate(gs) if z % ell == 0)

                    if divinds:
                        # Visible: S=ell*n, descend p+iq by pi/bar(pi).
                        assert divinds in ((1, 4), (2, 3))
                        assert S % ell == 0 and S < ell * ell
                        n = S // ell
                        k = gcd(n, eps * m)
                        delta = n // k
                        assert k and (eps * m) % k == 0
                        assert den == delta
                        assert B_min == eps * ell * m * delta // 2
                        totals["visible_super_non_torsion"] += 1
                        totals["unified_cofactor_checks"] += 1
                        visible_delta["delta_eq_1" if delta == 1 else "delta_gt_1"] += 1
                        maxima["visible_m"] = max(maxima["visible_m"], m)
                        maxima["visible_normV"] = max(maxima["visible_normV"], n)
                        maxima["visible_delta"] = max(maxima["visible_delta"], delta)
                    else:
                        # Invisible: ell does not divide S; raw p+iq is the cofactor V.
                        assert S % ell != 0
                        k = gcd(S, eps * m)
                        delta = S // k
                        assert k and (eps * m) % k == 0
                        assert den == delta
                        assert B_min == eps * ell * m * delta // 2
                        totals["invisible_super_non_torsion"] += 1
                        totals["unified_cofactor_checks"] += 1
                        invisible_delta["delta_eq_1" if delta == 1 else "delta_gt_1"] += 1
                        maxima["invisible_m"] = max(maxima["invisible_m"], m)
                        maxima["invisible_normV"] = max(maxima["invisible_normV"], S)
                        maxima["invisible_delta"] = max(maxima["invisible_delta"], delta)

    assert totals["visible_super_non_torsion"] == 1018
    assert totals["invisible_super_non_torsion"] == 12190
    assert totals["unified_cofactor_checks"] == 13208
    assert dict(visible_delta) == {"delta_eq_1": 676, "delta_gt_1": 342}
    assert dict(invisible_delta) == {"delta_eq_1": 230, "delta_gt_1": 11960}
    assert dict(maxima) == {
        "visible_m": 26,
        "visible_normV": 34,
        "visible_delta": 25,
        "invisible_m": 26,
        "invisible_normV": 1354,
        "invisible_delta": 685,
    }
    return {
        "totals": dict(totals),
        "visible_delta_counts": dict(visible_delta),
        "invisible_delta_counts": dict(invisible_delta),
        "maxima": dict(maxima),
    }


def cmul(z, w, p):
    x, y = z
    u, v = w
    return ((x * u - y * v) % p, (x * v + y * u) % p)


def cbar(z, p):
    return (z[0] % p, (-z[1]) % p)


def norm(z, p):
    return (z[0] * z[0] + z[1] * z[1]) % p


def universal_form(a, b, p, q):
    return (b * b * p * p - a * a * q * q) * (b * b * q * q - a * a * p * p)


def circle_points(lam):
    circles = defaultdict(list)
    for x in range(lam):
        for y in range(lam):
            r = norm((x, y), lam)
            if r:
                circles[r].append((x, y))
    return circles


def max_norm_circle_correlation(lam, opposite=False):
    circles = circle_points(lam)
    ppi = cbar(PI, lam) if opposite else PI
    dirs = {
        m: [cmul(PI, U, lam) for U in pts]
        for m, pts in circles.items()
    }
    covs = {
        n: [cmul(ppi, V, lam) for V in pts]
        for n, pts in circles.items()
    }

    max_abs = -1
    max_case = None
    for m, Apts in dirs.items():
        for n, Ppts in covs.items():
            total = 0
            for a, b in Apts:
                for p, q in Ppts:
                    total += legendre(universal_form(a, b, p, q), lam)
            if abs(total) > max_abs:
                max_abs = abs(total)
                max_case = {
                    "m": m,
                    "n": n,
                    "sum": total,
                    "circle_m_size": len(Apts),
                    "circle_n_size": len(Ppts),
                }
    return max_abs, max_case


def split_torus_audit():
    split = {}
    for lam in SPLIT_AUX:
        assert lam % 4 == 1 and 5 % lam != 0
        same_abs, same_case = max_norm_circle_correlation(lam, opposite=False)
        opp_abs, opp_case = max_norm_circle_correlation(lam, opposite=True)
        assert same_abs <= 25 * lam
        assert opp_abs <= 25 * lam
        split[str(lam)] = {
            "same_max_abs": same_abs,
            "same_case": same_case,
            "opposite_max_abs": opp_abs,
            "opposite_case": opp_case,
            "bound_25lambda": 25 * lam,
        }

    assert {p: split[str(p)]["same_max_abs"] for p in SPLIT_AUX} == {
        13: 64,
        17: 160,
        29: 144,
        37: 16,
        41: 288,
    }

    inert_abs, inert_case = max_norm_circle_correlation(INERT_RESONANCE, opposite=False)
    assert inert_abs == 144
    assert inert_case["m"] == 1 and inert_case["n"] == 2
    assert inert_abs == (INERT_RESONANCE + 1) ** 2

    return {
        "split_auxiliary": split,
        "inert_resonance": {
            "prime": INERT_RESONANCE,
            "pi": "1+2i",
            "max_abs": inert_abs,
            "case": inert_case,
            "equals_full_circle_product": True,
        },
    }


def main():
    skeleton = unified_norm_skeleton_audit()
    torus = split_torus_audit()
    report = {
        "stage": "14-t32",
        "unified_super_sqrt_norm_skeleton": {
            "direction": "a+ib=pi*U, N(U)=m, N(pi)=ell",
            "visible_cover": "p+iq=pi^(+/-)*V, N(V)=k*delta",
            "invisible_cover": "V=p+iq, N(V)=k*delta",
            "divisor_coupling": "k|epsilon*m",
            "physical_scale": "epsilon*ell*m*delta/2<=B",
            "fixed_ell_unsieved_mass": "B/ell*B^o(1)",
        },
        "split_torus_theorem": {
            "auxiliary_primes": "lambda=1 mod 4, lambda not dividing ell*Delta*m*n",
            "circle_coordinate": "s=x+iota*y, x-iota*y=R/s",
            "linear_product_formula": "Re(cz)Im(cz)=(c_+^2*s^4-c_-^2*R^2)/(4*iota*s^2)",
            "untwisted_1d_bound": "3sqrt(lambda)",
            "twisted_1d_bound": "4sqrt(lambda)",
            "two_torus_identity": "sum A(s/t)B(st)=sum(A)sum(B)+sum(eta*A)sum(eta*B)",
            "single_prime_correlation": "<=25lambda",
            "two_prime_correlation": "<=625lambda*mu",
            "inert_uniform_bound_valid": False,
        },
        "finite_audit": {
            "norm_skeleton": skeleton,
            "torus": torus,
        },
        "analytic_boundary": {
            "angular_complete_correlation_closed": True,
            "integral_norm_circles_are_sparse": "r_2(n)<=4tau(n)=n^o(1)",
            "remaining_sum": "divisor-coupled hyperbolic norm-index average over m,delta,k and Gaussian representations",
            "quadratic_Hecke_large_sieve_over_Qi": "structurally relevant; transfer of the Stage14 character with canonical-ell and divisor coupling not yet proved",
        },
        "decision": {
            "STAGE14_T32": "COMPLETE_SPLIT_TORUS_NORM_CORRELATION_AND_UNIFIED_COFACTOR_SKELETON",
            "VISIBLE_INVISIBLE_SUPER_SQRT_NORM_SKELETON_UNIFIED": True,
            "UNIFIED_NORM_SKELETON": "N(U)=m,N(V)=k*delta,k|epsilon*m,m*delta<<B/ell",
            "FIXED_ELL_UNSIEVED_NORM_MASS": "B/ell*B^o(1)",
            "INERT_AUXILIARY_NORM_CIRCLE_RESONANCE_EXISTS": True,
            "SPLIT_AUXILIARY_PRIME_RESTRICTION_REQUIRED_FOR_TORUS_BOUND": True,
            "SPLIT_NORM_CIRCLE_PARAMETERIZATION": True,
            "SPLIT_TORUS_TWO_FACTOR_IDENTITY": True,
            "SPLIT_GOOD_PRIME_NORM_CIRCLE_CORRELATION": "O(lambda)",
            "SPLIT_GOOD_TWO_PRIME_NORM_CIRCLE_CORRELATION": "O(lambda*mu)",
            "ANGULAR_COMPLETE_CORRELATION_CLOSED": True,
            "GAUSSIAN_HECKE_LARGE_SIEVE_TRANSFER_PROVED": False,
            "NORM_INDEX_HYPERBOLIC_CORRELATION_POWER_SAVING_PROVED": False,
            "VISIBLE_BRANCH_POWER_SAVING_PROVED": False,
            "INVISIBLE_BRANCH_POWER_SAVING_PROVED": False,
            "JOINT_COVER_CONDITIONED_SMOOTH_POWER_SAVING_PROVED": False,
            "A_11_POWER_SAVING_PROVED": False,
            "T_O_SQRT_B_PROVED": False,
            "PERFECT_CUBOID_NONEXISTENCE_PROVED": False,
            "NEXT": "Stage14-t33 convert the split-torus character into a quadratic Hecke-family symbol over Q(i) and prove a large-sieve bound for the divisor-coupled norm-index sum Sigma(lambda,mu;ell;X,B)",
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(skeleton, indent=2, sort_keys=True))
    print(json.dumps(torus, indent=2, sort_keys=True))
    print(json.dumps(report["decision"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
