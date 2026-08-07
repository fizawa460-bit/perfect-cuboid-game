#!/usr/bin/env python3
"""Stage12-N1-2k: final primitive remainder and constant audit.

This audit closes the analytic architecture for the primitive oriented count
defined in Stage12-N1-2b.  It replaces the parameter-uniform fixed-(r,s)
Selberg--Delange problem by a fixed primitive-circle coefficient, proves the
finite local-correction convolution, matches the two-modulus Euler product
eta to pi*kappa prime by prime, and records the standard multivariable
mean-value input needed for the final leading asymptotic.

The numerical Euler products are diagnostics, not certified enclosures.
"""
from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

DEFAULT_REPORT = Path("data/final_remainder_stage12_n1_2k_report.json")
CHECK_LIMIT = 5000
PRIME_LIMIT = 200_000


def build_spf(limit: int) -> list[int]:
    spf = list(range(limit + 1))
    if limit >= 1:
        spf[1] = 1
    for p in range(2, math.isqrt(limit) + 1):
        if spf[p] != p:
            continue
        for n in range(p * p, limit + 1, p):
            if spf[n] == n:
                spf[n] = p
    return spf


def factor_dict(n: int, spf: list[int]) -> dict[int, int]:
    out: dict[int, int] = {}
    while n > 1:
        p = spf[n]
        exponent = 0
        while n % p == 0:
            n //= p
            exponent += 1
        out[p] = exponent
    return out


def divisors_from_factor(factors: dict[int, int]) -> list[int]:
    divisors = [1]
    for p, exponent in factors.items():
        divisors = [d * p**j for d in divisors for j in range(exponent + 1)]
    return divisors


def mobius_from_factor(factors: dict[int, int]) -> int:
    if any(exponent > 1 for exponent in factors.values()):
        return 0
    return -1 if len(factors) % 2 else 1


def chi4(n: int) -> int:
    if n % 2 == 0:
        return 0
    return 1 if n % 4 == 1 else -1


def g_from_factor(factors: dict[int, int]) -> int:
    value = 1
    for p, exponent in factors.items():
        if p % 4 == 1:
            value *= 2 * exponent + 1
    return value


def g_value(n: int, spf: list[int]) -> int:
    return g_from_factor(factor_dict(n, spf))


def base_coefficient(n: int, spf: list[int]) -> int:
    """Coefficient of zeta(s)L(s,chi4)/((1+2^-s)zeta(2s))."""
    if n == 1:
        return 1
    factors = factor_dict(n, spf)
    if any(p % 4 != 1 for p in factors):
        return 0
    return 2 ** len(factors)


def sum_two_squares_coefficient(n: int, spf: list[int]) -> int:
    return sum(chi4(d) for d in divisors_from_factor(factor_dict(n, spf)))


def base_coefficient_by_convolution(n: int, spf: list[int]) -> int:
    """Coefficient from (zeta L) * zeta(2s)^-1 * (1+2^-s)^-1."""
    total = 0
    power_two = 1
    parity_exponent = 0
    while power_two <= n and n % power_two == 0:
        quotient = n // power_two
        for square_root in range(1, math.isqrt(quotient) + 1):
            square = square_root * square_root
            if quotient % square:
                continue
            mu = mobius_from_factor(factor_dict(square_root, spf))
            if mu:
                total += (
                    (-1) ** parity_exponent
                    * mu
                    * sum_two_squares_coefficient(quotient // square, spf)
                )
        parity_exponent += 1
        power_two *= 2
    return total


def primitive_height_weight(m: int, rs: int, spf: list[int]) -> int:
    rs_factors = factor_dict(rs, spf)
    base = g_from_factor(rs_factors)
    if m == 1:
        return base - 1
    value = base
    for p in factor_dict(m, spf):
        if p % 4 != 1:
            return 0
        value = value // (2 * rs_factors.get(p, 0) + 1) * 2
    return value


def correction_coefficient(n: int, rs: int, spf: list[int]) -> Fraction:
    """Coefficient of H_rs(s)=prod_{p^t||rs} (1-alpha p^-s)/(1+p^-s)."""
    if n == 1:
        return Fraction(1, 1)
    rs_factors = factor_dict(rs, spf)
    value = Fraction(1, 1)
    for p, exponent in factor_dict(n, spf).items():
        t = rs_factors.get(p, 0)
        if t == 0 or p % 4 != 1:
            return Fraction(0, 1)
        rho = Fraction(4 * t, 2 * t + 1)
        value *= rho if exponent % 2 == 0 else -rho
    return value


def corrected_convolution_weight(m: int, rs: int, spf: list[int]) -> Fraction:
    total = Fraction(0, 1)
    for d in divisors_from_factor(factor_dict(m, spf)):
        total += correction_coefficient(d, rs, spf) * base_coefficient(m // d, spf)
    return g_value(rs, spf) * total


def correction_l1_half(rs: int, spf: list[int]) -> float:
    product = 1.0
    for p, t in factor_dict(rs, spf).items():
        if p % 4 != 1:
            continue
        rho = 4.0 * t / (2.0 * t + 1.0)
        product *= 1.0 + rho / (math.sqrt(p) - 1.0)
    return product


def prime_sieve(limit: int) -> list[int]:
    is_prime = bytearray(b"\x01") * (limit + 1)
    is_prime[:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if is_prime[p]:
            is_prime[p * p : limit + 1 : p] = b"\x00" * (
                ((limit - p * p) // p) + 1
            )
    return [p for p in range(2, limit + 1) if is_prime[p]]


def euler_products(prime_limit: int) -> dict[str, float | int]:
    primes = prime_sieve(prime_limit)

    log_kappa_h = 3.0 * math.log(0.5)
    log_eta_h = 2.0 * math.log(0.5)
    ratio_local_checks = 0

    for p in primes:
        if p == 2:
            continue
        if p % 4 == 1:
            raw_local = 1.0 + 2.0 / (p - 1.0) + 4.0 * p / (p * p - 1.0)
            kappa_normalized = raw_local * (1.0 - 1.0 / p) ** 6
            eta_local = 1.0 + 4.0 * p / (p + 1.0) ** 2
            eta_normalized = eta_local * (1.0 - 1.0 / p) ** 4

            q = p
            exact_raw = Fraction(q * q + 6 * q + 1, q * q - 1)
            exact_kappa = exact_raw * Fraction((q - 1) ** 6, q**6)
            exact_eta = (
                Fraction(q * q + 6 * q + 1, (q + 1) ** 2)
                * Fraction((q - 1) ** 4, q**4)
            )
            if exact_eta / exact_kappa != Fraction(q * q, q * q - 1):
                raise ArithmeticError("eta/kappa local factor identity failed")
            ratio_local_checks += 1
        else:
            kappa_normalized = (1.0 - 1.0 / (p * p)) ** 3
            eta_normalized = (1.0 - 1.0 / (p * p)) ** 2

        log_kappa_h += math.log(kappa_normalized)
        log_eta_h += math.log(eta_normalized)

    kappa = (math.pi / 4.0) ** 3 * math.exp(log_kappa_h)
    eta = (math.pi / 4.0) ** 2 * math.exp(log_eta_h)

    return {
        "prime_cutoff": prime_limit,
        "stage12_kappa_partial": kappa,
        "primitive_two_modulus_eta_partial": eta,
        "eta_over_pi_kappa": eta / (math.pi * kappa),
        "candidate_leading_constant_kappa_over_12pi": kappa / (12.0 * math.pi),
        "candidate_leading_constant_eta_over_12pi2": eta / (12.0 * math.pi**2),
        "exact_q_1mod4_local_ratio_checks": ratio_local_checks,
    }


def run_finite_checks(spf: list[int]) -> dict[str, int | float]:
    base_checks = 0
    primitive_representation_checks = 0
    correction_checks = 0
    beta_domination_checks = 0

    for n in range(1, CHECK_LIMIT + 1):
        direct = base_coefficient(n, spf)
        convolution = base_coefficient_by_convolution(n, spf)
        if direct != convolution:
            raise ArithmeticError(f"base coefficient convolution failed at n={n}")
        base_checks += 1

    max_coordinate = math.isqrt(CHECK_LIMIT)
    primitive_norm_counts = [0] * (CHECK_LIMIT + 1)
    for x in range(-max_coordinate, max_coordinate + 1):
        for y in range(-max_coordinate, max_coordinate + 1):
            if x == 0 and y == 0:
                continue
            norm = x * x + y * y
            if norm > CHECK_LIMIT or norm % 2 == 0:
                continue
            if math.gcd(abs(x), abs(y)) == 1:
                primitive_norm_counts[norm] += 1
    for n in range(1, CHECK_LIMIT + 1, 2):
        if primitive_norm_counts[n] != 4 * base_coefficient(n, spf):
            raise ArithmeticError(f"primitive odd-circle coefficient failed at n={n}")
        primitive_representation_checks += 1

    for r in range(1, 32):
        for s in range(r + 1, 32):
            if math.gcd(r, s) != 1:
                continue
            rs = r * s
            for m in range(1, 129):
                direct = primitive_height_weight(m, rs, spf) + (1 if m == 1 else 0)
                convolved = corrected_convolution_weight(m, rs, spf)
                if convolved != direct:
                    raise ArithmeticError("fixed-rs correction convolution failed")
                correction_checks += 1

    for p in prime_sieve(2000):
        if p % 4 != 1:
            continue
        beta = Fraction(2 * (p - 1), p + 1)
        if not (Fraction(0, 1) <= beta < Fraction(2, 1)):
            raise ArithmeticError("beta local domination failed")
        beta_domination_checks += 1

    sample_l1 = []
    for rs in [1, 5, 13, 25, 65, 85, 221, 1105]:
        sample_l1.append(correction_l1_half(rs, spf))

    return {
        "base_dirichlet_coefficient_checks": base_checks,
        "primitive_odd_circle_representation_checks": primitive_representation_checks,
        "fixed_rs_correction_convolution_checks": correction_checks,
        "beta_local_domination_checks": beta_domination_checks,
        "largest_sample_correction_l1_half": max(sample_l1),
    }


def asymptotic_diagnostics() -> list[dict[str, float]]:
    rows: list[dict[str, float]] = []
    for log_b in [32.0, 64.0, 128.0, 256.0, 512.0, 1024.0]:
        tau = log_b ** (-0.75)
        log_x0 = tau * log_b
        if log_x0 > 1.0:
            omega_proxy = math.exp(
                -(log_x0 ** 0.6) * (math.log(log_x0) ** -0.2)
            )
        else:
            omega_proxy = math.exp(-math.sqrt(log_x0))
        rows.append(
            {
                "log_B": log_b,
                "tau": tau,
                "primitive_shallow_fraction": 3.0 * tau**2 - 2.0 * tau**3,
                "primitive_shallow_log_degree_proxy": (
                    log_b**3 * (3.0 * tau**2 - 2.0 * tau**3)
                ),
                "retained_log_X_min": log_x0,
                "retained_X_min": math.exp(log_x0),
                "primitive_circle_zero_free_decay_proxy": omega_proxy,
                "retained_error_log2_proxy": log_b**2 * omega_proxy,
            }
        )
    return rows


def build_report() -> dict[str, Any]:
    spf = build_spf(max(CHECK_LIMIT, 32 * 32, 2000))
    checks = run_finite_checks(spf)
    products = euler_products(PRIME_LIMIT)

    return {
        "metadata": {
            "stage": "12-N1-2k",
            "title": "Final primitive remainder, Euler constant, and beta two-modulus audit",
            "generated_by": "scripts/audit_final_remainder_stage12_n1_2k.py",
            "claim_status": (
                "The primitive-oriented leading asymptotic is reduced to standard fixed-domain "
                "primitive-circle and multivariable mean-value theorems; exact algebra and finite "
                "regressions are audited, while the numerical Euler product is not an enclosure."
            ),
        },
        "fixed_base_coefficient": {
            "definition": (
                "a0(n)=2^omega(n) when every prime divisor is 1 mod4, and a0(n)=0 otherwise."
            ),
            "dirichlet_series": (
                "sum a0(n)n^-s=zeta(s)L(s,chi4)/((1+2^-s)zeta(2s))."
            ),
            "geometric_identity": (
                "For odd n, 4*a0(n) is exactly the number of primitive integer pairs "
                "(x,y) with x^2+y^2=n."
            ),
            "summatory_estimate": (
                "A0(X)=X/pi+O(sqrt(X)*omega(X)), "
                "omega(X)=exp(-c(log X)^(3/5)(loglog X)^(-1/5)); "
                "this is the fixed disk primitive-lattice estimate with a finite parity split."
            ),
            "why_uniformity_disappears": (
                "The domain in the m-sum is one fixed disk/parity problem; r,s occur only "
                "in a finite Euler correction, so no varying-eccentricity theorem is required."
            ),
        },
        "fixed_rs_convolution": {
            "series_factorization": (
                "F_rs(s)=G(rs)*F0(s)*H_rs(s), with "
                "H_rs(s)=product_{p^t||rs,p=1 mod4}(1-((2t-1)/(2t+1))*p^-s)/(1+p^-s)."
            ),
            "local_coefficients": (
                "h_rs(p^j)=(-1)^j*4t/(2t+1) for j>=1 and p^t||rs, and zero "
                "for primes outside the 1 mod4 support of rs."
            ),
            "uniform_partial_sum": (
                "sum_{m<=X}A_rs(m)=gamma(rs)X-1+"
                "O(G(rs)H_abs(rs)sqrt(X)omega(X)), where "
                "H_abs(rs)=product(1+(4t/(2t+1))/(sqrt(p)-1))."
            ),
            "average_weight": (
                "W(n)=G(n)H_abs(n) is a fixed nonnegative multiplicative weight with "
                "Dirichlet pole order 2, hence sum_{n<=R}W(n)<<R log R."
            ),
            "global_retained_error": (
                "After summing coprime r,s, the retained fixed-rs remainder is "
                "<<B(log B)^2*omega(X0), with X0=exp((log B)^(1/4)); "
                "it is o(B(log B)^-A) for every fixed A."
            ),
            "shallow_region": (
                "With tau=(log B)^(-3/4), the primitive shallow contribution is "
                "O(B(log B)^(3/2+o(1))), hence o(B(log B)^3)."
            ),
        },
        "beta_two_modulus_main": {
            "beta": (
                "beta is multiplicative, supported on primes 1 mod4, with "
                "beta(p^j)=2(p-1)/(p+1) for j>=1."
            ),
            "local_factor": (
                "For q=1 mod4 the coprime two-modulus density factor is "
                "1+4q/(q+1)^2."
            ),
            "eta_euler_product": (
                "eta=(pi/4)^2*(1/2)^2*product_{p=3 mod4}(1-p^-2)^2*"
                "product_{q=1 mod4}(1+4q/(q+1)^2)(1-q^-1)^4."
            ),
            "standard_mean_value_input": (
                "The nonnegative two-variable coefficient system satisfies the hypotheses "
                "of de la Breteche's multiple-sum theorem; smooth dyadic partition and "
                "partial summation give a degree-3 logarithmic polynomial, while the "
                "Stage12-N1-2i core/wing bounds control smoothing and endpoints."
            ),
            "core_wing_transfer": (
                "0<=beta(p^j)<2, so the beta divisor weights are dominated by the fixed "
                "Ramanujan/divisor weights already admitted in the Stage12-N1-2i "
                "core and wing estimates."
            ),
        },
        "constant_identity": {
            "q_1mod4_ratio": (
                "eta_q/kappa_q=q^2/(q^2-1)=(1-q^-2)^-1."
            ),
            "p_3mod4_ratio": (
                "eta_p/kappa_p=(1-p^-2)^-1."
            ),
            "archimedean_two_adic_ratio": "eta_front/kappa_front=8/pi.",
            "odd_prime_product": (
                "product_{p odd}(1-p^-2)^-1=(1-2^-2)zeta(2)=pi^2/8."
            ),
            "exact_conclusion": "eta=pi*kappa.",
            "leading_constant": (
                "eta/(12*pi^2)=kappa/(12*pi)."
            ),
        },
        "final_asymptotic": {
            "counted_object": (
                "The primitive oriented Stage12-N1-2 count C_prim(B) defined in "
                "docs/stage12-n1-2b-average.md; repeated-side contribution is identically zero."
            ),
            "result": (
                "C_prim(B)~(kappa/(12*pi))*B*(log B)^3."
            ),
            "scope": (
                "This does not assert existence or nonexistence of a perfect cuboid and does "
                "not automatically convert an oriented multiplicity count into a separate "
                "exact-multiplicity theorem beyond the Stage12-N1 definition."
            ),
        },
        "finite_checks": checks,
        "euler_product_diagnostic": products,
        "cutoff_diagnostics": asymptotic_diagnostics(),
        "decision": {
            "classification": "A_N1_2_leading_asymptotic_closed_at_standard_theorem_level_series_complete",
            "closed": [
                "The fixed-rs remainder is reduced to a fixed primitive-circle estimate with finite local corrections.",
                "The averaged correction weight has only pole order 2 and the retained remainder is lower order.",
                "The beta two-modulus Euler product has the required degree and is compatible with the existing core/wing estimates.",
                "The identity eta=pi*kappa is exact prime by prime.",
                "The primitive oriented leading asymptotic and leading constant are determined at the standard-theorem application level.",
            ],
            "remaining_after_series": [
                "Independent AI or human review of the proof chain from Stage12-N1-2b through 2k.",
                "Optional conversion into a single publication-style theorem/proof document.",
                "Any separate exact-multiplicity subtraction not already included in the Stage12-N1 definition.",
            ],
            "next_stage": (
                "No automatic Stage12-N1-2l is recommended. Stop the N1-2 derivation here "
                "and perform an adversarial AI review of Stages 2b-2k."
            ),
        },
        "not_claimed": [
            "A certified numerical enclosure for kappa or eta.",
            "A new primitive-lattice theorem; the fixed-domain remainder is an application of known results.",
            "A perfect-cuboid existence or nonexistence theorem.",
            "That the research note has already received independent peer review.",
        ],
        "literature": [
            {
                "work": (
                    "Wenguang Zhai, On primitive lattice points in planar domains, "
                    "Acta Arithmetica 109 (2003), 1-26."
                ),
                "role": (
                    "Unconditional fixed-domain primitive lattice-point remainder "
                    "O(X^(1/2)omega(X))."
                ),
            },
            {
                "work": (
                    "Regis de la Breteche, Estimation de sommes multiples de fonctions "
                    "arithmetiques, Compositio Mathematica 128 (2001), 261-298."
                ),
                "role": (
                    "Multiple Dirichlet-series mean-value theorem for the beta two-modulus main term."
                ),
            },
            {
                "work": (
                    "Regis de la Breteche and Gerald Tenenbaum, Remarks on the "
                    "Selberg-Delange method, Acta Arithmetica 200 (2021), 349-369."
                ),
                "role": (
                    "One-variable multiplicative mean-value framework for the fixed correction weight."
                ),
            },
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    report = build_report()
    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"

    if args.check:
        if not args.output.exists():
            raise SystemExit(f"missing report: {args.output}")
        if args.output.read_text(encoding="utf-8") != rendered:
            raise SystemExit(f"report is stale: {args.output}")
        print(f"verified {args.output}")
        return

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(rendered, encoding="utf-8")
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
