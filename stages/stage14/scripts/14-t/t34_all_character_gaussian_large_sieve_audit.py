#!/usr/bin/env python3
"""Stage14-t34: all-character Gaussian large-sieve / tensor-barrier audit."""

from __future__ import annotations

import cmath
from collections import Counter
from math import gcd, sqrt
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
T33_DATA = ROOT / "stages/stage14/data/14-t33/hecke_mellin_transfer_boundary.json"
OUT = ROOT / "stages/stage14/data/14-t34/all_character_gaussian_large_sieve.json"

SPLIT_PRIMES = (13, 17, 29, 37, 41)
MODEL_RATIO_SQUARE = 4
TOL = 1e-7


def legendre(x: int, p: int) -> int:
    x %= p
    if x == 0:
        return 0
    return 1 if pow(x, (p - 1) // 2, p) == 1 else -1


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
    factors = factor_distinct(n)
    for g in range(2, p):
        if all(pow(g, n // q, p) != 1 for q in factors):
            return g
    raise AssertionError(("no primitive root", p))


def character_value(j: int, exponent: int, n: int) -> complex:
    return cmath.exp(2j * cmath.pi * j * exponent / n)


def torus_trace_value(s: int, p: int) -> int:
    return legendre(pow(s, 4, p) - MODEL_RATIO_SQUARE, p)


def gauss_energy_audit(p: int) -> dict:
    """Verify the exact multiplicative-to-additive energy identity over F_p."""
    g = primitive_root(p)
    n = p - 1
    logs = {}
    x = 1
    for e in range(n):
        logs[x] = e
        x = x * g % p

    # Deterministic real coefficients on F_p^*.
    coeff = {r: ((r * r + 3 * r + 1) % 7) - 3 for r in range(1, p)}

    mult_energy = 0.0
    unit_trivial_energy = 0.0
    for j in range(1, n):
        total = 0j
        for r in range(1, p):
            total += coeff[r] * character_value(j, logs[r], n)
        e = abs(total) ** 2
        mult_energy += e
        if j % 4 == 0:
            unit_trivial_energy += e

    additive_energy = 0.0
    additive_sum = 0j
    for b in range(1, p):
        s = sum(
            coeff[r] * cmath.exp(2j * cmath.pi * b * r / p)
            for r in range(1, p)
        )
        additive_energy += abs(s) ** 2
        additive_sum += s

    gauss_rhs = ((p - 1) * additive_energy - abs(additive_sum) ** 2) / p
    assert abs(mult_energy - gauss_rhs) <= 1e-6 * max(1.0, mult_energy)
    assert unit_trivial_energy <= mult_energy + TOL

    return {
        "nontrivial_multiplicative_energy": round(mult_energy, 6),
        "gauss_additive_rhs": round(gauss_rhs, 6),
        "mu4_trivial_subfamily_energy": round(unit_trivial_energy, 6),
    }


def quotient_orthogonality_audit(p: int) -> int:
    """Check character orthogonality on F_p^*/mu_4 for every residue pair."""
    g = primitive_root(p)
    n = p - 1
    logs = {}
    x = 1
    for e in range(n):
        logs[x] = e
        x = x * g % p

    chars = list(range(0, n, 4))
    h = (p - 1) // 4
    assert len(chars) == h
    mu4 = {x for x in range(1, p) if pow(x, 4, p) == 1}
    assert len(mu4) == 4

    checks = 0
    for r in range(1, p):
        for s in range(1, p):
            exponent_difference = (logs[r] - logs[s]) % n
            total = sum(
                character_value(j, exponent_difference, n)
                for j in chars
            )
            ratio = r * pow(s, -1, p) % p
            expected = h if ratio in mu4 else 0
            assert abs(total - expected) <= 1e-6
            checks += 1
    return checks


def mellin_packet_audit(p: int) -> dict:
    g = primitive_root(p)
    n = p - 1
    values = [torus_trace_value(pow(g, e, p), p) for e in range(n)]

    coeffs = []
    for j in range(n):
        ahat = sum(
            values[e] * cmath.exp(-2j * cmath.pi * j * e / n)
            for e in range(n)
        )
        coeffs.append(ahat / n)

    energy = sum(abs(c) ** 2 for c in coeffs)
    expected_energy = sum(abs(v) ** 2 for v in values) / n
    assert abs(energy - expected_energy) <= 1e-6
    assert energy <= 1.0 + TOL

    support = [j for j, c in enumerate(coeffs) if abs(c) > TOL]
    assert all(j % 4 == 0 for j in support)

    max_coeff = max(abs(c) for c in coeffs)
    assert max_coeff <= 4 / sqrt(p) + TOL

    packet: dict[tuple[int, int], complex] = {}
    for j, cj in enumerate(coeffs):
        if abs(cj) <= TOL:
            continue
        for k, ck in enumerate(coeffs):
            if abs(ck) <= TOL:
                continue
            key = ((j + k) % n, (k - j) % n)
            packet[key] = packet.get(key, 0j) + cj * ck

    packet_energy = sum(abs(c) ** 2 for c in packet.values())
    assert packet_energy <= 2.0 + TOL
    axis_energy = sum(abs(c) ** 2 for (xi, _), c in packet.items() if xi == 0)
    # Conservative consequence of |c_psi|<=4/sqrt(p), Parseval<=1,
    # and multiplicity at most two in the (psi,phi)->(xi,zeta) map.
    assert axis_energy <= 32 / p + TOL

    return {
        "mellin_energy": round(energy, 6),
        "packet_energy": round(packet_energy, 6),
        "packet_axis_energy": round(axis_energy, 6),
        "packet_constant_energy": round(abs(packet.get((0, 0), 0j)) ** 2, 6),
        "max_normalized_mellin_coeff": round(max_coeff, 6),
        "bound_4_over_sqrt_lambda": round(4 / sqrt(p), 6),
        "mu4_trivial_character_count": (p - 1) // 4,
    }


def tensor_barrier_audit() -> dict:
    samples = ((4, 16), (16, 64), (64, 256), (100, 400))
    rows = []
    for M, N in samples:
        best_value = None
        best_L = None
        for L in range(2, 101):
            value = (M + L * L) * (N + L * L) / L
            if best_value is None or value < best_value:
                best_value = value
                best_L = L
        lower = 2 * N * sqrt(M)
        assert best_value is not None and best_L is not None
        assert best_value + TOL >= lower
        rows.append(
            {
                "M": M,
                "N": N,
                "best_integer_L_2_to_100": best_L,
                "best_tensor_detector_bound": round(best_value, 6),
                "ambient_hyperbola_proxy_N": N,
                "ratio_to_ambient": round(best_value / N, 6),
                "algebraic_lower_envelope_2NsqrtM": round(lower, 6),
            }
        )
    return {
        "identity": "(M+L^2)(N+L^2)/L >= 2*N*sqrt(M) for M<=N",
        "samples": rows,
    }


def main() -> None:
    frozen33 = json.loads(T33_DATA.read_text())
    assert frozen33["decision"]["STAGE14_T33"] == (
        "COMPLETE_QUADRATIC_HECKE_VALUE_TRANSFER_AND_MELLIN_SPECTRAL_BOUNDARY"
    )
    assert frozen33["decision"]["HIGHER_ORDER_MELLIN_MODES_REQUIRED"] is True
    assert frozen33["decision"]["ALL_CHARACTER_MELLIN_HECKE_SIEVE_OBJECT_DEFINED"] is True

    prime_audits = {}
    orthogonality_checks = 0
    for p in SPLIT_PRIMES:
        row = gauss_energy_audit(p)
        row.update(mellin_packet_audit(p))
        checks = quotient_orthogonality_audit(p)
        orthogonality_checks += checks
        row["mu4_quotient_orthogonality_checks"] = checks
        prime_audits[str(p)] = row

    assert orthogonality_checks == 4080
    expected_mult = {"13": 515.0, "17": 911.0, "29": 3136.0, "37": 5075.0, "41": 6199.0}
    assert {p: d["nontrivial_multiplicative_energy"] for p, d in prime_audits.items()} == expected_mult
    expected_sub = {"13": 158.0, "17": 67.0, "29": 364.0, "37": 602.0, "41": 1229.0}
    assert {p: d["mu4_trivial_subfamily_energy"] for p, d in prime_audits.items()} == expected_sub

    tensor = tensor_barrier_audit()

    totals = Counter()
    totals["split_primes_gauss_transform_audited"] = len(SPLIT_PRIMES)
    totals["exact_gauss_energy_identities"] = len(SPLIT_PRIMES)
    totals["mu4_quotient_orthogonality_checks"] = orthogonality_checks
    totals["mellin_packet_energy_checks"] = len(SPLIT_PRIMES)
    totals["tensor_barrier_samples"] = len(tensor["samples"])

    report = {
        "stage": "14-t34",
        "t33_frozen_reference": {
            "higher_order_modes_required": True,
            "quadratic_only_directly_sufficient": False,
            "unified_cofactor_checks": frozen33["t32_frozen_reference"]["unified_cofactor_checks"],
        },
        "all_character_gaussian_large_sieve": {
            "gauss_transform": "M_psi=tau(barpsi)^-1*sum_c^* barpsi(c) S_varpi(c)",
            "exact_energy_identity": "sum_{psi!=1}|M_psi|^2=q^-1*((q-1)sum_c^*|S(c)|^2-|sum_c^*S(c)|^2)",
            "huxley_transfer": "sum_{N(varpi)<=L} sum_{psi|mu4=1,psi!=1}|sum a_z psi(z)|^2 << (Z+L^2) sum|a_z|^2",
            "character_order_uniform": True,
            "mu4_subfamily_index": 4,
        },
        "mellin_packet": {
            "normalized_one_factor_energy": "<=1",
            "two_factor_aggregated_energy": "<=2",
            "sample_individual_bound": "|c_lambda(psi)|<=4/sqrt(lambda)",
            "axis_energy_conservative_bound": "<=32/lambda in sampled model",
        },
        "tensor_barrier": {
            "independent_modulus_bound": "(M+L^2)(N+L^2)*coefficient_energy",
            "square_detector_bound": "(M+L^2)(N+L^2)/L^(1-o(1))",
            "lower_envelope": "2*N*sqrt(M)",
            "physical_scales": "M~X/ell, N~B/ell, true norm-hyperbola mass=N*B^o(1)",
            "closes_norm_hyperbola": False,
            "finite_samples": tensor,
        },
        "same_modulus_collision": {
            "one_variable": "sum_psi psi(U)barpsi(U')=h_lambda iff U/U' is a Gaussian unit modulo varpi, else 0",
            "two_variable": "same varpi must divide U-uU' and V-vV' for some u,v in mu4",
            "lost_by_independent_tensorization": True,
            "next_target": "dispersion bound for shared-prime collisions on divisor-coupled norm hyperbola",
        },
        "finite_audit": {
            "prime_audits": prime_audits,
            "totals": dict(totals),
        },
        "decision": {
            "STAGE14_T34": "COMPLETE_ALL_CHARACTER_GAUSSIAN_LARGE_SIEVE_AND_TENSOR_BARRIER",
            "ALL_CHARACTER_GAUSS_TRANSFORM_EXACT": True,
            "ALL_CHARACTER_GAUSSIAN_MULTIPLICATIVE_LARGE_SIEVE": True,
            "MU4_SUBFAMILY_FIXED_INDEX": True,
            "MELLIN_PACKET_L2_ENERGY_BOUNDED": True,
            "HIGHER_ORDER_MELLIN_MODES_LARGE_SIEVE_OBSTRUCTION": False,
            "NAIVE_TWO_VARIABLE_TENSORIZATION_BOUND": "(M+L^2)(N+L^2)",
            "TENSOR_SQUARE_DETECTOR_LOWER_ENVELOPE": "2N*sqrt(M)",
            "TENSOR_LARGE_SIEVE_CLOSES_NORM_HYPERBOLA": False,
            "SAME_MODULUS_SHARED_PRIME_COLLISION_IDENTITY": True,
            "NORM_INDEX_HYPERBOLIC_CORRELATION_POWER_SAVING_PROVED": False,
            "VISIBLE_BRANCH_POWER_SAVING_PROVED": False,
            "INVISIBLE_BRANCH_POWER_SAVING_PROVED": False,
            "JOINT_COVER_CONDITIONED_SMOOTH_POWER_SAVING_PROVED": False,
            "A_11_POWER_SAVING_PROVED": False,
            "T_O_SQRT_B_PROVED": False,
            "PERFECT_CUBOID_NONEXISTENCE_PROVED": False,
            "NEXT": (
                "Stage14-t35 prove a same-modulus dispersion/large-sieve bound from the shared-prime collision "
                "conditions varpi|(U-uU') and varpi|(V-vV'), retaining k|epsilon*N(U) and "
                "N(U)*delta<<B/ell"
            ),
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report["finite_audit"], indent=2, sort_keys=True))
    print(json.dumps(report["decision"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
