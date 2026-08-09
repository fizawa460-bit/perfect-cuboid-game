#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
TH0 = ROOT / "stages/stage14/14-tH0/result.md"
T32 = ROOT / "stages/stage14/14-t32/result.md"
TH1 = ROOT / "stages/stage14/14-tH1/result.md"
FROZEN = ROOT / "stages/stage14/data/tH1/gaussian_rayclass_normalization_summary.json"

Gaussian = tuple[int, int]
UNITS: tuple[Gaussian, ...] = ((1, 0), (-1, 0), (0, 1), (0, -1))
UNIT_I_POWER = {(1, 0): 0, (0, 1): 1, (-1, 0): 2, (0, -1): 3}
SPLIT_PRIMES = (5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97)
CRT_PRIMES = SPLIT_PRIMES[:7]


def require(text: str, marker: str, source: str) -> None:
    if marker not in text:
        raise AssertionError(f"missing marker in {source}: {marker}")


def gmul(z: Gaussian, w: Gaussian) -> Gaussian:
    a, b = z
    c, d = w
    return (a * c - b * d, a * d + b * c)


def gsub(z: Gaussian, w: Gaussian) -> Gaussian:
    return (z[0] - w[0], z[1] - w[1])


def divide_by_one_plus_i(z: Gaussian) -> Gaussian | None:
    a, b = z
    if (a + b) % 2 or (b - a) % 2:
        return None
    return ((a + b) // 2, (b - a) // 2)


def valuation_one_plus_i(z: Gaussian) -> int:
    if z == (0, 0):
        return 10**9
    value = 0
    while True:
        quotient = divide_by_one_plus_i(z)
        if quotient is None:
            return value
        z = quotient
        value += 1


def is_primary(z: Gaussian) -> bool:
    return valuation_one_plus_i(gsub(z, (1, 0))) >= 3


def primary_associate(z: Gaussian) -> Gaussian:
    candidates = [gmul(unit, z) for unit in UNITS if is_primary(gmul(unit, z))]
    if len(candidates) != 1:
        raise AssertionError(f"primary associate is not unique for {z}: {candidates}")
    return candidates[0]


def factor_distinct(n: int) -> list[int]:
    factors: list[int] = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            factors.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


def primitive_root(p: int) -> int:
    factors = factor_distinct(p - 1)
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in factors):
            return g
    raise AssertionError(f"no primitive root found mod {p}")


def two_adic_exponent_from_signature(signature: int) -> int:
    signature %= 4
    if signature == 0:
        return 0
    if signature == 2:
        return 2
    return 3


def unit_subgroup_powers(e: int) -> tuple[int, ...]:
    # Powers r with i^r == 1 mod (1+i)^e.
    if e in (0, 1):
        return (0, 1, 2, 3)
    if e == 2:
        return (0, 2)
    if e == 3:
        return (0,)
    raise ValueError(e)


def independently_minimal_two_adic_exponent(signature: int) -> int:
    signature %= 4
    for e in range(4):
        if all((signature * r) % 4 == 0 for r in unit_subgroup_powers(e)):
            return e
    raise AssertionError(signature)


def build_summary() -> dict:
    th0 = TH0.read_text(encoding="utf-8")
    t32 = T32.read_text(encoding="utf-8")
    th1 = TH1.read_text(encoding="utf-8")

    for marker in [
        "STAGE14_TH0=COMPLETE_INDEPENDENT_T_SUPPORT_ROADWORKS_ARCHITECTURE",
        "TH_MINIMUM_FROZEN_T_INPUT=Stage14-t32",
        "TH_MUST_NOT_REQUIRE_A_FUTURE_T_RESULT_FOR_NEXT_STAGE=true",
    ]:
        require(th0, marker, "Stage14-tH0")

    for marker in [
        "STAGE14_T32=COMPLETE_SPLIT_TORUS_NORM_CORRELATION_AND_UNIFIED_COFACTOR_SKELETON",
        "SPLIT_AUXILIARY_PRIME_RESTRICTION_REQUIRED_FOR_TORUS_BOUND=true",
    ]:
        require(t32, marker, "Stage14-t32")

    for marker in [
        "STAGE14_TH1=COMPLETE_GAUSSIAN_PRIMARY_RAY_CLASS_AND_CONDUCTOR_NORMALIZATION",
        "ODD_GAUSSIAN_IDEAL_HAS_UNIQUE_PRIMARY_GENERATOR=true",
        "PRIMARY_NORMALIZATION_MULTIPLICATIVE=true",
        "ARBITRARY_LOCAL_CHARACTER_ORDER_SUPPORTED=true",
        "TWO_ADIC_CONDUCTOR_EXPONENT_ONE_OCCURS=false",
        "EXACT_CRT_CONDUCTOR_NORM_FORMULA=true",
        "ALL_CHARACTER_MELLIN_HECKE_LARGE_SIEVE_PROVED=false",
        "NEXT=Stage14-tH2",
    ]:
        require(th1, marker, "Stage14-tH1")

    # 1. Unique primary associate on a deterministic odd Gaussian box.
    radius = 24
    odd_elements: list[Gaussian] = []
    for a in range(-radius, radius + 1):
        for b in range(-radius, radius + 1):
            z = (a, b)
            if z == (0, 0):
                continue
            if (a * a + b * b) % 2 == 0:
                continue
            odd_elements.append(z)
            primary_associate(z)

    # 2. Primary normalization is multiplicative on a 200 x 200 sample.
    sample = odd_elements[:200]
    multiplication_checks = 0
    for z in sample:
        pz = primary_associate(z)
        for w in sample:
            pw = primary_associate(w)
            lhs = primary_associate(gmul(z, w))
            rhs = gmul(pz, pw)
            if lhs != rhs:
                raise AssertionError((z, w, lhs, rhs))
            multiplication_checks += 1

    # 3. Unit filtration at the ramified prime.
    explicit_unit_subgroups: dict[int, list[int]] = {}
    for e in range(4):
        powers: list[int] = []
        for unit in UNITS:
            if e == 0 or valuation_one_plus_i(gsub(unit, (1, 0))) >= e:
                powers.append(UNIT_I_POWER[unit])
        powers.sort()
        explicit_unit_subgroups[e] = powers

    expected_unit_subgroups = {
        0: [0, 1, 2, 3],
        1: [0, 1, 2, 3],
        2: [0, 2],
        3: [0],
    }
    if explicit_unit_subgroups != expected_unit_subgroups:
        raise AssertionError(explicit_unit_subgroups)

    # 4. All local characters for several split primes and both orientations.
    oriented_prime_ideals_checked = 0
    local_characters_checked = 0
    max_character_order = 1
    local_e2_counts = {0: 0, 2: 0, 3: 0}
    primitive_roots: dict[str, int] = {}
    square_roots_minus_one: dict[str, int] = {}

    for p in SPLIT_PRIMES:
        g = primitive_root(p)
        iota = pow(g, (p - 1) // 4, p)
        if iota * iota % p != p - 1:
            raise AssertionError((p, g, iota))
        primitive_roots[str(p)] = g
        square_roots_minus_one[str(p)] = iota

        for rho in (1, -1):
            oriented_prime_ideals_checked += 1
            oriented_iota = iota if rho == 1 else (-iota) % p
            exponent = (p - 1) // 4 if rho == 1 else 3 * (p - 1) // 4
            if pow(g, exponent, p) != oriented_iota:
                raise AssertionError((p, rho, g, oriented_iota))

            for j in range(p - 1):
                signature = (rho * j) % 4
                e2 = two_adic_exponent_from_signature(signature)
                independent_e2 = independently_minimal_two_adic_exponent(signature)
                if e2 != independent_e2:
                    raise AssertionError((p, rho, j, e2, independent_e2))

                order = 1 if j == 0 else (p - 1) // gcd(j, p - 1)
                max_character_order = max(max_character_order, order)
                local_e2_counts[e2] += 1
                local_characters_checked += 1

    # 5. CRT: all two-factor combinations over the first seven split primes.
    # Conjugate ideals above one rational prime are included as distinct factors.
    oriented_factors: list[tuple[int, int]] = []
    for p in CRT_PRIMES:
        oriented_factors.append((p, 1))
        oriented_factors.append((p, -1))

    crt_pair_cases_checked = 0
    crt_e2_counts = {0: 0, 2: 0, 3: 0}
    for left in range(len(oriented_factors)):
        p1, rho1 = oriented_factors[left]
        for right in range(left + 1, len(oriented_factors)):
            p2, rho2 = oriented_factors[right]
            for j1 in range(p1 - 1):
                for j2 in range(p2 - 1):
                    signature = (rho1 * j1 + rho2 * j2) % 4
                    formula_e2 = two_adic_exponent_from_signature(signature)
                    independent_e2 = independently_minimal_two_adic_exponent(signature)
                    if formula_e2 != independent_e2:
                        raise AssertionError(
                            (p1, rho1, j1, p2, rho2, j2, formula_e2, independent_e2)
                        )
                    crt_e2_counts[formula_e2] += 1
                    crt_pair_cases_checked += 1

    return {
        "stage": "Stage14-tH1",
        "status": "COMPLETE_GAUSSIAN_PRIMARY_RAY_CLASS_AND_CONDUCTOR_NORMALIZATION",
        "minimum_frozen_t_input": "Stage14-t32",
        "requires_future_t_result": False,
        "normalization": {
            "ramified_prime": "1+i",
            "primary_modulus": "(1+i)^3",
            "unique_primary_generator_for_odd_ideals": True,
            "primary_normalization_multiplicative": True,
            "oriented_split_prime_key": ["p", "rho"],
            "local_character_key": ["p", "rho", "j_mod_p_minus_1"],
            "unit_signature": "rho*j mod 4",
            "global_unit_signature": "sum local signatures mod 4",
            "two_adic_exponent_map": {"0": 0, "1": 3, "2": 2, "3": 3},
            "two_adic_exponent_one_occurs": False,
            "conductor_norm": "2^e2 * product(active rational prime norms)",
        },
        "audit": {
            "primary_box_radius": radius,
            "primary_odd_elements_checked": len(odd_elements),
            "primary_multiplication_checks": multiplication_checks,
            "unit_subgroup_sizes_e0_e1_e2_e3": [4, 4, 2, 1],
            "split_primes": list(SPLIT_PRIMES),
            "oriented_prime_ideals_checked": oriented_prime_ideals_checked,
            "local_characters_checked": local_characters_checked,
            "max_character_order_checked": max_character_order,
            "local_two_adic_exponent_counts": {str(k): v for k, v in local_e2_counts.items()},
            "crt_primes": list(CRT_PRIMES),
            "crt_pair_cases_checked": crt_pair_cases_checked,
            "crt_two_adic_exponent_counts": {str(k): v for k, v in crt_e2_counts.items()},
            "primitive_roots": primitive_roots,
            "chosen_positive_square_roots_minus_one": square_roots_minus_one,
        },
        "proof_boundary": {
            "all_order_gaussian_ray_class_normalization_proved": True,
            "exact_two_adic_conductor_exponent_proved": True,
            "exact_finite_crt_conductor_formula_proved": True,
            "all_character_mellin_hecke_large_sieve_proved": False,
            "norm_index_hyperbolic_correlation_power_saving_proved": False,
            "perfect_cuboid_nonexistence_proved": False,
        },
        "next": "Stage14-tH2",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="rewrite frozen summary")
    args = parser.parse_args()

    summary = build_summary()
    rendered = json.dumps(summary, ensure_ascii=False, indent=2) + "\n"

    if args.write:
        FROZEN.parent.mkdir(parents=True, exist_ok=True)
        FROZEN.write_text(rendered, encoding="utf-8")
        print(FROZEN)
        return

    frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
    if frozen != summary:
        raise AssertionError(
            "frozen tH1 summary differs semantically; run gaussian_rayclass_normalization_audit.py --write"
        )

    print("Stage14-tH1 Gaussian ray-class normalization audit: OK")


if __name__ == "__main__":
    main()
