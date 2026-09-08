#!/usr/bin/env python3

DELTA = 472
D2 = 758
KDOT = 186

assert D2 + KDOT == 944
assert 2 * DELTA == 944

# Two smooth branches with contact order m=472:
# y^2-x^(2m)=(y-x^m)(y+x^m).
# The normalization image consists of pairs (u,v) with u-v divisible by t^m,
# so the normalization quotient has length m. Since x=t on each branch,
# dx=dt and the normalization map is immersive at both preimages.
m = 472
assert m == DELTA
two_branch_delta = m
two_branch_conductor_degree = 2 * m
two_branch_differential_ramification = 0
assert two_branch_delta == DELTA
assert two_branch_conductor_degree == 944
assert two_branch_differential_ramification == 0

# Unibranch model y^2=x^945 with x=t^2, y=t^945.
# The semigroup <2,945> has odd gaps 1,3,...,943.
gaps = list(range(1, 945, 2))
assert len(gaps) == DELTA
assert gaps[-1] == 943
unibranch_conductor_exponent = 944
# dx=2t dt and dy=945*t^944 dt, so the differential image ideal is (t).
unibranch_differential_ramification = min(2 - 1, 945 - 1)
assert unibranch_conductor_exponent == 944
assert unibranch_differential_ramification == 1

# Same defect and conductor scale, radically different tangent ramification.
assert two_branch_delta == len(gaps) == DELTA
assert two_branch_conductor_degree == unibranch_conductor_exponent == 944
assert two_branch_differential_ramification != unibranch_differential_ramification

print("PASS_EX1_05L_LOCAL_COUNTERMODELS")
