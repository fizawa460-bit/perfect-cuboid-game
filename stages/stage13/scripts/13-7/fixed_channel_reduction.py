#!/usr/bin/env python3
"""Stage13-7g: exact Stage12-coordinate and fixed-channel reduction.

This is an algebraic validator/report generator, not the final coupled-region
asymptotic theorem.  It records the exact OE/EE change of variables from the
outer Pythagorean parameters to the frozen Stage12 (h,r,s) coordinates and
checks the prime-local kernels obtained after expanding

    1/(G(p)-1) = sum_{j>=1} G(p)^(-j).

For a split prime q=1 mod 4 write
    a = v_q(k), b = v_q(rs), e=a+b,
where k=gcd(p,z) is the odd outer scale.  The transformed zero and angular
numerators then have the local formulas checked below.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

OUT = Path("stages/stage13/data/13-7/fixed_channel_reduction_report.json")


def D(e: int, x: float) -> float:
    return 1.0 + 2.0 * sum(math.cos(m * x) for m in range(1, e + 1))


def zero_local(a: int, b: int, j: int) -> float:
    e = a + b
    if a == 0:
        return float((2 * b + 1) ** (1 - j))
    return 2.0 / (2 * e + 1) ** j


def harmonic_local(a: int, b: int, j: int, x: float) -> float:
    e = a + b
    if a == 0:
        return D(b, x) / (2 * b + 1) ** j
    return 2.0 * math.cos(e * x) / (2 * e + 1) ** j


def build_report() -> dict:
    phase = 0.731234567
    max_zero_error = 0.0
    max_harmonic_error = 0.0
    cases = 0

    for j in range(1, 5):
        for a in range(0, 6):
            for b in range(0, 6):
                e = a + b
                G_e = 2 * e + 1
                H_e = D(e, phase)
                if a == 0:
                    direct_zero = G_e / G_e**j
                    direct_harmonic = H_e / G_e**j
                else:
                    direct_zero = (G_e - (2 * (e - 1) + 1)) / G_e**j
                    direct_harmonic = (H_e - D(e - 1, phase)) / G_e**j
                max_zero_error = max(max_zero_error, abs(direct_zero - zero_local(a, b, j)))
                max_harmonic_error = max(
                    max_harmonic_error,
                    abs(direct_harmonic - harmonic_local(a, b, j, phase)),
                )
                cases += 1

    lambda0 = (math.sqrt(6.0) + math.sqrt(2.0)) / 2.0
    lambda1 = 1.0 + math.sqrt(2.0)

    return {
        "metadata": {
            "stage": "13-7g",
            "scope": (
                "exact Stage12-coordinate bridge and fixed-channel singularity "
                "classification; no coupled (r,s) directional asymptotic theorem"
            ),
        },
        "stage12_coordinate_bridge": {
            "OE": {
                "from_outer_base": "r=u-v, s=u+v, h=k",
                "parity": "r,s odd; h=k odd",
                "gcd_p_z": "k=h",
            },
            "EE": {
                "from_outer_base": "r=v, s=u, h=2k",
                "parity": "r,s opposite parity; v2(h)=1",
                "gcd_p_z": "k=h/2",
            },
            "unified_identities": [
                "p=h*r*s",
                "z=h*(s^2-r^2)/2",
                "d=h*(r^2+s^2)/2",
                "d<=B iff h*(r^2+s^2)<=2B",
                "t=z/p=(s^2-r^2)/(2*r*s)",
            ],
            "directional_wedge": {
                "lambda0_t_equals_1_over_sqrt2": lambda0,
                "lambda1_t_equals_1": lambda1,
                "statement": (
                    "The ac-bc ordering kernel vanishes for s/r>=1+sqrt(2); "
                    "its formula changes at (sqrt(6)+sqrt(2))/2."
                ),
            },
        },
        "effective_scale_support": (
            "For a nonzero primitive transformed numerator, k is odd and every "
            "prime divisor of k is 1 mod 4. A factor 2 or q=3 mod 4 in gcd(p,z) "
            "kills the transformed numerator."
        ),
        "fixed_channel_local_kernel": {
            "notation": (
                "At q=1 mod 4 let a=v_q(k), b=v_q(rs), e=a+b. "
                "Since gcd(r,s)=1, b belongs to at most one of r,s."
            ),
            "zero_mode": {
                "a=0": "(2b+1)^(1-j)",
                "a>=1": "2/(2(a+b)+1)^j",
            },
            "harmonic_l": {
                "a=0": "D_b(8 l alpha_q)/(2b+1)^j",
                "a>=1": "2 cos(8 l (a+b) alpha_q)/(2(a+b)+1)^j",
            },
            "minimal_scale_subtraction": (
                "T_F=U_F-1 when k=1. This is h=1 in OE and h=2 in EE, "
                "so it is a separate two-variable boundary channel and cannot "
                "be silently discarded."
            ),
        },
        "free_scale_singularity": {
            "zero_generic_local": "1+sum_{a>=1} 2/(2a+1)^j q^(-as)",
            "zero_factorization": (
                "Z_0,j(s)=(zeta(s)L(s,chi_4))^(1/3^j) E_0,j(s), "
                "up to finitely many base-prime factors; E has local quotient "
                "1+O(q^(-2 sigma))."
            ),
            "zero_fixed_base_consequence": (
                "At the same external Selberg-Delange theorem level as Stage12, "
                "each fixed (r,s) zero-mode k-sum has exponent 1/3^j and scale "
                "Y(log Y)^(1/3^j-1), with a base-dependent constant."
            ),
            "harmonic_generic_local": (
                "1+sum_{a>=1} 2 cos(8 l a alpha_q)/(2a+1)^j q^(-as)"
            ),
            "harmonic_factorization": (
                "For fixed l>=1, Z_l,j(s)=L(s,xi_{8l})^(1/3^j) E_l,j(s) "
                "near s=1, again up to finitely many base-prime factors."
            ),
            "harmonic_consequence": (
                "The free scale k contributes no zeta pole to a nonzero angular "
                "harmonic. Uniform summatory cancellation while (r,s) grow is "
                "not proved here."
            ),
        },
        "normalization_tail": [
            {"J": J, "relative_shellwise_bound": 3.0 ** (-J)} for J in range(1, 9)
        ],
        "validation": {
            "local_cases": cases,
            "zero_max_abs_error": max_zero_error,
            "harmonic_max_abs_error": max_harmonic_error,
            "test_phase": phase,
        },
        "unresolved": (
            "The remaining analytic problem is uniformity in growing (r,s), "
            "including the minimal-scale boundary channel, followed by the "
            "weighted wedge/rectangle/wing transfer under h(r^2+s^2)<=2B."
        ),
    }


def main() -> None:
    report = build_report()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
