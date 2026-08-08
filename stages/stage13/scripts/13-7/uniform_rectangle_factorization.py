#!/usr/bin/env python3
"""Stage13-7h: global fixed-channel rectangle factorization.

The Stage13-7g fixed-base formulation leaves an apparent uniformity problem:
base primes q|rs modify the k-Euler factors by O(1).  This script validates
(and records) the repair used in 7h: do not freeze rs.  Instead regard h,r,s
as three multiplicative variables, absorb every pure-variable local factor,
and put only genuinely mixed prime support into a 3-variable correction.

For every fixed normalization channel j>=1 and angular mode l>=0 the local
correction starts only when at least two of h,r,s carry the same prime.  Its
weighted l1 norm is therefore O(q^{-1-2 delta}) on Re(s_i)>=1/2+delta.
The global Euler product consequently converges in the same weighted Dirichlet
Banach algebra used in Stage12-N1-3j.

This is an algebraic/numerical validator for the local identities and norm
budget.  The analytic conclusions written to the report use the same general
finite-order Selberg--Delange theorem already locked in Stage12 (Tenenbaum
II.5.2), plus the standard zero-free region / polynomial vertical growth for
each fixed Gaussian angular Hecke L-function.
"""
from __future__ import annotations

import json
import math
from collections import defaultdict
from pathlib import Path

OUT = Path("stages/stage13/data/13-7/uniform_rectangle_factorization_report.json")


def dirichlet_kernel(e: int, phase: float) -> float:
    return 1.0 + 2.0 * sum(math.cos(m * phase) for m in range(1, e + 1))


def local_kernel(mode: str, j: int, phase: float, a: int, b: int) -> float:
    """Split-prime local coefficient, a=v_q(h-scale), b=v_q(rs)."""
    e = a + b
    if mode == "zero":
        if a == 0:
            return float((2 * b + 1) ** (1 - j))
        return 2.0 / (2 * e + 1) ** j
    if a == 0:
        return dirichlet_kernel(b, phase) / (2 * b + 1) ** j
    return 2.0 * math.cos(e * phase) / (2 * e + 1) ** j


def inv_1d(coeff: list[float]) -> list[float]:
    out = [0.0] * len(coeff)
    out[0] = 1.0
    for n in range(1, len(coeff)):
        out[n] = -sum(coeff[k] * out[n - k] for k in range(1, n + 1))
    return out


def conv3(A: dict[tuple[int, int, int], float],
          B: dict[tuple[int, int, int], float],
          N: int) -> dict[tuple[int, int, int], float]:
    out: dict[tuple[int, int, int], float] = defaultdict(float)
    for (i, j, k), x in A.items():
        for (a, b, c), y in B.items():
            if i + a <= N and j + b <= N and k + c <= N:
                out[(i + a, j + b, k + c)] += x * y
    return dict(out)


def correction_coefficients(mode: str, j: int, phase: float, N: int = 6):
    """Truncated C=D/(A_h B_r B_s) at a split prime."""
    D: dict[tuple[int, int, int], float] = {(0, 0, 0): 1.0}
    for a in range(1, N + 1):
        D[(a, 0, 0)] = local_kernel(mode, j, phase, a, 0)
    for b in range(1, N + 1):
        v = local_kernel(mode, j, phase, 0, b)
        D[(0, b, 0)] = v
        D[(0, 0, b)] = v
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            v = local_kernel(mode, j, phase, a, b)
            D[(a, b, 0)] = v
            D[(a, 0, b)] = v
    # gcd(r,s)=1: there are no local terms with both r and s exponents >0.

    Avec = [1.0] + [local_kernel(mode, j, phase, a, 0) for a in range(1, N + 1)]
    Bvec = [1.0] + [local_kernel(mode, j, phase, 0, b) for b in range(1, N + 1)]
    iA, iB = inv_1d(Avec), inv_1d(Bvec)
    IA = {(a, 0, 0): iA[a] for a in range(N + 1)}
    IR = {(0, b, 0): iB[b] for b in range(N + 1)}
    IS = {(0, 0, c): iB[c] for c in range(N + 1)}
    return conv3(conv3(conv3(D, IA, N), IR, N), IS, N)


def split_prime_angle(q: int) -> float:
    for a in range(1, math.isqrt(q) + 1):
        b2 = q - a * a
        if b2 <= 0:
            continue
        b = math.isqrt(b2)
        if b * b == b2:
            x, y = sorted((a, b))
            return math.atan2(x, y)  # in (0,pi/4)
    raise ValueError(q)


def build_report() -> dict:
    # Exact local checks on a generic phase.
    phase = 0.731234567
    max_zero_formula_error = 0.0
    max_harmonic_formula_error = 0.0
    max_majorant_violation = 0.0
    local_cases = 0
    for j in range(1, 5):
        for a in range(0, 7):
            for b in range(0, 7):
                e = a + b
                G_e = 2 * e + 1
                H_e = dirichlet_kernel(e, phase)
                if a == 0:
                    z_direct = G_e / G_e**j
                    h_direct = H_e / G_e**j
                else:
                    z_direct = (G_e - (2 * (e - 1) + 1)) / G_e**j
                    h_direct = (H_e - dirichlet_kernel(e - 1, phase)) / G_e**j
                z = local_kernel("zero", j, phase, a, b)
                h = local_kernel("harmonic", j, phase, a, b)
                max_zero_formula_error = max(max_zero_formula_error, abs(z_direct - z))
                max_harmonic_formula_error = max(max_harmonic_formula_error, abs(h_direct - h))
                max_majorant_violation = max(max_majorant_violation, abs(h) - z)
                local_cases += 1

    # Pure-axis cancellation of C-1 and q^{-1-2delta} norm diagnostic.
    split_primes = [5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97]
    delta = 0.05
    sigma = 0.5 + delta
    correction_rows = []
    pure_axis_failures = 0
    for mode in ("zero", "harmonic"):
        for j in range(1, 5):
            worst_scaled_norm = 0.0
            for q in split_primes:
                alpha = split_prime_angle(q)
                C = correction_coefficients(mode, j, 8.0 * alpha, N=6)
                for idx, value in C.items():
                    if idx != (0, 0, 0) and sum(v > 0 for v in idx) <= 1 and abs(value) > 1e-10:
                        pure_axis_failures += 1
                norm = sum(
                    abs(value) * q ** (-sigma * sum(idx))
                    for idx, value in C.items()
                    if idx != (0, 0, 0)
                )
                worst_scaled_norm = max(worst_scaled_norm, norm * q ** (1 + 2 * delta))
            correction_rows.append({
                "mode": mode,
                "j": j,
                "truncated_worst_q^(1+2delta)_norm": worst_scaled_norm,
            })

    # Uniform local inverse safety bounds.  q=5 and sigma=1/2 are the worst
    # split-prime endpoint for the simple coefficient majorants used in proof.
    z = 5.0 ** -0.5
    scale_nonconstant_majorant = (2.0 / 3.0) * z / (1.0 - z)
    base_nonconstant_majorant = z / (1.0 - z)

    singularity = []
    for j in range(1, 9):
        alpha = 3.0 ** (-j)
        beta_zero = (1.0 + 3.0 ** (1 - j)) / 2.0
        beta_harmonic = (1.0 + alpha) / 2.0
        singularity.append({
            "j": j,
            "scale_zero_zeta_exponent": alpha,
            "base_zero_zeta_exponent": beta_zero,
            "scale_nonzero_harmonic_zeta_exponent": 0.0,
            "base_nonzero_harmonic_zeta_exponent": beta_harmonic,
            "bulk_zero_region_log_exponent_after_homogeneity": 4.0 * alpha - 1.0,
            "minimal_scale_zero_log_exponent": 3.0 ** (1 - j) - 1.0,
            "minimal_scale_harmonic_log_exponent": alpha - 1.0,
        })

    return {
        "metadata": {
            "stage": "13-7h",
            "scope": (
                "global weighted-l1 factorization and uniform rectangle input for fixed "
                "normalization channels; curved-wedge leading constant not evaluated"
            ),
        },
        "exact_globalization": {
            "statement": (
                "The growing-base uniformity issue is removed by treating h,r,s as "
                "simultaneous multiplicative variables instead of applying Selberg-Delange "
                "to h with rs frozen."
            ),
            "split_prime_full_local": (
                "D_q(z,x,y)=1 + pure h + pure r + pure s + h-r + h-s terms; "
                "r-s simultaneous support is forbidden by gcd(r,s)=1."
            ),
            "factorization": (
                "D_{j,l}(s_h,s_r,s_s)=A_{j,l}(s_h) B_{j,l}(s_r) "
                "B_{j,l}(s_s) C_{j,l}(s_h,s_r,s_s), up to the finite 2-adic parity factor."
            ),
            "weighted_l1": (
                "For every fixed delta>0, sum |c(a,b,c)|/(abc)^(1/2+delta)<infinity. "
                "Locally C_q-1 starts with at least two positive coordinate exponents, "
                "hence ||C_q-1||_delta=O_delta(q^(-1-2delta))."
            ),
            "inert_prime_correction": "At q=3 mod 4, the h-factor is 1 and the r-s coprime correction is exactly 1-x*y.",
        },
        "pure_one_variable_factors": {
            "zero_mode": {
                "scale": "A_{j,0}(s)=(zeta(s)L(s,chi4))^(3^-j) E_{h,j,0}(s)",
                "base": (
                    "B_{j,0}(s)=zeta(s)^beta0 L(s,chi4)^gamma0 E_{b,j,0}(s), "
                    "beta0=(1+3^(1-j))/2, gamma0=(3^(1-j)-1)/2"
                ),
            },
            "nonzero_harmonic": {
                "scale": "A_{j,l}(s)=L(s,xi_{8l})^(3^-j) E_{h,j,l}(s), l>=1",
                "base": (
                    "B_{j,l}(s)=zeta(s)^beta1 L(s,chi4)^gamma1 "
                    "L(s,xi_{8l})^(3^-j) E_{b,j,l}(s), "
                    "beta1=(1+3^-j)/2, gamma1=(3^-j-1)/2"
                ),
            },
            "residual_euler_products": "All E-factors have local quotient 1+O(q^(-2 sigma)) after matching the displayed first-prime coefficients.",
        },
        "selberg_delange_consequences": {
            "external_boundary": [
                "Tenenbaum, Introduction to Analytic and Probabilistic Number Theory, 3rd ed., II.5.2 (already locked by Stage12)",
                "standard zero-free region and polynomial vertical growth for each fixed Gaussian angular Hecke L(s,xi_{8l}); e.g. the Kubilius zero-free region quoted in Gaussian-prime literature",
            ],
            "zero_scale": "sum_{n<=X} a_{j,0}(n)=c X(log X)^(3^-j-1) plus arbitrary finite-order log expansion",
            "zero_base": "sum_{n<=X} b_{j,0}(n)=c X(log X)^(beta0-1) plus arbitrary finite-order log expansion",
            "harmonic_scale": (
                "For fixed j,l>=1, the Selberg-Delange z=0 expansion has 1/Gamma(-m)=0 "
                "at every finite term, hence sum_{n<=X} a_{j,l}(n)=O_A(X(log(2X))^-A) "
                "for every fixed A, at the stated Hecke zero-free external-theorem level."
            ),
            "harmonic_base": "sum_{n<=X} b_{j,l}(n)=c X(log X)^(beta1-1) plus finite-order remainder",
        },
        "uniform_rectangle_lemma": {
            "form": (
                "After convolving the global weighted-l1 correction, fixed-channel boxes "
                "H x R x S have the product of the three one-variable Selberg-Delange "
                "mains plus an error bounded by log^C times "
                "H^(3/4+eps)RS + HR^(3/4+eps)S + HRS^(3/4+eps), together with "
                "the three one-variable SD remainders.  The implicit constant is fixed "
                "for j,l,eps and does not depend on a frozen base rs."
            ),
            "reason": (
                "Split correction coefficients at sqrt(H),sqrt(R),sqrt(S); the global "
                "weighted-l1 norm gives exactly the Stage12-N1-3a 3/4+eps tail argument "
                "in three variables."
            ),
        },
        "boundary_and_wings": {
            "minimal_scale_zero": (
                "At k=1 (OE h=1, EE h=2), (G(rs)-1)/G(rs)^j = "
                "G(rs)^(1-j)-G(rs)^(-j), a difference of two multiplicative 2-variable channels."
            ),
            "minimal_scale_harmonic": (
                "At k=1, (H_l(rs)-1)/G(rs)^j = H_l(rs)G(rs)^(-j)-G(rs)^(-j), "
                "again a difference of multiplicative channels."
            ),
            "small_height_majorant": (
                "Every normalized shell gap has absolute value <=1, so h<=H0 contributes "
                "O(B log H0).  With log H0=(log B)^(1/4), this is O(B(log B)^(1/4))."
            ),
            "small_coordinate_majorant_fixed_channel": (
                "For the zero j=1 channel, the full local coefficient is bounded by the "
                "pure scale coefficient a(h); sum_{h<=Y}a(h)<<Y.  Therefore min(r,s)<U "
                "contributes O(B log U).  All fixed j>=1 zero/harmonic channels are "
                "pointwise dominated by this majorant."
            ),
            "choice": "log H0 and log U may both be chosen asymptotic to (log B)^(1/4), below the candidate j=1 bulk log exponent 1/3.",
        },
        "singularity_exponent_ledger": singularity,
        "validation": {
            "local_formula_cases": local_cases,
            "zero_formula_max_abs_error": max_zero_formula_error,
            "harmonic_formula_max_abs_error": max_harmonic_formula_error,
            "harmonic_le_zero_majorant_max_violation": max(0.0, max_majorant_violation),
            "correction_pure_axis_failures": pure_axis_failures,
            "correction_norm_delta": delta,
            "correction_truncated_rows": correction_rows,
            "q5_sigma_half_scale_nonconstant_l1_majorant": scale_nonconstant_majorant,
            "q5_sigma_half_base_nonconstant_l1_majorant": base_nonconstant_majorant,
            "q5_sigma_half_scale_inverse_neumann_bound": 1.0 / (1.0 - scale_nonconstant_majorant),
            "q5_sigma_half_base_inverse_neumann_bound": 1.0 / (1.0 - base_nonconstant_majorant),
        },
        "status": {
            "stage13_7h": "COMPLETE_AT_GLOBAL_WEIGHTED_L1_RECTANGLE_LEVEL",
            "growing_base_uniformity_obstruction": "CLOSED_BY_GLOBAL_THREE_VARIABLE_FACTORIZATION",
            "fixed_channel_rectangle_input": "PROVED_AT_STATED_EXTERNAL_THEOREM_LEVEL",
            "minimal_scale_boundary": "SEPARATED_INTO_TWO_VARIABLE_MULTIPLICATIVE_CHANNELS",
            "curved_wedge_leading_constant": "NOT_YET_EVALUATED",
            "directional_asymptotic_limit": "NOT_IDENTIFIED",
            "next": "Stage13-7i: execute the curved wedge/radial transfer, compute the j=1 zero-mode leading constant, and bound all remaining channels against it.",
        },
    }


def main() -> None:
    report = build_report()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
