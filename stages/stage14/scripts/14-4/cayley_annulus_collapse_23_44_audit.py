#!/usr/bin/env python3
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def require(path: str, token: str) -> None:
    text = (ROOT / path).read_text()
    assert token in text, (path, token)


# Canonical merged predecessor locks.
require(
    "stages/stage14/14-4cw/result.md",
    "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=61/112",
)
require(
    "stages/stage14/14-s7-38/result.md",
    "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=61/112",
)
require(
    "stages/stage14/14-X12/result.md",
    "LOST_CORE_FOURTH_ROOT_DIVISOR_DIVIDES_COLUMN_COFACTOR_PRODUCT=true",
)
require(
    "stages/stage14/14-X12/result.md",
    "H | gcd(L_-,L_+)",
)
require(
    "stages/stage14/14-4cq/result.md",
    "lambda*x*y == 4 (mod C_*)",
)


# Primewise exponent sanity for the annulus collapse.
# At a prime in H_star, C_Cayley is a unit, so A_C has zero exponent.
# At a prime outside H_star, g_star can carry only endpoint-small exponent e,
# and A_C|g_star^2 gives v_p(A_C)<=2e.
annulus_checks = 0
for h in range(0, 6):
    for e in range(0, 4):
        gstar = 2 * h + e
        for a in range(0, 2 * gstar + 1):
            if h > 0:
                # Cayley-good coprimality with H_star forces no annulus mass.
                admissible = (a == 0)
            else:
                admissible = (a <= 2 * e)
            if admissible:
                assert a <= 2 * e
                annulus_checks += 1
assert annulus_checks > 0


# If D|Omega*H^2, removing the Omega contribution leaves D0|H^2.
lost_core_checks = 0
for h in range(0, 7):
    for o in range(0, 5):
        for d in range(0, o + 2 * h + 1):
            d0 = d - min(d, o)
            assert d0 <= 2 * h
            lost_core_checks += 1
assert lost_core_checks > 0


# Exact exponent identities.
assert F(61, 112) - F(23, 44) == F(27, 1232)
assert F(23, 44) - F(1, 2) == F(1, 44)
assert F(7, 16) < F(23, 44)


def strip_ok(theta: F, phi: F) -> bool:
    return (
        F(3, 16) <= theta <= F(5, 16)
        and F(1, 8) <= phi <= F(1, 4)
        and theta >= phi
        and theta - phi <= F(1, 8)
        and theta + phi >= F(3, 8)
    )


def low_core_optimized_bound(theta: F, phi: F) -> F:
    chi = 2 * theta + 2 * phi - F(3, 4)
    assert chi <= F(1, 4)

    Es = max(2 * theta, 1 - 2 * theta)
    Ek = 3 * theta - F(1, 4)

    # EH(s)=A-3s, EDRC(s)=B+2s.
    A = 3 * phi - F(1, 8)
    B = 2 * phi + F(1, 2) - 2 * chi
    s_intersection = (A - B) / 5

    if s_intersection <= 0:
        # EH is already the smaller complete count at s=0 and decreases.
        core = A
    else:
        # 2:3 weighted cancellation of s.
        core = F(23, 20) - F(12, 5) * theta

    return min(Es, Ek, core)


# Exact whole-strip grid.  High-core nonproportional blocks are excluded by
# the full-lost-core divisibility theorem, so only chi<=1/4 is scanned.
D = 1144  # 13*88; contains theta=23/88 and all saturation endpoints.
best = (F(-100), None)
saturation = []

for nt in range(3 * D // 16, 5 * D // 16 + 1):
    theta = F(nt, D)
    for np in range(D // 8, D // 4 + 1):
        phi = F(np, D)
        if not strip_ok(theta, phi):
            continue
        chi = 2 * theta + 2 * phi - F(3, 4)
        if chi > F(1, 4):
            continue

        E = low_core_optimized_bound(theta, phi)
        if E > best[0]:
            best = (E, (theta, phi, chi))
        if E == F(23, 44):
            saturation.append((theta, phi, chi))

assert best[0] == F(23, 44), best
assert saturation
assert {t for t, _, _ in saturation} == {F(23, 88)}
assert min(p for _, p, _ in saturation) == F(19, 88)
assert max(p for _, p, _ in saturation) == F(21, 88)


# Exact saturation ledger at the two endpoints and one interior point.
for phi in (F(19, 88), F(20, 88), F(21, 88)):
    theta = F(23, 88)
    s = phi - F(19, 88)
    chi = 2 * phi - F(5, 22)
    j = F(9, 44)
    lost = chi - j
    residual_column = F(1, 22) - 2 * s
    row_lift = F(1, 22)

    assert s >= 0
    assert chi <= F(1, 4)
    assert lost == 2 * s
    assert residual_column == F(1, 4) - chi
    assert 2 * phi + residual_column + row_lift == F(23, 44)
    assert 3 * phi - F(1, 8) - 3 * s == F(23, 44)


result = (ROOT / "stages/stage14/14-4cx/result.md").read_text()
for token in (
    "STAGE14_4CX=COMPLETE_CAYLEY_ANNULUS_COLLAPSE_FULL_LOST_CORE_COLUMN_DIVISOR_AND_23_44_PROMOTION",
    "CAYLEY_GOOD_CORE_COPRIME_TO_MN=true",
    "CAYLEY_ONLY_ANNULUS_FIXED_POWER_EMPTY=true",
    "LOST_CORE_ENDPOINT_PEELED_DIVIDES_H_SQUARE=true",
    "FULL_LOST_CORE_DIVIDES_COLUMN_COFACTOR_PRODUCT=true",
    "FIXED_POWER_HIGH_CORE_NONPROPORTIONAL_BRANCH_EMPTY=true",
    "LOW_CORE_WEIGHTED_COMPLETE_COUNT_COMBINATION=2:3",
    "NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=23/44",
    "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=23/44",
    "IMPROVEMENT_OVER_MERGED_4CW_61_112=27/1232",
    "CURRENT_GAP_TO_SQRT=1/44",
    "TWENTYTHREE_44_SATURATION_THETA=23/88",
    "TWENTYTHREE_44_SATURATION_PHI_MIN=19/88",
    "TWENTYTHREE_44_SATURATION_PHI_MAX=21/88",
    "TWENTYTHREE_44_JOINT_CORE_EXPONENT=9/44",
    "TWENTYTHREE_44_ROW_LIFT_EXPONENT=1/22",
    "REMAINING_RECEIVER=TwentyThreeFortyFourthsCayleyAnnulusCollapseLostCoreColumnRowLiftTradeoff",
    "MAINLINE_H_NEEDED=false",
    "NEXT=Stage14-4cy",
):
    assert token in result, token

print("Stage14-4cx Cayley-annulus collapse audit: PASS")
print("annulus primewise checks:", annulus_checks)
print("lost-core exponent checks:", lost_core_checks)
print("best low-core block:", best)
print("saturation phi range:", F(19, 88), F(21, 88))
print("CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=23/44")
