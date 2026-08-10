#!/usr/bin/env python3
"""Stage14-s7-37 deterministic audit on latest main through merged X11.

The new s-route statement is stronger than merged X11 on the proportional branch:
if K=Kx*Ky is the same-side part of oddpart(gcd(z1,z2)), then

    gcd(K,q_xi)=1,
    K^2 | u_res.

On L_-=0, K*H=B^(1/8+o(1)); hence K^2|u_res forces
eta(H)>=1/8-theta+phi.  The merged xi fourth-power complete count then gives
E_prop<=3theta-1/2<=7/16.  Current main is already 19/34 from merged X11,
so this stage strengthens the proportional local theorem without a new global exponent.
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
    "s733_s737",
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


require(
    "stages/stage14/14-s7-36/result.md",
    "STAGE14_S7_36=COMPLETE_ROW_COLUMN_REOPTIMIZATION_AND_9_16_PROPORTIONAL_BARRIER_PROMOTION",
)
require(
    "stages/stage14/14-s7-36/result.md",
    "NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=19/34",
)
require(
    "stages/stage14/14-s7-34/result.md",
    "XI_COMMON_ROOT_GCD_FOURTH_POWER_DIVIDES_QXI=true",
)
require(
    "stages/stage14/14-4ci/result.md",
    "COMMON_Z_SCALE_SQUARE_DIVIDES_QK=true",
)
require(
    "stages/stage14/14-X11/result.md",
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=19/34",
)
require(
    "stages/stage14/14-X11/result.md",
    "PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=13/24",
)


# Finite physical check of the exact residual transfer.
groups = ch.make_groups(600)
checked = 0
nontrivial_same = 0
max_T0 = max_K = max_H = max_Kx = max_Ky = 1
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
            C, u_res, v_res = d["triple"]
            q_xi = C * v_res

            Kx = oddpart(gcd(a["x"], b["x"]))
            Ky = oddpart(gcd(a["y"], b["y"]))
            HS = oddpart(gcd(b["x"], a["y"]))
            HT = oddpart(gcd(a["x"], b["y"]))
            K = Kx * Ky
            H = HS * HT
            T0 = oddpart(gcd(a["z"], b["z"]))

            cells = (Kx, Ky, HS, HT)
            for r in range(4):
                for s in range(r + 1, 4):
                    assert gcd(cells[r], cells[s]) == 1
            assert T0 == Kx * Ky * HS * HT
            assert gcd(K, H) == 1

            # New s-route exact theorem.
            assert gcd(K, q_xi) == 1
            assert gcd(K, C) == 1
            assert u_res % (K * K) == 0

            checked += 1
            nontrivial_same += int(K > 1)
            max_T0 = max(max_T0, T0)
            max_K = max(max_K, K)
            max_H = max(max_H, H)
            max_Kx = max(max_Kx, Kx)
            max_Ky = max(max_Ky, Ky)

assert checked == 52, checked


# Pure root arithmetic: the four cells are pairwise coprime and multiply to odd gcd.
root_checks = 0
for x1 in range(1, 13):
    for y1 in range(1, 13):
        if gcd(x1, y1) != 1:
            continue
        for x2 in range(1, 13):
            for y2 in range(1, 13):
                if gcd(x2, y2) != 1:
                    continue
                Kx = oddpart(gcd(x1, x2))
                Ky = oddpart(gcd(y1, y2))
                HS = oddpart(gcd(x2, y1))
                HT = oddpart(gcd(x1, y2))
                cells = (Kx, Ky, HS, HT)
                for r in range(4):
                    for s in range(r + 1, 4):
                        assert gcd(cells[r], cells[s]) == 1
                assert oddpart(gcd(x1 * y1, x2 * y2)) == Kx * Ky * HS * HT
                root_checks += 1


# Exponent ledger.  Current main nonproportional 19/34 remains global.
D = 1632
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

        # On L_-=0, kappa+eta=1/8 and K^2|u_res with
        # u_res<=B^(2theta-2phi) imply eta>=1/8-theta+phi.
        # Thus E_H<=3phi-1/8-3eta<=3theta-1/2.
        Ekprop = 3 * theta - F(3, 8)
        EHprop = 3 * theta - F(1, 2)
        Eprop = min(Es, Ex, Ekprop, EHprop)
        if Eprop > best_prop[0]:
            best_prop = (Eprop, (theta, phi, chi, Es, Ex, Ekprop, EHprop))
        if Eprop == F(7, 16):
            prop_saturation.append((theta, phi, chi))

assert best_nonprop == (
    F(19, 34),
    (
        F(19, 68), F(1, 4), F(21, 68), F(19, 34),
        F(10, 17), F(5, 8), F(19, 34),
    ),
), best_nonprop
assert best_prop[0] == F(7, 16), best_prop
assert prop_saturation
assert {t for t, _, _ in prop_saturation} == {F(5, 16)}
assert min(p for _, p, _ in prop_saturation) == F(3, 16)
assert max(p for _, p, _ in prop_saturation) == F(1, 4)

# Proportional equality bookkeeping.
theta = F(5, 16)
for phi in (F(3, 16), F(11, 48), F(1, 4)):
    mu = 2 * theta - 2 * phi
    kappa = mu / 2
    eta = F(1, 8) - kappa
    assert eta == phi - F(3, 16)
    assert 3 * phi - F(1, 8) - 3 * eta == F(7, 16)
    assert 2 * kappa == mu

assert F(7, 16) < F(1, 2)
assert F(7, 16) < F(13, 24)
assert F(19, 34) - F(1, 2) == F(1, 17)
assert max(best_nonprop[0], best_prop[0]) == F(19, 34)


result = (ROOT / "stages/stage14/14-s7-37/result.md").read_text()
for token in (
    "STAGE14_S7_37=COMPLETE_PROPORTIONAL_SAMESIDE_RESIDUAL_TRANSFER_AND_19_34_REFINEMENT",
    "MERGED_X11_19_34_IMPORTED=true",
    "PROPORTIONAL_COMMON_Z_FOUR_ROOT_GCD_DECOMPOSITION_PROVED=true",
    "SAMESIDE_ROOT_GCD_COPRIME_TO_QXI=true",
    "SAMESIDE_ROOT_GCD_SQUARE_DIVIDES_U_RES=true",
    "PROPORTIONAL_CROSS_ROOT_LOWER_EXPONENT=1/8-theta+phi",
    "PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=7/16",
    "MERGED_X11_PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=13/24",
    "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=19/34",
    "S7_37_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false",
    "CURRENT_GAP_TO_SQRT=1/17",
    "REMAINING_RECEIVER=NineteenThirtyFourthsSingleCrossRootJointCoreTwinShortRowColumnIncidence",
    "S7_37_AUXILIARY_H_NEEDED=false",
    "NEXT=Stage14-s7-38",
):
    assert token in result, token

print("Stage14-s7-37 same-side residual refinement audit: PASS")
print("finite physical pairs checked:", checked)
print("finite pairs with nontrivial same-side K:", nontrivial_same)
print("max T0, K, H, Kx, Ky:", max_T0, max_K, max_H, max_Kx, max_Ky)
print("small-root four-cell checks:", root_checks)
print("new s-route proportional bound:", best_prop)
print("current nonproportional/global bound:", best_nonprop)
print("merged X11 proportional bound:", F(13, 24))
print("current whole-family exponent:", F(19, 34))
print("gap to sqrt:", F(1, 17))
