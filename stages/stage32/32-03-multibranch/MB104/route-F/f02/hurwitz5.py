"""Isomorphism classes of degree-5 slack-0 covers P1 -> P1 branched over the 6 points of B (local degrees 1 or 2):
cycle types 1^5 / 2 1^3 / 2^2 1 (n_y = 0, 1, 2), sum n_y = 8. Orbits of S5-conjugation on transitive tuples with
product 1 (fixed ordering of B). Output: hurwitz5.json {datum: [classes, tuples, {|Aut|: count}]} as hurwitz4.json."""
import itertools, json
from collections import Counter
n = 5
Sn = list(itertools.permutations(range(n)))
def mul(p, q): return tuple(p[q[i]] for i in range(n))
def inv(p):
    r = [0] * n
    for i, x in enumerate(p): r[x] = i
    return tuple(r)
def ntr(p):
    seen = set(); t = []
    for i in range(n):
        if i in seen: continue
        L = 0; j = i
        while j not in seen: seen.add(j); j = p[j]; L += 1
        t.append(L)
    return sum(1 for L in t if L == 2) if max(t) <= 2 else None
CL = {k: [p for p in Sn if ntr(p) == k] for k in range(3)}
def transitive(g):
    orb = {0}; ch = True
    while ch:
        ch = False
        for s in g:
            for x in list(orb):
                if s[x] not in orb: orb.add(s[x]); ch = True
    return len(orb) == n
out = {}
for ns in itertools.product(range(3), repeat=6):
    if sum(ns) != 2 * n - 2: continue
    tuples = []
    for tup in itertools.product(*[CL[k] for k in ns[:-1]]):
        pr = tuple(range(n))
        for g in tup: pr = mul(pr, g)
        last = inv(pr)
        if ntr(last) == ns[-1] and transitive(tup + (last,)): tuples.append(tup + (last,))
    seen = set(); aut = Counter(); k = 0
    for t in tuples:
        if t in seen: continue
        orb = {tuple(mul(mul(s, g), inv(s)) for g in t) for s in Sn}
        seen |= orb; k += 1; aut[120 // len(orb)] += 1
    out["".join(map(str, ns))] = [k, len(tuples), {str(a): c for a, c in aut.items()}]
json.dump(out, open("hurwitz5.json", "w"), indent=0)
print("data", len(out), "classes", sum(v[0] for v in out.values()), "max per datum", max(v[0] for v in out.values()))
