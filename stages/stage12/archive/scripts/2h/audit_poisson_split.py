#!/usr/bin/env python3
"""Stage12-N1-2h: Poisson/modulus/eccentricity compatibility audit.

The audit finds an exact reorganization that combines visibility, local
coprimality, and parity before Poisson summation.  For odd pairwise-coprime
b,c and an odd visibility divisor d coprime to bc, the scaled coordinates
x=bv and y=cw form a union of residue classes in a *square* period
Q=2*b*c*d.  The Fourier coefficients are Ramanujan sums.

This removes geometric eccentricity in the two-dimensional Poisson core.
The remaining dual phase is reciprocal and nonlinear:
    exp(± const * sqrt(k^2+l^2)/(b*c*d*sqrt(u))).
The script fixes the logarithmic mass split and audits which portions are
compatible with elementary spacing, two-dimensional Poisson, or a required
one-dimensional treatment.  No asymptotic or new exponential-sum theorem is
claimed.
"""
from __future__ import annotations

import argparse
import cmath
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

DEFAULT_REPORT = Path("data/poisson_split_stage12_n1_2h_report.json")
MAX_ODD_MODULUS_CHECK = 31
MAX_FOURIER_MULTIPLIER = 3
LOG_DIAGNOSTICS = [16.0, 32.0, 64.0, 128.0, 256.0]


def mobius(n: int) -> int:
    value = 1
    p = 2
    while p * p <= n:
        if n % p:
            p += 1
            continue
        n //= p
        value = -value
        if n % p == 0:
            return 0
        while n % p == 0:
            n //= p
        p += 1
    if n > 1:
        value = -value
    return value


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def ramanujan_sum(q: int, k: int) -> int:
    g = math.gcd(q, abs(k))
    return sum(d * mobius(q // d) for d in divisors(g))


def direct_coefficient(modulus: int, residues: list[int], k: int) -> complex:
    return sum(cmath.exp(2j * math.pi * k * r / modulus) for r in residues)


def coefficient_checks() -> dict[str, int]:
    checks = 0
    common_period_checks = 0
    for q in range(1, MAX_ODD_MODULUS_CHECK + 1, 2):
        odd_units = [r for r in range(2 * q) if r % 2 == 1 and math.gcd(r, q) == 1]
        even_coprime = [r for r in range(2 * q) if r % 2 == 0 and math.gcd(r, q) == 1]
        if len(odd_units) != sum(1 for r in range(2 * q) if math.gcd(r, 2 * q) == 1):
            raise ArithmeticError("odd-unit residue identification failed")
        for k in range(-MAX_FOURIER_MULTIPLIER * q, MAX_FOURIER_MULTIPLIER * q + 1):
            odd_value = direct_coefficient(2 * q, odd_units, k)
            even_value = direct_coefficient(2 * q, even_coprime, k)
            if abs(odd_value - ramanujan_sum(2 * q, k)) > 1e-8:
                raise ArithmeticError(f"odd coefficient failed for q={q}, k={k}")
            if abs(even_value - ramanujan_sum(q, k)) > 1e-8:
                raise ArithmeticError(f"even coefficient failed for q={q}, k={k}")
            checks += 2

    odds = list(range(1, 16, 2))
    for b in odds:
        for c in odds:
            if math.gcd(b, c) != 1:
                continue
            for d in odds:
                if math.gcd(d, b * c) != 1:
                    continue
                qx = b * d * (2 * c)
                qy = c * d * (2 * b)
                if qx != qy or qx != 2 * b * c * d:
                    raise ArithmeticError("common square period failed")
                common_period_checks += 1
    return {
        "ramanujan_fourier_coefficient_checks": checks,
        "common_square_period_checks": common_period_checks,
    }


def shallow_fraction(tau: float) -> float:
    return 6.0 * tau**2 - 8.0 * tau**3 + 3.0 * tau**4


def cutoff_diagnostics() -> list[dict[str, float]]:
    rows: list[dict[str, float]] = []
    for L in LOG_DIAGNOSTICS:
        eta = L ** (-0.25)
        sigma = eta
        min_side = math.exp(0.5 * math.sqrt(L))
        visibility_cutoff = math.exp(0.25 * math.sqrt(L))
        rows.append(
            {
                "log_B": L,
                "eta_equals_sigma": eta,
                "shallow_main_fraction_bound": shallow_fraction(eta),
                "terminal_u_harmonic_fraction": sigma,
                "deep_terminal_short_side_lower_bound": min_side,
                "visibility_cutoff_D": visibility_cutoff,
                "post_small_d_short_side_lower_bound": min_side / visibility_cutoff,
                "large_d_area_tail_factor_bound": 1.0 / (visibility_cutoff - 1.0),
            }
        )
    return rows


def build_report() -> dict[str, Any]:
    checks = coefficient_checks()

    total = Fraction(1, 48)
    two_dimensional_core = Fraction(1, 64)
    separated_core = Fraction(3, 512)
    clustered_core = two_dimensional_core - separated_core
    one_dimensional_wing = total - two_dimensional_core

    if two_dimensional_core / total != Fraction(3, 4):
        raise AssertionError("Q<=R fraction must be 3/4")
    if separated_core / total != Fraction(9, 32):
        raise AssertionError("Q<=sqrt(R) fraction must be 9/32")
    if clustered_core / total != Fraction(15, 32):
        raise AssertionError("middle fraction must be 15/32")
    if one_dimensional_wing / total != Fraction(1, 4):
        raise AssertionError("wing fraction must be 1/4")

    return {
        "metadata": {
            "stage": "12-N1-2h",
            "title": "Poisson, modulus, and eccentricity decomposition audit",
            "generated_by": "scripts/audit_poisson_split_stage12_n1_2h.py",
            "claim_status": (
                "Exact periodic/Fourier algebra and logarithmic mass decomposition; "
                "method compatibility only, with no asymptotic or new exponential-sum theorem claimed."
            ),
        },
        "starting_point": {
            "variables": "h=a*u, r=b*v, s=c*w with a,b,c odd, pairwise coprime, and supported on primes 1 mod4",
            "domain": "a*u*((b*v)^2+(c*w)^2)<=2B and b*v<c*w",
            "coprimality": "gcd(v,w)=gcd(v,c)=gcd(w,b)=1",
            "parity": "v,w odd with arbitrary u, or v,w of opposite parity with even u",
        },
        "deep_terminal_split": {
            "log_variables": "t=log U=log(B/(a*max(b,c)^2)); the formal main density is t",
            "shallow_fraction": "For 0<=tau<=1, the portion with t<=tau*log B is 6*tau^2-8*tau^3+3*tau^4.",
            "terminal_u_split": (
                "Within one modulus block, restricting u<=U^(1-sigma) removes exactly a sigma fraction "
                "of the harmonic log U main term and forces the shorter original lattice length "
                "sqrt(U/u)>=U^(sigma/2)."
            ),
            "canonical_choice": (
                "With eta=sigma=(log B)^(-1/4), shallow mass is O((log B)^(-1/2)), "
                "terminal mass is O((log B)^(-1/4)), and the retained shorter length is at least "
                "exp(0.5*sqrt(log B))."
            ),
            "visibility_split": (
                "For a slice with original side lengths V,W and D>=1, "
                "sum_{d>D} floor(V/d)floor(W/d)<=V*W*sum_{d>D}d^-2<=V*W/(D-1). "
                "Taking D as the square root of the retained shorter length makes the large-d tail "
                "subexponentially small while leaving both divided side lengths subexponentially large."
            ),
            "diagnostics": cutoff_diagnostics(),
        },
        "parity_local_coprimality_fourier_algebra": {
            "visibility": (
                "After the parity cases exclude both v,w even, "
                "1_{gcd(v,w)=1}=sum_{d odd, d|v,w}mu(d). "
                "The local conditions force gcd(d,b*c)=1."
            ),
            "substitution": "v=d*m and w=d*n; use scaled coordinates x=b*d*m and y=c*d*n.",
            "common_period": "Both coordinates have the same physical period Q=2*b*c*d.",
            "parity_fourier_coefficients": {
                "odd_m_coprime_c": "sum over odd r mod 2c with gcd(r,c)=1 equals the Ramanujan coefficient c_{2c}(k)",
                "even_m_coprime_c": "sum over even r mod 2c with gcd(r,c)=1 equals c_c(k)",
                "odd_n_coprime_b": "c_{2b}(l)",
                "even_n_coprime_b": "c_b(l)",
            },
            "poisson_formula": (
                "For a smooth sector weight W_R, one parity class equals "
                "Q^-2 * sum_{k,l} A_c(k)A_b(l) * hat(W_R)(k/Q,l/Q), Q=2bcd."
            ),
            "zero_frequency": (
                "A_c(0)=phi(c) and A_b(0)=phi(b) in every parity class; "
                "combining the odd-odd class with the two opposite-parity/even-u classes "
                "recovers the two-adic factor fixed in Stage12-N1-2f."
            ),
            "consequence": (
                "The previously anisotropic b/c ellipse is converted, in the full two-dimensional "
                "periodic formulation, into a fixed circular sector with an isotropic dual denominator Q. "
                "The arithmetic complexity moves into Ramanujan coefficients."
            ),
            "finite_checks": checks,
        },
        "dual_phase": {
            "fourier_decay_framework": (
                "After smoothing and stationary phase for the curved circular boundary, "
                "a nonzero frequency has oscillation with radial parameter "
                "Z=(R/Q)*sqrt(k^2+l^2)."
            ),
            "u_dependence": (
                "Since R is proportional to sqrt(B/a)*u^(-1/2), the phase is "
                "exp(plus_or_minus const*sqrt(B/a)*sqrt(k^2+l^2)/(b*c*d*sqrt(u)))."
            ),
            "second_derivative_test": (
                "For sum_{u~U} exp(A*u^(-1/2)), van der Corput gives "
                "O(A^(1/2)U^(-1/4)+A^(-1/2)U^(5/4)) "
                "=O(Z^(1/2)+U*Z^(-1/2)), where Z=A/sqrt(U)."
            ),
            "status": (
                "This supplies per-frequency cancellation when Z is large, but it does not by itself "
                "sum the two-dimensional frequencies, Ramanujan weights, and b,c,d blocks."
            ),
        },
        "leading_log_mass_zones": {
            "coordinates": (
                "Assume b<=c and write y=log b, z=log c, "
                "t=log(B/(a*c^2)); subpower d and smoothing shifts do not change leading fractions."
            ),
            "total_integral": "1/48 after normalizing log B=1",
            "zones": [
                {
                    "name": "A_separated_two_dimensional_core",
                    "condition": "Q<=sqrt(R), asymptotically y+z/2<=t/4",
                    "integral": "3/512",
                    "fraction_of_formal_main": "9/32",
                    "method_status": (
                        "Adjacent reciprocal moduli have phase separation R/Q^2>=1 at the lowest radial frequency, "
                        "so an additive-spacing or hybrid argument is structurally plausible."
                    ),
                },
                {
                    "name": "B_clustered_two_dimensional_core",
                    "condition": "sqrt(R)<Q<=R",
                    "integral": "5/512",
                    "fraction_of_formal_main": "15/32",
                    "method_status": (
                        "Two-dimensional Poisson remains oscillatory, but adjacent q values are unresolved "
                        "at low radial frequency; a nonlinear spacing/additive-energy estimate is required."
                    ),
                },
                {
                    "name": "C_one_dimensional_eccentric_wing",
                    "condition": "Q>R",
                    "integral": "1/192",
                    "fraction_of_formal_main": "1/4",
                    "method_status": (
                        "The common-period two-dimensional Poisson series contains many low frequencies. "
                        "Return to the original anisotropic lattice and apply one-dimensional Poisson or a "
                        "sawtooth expansion in the long direction."
                    ),
                },
            ],
            "two_dimensional_total": "Q<=R has integral 1/64 and fraction 3/4.",
            "exact_fraction_check": "9/32 + 15/32 + 8/32 = 1.",
        },
        "large_sieve_compatibility": {
            "spacing_resolution": (
                "On u~U, two moduli q,q' are distinguishable at radial frequency sqrt(m) only when "
                "R*sqrt(m)*abs(1/q-1/q') is at least order 1. "
                "For adjacent q~Q and m=1 this is R/Q^2."
            ),
            "ordinary_additive_large_sieve": (
                "Direct spacing therefore naturally covers Q<=sqrt(R), the 9/32 zone, "
                "but not the 15/32 clustered core."
            ),
            "kloosterman_or_spectral_large_sieve": (
                "Known Kloosterman large-sieve and Kloosterman-fraction estimates exploit modular inverses "
                "or genuine Kloosterman sums.  The present phase is a continuous reciprocal square-root phase "
                "with Ramanujan coefficients, so those theorems do not apply verbatim."
            ),
            "monomial_exponential_sums": (
                "After dyadic decomposition the phase belongs to a multivariable monomial/reciprocal family. "
                "Robert-Sargos-type or later monomial estimates are plausible inputs, but existing work also "
                "shows that applying dyadic-box monomial estimates mechanically can be insufficient in critical ranges."
            ),
            "required_new_bound": (
                "A weighted nonlinear hybrid inequality for "
                "sum lambda_1(b)lambda_1(c)mu(d) A_c(k)A_b(l) "
                "exp(C*sqrt(k^2+l^2)/(b*c*d*sqrt(u))), "
                "with a separate one-dimensional estimate for Q>R."
            ),
        },
        "literature_audit": [
            {
                "work": "Brandolini-Travaglini, Fourier analytic techniques for lattice point discrepancy, arXiv:1909.03439",
                "usable_part": "Poisson/Fourier and stationary-phase framework for planar convex-body discrepancy.",
                "gap": "Does not provide the required b,c,d,u-weighted Ramanujan hybrid estimate.",
            },
            {
                "work": "Drappeau, Sums of Kloosterman sums in arithmetic progressions, arXiv:1504.05549",
                "usable_part": "Power-saving technology for multilinear genuine Kloosterman sums with congruence variables.",
                "gap": "The Stage12 dual phase has no modular inverse or genuine Kloosterman kernel.",
            },
            {
                "work": "Bettin-Chandee, Trilinear forms with Kloosterman fractions, arXiv:1502.00769",
                "usable_part": "Strong bounds for reciprocal phases containing modular inverses.",
                "gap": "Its kernel e(a*inverse(m)/n) is structurally different from sqrt(k^2+l^2)/(b*c*d*sqrt(u)).",
            },
            {
                "work": "Pliego, Estimates for a three-dimensional exponential sum with monomials, arXiv:2211.02096",
                "usable_part": "Van der Corput, stationary phase, exponent-pair, and monomial-sum comparison tools.",
                "gap": "The paper itself records parameter ranges where generic dyadic-box monomial estimates are not satisfactory; the Stage12 weights and radial frequency require a dedicated budget.",
            },
        ],
        "decision": {
            "classification": "C_poisson_isotropization_succeeds_hybrid_spacing_only_partial",
            "closed": [
                "Shallow height, terminal u, and large visibility-divisor ranges admit an o(main) cutoff architecture.",
                "Parity and both local coprimality conditions can be Fourier-combined into a common square period Q=2bcd.",
                "The exact leading-log mass splits into 9/32 separated core, 15/32 clustered core, and 1/4 one-dimensional wing.",
                "The dual exponential phase and the precise large-sieve spacing barrier Q=sqrt(R) are explicit.",
            ],
            "not_closed": [
                "The 15/32 clustered reciprocal-phase core.",
                "The 1/4 one-dimensional eccentric wing.",
                "Summation of stationary-phase amplitudes and Ramanujan coefficients with lambda_1 weights.",
                "A raw error of power-saving size or O(B*(log B)^(2-eta)).",
            ],
            "next_stage": (
                "12-N1-2i: derive exponent-pair and Ramanujan-second-moment budgets for the 15/32 clustered core "
                "and the 1/4 one-dimensional wing; decide whether the concrete Poisson sums can meet the primitive-error target."
            ),
        },
        "not_claimed": [
            "A proved raw or primitive asymptotic.",
            "That the large-d and smoothing budgets have been written with final sharp constants.",
            "That existing Kloosterman or monomial theorems cannot be adapted after further transformations.",
            "That zone A is already closed; only structural compatibility and spacing are established.",
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
