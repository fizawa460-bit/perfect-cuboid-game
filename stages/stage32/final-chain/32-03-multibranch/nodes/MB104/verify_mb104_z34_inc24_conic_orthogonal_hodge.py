#!/usr/bin/env python3
from fractions import Fraction

# Z34 symbolic checksum only.  This verifier does not reconstruct the archived
# incidence-24 geometry; the source-locked archived checkpoint supplies:
#   8 pairwise-disjoint smooth conics Q_j,
#   H^2=16, H.Q_j=2, Q_j^2=-4.

n=8
H2=Fraction(16,1)
HQ=Fraction(2,1)
Q2=Fraction(-4,1)

# H24 = H + 1/2 sum Q_j
assert HQ + Fraction(1,2)*Q2 == 0
H24_2 = H2 + n*HQ + Fraction(1,4)*n*Q2
assert H24_2 == 24

# Adjunction for a rational conic: -2 = Q^2 + K.Q, K=H.
assert Q2 + HQ == -2

print("PASS STAGE32_MB104_Z34_INC24_CONIC_ORTHOGONAL_HODGE_V1")
print("conics=8 gram=-4I8 H24_square=24")
print("population_bound=D2<=d2/24")
print("finite_degree_window=false credit=none")
