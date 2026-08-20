#!/usr/bin/env python3
import cmath
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
S27 = ROOT / "stages" / "stage27"


def read(path):
    return path.read_text(encoding="utf-8")


def req(text, token):
    assert token in text, f"missing marker: {token}"


# Lifecycle parent: audited and merged #1247 is the only accepted predecessor.
parent_audit = read(S27 / "27-20-r302p-u" / "audit.md")
for token in (
    "AUDIT_VERDICT=PASS_WITH_LIFECYCLE_VERIFIER_REPAIR",
    "AUDITED_PR=1247",
    "REPAIR_REQUIRED=false",
    "NEXT_DERIVED_ROUTE_AFTER_MERGE=27-20-r302v",
):
    req(parent_audit, token)

# Route-chain / firewall markers.
checks = {
    "27-20-r302v": (
        "GRAM_DIAGONAL_FLAT_ON_ADMISSIBLE_CLASS=true",
        "NEXT_DERIVED_ROUTE=27-20-r302w",
    ),
    "27-20-r302w": (
        "ADMISSIBLE_CLASS_DIAGONAL_PRODUCT_IDENTITY_PROVED=true",
        "NEXT_DERIVED_ROUTE=27-20-r302x",
    ),
    "27-20-r302x": (
        "SQUARED_FREQUENCY_PHASE_DIFFERENCE_EXPOSED=true",
        "NEXT_DERIVED_ROUTE=27-20-r302y",
    ),
    "27-20-r302y": (
        "ODD_SQUARED_FREQUENCY_COLLISION_SPLIT_PROVED=true",
        "NEXT_DERIVED_ROUTE=27-20-r302z",
    ),
    "27-20-r302z": (
        "ODD_PRIME_POWER_COLLISION_COUNT_PROVED=true",
        "CRT_COLLISION_DEGREE_BOUND_PROVED=true",
        "NEXT_DERIVED_ROUTE=27-20-r302aa",
    ),
    "27-20-r302aa": (
        "UNIT_COLLISION_PAID_BY_DIAGONAL_UP_TO_SUBPOWER=true",
        "NEXT_DERIVED_ROUTE=27-20-r302ab",
    ),
    "27-20-r302ab": (
        "FOURIER_PROGRESSION_ENERGY_IDENTITY_PROVED=true",
        "PRIMITIVE_PARITY_CLASS_RETAINED=true",
        "NEXT_DERIVED_ROUTE=27-20-r302ac",
    ),
    "27-20-r302ac": (
        "PROJECTED_COARSE_FINE_COSET_IDENTITY_PROVED=true",
        "PROJECTED_COSET_ENERGY_BLOCK_MULTIPLICITY_BOUND_PROVED=true",
        "NEXT_DERIVED_ROUTE=27-20-r302ad",
    ),
    "27-20-r302ad": (
        "SQUARED_DIFFERENCE_TO_PRODUCT_PHASE_PROVED=true",
        "NEXT_DERIVED_ROUTE=27-20-r302ae",
    ),
    "27-20-r302ae": (
        "ODD_SHEAR_FROBENIUS_ENERGY_IDENTITY_PROVED=true",
        "NEXT_DERIVED_ROUTE=27-20-r302af",
    ),
    "27-20-r302af": (
        "UNIFORM_PRIMITIVE_UNIT_SUBTRACTION_EXACT=true",
        "RAMANUJAN_MAIN_TERM_EXPOSED=true",
        "NEXT_DERIVED_ROUTE=27-20-r302ag",
    ),
    "27-20-r302ag": (
        "RAMANUJAN_MAIN_TERM_REDUCED_TO_SINGULAR_WEIGHTED_ENERGY=true",
        "NEXT_DERIVED_ROUTE=27-20-r302ah",
    ),
    "27-20-r302ah": (
        "POINTWISE_UNIT_EQUIDISTRIBUTION_SUFFICIENT=true",
        "NEXT_DERIVED_ROUTE=27-20-r302ai",
    ),
    "27-20-r302ai": (
        "UNIT_GROUP_CHARACTER_INVERSION_PROVED=true",
        "NEXT_DERIVED_ROUTE=27-20-r302aj",
    ),
    "27-20-r302aj": (
        "FIXED_POWER_DISCREPANCY_ROUTE_MINIMAL=false",
        "NEXT_DERIVED_ROUTE=27-20-r302ak",
    ),
    "27-20-r302ak": (
        "FULL_TWO_PRIMARY_RECOMBINATION_PROVED=false",
        "NEXT_DERIVED_ROUTE=27-20-r302al",
    ),
    "27-20-r302al": (
        "JOINT_ADDITIVE_PARSEVAL_REDUCTION_PROVED=true",
        "TWO_ADIC_SQUARE_FIBER_BOUND_PROVED=true",
        "NEXT_DERIVED_ROUTE=27-20-r302am",
    ),
    "27-20-r302am": (
        "JOINT_SINGULAR_FOURIER_ENERGY_PROGRESSION_IDENTITY_PROVED=true",
        "NEXT_DERIVED_ROUTE=27-20-r302an",
    ),
    "27-20-r302an": (
        "SOLE_FIXED_POWER_INPUT_COUNT=1",
        "ZERO_LOSS_ADAPTER_COUNT=2",
        "SEPARATE_OFFDIAGONAL_FIXED_POWER_REQUIRED=false",
        "NEXT_DERIVED_ROUTE=27-20-r302ao",
    ),
}

for route, tokens in checks.items():
    text = read(S27 / route / "result.md")
    for token in tokens:
        req(text, token)
    for firewall in (
        "MAIN_ARITHMETIC_HOST_CORRELATION_POWER_DEFICIT_PROVED=false",
        "STRICT_SUB_SQRT_UPPER_PROVED=false",
        "NEW_MU_LT_HALF_PROVED=false",
        "TRUE_N2_EXPONENT_IDENTIFIED=false",
        "ADVANCE_TO_CHECKPOINT50=false",
    ):
        req(text, firewall)


# Elementary arithmetic helpers.
def vp(n, p, cap):
    if n == 0:
        return cap
    s = 0
    while s < cap and n % p == 0:
        n //= p
        s += 1
    return s


def phi(n):
    result = n
    x = n
    p = 2
    while p * p <= x:
        if x % p == 0:
            result -= result // p
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        result -= result // x
    return result


def mobius(n):
    if n == 1:
        return 1
    x = n
    count = 0
    p = 2
    while p * p <= x:
        if x % p == 0:
            x //= p
            count += 1
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        count += 1
    return -1 if count % 2 else 1


# r302z: exact odd prime-power square-collision formula.
for p in (3, 5):
    for k in range(1, 5):
        modulus = p ** k
        for u in range(modulus):
            actual = sum(1 for v in range(modulus) if (v * v - u * u) % modulus == 0)
            s = vp(u, p, k)
            expected = 2 * (p ** s) if 2 * s < k else p ** (k // 2)
            assert actual == expected, (p, k, u, actual, expected)


# r302al: safe 2-adic square-fiber bound on y mod 2^(nu-1).
for nu in range(2, 10):
    mod_y = 2 ** (nu - 1)
    modulus = 2 ** nu
    two_star = 2 ** (nu // 2)
    for y in range(mod_y):
        actual = sum(1 for z in range(mod_y) if (z * z - y * y) % modulus == 0)
        bound = 2 * math.gcd(y, two_star)
        assert actual <= bound, (nu, y, actual, bound)


# r302ab: exact arithmetic-progression Fourier energy identity.
def coeffs(W):
    q = len(W)
    return [
        sum(W[f] * cmath.exp(-2j * math.pi * b * f / q) for f in range(q)) / q
        for b in range(q)
    ]


def projected_energy(W, M, b0):
    q = len(W)
    N = q // M
    total = 0.0
    for t in range(N):
        block = sum(
            W[t + j * N] * cmath.exp(-2j * math.pi * b0 * j / M)
            for j in range(M)
        )
        total += abs(block) ** 2
    return total


for q in (12, 18, 24):
    W = [complex((7 * i + 3) % 11 - 5, (5 * i + 1) % 7 - 3) for i in range(q)]
    c = coeffs(W)
    for M in (d for d in range(1, q + 1) if q % d == 0):
        for b0 in range(M):
            lhs = sum(abs(c[b]) ** 2 for b in range(q) if b % M == b0)
            rhs = projected_energy(W, M, b0) / (q * M)
            assert abs(lhs - rhs) < 1e-8, (q, M, b0, lhs, rhs)


# r302ac: exact coarse/fine projected grouping identity.
def projected_block(W, M, b0, t):
    q = len(W)
    N = q // M
    return sum(
        W[t + j * N] * cmath.exp(-2j * math.pi * b0 * j / M)
        for j in range(M)
    )


for q in (24, 36):
    W = [complex((7 * i + 3) % 11 - 5, (5 * i + 1) % 7 - 3) for i in range(q)]
    for M0 in (d for d in range(1, q + 1) if q % d == 0):
        quotient = q // M0
        for r in (d for d in range(1, quotient + 1) if quotient % d == 0):
            Mr = M0 * r
            Nr = q // Mr
            for b0 in range(min(M0, 3)):
                br = b0  # one representative with br=b0 mod M0
                for t in range(Nr):
                    lhs = projected_block(W, Mr, br, t)
                    rhs = sum(
                        cmath.exp(-2j * math.pi * br * k / Mr)
                        * projected_block(W, M0, b0, t + k * Nr)
                        for k in range(r)
                    )
                    assert abs(lhs - rhs) < 1e-8, (q, M0, r, b0, t)


# r302af: Ramanujan-sum formula on representative odd moduli.
for m in (3, 5, 9, 15, 25, 27, 45):
    units = [a for a in range(m) if math.gcd(a, m) == 1]
    for h in range(m):
        actual = sum(cmath.exp(-2j * math.pi * a * h / m) for a in units)
        g = math.gcd(m, h)
        expected = mobius(m // g) * phi(m) / phi(m // g)
        assert abs(actual - expected) < 1e-8, (m, h, actual, expected)


# gcd divisor expansion used in r302ab/am.
for n in range(1, 80):
    for M in range(1, 80):
        lhs = math.gcd(n, M)
        rhs = sum(phi(r) for r in range(1, M + 1) if M % r == 0 and n % r == 0)
        assert lhs == rhs, (n, M, lhs, rhs)


registry = json.loads(read(S27 / "27-20-r302v-an" / "batch-registry.json"))
assert registry["status"] == "SUBMITTED_PENDING_FRESH_AUDIT"
assert registry["audit_status"] == "PENDING"
assert registry["merge_allowed"] is False
assert registry["fresh_reaudit_required"] is True
assert registry["claims"]["sole_fixed_power_input_count"] == 1
assert registry["claims"]["zero_loss_adapter_count"] == 2
assert registry["claims"]["main_arithmetic_host_correlation_power_deficit_proved"] is False
assert registry["advance_to_checkpoint50"] is False
assert registry["next_derived_route"] == "27-20-r302ao"
assert registry["next_expected_command"] == "Stage27-20-r302-audit"

print("Stage27-20-r302v-an algebra/lifecycle verification: PASS")
