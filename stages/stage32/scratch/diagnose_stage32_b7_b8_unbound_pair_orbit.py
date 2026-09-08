#!/usr/bin/env python3
"""Scratch exact replay for the unbound Cecotti B.7/B.8 -> retained G12 mod-2 pair orbit.

No authority or mathematical credit is promoted by this diagnostic.
"""

from collections import Counter

B7 = (
    (1,0,0,0),
    (1,0,1,0),
    (1,1,0,0),
    (0,1,1,1),
)
B8 = (
    (1,1,0,0),
    (1,0,0,0),
    (1,0,0,1),
    (0,1,1,1),
)
S = (
    (1,1,0,0),
    (0,1,0,0),
    (0,1,1,1),
    (0,0,0,1),
)
T = (
    (1,1,0,0),
    (1,0,0,0),
    (0,0,1,1),
    (0,0,1,0),
)
I = (
    (1,0,0,0),
    (0,1,0,0),
    (0,0,1,0),
    (0,0,0,1),
)
Z3 = (1,0,0,0)
LINES = {
    (0,0,1,0): "L1",
    (0,0,0,1): "L2",
    (0,0,1,1): "L3",
}

def matmul(a, b):
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(4)) & 1 for j in range(4))
        for i in range(4)
    )

def matvec(a, v):
    return tuple(sum(a[i][k] * v[k] for k in range(4)) & 1 for i in range(4))

def inv(a):
    aug = [list(a[i]) + [1 if i == j else 0 for j in range(4)] for i in range(4)]
    row = 0
    for col in range(4):
        pivot = next((r for r in range(row, 4) if aug[r][col]), None)
        if pivot is None:
            return None
        aug[row], aug[pivot] = aug[pivot], aug[row]
        for r in range(4):
            if r != row and aug[r][col]:
                aug[r] = [x ^ y for x, y in zip(aug[r], aug[row])]
        row += 1
    return tuple(tuple(aug[i][4:]) for i in range(4))

def group(gens):
    seen = {I}
    stack = [I]
    while stack:
        a = stack.pop()
        for g in gens:
            b = matmul(a, g)
            if b not in seen:
                seen.add(b)
                stack.append(b)
    return seen

def all_gl4():
    for bits in range(1 << 16):
        a = tuple(
            tuple((bits >> (4*i+j)) & 1 for j in range(4))
            for i in range(4)
        )
        ai = inv(a)
        if ai is not None:
            yield a, ai

G = group((S, T))
assert len(G) == 24

inner_pairs = set()
for g in G:
    gi = inv(g)
    inner_pairs.add((matmul(matmul(g, S), gi), matmul(matmul(g, T), gi)))
assert len(inner_pairs) == 24

pair_counts = Counter()
line_counts = Counter()
literal_count = 0
literal_lines = set()
gl_count = 0
admissible_count = 0

for p, pi in all_gl4():
    gl_count += 1
    s = matmul(matmul(p, B7), pi)
    t = matmul(matmul(p, B8), pi)
    if s not in G or t not in G:
        continue
    if group((s, t)) != G:
        continue
    admissible_count += 1
    pair_counts[(s, t)] += 1
    image = matvec(p, Z3)
    assert image in LINES
    line_counts[LINES[image]] += 1
    if s == S and t == T:
        literal_count += 1
        literal_lines.add(LINES[image])

assert gl_count == 20160
assert admissible_count == 48
assert len(pair_counts) == 24
assert set(pair_counts) == inner_pairs
assert set(pair_counts.values()) == {2}
assert line_counts == Counter({"L1": 16, "L2": 16, "L3": 16})
assert literal_count == 2
assert literal_lines == {"L3"}

print("PASS_STAGE32_SCRATCH_B7_B8_UNBOUND_PAIR_ORBIT")
print("GL4(F2)=20160")
print("retained_group_order=24")
print("admissible_intertwiners=48")
print("distinct_ordered_pairs=24")
print("pair_orbit=inner_conjugacy_orbit(S,T)")
print("pair_multiplicity=2")
print("delta_0inf_line_counts=L1:16,L2:16,L3:16")
print("literal_pair_intertwiners=2")
print("literal_pair_delta_0inf=L3")
