from pathlib import Path
from math import isqrt

ROOT = Path(__file__).resolve().parents[4]

S111 = ROOT / "stages/stage14/14-s7-111/result.md"
S112 = ROOT / "stages/stage14/14-s7-112/result.md"
S113 = ROOT / "stages/stage14/14-s7-113/result.md"
REPORT = ROOT / "stages/stage14/14-s-batch/s7-111-113-report.md"
WORK37 = ROOT / "stages/stage14/14-Work-byX37/result.md"
MAIN_GB = ROOT / "stages/stage14/14-4gb/result.md"
S110 = ROOT / "stages/stage14/14-s7-110/result.md"


def text(path: Path) -> str:
    assert path.exists(), path
    return path.read_text(encoding="utf-8")


def sqf(n: int) -> int:
    out = 1
    p = 2
    x = n
    while p * p <= x:
        e = 0
        while x % p == 0:
            x //= p
            e += 1
        if e % 2:
            out *= p
        p += 1
    if x > 1:
        out *= x
    return out


s111 = text(S111)
s112 = text(S112)
s113 = text(S113)
report = text(REPORT)
work37 = text(WORK37)
main_gb = text(MAIN_GB)
s110 = text(S110)

# Canonical merged-source locks.
for needle in [
    "FIBERED_BOUNDED_MULTIPLICITY_MULTIPLICATION_LEMMA_PROVED=true",
    "GLOBAL_S_HEAVY_RECEIVERS_ALL_REDUCED_TO_CONDITIONAL_PHYSICAL_COMPLETION_OR_LIFT=true",
    "S_ROUTE_H_NEEDED=false",
]:
    assert needle in work37, needle

assert "FixedComplementaryDilationTwoSidedPrincipalRectangularConditionalCanonicalReversePhysicalCompletionDeficitWithCapacityHeadroomKappaMinusMu" in main_gb
assert "PolynomialComplementaryDilationPolynomialPrimitiveProductPrincipalFiberedDistinctProductOuterPairCapacityVersusConditionalPhysicalLiftDeficit" in s110

# s7-111 boundary locks.
for needle in [
    "WORK_BYX37_CONSUMED=true",
    "S_ALL_FOUR_HEAVY_REALIZATIONS_COMPLETION_ONLY=true",
    "PRECOMPLETION_NORMALIZED_RECONSTRUCTION_EXACT=true",
    "EXACT_PHYSICAL_COMPLETION_BOOLEAN_DEFINED=true",
    "PHYSICAL_COMPLETION_EXISTENCE_AUTOMATIC=false",
]:
    assert needle in s111, needle

# Finite deterministic audit of E=J1*g^2 and reconstruction identities.
for E in range(1, 160):
    J1 = sqf(E)
    q = E // J1
    g = isqrt(q)
    assert g * g == q
    assert E == J1 * g * g
    for u, v in [(2, 3), (3, 5), (4, 7), (5, 8)]:
        n = E * u * v
        L = E * u * u
        a1 = g * u
        b1 = g * v
        assert n * u == L * v
        assert a1 * b1 * J1 == g * g * J1 * u * v
        assert g * g * J1 * u * v == n

# s7-112 quantifier split / no-recharge locks.
for needle in [
    "PRECOMPLETION_FILTER_DEFINED_BY_PROVEN_VARIABLE_DEPENDENCE=true",
    "EXISTENTIAL_REVERSE_POSTCOLUMN_COMPLETION_BOOLEAN_DEFINED=true",
    "PHYSICAL_BOOLEAN_SPLIT_USES_INDEPENDENCE=false",
    "REVERSE_POSTCOLUMN_WITNESS_MULTIPLICITY=Bo1",
    "REVERSE_POSTCOLUMN_EXISTENCE_AUTOMATIC=false",
    "REVERSE_COMPLETION_MULTIPLICITY_RECHARGE_ALLOWED=false",
    "EXISTENTIAL_SUPPORT_NOT_WITNESS_COUNT_IS_RECEIVER=true",
]:
    assert needle in s112, needle

# Nested-support exponent accounting is arithmetic bookkeeping only.
toy = [
    (0.20, 0.18, 0.17, 0.15),
    (0.16, 0.16, 0.15, 0.14),
    (0.10, 0.08, 0.06, 0.05),
]
for kappa, sigma, tau, mu in toy:
    assert kappa >= sigma >= tau
    delta_pre = kappa - sigma
    delta_ext = sigma - tau
    assert abs((kappa - delta_pre - delta_ext) - tau) < 1e-12
    assert (tau >= mu) == (kappa - delta_pre - delta_ext >= mu)

for needle in [
    "TWO_LEVEL_COMPLETION_DEFICIT_LEDGER_EXACT=true",
    "HEAVY_SURVIVAL_LEDGER=kappa_minus_delta_pre_minus_delta_ext_ge_mu",
    "NEAR_THRESHOLD_SURVIVOR_FORCES_ZERO_PREFILTER_DEFICIT=true",
    "NEAR_THRESHOLD_SURVIVOR_FORCES_ZERO_EXTENSION_DEFICIT=true",
    "WORK_BYX37_REVISIT_TRIGGER_S7_113_REACHED=true",
    "RECEIVER_MATERIALLY_CHANGED=true",
    "S_ROUTE_H_NEEDED=false",
    "NEXT=Stage14-s7-114",
]:
    assert needle in s113 or needle in report, needle

# Batch contract boundary.
for needle in [
    "BATCH_FIRST_STAGE=Stage14-s7-111",
    "BATCH_LAST_STAGE=Stage14-s7-113",
    "BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3",
    "BATCH_INTEGRATED_H_UNITS=NONE",
    "BATCH_STOP_REASON=receiver_change",
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
    "S_ROUTE_H_NEEDED=false",
    "NEXT=Stage14-s7-114",
]:
    assert needle in report, needle

print("STAGE14_S_BATCH_AUDIT=PASS")
print("S7_111_113_COMPLETION_BOOLEAN_OPENING_AUDIT=PASS")
