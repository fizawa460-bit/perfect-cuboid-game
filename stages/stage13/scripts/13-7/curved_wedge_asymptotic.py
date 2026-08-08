#!/usr/bin/env python3
"""Stage13-7i: j=1 zero-mode curved-wedge asymptotic and constant audit.

This validator turns the Stage13-7h fixed-channel rectangle factorization into
an explicit curved-region leading constant for the unique positive-singularity
channel: zero angular mode, normalization j=1.

The theorem-level input is the 7h uniform three-variable rectangle lemma and
the same finite-order Selberg--Delange theorem already locked in Stage12.
This script audits the local Euler factors, the parity/radial ledger, the
archimedean wedge integral, and a finite coordinate sum.  It does not by itself
close the infinite nonzero-harmonic family; that is handled by the companion
harmonic_uniformity_budget.py.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

OUT = Path("stages/stage13/data/13-7/curved_wedge_asymptotic_report.json")


def primes_upto(n: int) -> list[int]:
    sieve = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        sieve[0] = 0
    if n >= 1:
        sieve[1] = 0
    for p in range(2, math.isqrt(n) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return [p for p in range(2, n + 1) if sieve[p]]


def split_scale_local_at_one(q: int) -> float:
    """A_q(1)=1+sum_{a>=1} 2/(2a+1) q^{-a}, q=1 mod 4."""
    x = 1.0 / q
    y = math.sqrt(x)
    return 2.0 * math.atanh(y) / y - 1.0


def split_mixed_sum_at_one(q: int, tol: float = 1e-20) -> float:
    """sum_{a,b>=1} 2/(2(a+b)+1) q^{-(a+b)}."""
    x = 1.0 / q
    n = 2
    xn = x * x
    acc = 0.0
    while True:
        term = (n - 1) * 2.0 * xn / (2 * n + 1)
        acc += term
        if abs(term) < tol:
            return acc
        n += 1
        xn *= x


def split_cross_local_at_one(q: int) -> float:
    """C_q(1,1,1) after factoring A_q and two zeta base factors."""
    x = 1.0 / q
    A = split_scale_local_at_one(q)
    X = x / (1.0 - x)
    mixed = split_mixed_sum_at_one(q)
    D = A + 2.0 * X + 2.0 * mixed
    return D * (1.0 - x) ** 2 / A


def euler_constants(prime_cutoff: int) -> dict[str, float]:
    # A(s)=(zeta(s)L(s,chi4))^(1/3) E_h(s), where A is the odd split-prime
    # scale series.  p=2 and inert primes are therefore residual factors.
    log_E_scale = (1.0 / 3.0) * math.log(1.0 - 0.5)
    log_C_odd = 0.0
    for p in primes_upto(prime_cutoff):
        if p == 2:
            continue
        if p % 4 == 1:
            A = split_scale_local_at_one(p)
            log_E_scale += math.log(A) + (2.0 / 3.0) * math.log1p(-1.0 / p)
            log_C_odd += math.log(split_cross_local_at_one(p))
        else:
            log_E_scale += (1.0 / 3.0) * math.log1p(-1.0 / (p * p))
            log_C_odd += math.log1p(-1.0 / (p * p))

    E_scale = math.exp(log_E_scale)
    C_odd = math.exp(log_C_odd)
    gamma_13 = math.gamma(1.0 / 3.0)
    scale_sd_constant = E_scale * (math.pi / 4.0) ** (1.0 / 3.0) / gamma_13
    return {
        "E_scale_at_1_truncated": E_scale,
        "C_odd_at_111_truncated": C_odd,
        "scale_summatory_constant_truncated": scale_sd_constant,
    }


def t_of_phi(phi: float) -> float:
    r, s = math.cos(phi), math.sin(phi)
    return (s * s - r * r) / (2.0 * r * s)


def k0_of_t(t: float) -> float:
    invsqrt2 = 1.0 / math.sqrt(2.0)
    if t < invsqrt2:
        return 8.0 * math.asin(t) / math.pi - 1.0
    if t < 1.0:
        return 4.0 * math.acos(t) / math.pi
    return 0.0


def simpson(f, a: float, b: float, n: int = 200000) -> float:
    if n % 2:
        n += 1
    h = (b - a) / n
    acc = f(a) + f(b)
    for i in range(1, n):
        acc += (4.0 if i % 2 else 2.0) * f(a + i * h)
    return acc * h / 3.0


def spf_sieve(n: int) -> list[int]:
    spf = list(range(n + 1))
    if n >= 1:
        spf[1] = 1
    for p in range(2, math.isqrt(n) + 1):
        if spf[p] == p:
            for m in range(p * p, n + 1, p):
                if spf[m] == m:
                    spf[m] = p
    return spf


def factor(n: int, spf: list[int]) -> dict[int, int]:
    out: dict[int, int] = {}
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        out[p] = e
    return out


def G_from_factorization(f: dict[int, int]) -> int:
    g = 1
    for p, e in f.items():
        if p % 4 == 1:
            g *= 2 * e + 1
    return g


def scale_kernel_j1(k: int, rs_factors: dict[int, int], spf: list[int]) -> float:
    """Multiplicative U_G/G coefficient for k>1."""
    kf = factor(k, spf)
    coeff = 1.0
    for p, a in kf.items():
        if p % 4 != 1:
            return 0.0
        b = rs_factors.get(p, 0)
        coeff *= 2.0 / (2 * (a + b) + 1)
    return coeff


def finite_j1_zero_sum(B: int, spf: list[int]) -> dict[str, float]:
    """Exact Stage13-7g coordinate sum for the j=1 zero channel."""
    max_rs = math.isqrt(2 * B) + 2
    lam_end = 1.0 + math.sqrt(2.0)
    oe_k1 = oe_bulk = ee_k1 = ee_bulk = 0.0

    for r in range(1, max_rs):
        if r * r >= 2 * B:
            break
        smax = math.isqrt(2 * B - r * r)
        for s in range(r + 1, smax + 1):
            if math.gcd(r, s) != 1:
                continue
            if s / r >= lam_end:
                break
            t = (s * s - r * r) / (2.0 * r * s)
            wedge = k0_of_t(t)
            q = r * r + s * s
            rs_f = factor(r * s, spf)
            G = G_from_factorization(rs_f)
            boundary_coeff = 1.0 - 1.0 / G

            if (r & 1) and (s & 1):
                kmax = (2 * B) // q
                if kmax >= 1:
                    oe_k1 += wedge * boundary_coeff
                for k in range(2, kmax + 1):
                    oe_bulk += wedge * scale_kernel_j1(k, rs_f, spf)

            if (r + s) & 1:
                kmax = B // q
                if kmax >= 1:
                    ee_k1 += wedge * boundary_coeff
                for k in range(2, kmax + 1):
                    ee_bulk += wedge * scale_kernel_j1(k, rs_f, spf)

    return {
        "OE_minimal_scale": oe_k1,
        "OE_k_gt_1": oe_bulk,
        "EE_minimal_scale": ee_k1,
        "EE_k_gt_1": ee_bulk,
        "total": oe_k1 + oe_bulk + ee_k1 + ee_bulk,
    }


def build_report() -> dict:
    phi_a = math.pi / 4.0
    phi_b = 3.0 * math.pi / 8.0
    angular_integral = simpson(lambda phi: k0_of_t(t_of_phi(phi)), phi_a, phi_b)

    product_cutoffs = [1000, 10000, 100000, 1000000]
    products = []
    for cutoff in product_cutoffs:
        row = {"prime_cutoff": cutoff}
        row.update(euler_constants(cutoff))
        products.append(row)

    final = products[-1]
    # OE: odd-odd base density 1/4 and radius^2 cutoff 2B/k -> area B/k.
    # EE: opposite-parity density 1/2 and radius^2 cutoff B/k -> area B/(2k).
    # The two contributions are 1/4 and 1/4, hence total parity/radial factor 1/2.
    parity_radial_factor = 0.5
    predicted_constant = (
        3.0
        * final["scale_summatory_constant_truncated"]
        * final["C_odd_at_111_truncated"]
        * parity_radial_factor
        * angular_integral
    )

    finite_B = [100000, 1000000]
    spf = spf_sieve(max(finite_B) + 2)
    finite_rows = []
    for B in finite_B:
        row = finite_j1_zero_sum(B, spf)
        leading = predicted_constant * B * math.log(B) ** (1.0 / 3.0)
        row.update({
            "B": B,
            "leading_model_using_1e6_prime_product": leading,
            "finite_total_over_leading_model": row["total"] / leading,
        })
        finite_rows.append(row)

    return {
        "metadata": {
            "stage": "13-7i",
            "scope": "j=1 zero-mode curved wedge asymptotic and positive leading constant",
        },
        "exact_j1_zero_factorization": {
            "scale_series": (
                "A(s)=prod_{q=1 mod4}[1+sum_{a>=1}2/(2a+1)q^(-as)] "
                "=(zeta(s)L(s,chi4))^(1/3) E_h(s)"
            ),
            "scale_residual_at_1": (
                "E_h(1)=(1-1/2)^(1/3) prod_{p=3 mod4}(1-p^-2)^(1/3) "
                "prod_{q=1 mod4} A_q(1)(1-q^-1)^(2/3)"
            ),
            "scale_summatory": (
                "sum_{k<=X} a(k) ~ c_h X(log X)^(-2/3), "
                "c_h=E_h(1)(pi/4)^(1/3)/Gamma(1/3); hence "
                "sum_{k<=X}a(k)/k ~ 3 c_h (log X)^(1/3)"
            ),
            "odd_cross_correction": (
                "C_odd(1,1,1)=prod_{p=3 mod4}(1-p^-2) "
                "prod_{q=1 mod4} C_q, with C_q=(1-q^-1)^2 D_q/A_q and "
                "D_q=A_q+2/(q-1)+2*sum_{a,b>=1}2/(2(a+b)+1)q^(-(a+b))."
            ),
        },
        "parity_radial_ledger": {
            "OE": "r,s odd gives 2-adic base density 1/4; k(r^2+s^2)<=2B gives radial area B/k; product factor 1/4",
            "EE": "r,s opposite parity gives density 1/2; k(r^2+s^2)<=B gives radial area B/(2k); product factor 1/4",
            "combined_factor": parity_radial_factor,
        },
        "archimedean_wedge": {
            "support": "phi in (pi/4,3pi/8), t=-cot(2phi)",
            "integral": "I0=int k0(t(phi)) dphi",
            "numeric_value": angular_integral,
            "positive": angular_integral > 0.0,
        },
        "euler_product_diagnostics": products,
        "leading_constant": {
            "exact_form": "K0=(3/2)*c_h*C_odd(1,1,1)*I0",
            "numeric_truncation_at_prime_1e6": predicted_constant,
            "theorem": "Delta_zero,j=1(B) ~ K0 * B * (log B)^(1/3)",
            "sign": "positive",
        },
        "finite_coordinate_audit": finite_rows,
        "boundary": {
            "minimal_scale": "k=1 is a separate two-variable channel of size O(B)=o(B(log B)^(1/3))",
            "core_wings": "Stage13-7h gives O(B(log B)^(1/4)) for removed small-height/coordinate regions",
        },
        "status": {
            "j1_zero_curved_wedge_asymptotic": True,
            "j1_zero_leading_constant_positive": True,
            "full_nonzero_harmonic_family_closed_here": False,
            "companion": "harmonic_uniformity_budget.py",
        },
    }


def main() -> None:
    report = build_report()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
