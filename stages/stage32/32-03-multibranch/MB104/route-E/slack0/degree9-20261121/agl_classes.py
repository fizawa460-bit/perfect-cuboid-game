import itertools, numpy as np, collections
pts = [(a, b) for a in range(3) for b in range(3)]; idx = {p: i for i, p in enumerate(pts)}
G = []
for A in itertools.product(range(3), repeat=4):
    if (A[0]*A[3] - A[1]*A[2]) % 3 == 0: continue
    for b in pts:
        perm = tuple(idx[((A[0]*x + A[1]*y + b[0]) % 3, (A[2]*x + A[3]*y + b[1]) % 3)] for x, y in pts)
        G.append(perm)
G = sorted(set(G)); print('|AGL(2,3)|', len(G))
def ntr(p): return sum(1 for i in range(9) if p[i] > i) if all(p[p[i]] == i for i in range(9)) else -1
by = collections.defaultdict(list)
for g in G: by[ntr(g)].append(g)
print({k: len(v) for k, v in by.items() if k >= 0})
def mul(p, q): return tuple(q[p[i]] for i in range(9))   # p then q
def inv(p):
    r = [0]*9
    for i, x in enumerate(p): r[x] = i
    return tuple(r)
def transitive(gens):
    seen = {0}; st = [0]
    while st:
        x = st.pop()
        for g in gens:
            if g[x] not in seen: seen.add(g[x]); st.append(g[x])
    return len(seen) == 9

import sys, pickle
sys.path.insert(0, '/home/user/perfect-cuboid-game/stages/stage32/32-03-multibranch/MB104/route-E/slack0/speedup-20261118')
import monodromy as md
ORDER = (0, 2, 5, 1, 3, 4)      # mono_dir's tuples: g0 g2 g5 g1 g3 g4 = 1 (left to right, p then q)
out = {}
for prof in [(0,3,3,3,3,4), (0,0,4,4,4,4)]:
    C = {}
    S_last = set(by[prof[ORDER[-1]]])
    for g in itertools.product(*[by[prof[y]] for y in ORDER[:-1]]):
        p = g[0]
        for h in g[1:]: p = mul(p, h)
        last = inv(p)
        if last not in S_last: continue
        t = [None] * 6
        for y, e in zip(ORDER, list(g) + [last]): t[y] = e
        if not transitive(t): continue
        c, au = md.canon(tuple(t))
        if c is not None: C[c] = au
    out[prof] = C
    print(prof, 'classes', len(C), 'weighted', sum(1 / a for a in C.values()))
pickle.dump(out, open('/mnt/project-files/deg9gen/agl_classes.pkl', 'wb'))
