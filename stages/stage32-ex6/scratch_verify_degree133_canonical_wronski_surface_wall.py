#!/usr/bin/env python3
"""Scratch verifier for the degree-133 Beauville branch-root canonical/Wronski wall.

This checks only the exact numerical identities used by the accompanying scratch
note.  It grants no endpoint, MAIN, hostile-audit, or lower-O credit.
"""

from math import comb

n = 133
branch = 266
gY = 134

# Full canonical series of the genus-134 Beauville pullback.
generic_branch_seq = [0, 1] + list(range(2, 2 * n, 2))
assert len(generic_branch_seq) == gY
assert generic_branch_seq[-1] == 264

generic_branch_weight = sum(generic_branch_seq) - sum(range(gY))
assert generic_branch_weight == 8646

# At an inflection point of the complete g^(n-1)_n on the elliptic base,
# the base sequence 0,...,n-2,n pulls back to even orders, with the
# anti-invariant canonical section contributing order one.
inflected_branch_seq = [0, 1] + list(range(2, 2 * n - 3, 2)) + [2 * n]
assert len(inflected_branch_seq) == gY
inflected_branch_weight = sum(inflected_branch_seq) - sum(range(gY))
assert inflected_branch_weight == 8648
assert inflected_branch_weight - generic_branch_weight == 2

canonical_total_weight = gY**3 - gY
assert canonical_total_weight == 2_405_970
assert branch * generic_branch_weight == 2_299_836
assert canonical_total_weight - branch * generic_branch_weight == 106_134
assert 106_134 == 6 * n**2

# Wronski target for pencils V subset H0(A), deg A=n on an elliptic curve.
h0_A = n
h0_A2 = 2 * n
grassmann_dim = 2 * (h0_A - 2)
wronski_target_projective_dim = h0_A2 - 1
assert grassmann_dim == 262
assert wronski_target_projective_dim == 265
assert wronski_target_projective_dim - grassmann_dim == 3

# Surface half-branch intersection firewall: if 2L=sum E_i and the 48
# exceptional curves are disjoint (-2)-curves, then L.E_i=-1.  No effective
# exceptional-supported integer divisor D=sum a_i E_i can have this pairing,
# since D.E_i=-2a_i is even.
assert (-2) // 2 == -1
assert all((-2 * a) % 2 == 0 for a in range(10))

print("PASS: degree133 canonical/Wronski/surface-section scratch wall")
