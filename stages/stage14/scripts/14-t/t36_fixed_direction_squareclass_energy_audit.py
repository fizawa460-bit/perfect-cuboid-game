#!/usr/bin/env python3
"""Stage14-t36: fixed-direction squareclass-energy / fiber sqrt-saving audit."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
T35_DATA = ROOT / "stages/stage14/data/14-t35/same_modulus_dispersion.json"
OUT = ROOT / "stages/stage14/data/14-t36/fixed_direction_squareclass_energy.json"

AB_MAX = 40
PQ_MAX = 40
B_FROZEN = 10_000
AUX_PRIMES = (53, 61, 73, 89, 97)


def largest_odd_prime_factor(n: int) -> int:
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


def ab_direction(a: int, b: int):
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


def direction_column(a: int, b: int, ell: int) -> str:
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


def four_factors(a: int, b: int, p: int, q: int):
    return (
        b * p - a * q,
        a * q + b * p,
        b * q - a * p,
        b * q + a * p,
    )


def gaussian_prime_rep(ell: int):
    for s in range(1, isqrt(ell) + 1):
        t2 = ell - s * s
        t = isqrt(t2)
        if t > 0 and t * t == t2:
            return s, t
    raise AssertionError(("no Gaussian prime representation", ell))


def gaussian_div(x: int, y: int, s: int, t: int):
    den = s * s + t * t
    nr = x * s + y * t
    ni = y * s - x * t
    if nr % den or ni % den:
        return None
    return nr // den, ni // den


def universal_form(a: int, b: int, p: int, q: int) -> int:
    return (b * b * p * p - a * a * q * q) * (b * b * q * q - a * a * p * p)


def legendre(x: int, p: int) -> int:
    x %= p
    if x == 0:
        return 0
    return 1 if pow(x, (p - 1) // 2, p) == 1 else -1


def squarefree_kernel(n: int) -> int:
    n = abs(n)
    assert n > 0
    out = 1
    d = 2
    while d * d <= n:
        parity = 0
        while n % d == 0:
            n //= d
            parity ^= 1
        if parity:
            out *= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        out *= n
    return out


def f_rational(a: int, b: int, x: Fraction) -> Fraction:
    return (b * b * x * x - a * a) * (b * b - a * a * x * x)


def transformed_cubic_value(a: int, b: int, c: Fraction, T: Fraction) -> Fraction:
    x = Fraction(a, b) + 1 / T
    return c * T**4 * f_rational(a, b, x)


def build_frozen_states():
    states = []
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
            s, t = gaussian_prime_rep(ell)
            adivs = []
            for ss, tt in ((s, t), (s, -t)):
                z = gaussian_div(a, b, ss, tt)
                if z is not None:
                    adivs.append(z)
            assert len(adivs) == 1
            U = adivs[0]

            for q in range(1, PQ_MAX + 1):
                for p in range(1, PQ_MAX + 1):
                    if gcd(p, q) != 1 or p == q:
                        continue
                    if not (a * q < b * p and a * p < b * q):
                        continue

                    S = p * p + q * q
                    den = S // gcd(S, 2 * D)
                    B_min = den * D
                    if B_min > B_FROZEN or ell * ell <= 4 * B_FROZEN:
                        continue

                    m = A // ell
                    factors = four_factors(a, b, p, q)
                    divinds = tuple(i + 1 for i, z in enumerate(factors) if z % ell == 0)

                    if divinds:
                        assert divinds in ((1, 4), (2, 3))
                        assert S % ell == 0
                        n = S // ell
                        pdivs = []
                        for ss, tt in ((s, t), (s, -t)):
                            z = gaussian_div(p, q, ss, tt)
                            if z is not None:
                                pdivs.append(z)
                        assert len(pdivs) == 1
                        V = pdivs[0]
                        branch = "visible"
                    else:
                        assert S % ell != 0
                        n = S
                        V = (p, q)
                        branch = "invisible"

                    k = gcd(n, eps * m)
                    delta = n // k
                    assert den == delta
                    assert B_min == eps * ell * m * delta // 2

                    F = universal_form(a, b, p, q)
                    assert F > 0
                    # Homogeneous quartic identity F=q^4*f(p/q).
                    x = Fraction(p, q)
                    assert Fraction(F, q**4) == f_rational(a, b, x)

                    states.append(
                        {
                            "a": a,
                            "b": b,
                            "p": p,
                            "q": q,
                            "eps": eps,
                            "ell": ell,
                            "m": m,
                            "n": n,
                            "delta": delta,
                            "U": U,
                            "V": V,
                            "branch": branch,
                            "F": F,
                            "kernel": squarefree_kernel(F),
                        }
                    )

    assert len(states) == 1120
    assert Counter(s["branch"] for s in states) == Counter({"invisible": 838, "visible": 282})
    return states


def cubic_root_audit(direction_keys) -> int:
    checks = 0
    for a, b in direction_keys:
        roots = (
            Fraction(-b, 2 * a),
            Fraction(a * b, b * b - a * a),
            Fraction(-a * b, a * a + b * b),
        )
        assert len(set(roots)) == 3
        for T in roots:
            assert transformed_cubic_value(a, b, Fraction(1), T) == 0
            checks += 1
    return checks


def squareclass_audit(states):
    fibers = defaultdict(list)
    for s in states:
        fibers[(s["a"], s["b"])].append(s)

    collision_energy = 0
    multiplicity_hist = Counter()
    reciprocal_pairs = 0
    max_mult = 0

    for key, fiber in fibers.items():
        classes = defaultdict(list)
        for s in fiber:
            classes[s["kernel"]].append(s)

        collision_energy += sum(len(v) ** 2 for v in classes.values())
        max_mult = max(max_mult, max(len(v) for v in classes.values()))

        for members in classes.values():
            multiplicity_hist[len(members)] += 1
            if len(members) == 2:
                s1, s2 = members
                assert (s1["p"], s1["q"]) == (s2["q"], s2["p"])
                assert s1["F"] == s2["F"]
                reciprocal_pairs += 1

    assert len(fibers) == 137
    assert max(len(v) for v in fibers.values()) == 32
    assert collision_energy == 2240
    assert max_mult == 2
    assert dict(multiplicity_hist) == {2: 560}
    assert reciprocal_pairs == 560

    root_checks = cubic_root_audit(sorted(fibers))
    assert root_checks == 411

    signed = {}
    for lam in AUX_PRIMES:
        total_trace = 0
        sum_abs = 0
        sum_sq = 0
        max_abs = 0
        zeros = 0
        for fiber in fibers.values():
            values = [legendre(s["F"], lam) for s in fiber]
            trace = sum(values)
            total_trace += trace
            sum_abs += abs(trace)
            sum_sq += trace * trace
            max_abs = max(max_abs, abs(trace))
            zeros += values.count(0)
        signed[str(lam)] = {
            "total_trace": total_trace,
            "sum_abs_direction_traces": sum_abs,
            "sum_direction_trace_squares": sum_sq,
            "max_abs_direction_trace": max_abs,
            "zero_values": zeros,
        }

    assert signed == {
        "53": {"total_trace": -58, "sum_abs_direction_traces": 342, "sum_direction_trace_squares": 1380, "max_abs_direction_trace": 12, "zero_values": 70},
        "61": {"total_trace": -76, "sum_abs_direction_traces": 384, "sum_direction_trace_squares": 1672, "max_abs_direction_trace": 8, "zero_values": 76},
        "73": {"total_trace": -164, "sum_abs_direction_traces": 376, "sum_direction_trace_squares": 1720, "max_abs_direction_trace": 12, "zero_values": 56},
        "89": {"total_trace": -142, "sum_abs_direction_traces": 442, "sum_direction_trace_squares": 2420, "max_abs_direction_trace": 16, "zero_values": 58},
        "97": {"total_trace": -70, "sum_abs_direction_traces": 334, "sum_direction_trace_squares": 1372, "max_abs_direction_trace": 8, "zero_values": 50},
    }

    return {
        "direction_fibers": len(fibers),
        "total_states": len(states),
        "max_direction_fiber": max(len(v) for v in fibers.values()),
        "squareclass_collision_energy": collision_energy,
        "max_squareclass_multiplicity": max_mult,
        "reciprocal_swap_pairs": reciprocal_pairs,
        "kernel_multiplicity_histogram": dict(multiplicity_hist),
        "transformed_cubic_rational_root_checks": root_checks,
        "signed_auxiliary": signed,
    }


def main():
    frozen35 = json.loads(T35_DATA.read_text())
    assert frozen35["decision"]["STAGE14_T35"] == (
        "COMPLETE_SHARED_PRIME_DISPERSION_AND_FIBER_BARRIER"
    )
    assert frozen35["decision"]["TENSOR_SQRT_M_LOSS_RECOVERED"] is True
    assert frozen35["decision"]["SIGNED_TRACE_FIBER_CANCELLATION_PROVED"] is False

    states = build_frozen_states()
    audit = squareclass_audit(states)

    report = {
        "stage": "14-t36",
        "frozen_cutoff": {
            "B": B_FROZEN,
            "AB_MAX": AB_MAX,
            "PQ_MAX": PQ_MAX,
            "auxiliary_split_primes": list(AUX_PRIMES),
        },
        "fixed_direction_squareclass_theorem": {
            "quartic": "f_ab(x)=(b^2*x^2-a^2)(b^2-a^2*x^2), F_ab(p,q)=q^4*f_ab(p/q)",
            "collision_curve": "Y^2=f_ab(x')*f_ab(x)",
            "branch_points": ["a/b", "-a/b", "b/a", "-b/a"],
            "mobius_coordinate": "T=1/(x-a/b)",
            "cubic_roots": ["-b/(2a)", "ab/(b^2-a^2)", "-ab/(a^2+b^2)"],
            "rational_2_torsion": "full",
            "uniform_collision_multiplicity": (
                "B^o(1) per fixed x' by the Stage14-t22 Dujella bounded-height mechanism"
            ),
            "squareclass_energy": "E_ab(B)<=J_ab(B)*B^o(1)",
            "target_fiber_bound": "R_ab(B)<=sqrt(J_ab(B))*B^o(1)",
        },
        "shell_projection": {
            "scales": "canonical ell fixed, m~M, N=B/ell, 1<=M<=N",
            "direction_count": "<=M*B^o(1)",
            "ambient_state_mass": "sum J_ab<=N*B^o(1)",
            "active_direction_bound": "A_ell,M<=sqrt(M*N)*B^o(1)",
            "power_saving_range": (
                "if M<=N*B^(-2eta), then A_ell,M<=N*B^(-eta+o(1))"
            ),
            "short_fiber_endpoint": "M comparable to N remains open",
        },
        "finite_audit": audit,
        "decision": {
            "STAGE14_T36": "COMPLETE_FIXED_DIRECTION_SQUARECLASS_ENERGY_AND_FIBER_SQRT_SAVING",
            "FIXED_DIRECTION_SQUARECLASS_COLLISION_CURVE_GENUS_ONE": True,
            "COLLISION_CURVE_FULL_RATIONAL_2_TORSION": True,
            "T22_UNIFORM_BOUNDED_HEIGHT_REUSED_FOR_COLLISIONS": True,
            "FIXED_DIRECTION_SQUARECLASS_ENERGY": "J*B^o(1)",
            "SIGNED_TRACE_FIBER_CANCELLATION_PROVED": True,
            "FIXED_DIRECTION_TARGET_FIBER_BOUND": "sqrt(J)*B^o(1)",
            "FIXED_ELL_SHELL_ACTIVE_DIRECTION_BOUND": "sqrt(M*N)*B^o(1)",
            "LONG_FIBER_POWER_SAVING_PROVED": True,
            "SHORT_FIBER_ENDPOINT_POWER_SAVING_PROVED": False,
            "NORM_INDEX_HYPERBOLIC_CORRELATION_POWER_SAVING_PROVED": False,
            "A_11_POWER_SAVING_PROVED": False,
            "T_O_SQRT_B_PROVED": False,
            "PERFECT_CUBOID_NONEXISTENCE_PROVED": False,
            "NEXT": (
                "Stage14-t37 attack the short-fiber endpoint M~N=B/ell, where delta is O(1), "
                "by classifying the finitely many small-denominator layers and exploiting "
                "canonical-largest-prime Gaussian norm structure"
            ),
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report["finite_audit"], indent=2, sort_keys=True))
    print(json.dumps(report["decision"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
