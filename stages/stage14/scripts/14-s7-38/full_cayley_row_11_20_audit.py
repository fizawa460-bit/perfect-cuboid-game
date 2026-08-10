#!/usr/bin/env python3
"""Deterministic audit for Stage14-s7-38."""
from fractions import Fraction as F
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def require(path: str, token: str) -> None:
    text = (ROOT / path).read_text()
    assert token in text, (path, token)


def crt2(a: int, m: int, b: int, n: int) -> int:
    assert gcd(m, n) == 1
    return (a + m * (((b - a) * pow(m, -1, n)) % n)) % (m * n)


require("stages/stage14/14-X12/result.md", "STAGE14_X12=COMPLETE_LOST_CORE_FOURTH_ROOT_COLUMN_COFACTOR_COUPLING_AND_71_128_PROMOTION")
require("stages/stage14/14-X12/result.md", "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=71/128")
require("stages/stage14/14-X12/result.md", "LOST_CORE_FOURTH_ROOT_DIVISOR_DIVIDES_COLUMN_COFACTOR_PRODUCT=true")
require("stages/stage14/14-s7-37/result.md", "PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=7/16")
require("stages/stage14/14-s7-36/result.md", "NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=19/34")
require("stages/stage14/14-s7-35/result.md", "XI_EXTRA_GCD_DIVIDES_ENDPOINT_OMEGA_PRODUCT=true")
require("stages/stage14/14-4cu/result.md", "JOINT_CORE_DIVIDES_ENDPOINT_LINEAR_PRODUCT=true")
require("stages/stage14/14-4cv/result.md", "STAGE14_4CV=COMPLETE_JOINT_CORE_ROW_COLUMN_COFACTOR_RECONSTRUCTION_AND_SEVEN_TWELFTHS_PROMOTION")

# Synthetic asymmetric row/column CRT: J carries both sign bits; the annulus
# extends only the Cayley row modulus.
synthetic = 0
for cells in ((5, 13, 17, 29), (13, 17, 29, 37), (17, 29, 37, 41)):
    jmm, jmp, jpm, jpp = cells
    J = jmm * jmp * jpm * jpp
    JCm, JCp = jmm * jmp, jpm * jpp
    JLm, JLp = jmm * jpm, jmp * jpp
    assert JCm * JCp == JLm * JLp == J
    assert gcd(JCm, JCp) == gcd(JLm, JLp) == 1
    for Am, Ap in ((43, 47), (53, 61), (73, 89)):
        assert gcd(Am, Ap) == gcd(Am * Ap, J) == 1
        CCm, CCp = JCm * Am, JCp * Ap
        CC = CCm * CCp
        assert CC % J == 0 and gcd(CCm, CCp) == 1
        for hm, hp in ((1, 1), (3, 5), (5, 9)):
            Lm, Lp = JLm * hm, JLp * hp
            Aend = (Lp + Lm) // 2
            Bend = (Lp - Lm) // 2
            assert Aend - Bend == Lm and Aend + Bend == Lp
            for M in (19, 123, 1001, 65537):
                nJ = crt2(M % JCm, JCm, (-M) % JCp, JCp)
                nC = crt2(M % CCm, CCm, (-M) % CCp, CCp)
                assert (nJ - M) % JCm == 0 and (nJ + M) % JCp == 0
                assert (nC - M) % CCm == 0 and (nC + M) % CCp == 0
                assert 0 <= nC < CC
                synthetic += 1
assert synthetic == 108


def strip_ok(t: F, p: F) -> bool:
    return F(3,16) <= t <= F(5,16) and F(1,8) <= p <= F(1,4) and 0 <= t-p <= F(1,8) and t+p >= F(3,8)


def combined_worst(t: F, p: F):
    d = 2*t + 2*p - 1
    lo = max(F(0), d/4)
    hi = F(1,8)
    assert lo <= hi
    candidates = {lo, hi}
    for s in (d/3, d/2):
        if lo <= s <= hi:
            candidates.add(s)
    s1 = (p-F(1,8))/3
    if lo <= s1 <= hi and 3*s1 <= d:
        candidates.add(s1)
    s2 = (p-F(1,8)+d)/6
    if lo <= s2 <= hi and 3*s2 >= d and 2*s2 <= d:
        candidates.add(s2)
    s3 = (p-F(1,8)+2*d)/8
    if lo <= s3 <= hi and 2*s3 >= d:
        candidates.add(s3)
    best = (F(-100), None, None)
    for s in candidates:
        EH = 3*p-F(1,8)-3*s
        ECRC = 2*p + max(F(0),3*s-d) + max(F(0),2*s-d)
        E = min(EH,ECRC)
        if E > best[0]:
            best = (E,s,(EH,ECRC,d))
    return best

D = 1792
best = (F(-1), None)
equalities = []
for nt in range(3*D//16, 5*D//16+1):
    theta = F(nt,D)
    for np in range(D//8, D//4+1):
        phi = F(np,D)
        if not strip_ok(theta,phi):
            continue
        Es = max(2*theta,1-2*theta)
        Ek = 3*theta-F(1,4)
        Ex = 3*phi-F(1,8)
        Eold = (18*phi-12*theta+5)/11
        EX12 = F(3,2)*phi-F(6,5)*theta+F(41,80)
        ECRC,sH,detail = combined_worst(theta,phi)
        E = min(Es,Ek,Ex,Eold,EX12,ECRC)
        payload=(theta,phi,sH,Es,Ek,Ex,Eold,EX12,ECRC,detail)
        if E>best[0]:
            best=(E,payload); equalities=[payload]
        elif E==best[0]:
            equalities.append(payload)

assert best[0] == F(61,112), best
assert len(equalities) == 1, equalities
assert equalities[0][0:3] == (F(61,224), F(1,4), F(3,112))

theta=F(61,224); phi=F(1,4)
chi=2*theta+2*phi-F(3,4); d=chi-F(1,4); sH=F(3,112)
eta_star=sH; eta_other=F(0); rho=2*eta_star
j=chi-4*eta_star-2*eta_other; cC=chi-2*sH
lost=chi-j; raw_col=F(1,4)-j; forced=lost/4
eff_col=raw_col-forced; row_lift=F(1,4)-cC; annulus=cC-j
assert chi==F(33,112) and d==F(5,112)
assert eta_star==F(3,112) and rho==F(3,56)
assert j==F(3,16) and cC==F(27,112)
assert lost==F(3,28) and raw_col==F(1,16) and forced==F(3,112)
assert eff_col==F(1,28) and row_lift==F(1,112)
assert annulus==F(3,56)==rho
assert 2*phi+eff_col+row_lift==F(61,112)
assert 3*phi-F(1,8)-3*sH==F(61,112)
assert 2*theta==F(61,112)
assert F(71,128)-F(61,112)==F(9,896)
assert F(61,112)-F(1,2)==F(5,112)

result=(ROOT/"stages/stage14/14-s7-38/result.md").read_text()
for token in (
    "STAGE14_S7_38=COMPLETE_X12_COLUMN_DIVISOR_FULL_CAYLEY_ROW_CORE_RECONSTRUCTION_AND_61_112_PROMOTION",
    "MERGED_X12_71_128_IMPORTED=true",
    "X12_LOST_CORE_FOURTH_ROOT_COLUMN_SAVING_RETAINED=true",
    "FULL_CAYLEY_CORE_USED_FOR_ROW_CRT=true",
    "ROW_AND_COLUMN_REFINEMENTS_COMPATIBLE=true",
    "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=61/112",
    "IMPROVEMENT_OVER_PREVIOUS_71_128=9/896",
    "CURRENT_GAP_TO_SQRT=5/112",
    "SIXTYONE_112_SATURATION_THETA=61/224",
    "SIXTYONE_112_SATURATION_PHI=1/4",
    "SIXTYONE_112_JOINT_CORE_EXPONENT=3/16",
    "SIXTYONE_112_CAYLEY_CORE_EXPONENT=27/112",
    "SIXTYONE_112_EFFECTIVE_COLUMN_SUPPORT_EXPONENT=1/28",
    "SIXTYONE_112_ROW_CRT_LIFT_EXPONENT=1/112",
    "SIXTYONE_112_CAYLEY_ONLY_ANNULUS_EXPONENT=3/56",
    "REMAINING_RECEIVER=SixtyOneOneHundredTwelfthsSingleCrossRootCayleyAnnulusEffectiveColumnTinyRowLiftIncidence",
    "S7_38_AUXILIARY_H_NEEDED=false",
    "NEXT=Stage14-s7-39",
):
    assert token in result, token

print("Stage14-s7-38 X12 + full Cayley-row audit: PASS")
print("synthetic asymmetric row/column CRT checks:", synthetic)
print("whole-strip maximum:", best)
print("unique equality:", equalities[0])
print("chi, eta_star, rho, j, c_C:", chi, eta_star, rho, j, cC)
print("lost/raw/forced/effective/row/annulus:", lost, raw_col, forced, eff_col, row_lift, annulus)
print("current whole-family exponent:", F(61,112))
print("saving over 71/128:", F(9,896))
print("gap to sqrt:", F(5,112))
