from pathlib import Path
from math import prod

ROOT = Path(__file__).resolve().parents[3]


def text(rel):
    return (ROOT / rel).read_text()


t149 = text('stages/stage14/14-t149/result.md')
t150 = text('stages/stage14/14-t150/result.md')
t151 = text('stages/stage14/14-t151/result.md')
t152 = text('stages/stage14/14-t152/result.md')
t147 = text('stages/stage14/14-t147/result.md')
t144 = text('stages/stage14/14-t144/result.md')
th32 = text('stages/stage14/14-tH32/result.md')

assert 'NEXT=Stage14-t150' in t149
assert 'ORDINARY_GAUSSIAN_RESIDUE_GROUP_ORDER_EXACT=true' in t147
assert 'HK0_EQUALS_ETA_EPSILON_M=true' in t144
assert 'KAI_MITSUI_NEAR_FULL_SHORT_INTERVAL_THRESHOLD' in th32

for token in [
    'ENDPOINT_DYADIC_NORM_THICKNESS_LE_Y_OVER_2HK0=true',
    'FIXED_RESIDUE_COFACTOR_IS_SINGLE_AFFINE_GAUSSIAN_LATTICE=true',
    'GAUSSIAN_ANNULUS_LATTICE_AREA_TERM=Y_over_hk0_d2',
    'PER_NORM_BO1_REPRESENTATION_LOSS_REMOVED=true',
    'RECEIVER_MATERIALLY_CHANGED=false',
    'NEXT=Stage14-t151',
]:
    assert token in t150, token

for token in [
    'DOUBLE_RESIDUE_NORMALIZED_CAPACITY_PROVED=true',
    'DOUBLE_RESIDUE_AREA_TERM=Y2_over_qd_hk0_d2',
    'DOUBLE_RESIDUE_BOUNDARY_TERM=Y_Bquarter_over_qd_d_sqrtHK0',
    'DOUBLE_RESIDUE_SINGLETON_TERM=Y_over_qd',
    'LATTICE_BOUNDARY_NEW_FIXED_POWER_RECEIVER=false',
    'SPARSE_NEARFULL_NECESSARY_CONDITION=Y_over_qd_GE_BsHalfMinusO1',
    'NEXT=Stage14-t152',
]:
    assert token in t151, token

for token in [
    'GAUSSIAN_LATTICE_AREA_MANY_WIDTH_FLOOR_PROVED=true',
    'GAUSSIAN_LATTICE_AREA_MANY_WIDTH_FLOOR_SCALE=BsQuarterTimes_d2_TimesSqrtHK0',
    'BEYOND_MITSUI_D_FIVE_HALVES_WIDTH_GAIN_PROVED=true',
    'RECEIVER_MATERIALLY_CHANGED=true',
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    'STRICT_SUBSQRT_POWER_SAVING_PROVED=false',
    'T_ROUTE_H_NEEDED=false',
    'TH33_NEEDED=false',
    'NEXT=Stage14-t153',
]:
    assert token in t152, token

# Exact local order check for odd squarefree d.
def chi4(p):
    return 1 if p % 4 == 1 else -1


def q_order(primes):
    return prod((p - 1) * (p - chi4(p)) for p in primes)


def phi_square(primes):
    return prod((p - 1) ** 2 for p in primes)

for primes in ([3], [5], [3, 5], [5, 13], [3, 7, 11]):
    q = q_order(primes)
    assert q >= phi_square(primes)

# Endpoint norm map derivative bound:
# n(H)=2B/(hk*(2sqrt(B)+H)), so |n'|<=1/(2hk).
def n_of_h(B, hk, H):
    return 2 * B / (hk * (2 * B ** 0.5 + H))

for B, hk, Y in [(10**8, 10, 100), (10**12, 37, 10**4), (10**16, 101, 10**6)]:
    delta = n_of_h(B, hk, Y) - n_of_h(B, hk, 2 * Y)
    assert delta <= Y / (2 * hk) + 1e-9

# Algebra of the new area width floor:
# Y^2/(q*hk*d^2) >= B^(1/2) => Y >= B^(1/4)*d*sqrt(q*hk).
B = 10**16
d = 15
hk = 225
q = q_order([3, 5])
Y = B ** 0.25 * d * (q * hk) ** 0.5
lhs = Y * Y / (q * hk * d * d)
assert abs(lhs / (B ** 0.5) - 1.0) < 1e-10

print('Stage14-t-batch t150-t152 audit: OK')
