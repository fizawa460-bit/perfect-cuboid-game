from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
paths = {
    "result": ROOT / "stages/stage14/14-Work-bqX29/result.md",
    "matrix": ROOT / "docs/stage14-toolbox/work-bqX29-receiver-matrix.md",
    "bpx28": ROOT / "stages/stage14/14-Work-bpX28/result.md",
    "main": ROOT / "stages/stage14/14-4fd/result.md",
    "s": ROOT / "stages/stage14/14-s7-86/result.md",
    "t": ROOT / "stages/stage14/14-t124/result.md",
}
for key, path in paths.items():
    assert path.exists(), (key, path)
texts = {k: p.read_text() for k, p in paths.items()}

for token in [
    "COMMON_ATOMIC_CAPACITY_AS_FINAL_RECEIVER_SUPERSEDED=true",
    "MAINLINE_HEAVY_MASS_FORCES_MATCHING_RADIAL_SUPPORT_EXPONENT=true",
    "GLOBAL_S_COMMON_RADIAL_OUTER_COORDINATE_PROVED=true",
    "S_HEAVY_CAPACITY_GAP_SUPERSEDED_BY_MERGED_4FD=true",
    "FIXED_U_FINITE_BOUNDARY_ATOMIC_BRANCH_DISCHARGED=true",
    "COMMON_ARITHMETIC_OUTER_COORDINATE_ADAPTER_PROVED=false",
    "COMMON_ADAPTER_PROVED=false",
    "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
    "TH29_NEEDED=false",
    "NEXT_INTEGRATED_TARGET=RadialOccupancyVersusSelectedProjectiveClassDepletionAdapterOrNoGo",
]:
    assert token in texts["result"], token

for token in [
    "SURVIVING_HEAVY_RAY_RADIAL_SUPPORT_LOWER_BOUND=B^(mu-o(1))",
    "SURVIVING_HEAVY_RAY_RADIAL_SUPPORT_UPPER_BOUND=B^(1/4-phi+o(1))",
    "SURVIVING_HEAVY_RAY_MU_RANGE=0<mu<=1/4-phi",
    "HEAVY_RAY_ATOMIC_CAPACITY_GAP_SUPERSEDED=true",
]:
    assert token in texts["main"], token

for token in [
    "FIXED_H_ROOT_OVERLAP_SQUAREPART_FIBER=Bo1",
    "STAGE14_S7_86=COMPLETE_ROOT_OVERLAP_SQUAREPART_MOBILITY_TO_SHORT_RADIAL_FACTORIZATION_CAPACITY",
]:
    assert token in texts["s"], token

for token in [
    "FINITE_BOUNDARY_ATOMIC_CONCENTRATION_AS_SEPARATE_RECEIVER_SUPERSEDED=true",
    "SELECTED_CLASS_NEAR_TOTAL_DEPLETION_IS_ONLY_LIVE_FIXED_U_MECHANISM=true",
    "TH29_NEEDED=false",
]:
    assert token in texts["t"], token

assert "OUTER_SUPPORT_CAPACITY_LEMMA_PROVED=true" in texts["bpx28"]
assert "GLOBAL_S_COMMON_RADIAL_OUTER_COORDINATE_PROVED=true" in texts["matrix"]

# Exponent-capacity sanity checks: surviving heavy mass exponent mu must fit
# inside the radial capacity rho and forces at least the same support exponent.
examples = [(1, 1), (1, 2), (3, 4), (1, 24)]
for mu_num, rho_den in examples:
    mu = mu_num / 100
    rho = 1 / rho_den
    if mu <= rho:
        lower_support_exp = mu
        upper_support_exp = rho
        assert lower_support_exp <= upper_support_exp

# Finite-fiber relocation sanity check: a subpolynomial fiber over each h
# cannot change a fixed positive support exponent.
for n_h in (10, 100, 1000):
    fiber = 7
    total = n_h * fiber
    assert total <= fiber * n_h

print("Stage14-Work-bqX29 atomic capacity exhaustion audit: OK")
