#!/usr/bin/env python3
"""Stage14-s7-35 deterministic audit.

New exact arithmetic:
  for the xi switched S-host,
      g_S = oddpart(gcd(Re W_S, Im W_S)),
      H_S = oddpart(gcd(x_2,y_1)),
  one has
      gcd(g_S,S)=1,
      g_S/H_S^2 | oddpart(omega_1*omega_2).
The T-host is symmetric.

Since omega_i=B^o(1), the fixed-power `extra` residual gcd isolated in s7-34
cannot exist.  Thus rho=2*eta_star+o(1).  Retaining the exact 4cu/s7-34
joint-core inequality gives eta >= (chi-1/4)/4 and the complete H-count
saving 3(chi-1/4)/4.  Exact strip minimax yields 4/7.
"""
from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve()
ROOT = HERE.parents[4]
SCRIPTS = HERE.parents[1]


def load_module(name: str, path: Path):
    spec = spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    mod = module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


s733 = load_module(
    "s733_s735",
    SCRIPTS / "14-s7-33" / "shared_common_core_orientation_probe.py",
)
s28 = s733.s28
s32 = s733.s32
ch = s733.ch


def oddpart(n: int) -> int:
    return s32.oddpart(abs(n))


def require(path: str, token: str) -> None:
    text = (ROOT / path).read_text()
    assert token in text, (path, token)


# Canonical predecessor locks.
require(
    "stages/stage14/14-s7-34/result.md",
    "STAGE14_S7_34=COMPLETE_XI_FOURTH_POWER_ROOT_GCD_TRANSFER_AND_47_80_PROMOTION",
)
require(
    "stages/stage14/14-s7-34/result.md",
    "XI_COMMON_ROOT_GCD_FOURTH_POWER_DIVIDES_QXI=true",
)
require(
    "stages/stage14/14-s7-34/result.md",
    "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=47/80",
)
require(
    "stages/stage14/14-4cu/result.md",
    "JOINT_CORE_DIVIDES_ENDPOINT_LINEAR_PRODUCT=true",
)


# Finite physical packet audit of the exact extra-gcd support collapse.
groups = ch.make_groups(600)
checked = 0
max_extra_S = max_extra_T = max_omega_prod = 1
nontrivial_extra = 0
for states in groups.values():
    for i in range(len(states)):
        for j in range(i + 1, len(states)):
            a, b = states[i], states[j]
            if (a["a"], a["b"]) == (b["a"], b["b"]):
                continue
            if (a["km"], a["kp"]) == (b["km"], b["kp"]):
                continue

            s32.audit_packet(a, b)
            d = s28.packet_data(a, b)
            R, S, T, J, *_ = d["cells"]

            HS = oddpart(gcd(b["x"], a["y"]))
            HT = oddpart(gcd(a["x"], b["y"]))

            _, _, g1 = s32.state_pq(a)
            _, _, g2 = s32.state_pq(b)
            omega1 = g1 * a["r"] * a["s"]
            omega2 = g2 * b["r"] * b["s"]
            omprod = oddpart(omega1 * omega2)

            ZS = (R * b["x"] ** 2 * omega1, J * a["y"] ** 2 * omega2)
            ZT = (J * b["y"] ** 2 * omega1, R * a["x"] ** 2 * omega2)
            _, WS = s32.gaussian_descent_allow_one(ZS[0], ZS[1], S)
            _, WT = s32.gaussian_descent_allow_one(ZT[0], ZT[1], T)

            gS = oddpart(gcd(WS[0], WS[1]))
            gT = oddpart(gcd(WT[0], WT[1]))

            # Switched-cell primes cannot enter the rational coordinate gcd
            # of the residual host; otherwise p would divide both raw host
            # coordinates after multiplication by lambda^2.
            assert gcd(gS, oddpart(S)) == 1
            assert gcd(gT, oddpart(T)) == 1

            # At primes outside the switch cell Gaussian descent is invertible
            # over Z_p^2, so the rational gcd is unchanged.
            rawS = oddpart(gcd(ZS[0], ZS[1]))
            rawT = oddpart(gcd(ZT[0], ZT[1]))
            assert gS == rawS
            assert gT == rawT

            assert gS % (HS * HS) == 0
            assert gT % (HT * HT) == 0
            extraS = gS // (HS * HS)
            extraT = gT // (HT * HT)

            # Write x2=HS*x2', y1=HS*y1'.  Reducedness gives
            # gcd(R*x2'^2, J*y1'^2)=1, hence every remaining common prime
            # must be supplied by omega1 or omega2.  Symmetrically for T.
            assert omprod % extraS == 0
            assert omprod % extraT == 0

            checked += 1
            nontrivial_extra += int(extraS > 1 or extraT > 1)
            max_extra_S = max(max_extra_S, extraS)
            max_extra_T = max(max_extra_T, extraT)
            max_omega_prod = max(max_omega_prod, omprod)

assert checked == 52, checked


# Synthetic arithmetic guard for the general gcd lemma.
synthetic = 0
for R, J in ((5, 13), (13, 17), (17, 29)):
    for xp, yp in ((1, 1), (1, 3), (2, 5), (5, 2), (7, 9)):
        if gcd(R * xp * xp, J * yp * yp) != 1:
            continue
        for h in (1, 3, 5, 9):
            for om1, om2 in ((1, 1), (3, 5), (7, 3), (9, 25)):
                A = R * (h * xp) ** 2 * om1
                B = J * (h * yp) ** 2 * om2
                graw = oddpart(gcd(A, B))
                assert graw % (oddpart(h) ** 2) == 0
                extra = graw // (oddpart(h) ** 2)
                assert oddpart(om1 * om2) % extra == 0
                synthetic += 1


# Exact whole-strip minimax with forced saving 3/4*(chi-1/4).
# Denominator 2240 contains theta=2/7 and all balanced endpoints.
D = 2240
best = (F(-1), None)
low_core_best = (F(-1), None)
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

        if chi > F(1, 4):
            d = chi - F(1, 4)
            # g_star = H_star^2 * B^o(1), so rho=2 eta_star.
            # Exact joint-core pressure:
            # d <= 2 rho + 2 eta_other
            #   = 4 eta_star + 2 eta_other <= 4 eta.
            # Hence eta>=d/4 and the H^4 complete count saves 3d/4.
            Ex -= F(3, 4) * d
        else:
            E0 = min(Es, Ek, Ex)
            if E0 > low_core_best[0]:
                low_core_best = (E0, (theta, phi, chi))

        E = min(Es, Ek, Ex)
        if E > best[0]:
            best = (E, (theta, phi, chi, Es, Ek, Ex))

assert low_core_best[0] == F(11, 20), low_core_best
assert best == (
    F(4, 7),
    (
        F(2, 7),
        F(1, 4),
        F(9, 28),
        F(4, 7),
        F(17, 28),
        F(4, 7),
    ),
), best

# Equality profile.
theta = F(2, 7)
phi = F(1, 4)
chi = F(9, 28)
d = chi - F(1, 4)
eta = d / 4
eta_star = eta
eta_other = F(0)
rho = 2 * eta_star
jexp = chi - 2 * rho - 2 * eta_other
assert d == F(1, 14)
assert eta == F(1, 56)
assert rho == F(1, 28)
assert jexp == F(1, 4)
assert 3 * phi - F(1, 8) - 3 * eta == F(4, 7)
assert 2 * theta == F(4, 7)
assert F(9, 16) < F(4, 7)
assert F(11, 20) < F(4, 7)
assert F(47, 80) - F(4, 7) == F(9, 560)

# Freeze theorem boundary.
result = (ROOT / "stages/stage14/14-s7-35/result.md").read_text()
for token in (
    "STAGE14_S7_35=COMPLETE_EXTRA_XI_RESIDUAL_GCD_COLLAPSE_AND_4_7_PROMOTION",
    "XI_RESIDUAL_GCD_COPRIME_TO_SWITCH_CELL=true",
    "XI_RESIDUAL_GCD_EQUALS_RAW_HOST_ODD_GCD=true",
    "XI_EXTRA_GCD_DIVIDES_ENDPOINT_OMEGA_PRODUCT=true",
    "XI_EXTRA_GCD_FIXED_POWER_SUPPORT=false",
    "NONPROPORTIONAL_FORCED_H_EXPONENT=(chi-1/4)/4",
    "NONPROPORTIONAL_FORCED_SAVING=3*(chi-1/4)/4",
    "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=4/7",
    "IMPROVEMENT_OVER_PREVIOUS_47_80=9/560",
    "FOUR_SEVENTHS_SATURATION_THETA=2/7",
    "FOUR_SEVENTHS_SATURATION_PHI=1/4",
    "FOUR_SEVENTHS_SINGLE_CROSS_ROOT_EXPONENT=1/56",
    "FOUR_SEVENTHS_JOINT_CORE_EXPONENT=1/4",
    "FOUR_SEVENTHS_LINEAR_PRODUCT_COFACTOR_EXPONENT=0",
    "REMAINING_RECEIVER=FourSeventhsSingleCrossRootFullJointCoreLinearProductIncidence",
    "S7_35_AUXILIARY_H_NEEDED=false",
    "NEXT=Stage14-s7-36",
):
    assert token in result, token

print("Stage14-s7-35 extra-gcd collapse audit: PASS")
print("finite physical pairs checked:", checked)
print("finite packets with nontrivial endpoint extra gcd:", nontrivial_extra)
print("max finite extra S/T:", max_extra_S, max_extra_T)
print("max finite omega product:", max_omega_prod)
print("synthetic gcd checks:", synthetic)
print("low-core max:", low_core_best)
print("whole-strip max:", best)
print("new saving over 47/80:", F(9, 560))
