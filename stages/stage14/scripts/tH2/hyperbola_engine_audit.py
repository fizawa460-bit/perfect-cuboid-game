#!/usr/bin/env python3
from __future__ import annotations

import json
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
TH1 = ROOT / "stages/stage14/14-tH1/result.md"
T32 = ROOT / "stages/stage14/14-t32/result.md"
TH2 = ROOT / "stages/stage14/14-tH2/result.md"
FROZEN = ROOT / "stages/stage14/data/tH2/hyperbola_engine_summary.json"

EPSILON_STATES = (1, 2, 3, 4, 6, 8, 12)
Y = 256


def require(text: str, marker: str, source: str) -> None:
    if marker not in text:
        raise AssertionError(f"missing marker in {source}: {marker}")


def divisors(n: int) -> list[int]:
    out: list[int] = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


def tau(n: int) -> int:
    return len(divisors(n))


def r2(n: int) -> int:
    # Exact ordered signed two-square representation count via divisor classes.
    d1 = 0
    d3 = 0
    for d in divisors(n):
        residue = d % 4
        if residue == 1:
            d1 += 1
        elif residue == 3:
            d3 += 1
    return 4 * (d1 - d3)


def dyadic_lower(n: int) -> int:
    return 1 << (n.bit_length() - 1)


def enumerate_original() -> list[tuple[int, int, int, int]]:
    tuples: list[tuple[int, int, int, int]] = []
    for epsilon in EPSILON_STATES:
        for m in range(1, Y + 1):
            for delta in range(1, Y // m + 1):
                for k in divisors(epsilon * m):
                    tuples.append((epsilon, m, k, delta))
    return tuples


def transform(
    item: tuple[int, int, int, int]
) -> tuple[int, int, int, int, int]:
    epsilon, m, k, delta = item
    g = gcd(k, epsilon)
    h = k // g
    if m % h:
        raise AssertionError(("h does not divide m", item, g, h))
    r = m // h
    if gcd(h, epsilon // g) != 1:
        raise AssertionError(("coprimality failed", item, g, h, r))
    if h * r * delta > Y:
        raise AssertionError(("budget failed", item, g, h, r, delta))
    return (epsilon, g, h, r, delta)


def enumerate_transformed() -> list[tuple[int, int, int, int, int]]:
    tuples: list[tuple[int, int, int, int, int]] = []
    for epsilon in EPSILON_STATES:
        for g in divisors(epsilon):
            epsilon_prime = epsilon // g
            for h in range(1, Y + 1):
                if gcd(h, epsilon_prime) != 1:
                    continue
                for r in range(1, Y // h + 1):
                    for delta in range(1, Y // (h * r) + 1):
                        tuples.append((epsilon, g, h, r, delta))
    return tuples


def build_summary() -> dict:
    th1 = TH1.read_text(encoding="utf-8")
    t32 = T32.read_text(encoding="utf-8")
    th2 = TH2.read_text(encoding="utf-8")

    for marker in [
        "STAGE14_TH1=COMPLETE_GAUSSIAN_PRIMARY_RAY_CLASS_AND_CONDUCTOR_NORMALIZATION",
        "TH_REQUIRES_FUTURE_T_RESULT=false",
    ]:
        require(th1, marker, "Stage14-tH1")

    for marker in [
        "STAGE14_T32=COMPLETE_SPLIT_TORUS_NORM_CORRELATION_AND_UNIFIED_COFACTOR_SKELETON",
        "VISIBLE_INVISIBLE_SUPER_SQRT_NORM_SKELETON_UNIFIED=true",
    ]:
        require(t32, marker, "Stage14-t32")

    for marker in [
        "STAGE14_TH2=COMPLETE_DIVISOR_COUPLED_GAUSSIAN_NORM_HYPERBOLA_ENGINE",
        "DIVISOR_REPARAMETERIZATION_BIJECTION_PROVED=true",
        "EXACT_SUMMATION_IDENTITY_PROVED=true",
        "EXACT_BALANCED_HYPERBOLA_IDENTITY_PROVED=true",
        "EVERY_HYPERBOLA_POINT_HAS_ONE_SHORT_NORM=true",
        "SHARP_HYPERBOLA_RECTANGULARIZED_WITHOUT_ERROR=false",
        "NEXT=Stage14-tH3",
    ]:
        require(th2, marker, "Stage14-tH2")

    original = enumerate_original()
    transformed = [transform(item) for item in original]
    transformed_enum = enumerate_transformed()

    transformed_set = set(transformed)
    transformed_enum_set = set(transformed_enum)
    if len(transformed_set) != len(transformed):
        raise AssertionError("forward transform is not injective")
    if transformed_set != transformed_enum_set:
        raise AssertionError("forward/inverse transformed sets differ")

    # Reconstruct each original tuple exactly.
    reconstructed: set[tuple[int, int, int, int]] = set()
    for epsilon, g, h, r, delta in transformed_enum:
        m = h * r
        k = g * h
        if gcd(k, epsilon) != g:
            raise AssertionError((epsilon, g, h, r, delta, "wrong gcd"))
        if (epsilon * m) % k:
            raise AssertionError((epsilon, g, h, r, delta, "k does not divide epsilon*m"))
        reconstructed.add((epsilon, m, k, delta))
    if reconstructed != set(original):
        raise AssertionError("inverse reconstruction differs from original tuples")

    r_arm = 0
    delta_arm = 0
    overlap = 0
    cover_failures = 0
    active_blocks: set[tuple[int, int, int, int, int]] = set()
    max_full_box_factor = 0
    max_u_norm = 0
    max_v_norm = 0

    for epsilon, g, h, r, delta in transformed:
        # Integer versions of r <= sqrt(gY/h) and delta <= sqrt(Y/(gh)).
        in_r_arm = r * r * h <= g * Y
        in_delta_arm = delta * delta * g * h <= Y
        if not (in_r_arm or in_delta_arm):
            cover_failures += 1
        if in_r_arm:
            r_arm += 1
        if in_delta_arm:
            delta_arm += 1
        if in_r_arm and in_delta_arm:
            overlap += 1

        u_norm = h * r
        v_norm = g * h * delta
        max_u_norm = max(max_u_norm, u_norm)
        max_v_norm = max(max_v_norm, v_norm)

        # Direct one-short-norm check, squared to avoid floating-point error.
        short_norm = min(u_norm, v_norm)
        if short_norm * short_norm > g * h * Y:
            raise AssertionError((epsilon, g, h, r, delta, u_norm, v_norm))

        H = dyadic_lower(h)
        R = dyadic_lower(r)
        D = dyadic_lower(delta)
        if H * R * D > Y:
            raise AssertionError(("dyadic lower box exceeds Y", H, R, D))
        active_blocks.add((epsilon, g, H, R, D))
        # (2H)(2R)(2D) / Y <= 8 because HRD <= h*r*delta <=Y.
        numerator = 8 * H * R * D
        # Store the ceiling-free exact maximum factor; here Y is a divisor in max case.
        if numerator > max_full_box_factor * Y:
            max_full_box_factor = (numerator + Y - 1) // Y

    if cover_failures:
        raise AssertionError(f"hyperbola cover failures: {cover_failures}")
    if r_arm + delta_arm - overlap != len(transformed):
        raise AssertionError("hyperbola inclusion-exclusion identity failed")

    # Gaussian representation multiplicity audit on the whole frozen tuple set.
    r2_cache = {n: r2(n) for n in range(1, max_v_norm + 1)}
    tau_cache = {n: tau(n) for n in range(1, max_v_norm + 1)}
    representation_pair_mass = 0
    r2_product_bound_violations = 0
    for epsilon, m, k, delta in original:
        n = k * delta
        pair_mass = r2_cache[m] * r2_cache[n]
        representation_pair_mass += pair_mass
        if pair_mass > 16 * tau_cache[m] * tau_cache[n]:
            r2_product_bound_violations += 1

    return {
        "stage": "Stage14-tH2",
        "status": "COMPLETE_DIVISOR_COUPLED_GAUSSIAN_NORM_HYPERBOLA_ENGINE",
        "minimum_frozen_t_input": "Stage14-t32",
        "requires_future_t_result": False,
        "exact_reparameterization": {
            "g": "gcd(k,epsilon)",
            "h": "k/g",
            "r": "m/h",
            "inverse_m": "h*r",
            "inverse_k": "g*h",
            "g_divides_epsilon": True,
            "coprimality": "gcd(h,epsilon/g)=1",
            "transformed_budget": "h*r*delta<=Y",
            "u_norm": "h*r",
            "v_norm": "g*h*delta",
            "shared_norm_factor": "h",
        },
        "hyperbola": {
            "fixed_gh_T": "Y/h",
            "r_threshold": "sqrt(g*Y/h)",
            "delta_threshold": "sqrt(Y/(g*h))",
            "balance_norm_scale": "sqrt(g*h*Y)",
            "exact_two_arm_identity": True,
            "every_point_has_one_short_norm": True,
            "sharp_cutoff_retained": True,
            "rectangularized_without_error": False,
        },
        "dyadic": {
            "block_variables": ["epsilon", "g", "H", "R", "D"],
            "active_block_condition": "H*R*D<=Y",
            "full_box_product_upper_factor": 8,
            "u_norm_scale": "H*R",
            "v_norm_scale": "g*H*D",
            "balance_ratio": "R/(g*D)",
            "block_count_power_loss": False,
        },
        "multiplicity": {
            "r2_bound": "r2(n)<=4*tau(n)",
            "unsieved_mass": "Y^(1+eta)",
            "fixed_power_loss": False,
            "coefficient_collision_energy_closed": False,
        },
        "audit": {
            "epsilon_states": list(EPSILON_STATES),
            "Y": Y,
            "original_tuple_count": len(original),
            "transformed_tuple_count": len(transformed),
            "unique_transformed_tuple_count": len(transformed_set),
            "bijection_failures": 0,
            "r_arm_memberships": r_arm,
            "delta_arm_memberships": delta_arm,
            "overlap_memberships": overlap,
            "inclusion_exclusion_total": r_arm + delta_arm - overlap,
            "hyperbola_cover_failures": cover_failures,
            "active_dyadic_blocks": len(active_blocks),
            "max_full_box_product_over_Y": max_full_box_factor,
            "max_u_norm": max_u_norm,
            "max_v_norm": max_v_norm,
            "exact_gaussian_representation_pair_mass": representation_pair_mass,
            "r2_product_bound_violations": r2_product_bound_violations,
        },
        "proof_boundary": {
            "divisor_reparameterization_bijection_proved": True,
            "exact_summation_identity_proved": True,
            "exact_balanced_hyperbola_identity_proved": True,
            "all_character_mellin_hecke_large_sieve_proved": False,
            "norm_index_hyperbolic_correlation_power_saving_proved": False,
            "a11_power_saving_proved": False,
            "t_o_sqrt_b_proved": False,
            "perfect_cuboid_nonexistence_proved": False,
        },
        "next": "Stage14-tH3",
    }


def main() -> None:
    summary = build_summary()
    frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
    if frozen != summary:
        raise AssertionError("frozen tH2 summary differs semantically")
    print("Stage14-tH2 hyperbola engine audit: OK")


if __name__ == "__main__":
    main()
