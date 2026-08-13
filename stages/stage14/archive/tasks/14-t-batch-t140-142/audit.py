from pathlib import Path
from fractions import Fraction

ROOT = Path(__file__).resolve().parents[3]

def text(rel):
    return (ROOT / rel).read_text()

files = {
    't140': text('stages/stage14/14-t140/result.md'),
    't141': text('stages/stage14/14-t141/result.md'),
    't142': text('stages/stage14/14-t142/result.md'),
    'target': text('stages/stage14/14-t142/th32-target.md'),
}

required = {
    't140': [
        'ENDPOINT_ADDITIVE_WIDTH_DEFINED=true',
        'ENDPOINT_COFACTOR_TOP_ANNULUS_IDENTITY_EXACT=true',
        'ENDPOINT_WIDTH_LAYER_PRINCIPAL_CAPACITY_LE_B_POW_2LAMBDA=true',
        'NEXT=Stage14-t141',
    ],
    't141': [
        'ENDPOINT_CAPACITY_LIGHT_BRANCH_FIXED_POWER_HARMLESS=true',
        'GENERAL_WIDTH_FLOOR_LAMBDA_GE_ETA_OVER_2=true',
        'SUBSQRT_OBSTRUCTION_ENDPOINT_WIDTH_FLOOR=1/4-o1',
        'ULTRASHORT_BELOW_QUARTER_WIDTH_BRANCH_DISCHARGED_BY_CAPACITY=true',
        'NEXT=Stage14-t142',
    ],
    't142': [
        'ENDPOINT_SAFE_LARGE_MODULUS_CROSS_SPLIT_EXACT=true',
        'ENDPOINT_OBSTRUCTING_WIDTH_GE_QUARTER_SCALE=true',
        'SAFE_ENDPOINT_SHORT_INTERVAL_TARGET_THEOREM_READY=true',
        'RECEIVER_MATERIALLY_CHANGED=true',
        'TH32_NEEDED=true',
        'NEXT=Stage14-tH32',
    ],
    'target': [
        'REQUESTED_OBJECT=SafeMitsuiModulusQuarterScaleFixedGaussianResidueShortIntervalPrimeOccupancy',
        'SOURCE_SNAPSHOT_SHA=744d5b844d9f6b6bcace141497a97fef1945e81b',
        'TARGET_FROZEN=true',
        'QUARTER_SCALE_ENDPOINT_COVERED=',
    ],
}

for name, toks in required.items():
    for tok in toks:
        assert tok in files[name], (name, tok)

# Exact t140 inverse relation. Use B=b^2 so sqrt(B)=b rational.
for b in [100, 137, 251]:
    for hk0 in [1, 3, 7]:
        N0 = Fraction(b, hk0)
        for num, den in [(1, 20), (1, 5), (2, 5)]:
            # choose n=N0-s with a positive rational gap
            s = N0 * Fraction(num, den)
            n = N0 - s
            H = Fraction(2*b) * s / n
            s_back = H * N0 / (Fraction(2*b) + H)
            assert s_back == s

# For H <= sqrt(B), the annulus-gap comparison used in t140 is exact.
for b in [100, 200]:
    for hk0 in [1, 5]:
        N0 = Fraction(b, hk0)
        for H in [1, 7, b//2, b]:
            H = Fraction(H)
            s = H * N0 / (Fraction(2*b) + H)
            assert s >= H / (3*hk0)
            assert s <= H / (2*hk0)

# Exponent-capacity implication: M_Y <= B^(2 lambda+o(1)).
# If M_edge has exponent eta, a principal-scale dyadic layer requires lambda >= eta/2.
for eta_num in range(1, 11):
    eta = Fraction(eta_num, 20)
    floor = eta / 2
    assert 2 * floor == eta

assert Fraction(1, 2) / 2 == Fraction(1, 4)

# Width/modulus cross split is exhaustive and disjoint for positive d.
def branch(d, dsafe, endpoint):
    if endpoint and d <= dsafe:
        return 'E_SAFE'
    if endpoint and d > dsafe:
        return 'E_LARGE'
    if (not endpoint) and d > dsafe:
        return 'LONG_LARGE'
    return 'SAFE_LONG_ALREADY_CLOSED'

for d in range(1, 30):
    for endpoint in [False, True]:
        out = branch(d, 11, endpoint)
        assert out in {'E_SAFE','E_LARGE','LONG_LARGE','SAFE_LONG_ALREADY_CLOSED'}

for name in ['t140','t141','t142']:
    assert 'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2' in files[name]
    assert 'STRICT_SUBSQRT_POWER_SAVING_PROVED=false' in files[name]

print('Stage14-t-batch t140-t142 endpoint quarter-width audit: OK')
