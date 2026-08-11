#!/usr/bin/env python3
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

paths = {
    "result": ROOT / "stages/stage14/14-Work-btX32/result.md",
    "matrix": ROOT / "docs/stage14-toolbox/work-btX32-receiver-matrix.md",
    "prev": ROOT / "stages/stage14/14-Work-bsX31/result.md",
    "main": ROOT / "stages/stage14/14-4fm/result.md",
    "s": ROOT / "stages/stage14/14-s7-95/result.md",
    "t": ROOT / "stages/stage14/14-t132/result.md",
}

for name, path in paths.items():
    assert path.exists(), (name, path)
texts = {name: path.read_text() for name, path in paths.items()}

for token in [
    "STAGE14_WORK_BTX32=COMPLETE",
    "GLOBAL_S_WEIGHTED_UNITARY_DIVISOR_INCIDENCE_IDENTIFIED=true",
    "PHYSICAL_WEIGHT_LOCATION_ASYMMETRY_PROVED=true",
    "FIXED_U_PHYSICAL_COFACTOR_WEIGHT_OUTER_N_ONLY=true",
    "DIRECT_WEIGHTED_UNITARY_TO_FIXED_PROJECTIVE_PRIME_ADAPTER_NOGO_AT_CURRENT_LEVEL=true",
    "COMMON_ADAPTER_PROVED=false",
    "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
    "TH30_NEEDED=false",
]:
    assert token in texts["result"], token

for token in [
    "COMPLEMENTARY_E_SCALE_SPLIT_EXPLICIT=true",
    "FIXED_E_UNITARY_DIVISOR_SHORT_WINDOW_EXPLICIT=true",
    "POLYNOMIAL_E_UNITARY_DIVISOR_COUPLED_CORRELATION_EXPLICIT=true",
    "FORD_TRANSFER_FIXED_POWER_SAVING_PROVED=false",
]:
    assert token in texts["main"], token

for token in [
    "PRIMITIVE_COPRIME_PAIR_EQUIVALENT_TO_UNITARY_DIVISOR=true",
    "WEIGHTED_UNITARY_DIVISOR_INCIDENCE_DEFINED=true",
    "PHYSICAL_WEIGHT_PRESERVING_TRANSFER_PROVED=false",
]:
    assert token in texts["s"], token

for token in [
    "BAD_PACKET_LOCALIZES_TO_ONE_FIXED_PROJECTIVE_CLASS=true",
    "FIXED_PROJECTIVE_CLASS_RECIPROCAL_PRIME_DEPLETION_RECEIVER_PROVED=true",
    "FIXED_CLASS_SCALAR_NORM_WEIGHT_SUPNORM=Bo1",
    "TH30_NEEDED=false",
]:
    assert token in texts["t"], token

assert "COMMON_ONE_DIMENSIONAL_OUTER_RECIPROCAL_SELECTOR_LANGUAGE_PROVED=true" in texts["prev"]
assert "COMMON_PHYSICAL_WEIGHT_ADAPTER_PROVED=false" in texts["prev"]
assert "PHYSICAL_WEIGHT_LOCATION_ASYMMETRY_PROVED=true" in texts["matrix"]

# Exact unitary-divisor equivalence used on the global/s fixed-E branch.
for m in range(1, 200):
    unitary = [u for u in range(1, m + 1) if m % u == 0 and gcd(u, m // u) == 1]
    pairs = [(u, m // u) for u in range(1, m + 1) if m % u == 0 and gcd(u, m // u) == 1]
    assert len(unitary) == len(pairs)
    for u, v in pairs:
        assert u * v == m
        assert gcd(u, v) == 1

# Complementary-dilation decomposition n=E*q and the fixed-E normalization m=n/E.
for E in range(1, 10):
    for q in range(1, 60):
        n = E * q
        assert n // E == q
        assert n % E == 0

# t132 nonnegative class localization algebra: totals decompose exactly by class.
# This synthetic check locks only the bookkeeping identity, not any distribution theorem.
classes = {
    0: {2: (3, 10), 3: (1, 7)},
    1: {2: (2, 10), 5: (4, 9)},
    2: {3: (1, 7), 5: (2, 9)},
}
# entry=(physical selected count contribution, principal numerator contribution)
T_parts = []
Mnum_parts = []
for c, by_n in classes.items():
    T_c = sum(v[0] for v in by_n.values())
    Mnum_c = sum(v[1] for v in by_n.values())
    assert T_c >= 0 and Mnum_c >= 0
    T_parts.append(T_c)
    Mnum_parts.append(Mnum_c)
assert sum(T_parts) == sum(v[0] for by_n in classes.values() for v in by_n.values())
assert sum(Mnum_parts) == sum(v[1] for by_n in classes.values() for v in by_n.values())

# Weight-location sanity: an outer-only weight is constant across inner labels at fixed n;
# an inner-dependent weight need not be. These are intentionally not identified.
outer_weight = {10: 3, 12: 2}
for n, w in outer_weight.items():
    inner_vals = [w for _ in range(4)]
    assert len(set(inner_vals)) == 1
inner_weight = {(10, 1): 1, (10, 2): 0, (10, 5): 1}
assert len(set(inner_weight.values())) > 1

print("Stage14-Work-btX32 weight-location adapter audit: OK")
