#!/usr/bin/env python3
"""Stage12-N1-2e: exact divisor-indicator expansion and dyadic error budget.

The audit proves and finitely checks

  G(n) = sum_{d|n} lambda_1(d),

where lambda_1(d)=2^omega(d) when every prime divisor of d is 1 mod 4,
and lambda_1(d)=0 otherwise.  It also records the exact three-coordinate
expansion of G(h*r*s), the true modulus ranges, and a sufficient averaged
error target.  No asymptotic formula or large-sieve theorem is claimed.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

from audit_shared_p_convolution_stage11 import build_spf, factor_with_spf

DEFAULT_REPORT = Path("data/divisor_dyadic_stage12_n1_2e_report.json")
MAX_SINGLE_CHECK = 5000
MAX_TRIPLE_CHECK = 24
DOMAIN_CHECK_B = 500


def divisors(n: int, spf: list[int]) -> list[int]:
    values = [1]
    for prime, exponent in factor_with_spf(n, spf):
        powers = [prime**j for j in range(exponent + 1)]
        values = [value * power for value in values for power in powers]
    return values


def lambda_one_mod_four(n: int, spf: list[int]) -> int:
    if n == 1:
        return 1
    omega = 0
    for prime, _ in factor_with_spf(n, spf):
        if prime % 4 != 1:
            return 0
        omega += 1
    return 1 << omega


def g_weight(n: int, spf: list[int]) -> int:
    value = 1
    for prime, exponent in factor_with_spf(n, spf):
        if prime % 4 == 1:
            value *= 2 * exponent + 1
    return value


def divisor_expansion(n: int, spf: list[int]) -> int:
    return sum(lambda_one_mod_four(d, spf) for d in divisors(n, spf))


def triple_divisor_expansion(h: int, r: int, s: int, spf: list[int]) -> int:
    total = 0
    for a in divisors(h, spf):
        la = lambda_one_mod_four(a, spf)
        if la == 0:
            continue
        for b in divisors(r, spf):
            lb = lambda_one_mod_four(b, spf)
            if lb == 0 or math.gcd(a, b) != 1:
                continue
            for c in divisors(s, spf):
                lc = lambda_one_mod_four(c, spf)
                if lc == 0:
                    continue
                if math.gcd(a, c) != 1 or math.gcd(b, c) != 1:
                    continue
                total += la * lb * lc
    return total


def domain_points(bound: int) -> list[tuple[int, int, int]]:
    points: list[tuple[int, int, int]] = []
    for h in range(1, 2 * bound + 1):
        max_s = math.isqrt((2 * bound) // h)
        for r in range(1, max_s + 1):
            for s in range(r + 1, max_s + 1):
                if math.gcd(r, s) != 1:
                    continue
                if h * (r * r + s * s) > 2 * bound:
                    continue
                if h * (r * r + s * s) % 2:
                    continue
                points.append((h, r, s))
    return points


def build_report() -> dict[str, Any]:
    spf = build_spf(MAX_SINGLE_CHECK * MAX_TRIPLE_CHECK)

    single_checks = 0
    for n in range(1, MAX_SINGLE_CHECK + 1):
        if divisor_expansion(n, spf) != g_weight(n, spf):
            raise ArithmeticError(f"single-variable divisor expansion failed at n={n}")
        single_checks += 1

    triple_checks = 0
    for h in range(1, MAX_TRIPLE_CHECK + 1):
        for r in range(1, MAX_TRIPLE_CHECK + 1):
            for s in range(1, MAX_TRIPLE_CHECK + 1):
                if triple_divisor_expansion(h, r, s, spf) != g_weight(h * r * s, spf):
                    raise ArithmeticError(f"triple divisor expansion failed at {(h, r, s)}")
                triple_checks += 1

    points = domain_points(DOMAIN_CHECK_B)
    domain_checks = 0
    max_product = 0
    direct_sum = expanded_sum = 0
    for h, r, s in points:
        direct = g_weight(h * r * s, spf) - 1
        expanded = triple_divisor_expansion(h, r, s, spf) - 1
        if direct != expanded:
            raise ArithmeticError(f"domain expansion failed at {(h, r, s)}")
        if not h * r * s < DOMAIN_CHECK_B:
            raise ArithmeticError("pointwise modulus bound h*r*s<B failed")
        direct_sum += direct
        expanded_sum += expanded
        max_product = max(max_product, h * r * s)
        domain_checks += 1
    if direct_sum != expanded_sum:
        raise ArithmeticError("domain weighted sums differ")

    return {
        "metadata": {
            "stage": "12-N1-2e",
            "title": "Exact divisor expansion and dyadic modulus budget",
            "generated_by": "scripts/audit_divisor_dyadic_stage12_n1_2e.py",
            "claim_status": "Exact algebraic expansion, finite checks, and sufficient error criteria only; no asymptotic theorem claimed.",
        },
        "coefficient": {
            "name": "lambda_1",
            "definition": "lambda_1(1)=1; lambda_1(d)=2^omega(d) if every prime q|d satisfies q=1 mod4; otherwise lambda_1(d)=0",
            "local_identity": "2*v_q(n)+1 = 1 + 2*sum_{j=1}^{v_q(n)} 1 for q=1 mod4",
            "single_variable_expansion": "G(n)=sum_{d|n}lambda_1(d)",
        },
        "exact_three_coordinate_expansion": {
            "formula": "G(h*r*s)=sum_{a|h,b|r,c|s, gcd(a,b)=gcd(a,c)=gcd(b,c)=1} lambda_1(a)lambda_1(b)lambda_1(c)",
            "local_reason": "For each q=1 mod4, the multidimensional Mobius coefficient is 1 at (0,0,0), 2 when exactly one exponent is positive, and 0 when two or three exponents are positive.",
            "target_sum": "C_raw(B)=sum_{(h,r,s) in D_B} sum_{(a,b,c)!=(1,1,1), a|h,b|r,c|s, pairwise coprime} lambda_1(a)lambda_1(b)lambda_1(c)",
            "consequence": "The shared-prime correction K is absorbed exactly by the pairwise-coprime condition on the three divisor moduli.",
        },
        "scaled_lattice_form": {
            "substitution": "h=a*u, r=b*v, s=c*w",
            "conditions": [
                "a*u*(b^2*v^2+c^2*w^2)<=2B",
                "b*v<c*w",
                "gcd(v,w)=gcd(v,c)=gcd(w,b)=1, since gcd(b,c)=1",
                "u*(v^2+w^2) is even, because a,b,c are odd",
            ],
            "classification": "anisotropic lattice-point count with coprimality and parity; no quadratic-root congruence is forced by the exact G expansion",
        },
        "dyadic_ranges": {
            "original_block": "H<=h<2H, R<=r<2R, S<=s<2S",
            "admissibility": [
                "A nonempty block has H*(R^2+S^2)<=2B up to dyadic endpoint constants.",
                "The order r<s implies R<2S; neighboring diagonal blocks can be treated separately.",
                "Hence H*S^2 is O(B).",
            ],
            "divisor_blocks": [
                "A<=a<2A with A<=2H",
                "M<=b<2M with M<=2R",
                "N<=c<2N with N<=2S",
                "a,b,c are pairwise coprime and supported on primes 1 mod4",
            ],
            "pointwise_combined_modulus": "a*b*c<=h*r*s<B, since 2*r*s<r^2+s^2 for r<s",
            "scaled_lengths": "u has length about H/A, v about R/M, and w about S/N",
            "block_count": "At most O((log B)^6) dyadic blocks before exploiting admissibility.",
        },
        "required_averaged_error": {
            "block_discrepancy": "E_{a,b,c}^{H,R,S}(X)=N_{a,b,c}^{H,R,S}(X)-V_{a,b,c}^{H,R,S}(X), where V is the eventual volume/local-density main term.",
            "weighted_block_error": "mathcal_E=sum lambda_1(a)lambda_1(b)lambda_1(c) E_{a,b,c}^{H,R,S}(X) over one admissible modulus block",
            "sufficient_first_moment_target": "sum_over_admissible_blocks |mathcal_E| << X^(1-delta) for some fixed delta>0",
            "large_sieve_square_mean_translation": {
                "weight_second_moment": "W_2(A,M,N)=sum lambda_1(a)^2 lambda_1(b)^2 lambda_1(c)^2 over the modulus block",
                "cauchy_schwarz": "|mathcal_E| <= W_2(A,M,N)^(1/2) * (sum |E_{a,b,c}|^2)^(1/2)",
                "uniform_sufficient_bound": "With L=log(2X), sum |E_{a,b,c}|^2 << X^(2-2delta)/(L^12*W_2(A,M,N)) per admissible block is sufficient; O(L^6) blocks then total O(X^(1-delta)).",
                "status": "sufficient, deliberately uniform, and not asserted to be necessary or presently available",
            },
            "method_boundary": "The needed average is over three coordinate-divisibility moduli. A large sieve for roots of t^2=-1 mod m is not the immediate object produced by this exact expansion.",
        },
        "global_mobius_budget": {
            "identity": "C_prim(B)=sum_{k<=B}mu(k)C_distinct_raw(floor(B/k))",
            "absolute_error_effect": "If E(X)<<X^(1-delta)(log X)^C, then absolute summation over k gives at best O(B(log B)^C), not a preserved power saving.",
            "implication": "A raw power-saving error is sufficient only after proving that the distinct-raw main term dominates B by a logarithmic factor, or after obtaining cancellation in the outer Mobius sum.",
            "remaining_dependency": "The main-term logarithmic degree and the repeated-side subtraction must be determined before primitive asymptotics are closed.",
        },
        "audit_counts": {
            "single_variable_identity_checks": single_checks,
            "triple_identity_checks": triple_checks,
            "domain_bound": DOMAIN_CHECK_B,
            "domain_identity_checks": domain_checks,
            "domain_direct_weighted_sum": direct_sum,
            "domain_expanded_weighted_sum": expanded_sum,
            "max_h_r_s_in_domain_check": max_product,
        },
        "decision": {
            "classification": "A_exact_divisor_expansion_replaces_quadratic_root_route",
            "confirmed": [
                "G has an exact positive divisor-indicator expansion.",
                "G(h*r*s) has an exact three-coordinate expansion with pairwise-coprime divisor moduli.",
                "The full combined modulus is pointwise below B.",
                "The immediate analytic problem is a weighted lattice discrepancy over coordinate moduli, not a modular-hyperbola or quadratic-root count.",
            ],
            "next_stage": "12-N1-2f: derive the volume and local-density main term, determine its logarithmic degree, and isolate the repeated-side contribution before global Mobius inversion.",
        },
        "not_claimed": [
            "An asymptotic for C_raw or C_distinct_raw.",
            "That the sufficient square-mean estimate is known.",
            "That large-sieve methods can never be useful after another reorganization.",
            "That an O(B) post-inversion absolute error is lower order before the main logarithmic degree is proved.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()
    report = build_report()
    args.write_report.parent.mkdir(parents=True, exist_ok=True)
    args.write_report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["decision"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
