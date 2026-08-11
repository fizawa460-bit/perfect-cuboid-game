#!/usr/bin/env python3
from math import isqrt

# Deterministic audit for Stage14-s7-54.
# Verify the Pythagorean pairwise reconstruction identities on a finite mesh.
checks = 0
for D in range(2, 100):
    for A in range(1, D):
        xp = D*D + A*A
        xm = D*D - A*A
        x0 = 2*D*A
        assert xp*xp == xm*xm + x0*x0

        # (+,-) recovers k projection.
        z = xp*xp - xm*xm
        r = isqrt(z)
        assert r*r == z and r == x0

        # (+,k) recovers minus projection.
        z = xp*xp - x0*x0
        r = isqrt(z)
        assert r*r == z and r == xm

        # (-,k) recovers plus projection.
        z = xm*xm + x0*x0
        r = isqrt(z)
        assert r*r == z and r == xp
        checks += 1

assert checks > 1000

print('Stage14-s7-54 pairwise projection equivalence audit: PASS')
print('Pythagorean packets checked:', checks)
print('pairwise branches at fixed power: 1')
print('next: Stage14-s7-55')
