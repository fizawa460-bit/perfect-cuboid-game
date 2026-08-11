#!/usr/bin/env python3
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

for rel, needle in {
    "stages/stage14/14-4dm/result.md": "COMMON_PAIRWISE_COVARIANCE_ZERO_CENTERED_RECENTERING_PROVED=true",
    "stages/stage14/14-s7-56/result.md": "PAIR_JOINT_OCCUPANCY_FIXED_POWER_DEFICIT_STRICT_SUBSQRT=true",
    "stages/stage14/14-s7-52/result.md": "SQRT_THREE_PROJECTION_SATURATION_REQUIRES_ALL_MARGINALS_INTERIOR=true",
    "stages/stage14/14-s7-54/result.md": "PAIRWISE_BRANCHES_POWER_EQUIVALENT=true",
}.items():
    assert needle in (ROOT / rel).read_text(), (rel, needle)


def avg(xs):
    return sum(xs, Fraction(0)) / len(xs)


def cov(xs, ys):
    ax, ay = avg(xs), avg(ys)
    return avg([(x-ax)*(y-ay) for x,y in zip(xs,ys)])

samples = [
    ([0,0,1,1,1,1], [0,1,0,1,1,1]),
    ([0,1,0,1,0,1], [0,0,1,1,0,1]),
    ([0,0,0,1,1,1], [1,0,0,1,1,0]),
]

for Araw, Braw in samples:
    A = [Fraction(x) for x in Araw]
    B = [Fraction(x) for x in Braw]
    mu = avg(A)
    one = [b for a,b in zip(A,B) if a == 1]
    zero = [b for a,b in zip(A,B) if a == 0]
    assert one and zero
    nu1, nu0 = avg(one), avg(zero)
    assert cov(A,B) == mu*(1-mu)*(nu1-nu0)
    assert max(cov(A,B), Fraction(0)) == mu*(1-mu)*max(nu1-nu0, Fraction(0))

result = (ROOT / "stages/stage14/14-4dn/result.md").read_text()
for needle in [
    "STAGE14_4DN=COMPLETE_ZERO_MODE_COFACTOR_COVARIANCE_CONDITIONAL_UPLIFT_REDUCTION",
    "ZERO_MODE_COVARIANCE_TWO_SLICE_IDENTITY_PROVED=true",
    "ZERO_MODE_POSITIVE_OBSTRUCTION_EQUALS_POSITIVE_CONDITIONAL_UPLIFT=true",
    "FIXED_POWER_CONDITIONAL_UPLIFT_DEFICIT_STRICT_SUBSQRT=true",
    "CONDITIONAL_UPLIFT_FIXED_POWER_DEFICIT_PROVED_UNIFORMLY=false",
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    "NEXT_H_NEEDED=false",
]:
    assert needle in result, needle

print({"stage":"14-4dn","two_slice":True,"conditional_uplift":True,"current_exponent":"1/2","next":"Stage14-4do"})
