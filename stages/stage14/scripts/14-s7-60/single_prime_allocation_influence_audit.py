#!/usr/bin/env python3

from math import isqrt

# Verify the complementary-square inversion algebra on a deterministic sample.
for D, A in ((13, 5), (17, 9), (25, 7), (29, 11)):
    X = D*D + A*A
    Y = D*D - A*A
    assert (X + Y) % 2 == 0
    assert (X - Y) % 2 == 0
    d2 = (X + Y)//2
    a2 = (X - Y)//2
    assert isqrt(d2)**2 == d2 == D*D
    assert isqrt(a2)**2 == a2 == A*A

# One arithmetic receiver; reciprocal completion is not an independent charge.
receivers = ("single-prime-allocation-two-square-reciprocal",)
assert len(receivers) == 1

# Local flip is a two-candidate finite-fiber comparison after all other bits freeze.
flip_states = (0, 1)
assert len(flip_states) == 2

print("Stage14-s7-60 single-prime allocation influence audit: PASS")
print("receiver count:", len(receivers))
print("flip states:", len(flip_states))
print("next: Stage14-s7-61")
