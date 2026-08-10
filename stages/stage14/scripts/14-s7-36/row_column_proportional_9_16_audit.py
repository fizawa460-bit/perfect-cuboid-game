#!/usr/bin/env python3
from fractions import Fraction as F
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def require(path: str, token: str) -> None:
    text = (ROOT / path).read_text()
    assert token in text, (path, token)


# Canonical merged inputs.
require(
    "stages/stage14/14-s7-35/result.md",
    "STAGE14_S7_35=COMPLETE_EXTRA_XI_RESIDUAL_GCD_COLLAPSE_AND_4_7_PROMOTION",
)
require(
    "stages/stage14/14-s7-35/result.md",
    "XI_EXTRA_GCD_DIVIDES_ENDPOINT_OMEGA_PRODUCT=true",
)
require(
    "stages/stage14/14-s7-35/result.md",
    "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=4/7",
)
require(
    "stages/stage14/14-4cv/result.md",
    "STAGE14_4CV=COMPLETE_JOINT_CORE_ROW_COLUMN_COFACTOR_RECONSTRUCTION_AND_SEVEN_TWELFTHS_PROMOTION",
)
require(
    "stages/stage14/14-4cv/result.md",
    "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/12",
)
require(
    "stages/stage14/14-4cu/result.md",
    "PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=9/16",
)


# Small CRT helper for a synthetic reconstruction regression.
def invmod(a: int, m: int) -> int:
    return pow(a, -1, m)


def crt2(a: int, m: int, b: int, n: int) -> int:
    assert gcd(m, n) == 1
    t = ((b - a) * invmod(m, n)) % n
    return (a + m * t) % (m * n)


# Exact 2x2 row/column reading of one modulus.
# First sign = Cayley row, second sign = endpoint-linear column.
synthetic_checks = 0
cell_sets = (
    (5, 13, 17, 29),
    (13, 17, 29, 37),
    (17, 29, 37, 41),
    (29, 37, 41, 53),
)
for Jmm, Jmp, Jpm, Jpp in cell_sets:
    Jcm = Jmm * Jmp
    Jcp = Jpm * Jpp
    Jlm = Jmm * Jpm
    Jlp = Jmp * Jpp
    J = Jmm * Jmp * Jpm * Jpp
    assert Jcm * Jcp == J
    assert Jlm * Jlp == J
    assert gcd(Jcm, Jcp) == gcd(Jlm, Jlp) == 1

    for hm in (1, 3, 5, 7):
        for hp in (1, 3, 9):
            Lm = Jlm * hm
            Lp = Jlp * hp
            A = (Lp + Lm) // 2
            B = (Lp - Lm) // 2
            assert 2 * A == Lp + Lm
            assert 2 * B == Lp - Lm
            assert abs(hm * hp) == abs(Lm * Lp) // J

            for M in (1, 19, 123, 1001):
                N0 = crt2(M % Jcm, Jcm, (-M) % Jcp, Jcp)
                assert (N0 - M) % Jcm == 0
                assert (N0 + M) % Jcp == 0
                # One residue class modulo the same already-charged J.
                assert 0 <= N0 < J
                synthetic_checks += 1

assert synthetic_checks == 192


# Exponent ledger.
# s7-35 gives, for selected cross cell exponents a=eta_star >= b=eta_other,
#   rho = 2a + o(1),
# and the pre-relaxation joint-core lower bound
#   j >= chi - 4a - 2b.
# 4cv row/column reconstruction therefore gives
#   E_RC <= 2phi+1/2-2chi + 8a + 4b.
# The fourth-power-root complete count is
#   E_H <= 3phi-1/8 - 3a - 3b.
# Taking (8 E_H + 3 E_RC)/11 cancels a and leaves a favorable -12b/11.
# Hence every nonproportional block satisfies
#   E <= (18phi - 12theta + 5)/11.

D = 816  # divisible by 16, 48 and 68; contains all equality points below.
best_nonprop = (F(-1), None)
best_prop = (F(-1), None)
prop_saturation = []

for nt in range(3 * D // 16, 5 * D // 16 + 1):
    theta = F(nt, D)
    for np in range(D // 8, D // 4 + 1):
        phi = F(np, D)
        if theta < phi or theta - phi > F(1, 8) or theta + phi < F(3, 8):
            continue

        Es = max(2 * theta, 1 - 2 * theta)
        Ek = 3 * theta - F(1, 4)
        Ex = 3 * phi - F(1, 8)
        chi = 2 * theta + 2 * phi - F(3, 4)

        ErcH = (18 * phi - 12 * theta + 5) / 11
        Enon = min(Es, Ek, Ex, ErcH)
        if Enon > best_nonprop[0]:
            best_nonprop = (Enon, (theta, phi, chi, Es, Ek, Ex, ErcH))

        # 4cu proportional branch: L_-=0 gives a common z-scale t~B^(1/8)
        # surviving into the k residual host and therefore
        # E_k,prop <= 3theta-3/8.
        Ekprop = 3 * theta - F(3, 8)
        Eprop = min(Es, Ex, Ekprop)
        if Eprop > best_prop[0]:
            best_prop = (Eprop, (theta, phi, chi, Es, Ex, Ekprop))
        if Eprop == F(9, 16):
            prop_saturation.append((theta, phi, chi))

assert best_nonprop == (
    F(19, 34),
    (
        F(19, 68),
        F(1, 4),
        F(21, 68),
        F(19, 34),
        F(10, 17),
        F(5, 8),
        F(19, 34),
    ),
), best_nonprop

assert best_prop[0] == F(9, 16), best_prop
assert prop_saturation
assert min(p for _, p, _ in prop_saturation) == F(11, 48)
assert max(p for _, p, _ in prop_saturation) == F(1, 4)
assert {t for t, _, _ in prop_saturation} == {F(5, 16)}
assert min(c for _, _, c in prop_saturation) == F(1, 3)
assert max(c for _, _, c in prop_saturation) == F(3, 8)

# Nonproportional equality profile.
theta = F(19, 68)
phi = F(1, 4)
chi = F(21, 68)
eta_other = F(0)
eta_star = (F(5, 8) - F(19, 34)) / 3
rho = 2 * eta_star
j = chi - 4 * eta_star - 2 * eta_other
short = F(1, 4) - j
assert eta_star == F(3, 136)
assert rho == F(3, 68)
assert j == F(15, 68)
assert short == F(1, 34)
assert F(9, 16) - F(19, 34) == F(1, 272)

# Whole-family promotion is now controlled by the proportional branch.
assert max(best_nonprop[0], best_prop[0]) == F(9, 16)
assert F(4, 7) - F(9, 16) == F(1, 112)
assert F(9, 16) - F(1, 2) == F(1, 16)

result = (ROOT / "stages/stage14/14-s7-36/result.md").read_text()
for token in (
    "STAGE14_S7_36=COMPLETE_ROW_COLUMN_REOPTIMIZATION_AND_9_16_PROPORTIONAL_BARRIER_PROMOTION",
    "MERGED_4CV_ROW_COLUMN_RECONSTRUCTION_IMPORTED=true",
    "S7_35_EXTRA_GCD_COLLAPSE_INSERTED_INTO_ROW_COLUMN_LEDGER=true",
    "NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=19/34",
    "NONPROPORTIONAL_SATURATION_THETA=19/68",
    "NONPROPORTIONAL_TWIN_SHORT_SUPPORT_EXPONENT=1/34",
    "PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=9/16",
    "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=9/16",
    "IMPROVEMENT_OVER_PREVIOUS_4_7=1/112",
    "CURRENT_GAP_TO_SQRT=1/16",
    "REMAINING_RECEIVER=NineSixteenthsProportionalCommonZScaleKGaussianResidualIncidence",
    "S7_36_AUXILIARY_H_NEEDED=false",
    "NEXT=Stage14-s7-37",
):
    assert token in result, token

print("Stage14-s7-36 row/column + proportional audit: PASS")
print("synthetic row/column checks:", synthetic_checks)
print("best nonproportional:", best_nonprop)
print("best proportional:", best_prop)
print("proportional saturation phi range:", F(11, 48), F(1, 4))
print("whole-family exponent:", F(9, 16))
print("saving over 4/7:", F(1, 112))
print("gap to sqrt:", F(1, 16))
