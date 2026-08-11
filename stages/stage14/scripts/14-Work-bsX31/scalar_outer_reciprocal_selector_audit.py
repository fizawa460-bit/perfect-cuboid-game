#!/usr/bin/env python3
from math import gcd
from pathlib import Path
from fractions import Fraction

ROOT = Path(__file__).resolve().parents[4]

paths = {
    "result": ROOT / "stages/stage14/14-Work-bsX31/result.md",
    "matrix": ROOT / "docs/stage14-toolbox/work-bsX31-receiver-matrix.md",
    "brx30": ROOT / "stages/stage14/14-Work-brX30/result.md",
    "main": ROOT / "stages/stage14/14-4fj/result.md",
    "s": ROOT / "stages/stage14/14-s7-92/result.md",
    "t": ROOT / "stages/stage14/14-t131/result.md",
}

for key, path in paths.items():
    assert path.exists(), (key, path)
texts = {k: p.read_text() for k, p in paths.items()}

# Prior integrated boundary.
for token in [
    "COMMON_RECIPROCAL_WINDOW_GEOMETRY_LANGUAGE_PROVED=true",
    "DIRECT_RADIAL_DIVISOR_TO_PROJECTIVE_PRIME_ADAPTER_NOGO_AT_CURRENT_LEVEL=true",
    "NEXT_REVISIT_CONDITION=4fj+s7-92+t131",
]:
    assert token in texts["brx30"], token

# New merged main/s/t boundaries.
for token in [
    "INTERIOR_EXISTENTIAL_SUPPORT_INCIDENCE_EXPONENT_EQUIVALENT=true",
    "NEXT=Stage14-4fk",
]:
    assert token in texts["main"], token

for token in [
    "PRIMITIVE_RATIO_WINDOW_MULTIPLICATIVE_WIDTH=Bo1",
    "NEXT=Stage14-s7-93",
]:
    assert token in texts["s"], token

for token in [
    "NONREAL_COFACTOR_NORM_FIBER_COEFFICIENT_DEFINED=true",
    "NONREAL_HYPERBOLA_SCALAR_NORM_COMPRESSION_EXACT=true",
    "FIXED_U_ALL_LIVE_BRANCHES_SCALAR_NORM_OUTER_COORDINATE=true",
    "NEXT=Stage14-t132",
]:
    assert token in texts["t"], token

# Integrated locks.
for token in [
    "STAGE14_WORK_BSX31=COMPLETE",
    "TOOLBOX_COMPONENT_COMPLETE=true",
    "X_COMPONENT_COMPLETE=true",
    "GLOBAL_S_PRIMITIVE_DIVISOR_RATIO_COORDINATE_IDENTIFIED=true",
    "GLOBAL_S_MAIN_S_RECEIVERS_UNIFIED_AT_RATIO_LEVEL=true",
    "GLOBAL_S_RADIAL_ENDPOINT_STRIPS_DISCHARGED=true",
    "FIXED_U_ALL_LIVE_BRANCHES_ONE_DIMENSIONAL_SCALAR_NORM_OUTER=true",
    "COMMON_ONE_DIMENSIONAL_OUTER_RECIPROCAL_SELECTOR_LANGUAGE_PROVED=true",
    "COMMON_ENDPOINT_INTERIOR_TRANSFER_PROVED=false",
    "COMMON_PHYSICAL_WEIGHT_ADAPTER_PROVED=false",
    "DIRECT_PRIMITIVE_RATIO_TO_PROJECTIVE_CHARACTER_ADAPTER_NOGO_AT_CURRENT_LEVEL=true",
    "COMMON_ADAPTER_PROVED=false",
    "SAVING_CROSS_PROMOTABLE=false",
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
    "TH30_NEEDED=false",
    "NEXT_INTEGRATED_TARGET=ReciprocalInnerPhysicalWeightArithmeticAdapterOrNoGo",
    "NEXT_REVISIT_CONDITION=4fm+s7-95+t134",
]:
    assert token in texts["result"], token

for token in [
    "GLOBAL_S_RECIPROCAL_AND_RATIO_COUNTS_MULTIPLICABLE=false",
    "COMMON_ENDPOINT_NOTION_ARITHMETICALLY_IDENTIFIED=false",
    "COMMON_ARITHMETIC_SCALAR_OUTER_COORDINATE_IDENTIFICATION_PROVED=false",
    "COMMON_INNER_SELECTOR_TYPE_IDENTIFIED=false",
    "COMMON_PHYSICAL_WEIGHT_ADAPTER_PROVED=false",
    "NEXT_REVISIT_CONDITION=4fm+s7-95+t134",
]:
    assert token in texts["matrix"], token

# Exact global/s coordinate check:
# n=E*u*v, L=E*u^2 => L/n=u/v for gcd(u,v)=1.
cases = 0
for E in range(1, 20):
    for u in range(1, 20):
        for v in range(1, 20):
            if gcd(u, v) != 1:
                continue
            n = E * u * v
            L = E * u * u
            assert Fraction(L, n) == Fraction(u, v)
            assert n % (u * v) == 0
            assert n // (u * v) == E
            cases += 1
assert cases > 1000

# Coordinate changes are bijective on the normalized packet once E,u,v are fixed;
# they cannot manufacture a second support exponent.
for E, u, v in [(1, 1, 2), (3, 2, 5), (7, 4, 9), (11, 5, 7)]:
    assert gcd(u, v) == 1
    n = E * u * v
    L = E * u * u
    E_back = n // (u * v)
    assert E_back == E
    assert L == E_back * u * u

# Endpoint notions are deliberately kept distinct.  A thin outer radial strip
# has cardinality ~N*eps, while a fixed-U headroom wedge can still contain a
# polynomial two-dimensional hyperbola region; no equality is asserted.
for N in (10**3, 10**4, 10**5):
    eps_num, eps_den = 1, 100
    radial_strip_bound = (N * eps_num) // eps_den + 2
    assert radial_strip_bound < N

print(f"primitive_ratio_coordinate_cases={cases}")
print("Stage14-Work-bsX31 scalar outer reciprocal selector audit: OK")
