#!/usr/bin/env python3

# Deterministic checks for Stage14-s7-61.

def mod4_split_primes(limit=200):
    out=[]
    for n in range(3, limit+1, 2):
        if all(n%d for d in range(3, int(n**0.5)+1, 2)):
            if n % 4 == 1:
                out.append(n)
    return out

# Verify x^2 == -1 mod p has a solution exactly for sampled odd primes p == 1 mod 4.
for p in mod4_split_primes():
    assert any((x*x + 1) % p == 0 for x in range(1,p))

for p in (3,7,11,19,23,31,43,47,59,67,71,79):
    assert p % 4 == 3
    assert not any((x*x + 1) % p == 0 for x in range(1,p))

# Exact complementary-square reconstruction identities.
for D,A in ((5,2),(7,4),(9,2),(11,6)):
    X=D*D+A*A
    Y=D*D-A*A
    assert (X+Y)//2 == D*D
    assert (X-Y)//2 == A*A

print('Stage14-s7-61 residue support audit: PASS')
print('fresh thin residue support: false')
print('next: Stage14-s7-62')
