#!/usr/bin/env python3
from fractions import Fraction
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]

for rel, needle in {
    "stages/stage14/14-4dl/result.md": "PAIRWISE_SQRT_SATURATION_REQUIRES_RIJ=Bo0=true",
    "stages/stage14/14-s7-54/result.md": "PAIRWISE_BRANCHES_POWER_EQUIVALENT=true",
    "stages/stage14/14-s7-55/result.md": "PAIRWISE_PRINCIPAL_JOINT_DENSITY_DEFECT_PRESENT=true",
    "stages/stage14/14-s7-56/result.md": "PAIR_JOINT_OCCUPANCY_FIXED_POWER_DEFICIT_STRICT_SUBSQRT=true",
    "stages/stage14/14-s7-49/result.md": "EXACT_LOCAL_CENTERING_PROVED=true",
    "stages/stage14/14-s7-50/result.md": "FULL_CONDUCTOR_ENDPOINT_PROVED=true",
    "stages/stage14/14-X15/result.md": "THREE_COMPLETE_COORDINATE_SYSTEMS_FINITE_FIBER_EQUIVALENT=true",
    "stages/stage14/archive/docs/q-research/stage14-q11-nearmax-pythagorean-correlation-literature-radar.md": "DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0",
}.items():
    assert needle in (ROOT / rel).read_text(), (rel, needle)


def avg(v):
    return sum(v, Fraction(0)) / len(v)


def cov(x, y):
    ax, ay = avg(x), avg(y)
    return avg([(u-ax)*(v-ay) for u, v in zip(x, y)])

A = [Fraction(x) for x in (0,1,1,0,1,0)]
B = [Fraction(x) for x in (1,0,1,1,0,0)]
K = [Fraction(x) for x in (1,-1,0,1,-1,0)]
a = Fraction(1,5)
R = [a+k for k in K]
AR = [u*r for u, r in zip(A, R)]
AK = [u*k for u, k in zip(A, K)]
assert cov(AR, B) == a*cov(A, B) + cov(AK, B)

for xraw, yraw in [
    ((0,0,1,1),(0,1,1,1)),
    ((0,1,0,1),(1,0,1,0)),
    ((1,1,1,0),(1,1,0,0)),
]:
    x = [Fraction(t) for t in xraw]
    y = [Fraction(t) for t in yraw]
    joint = avg([u*v for u, v in zip(x, y)])
    assert max(cov(x, y), Fraction(0)) <= joint

result = (ROOT / "stages/stage14/14-4dm/result.md").read_text()
for needle in [
    "STAGE14_4DM=COMPLETE_POSITIVE_PAIRWISE_ZERO_MODE_COFACTOR_AND_MASKED_CENTERED_COVARIANCE_REDUCTION",
    "MERGED_S7_55_IMPORTED=true",
    "MERGED_Q11_COMPATIBLE=true",
    "NEGATIVE_PAIRWISE_COVARIANCE_IS_UPPER_BOUND_OBSTRUCTION=false",
    "COMMON_PAIRWISE_COVARIANCE_ZERO_CENTERED_RECENTERING_PROVED=true",
    "PAIRWISE_RECEIVER_EQUALS_ONLY_INVERSE_FRACTION_ERROR=false",
    "PAIRWISE_ZERO_MODE_COFACTOR_COVARIANCE_REMAINS=true",
    "PAIRWISE_MASKED_CENTERED_INVERSE_FRACTION_COVARIANCE_REMAINS=true",
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
    "NEXT_H_NEEDED=false",
]:
    assert needle in result, needle

print(json.dumps({
    "stage":"14-4dm",
    "s7_55_imported":True,
    "s7_56_compatible":True,
    "q11_compatible":True,
    "positive_pairwise_only":True,
    "zero_centered_recentering":True,
    "pairwise_fixed_power_branches":1,
    "current_exponent":"1/2",
    "strict_subsqrt_saving":False,
    "next_h_needed":False,
    "next":"Stage14-4dn"
}, sort_keys=True))
