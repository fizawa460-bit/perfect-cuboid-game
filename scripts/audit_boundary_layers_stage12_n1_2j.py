#!/usr/bin/env python3
"""Stage12-N1-2j: primitive-first Möbius and boundary-layer audit.

The audit moves global Möbius inversion inside the h-parameter before any
shallow-height or terminal-u cut.  It proves the exact local convolution
formula, checks both parity classes, derives the fixed-(r,s) Dirichlet series
and residue weight, and compares the direct primitive-first enumeration with
the previous global-Möbius counts through B=200000.

No uniform Selberg-Delange theorem over the full (r,s) family, and no final
N1 asymptotic, is claimed here.
"""
from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

DEFAULT_REPORT = Path("data/boundary_layers_stage12_n1_2j_report.json")
MAX_B = 200_000
THRESHOLDS = [1_000, 2_000, 5_000, 10_000, 20_000, 50_000, 100_000, 200_000]
EXPECTED_PRIMITIVE = {
    1_000: 1_208,
    2_000: 2_888,
    5_000: 9_030,
    10_000: 21_360,
    20_000: 49_592,
    50_000: 147_998,
    100_000: 336_416,
    200_000: 760_206,
}
EULER_PRODUCT_LIMIT = 200_000


def build_spf(limit: int) -> list[int]:
    spf = list(range(limit + 1))
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


def g_from_factor(factors: dict[int, int]) -> int:
    value = 1
    for p, exponent in factors.items():
        if p % 4 == 1:
            value *= 2 * exponent + 1
    return value


def g_value(n: int, spf: list[int]) -> int:
    return g_from_factor(factor_dict(n, spf))


def mobius_sieve(limit: int) -> list[int]:
    mu = [0] * (limit + 1)
    mu[1] = 1
    primes: list[int] = []
    composite = [False] * (limit + 1)
    for n in range(2, limit + 1):
        if not composite[n]:
            primes.append(n)
            mu[n] = -1
        for p in primes:
            if n * p > limit:
                break
            composite[n * p] = True
            if n % p == 0:
                mu[n * p] = 0
                break
            mu[n * p] = -mu[n]
    return mu


def primitive_weight_from_factors(
    m: int,
    rs_factors: dict[int, int],
    m_factors: dict[int, int],
) -> int:
    """A_{r,s}(m)=sum_{k|m} mu(k)(G((m/k)rs)-1)."""
    base = g_from_factor(rs_factors)
    if m == 1:
        return base - 1
    value = base
    for p in m_factors:
        if p % 4 != 1:
            return 0
        denominator = 2 * rs_factors.get(p, 0) + 1
        value = value // denominator * 2
    return value


def convolution_weight(
    m: int,
    rs: int,
    spf: list[int],
    mu: list[int],
) -> int:
    return sum(
        mu[k] * (g_value((m // k) * rs, spf) - 1)
        for k in divisors_from_factor(factor_dict(m, spf))
    )


def parity_convolution_weight(
    n: int,
    rs: int,
    opposite_parity: bool,
    spf: list[int],
    mu: list[int],
) -> int:
    total = 0
    for k in divisors_from_factor(factor_dict(n, spf)):
        quotient = n // k
        if opposite_parity and quotient % 2:
            continue
        total += mu[k] * (g_value(quotient * rs, spf) - 1)
    return total


def predicted_parity_weight(
    n: int,
    rs_factors: dict[int, int],
    opposite_parity: bool,
    spf: list[int],
) -> int:
    if opposite_parity:
        if n % 2 or n % 4 == 0:
            return 0
        m = n // 2
    else:
        m = n
    return primitive_weight_from_factors(m, rs_factors, factor_dict(m, spf))


def prefix(values: list[int]) -> list[int]:
    out = [0] * len(values)
    running = 0
    for index, value in enumerate(values):
        running += value
        out[index] = running
    return out


def direct_primitive_prefix(limit: int, spf: list[int]) -> tuple[list[int], dict[str, int]]:
    exact = [0] * (limit + 1)
    pair_count = 0
    nonzero_terms = 0
    max_s = math.isqrt(2 * limit) + 1

    for r in range(1, max_s + 1):
        for s in range(r + 1, max_s + 1):
            q = r * r + s * s
            if q > 2 * limit:
                break
            if math.gcd(r, s) != 1:
                continue

            both_odd = (r % 2 == 1 and s % 2 == 1)
            if both_odd:
                max_m = (2 * limit) // q
            else:
                max_m = limit // q
            if max_m < 1:
                continue

            pair_count += 1
            rs_factors = factor_dict(r * s, spf)
            for m in range(1, max_m + 1):
                weight = primitive_weight_from_factors(
                    m,
                    rs_factors,
                    factor_dict(m, spf),
                )
                if weight == 0:
                    continue
                height = m * q // 2 if both_odd else m * q
                exact[height] += weight
                nonzero_terms += 1

    return prefix(exact), {
        "primitive_pair_parameter_blocks": pair_count,
        "nonzero_direct_weight_terms": nonzero_terms,
    }


def prime_sieve(limit: int) -> list[int]:
    is_prime = bytearray(b"\x01") * (limit + 1)
    is_prime[:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if is_prime[p]:
            is_prime[p * p : limit + 1 : p] = b"\x00" * (((limit - p * p) // p) + 1)
    return [p for p in range(2, limit + 1) if is_prime[p]]


def euler_constant_diagnostic(prime_limit: int) -> dict[str, float | int]:
    primes = prime_sieve(prime_limit)

    log_raw_h = 3.0 * math.log(0.5)
    for p in primes:
        if p == 2:
            continue
        if p % 4 == 1:
            raw_local = 1.0 + 2.0 / (p - 1.0) + 4.0 * p / (p * p - 1.0)
            normalized = raw_local * (1.0 - 1.0 / p) ** 6
        else:
            normalized = (1.0 - 1.0 / (p * p)) ** 3
        log_raw_h += math.log(normalized)
    kappa = (math.pi / 4.0) ** 3 * math.exp(log_raw_h)

    log_primitive_h = 2.0 * math.log(0.5)
    for p in primes:
        if p == 2:
            continue
        if p % 4 == 1:
            primitive_local = 1.0 + 4.0 * p / (p + 1.0) ** 2
            normalized = primitive_local * (1.0 - 1.0 / p) ** 4
        else:
            normalized = (1.0 - 1.0 / (p * p)) ** 2
        log_primitive_h += math.log(normalized)
    eta = (math.pi / 4.0) ** 2 * math.exp(log_primitive_h)

    return {
        "prime_cutoff": prime_limit,
        "stage12_kappa_partial": kappa,
        "primitive_two_modulus_eta_partial": eta,
        "eta_over_pi_kappa": eta / (math.pi * kappa),
        "candidate_primitive_constant_from_eta": eta / (12.0 * math.pi * math.pi),
        "candidate_primitive_constant_from_kappa": kappa / (12.0 * math.pi),
    }


def run_exact_checks(spf: list[int], mu: list[int]) -> dict[str, int]:
    local_checks = 0
    parity_checks = 0
    residue_checks = 0
    beta_checks = 0

    for r in range(1, 24):
        for s in range(r + 1, 24):
            if math.gcd(r, s) != 1:
                continue
            rs = r * s
            rs_factors = factor_dict(rs, spf)
            opposite = (r + s) % 2 == 1
            for m in range(1, 97):
                direct = primitive_weight_from_factors(m, rs_factors, factor_dict(m, spf))
                if direct != convolution_weight(m, rs, spf, mu):
                    raise ArithmeticError("primitive local convolution identity failed")
                local_checks += 1
            for n in range(1, 129):
                actual = parity_convolution_weight(n, rs, opposite, spf, mu)
                predicted = predicted_parity_weight(n, rs_factors, opposite, spf)
                if actual != predicted:
                    raise ArithmeticError("parity-restricted convolution identity failed")
                parity_checks += 1

    for p in prime_sieve(500):
        if p % 4 != 1:
            continue
        for exponent in range(1, 9):
            residue_local = Fraction(
                (2 * exponent + 1) * p - (2 * exponent - 1),
                p + 1,
            )
            beta_sum = 1 + exponent * Fraction(2 * (p - 1), p + 1)
            if residue_local != beta_sum:
                raise ArithmeticError("residue/beta local identity failed")
            residue_checks += 1

    for n in range(1, 1_001):
        factors = factor_dict(n, spf)
        residue_product = Fraction(1, 1)
        for p, exponent in factors.items():
            if p % 4 == 1:
                residue_product *= 1 + exponent * Fraction(2 * (p - 1), p + 1)

        beta_divisor_sum = Fraction(0, 1)
        for d in divisors_from_factor(factors):
            beta = Fraction(1, 1)
            for p in factor_dict(d, spf):
                if p % 4 != 1:
                    beta = Fraction(0, 1)
                    break
                beta *= Fraction(2 * (p - 1), p + 1)
            beta_divisor_sum += beta
        if residue_product != beta_divisor_sum:
            raise ArithmeticError("global residue divisor expansion failed")
        beta_checks += 1

    return {
        "local_mobius_convolution_checks": local_checks,
        "parity_convolution_checks": parity_checks,
        "residue_local_checks": residue_checks,
        "beta_divisor_expansion_checks": beta_checks,
    }


def boundary_diagnostics() -> list[dict[str, float]]:
    rows: list[dict[str, float]] = []
    for log_b in [16.0, 32.0, 64.0, 128.0, 256.0, 512.0]:
        tau = log_b ** (-0.75)
        raw_fraction = 6.0 * tau**2 - 8.0 * tau**3 + 3.0 * tau**4
        primitive_fraction = 3.0 * tau**2 - 2.0 * tau**3
        retained_log_height = tau * log_b
        rows.append(
            {
                "log_B": log_b,
                "tau_equals_logB_power_minus_3_over_4": tau,
                "old_raw_shallow_fraction": raw_fraction,
                "primitive_first_shallow_fraction": primitive_fraction,
                "primitive_shallow_log_mass_L3_times_fraction": log_b**3 * primitive_fraction,
                "retained_log_height_tau_L": retained_log_height,
                "retained_short_side_proxy": math.exp(0.5 * retained_log_height),
                "baseline_selberg_delange_decay_proxy": math.exp(-math.sqrt(retained_log_height)),
            }
        )
    return rows


def build_report() -> dict[str, Any]:
    spf = build_spf(2 * MAX_B)
    mu = mobius_sieve(2 * MAX_B)
    exact_checks = run_exact_checks(spf, mu)
    primitive_prefix, enumeration_meta = direct_primitive_prefix(MAX_B, spf)

    count_rows: list[dict[str, int]] = []
    for bound in THRESHOLDS:
        direct = primitive_prefix[bound]
        expected = EXPECTED_PRIMITIVE[bound]
        if direct != expected:
            raise ArithmeticError(f"primitive-first regression failed at B={bound}")
        count_rows.append(
            {
                "B": bound,
                "primitive_first_direct_count": direct,
                "previous_global_mobius_count": expected,
                "difference": direct - expected,
            }
        )

    return {
        "metadata": {
            "stage": "12-N1-2j",
            "title": "Primitive-first Möbius and boundary-layer audit",
            "generated_by": "scripts/audit_boundary_layers_stage12_n1_2j.py",
            "claim_status": (
                "Exact primitive-first convolution, parity support, residue algebra, "
                "and finite count equivalence; uniform averaged remainder remains open."
            ),
        },
        "exact_primitive_first_identity": {
            "global_identity": (
                "C_prim(B)=sum_k mu(k) C_raw(floor(B/k)); reindex n=k*h "
                "before any dyadic or boundary cut."
            ),
            "same_parity_case": (
                "For r,s odd, q=r^2+s^2 is even. The effective primitive height n is odd "
                "and supported only on primes 1 mod4."
            ),
            "opposite_parity_case": (
                "For r,s of opposite parity, q is odd and raw h is even. The reindexed "
                "height has v_2(n)=1 exactly, so n=2m with m odd and supported only on "
                "primes 1 mod4."
            ),
            "direct_count": (
                "For r,s odd use m<=2B/(r^2+s^2); for opposite parity use "
                "m<=B/(r^2+s^2)."
            ),
        },
        "primitive_weight": {
            "definition": "A_{r,s}(m)=sum_{k|m} mu(k)*(G((m/k)rs)-1)",
            "m_equals_1": "A_{r,s}(1)=G(rs)-1",
            "m_greater_1": (
                "A_{r,s}(m)=0 unless every prime dividing m is 1 mod4; otherwise "
                "A_{r,s}(m)=G(rs)*product_{p|m} 2/(2*v_p(rs)+1)."
            ),
            "sign": "All direct primitive-first weights are nonnegative.",
            "finite_checks": exact_checks,
        },
        "fixed_rs_dirichlet_series": {
            "positive_version": "A^+_{r,s}(m)=A_{r,s}(m)+1_{m=1}",
            "series": (
                "sum_m A^+_{r,s}(m)m^-s = G(rs)*product_{p=1 mod4}" 
                "[1 + (2/(2*v_p(rs)+1))*p^-s/(1-p^-s)]."
            ),
            "base_product": (
                "product_{p=1 mod4}(1+2*p^-s/(1-p^-s))="
                "zeta(s)L(s,chi_4)/((1+2^-s)zeta(2s))."
            ),
            "finite_local_correction": (
                "For p^t||rs, divide the base local factor by replacing it with "
                "R_{p,t}(s)=(1-((2t-1)/(2t+1))*p^-s)/(1+p^-s)."
            ),
            "base_residue": "The base product has residue 1/pi at s=1.",
            "residue_weight": (
                "gamma(rs)=(1/pi)*product_{p^t||rs,p=1 mod4}" 
                "[1+2t(p-1)/(p+1)]."
            ),
        },
        "two_modulus_divisor_expansion": {
            "beta": (
                "beta is multiplicative, supported on primes 1 mod4, with "
                "beta(p^j)=2(p-1)/(p+1) for every j>=1."
            ),
            "identity": (
                "gamma(n)=(1/pi)*sum_{d|n} beta(d). Since gcd(r,s)=1, "
                "the residue weight separates into one divisor modulus on r and one on s."
            ),
            "consequence": (
                "After the h-sum, the primitive problem has two divisor moduli rather than "
                "the raw three-modulus family. The radial logarithm then gives the third "
                "logarithmic degree."
            ),
        },
        "boundary_layer_resolution": {
            "outer_mobius": (
                "There is no absolute outer-Mobius error sum after the exact reindexing; "
                "the conservative raw target B(log B)^(2-eta) is therefore no longer the "
                "boundary-layer requirement."
            ),
            "terminal_u": (
                "The h=a*u decomposition is not used. The full m partial sum is evaluated "
                "at once, so the terminal-u layer disappears rather than being discarded."
            ),
            "primitive_simplex": (
                "The formal primitive logarithmic simplex is integral "
                "(L-2max(y,z)) dy dz=L^3/12."
            ),
            "shallow_fraction": (
                "For t=L-2max(y,z)<=tau*L, the exact primitive-main fraction is "
                "3*tau^2-2*tau^3."
            ),
            "canonical_cut": (
                "Taking tau=L^(-3/4) makes the shallow formal mass O(B*L^(3/2)), "
                "while the retained short-side proxy is exp(0.5*L^(1/4)), which still "
                "beats every fixed logarithmic loss in the Stage12-N1-2i estimates."
            ),
            "diagnostics": boundary_diagnostics(),
        },
        "uniform_remainder_target": {
            "candidate_fixed_rs_asymptotic": (
                "sum_{m<=X} A_{r,s}(m)=gamma(rs)*X-1+R_{r,s}(X)."
            ),
            "sufficient_average_form": (
                "It is enough to prove an averaged estimate for R_{r,s}(X) with "
                "exp(-c*sqrt(log X)) or any fixed negative power of log X on the retained "
                "X>=exp((log B)^(1/4)) range, allowing fixed divisor-weight losses."
            ),
            "method": (
                "Apply Selberg-Delange/Perron to the base product and absorb the finite "
                "R_{p,t} corrections through their absolutely summable local coefficients."
            ),
            "remaining_issue": (
                "The required uniformity is averaged over the changing rs family; it is not "
                "asserted as a direct corollary of a cited fixed-function theorem."
            ),
        },
        "finite_count_equivalence": {
            "through_B": MAX_B,
            **enumeration_meta,
            "rows": count_rows,
        },
        "euler_constant_diagnostic": euler_constant_diagnostic(EULER_PRODUCT_LIMIT),
        "decision": {
            "classification": "A_primitive_first_boundary_layers_close_uniform_average_remainder_open",
            "closed": [
                "Global Mobius inversion can be moved inside the h-parameter exactly.",
                "Both parity cases reduce to an explicit nonnegative primitive height weight.",
                "Direct primitive-first counts equal all previous global-Mobius counts through B=200000.",
                "The terminal-u layer disappears and the shallow primitive layer is lower order with a compatible cutoff.",
                "The fixed-rs residue has an exact two-modulus beta divisor expansion.",
            ],
            "not_closed": [
                "A fully written uniform averaged Selberg-Delange remainder over r,s.",
                "Final smoothing and endpoint bookkeeping after replacing lambda_1 by beta.",
                "A proved primitive N1 asymptotic with the candidate constant.",
            ],
            "next_stage": (
                "12-N1-2k: prove the averaged fixed-rs partial-sum remainder, match the "
                "two-modulus Euler constant to kappa, and rerun the retained core/wing "
                "bookkeeping with beta weights."
            ),
        },
        "not_claimed": [
            "That a uniform Selberg-Delange estimate has already been proved for every rs.",
            "That the partial Euler products are certified enclosures.",
            "That the Stage12-N1-2i smoothing argument is already a complete published proof.",
            "A final raw or primitive asymptotic theorem.",
        ],
        "literature": [
            {
                "work": "de la Breteche and Tenenbaum, Remarks on the Selberg-Delange method, arXiv:2010.12929",
                "role": "Framework for partial sums of multiplicative functions with zeta-power Dirichlet series.",
                "limitation": "Stage12 still needs parameter-uniform averaged control of the finite rs corrections.",
            }
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()
    report = build_report()
    args.write_report.parent.mkdir(parents=True, exist_ok=True)
    args.write_report.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report["decision"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
