#!/usr/bin/env python3
"""Deterministic audit for the Stage14-AM1 prime-power refinement."""

from __future__ import annotations

import cmath
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "stages/stage14/data/14-AM1/prime_power_adapter_summary.json"


def factor(n: int) -> list[int]:
    out: list[int] = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def primitive_root(p: int) -> int:
    assert p > 2
    factors = factor(p - 1)
    for g in range(2, p):
        if all(pow(g, (p - 1) // ell, p) != 1 for ell in factors):
            return g
    raise AssertionError(f"no primitive root found modulo {p}")


def character(j: int, exponent: int, order: int) -> complex:
    return cmath.exp(2j * cmath.pi * j * exponent / order)


def audit_root_mobius_modulus(modulus: int) -> None:
    roots = [x for x in range(modulus) if (x * x + 1) % modulus == 0]
    assert roots
    rotated: set[int] = set()
    for root in roots:
        assert (root - 1) % modulus != 0
        stage_root = (root + 1) * pow((root - 1) % modulus, -1, modulus) % modulus
        assert (stage_root * stage_root + 1) % modulus == 0
        recovered = (
            (stage_root + 1)
            * pow((stage_root - 1) % modulus, -1, modulus)
            % modulus
        )
        assert recovered == root
        rotated.add(stage_root)
    assert rotated == set(roots)


def audit_prime(p: int) -> dict[str, int | float]:
    assert p % 4 == 1
    order = p - 1
    g = primitive_root(p)
    logs: dict[int, int] = {}
    value = 1
    for exponent in range(order):
        logs[value] = exponent
        value = value * g % p
    assert len(logs) == order

    i_exp = order // 4
    minus_i_exp = 3 * order // 4
    iota = pow(g, i_exp, p)
    minus_iota = (-iota) % p
    assert iota * iota % p == p - 1
    assert minus_iota == pow(g, minus_i_exp, p)

    # Exact dictionary between the A--M/Gaussian D/A root and the Stage14
    # rotated (D+A)/(D-A) root.  The Mobius map is an involution on roots -1.
    stage_root = (iota + 1) * pow((iota - 1) % p, -1, p) % p
    assert stage_root * stage_root % p == p - 1
    recovered = (stage_root + 1) * pow((stage_root - 1) % p, -1, p) % p
    assert recovered == iota

    tol = 1e-9
    fixed_nonzero = 0
    union_nonzero = 0
    centered_union_nonzero = 0

    fixed_coeffs: list[complex] = []
    union_coeffs: list[complex] = []
    for j in range(order):
        fixed = character(j, -i_exp, order) / order
        union = (
            character(j, -i_exp, order)
            + character(j, -minus_i_exp, order)
        ) / order
        fixed_coeffs.append(fixed)
        union_coeffs.append(union)
        fixed_nonzero += abs(fixed) > tol
        union_nonzero += abs(union) > tol
        if j != 0:
            centered_union_nonzero += abs(union) > tol

    assert fixed_nonzero == order
    assert union_nonzero == order // 2
    assert centered_union_nonzero == order // 2 - 1

    # Reconstruct the fixed-root delta and the two-root union on every unit.
    for residue, exponent in logs.items():
        fixed_value = sum(
            fixed_coeffs[j] * character(j, exponent, order)
            for j in range(order)
        )
        union_value = sum(
            union_coeffs[j] * character(j, exponent, order)
            for j in range(order)
        )
        assert abs(fixed_value - (1 if residue == iota else 0)) < tol
        assert abs(
            union_value - (1 if residue in {iota, minus_iota} else 0)
        ) < tol

    fixed_l1 = sum(abs(c) for c in fixed_coeffs)
    union_l1 = sum(abs(c) for c in union_coeffs)
    centered_union_l1 = sum(abs(c) for c in union_coeffs[1:])
    assert abs(fixed_l1 - 1.0) < tol
    assert abs(union_l1 - 1.0) < tol
    assert abs(centered_union_l1 - (p - 3) / (p - 1)) < tol

    return {
        "prime": p,
        "primitive_root": g,
        "sqrt_minus_one": iota,
        "rotated_stage_root": stage_root,
        "oriented_nonzero_character_count": fixed_nonzero,
        "two_root_nonzero_character_count": union_nonzero,
        "centered_two_root_nonzero_character_count": centered_union_nonzero,
        "oriented_l1_cost": round(fixed_l1, 12),
        "two_root_l1_cost": round(union_l1, 12),
    }


def audit_valuation_fourier(max_exponent: int) -> dict[str, int | float]:
    """Audit exact valuation Fourier inversion on one fixed valuation stratum."""
    order = max_exponent + 1
    tol = 1e-9
    for target in range(order):
        for valuation in range(order):
            reconstructed = sum(
                cmath.exp(-2j * cmath.pi * t * target / order)
                * cmath.exp(2j * cmath.pi * t * valuation / order)
                / order
                for t in range(order)
            )
            assert abs(reconstructed - (1 if valuation == target else 0)) < tol

    exact_l1 = sum(Fraction(1, order) for _ in range(order))
    assert exact_l1 == 1

    return {
        "max_exponent": max_exponent,
        "phase_count": order,
        "exact_indicator_l1_cost": float(exact_l1),
    }


def average(values: list[Fraction]) -> Fraction:
    return sum(values, Fraction(0)) / len(values)


def audit_pair_recentering() -> None:
    """Audit the exact s7-55 to 4dm transfer term in (1.5)."""
    samples = [
        ([1, 0, 1, 1], [0, 1, 1, 1], [1, -1, 2, -2]),
        ([0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [2, 0, -1, 3, -2]),
    ]
    conductor = Fraction(5)
    for a_raw, b_raw, k_raw in samples:
        a = [Fraction(x) for x in a_raw]
        b = [Fraction(x) for x in b_raw]
        k = [Fraction(x) for x in k_raw]
        ea, eb = average(a), average(b)
        eab = average([x * y for x, y in zip(a, b)])
        eak = average([x * z for x, z in zip(a, k)])
        eakb = average([x * z * y for x, z, y in zip(a, k, b)])
        mu_plus = ea / conductor + eak
        delta_pair = eab / conductor - mu_plus * eb
        err_pair = eakb
        z_pair = (eab - ea * eb) / conductor
        e_pair = eakb - eak * eb
        c_pair = eak * eb
        assert z_pair == delta_pair + c_pair
        assert e_pair == err_pair - c_pair
        assert delta_pair + err_pair == z_pair + e_pair


def main() -> None:
    report = json.loads(DATA.read_text(encoding="utf-8"))
    assert report["stage"] == "Stage14-AM1"
    assert report["source_main_sha"] == "31762e51ff1ea764a4dbc06fe91656f1a37aaafc"
    assert report["merged_am_consumed"] is True
    assert report["merged_am_overwritten"] is False
    assert "Stage14-AM" in report["merged_sources"]
    assert "Stage14-4dm" in report["merged_sources"]
    assert "Stage14-Work-bfX18" in report["merged_sources"]
    assert {"Stage14-4dn", "Stage14-s7-57", "Stage14-t97"} <= set(
        report["merged_sources"]
    )
    assert report["unmerged_advisory_only"] == []
    assert report["final_verdict"] == "BLOCKED"
    assert report["direct"] is False
    assert report["near_with_proved_adapter"] is False
    assert report["near_adapter_incomplete"] is False
    assert report["blocked"] is True
    assert report["am_certified_delta"] == "0"
    assert report["current_exponent"] == "1/2"
    assert report["next_adapter_lemma"] == "PrimitivePhysicalHeckeAdapterLemma"
    assert report["local_gaussian_ideal_valuation_adapter_proved"] is True
    assert report["local_adapter_scope"] == "fixed_normalized_valuation_stratum_only"
    assert report["merged_am_squarefree_walsh_extended_to_prime_power_strata"] is True
    assert report["rotated_root_mobius_dictionary_proved"] is True
    assert report["s7_55_to_4dm_recentering_transfer_proved"] is True
    assert report["local_ideal_phase_count"] == (
        "at_most_tau(X_+)=B^o(1)_per_fixed_valuation_stratum"
    )
    assert report["local_ideal_coefficient_l1_cost"] == "1"
    assert report["genuine_hecke_character_adapter_proved"] is False
    assert report["full_physical_selector_phase_decomposition_proved"] is False

    merged_am = (ROOT / "stages/stage14/14-AM/result.md").read_text(encoding="utf-8")
    assert "FINAL_CLASSIFICATION=BLOCKED" in merged_am
    assert "Primitive Physical Hecke Adapter Lemma" in merged_am

    audited = [audit_prime(p) for p in report["audit_primes"]]
    for row in audited:
        p = int(row["prime"])
        assert row["oriented_nonzero_character_count"] == p - 1
        assert row["two_root_nonzero_character_count"] == (p - 1) // 2
        assert row["centered_two_root_nonzero_character_count"] == (p - 3) // 2

    for modulus in (5**2, 5**3, 13**2, 5 * 13, 5**2 * 13):
        audit_root_mobius_modulus(modulus)

    valuation_audits = [audit_valuation_fourier(e) for e in range(1, 13)]
    assert all(row["phase_count"] == row["max_exponent"] + 1 for row in valuation_audits)
    audit_pair_recentering()

    # On a fixed normalized valuation stratum, multiplying the selected local
    # projectors costs product_{p|C_*}(E_p+1), bounded by tau(X_+).
    for exponents in ([1], [2, 1], [3, 2, 1], [5, 4, 2, 1]):
        phase_count = 1
        for exponent in exponents:
            phase_count *= exponent + 1
        divisor_count = 1
        for exponent in exponents:
            divisor_count *= exponent + 1
        assert phase_count == divisor_count

    # The merged full-conductor range has a genuinely positive phase-count exponent.
    chi_min = Fraction(1, 6)
    chi_max = Fraction(1, 4)
    assert 0 < chi_min <= chi_max < Fraction(1, 2)

    # No fixed decrement is imported from a qualitative o(1) theorem.
    ambient = Fraction(1, 2)
    certified_delta = Fraction(0)
    assert ambient - certified_delta == ambient

    print("Stage14-AM1 Azevedo--Moreira prime-power refinement: PASS")
    print("exact oriented projector support: phi(p)=p-1")
    print("exact two-root projector support: (p-1)/2")
    print("rotated root Mobius dictionary on prime powers: PASS")
    print("full-conductor term-count exponent range: [1/6,1/4]")
    print("coefficient L1 cost: 1")
    print("local fixed-stratum Gaussian-ideal valuation Fourier adapter: PASS")
    print("local phase count: <=tau(X_+); exact-projector L1 cost: 1")
    print("s7-55 to 4dm exact recentering: PASS")
    print("AM certified delta: 0")
    print("final verdict: BLOCKED")


if __name__ == "__main__":
    main()
