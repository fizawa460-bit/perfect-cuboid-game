#!/usr/bin/env python3
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
TH7 = ROOT / "stages/stage14/14-tH7/result.md"
T39 = ROOT / "stages/stage14/14-t39/result.md"
TH8 = ROOT / "stages/stage14/14-tH8/result.md"
FROZEN = ROOT / "stages/stage14/data/tH8/external_auxiliary_spin_dispersion_summary.json"

SPLIT_PRIMES = (13, 17, 29, 37, 41)
C_VALUES = ((1, 0), (1, 1), (2, 1), (1, 2))
Z_VALUES = ((1, 2), (1, 3), (2, 3), (2, 5), (3, 4), (3, 5), (4, 5))


def require(text: str, marker: str, source: str) -> None:
    if marker not in text:
        raise AssertionError(f"missing marker in {source}: {marker}")


def gmul(z: tuple[int, int], w: tuple[int, int]) -> tuple[int, int]:
    a, b = z
    c, d = w
    return a * c - b * d, a * d + b * c


def psi(c: tuple[int, int], z: tuple[int, int]) -> int:
    x, y = gmul(c, z)
    return x * y


def phi(c: tuple[int, int], z: tuple[int, int]) -> int:
    return psi(c, gmul(z, z))


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    v = pow(a, (p - 1) // 2, p)
    if v == p - 1:
        return -1
    if v == 1:
        return 1
    raise AssertionError((a, p, v))


def build_packets() -> list[dict]:
    packets: list[dict] = []
    for kind in ("psi", "phi"):
        for c in C_VALUES:
            for z in Z_VALUES:
                value = psi(c, z) if kind == "psi" else phi(c, z)
                if value == 0:
                    continue
                packets.append({"kind": kind, "c": c, "z": z, "P": value})
    return packets


def dispersion_audit() -> dict:
    packets = build_packets()
    local_evaluations = len(packets) * len(SPLIT_PRIMES)
    zero_evaluations = sum(
        1
        for packet in packets
        for p in SPLIT_PRIMES
        if legendre(packet["P"], p) == 0
    )

    multiplicativity_checks = 0
    multiplicativity_failures = 0
    for p in SPLIT_PRIMES:
        for left in packets:
            for right in packets:
                multiplicativity_checks += 1
                lhs = legendre(left["P"], p) * legendre(right["P"], p)
                rhs = legendre(left["P"] * right["P"], p)
                if lhs != rhs:
                    multiplicativity_failures += 1
    if multiplicativity_failures:
        raise AssertionError(multiplicativity_failures)

    auxiliary_weights = {
        p: (-1 if i % 2 else 1) * (i + 1)
        for i, p in enumerate(SPLIT_PRIMES)
    }
    physical_weights = [((-1) ** i) * (1 + (i % 4)) for i in range(len(packets))]

    auxiliary_energy = sum(a * a for a in auxiliary_weights.values())
    physical_energy = sum(d * d for d in physical_weights)

    inner_auxiliary: dict[int, int] = {}
    direct_T = 0
    for p in SPLIT_PRIMES:
        inner = sum(
            physical_weights[i] * legendre(packet["P"], p)
            for i, packet in enumerate(packets)
        )
        inner_auxiliary[p] = inner
        direct_T += auxiliary_weights[p] * inner

    route_a_second_moment = sum(v * v for v in inner_auxiliary.values())
    route_a_cross = 0
    route_a_diagonal = 0
    route_a_off_diagonal = 0
    diagonal_good_count_total = 0

    for i, left in enumerate(packets):
        diagonal_good = sum(
            legendre(left["P"], p) ** 2 for p in SPLIT_PRIMES
        )
        diagonal_good_count_total += diagonal_good
        for j, right in enumerate(packets):
            kernel = sum(
                legendre(left["P"], p) * legendre(right["P"], p)
                for p in SPLIT_PRIMES
            )
            term = physical_weights[i] * physical_weights[j] * kernel
            route_a_cross += term
            if i == j:
                route_a_diagonal += term
            else:
                route_a_off_diagonal += term

    if route_a_cross != route_a_second_moment:
        raise AssertionError((route_a_cross, route_a_second_moment))

    direct_square = direct_T * direct_T
    route_a_cauchy_rhs = auxiliary_energy * route_a_second_moment
    if direct_square > route_a_cauchy_rhs:
        raise AssertionError((direct_square, route_a_cauchy_rhs))

    inner_physical: list[int] = []
    for packet in packets:
        inner_physical.append(
            sum(
                auxiliary_weights[p] * legendre(packet["P"], p)
                for p in SPLIT_PRIMES
            )
        )

    route_b_second_moment = sum(v * v for v in inner_physical)
    route_b_cross = 0
    route_b_diagonal = 0
    route_b_off_diagonal = 0

    for p in SPLIT_PRIMES:
        for q in SPLIT_PRIMES:
            kernel = sum(
                legendre(packet["P"], p) * legendre(packet["P"], q)
                for packet in packets
            )
            term = auxiliary_weights[p] * auxiliary_weights[q] * kernel
            route_b_cross += term
            if p == q:
                route_b_diagonal += term
            else:
                route_b_off_diagonal += term

    if route_b_cross != route_b_second_moment:
        raise AssertionError((route_b_cross, route_b_second_moment))

    route_b_cauchy_rhs = physical_energy * route_b_second_moment
    if direct_square > route_b_cauchy_rhs:
        raise AssertionError((direct_square, route_b_cauchy_rhs))

    if diagonal_good_count_total != local_evaluations - zero_evaluations:
        raise AssertionError(
            (diagonal_good_count_total, local_evaluations, zero_evaluations)
        )

    return {
        "external_split_primes": list(SPLIT_PRIMES),
        "physical_packets": len(packets),
        "local_character_evaluations": local_evaluations,
        "nonzero_character_evaluations": local_evaluations - zero_evaluations,
        "zero_bad_prime_evaluations": zero_evaluations,
        "legendre_product_checks": multiplicativity_checks,
        "legendre_product_failures": multiplicativity_failures,
        "direct_T": direct_T,
        "direct_T_square": direct_square,
        "auxiliary_coefficient_l2": auxiliary_energy,
        "physical_coefficient_l2": physical_energy,
        "route_a_second_moment": route_a_second_moment,
        "route_a_cross_expansion": route_a_cross,
        "route_a_diagonal_contribution": route_a_diagonal,
        "route_a_off_diagonal_contribution": route_a_off_diagonal,
        "route_a_cauchy_rhs": route_a_cauchy_rhs,
        "route_b_second_moment": route_b_second_moment,
        "route_b_cross_expansion": route_b_cross,
        "route_b_diagonal_contribution": route_b_diagonal,
        "route_b_off_diagonal_contribution": route_b_off_diagonal,
        "route_b_cauchy_rhs": route_b_cauchy_rhs,
        "diagonal_good_count_total": diagonal_good_count_total,
    }


def exponent_audit() -> dict:
    scales = (
        Fraction(1, 8),
        Fraction(1, 4),
        Fraction(3, 8),
        Fraction(1, 2),
        Fraction(5, 8),
        Fraction(3, 4),
    )
    checks = 0
    failures = 0
    for mu in scales:
        for nu in scales:
            checks += 1
            trivial = mu + nu
            fi = max(mu, nu) / 12 + Fraction(11, 12) * (mu + nu)
            saving = trivial - fi
            if saving != min(mu, nu) / 12:
                failures += 1
    if failures:
        raise AssertionError(failures)

    balanced_trivial = Fraction(2, 1)
    balanced_fi = Fraction(23, 12)
    balanced_saving = balanced_trivial - balanced_fi
    if balanced_saving != Fraction(1, 12):
        raise AssertionError(balanced_saving)

    return {
        "scale_values": [str(v) for v in scales],
        "exact_mu_nu_checks": checks,
        "failures": failures,
        "fi_block_saving_formula": "min(mu,nu)/12",
        "balanced_trivial_exponent": str(balanced_trivial),
        "balanced_fi_exponent": str(balanced_fi),
        "balanced_saving": str(balanced_saving),
    }


def build_summary() -> dict:
    th7 = TH7.read_text(encoding="utf-8")
    t39 = T39.read_text(encoding="utf-8")
    th8 = TH8.read_text(encoding="utf-8")

    for marker in [
        "STAGE14_TH7=COMPLETE_ROADWORKS_STRESS_GATE_AND_NEW_CYCLE_DECISION",
        "TH_CYCLE1_PARKED=true",
        "TH_SUPPORT_ROUTE_PARKED=false",
        "T38_GAUSSIAN_SPIN_TYPE_I_II_NEW_ROADWORK_IDENTIFIED=true",
    ]:
        require(th7, marker, "Stage14-tH7")

    for marker in [
        "STAGE14_T39=COMPLETE_FI_TRANSFER_AUDIT_AND_EXTERNAL_AUXILIARY_TRILINEAR_BOUNDARY",
        "DIRECT_TWO_VARIABLE_FI_TRANSFER_VALID=false",
        "EXTERNAL_AUXILIARY_THIRD_VARIABLE_ESSENTIAL=true",
        "NATURAL_MODULUS_PSI_TRACE=CONSTANT_OR_ZERO",
        "NATURAL_MODULUS_PHI_TRACE=CONSTANT_OR_ZERO",
    ]:
        require(t39, marker, "Stage14-t39")

    for marker in [
        "STAGE14_TH8=COMPLETE_EXTERNAL_AUXILIARY_GAUSSIAN_SPIN_DISPERSION_ADAPTER",
        "AUXILIARY_FAMILY_CAUCHY_DISPERSION_IDENTITY_PROVED=true",
        "PHYSICAL_PACKET_CAUCHY_DISPERSION_IDENTITY_PROVED=true",
        "FI_DIRICHLET_SYMBOL_CERTIFICATE_DEFINED=true",
        "QUADRATIC_HECKE_FAMILY_CERTIFICATE_DEFINED=true",
        "RAW_STAGE14_EXTERNAL_TRACE_FI_READY=false",
        "NEXT=Stage14-tH9",
    ]:
        require(th8, marker, "Stage14-tH8")

    dispersion = dispersion_audit()
    exponent = exponent_audit()

    return {
        "stage": "Stage14-tH8",
        "status": "COMPLETE_EXTERNAL_AUXILIARY_GAUSSIAN_SPIN_DISPERSION_ADAPTER",
        "requires_future_t_result": False,
        "dependencies": ["Stage14-tH7", "Stage14-t39"],
        "adapter": {
            "external_auxiliary_spin_packet_standardized": True,
            "auxiliary_family_cauchy_dispersion_identity_proved": True,
            "physical_packet_cauchy_dispersion_identity_proved": True,
            "dispersion_diagonals_explicit": True,
            "fi_dirichlet_symbol_certificate_defined": True,
            "quadratic_hecke_family_certificate_defined": True,
            "raw_stage14_external_trace_fi_ready": False,
            "raw_stage14_natural_self_trace_fi_useful": False,
            "auxiliary_dispersion_fi_certificate_proved": False,
            "physical_dispersion_fi_certificate_proved": False,
            "auxiliary_dispersion_quadratic_hecke_certificate_proved": False,
            "physical_dispersion_quadratic_hecke_certificate_proved": False,
        },
        "audit": {
            "dispersion": dispersion,
            "fi_exponent_ledger": exponent,
        },
        "proof_boundary": {
            "external_auxiliary_dispersion_adapter_proved": True,
            "critical_sqrt_ell_strip_power_saving_proved": False,
            "a11_power_saving_proved": False,
            "t_o_sqrt_b_proved": False,
            "perfect_cuboid_nonexistence_proved": False,
        },
        "next": "Stage14-tH9",
    }


def main() -> None:
    summary = build_summary()
    frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
    if frozen != summary:
        raise AssertionError("frozen tH8 summary differs semantically")
    print("Stage14-tH8 external-auxiliary spin dispersion audit: OK")


if __name__ == "__main__":
    main()
