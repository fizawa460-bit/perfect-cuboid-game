#!/usr/bin/env python3
"""Stage14-tH16: audit same-modulus/reciprocity/hyperbolic routes for t58."""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import cmath
import json
import math
import runpy

ROOT = Path(__file__).resolve().parents[4]
T36_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py"
T42_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t42_kummer_transversality_audit.py"
T57_RESULT = ROOT / "stages/stage14/14-t57/result.md"
T58_RESULT = ROOT / "stages/stage14/14-t58/result.md"
TH14_R2 = ROOT / "stages/stage14/14-tH14/r2.md"
SUMMARY = ROOT / "stages/stage14/data/tH16/canonical_prime_delta_toroidal_audit_summary.json"


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    v = pow(a, (p - 1) // 2, p)
    return -1 if v == p - 1 else v


def squarefree_kernel(n: int) -> int:
    if n == 0:
        return 0
    sign = -1 if n < 0 else 1
    n = abs(n)
    out = 1
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e ^= 1
        if e:
            out *= p
        p += 1 if p == 2 else 2
    if n > 1:
        out *= n
    return sign * out


def is_squarefree_positive(n: int) -> bool:
    if n <= 0:
        return False
    p = 2
    while p * p <= n:
        if n % (p * p) == 0:
            return False
        p += 1
    return True


def primitive_root(p: int) -> int:
    phi = p - 1
    factors = []
    n = phi
    q = 2
    while q * q <= n:
        if n % q == 0:
            factors.append(q)
            while n % q == 0:
                n //= q
        q += 1
    if n > 1:
        factors.append(n)
    for g in range(2, p):
        if all(pow(g, phi // q, p) != 1 for q in factors):
            return g
    raise AssertionError("primitive root not found")


def log_table(p: int, g: int) -> dict[int, int]:
    out = {}
    x = 1
    for j in range(p - 1):
        out[x] = j
        x = (x * g) % p
    return out


def char_value(k: int, z: int, p: int, logs: dict[int, int]) -> complex:
    if z % p == 0:
        return 0j
    angle = 2.0 * math.pi * k * logs[z % p] / (p - 1)
    return cmath.exp(1j * angle)


def kernel_from_projective(A: int, B: int, P: int, Q: int, r: int) -> tuple[int, int]:
    # t=A/B, x=P/Q. Denominators are squares in the quadratic symbol.
    delta = (B * B * P * P - A * A * Q * Q) * (B * B * Q * Q - A * A * P * P)
    return legendre(delta, r), delta


def main() -> None:
    t57 = T57_RESULT.read_text()
    t58 = T58_RESULT.read_text()
    th14 = TH14_R2.read_text()
    summary = json.loads(SUMMARY.read_text())

    assert "FIXED_U_MELLIN_PACKET_L2_ENERGY_LE_ONE=true" in t57
    assert "SHARED_U_PHYSICAL_TOROIDAL_MELLIN_CORRELATION_PROVED=false" in t57
    assert "SHARED_U_CANONICAL_PRIME_DELTA_TOROIDAL_SECOND_MOMENT_PROVED=false" in t58
    assert "FIXED_U_PHYSICAL_SELECTOR_SUPPORT_ENERGY_TRANSFER_PROVED=true" in t58
    assert "DUAL_QUADRATIC_LARGE_SIEVE_PRODUCT_ROW_ADAPTER_PROVED=true" in th14
    assert "PHYSICAL_WEIGHTED_SQUARECLASS_FIBER_ENERGY_PROVED=false" in th14

    # Physical delta is genuinely not a squarefree variable, so the direct
    # odd-squarefree Jacobi hyperbola theorem cannot be invoked verbatim.
    t36 = runpy.run_path(str(T36_SCRIPT), run_name="stage14_t36_import")
    t42 = runpy.run_path(str(T42_SCRIPT), run_name="stage14_t42_import")
    reps = t42["reciprocal_quotient"](t36["build_frozen_states"]())
    invisible = [s for s in reps if s["branch"] == "invisible"]
    nonsquarefree_delta = [s for s in invisible if not is_squarefree_positive(s["delta"])]
    assert nonsquarefree_delta, "expected physical invisible states with non-squarefree delta"

    # Exact toroidal/projective quadratic-symbol identity and squareclass
    # projection on several split auxiliary primes.
    samples = [
        (1, 2, 2, 3),
        (2, 3, 3, 5),
        (1, 3, 4, 5),
        (3, 4, 5, 7),
    ]
    split_primes = [p for p in range(13, 100) if is_prime(p) and p % 4 == 1]
    reciprocity_checks = 0
    for A, B, P, Q in samples:
        for r in split_primes:
            if (B * Q) % r == 0:
                continue
            kval, delta = kernel_from_projective(A, B, P, Q, r)
            if delta % r == 0:
                continue
            sf = squarefree_kernel(delta)
            assert kval == legendre(sf, r)
            reciprocity_checks += 1
    assert reciprocity_checks > 20

    # Equal-squareclass rows are literally indistinguishable to every good
    # quadratic auxiliary prime: this is the coefficient-energy obstruction.
    coherent_primes = [p for p in range(13, 200) if is_prime(p) and p % 4 == 1 and p not in (3, 5)]
    for p in coherent_primes:
        assert legendre(5, p) == legendre(45, p)
    r_mult = 7
    Pcount = len(coherent_primes)
    lhs_coherent = Pcount * (Pcount - 1) * r_mult * r_mult
    target_coherent = Pcount * Pcount * r_mult
    assert lhs_coherent > target_coherent

    # Full same-modulus character-pair orthogonality. This is the exact
    # identity behind the naive Mellin Cauchy loss.
    p = 13
    g = primitive_root(p)
    logs = log_table(p, g)
    states = [
        (2, 3, 1.0),
        (2, 3, -2.0),
        (4, 5, 3.0),
        (7, 8, 2.0),
    ]
    spectral_sum = 0.0
    for a in range(p - 1):
        for b in range(p - 1):
            S = 0j
            for t, x, w in states:
                S += w * char_value(a, t, p, logs) * char_value(b, x, p, logs)
            spectral_sum += abs(S) ** 2
    fibers = defaultdict(float)
    for t, x, w in states:
        fibers[(t % p, x % p)] += w
    rhs = (p - 1) ** 2 * sum(v * v for v in fibers.values())
    assert abs(spectral_sum - rhs) < 1e-7 * max(1.0, rhs)

    # Critical exponent ledger. If K=B^d in the reciprocity frame and
    # L=B^rho, product-row conductor cost is absorbed only for 2 rho >= d.
    d = Fraction(4, 1)
    rho_bad = Fraction(3, 2)
    rho_good = Fraction(2, 1)
    assert 2 * rho_bad < d
    assert 2 * rho_good >= d
    mellin_two_prime_overhead = 4 * Fraction(1, 4)
    assert mellin_two_prime_overhead == 1

    decision = summary["proof_boundary"]
    expected = {
        "QUADRATIC_RECIPROCITY_PROJECTION_PROVED": True,
        "TH14_R2_PRODUCT_ROW_QUADRATIC_LARGE_SIEVE_IMPORT_VALID": True,
        "QUADRATIC_LARGE_SIEVE_CLOSES_T58_TARGET": False,
        "QUADRATIC_LARGE_SIEVE_FAILURE_IS_SQUARECLASS_COEFFICIENT_ENERGY": True,
        "FULL_MODE_ORTHOGONALITY_IDENTITY_PROVED": True,
        "NAIVE_SAME_MODULUS_MELLIN_CAUCHY_CLOSES_TARGET": False,
        "GAUSSIAN_ADDITIVE_SPARSE_MODULI_LARGE_SIEVE_DIRECT_IMPORT_VALID": False,
        "DIRECT_GAUSSIAN_RECIPROCITY_SEPARATION_PROVED": False,
        "DIRECT_FI_GAUSSIAN_SYMBOL_IMPORT_VALID": False,
        "HYPERBOLIC_REGION_GEOMETRY_COMPATIBLE": True,
        "HYPERBOLIC_JACOBI_KERNEL_IDENTITY_PROVED": False,
        "DELTA_SQUAREFREE_ON_PHYSICAL_PACKET": False,
        "WILSON_HYPERBOLIC_BILINEAR_DIRECT_IMPORT_VALID": False,
        "SAME_MODULUS_TOROIDAL_KUMMER_LARGE_SIEVE_PROVED": False,
        "TOROIDAL_HYPERBOLIC_JACOBI_BRIDGE_PROVED": False,
        "PAIR_COLLAPSE_BEFORE_PHYSICAL_CANCELLATION_ALLOWED": False,
        "E4_COEFFICIENT_ENERGY_USED": False,
        "SHARED_U_CANONICAL_PRIME_DELTA_TOROIDAL_SECOND_MOMENT_PROVED": False,
    }
    for key, value in expected.items():
        assert decision[key] == value, (key, decision[key], value)

    report = {
        "reciprocity_checks": reciprocity_checks,
        "split_auxiliary_primes_checked": len(split_primes),
        "physical_invisible_states": len(invisible),
        "physical_non_squarefree_delta_states": len(nonsquarefree_delta),
        "first_non_squarefree_deltas": sorted({s["delta"] for s in nonsquarefree_delta})[:10],
        "coherence_countermodel": {
            "multiplicity": r_mult,
            "auxiliary_primes": Pcount,
            "lhs": lhs_coherent,
            "near_linear_target": target_coherent,
        },
        "same_modulus_orthogonality": {
            "prime": p,
            "spectral_sum": spectral_sum,
            "collision_rhs": rhs,
        },
        "critical_ledger": {
            "quadratic_frame_d": str(d),
            "rho_bad": str(rho_bad),
            "rho_good": str(rho_good),
            "naive_mellin_overhead_at_rho_1_4": str(mellin_two_prime_overhead),
        },
        "status": summary["status"],
        "minimal_remaining_obstruction": summary["minimal_remaining_obstruction"],
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
