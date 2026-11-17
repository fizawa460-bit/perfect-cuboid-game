"""Isomorphism classes of degree-4 covers P1 -> P1 branched over the 6 points of B, every local degree 1 or 2
(slack 0, E11 Lemma 1): cycle types 1111 / 211 / 22 with n_y = 0 / 1 / 2 transposition-equivalents, sum n_y = 6.
Counted as orbits of S4-conjugation on transitive tuples with product 1 (fixed ordering of B)."""
import itertools, json
from collections import Counter
S4 = list(itertools.permutations(range(4)))
def mul(p, q): return tuple(p[q[i]] for i in range(4))   # p after q
def inv(p):
    r = [0]*4
    for i, x in enumerate(p): r[x] = i
    return tuple(r)
def ctype(p):
    seen = set(); t = []
    for i in range(4):
        if i in seen: continue
        L = 0; j = i
        while j not in seen: seen.add(j); j = p[j]; L += 1
        t.append(L)
    return tuple(sorted(t, reverse=True))
CL = {0: [p for p in S4 if ctype(p) == (1, 1, 1, 1)], 1: [p for p in S4 if ctype(p) == (2, 1, 1)], 2: [p for p in S4 if ctype(p) == (2, 2)]}
def transitive(gens):
    orb = {0}; ch = True
    while ch:
        ch = False
        for g in gens:
            for x in list(orb):
                if g[x] not in orb: orb.add(g[x]); ch = True
    return len(orb) == 4
def classes(ns):
    tuples = []
    for tup in itertools.product(*[CL[n] for n in ns[:-1]]):
        prod = (0, 1, 2, 3)
        for g in tup: prod = mul(prod, g)
        last = inv(prod)
        if ctype(last) != ctype(CL[ns[-1]][0]): continue
        t = tup + (last,)
        if transitive(t): tuples.append(t)
    seen = set(); orbits = []
    for t in tuples:
        if t in seen: continue
        orb = {tuple(mul(mul(g, x), inv(g)) for x in t) for g in S4}
        seen |= orb; orbits.append(len(orb))
    return len(orbits), len(tuples), Counter(24 // o for o in orbits)
res = {}
tot = 0; totaut = Counter()
for ns in itertools.product(range(3), repeat=6):
    if sum(ns) != 6: continue
    n, nt, aut = classes(ns)
    if n: res["".join(map(str, ns))] = [n, nt, dict(aut)]; tot += n; totaut.update(aut)
print(json.dumps(res))
print("branch data with covers:", len(res), " total isomorphism classes:", tot, " by |Aut|:", dict(totaut))
