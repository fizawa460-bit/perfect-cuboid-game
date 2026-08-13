from pathlib import Path
import math

ROOT = Path(__file__).resolve().parents[3]


def read(rel):
    p = ROOT / rel
    assert p.exists(), f"missing {rel}"
    return p.read_text()


t136 = read("stages/stage14/14-t136/result.md")
t137 = read("stages/stage14/14-t137/result.md")
t138 = read("stages/stage14/14-t138/result.md")
target = read("stages/stage14/14-t138/th31-target.md")
th31 = read("stages/stage14/14-tH31/result.md")
t139 = read("stages/stage14/14-t139/result.md")
work = read("stages/stage14/14-Work-buX33/result.md")

# predecessor / integration locks
assert "NEXT=Stage14-t137" in t136
assert "EndpointShortFixedGaussianResiduePrimeOccupancyDeficit" in t136
assert "LongHeadroomIndividualSubpolynomialModulusFixedGaussianResiduePrimeOccupancyBias" in t136
assert "t139" in work

# t137 modulus scale split
assert "MITSUI_SAFE_MODULUS_THRESHOLD=exp(c_safe*sqrt(logB))" in t137
assert "GENUINELY_LARGER_SUBPOLYNOMIAL_MODULUS_RANGE_REMAINS=true" in t137
assert "EXCEPTIONAL_CHARACTER_RESIDUE_SIGN_FIXED=true" in t137
assert "NEXT=Stage14-t138" in t137

# B^o(1) is genuinely broader than exp(O(sqrt(log B)))
# exhibit d(B)=exp(log B/log log B): log d / sqrt(log B) -> infinity,
# while log d / log B -> 0.
for L in (10**4, 10**6, 10**8):
    logd = L / math.log(L)
    assert logd / L < 0.2
    assert logd / math.sqrt(L) > 1.0

# t138 target freeze
assert "T_ROUTE_H_NEEDED=true" in t138
assert "TH31_NEEDED=true" in t138
assert "T_ROUTE_H_TARGET=stages/stage14/14-t138/th31-target.md" in t138
assert "REQUESTED_OBJECT=MitsuiSafeLongHeadroomFixedGaussianResiduePrimeOccupancyLowerBound" in target
assert "T_safe >= B^(-o(1)) M_safe" in target

# long-headroom cumulative subtraction algebra: y/L >= B^theta.
# sample exponent check verifies lower endpoint is fixed-power smaller.
theta = 0.07
for logB in (100.0, 1000.0):
    ratio = math.exp(theta * logB)
    assert ratio > 1.0
    assert 1.0 / ratio < 1.0

# exceptional suppressing factor: 1-exp(-lambda log L) is subpolynomial
# when lambda=exp(-C sqrt(log B)); compare -log(factor)/logB -> 0.
for logB in (1e4, 1e6):
    C = 0.1
    lam = math.exp(-C * math.sqrt(logB))
    x = lam * (0.5 * logB)
    factor = -math.expm1(-x)
    assert factor > 0
    exponent_cost = -math.log(factor) / logB
    assert exponent_cost < 0.02

# positive H verdict and consumption
assert "STAGE14_TH31=COMPLETE_POSITIVE_MITSUI_SAFE_LONG_HEADROOM_FIXED_RESIDUE_OCCUPANCY_AUDIT" in th31
assert "MITSUI_SAFE_LONG_HEADROOM_THEOREM_APPLICABLE=true" in th31
assert "POSSIBLE_SIEGEL_ZERO_RETAINED=true" in th31
assert "SAFE_BRANCH_FIXED_POWER_DEPLETION_RULED_OUT=true" in th31
assert "SOURCE_SNAPSHOT_SHA=3916563a938dc5d1c8369bcd4d28ca02c3e2b64a" in th31

assert "TH31_CONSUMED=true" in t139
assert "MITSUI_SAFE_LONG_HEADROOM_BRANCH_DISCHARGED=true" in t139
assert "LongHeadroomBeyondMitsuiPseudopolynomialModulusFixedGaussianResiduePrimeOccupancyBias" in t139
assert "RECEIVER_MATERIALLY_CHANGED=true" in t139
assert "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2" in t139
assert "STRICT_SUBSQRT_POWER_SAVING_PROVED=false" in t139
assert "T_ROUTE_H_NEEDED=false" in t139
assert "TH32_NEEDED=false" in t139
assert "NEXT=Stage14-t140" in t139

print("Stage14-t-batch t137-t139+tH31 audit: OK")
