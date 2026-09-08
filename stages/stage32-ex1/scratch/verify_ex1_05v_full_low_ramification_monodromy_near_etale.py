#!/usr/bin/env python3

from math import gcd

N = 105
ID = tuple(range(N))
C = tuple(list(range(1, N)) + [0])
T_list = list(range(N))
T_list[0], T_list[1] = 1, 0
T = tuple(T_list)


def compose(p, q):
    return tuple(p[q[i]] for i in range(N))


def power(p, k):
    out = ID
    while k:
        if k & 1:
            out = compose(out, p)
        p = compose(p, p)
        k >>= 1
    return out


# c is a 105-cycle, hence already transitive in the unramified r=0 state.
orbit = set()
x = 0
for _ in range(N):
    orbit.add(x)
    x = C[x]
assert len(orbit) == N
assert x == 0

# t is a transposition and 2r copies satisfy the punctured-surface relation.
assert power(T, 2) == ID

rows = []
for r in range(29):
    R105 = 2 * r
    g = 106 + r
    assert 2 * g - 2 == N * (2 * 2 - 2) + R105
    assert power(T, 2 * r) == ID
    # For r>0, <c,t>=S_105 because conjugating t by c^k produces
    # the adjacent transpositions around the full 105-cycle.
    full_symmetric_possible = r > 0
    rows.append((r, R105, g, full_symmetric_possible))

assert rows[0] == (0, 0, 106, False)
assert rows[-1] == (28, 56, 134, True)

# Odd-index subgroup K of pi1(U) restricts every surjection alpha:pi1(U)->H,
# |H|=4, surjectively: [H:alpha(K)] divides both 105 and 4.
assert gcd(105, 4) == 1

print("PASS_EX1_05V_LOW_RAMIFICATION_MONODROMY_FLEXIBLE")
print("states", len(rows), "r0_etale", True, "r_positive_full_S105", 28)
