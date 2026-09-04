#!/usr/bin/env python3
import json
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages/stage35-ex/MAIN-STATE.json"
DOC = ROOT / "stages/stage35-ex/35ex-17/product-hypotenuse-successor-or-no-self-map.md"


def square(n: int) -> bool:
    return n >= 0 and isqrt(n) ** 2 == n


state = json.loads(STATE.read_text())
doc = DOC.read_text()

assert state["stage"] == "35-EX"
unit17 = state["completed_units"]["35EX-17"]
assert unit17["status"] in {
    "PROVISIONAL_EXACT_PRODUCT_HYPOTENUSE_NO_SELF_MAP_FREEZE_NO_CREDIT",
    "AUDITED_EXACT_PRODUCT_HYPOTENUSE_NO_SELF_MAP_FREEZE_NO_CREDIT",
}
assert unit17["product_hypotenuse_primitive_triple_inherited"] is True
assert unit17["canonical_two_triple_reconstruction_proved"] is False
assert unit17["natural_successor_P_T2_requires_new_square_obligations"] is True
assert unit17["natural_successor_T1_P_requires_new_square_obligations"] is True
assert unit17["strict_well_founded_same_type_height_decrease_proved"] is False
assert unit17["all_product_hypotenuse_descents_ruled_out_in_principle"] is False
assert unit17["infinite_descent_proved"] is False
assert unit17["audited_theorem_credit"] is False

for text in (
    "PRODUCT_HYPOTENUSE_CANONICAL_TWO_TRIPLE_RECONSTRUCTION=false",
    "CURRENT_PRODUCT_HYPOTENUSE_SELF_MAP_ROUTE=FROZEN_NO_CANONICAL_SAME_TYPE_SUCCESSOR",
    "NATURAL_SUCCESSOR_P_T2_REQUIRES_NEW_SQUARE_OBLIGATIONS=true",
    "NATURAL_SUCCESSOR_T1_P_REQUIRES_NEW_SQUARE_OBLIGATIONS=true",
    "STRICT_WELL_FOUNDED_SAME_TYPE_HEIGHT_DECREASE_PROVED=false",
    "ALL_PRODUCT_HYPOTENUSE_DESCENTS_RULED_OUT_IN_PRINCIPLE=false",
    "INFINITE_DESCENT_PROVED=false",
    "EXHAUSTIVE_VIEW_AUDIT",
    "BLIND_REDISCOVERY",
):
    assert text in doc

# Verify the two candidate identities on a deterministic primitive-source panel.
# These identities hold without assuming the hypothetical E1 square; E2 below is
# the raw E1 norm and is substituted algebraically for E^2.
checked = 0
product_triples = 0
for a in range(2, 31):
    for b in range(1, a):
        if gcd(a, b) != 1 or (a - b) % 2 != 1:
            continue
        U1, V1, W1 = a*a-b*b, 2*a*b, a*a+b*b
        for m in range(2, 61):
            for n in range(1, m):
                if gcd(m, n) != 1 or (m - n) % 2 != 1:
                    continue
                U2, V2, W2 = m*m-n*n, 2*m*n, m*m+n*n
                p = gcd(W1, V2)
                d = gcd(V1, W2)
                pd = p*d
                E2 = W1*W1*W2*W2 - V1*V1*V2*V2
                assert E2 == (W1*U2)**2 + (U1*V2)**2

                # Candidate A=(P,T2): after removing a rational square factor.
                A_master_core = (V1*U2)**2 + E2
                A_master_alt = (U1*W2)**2 + 2*(V1*U2)**2
                assert A_master_core == A_master_alt

                A_e1_core = (W1*W2*U2)**2 + E2*V2*V2
                A_e1_alt = (W1*W2*W2)**2 - (V1*V2*V2)**2
                assert A_e1_core == A_e1_alt

                # Candidate B=(T1,P): likewise after removing a rational square.
                B_master_core = E2 + (U1*V2)**2
                B_master_alt = (W1*U2)**2 + 2*(U1*V2)**2
                assert B_master_core == B_master_alt

                B_e1_core = W1*W1*E2 + (U1*V1*V2)**2
                B_e1_alt = (W1*W1*W2)**2 - (V1*V1*V2)**2
                assert B_e1_core == B_e1_alt

                # Whenever the raw E1 norm is a square, reconstruct the exact
                # 35EX-14 product-hypotenuse primitive triple.
                if square(E2):
                    Pminus = W1*W2 - V1*V2
                    Pplus = W1*W2 + V1*V2
                    assert Pminus % pd == Pplus % pd == 0
                    Lminus = Pminus // pd
                    Lplus = Pplus // pd
                    assert square(Lminus) and square(Lplus)
                    x, y = isqrt(Lminus), isqrt(Lplus)
                    R, S = (y+x)//2, (y-x)//2
                    U3 = isqrt(E2) // pd
                    V3 = V1*V2 // pd
                    W3 = W1*W2 // pd
                    assert U3 == R*R-S*S
                    assert V3 == 2*R*S
                    assert W3 == R*R+S*S
                    assert U3*U3 + V3*V3 == W3*W3
                    assert gcd(U3, V3) == gcd(U3, W3) == gcd(V3, W3) == 1
                    product_triples += 1
                checked += 1

assert checked > 100000
assert product_triples > 0

for key in (
    "new_theorem_credit",
    "R29_PESCH_E1_closed",
    "R29_FIB2_closed",
    "J12_PARAMETRIC_closed",
    "stage35_closed",
    "perfect_cuboid_existence_claim",
    "perfect_cuboid_nonexistence_claim",
):
    assert state["claims"][key] is False

print("PASS STAGE35_EX_17_PRODUCT_HYPOTENUSE_NO_SELF_MAP_FREEZE")
