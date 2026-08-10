#!/usr/bin/env python3
"""Stage14-s7-34 deterministic audit.

Combines merged s7-33/4cu with the exact two-cross-cell root gcd split.
The new arithmetic point is

    H_S^2 | g_S, H_T^2 | g_T,
    g_S^2 | q_xi, g_T^2 | q_xi,
    gcd(H_S,H_T)=1

and hence H^4 | q_xi for H=H_S H_T.

This supplies a second complete xi one-host count with saving 3*eta when
H=B^(eta+o(1)).  Combining it by min with the 4cu residual-gcd saving rho
and the nonproportional joint-core inequality yields a forced saving
3*(chi-1/4)/7 and the exact 47/80 minimax.
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
    "s733_s734",
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
    "stages/stage14/14-s7-33/result.md",
    "STAGE14_S7_33=COMPLETE_COMMON_CORE_GAUSSIAN_ORIENTATION_IDENTIFICATION_AND_TRANSFER_NOGO",
)
require(
    "stages/stage14/14-s7-33/result.md",
    "COMMON_CORE_CANCELLED_GAUSSIAN_TRANSFER_IDENTITY_PROVED=true",
)
require(
    "stages/stage14/14-4cu/result.md",
    "STAGE14_4CU=COMPLETE_RESIDUAL_CAYLEY_ORIENTATION_LINEAR_PRODUCT_TRANSFER_AND_19_32_PROMOTION",
)
require(
    "stages/stage14/14-4cu/result.md",
    "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=19/32",
)
require(
    "stages/stage14/14-4cu/result.md",
    "JOINT_CORE_DIVIDES_ENDPOINT_LINEAR_PRODUCT=true",
)


# Physical-packet fourth-power audit.
groups = ch.make_groups(600)
checked = 0
h_nontrivial = 0
max_H = max_HS = max_HT = max_gS = max_gT = max_qxi = 1
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
            C, _, v_res = d["triple"]

            HS = oddpart(gcd(b["x"], a["y"]))
            HT = oddpart(gcd(a["x"], b["y"]))
            H = oddpart(gcd(a["x"] * b["x"], a["y"] * b["y"]))
            assert H == HS * HT
            assert gcd(HS, HT) == 1

            _, _, g1 = s32.state_pq(a)
            _, _, g2 = s32.state_pq(b)
            omega1 = g1 * a["r"] * a["s"]
            omega2 = g2 * b["r"] * b["s"]
            ZS = (R * b["x"] ** 2 * omega1, J * a["y"] ** 2 * omega2)
            ZT = (J * b["y"] ** 2 * omega1, R * a["x"] ** 2 * omega2)
            _, WS = s32.gaussian_descent_allow_one(ZS[0], ZS[1], S)
            _, WT = s32.gaussian_descent_allow_one(ZT[0], ZT[1], T)

            gS = oddpart(gcd(WS[0], WS[1]))
            gT = oddpart(gcd(WT[0], WT[1]))
            qS = oddpart(s32.gnorm(WS))
            qT = oddpart(s32.gnorm(WT))
            qxi = C * oddpart(v_res)
            assert qS == qT == qxi

            # 4cu matched-cross-cell divisibilities, now pushed through norms.
            assert gS % (HS * HS) == 0
            assert gT % (HT * HT) == 0
            assert qxi % (gS * gS) == 0
            assert qxi % (gT * gT) == 0
            assert qxi % (HS ** 4) == 0
            assert qxi % (HT ** 4) == 0
            assert qxi % (H ** 4) == 0

            checked += 1
            h_nontrivial += int(H > 1)
            max_H = max(max_H, H)
            max_HS = max(max_HS, HS)
            max_HT = max(max_HT, HT)
            max_gS = max(max_gS, gS)
            max_gT = max(max_gT, gT)
            max_qxi = max(max_qxi, qxi)

assert checked == 52, checked


# Exact minimax. Denominator 2240 contains 47/160, 1/4, and all strip endpoints.
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
            # If Delta=max(rho,3*eta), then
            # d <= 2*rho + eta <= 7*Delta/3.
            Delta = F(3, 7) * d
            Ex -= Delta
        else:
            if min(Es, Ek, Ex) > low_core_best[0]:
                low_core_best = (min(Es, Ek, Ex), (theta, phi, chi))

        E = min(Es, Ek, Ex)
        if E > best[0]:
            best = (E, (theta, phi, chi, Es, Ek, Ex))

assert low_core_best[0] == F(11, 20), low_core_best
assert best == (
    F(47, 80),
    (
        F(47, 160),
        F(1, 4),
        F(27, 80),
        F(47, 80),
        F(101, 160),
        F(47, 80),
    ),
), best

# Equality-profile arithmetic for the new envelope.
theta = F(47, 160)
phi = F(1, 4)
chi = F(27, 80)
d = chi - F(1, 4)
Delta = F(3, 7) * d
rho = Delta
eta = Delta / 3
eta_each = eta / 2
Jexp = chi - 2 * rho - eta
assert d == F(7, 80)
assert Delta == F(3, 80)
assert rho == F(3, 80)
assert eta == F(1, 80)
assert eta_each == F(1, 160)
assert Jexp == F(1, 4)
assert 3 * phi - F(1, 8) - Delta == F(47, 80)
assert 2 * theta == F(47, 80)
assert F(9, 16) < F(47, 80)
assert F(11, 20) < F(47, 80)
assert F(19, 32) - F(47, 80) == F(1, 160)

# Freeze theorem boundary after result.md exists in the same branch/PR.
result = (ROOT / "stages/stage14/14-s7-34/result.md").read_text()
for token in (
    "STAGE14_S7_34=COMPLETE_XI_FOURTH_POWER_ROOT_GCD_TRANSFER_AND_47_80_PROMOTION",
    "XI_COMMON_ROOT_GCD_FOURTH_POWER_DIVIDES_QXI=true",
    "XI_H_DYADIC_COMPLETE_COUNT_EXPONENT=3phi-1/8-3eta",
    "NONPROPORTIONAL_FORCED_SAVING=3*(chi-1/4)/7",
    "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=47/80",
    "IMPROVEMENT_OVER_PREVIOUS_19_32=1/160",
    "FORTY_SEVEN_EIGHTIETHS_SATURATION_THETA=47/160",
    "FORTY_SEVEN_EIGHTIETHS_SATURATION_PHI=1/4",
    "FORTY_SEVEN_EIGHTIETHS_SATURATION_H_EXPONENT=1/80",
    "FORTY_SEVEN_EIGHTIETHS_SATURATION_SELECTED_XI_GCD_EXPONENT=3/80",
    "REMAINING_RECEIVER=FortySevenEightiethsExtraXiResidualGcdJointCoreLinearFactorIncidence",
    "S7_34_AUXILIARY_H_NEEDED=false",
    "NEXT=Stage14-s7-35",
):
    assert token in result, token

print("Stage14-s7-34 fourth-power root transfer audit: PASS")
print("finite physical pairs checked:", checked)
print("nontrivial H packets:", h_nontrivial)
print("max H, HS, HT:", max_H, max_HS, max_HT)
print("max gS, gT, q_xi:", max_gS, max_gT, max_qxi)
print("low-core max:", low_core_best)
print("whole-strip max:", best)
print("new saving over 19/32:", F(1, 160))
