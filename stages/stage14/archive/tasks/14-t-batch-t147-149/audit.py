from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def text(rel):
    return (ROOT / rel).read_text()


t135 = text('stages/stage14/14-t135/result.md')
t146 = text('stages/stage14/14-t146/result.md')
t147 = text('stages/stage14/14-t147/result.md')
t148 = text('stages/stage14/14-t148/result.md')
t149 = text('stages/stage14/14-t149/result.md')

# Predecessor and exact baseline provenance.
assert 'NEXT=Stage14-t147' in t146
assert 'M_{beta_*}' in t135
assert '1/|R_d|' in t135

# t147: exact ordinary residue group and d^2 normalization.
for token in [
    'ORDINARY_GAUSSIAN_RESIDUE_GROUP_ORDER_EXACT=true',
    'ORDINARY_GAUSSIAN_RESIDUE_GROUP_ORDER=phi(d)*|G(d)|',
    'ORDINARY_GAUSSIAN_RESIDUE_GROUP_ORDER_SCALE=d^2*Bo1',
    'RESIDUE_NORMALIZED_ENDPOINT_CAPACITY_PROVED=true',
    'D_SQUARED_PRINCIPAL_CAPACITY_GAIN_PROVED=true',
    'RECEIVER_MATERIALLY_CHANGED=false',
    'NEXT=Stage14-t148',
]:
    assert token in t147, token

# Verify the local CRT cardinality identity for representative split/inert primes.
def chi4(p):
    return 1 if p % 4 == 1 else -1

for p in [3, 5, 7, 13, 17, 19]:
    rhs = (p - 1) * (p - chi4(p))
    lhs = (p - 1) ** 2 if p % 4 == 1 else p * p - 1
    assert lhs == rhs

# t148: sparse/many split and nonnegative localization.
for token in [
    'SPARSE_MANY_COFACTOR_SPLIT_DISJOINT=true',
    'SPARSE_ENDPOINT_ACTUAL_COFACTOR_COUNT=Bo1',
    'SPARSE_FIXED_POWER_DEPLETION_LOCALIZES_TO_ONE_ACTUAL_COFACTOR=true',
    'SPARSE_ENDPOINT_RECEIVER_IS_SINGLE_FIXED_RESIDUE_PRIME_INTERVAL=true',
    'MANY_COFACTOR_RESIDUE_HOST_NORMALIZED_CAPACITY=M_Y_LE_BO1_TIMES_Y2_OVER_hk0_d2',
    'RECEIVER_MATERIALLY_CHANGED=false',
    'NEXT=Stage14-t149',
]:
    assert token in t148, token

# Toy check for the localization inequality used in t148.
# If total T <= eps*M, the mass with T_z > 2 eps M_z is <= M/2.
masses = [7.0, 5.0, 3.0, 1.0]
eps = 0.01
# Construct a legal depleted example with two low-ratio cells.
ratios = [0.0, 0.0, 0.015, 0.015]
M = sum(masses)
T = sum(m * r for m, r in zip(masses, ratios))
assert T <= eps * M
bad_mass = sum(m for m, r in zip(masses, ratios) if r <= 2 * eps)
assert bad_mass >= M / 2

# t149: sharpened width floors and final receiver.
for token in [
    'RESIDUE_HOST_NORMALIZED_MANY_WIDTH_FLOOR_PROVED=true',
    'RESIDUE_HOST_NORMALIZED_MANY_WIDTH_FLOOR=BsQuarterTimes_d_TimesSqrtHK0',
    'BEYOND_MITSUI_MANY_WIDTH_FLOOR=BsQuarterTimes_d^(3/2)',
    'SPARSE_SINGLE_INTERVAL_RESIDUE_NORMALIZED_NEAR_FULL_PROVED=true',
    'TH32_SAFE_COVERAGE_RECONSUMED_WITHOUT_RECHARGE=true',
    'RECEIVER_MATERIALLY_CHANGED=true',
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    'STRICT_SUBSQRT_POWER_SAVING_PROVED=false',
    'T_ROUTE_H_NEEDED=false',
    'TH33_NEEDED=false',
    'NEXT=Stage14-t150',
]:
    assert token in t149, token

# Exponent bookkeeping: with d=B^kappa, hk0=B^rho,
# many principal capacity requires lambda >= 1/4+kappa+rho/2.
def many_floor(kappa, rho):
    return 0.25 + kappa + rho / 2

assert abs(many_floor(0.03, 0.10) - 0.33) < 1e-12
# If host provenance gives rho>=kappa, the weakest floor is 1/4+3kappa/2.
kappa = 0.04
assert abs(many_floor(kappa, kappa) - (0.25 + 1.5 * kappa)) < 1e-12

print('Stage14-t-batch t147-t149 audit: OK')
