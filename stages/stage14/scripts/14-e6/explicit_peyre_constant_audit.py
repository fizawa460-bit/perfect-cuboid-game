#!/usr/bin/env python3

import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
E4_DATA = ROOT / "stages/stage14/data/14-e4/directional_tamagawa_audit.json"
OUT = ROOT / "stages/stage14/data/14-e6/explicit_peyre_constant_audit.json"
PRIME_CUTOFF = 1_000_000


def integral_monomial(coeff: Fraction, power: int, lo: Fraction, hi: Fraction) -> Fraction:
    return coeff * (hi ** (power + 1) - lo ** (power + 1)) / Fraction(power + 1)


def alpha_exact():
    # Dual effective-cone coordinates are (a,b,c1,c2,c3,c4), with ci>=0,
    # a>=c1+c2, a>=c3+c4, b>=c1+c3, b>=c2+c4 and
    # 2a+2b-(c1+c2+c3+c4)<=1.
    # After S,r,k,l Hadamard coordinates, the 4D c-sublevel volume reduces to
    # two elementary regions.  The exact pieces below are the direct
    # antiderivatives of 1/2*(1-2R-K)^2.
    lo = Fraction(0)
    one_third = Fraction(1, 3)
    one_half = Fraction(1, 2)

    # Region 0<=R<=1/3, 0<=K<=R gives inner polynomial
    # 19 R^3/6 - 5 R^2/2 + R/2.
    v1 = (
        integral_monomial(Fraction(19, 6), 3, lo, one_third)
        + integral_monomial(Fraction(-5, 2), 2, lo, one_third)
        + integral_monomial(Fraction(1, 2), 1, lo, one_third)
    )

    # Region 1/3<=R<=1/2, 0<=K<=1-2R gives (1-2R)^3/6.
    # Expand: 1/6 - R + 2R^2 - 4R^3/3.
    v2 = (
        integral_monomial(Fraction(1, 6), 0, one_third, one_half)
        + integral_monomial(Fraction(-1), 1, one_third, one_half)
        + integral_monomial(Fraction(2), 2, one_third, one_half)
        + integral_monomial(Fraction(-4, 3), 3, one_third, one_half)
    )

    assert v1 == Fraction(13, 1944)
    assert v2 == Fraction(1, 3888)
    c_sublevel_volume = v1 + v2
    assert c_sublevel_volume == Fraction(1, 144)

    # Integrating the two nonnegative slack variables A,B contributes 1/120.
    six_dimensional_volume = c_sublevel_volume / 120
    assert six_dimensional_volume == Fraction(1, 17280)

    picard_rank = 6
    alpha = picard_rank * six_dimensional_volume
    assert alpha == Fraction(1, 2880)
    return v1, v2, c_sublevel_volume, six_dimensional_volume, alpha


def sieve_primes(n: int):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    lim = int(n ** 0.5)
    for p in range(2, lim + 1):
        if sieve[p]:
            start = p * p
            sieve[start:n + 1:p] = b"\x00" * (((n - start) // p) + 1)
    return [p for p in range(2, n + 1) if sieve[p]]


def odd_local_factor(p: int) -> float:
    x = 1.0 / p
    return (1.0 - x) ** 6 * (1.0 + 6.0 * x + x * x)


def fmt(x: float) -> str:
    return f"{x:.15g}"


def main():
    e4 = json.loads(E4_DATA.read_text())
    masses = e4["chamber_masses"]

    v1, v2, cvol, vol6, alpha = alpha_exact()

    # Exact p=2 calculation for the physical projective metric.
    # For v2(q)=0, h=max(1,|t(q)|_2)=1.  For n!=0,
    # h=2^(|n|+1).  Each valuation shell has |dq/q|-measure 1/2.
    # Hence the two-variable unscaled integral is
    # 1/4 + sum_{k>=2} 2(k-1)/2^k = 9/4.
    two_adic_unscaled_integral = Fraction(9, 4)
    frame_scale_at_2 = Fraction(4, 1)  # |4|_2^{-1}
    two_adic_metric_integral = two_adic_unscaled_integral * frame_scale_at_2
    assert two_adic_metric_integral == 9
    two_adic_convergence = Fraction(1, 2) ** 6
    tau_2 = two_adic_metric_integral * two_adic_convergence
    assert tau_2 == Fraction(9, 64)

    primes = sieve_primes(PRIME_CUTOFF)
    log_prod = 0.0
    odd_prime_count = 0
    for p in primes:
        if p == 2:
            continue
        fp = odd_local_factor(p)
        assert 0.0 < fp < 1.0
        log_prod += math.log(fp)
        odd_prime_count += 1
    odd_product_upper = math.exp(log_prod)

    # For x=1/p<=1/3,
    # log((1-x)^6(1+6x+x^2)) + 20x^2 >= 0.
    # Thus -log f_p <=20/p^2, and
    # sum_{p>N} 1/p^2 <= sum_{n>N}1/n^2 <1/N.
    tail_log_bound = 20.0 / PRIME_CUTOFF
    odd_product_lower = odd_product_upper * math.exp(-tail_log_bound)

    beta = Fraction(1, 1)
    arch_scale = Fraction(1, 4)  # s0=4*omega^{-1}
    rational_prefactor = alpha * beta * arch_scale * tau_2
    assert rational_prefactor == Fraction(1, 81920)

    pref = float(rational_prefactor)
    lambda_lower = pref * odd_product_lower
    lambda_upper = pref * odd_product_upper

    constants = {}
    for key in ("a", "b", "c", "total"):
        m = float(masses[key])
        constants[key] = {
            "lower": fmt(lambda_lower * m),
            "upper": fmt(lambda_upper * m),
        }

    report = {
        "metadata": {
            "stage": "14-e6",
            "track": "explicit Peyre/Tamagawa constant for physical ambient height",
            "toric_model": "Bl_4(P1xP1)",
            "picard_rank": 6,
            "prime_product_cutoff": PRIME_CUTOFF,
        },
        "effective_cone": {
            "c_sublevel_region_piece_1": str(v1),
            "c_sublevel_region_piece_2": str(v2),
            "c_sublevel_volume": str(cvol),
            "six_dimensional_slice_volume_leq_1": str(vol6),
            "alpha": str(alpha),
        },
        "cohomological_factor": {
            "beta": str(beta),
            "split_picard_action": True,
            "brauer_correction_nontrivial": False,
        },
        "archimedean_normalization": {
            "e4_mass_density": "dq1*dq2/(q1*q2*sqrt(1+t1^2+t2^2))",
            "invariant_frame_relation": "s0=4*omega^{-1}",
            "exact_scale_relative_to_e4_Mq": str(arch_scale),
        },
        "finite_local_factors": {
            "odd_prime_formula": "(1-1/p)^6*(1+6/p+1/p^2)",
            "odd_prime_polynomial": "1-20/p^2+64/p^3-90/p^4+64/p^5-20/p^6+1/p^8",
            "p2_unscaled_integral": str(two_adic_unscaled_integral),
            "p2_frame_scaled_integral": str(two_adic_metric_integral),
            "p2_tamagawa_factor": str(tau_2),
            "odd_primes_in_truncation": odd_prime_count,
        },
        "euler_product": {
            "exact_formula": "Lambda_E=(1/81920)*PROD_{p>=3}(1-1/p)^6*(1+6/p+1/p^2)",
            "rational_prefactor": str(rational_prefactor),
            "odd_product_lower": fmt(odd_product_lower),
            "odd_product_upper": fmt(odd_product_upper),
            "tail_log_bound": fmt(tail_log_bound),
            "lambda_E_lower": fmt(lambda_lower),
            "lambda_E_upper": fmt(lambda_upper),
        },
        "leading_constants": constants,
        "thin_set_transfer": {
            "third_face_square_removed": True,
            "leading_constant_unchanged": True,
            "input": "Stage14-e4 thin type-II zero-density theorem",
        },
        "status": {
            "STAGE14_E6": "COMPLETE_EXPLICIT_PEYRE_TAMAGAWA_CONSTANT",
            "ALPHA_Y": "1/2880",
            "BETA_Y": "1",
            "PHYSICAL_P2_FACTOR": "9/64",
            "GLOBAL_ARITHMETIC_CONSTANT_LAMBDA_E_EVALUATED": True,
            "SECONDARY_ASYMPTOTIC_PROVED": False,
            "NEXT_E_SUPPLEMENT": "Stage14-e7 secondary asymptotics / finite crossover",
        },
        "pass": True,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report["euler_product"], indent=2, sort_keys=True))
    print("Stage14-e6 explicit Peyre/Tamagawa audit: PASS")


if __name__ == "__main__":
    main()
