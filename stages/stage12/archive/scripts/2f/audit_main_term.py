#!/usr/bin/env python3
"""Stage12-N1-2f: formal main term, local densities, and repeated-side audit.

The audit derives the fixed-modulus volume/local-density coefficient produced by
Stage12-N1-2e, records the resulting formal logarithmic degrees, and closes the
repeated-side subtraction by reducing it to Fermat's right-triangle theorem
(equivalently Zelator, arXiv:0903.1280, Theorem 1).

The leading constants are conditional on obtaining the uniform lattice
remainder required in Stage12-N1-2e.  No asymptotic theorem is claimed here.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

DEFAULT_REPORT = Path("data/main_term_stage12_n1_2f_report.json")
MAX_B = 200_000
THRESHOLDS = [1_000, 2_000, 5_000, 10_000, 20_000, 50_000, 100_000, 200_000]
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


def build_g_table(limit: int, spf: list[int]) -> list[int]:
    g = [1] * (limit + 1)
    for n in range(2, limit + 1):
        p = spf[n]
        reduced = n
        exponent = 0
        while reduced % p == 0:
            reduced //= p
            exponent += 1
        g[n] = g[reduced] * (2 * exponent + 1 if p % 4 == 1 else 1)
    return g


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


def prefix(values: list[int]) -> list[int]:
    out = [0] * len(values)
    running = 0
    for i, value in enumerate(values):
        running += value
        out[i] = running
    return out


def enumerate_domain(limit: int, g: list[int]) -> tuple[list[int], list[int], list[int]]:
    points_exact = [0] * (limit + 1)
    raw_exact = [0] * (limit + 1)
    repeated_exact = [0] * (limit + 1)

    for h in range(1, 2 * limit + 1):
        max_s = math.isqrt((2 * limit) // h)
        for r in range(1, max_s + 1):
            for s in range(r + 1, max_s + 1):
                q = r * r + s * s
                d = h * q // 2
                if d > limit:
                    break
                if math.gcd(r, s) != 1 or h * q % 2:
                    continue
                p = h * r * s
                if p >= limit:
                    raise ArithmeticError("pointwise bound p=h*r*s<B failed")
                points_exact[d] += 1
                raw_exact[d] += g[p] - 1

                # Repeated side means c is a leg of a first triangle with hypotenuse p.
                c = h * (s * s - r * r) // 2
                if c < p:
                    other_sq = p * p - c * c
                    other = math.isqrt(other_sq)
                    if other * other == other_sq:
                        repeated_exact[d] += 1

    return prefix(points_exact), prefix(raw_exact), prefix(repeated_exact)


def prime_sieve(limit: int) -> list[int]:
    is_prime = bytearray(b"\x01") * (limit + 1)
    is_prime[:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if is_prime[p]:
            is_prime[p * p : limit + 1 : p] = b"\x00" * (((limit - p * p) // p) + 1)
    return [p for p in range(2, limit + 1) if is_prime[p]]


def singular_constant(prime_limit: int) -> dict[str, float | int]:
    # F(s)=prod_{q=1 mod4}[1+2/(q^s-1)+4q/((q+1)(q^s-1))].
    # Extract zeta(s)^3 L(s,chi_4)^3; L(1,chi_4)=pi/4.
    log_h = 3.0 * math.log(0.5)
    primes = prime_sieve(prime_limit)
    for p in primes:
        if p == 2:
            continue
        if p % 4 == 1:
            local_modulus = 1.0 + 2.0 / (p - 1.0) + 4.0 * p / (p * p - 1.0)
            normalized = local_modulus * (1.0 - 1.0 / p) ** 6
        else:
            normalized = (1.0 - 1.0 / (p * p)) ** 3
        log_h += math.log(normalized)
    kappa = (math.pi / 4.0) ** 3 * math.exp(log_h)
    return {
        "prime_cutoff": prime_limit,
        "kappa_partial_product": kappa,
        "formal_raw_leading_constant": kappa / (48.0 * math.pi),
        "formal_primitive_leading_constant": kappa / (12.0 * math.pi),
    }


def build_report() -> dict[str, Any]:
    spf = build_spf(MAX_B)
    g = build_g_table(MAX_B, spf)
    mu = mobius_sieve(MAX_B)
    points, raw, repeated = enumerate_domain(MAX_B, g)
    euler = singular_constant(EULER_PRODUCT_LIMIT)

    rows: list[dict[str, Any]] = []
    for bound in THRESHOLDS:
        primitive = sum(mu[k] * raw[bound // k] for k in range(1, bound + 1))
        log_b = math.log(bound)
        rows.append(
            {
                "B": bound,
                "second_triangle_parameter_points": points[bound],
                "raw_oriented_weight": raw[bound],
                "primitive_oriented_by_global_mobius": primitive,
                "repeated_side_parameter_points": repeated[bound],
                "unweighted_over_B_logB_over_pi": points[bound] / (bound * log_b / math.pi),
                "raw_over_B_logB_power4": raw[bound] / (bound * log_b**4),
                "primitive_over_B_logB_power3": primitive / (bound * log_b**3),
            }
        )

    if any(row["repeated_side_parameter_points"] != 0 for row in rows):
        raise ArithmeticError("finite repeated-side audit unexpectedly found a point")
    if rows[4]["raw_oriented_weight"] != 185_206:
        raise ArithmeticError("Stage12 raw regression at B=20000")
    if rows[4]["primitive_oriented_by_global_mobius"] != 49_592:
        raise ArithmeticError("Stage12 primitive regression at B=20000")

    return {
        "metadata": {
            "stage": "12-N1-2f",
            "title": "Formal main term, local densities, and repeated-side closure",
            "generated_by": "scripts/audit_main_term_stage12_n1_2f.py",
            "claim_status": "Exact local-density algebra and repeated-side nonexistence; formal leading term conditional on a uniform lattice remainder.",
        },
        "fixed_modulus_volume": {
            "moduli": "a|h, b|r, c|s, pairwise coprime, supported on primes 1 mod4",
            "rho": "rho(n)=product_{p|n} p/(p+1)",
            "odd_prime_density": "For p not dividing bc use 1-1/p^2; for p^e||b or p^e||c the divisibility-plus-coprimality density is p^(-e)(1-1/p), producing the relative factor p/(p+1).",
            "two_adic_density": {
                "both_r_s_odd": "Residue mass 1/4 and h-length factor 2, contribution 1/2.",
                "opposite_parity": "Residue mass 1/2 and even-h factor 1, contribution 1/2.",
                "combined": 1,
            },
            "archimedean_sector": "The sector 0<r<s has angular width pi/4; radial integration of 1/(r^2+s^2) contributes (pi/8) log B.",
            "formal_fixed_modulus_term": "V_{a,b,c}(B)=(B/(pi*a*b*c))*rho(b*c)*[log(B/(a*max(b,c)^2))]_+ plus a lower logarithmic term, for fixed a,b,c.",
            "unweighted_check": "At a=b=c=1 this gives (1/pi) B log B, matching the finite parameter-point normalization trend.",
        },
        "modulus_singularity": {
            "q_local_factor": "F_q(s)=1+2/(q^s-1)+4q/((q+1)(q^s-1)) for q=1 mod4",
            "interpretation": [
                "2/(q^s-1) assigns q-powers to the h-modulus a.",
                "Each of b and c contributes 2q/((q+1)(q^s-1)), including rho(q)=q/(q+1).",
            ],
            "factorization": "prod F_q(s)=zeta(s)^3 L(s,chi_4)^3 H(s), with H holomorphic and nonzero at s=1.",
            "pole_order": 3,
            "kappa_euler_product": "kappa=(pi/4)^3*(1-1/2)^3*product_{p=3 mod4}(1-p^-2)^3*product_{q=1 mod4}F_q(1)(1-q^-1)^6",
            "numerical_partial_product": euler,
        },
        "logarithmic_degree": {
            "log_simplex": "With x=log a, y=log b, z=log c and L=log B, integral_{x+2max(y,z)<L}(L-x-2max(y,z)) dx dy dz = L^4/48.",
            "formal_raw_main": "C_raw(B) ~ (kappa/(48*pi))*B*(log B)^4",
            "raw_degree": 4,
            "global_mobius_effect": "C_prim(B)=sum mu(k)C_raw(floor(B/k)) divides the Mellin/Dirichlet singularity by zeta(s), lowering the pole order from 5 to 4.",
            "formal_primitive_main": "C_prim(B) ~ (kappa/(12*pi))*B*(log B)^3",
            "primitive_degree": 3,
            "status": "The degrees and candidate constants are the formal main-term architecture. Proving the asymptotics still requires a uniform remainder and a justified Selberg-Delange/Tauberian passage.",
        },
        "repeated_side": {
            "possible_equalities": "The two first-triangle legs cannot be equal; only c=x or c=y could repeat.",
            "reduction": "If z is the repeated leg, then z^2+w^2=p^2 and z^2+p^2=d^2. In the triangle (z,p,d), p is the larger leg and is the hypotenuse of (z,w,p), while the smaller leg z repeats.",
            "nonexistence_input": "Zelator, A Non-Existence Property of Pythagorean Triangles with a 3-D Application, arXiv:0903.1280, Theorem 1; equivalently Fermat's right-triangle theorem forbidding square area.",
            "square_area_certificate": "Writing u=w/p, t=z/p, v=d/p gives (v+u)^2+(v-u)^2=4 and area ((v+u)(v-u))/2=t^2, a nonzero rational square, contradiction.",
            "conclusion": "Repeated-side contribution is exactly zero for every B; hence C_distinct_raw(B)=C_raw(B) identically.",
            "finite_checks_through": MAX_B,
            "finite_repeated_points": repeated[MAX_B],
        },
        "finite_diagnostics": rows,
        "decision": {
            "classification": "A_formal_main_term_and_repeated_side_closed_uniform_error_open",
            "confirmed": [
                "The fixed-modulus volume and all local-density factors are explicit.",
                "The modulus Euler product has a cubic singularity.",
                "The formal raw logarithmic degree is 4 and the post-Mobius primitive degree is 3.",
                "Repeated-side subtraction vanishes identically, not merely in the audited range.",
            ],
            "next_stage": "12-N1-2g: prove or refute the uniform fixed-modulus lattice remainder needed to upgrade the formal B(log B)^4 raw main term and B(log B)^3 primitive main term to asymptotics.",
        },
        "not_claimed": [
            "That the formal raw or primitive asymptotic has been proved.",
            "That the prime-cutoff numerical Euler product is a rigorous enclosure of kappa.",
            "That a currently cited large-sieve theorem supplies the required uniform remainder.",
            "That the primitive oriented asymptotic immediately isolates N1 from exact-two and exact-three multiplicities.",
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
