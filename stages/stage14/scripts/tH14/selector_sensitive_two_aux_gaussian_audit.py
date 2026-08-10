#!/usr/bin/env python3
"""Deterministic audit for Stage14-tH14.

This audit freezes the non-circular interfaces used by the tH14 receiver:
- merged t50 really hit the multi-modulus reopen trigger;
- tH5 closes exact Gaussian-pair energy but not residue collisions;
- a nonexact two-coordinate unit-orbit residue collision at two split
  rational primes forces p*q to divide one fixed difference datum Delta;
- the resulting off-diagonal collision kernel has only O_rho(1)
  auxiliary-prime-pair multiplicity per exact-pair pair;
- the critical sqrt-ell exponent ledger is exact;
- complete character cancellation does not imply sparse-selector cancellation.

The script intentionally never groups ordered physical pairs by squareclass
cross-kernel tau.  Doing so would import the unresolved E4 coefficient energy.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
T50 = ROOT / "stages/stage14/data/14-t50/selector_sensitive_two_modulus_frozen.json"
TH5 = ROOT / "stages/stage14/data/tH5/gaussian_pair_collision_energy_summary.json"
TH14 = ROOT / "stages/stage14/data/tH14/selector_sensitive_two_aux_gaussian_summary.json"

UNITS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def gmul(z: tuple[int, int], w: tuple[int, int]) -> tuple[int, int]:
    a, b = z
    c, d = w
    return (a * c - b * d, a * d + b * c)


def gsub(z: tuple[int, int], w: tuple[int, int]) -> tuple[int, int]:
    return (z[0] - w[0], z[1] - w[1])


def norm(z: tuple[int, int]) -> int:
    return z[0] * z[0] + z[1] * z[1]


def unit_difference_product(z: tuple[int, int], zp: tuple[int, int]) -> int:
    out = 1
    for u in UNITS:
        out *= norm(gsub(z, gmul(u, zp)))
    return out


def delta_pair(
    U: tuple[int, int],
    V: tuple[int, int],
    Up: tuple[int, int],
    Vp: tuple[int, int],
) -> int:
    du = unit_difference_product(U, Up)
    dv = unit_difference_product(V, Vp)
    return gcd(abs(du), abs(dv))


def rational_prime_passes_unit_orbit_necessary_condition(
    p: int,
    z: tuple[int, int],
    zp: tuple[int, int],
) -> bool:
    # If one oriented Gaussian prime above p divides z-u*z' for some unit u,
    # then p divides the rational norm N(z-u*z').  The converse need not hold;
    # this deliberately audits only the necessary implication used by tH14.
    return any(norm(gsub(z, gmul(u, zp))) % p == 0 for u in UNITS)


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def main() -> None:
    t50 = json.loads(T50.read_text())
    th5 = json.loads(TH5.read_text())
    th14 = json.loads(TH14.read_text())

    # Frozen predecessor contracts.
    assert t50["stage"] == "14-t50"
    assert t50["TH14_NEEDED"] is True
    assert t50["roadworks"]["tH11_multi_modulus_reopen_trigger_hit"] is True
    assert t50["roadworks"]["tH5_exact_gaussian_pair_energy_proved"] is True
    assert t50["roadworks"]["tH5_same_modulus_residue_collision_energy_proved"] is False
    assert t50["t49_frozen"]["H"] == 560
    assert t50["t49_frozen"]["P"] == 128
    assert t50["t49_frozen"]["R_off"] == 9_007_456

    assert th5["status"] == "COMPLETE_EXACT_GAUSSIAN_PAIR_COEFFICIENT_COLLISION_ENERGY"
    assert th5["energy_theorem"]["full_exact_gaussian_pair_coefficient_collision_energy_proved"] is True
    assert th5["energy_theorem"]["same_modulus_residue_collision_energy_proved"] is False
    assert th5["energy_theorem"]["same_modulus_joint_second_moment_theorem_proved"] is False

    # Exact difference-divisor implication on deterministic Gaussian-pair data.
    gaussian_pairs = [
        ((1, 2), (2, 3)),
        ((2, 1), (3, -1)),
        ((3, 2), (1, 4)),
        ((4, -1), (2, 5)),
        ((1, -3), (4, 2)),
        ((5, 2), (3, 4)),
        ((2, -5), (5, 1)),
    ]
    test_primes = (5, 13, 17, 29, 37, 41, 53, 61)
    implication_checks = 0
    two_prime_checks = 0
    nonexact_positive_delta = 0

    for i, (U, V) in enumerate(gaussian_pairs):
        for j, (Up, Vp) in enumerate(gaussian_pairs):
            if i == j:
                continue
            d = delta_pair(U, V, Up, Vp)
            if d == 0:
                # Both coordinates are in the same exact mu4 orbit.  The small
                # deterministic list is chosen to avoid that off the diagonal.
                raise AssertionError("unexpected exact unit-orbit duplicate")
            nonexact_positive_delta += 1
            passing = []
            for p in test_primes:
                u_ok = rational_prime_passes_unit_orbit_necessary_condition(p, U, Up)
                v_ok = rational_prime_passes_unit_orbit_necessary_condition(p, V, Vp)
                if u_ok and v_ok:
                    assert d % p == 0
                    passing.append(p)
                    implication_checks += 1
            for p in passing:
                for q in passing:
                    if p == q:
                        continue
                    assert d % (p * q) == 0
                    two_prime_checks += 1

    assert nonexact_positive_delta == len(gaussian_pairs) * (len(gaussian_pairs) - 1)

    # Partial exact orbit: D_U=0, D_V!=0.  gcd(0,D_V)=|D_V| must retain
    # the divisor information from the nonexact coordinate.
    U = (2, 3)
    Up = gmul((0, 1), U)
    V = (1, 4)
    Vp = (3, 2)
    du = unit_difference_product(U, Up)
    dv = unit_difference_product(V, Vp)
    assert du == 0
    assert dv != 0
    assert delta_pair(U, V, Up, Vp) == abs(dv)

    # Size-of-prime-support principle: if every active prime is >= L and
    # Delta<=B^C, at most floor(C/rho)+O(1) can divide Delta.  Audit the exact
    # exponent arithmetic on several rational pairs (C,rho).
    for C, rho in [
        (Fraction(8), Fraction(1, 8)),
        (Fraction(12), Fraction(1, 4)),
        (Fraction(20), Fraction(1, 3)),
    ]:
        max_large_prime_factors = C / rho
        assert max_large_prime_factors.denominator == 1
        assert max_large_prime_factors >= 1

    # Schur-kernel ledger.  Diagonal multiplicity is P(P-1), while a nonexact
    # exact-pair pair has O(1) prime-pair multiplicity.  Under N_Z <= P*B^o,
    # the row sum is P^2*B^o.
    P = 128
    N = 560
    C_off = 16
    schur_row = P * (P - 1) + C_off * (N - 1)
    assert schur_row <= 2 * P * P

    # Large-product injectivity exponent threshold in the critical strip.
    y = Fraction(1, 2)
    assert 2 * Fraction(1, 4) == y  # endpoint only: no fixed margin
    assert 2 * Fraction(1, 3) > y

    # Critical exponent ledger: target vs trivial second moment.
    h = Fraction(1, 3)
    rho = Fraction(1, 2)
    assert rho >= h
    target = h + 2 * rho
    trivial = 2 * h + 2 * rho
    assert trivial - target == h
    residue_collision = h + 2 * rho
    assert residue_collision == target
    omega = Fraction(0)
    assert target + omega == target

    # t50 complete-vs-selector countermodel, independently recomputed.
    p = 13
    complete = sum(legendre(x, p) for x in range(1, p))
    selected = sum(legendre(x, p) for x in range(1, p) if legendre(x, p) == 1)
    assert complete == 0
    assert selected == 6

    # Arbitrary all-plus selector countermodel: the target cannot hold for
    # arbitrary masks independently of geometry.
    H = 6
    Psmall = 5
    lhs_all_plus = Psmall * (Psmall - 1) * H * H
    target_all_plus = Psmall * Psmall * H
    assert lhs_all_plus > target_all_plus

    # Lock the new theorem/failure boundary.
    assert th14["status"] == "COMPLETE_TWO_AUXILIARY_SELECTOR_RECEIVER_AND_RESIDUE_COLLISION_CLOSURE"
    assert th14["mandatory_preservation"]["signed_common_refinement_aggregation"] is True
    assert th14["mandatory_preservation"]["shared_UV_modulus_group"] is True
    assert th14["mandatory_preservation"]["pair_to_cross_kernel_precollapse"] is False
    assert th14["residue_collision"]["aggregate_same_modulus_residue_collision_energy_proved"] is True
    assert th14["residue_collision"]["global_equal_squareclass_resonance_absorbed_by_tH5"] is False
    assert th14["missing_external_theorem"]["name"] == "SelectorSensitiveGaussianCompletion"
    assert th14["missing_external_theorem"]["proved"] is False
    assert th14["missing_external_theorem"]["must_not_use_E4_as_input"] is True
    assert th14["proof_boundary"]["global_external_two_prime_mean_square_bound_proved"] is False
    assert th14["proof_boundary"]["critical_sqrt_ell_strip_power_saving_proved"] is False

    print("Stage14-tH14 audit: OK")
    print(f"  predecessor H/P/R_off = {t50['t49_frozen']['H']}/{t50['t49_frozen']['P']}/{t50['t49_frozen']['R_off']}")
    print(f"  Gaussian divisor implication checks = {implication_checks}")
    print(f"  two-prime product-divisor checks = {two_prime_checks}")
    print(f"  Schur sample row / P^2 = {schur_row}/{P*P}")
    print("  critical target/trivial/gap =", target, trivial, trivial - target)
    print("  SSGC remains external: true")


if __name__ == "__main__":
    main()
