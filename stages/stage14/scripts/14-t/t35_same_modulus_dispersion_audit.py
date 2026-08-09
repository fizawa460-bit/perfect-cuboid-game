#!/usr/bin/env python3
"""Stage14-t35: shared-prime dispersion / fixed-U fiber audit."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
from math import gcd, isqrt, log
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
T34_DATA = ROOT / "stages/stage14/data/14-t34/all_character_gaussian_large_sieve.json"
OUT = ROOT / "stages/stage14/data/14-t35/same_modulus_dispersion.json"

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


def unit_mult(z, j: int):
    x, y = z
    return ((x, y), (-y, x), (-x, -y), (y, -x))[j]


def canonical_unit_orbit(z):
    return min(unit_mult(z, j) for j in range(4))


def integer_norm(z) -> int:
    return z[0] * z[0] + z[1] * z[1]


def sqrt_minus_one(p: int) -> int:
    for x in range(2, p):
        if (x * x + 1) % p == 0:
            return x
    raise AssertionError(("no sqrt(-1)", p))


def residue_unit_orbit(z, p: int) -> int:
    iota = sqrt_minus_one(p)
    r = (z[0] + iota * z[1]) % p
    units = (1, p - 1, iota, p - iota)
    return min((r * u) % p for u in units)


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
            adivs = {}
            for label, (ss, tt) in (("pi", (s, t)), ("bar", (s, -t))):
                z = gaussian_div(a, b, ss, tt)
                if z is not None:
                    adivs[label] = z
            assert len(adivs) == 1
            U = next(iter(adivs.values()))

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

                    assert A % ell == 0
                    m = A // ell
                    factors = four_factors(a, b, p, q)
                    divinds = tuple(i + 1 for i, z in enumerate(factors) if z % ell == 0)

                    if divinds:
                        assert divinds in ((1, 4), (2, 3))
                        assert S % ell == 0
                        n = S // ell
                        pdivs = {}
                        for label, (ss, tt) in (("pi", (s, t)), ("bar", (s, -t))):
                            z = gaussian_div(p, q, ss, tt)
                            if z is not None:
                                pdivs[label] = z
                        assert len(pdivs) == 1
                        V = next(iter(pdivs.values()))
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
                    assert integer_norm(U) == m
                    assert integer_norm(V) == n

                    states.append(
                        {
                            "eps": eps,
                            "ell": ell,
                            "m": m,
                            "n": n,
                            "delta": delta,
                            "U": U,
                            "V": V,
                            "branch": branch,
                        }
                    )

    for idx, state in enumerate(states):
        state["id"] = idx

    assert len(states) == 1120
    assert Counter(s["branch"] for s in states) == Counter({"invisible": 838, "visible": 282})
    assert max(s["m"] for s in states) == 5
    assert max(s["n"] for s in states) == 74
    return states


def collision_audit(states):
    fibers = Counter((s["ell"], canonical_unit_orbit(s["U"])) for s in states)
    full_orbits = Counter(
        (s["ell"], canonical_unit_orbit(s["U"]), canonical_unit_orbit(s["V"]))
        for s in states
    )

    rows = {}
    pair_support = Counter()
    total_buckets = 0
    total_ordered_offdiag = 0

    for lam in AUX_PRIMES:
        assert lam % 4 == 1
        assert lam > 8 * max(s["m"] for s in states)

        good = [s for s in states if s["m"] % lam and s["n"] % lam]
        assert len(good) == 1120

        buckets = defaultdict(list)
        uclasses = defaultdict(set)
        for state in good:
            ku = residue_unit_orbit(state["U"], lam)
            kv = residue_unit_orbit(state["V"], lam)
            buckets[(state["ell"], ku, kv)].append(state["id"])
            uclasses[(state["ell"], ku)].add(canonical_unit_orbit(state["U"]))

        # lambda>8M: a residue U-unit collision must already be an exact integral U-unit orbit.
        assert all(len(v) == 1 for v in uclasses.values())

        energy = sum(len(ids) ** 2 for ids in buckets.values())
        offdiag = energy - len(good)
        rows[str(lam)] = {
            "good_states": len(good),
            "collision_energy": energy,
            "ordered_off_diagonal": offdiag,
            "residue_buckets": len(buckets),
        }
        total_buckets += len(buckets)
        total_ordered_offdiag += offdiag

        for ids in buckets.values():
            for i, j in combinations(ids, 2):
                pair_support[(min(i, j), max(i, j))] += 1

    exact_hist = Counter()
    nonorbit_hist = Counter()
    divisor_product_checks = 0
    max_nonorbit_support = 0
    Lmin = min(AUX_PRIMES)

    for (i, j), support in pair_support.items():
        s1, s2 = states[i], states[j]
        same_full_orbit = (
            s1["ell"] == s2["ell"]
            and canonical_unit_orbit(s1["U"]) == canonical_unit_orbit(s2["U"])
            and canonical_unit_orbit(s1["V"]) == canonical_unit_orbit(s2["V"])
        )
        if same_full_orbit:
            exact_hist[support] += 1
            continue

        nonorbit_hist[support] += 1
        max_nonorbit_support = max(max_nonorbit_support, support)

        # Any sampled collision prime must divide one of the four nonzero
        # Gaussian differences V-vV'.  Hence it divides their norm product.
        product = 1
        for unit_index in range(4):
            vv = unit_mult(s2["V"], unit_index)
            diff = (s1["V"][0] - vv[0], s1["V"][1] - vv[1])
            ndiff = integer_norm(diff)
            assert ndiff > 0
            product *= ndiff
        assert support * log(Lmin) <= log(product) + 1e-12
        divisor_product_checks += 1

    assert rows == {
        "53": {"good_states": 1120, "collision_energy": 2166, "ordered_off_diagonal": 1046, "residue_buckets": 727},
        "61": {"good_states": 1120, "collision_energy": 2044, "ordered_off_diagonal": 924, "residue_buckets": 778},
        "73": {"good_states": 1120, "collision_energy": 1860, "ordered_off_diagonal": 740, "residue_buckets": 822},
        "89": {"good_states": 1120, "collision_energy": 1834, "ordered_off_diagonal": 714, "residue_buckets": 824},
        "97": {"good_states": 1120, "collision_energy": 1790, "ordered_off_diagonal": 670, "residue_buckets": 851},
    }
    assert dict(exact_hist) == {5: 246}
    assert dict(nonorbit_hist) == {1: 533, 2: 142}
    assert max_nonorbit_support == 2
    assert divisor_product_checks == 675
    assert len(fibers) == 129
    assert max(fibers.values()) == 32
    assert sum(v * v for v in fibers.values()) == 15568
    assert len(full_orbits) == 915
    assert sum(v * (v - 1) // 2 for v in full_orbits.values()) == 246
    assert total_buckets == 4002
    assert total_ordered_offdiag == 4094

    return {
        "states": {
            "total": len(states),
            "visible": 282,
            "invisible": 838,
            "max_m": max(s["m"] for s in states),
            "max_n": max(s["n"] for s in states),
        },
        "unit_fibers": {
            "count": len(fibers),
            "max_size": max(fibers.values()),
            "sum_size_squared": sum(v * v for v in fibers.values()),
            "distinct_full_unit_orbits": len(full_orbits),
            "duplicate_unordered_pairs": sum(v * (v - 1) // 2 for v in full_orbits.values()),
        },
        "auxiliary_collisions": rows,
        "pair_support": {
            "exact_orbit_support_histogram": dict(sorted(exact_hist.items())),
            "non_orbit_support_histogram": dict(sorted(nonorbit_hist.items())),
            "max_non_orbit_auxiliary_prime_support": max_nonorbit_support,
            "non_orbit_divisor_product_checks": divisor_product_checks,
            "total_residue_buckets": total_buckets,
            "total_ordered_off_diagonal_collisions": total_ordered_offdiag,
        },
    }


def main():
    frozen34 = json.loads(T34_DATA.read_text())
    assert frozen34["decision"]["STAGE14_T34"] == (
        "COMPLETE_ALL_CHARACTER_GAUSSIAN_LARGE_SIEVE_AND_TENSOR_BARRIER"
    )
    assert frozen34["decision"]["SAME_MODULUS_SHARED_PRIME_COLLISION_IDENTITY"] is True
    assert frozen34["decision"]["TENSOR_LARGE_SIEVE_CLOSES_NORM_HYPERBOLA"] is False

    states = build_frozen_states()
    audit = collision_audit(states)

    report = {
        "stage": "14-t35",
        "frozen_cutoff": {
            "B": B_FROZEN,
            "AB_MAX": AB_MAX,
            "PQ_MAX": PQ_MAX,
            "auxiliary_split_primes": list(AUX_PRIMES),
        },
        "finite_audit": audit,
        "same_modulus_dispersion": {
            "u_injection_threshold": (
                "lambda>8M implies U congruent to unit*U' mod varpi only when U=unit*U' in Z[i]"
            ),
            "off_diagonal_prime_support": (
                "nu_L(s,s')<=4*log(8N)/log(L) after U-orbit injection"
            ),
            "physical_fiber": "J(U)<=N/M*B^o(1) on m~M, where N=B/ell",
            "positive_collision_sum": (
                "sum_varpi C_varpi <= P(L)*|H| + R_L*J_max*|H|, R_L=O(log N/log L)"
            ),
            "generic_packet_detector": (
                "after Mellin-packet Cauchy/duality and L~M, bound is (M^2+N)*B^o(1)"
            ),
            "recovers_tensor_sqrtM_loss": True,
            "gives_fixed_power_saving_below_ambient_N": False,
        },
        "decision": {
            "STAGE14_T35": "COMPLETE_SHARED_PRIME_DISPERSION_AND_FIBER_BARRIER",
            "SHARED_PRIME_COLLISION_DIVISOR_BOUND": True,
            "L_GT_8M_FORCES_U_UNIT_ORBIT": True,
            "PHYSICAL_U_FIBER_BOUND": "N/M*B^o(1)",
            "SAME_MODULUS_POSITIVE_DISPERSION_BOUND": True,
            "TENSOR_SQRT_M_LOSS_RECOVERED": True,
            "GENERIC_PACKET_CAUCHY_BOUND": "(M^2+N)*B^o(1)",
            "GENERIC_PACKET_CAUCHY_CLOSES_NORM_HYPERBOLA": False,
            "SIGNED_TRACE_FIBER_CANCELLATION_PROVED": False,
            "NORM_INDEX_HYPERBOLIC_CORRELATION_POWER_SAVING_PROVED": False,
            "VISIBLE_BRANCH_POWER_SAVING_PROVED": False,
            "INVISIBLE_BRANCH_POWER_SAVING_PROVED": False,
            "JOINT_COVER_CONDITIONED_SMOOTH_POWER_SAVING_PROVED": False,
            "A_11_POWER_SAVING_PROVED": False,
            "T_O_SQRT_B_PROVED": False,
            "PERFECT_CUBOID_NONEXISTENCE_PROVED": False,
            "NEXT": (
                "Stage14-t36 prove signed auxiliary-trace cancellation inside fixed-U fibers "
                "(V norm k*delta, k|epsilon*m), using the same-modulus injection to avoid "
                "reintroducing the U-dimension loss"
            ),
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report["finite_audit"], indent=2, sort_keys=True))
    print(json.dumps(report["decision"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
