#!/usr/bin/env python3
import cmath
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
S27 = ROOT / "stages" / "stage27"


def read(path):
    return path.read_text(encoding="utf-8")


def req(text, marker):
    assert marker in text, f"missing marker: {marker}"


def divisors(n):
    out = []
    for d in range(1, int(math.isqrt(n)) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


def mobius(n):
    if n == 1:
        return 1
    p = 2
    sign = 1
    x = n
    while p * p <= x:
        if x % p == 0:
            x //= p
            sign = -sign
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        sign = -sign
    return sign


def ramanujan_sum(q, n):
    return sum(d * mobius(q // d) for d in divisors(math.gcd(q, n)))


def valuation_capped(n, p, cap):
    if n == 0:
        return cap
    n = abs(n)
    v = 0
    while v < cap and n % p == 0:
        n //= p
        v += 1
    return v


def factorization(n):
    out = []
    p = 2
    x = n
    while p * p <= x:
        if x % p == 0:
            k = 0
            while x % p == 0:
                x //= p
                k += 1
            out.append((p, k))
        p += 1
    if x > 1:
        out.append((x, 1))
    return out


def s_factor(C, q):
    ans = 1
    for p, k in factorization(q):
        v = valuation_capped(C, p, k)
        ans *= p ** min(k // 2, v // 2)
    return ans


def omega_odd(q):
    return sum(1 for p, _ in factorization(q) if p != 2)


def roots(C, q):
    return [x for x in range(q) if (x * x - C) % q == 0]


# Lifecycle / route-chain checks.
parent = read(S27 / "27-20-r302an" / "result.md")
req(parent, "NEXT_DERIVED_ROUTE=27-20-r302ao")

checks = {
    "27-20-r302ao": [
        "R302V_FULL_STRATUM_FREQUENCY_FLAT_DIAGONAL_JUSTIFIED=false",
        "R302V_AN_ABC_PACKAGE_CANONICAL=false",
        "NEXT_DERIVED_ROUTE=27-20-r302ap",
    ],
    "27-20-r302ap": [
        "FULL_GCD_STRATUM_RAMANUJAN_RECOMBINATION_PROVED=true",
        "NEXT_DERIVED_ROUTE=27-20-r302aq",
    ],
    "27-20-r302aq": [
        "ALL_GCD_STRATA_RECOMBINE_TO_ROOT_PROJECTOR=true",
        "ROOT_KERNEL_PARSEVAL_IDENTITY_PROVED=true",
        "NEXT_DERIVED_ROUTE=27-20-r302ar",
    ],
    "27-20-r302ar": [
        "QUADRATIC_ROOT_PROJECTOR_L2_NORM=1",
        "GENERIC_ALL_C_SELECTOR_FIXED_POWER_CONTRACTION=false",
        "NEXT_DERIVED_ROUTE=27-20-r302as",
    ],
    "27-20-r302as": [
        "ACTUAL_ROOT_SET_CAUCHY_REDUCTION_PROVED=true",
        "NEXT_DERIVED_ROUTE=27-20-r302at",
    ],
    "27-20-r302at": [
        "LOCAL_QUADRATIC_ROOT_VALUATION_BOUND_PROVED=true",
        "REGULAR_UNIT_ROOT_MULTIPLICITY_SUBPOWER=true",
        "NEXT_DERIVED_ROUTE=27-20-r302au",
    ],
    "27-20-r302au": [
        "SINGULARITY_WEIGHTED_EFFECTIVE_SUPPORT_CRITERION_PROVED=true",
        "NEXT_DERIVED_ROUTE=27-20-r302av",
    ],
    "27-20-r302av": [
        "SR_STR_173_SUPPORT_FIREWALL_IMPORTED=true",
        "NEXT_DERIVED_ROUTE=27-20-r302aw",
    ],
    "27-20-r302aw": [
        "AR_012_IMPORTED_AS_DENSITY_SAVING=false",
        "R302J_MULTIPLICITY_DENSITY_FIREWALL_PRESERVED=true",
        "NEXT_DERIVED_ROUTE=27-20-r302ax",
    ],
    "27-20-r302ax": [
        "RESIDUE_L4_COLLISION_INDEX_DEFINED=true",
        "ROOT_ENERGY_L4_CAUCHY_REDUCTION_PROVED=true",
        "NEXT_DERIVED_ROUTE=27-20-r302ay",
    ],
    "27-20-r302ay": [
        "WEIGHTED_Z_MEAN_IMPLIES_BAD_PACKET_EXCEPTIONAL_MASS=true",
        "ONE_FIXED_POWER_THEOREM_SUFFICIENT=true",
        "NEXT_DERIVED_ROUTE=27-20-r302az",
    ],
    "27-20-r302az": [
        "RESIDUE_COLLISION_PARSEVAL_IDENTITY_PROVED=true",
        "COLLISION_NONZERO_FREQUENCY_ENERGY_EXPOSED=true",
        "NEXT_DERIVED_ROUTE=27-20-r302ba",
    ],
    "27-20-r302ba": [
        "S_Q_C_SQUARED_LE_GCD_C_Q=true",
        "ZERO_MODE_BY_GCD_THREE_HALVES_OVER_Q_PROVED=true",
        "NEXT_DERIVED_ROUTE=27-20-r302bb",
    ],
    "27-20-r302bb": [
        "COLLISION_STATISTIC_SPLIT_INTO_TWO_NONNEGATIVE_PARTS=true",
        "ZERO_AND_NONZERO_SAVINGS_MULTIPLIED=false",
        "NEXT_DERIVED_ROUTE=27-20-r302bc",
    ],
    "27-20-r302bc": [
        "FULL_ADDITIVE_FREQUENCY_RECOMBINATION_COMPLETE=true",
        "ONE_WEIGHTED_FIXED_POWER_THEOREM_SUFFICIENT=true",
        "SINGULARITY_WEIGHTED_RESIDUE_FOURTH_MOMENT_DEFICIT_PROVED=false",
        "ADVANCE_TO_CHECKPOINT50=false",
        "NEXT_DERIVED_ROUTE=27-20-r302bd",
    ],
}

for route, markers in checks.items():
    text = read(S27 / route / "result.md")
    for marker in markers:
        req(text, marker)
    req(text, "CHECKPOINT=40")
    req(text, "STRICT_SUB_SQRT_UPPER_PROVED=false")

reg = json.loads(read(S27 / "27-20-r302ao-bc" / "batch-registry.json"))
assert reg["status"] == "SUBMITTED_PENDING_FRESH_AUDIT"
assert reg["audit_status"] == "PENDING"
assert reg["merge_allowed"] is False
assert reg["advance_to_checkpoint50"] is False
assert reg["claims"]["full_gcd_stratum_frequency_flat_diagonal_justified"] is False
assert reg["claims"]["full_gcd_stratum_ramanujan_recombination_proved"] is True
assert reg["claims"]["all_strata_root_projector_recombination_proved"] is True
assert reg["claims"]["generic_all_coefficient_local_fixed_power_contraction"] is False
assert reg["claims"]["singularity_weighted_residue_fourth_moment_deficit_proved"] is False

# Exact Ramanujan-stratum and full-projector identities.
for q in range(1, 49):
    for C in range(q):
        for f in range(q):
            n = f * f - C
            total = sum(ramanujan_sum(Q, n) for Q in divisors(q))
            assert total == (q if n % q == 0 else 0)

            # Direct complex check for every gcd stratum.
            for d in divisors(q):
                Q = q // d
                direct = sum(
                    cmath.exp(2j * math.pi * a * n / q)
                    for a in range(q)
                    if math.gcd(a, q) == d
                )
                expected = ramanujan_sum(Q, n)
                assert abs(direct - expected) < 1e-8

# Root multiplicity envelope R_q(C) <= 4 * 2^omega(q_odd) * s_q(C).
for q in range(1, 129):
    for C in range(q):
        R = len(roots(C, q))
        bound = 4 * (2 ** omega_odd(q)) * s_factor(C, q)
        assert R <= bound, (q, C, R, bound)
        if math.gcd(C, q) == 1:
            assert s_factor(C, q) == 1

# L4/root-energy and collision-Parseval regression checks on deterministic weights.
for q in range(2, 25):
    W = [complex((3 * f + 1) % 5 - 2, (2 * f + 3) % 3 - 1) for f in range(q)]
    E = sum(abs(w) ** 2 for w in W)
    if E == 0:
        continue
    Lambda = sum(abs(w) ** 4 for w in W) / (E * E)
    nu = [abs(w) ** 2 for w in W]
    nuhat = [
        sum(nu[f] * cmath.exp(-2j * math.pi * h * f / q) for f in range(q))
        for h in range(q)
    ]
    parseval_lambda = sum(abs(z) ** 2 for z in nuhat) / (q * E * E)
    assert abs(Lambda - parseval_lambda) < 1e-8
    assert abs(abs(nuhat[0]) / E - 1.0) < 1e-8

    for C in range(q):
        rr = roots(C, q)
        R = len(rr)
        Eroot = sum(abs(W[f]) ** 2 for f in rr)
        lhs = R * Eroot / E
        rhs = (R ** 1.5) * math.sqrt(Lambda) if R else 0.0
        assert lhs <= rhs + 1e-8

print("Stage27-20-r302ao-bc verification: PASS")
