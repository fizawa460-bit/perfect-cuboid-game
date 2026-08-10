#!/usr/bin/env python3
"""Stage14-t57: rank-one Kummer ratio/product and Mellin adapter audit."""

from __future__ import annotations

import cmath
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
T56_RESULT = ROOT / "stages/stage14/14-t56/result.md"
TOOLBOX_AS = ROOT / "stages/stage14/14-toolbox-as/result.md"
OUT = ROOT / "stages/stage14/data/14-t57/rank1_kummer_mellin.json"

SPLIT_PRIMES = (5, 13, 17, 29, 37)
TOL = 1e-8


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def factor_distinct(n: int) -> list[int]:
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def primitive_root(p: int) -> int:
    n = p - 1
    qs = factor_distinct(n)
    for g in range(2, p):
        if all(pow(g, n // q, p) != 1 for q in qs):
            return g
    raise AssertionError("primitive root not found")


def logs_mod_p(p: int) -> tuple[int, dict[int, int]]:
    g = primitive_root(p)
    logs: dict[int, int] = {}
    z = 1
    for e in range(p - 1):
        logs[z] = e
        z = z * g % p
    assert len(logs) == p - 1
    return g, logs


def A(z: int, p: int) -> int:
    return legendre(z * z - 1, p)


def K(t: int, x: int, p: int) -> int:
    return legendre((x * x - t * t) * (1 - t * t * x * x), p)


def ratio_product_value(t: int, x: int, p: int) -> int:
    inv_t = pow(t, p - 2, p)
    return A(x * inv_t % p, p) * A(t * x % p, p)


def mellin_coefficients(p: int) -> tuple[list[complex], dict[int, int]]:
    n = p - 1
    _, logs = logs_mod_p(p)
    coeffs: list[complex] = []
    for j in range(n):
        total = 0j
        for z, e in logs.items():
            total += A(z, p) * cmath.exp(-2j * math.pi * j * e / n)
        coeffs.append(total)
    return coeffs, logs


def reconstruct_A(z: int, p: int, coeffs: list[complex], logs: dict[int, int]) -> complex:
    n = p - 1
    e = logs[z]
    return sum(
        coeffs[j] * cmath.exp(2j * math.pi * j * e / n)
        for j in range(n)
    ) / n


def audit_prime(p: int) -> dict:
    assert p % 4 == 1
    n = p - 1

    # Exact affine ratio/product identity.
    rp_checks = 0
    cayley_checks = 0
    for t in range(1, p):
        for x in range(1, p):
            assert K(t, x, p) == ratio_product_value(t, x, p)
            rp_checks += 1

            d1 = (1 + t * x) % p
            d2 = (1 - t * x) % p
            if d1 and d2:
                r = (x - t) * pow(d1, p - 2, p) % p
                s = (x + t) * pow(d2, p - 2, p) % p
                lhs = (x * x - t * t) * pow((1 - t * t * x * x) % p, p - 2, p) % p
                assert lhs == r * s % p
                # Original quartic / (r*s) is the square denominator^2 when nonzero.
                if r and s:
                    quartic = (x * x - t * t) * (1 - t * t * x * x) % p
                    ratio = quartic * pow((r * s) % p, p - 2, p) % p
                    sq = (1 - t * t * x * x) ** 2 % p
                    assert ratio == sq
                cayley_checks += 1

    coeffs, logs = mellin_coefficients(p)

    # Evenness kills characters with eta(-1)=-1, i.e. odd exponent j.
    odd_mode_max = max(abs(coeffs[j]) for j in range(1, n, 2)) if n > 1 else 0.0
    assert odd_mode_max < TOL

    # Fourier inversion on every nonzero field element.
    reconstruction_error = 0.0
    for z in range(1, p):
        rec = reconstruct_A(z, p, coeffs, logs)
        reconstruction_error = max(reconstruction_error, abs(rec - A(z, p)))
    assert reconstruction_error < TOL

    # Exact Parseval target, verified numerically to roundoff.
    spectral_sq = sum(abs(c) ** 2 for c in coeffs)
    parseval_target = n * (p - 3)  # A vanishes exactly at z=+-1.
    assert abs(spectral_sq - parseval_target) < 1e-6

    normalized_one_energy = spectral_sq / (n * n)
    normalized_two_energy = normalized_one_energy * normalized_one_energy
    expected_one = (p - 3) / (p - 1)
    expected_two = expected_one * expected_one
    assert abs(normalized_one_energy - expected_one) < 1e-8
    assert abs(normalized_two_energy - expected_two) < 1e-8
    assert normalized_two_energy <= 1 + TOL

    # Safe rank-one Kummer Weil scale; finite audit only, theorem statement is in result.md.
    max_coeff = max(abs(c) for c in coeffs)
    assert max_coeff <= 2 * math.sqrt(p) + 1e-7

    # Spot-check the exact two-coordinate Mellin formula through reconstructed A factors.
    mellin_kernel_checks = 0
    for t in range(1, p):
        inv_t = pow(t, p - 2, p)
        et = logs[t]
        for x in range(1, p):
            u = x * inv_t % p
            v = t * x % p
            Au = reconstruct_A(u, p, coeffs, logs)
            Av = reconstruct_A(v, p, coeffs, logs)
            assert abs(Au * Av - K(t, x, p)) < 1e-7
            mellin_kernel_checks += 1

    return {
        "p": p,
        "ratio_product_checks": rp_checks,
        "cayley_checks": cayley_checks,
        "mellin_kernel_checks": mellin_kernel_checks,
        "odd_mode_max_abs": odd_mode_max,
        "reconstruction_max_error": reconstruction_error,
        "max_mellin_coeff_abs": max_coeff,
        "two_sqrt_p": 2 * math.sqrt(p),
        "normalized_one_coordinate_energy": normalized_one_energy,
        "normalized_two_coordinate_energy": normalized_two_energy,
    }


def main() -> None:
    t56 = T56_RESULT.read_text()
    toolbox_as = TOOLBOX_AS.read_text()
    assert "STAGE14_T56=COMPLETE_CENTERED_SELECTOR_TO_INVISIBLE_SUBD_BRIDGE_AND_ADAPTER_BOUNDARY" in t56
    assert "SHARED_U_CENTERED_PROJECTIVE_SELECTOR_DISPERSION_PROVED=false" in t56
    assert "FIXED_U_CLOSEST_SOURCE=PING_XI_ARBITRARY_SET_TRACE_BILINEAR" in toolbox_as
    assert "FIXED_U_ONE_FIELD_TRACE_SHEAF_CERTIFICATE_PROVED=false" in toolbox_as
    assert "FIXED_U_PHYSICAL_SELECTOR_SUPPORT_ENERGY_TRANSFER_PROVED=false" in toolbox_as
    assert "FIXED_U_TWO_PRIME_REASSEMBLY_WITH_ZERO_FIXED_LOSS_PROVED=false" in toolbox_as

    rows = [audit_prime(p) for p in SPLIT_PRIMES]

    # Kernel-side CRT spectral energies tensor exactly and remain <=1.
    crt_pairs = []
    for i, r1 in enumerate(rows):
        for r2 in rows[i + 1:]:
            e = r1["normalized_two_coordinate_energy"] * r2["normalized_two_coordinate_energy"]
            assert e <= 1 + TOL
            crt_pairs.append({"p": r1["p"], "q": r2["p"], "tensor_energy": e})

    report = {
        "stage": "14-t57",
        "split_primes": list(SPLIT_PRIMES),
        "prime_rows": rows,
        "crt_pair_count": len(crt_pairs),
        "max_crt_tensor_energy": max(x["tensor_energy"] for x in crt_pairs),
        "ratio_product_identity": "K_p(t,x)=A_p(x/t)A_p(tx), A_p(z)=chi_p(z^2-1)",
        "mellin_identity": "K=(p-1)^-2 sum_eta,xi Ahat(eta)Ahat(xi)(xi eta^-1)(t)(eta xi)(x)",
        "mellin_packet_l2_bound": "((p-3)/(p-1))^2<=1",
        "decision": {
            "STAGE14_T57": "COMPLETE_RANK1_KUMMER_MELLIN_ADAPTER_AND_PHYSICAL_SELECTOR_CORRELATION_BOUNDARY",
            "FIXED_U_ONE_FIELD_RANK1_KUMMER_CERTIFICATE_PROVED": True,
            "FIXED_U_ALL_ORDER_MELLIN_PACKET_PROVED": True,
            "FIXED_U_MELLIN_PACKET_L2_ENERGY_LE_ONE": True,
            "PING_XI_DIRECT_IMPORT_VALID": False,
            "FKMS_2026_DIRECT_IMPORT_VALID": False,
            "TWO_PRIME_KERNEL_SPECTRAL_REASSEMBLY_FIXED_POWER_LOSS": 0,
            "FIXED_U_PHYSICAL_SELECTOR_SUPPORT_ENERGY_TRANSFER_PROVED": False,
            "SHARED_U_PHYSICAL_TOROIDAL_MELLIN_CORRELATION_PROVED": False,
            "SHARED_U_CENTERED_PROJECTIVE_SELECTOR_DISPERSION_PROVED": False,
            "SHARED_U_MIXED_BRANCH_DISPERSION_PROVED": False,
            "SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_PROVED": False,
            "TH16_NEEDED": False,
            "NEXT": "Stage14-t58 attack SharedUPhysicalToroidalMellinCorrelation; test separated/toroidal decomposition of the physical reconstruction masks",
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
